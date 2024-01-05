from nltk.tokenize import word_tokenize

# 输入文本
text = "Q:Olivia has $23. She bought ﬁve bagels for $3 each. How much money does she have left? +\
        A:Shebought 5bagels for$3each. This means shespent 5*$3=$15onthebagels. Shehad$23inbeginning,"

# 使用NLTK的分词器来将文本分割成tokens
tokens = word_tokenize(text)

# 计算tokens长度
tokens_length = len(tokens)
print("tokens length:", tokens_length)
