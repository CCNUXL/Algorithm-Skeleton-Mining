from sentence_transformers import SentenceTransformer, util
 
model = SentenceTransformer('E:/Python/ASM/all-MiniLM-L6-v2')
 
# 文本列表
# sentences = ['The cat sits outside',
#              'A man is playing guitar',
#              'I love pasta',
#              'The new movie is awesome',
#              'The cat plays in the garden']

sentences = ['The proposed BERT model achieved 90% results on the benchmark MRC challenge datasets, SQuAD2.0 and NewsQA.',
             'The proposed Retro-Reader model achieved 90% results on the benchmark MRC challenge datasets, SQuAD2.0 and NewsQA.']
 
# 计算embeddings
embeddings = model.encode(sentences, convert_to_tensor=True)
 
# 计算不同文本之间的相似度
cosine_scores = util.cos_sim(embeddings, embeddings)
 
# 保存结果
pairs = []
for i in range(len(cosine_scores)-1):
    for j in range(i+1, len(cosine_scores)):
        pairs.append({'index': [i, j], 'score': cosine_scores[i][j]})
 
# 按照相似度分数进行排序打印
pairs = sorted(pairs, key=lambda x: x['score'], reverse=True)
 
for pair in pairs:
    i, j = pair['index']
    print("{:<30} \t\t {:<30} \t\t Score: {:.4f}".format(sentences[i], sentences[j], pair['score']))