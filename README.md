# Algorithm-Skeleton-Mining
Tracing The Evolution of Algorithm Skeleton in Paper Collections

追踪论文集合中的算法框架的变化

## 1 Algorithm Skeleton Extraction of Papers
### 1.1 Deploy the ChatGLM-6B-int4 model locally
### 硬件需求

| **量化等级**   | **最低 GPU 显存**（推理） | **最低 GPU 显存**（高效参数微调） |
| -------------- | ------------------------- | --------------------------------- |
| INT4           | 6 GB                      | 7 GB                              |
### 1.2 Definition of algorithm skeleton
#### 1.2.1 Six-dimensional algorithm skeleton
![](resources/as.png)

针对六个维度的算法特征信息, 我们设计了六种情况的Prompt来引导LLM提取特征

| **维度特征**   | **提示模版**  |
| -------------- | ------------------------- |
| Background     | The writing background of the algorithm in the paper (note that only the original information in the article can be extracted, not generated)                                                                                                             |
| Scope          | Applicable field scenarios of the algorithm in the paper (note that only the original information in the article can be extracted, not generated)                                                                                                          |
| Approach       | Please keep the number of words within 200 to describe the specific implementation method proposed by the algorithm in the paper (note that only the original information in the article can be extracted, not generated)                                 |
| Model          | Please control the number of words within 200 for the mathematical model or artificial intelligence description used in the algorithm of the paper (note that only the original information in the article can be extracted, not generated)                                                                                                                            |
| Dataset        | Please keep the word count within 200 for the description of the datasets used in the algorithm verification of the paper (note that only the original information in the article can be extracted, not generated)                                        |
| Result         | For a description of the results and significance of the paper's algorithm, please limit the number of words to less than 200 (note that only the original information in the article can be extracted, not generated)                                                                                                                            |

同时，采用分段总结形式，将最终输出结果长度限定在可控范围

| **提示模版**  |
|------------- |
|Please provide a concise summary of the above multiple paragraphs of text, with the number of words within 200.|

#### 1.2.2 Text segmentation
我们采用Langchain来对一整篇科技文章进行切分，切分的执行过程可以运行下述代码：
``` python
    python spliter.py
```

### 1.3 Construction of Algorithm Skeleton Dataset of Survey paper Citations

## 2 Algorithmic Relation Network
### 2.1 Domain Clustering
#### 2.1.1 Word2Vec

#### 2.1.2 tf-idf

#### 2.1.3 K-means Clustering

### 2.2 Evolution Relation Mining
#### 2.2.1 sentence-BERT

#### 2.2.2 cosine similarity

### 2.3 Visualization

