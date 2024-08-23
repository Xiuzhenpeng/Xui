import json
import os
import random

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, '..', 'workflow_api', 'workflow_api.json')

def change_json_file(data):
    
    seed = random.randint(1, 2 ** 32 - 1)
    data["3"]["inputs"]["seed"] = seed

    return data