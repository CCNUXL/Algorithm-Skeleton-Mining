from paper_splitter import Splitter


def load_prompt(prompt_file):
    with open(prompt_file, "r", newline='', encoding='utf-8') as file:
        prompt = file.read()
    return prompt


def llm_response(prompt):
    response = prompt + '\n' + "OK"
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
