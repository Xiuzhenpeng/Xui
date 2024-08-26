import json
import os
import random

# 输入 gradio 的 style name 输出 json 格式
def load_json_data(name):
    json_name = f"{name}.json"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, '..', 'workflow_api', json_name)

    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


class FileProcessor:
    def __init__(self, json_content: dict):
        self.data = json_content

    def __str__(self):
        return str(self.data)
    
    def change_seed(self, id, seed):
        if seed == -1:
            seed = random.randint(1, 2 ** 32 - 1)
        self.data[f"{id}"]["inputs"]["seed"] = seed

    def change_width(self, id, width):
        self.data[f"{id}"]["inputs"]["width"] = width

    def change_height(self, id, height):
        self.data[f"{id}"]["inputs"]["height"] = height

    def change_prompt(self, id, prompt):
        self.data[f"{id}"]["inputs"]["text"] = prompt

# style_name, random_seed, seed_number, image_aspect_ratio, user_prompt

# “无” 风格
def change_无(seed, width, height, prompt):
    json_data = load_json_data("无")
    json_file = FileProcessor(json_data)
    json_file.change_seed(3, seed)
    json_file.change_width(5, width)
    json_file.change_height(5, height)
    json_file.change_prompt(6, prompt)
    return json_file


if __name__ == "__main__":
    # print(change_无(1, 12, 123, "1234"))
    json_name = f"无.json"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, '..', 'workflow_api', json_name)

    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(data)