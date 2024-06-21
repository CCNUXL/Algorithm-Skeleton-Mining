import numpy as np
import pickle


class Word2Vec:
    def __init__(self, corpus, window_size, n_hidden, n_epochs, learning_rate):
        self.corpus = corpus
        self.window_size = window_size
        self.n_hidden = n_hidden
        self.n_epochs = n_epochs
        self.learning_rate = learning_rate
        self.build_vocab()
        self.vocabulary = set(corpus)
        self.word_to_index = {word: i for i, word in enumerate(self.vocabulary)}

    def build_vocab(self):
        self.words = list(set(self.corpus))
        self.word2idx = {word: idx for idx, word in enumerate(self.words)}
        self.idx2word = {idx: word for idx, word in enumerate(self.words)}

    def train(self):
        # 初始化权重
        self.W1 = np.random.rand(len(self.words), self.n_hidden)
        self.W2 = np.random.rand(self.n_hidden, len(self.words))

        for epoch in range(self.n_epochs):
            loss = 0
            for word_idx, word in enumerate(self.corpus):
                # 获取输入词的one-hot向量
                X = np.zeros(len(self.words))
                X[self.word2idx[word]] = 1

                # 前向传播
                H = np.dot(self.W1.T, X)
                U = np.dot(self.W2.T, H)
                y_pred = self.softmax(U)

                # 计算误差
                context_words = [self.word2idx[word] for word in self.corpus[max(0, word_idx-self.window_size):min(len(self.corpus), word_idx+self.window_size+1)] if word != self.corpus[word_idx]]
                EI = np.sum([np.subtract(y_pred, np.eye(len(self.words))[word]) for word in context_words], axis=0)

                # 反向传播
                dW1 = np.outer(X, np.dot(self.W2, EI))
                self.W1 = self.W1 - self.learning_rate * dW1[:self.W1.shape[0], :self.W1.shape[1]]

                dW2 = np.outer(H, EI)
                self.W2 = self.W2 - self.learning_rate * dW2[:self.W2.shape[0], :self.W2.shape[1]]

                # 计算损失
                loss += -np.sum([U[word] for word in context_words]) + len(context_words) * np.log(np.sum(np.exp(U)))

                print(f'Epoch: {epoch}, Loss: {loss}')

    def softmax(self, x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=0)
    
    def get_vector(self, word):
        word_index = self.word_to_index[word]
        return self.W1[word_index]

corpus = ["cat", "say", "meow", "dog", "say", "woof"]
w2v = Word2Vec(corpus, window_size=2, n_hidden=5, n_epochs=100, learning_rate=0.1)
w2v.train()


# 保存模型参数
with open('Model/word2vec_model.pkl', 'wb') as f:
    pickle.dump((w2v.W1, w2v.W2, w2v.word_to_index), f)


