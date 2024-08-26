import json
import os
import random

def json_path(name=str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, '..', 'workflow_api', name)
    return json_path


class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self._read_json()

    def _read_json(self) -> dict:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"文件 {self.file_path} 不存在。")
            return {}
        except json.JSONDecodeError:
            print(f"文件 {self.file_path} 不是有效的 JSON 格式。")
            return {}
        
    def __str__(self):
        # 实现字符串表示方法
        return str(self.data)
    
    def change_seed(self, id, seed):
        if seed == -1:
            seed = random.randint(1, 2 ** 32 - 1)
            self.data[f"{id}"]["inputs"]["seed"] = seed
        else:
            self.data[f"{id}"]["inputs"]["seed"] = seed

    # change width and hight
    def change_width(self, id, width,):
        self.data[f"{id}"]["inputs"]["width"] = width
        

    def change_hight(self, id, height,):
        self.data[f"{id}"]["inputs"]["height"] = height
        

    # change prompt or negative prompt
    def change_prompt(self, id, str):
        self.data[f"{id}"]["inputs"]["text"] = str

# “无” 风格
def change_无(seed, width, hight, prompt=str):
    json_name = "无.json"
    json_file = FileProcessor(json_path(json_name))
    json_file.change_seed(3, seed)
    json_file.change_width(5, width)
    json_file.change_hight(5, hight)
    json_file.change_prompt(6, prompt)
    return json_file


if __name__ == "__main__":
    print(change_无(-1, 1920, 1080, "a beautiful girl"))
