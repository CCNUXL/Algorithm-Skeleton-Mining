# from paper_splitter import splitter
from transformers import AutoTokenizer, AutoModel
from IPython.display import display, Markdown, clear_output


def load_prompt(prompt_file):
    with open(prompt_file, "r", newline='', encoding='utf-8') as file:
        prompt = file.read()
    return prompt


def llm_response(prompt):
    # 加载模型
    model_path = "Model\chatglm-6b-int4"
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    # 按需修改，目前只支持 4/8 bit 量化
    model = AutoModel.from_pretrained(model_path, trust_remote_code=True).quantize(4).half().cuda()
    model = model.eval()
    # # 使用 IPython.display 流式打印模型输出
    # for response, history in model.stream_chat(
    #         tokenizer, prompt, history=[]):
    #     clear_output(wait=True)
    #     display(Markdown(response))
    response, history = model.chat(tokenizer, prompt, history=[])
    return response


def structured_mining(texts):
    # 六个层次的结构化挖掘
    # Background Aspect Scope Approach Model Dataset
    structure_info = {
        "Background": "",
        "Aspect": "",
        "Scope": "",
        "Approach": "",
        "Model": "",
        "Dataset": ""
    }
    background = ""
    for i in range(0, len(texts)):
        # 动态存储六个维度的信息
        dynamic_res_list = []  # 动态存储每个片段的结果（容量大小为10）
        res_list = []  # 每10个片段的结果总结后存入每个单元（容量大小为chunk_num/10)
        dynamic_num = 0  # 动态存储块中的片段数量
        # prompt模版
        prompt = load_prompt("项目代码/Algorithm_Skeleton/Hierarchical_Prompt_list/Background.txt")
        res = llm_response(prompt)
        dynamic_res_list.append(res)
        dynamic_num += 1
        if dynamic_num == 10:
            prompt = load_prompt("项目代码/Algorithm_Skeleton/Prompt_list/combine_res.txt")
            res = llm_response(prompt)
            res_list.append(res)
            dynamic_num = 0
            dynamic_res_list = []
        if i == len(texts) - 1:
            prompt = load_prompt("项目代码/Algorithm_Skeleton/Prompt_list/combine_res.txt")
            res = llm_response(prompt)
            background = res

    print(background)


if __name__ == "__main__":
    llm_response("宫保鸡丁怎么做?")
