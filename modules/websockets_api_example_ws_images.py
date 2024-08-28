#This is an example that uses the websockets api and the SaveImageWebsocket node to get images directly without
#them being saved to disk

import websocket #NOTE: websocket-client (https://github.com/websocket-client/websocket-client)
import os
import sys
import uuid
import json
import random
import urllib.request
import urllib.parse
import time

import gradio as gr

# from change_json import load_json_data

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

client_id = str(uuid.uuid4())

def queue_prompt(prompt, server_address):
    p = {"prompt": prompt, "client_id": client_id}
    data = json.dumps(p).encode('utf-8')
    req =  urllib.request.Request("http://{}/prompt".format(server_address), data=data)
    return json.loads(urllib.request.urlopen(req).read())

def get_image(filename, subfolder, folder_type):
    data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
    url_values = urllib.parse.urlencode(data)
    with urllib.request.urlopen("http://{}/view?{}".format(server_address, url_values)) as response:
        return response.read()

def get_history(prompt_id):
    with urllib.request.urlopen("http://{}/history/{}".format(server_address, prompt_id)) as response:
        return json.loads(response.read())

def get_images(ws, prompt, url, progress=gr.Progress()):
    prompt_id = queue_prompt(prompt, url)['prompt_id']
    output_images = {}
    current_node = ""
    while True:
        out = ws.recv()
        if isinstance(out, str):
            message = json.loads(out)
            if message['type'] == 'status':
                progress(random.randint(1,3) / 100, desc="Loading Model...")
            if message['type'] == 'progress':
                data = message['data']
                if data["value"] >= 2:
                    progress(message["data"]["value"] / message["data"]["max"], desc="Progressing",)
                    progress(data["value"] / data["max"], desc="Progressing",)            
            if message['type'] == 'executing':
                data = message['data']
                if data['prompt_id'] == prompt_id:
                    if data['node'] is None:
                        progress(1, desc="Finished",)
                        break #Execution is done
                    else:
                        current_node = data['node']
        else:
            if current_node == 'save_image_websocket_node':
                images_output = output_images.get(current_node, [])
                images_output.append(out[8:])
                output_images[current_node] = images_output

    return output_images

def inference_image(data, url, progress=gr.Progress()):
    prompt = data

    ws = websocket.WebSocket()
    ws.connect("ws://{}/ws?clientId={}".format(url, client_id))

    images = get_images(ws, prompt, url, gr.Progress())

    for node_id in images:
        for image_data in images[node_id]:
            from PIL import Image
            import io
            image = Image.open(io.BytesIO(image_data))

    time.sleep(0.2)

    return image


if __name__ == "__main__":
    server_address = "127.0.0.1:8188"

    from change_json import change_file
    data = change_file.change_无(1, 1024, 1024, "a car running on city")

    image = get_history("'4b33a209-d24c-4bcb-92dd-3c4e11a68e1a")
    print(image)

    # image.show()
# else:
#     from modules.change_json import change_json_file
