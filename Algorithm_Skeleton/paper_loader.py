import os
import PyPDF2
import json



def batch_process_pdfs(folder_path, output_json):
    # 获取文件夹中所有PDF文件的路径
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    # 存储处理结果的列表
    results = []

    # 遍历每个PDF文件并处理
    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        print(f"Processing PDF: {pdf_path}")

        # 获取文件名（不包括扩展名）
        file_name = os.path.splitext(pdf_file)[0]




