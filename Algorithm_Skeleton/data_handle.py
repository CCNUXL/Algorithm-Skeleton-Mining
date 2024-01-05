import csv
from paper_splitter import splitter
from transformers import AutoTokenizer, AutoModel
from nltk.tokenize import word_tokenize


# from IPython.display import display, Markdown, clear_output


def load_prompt(prompt_file):
    with open(prompt_file, "r", newline='', encoding='utf-8') as file:
        prompt = file.read()
    return prompt


def llm_initialize():
    model_path = "model\chatglm-6b-int4"
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    # 按需修改，目前只支持 4/8 bit 量化
    model = AutoModel.from_pretrained(model_path, trust_remote_code=True).quantize(4).half().cuda()
    model = model.eval()

    return model, tokenizer


def llm_response(prompt, model, tokenizer):
    # 加载模型
    # # 使用 IPython.display 流式打印模型输出
    # for response, history in model.stream_chat(
    #         tokenizer, prompt, history=[]):
    #     clear_output(wait=True)
    #     display(Markdown(response))
    response, history = model.chat(tokenizer, prompt, history=[])
    return response


# def dynamic_tokens(text):
#     tokens = word_tokenize(text)
#     return tokens


def structure_mining(texts):
    # 六个层次的结构化挖掘
    # Background Aspect Scope Approach Model Dataset
    background = ""
    background_prompt = load_prompt("Prompt_list/background_res.txt")
    background = llm_response(background_prompt + "\n" + texts, model, tokenizer)
    return background


if __name__ == "__main__":
    background = ""
    # 初始化模型
    model, tokenizer = llm_initialize()
    # 对论文进行切分
    pdf_path = "Algorithm_Skeleton/pdf_files/Distilling Model/2212.00193.pdf"
    split_result = splitter(pdf_path)

    token_lengths = 0
    for i in range(0, len(split_result)):
        result = structure_mining(split_result[i].page_content)
        background += result
        # print(background)

    # 存储背景
    text_to_store = background
    # CSV文件名
    csv_filename = "result/background.csv"
    # 打开CSV文件并写入字符串数据
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        # 写入单行数据，这里将字符串作为单元素列表写入
        csv_writer.writerow([text_to_store])

    print(f"已将字符串存储到 '{csv_filename}' 文件中.")
