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
import base64
from PIL import Image
from io import BytesIO
import requests
from modules.html import make_progress_html
import gradio as gr

# def update_progress(progress, text="Progressing"):
#     # 将浮点数转换为百分比
#     percent = int(progress * 100)
    
#     # 创建 HTML 进度条的代码，并添加文字描述
#     progress_html = f"""
#     <div style="font-size: 15px; padding-bottom: 3px;">
#         {text}
#     </div>
#     <div style="width: 100%; background-color: #ddd;">
#         <div style="width: {percent}%; padding: 3px; height: 10px; background-color: #4CAF50; text-align: right; color: white;">
#             {percent}%
#         </div>
#     </div>
#     """
#     return progress_html

def get_new_session(url):
    data = json.dumps({}).encode('utf-8')
    req = urllib.request.Request(f"http://{url}/API/GetNewSession", data=data)
    req.add_header("Content-Type", "application/json")
    response = urllib.request.urlopen(req).read()
    return json.loads(response)

# def get_image(ws, url, prompt_data):
#     session_id = get_new_session(url)["session_id"]

#     ws.connect(f"ws://{url}/API/GenerateText2ImageWS")

#     # yield None, update_progress(0, "Loading Model")
#     prompt_data["session_id"] = session_id
    
#     ws.send(json.dumps(prompt_data))

#     # 接收数据
#     while True:
#         try:
#             out = ws.recv()
#             # print(out)            
#             if isinstance(out, str):
#                 message = json.loads(out)
#                 if 'gen_progress' in message:
#                     data = message["gen_progress"]
#                     if 'preview' in data:
#                         image_base64 = data["preview"].split(",")[-1]
#                         image_data = base64.b64decode(image_base64)
#                         image = Image.open(BytesIO(image_data))
#                         # progress_html = update_progress(data["current_percent"])
#                         # image.show()
#                         yield image
#                 if "image" in message:
#                     image_name = message["image"]
#                     image_url = f"http://{url}/{image_name}"
#                     response = requests.get(image_url)
#                     image = Image.open(BytesIO(response.content))
#                     # image.show()
#                     # progress_html = gr.update(visible=False)
#                     yield image
#                 if "discard_indices" in message:
#                     ws.close()
#                     break
#         except websocket.WebSocketConnectionClosedException:
#             break

def get_image(ws, url, prompt_data):
    session_id = get_new_session(url)["session_id"]
    
    ws.connect(f"ws://{url}/API/GenerateText2ImageWS")
    # 添加 session_id 到 prompt_data
    prompt_data["session_id"] = session_id
    
    ws.send(json.dumps(prompt_data))
    # ws.send(prompt_data)

    # 初始化图像计数器
    image_counter = 0

    # 接收数据
    while True:
        try:
            out = ws.recv()
            if isinstance(out, str):
                try:
                    message = json.loads(out)
                    if 'gen_progress' in message:
                        data = message["gen_progress"]
                        if 'current_percent' in data:                            
                            current_percent = data['current_percent']                             
                            if 0 < current_percent <= 1:                                 
                                progress_html = make_progress_html(current_percent * 100, "Processing")
                        if 'preview' in data:
                            image_base64 = data["preview"].split(",")[-1]
                            image_data = base64.b64decode(image_base64)
                            image = Image.open(BytesIO(image_data))
                            # 计数图像
                            image_counter += 1
                            # 第一个图像不传递给 Gradio，直接 yield None
                            if image_counter <= 2:
                                yield None,None
                            else:
                                # 从第二个图像开始传递给 Gradio
                                yield image,progress_html

                    if "image" in message:
                        image_name = message["image"]
                        image_url = f"http://{url}/{image_name}"
                        response = requests.get(image_url)
                        image = Image.open(BytesIO(response.content))
                        image_counter += 1
                        if image_counter <= 2:
                            yield None,None
                        else:
                            yield image,progress_html
                    if "discard_indices" in message:
                        ws.close()
                except:
                    ws.close()
        except websocket.WebSocketConnectionClosedException:
            break

if __name__ == "__main__":
    url = "localhost:7802"
