import pickle
from train import Word2Vec  # 假设Word2Vec类定义在train.py文件中

# 加载模型参数
with open('Model/word2vec_model.pkl', 'rb') as f:
    W1, W2, word_to_index = pickle.load(f)

# 创建一个新的Word2Vec对象，并设置其参数
w2v = Word2Vec("cat", window_size=2, n_hidden=5, n_epochs=100, learning_rate=0.1)
w2v.W1 = W1
w2v.W2 = W2
w2v.word_to_index = word_to_index