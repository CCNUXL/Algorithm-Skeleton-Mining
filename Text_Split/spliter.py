import os
import argparse
# from langchain.document_loaders import PyPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from nltk.tokenize import word_tokenize


# 获取当前文件的路径
current_file_path = os.path.abspath(__file__)

# 获取当前文件所在目录的上级目录路径
parent_directory = os.path.dirname(current_file_path)
parent_parent_directory = os.path.dirname(parent_directory)

parser = argparse.ArgumentParser(description='Process some documents.')
parser.add_argument('pdf_path', type=str, help='The path to the PDF file')

args = parser.parse_args()

# 拼接文件路径
pdf_path = os.path.join(parent_parent_directory, args.pdf_path)

print(pdf_path)

# loader = PyPDFLoader(pdf_path)
# pages = loader.load_and_split()
# print(f"加载完毕，共加载{len(pages)}页PDF文件")

# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=2000,
#     chunk_overlap=10,
#     length_function=len
# )

# texts = text_splitter.split_documents(pages)
# print(f"文章共切分为{len(texts)}段")

# for i in range(0, len(texts)):
#     print(f"段{i}")
#     print(texts[i].page_content)
#     tokens = word_tokenize(texts[i].page_content)
#     tokens_length = len(tokens)
#     print("tokens length:", tokens_length)


