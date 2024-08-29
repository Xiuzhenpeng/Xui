import requests
from PIL import Image
import uuid
import os
import socket

def upload_image(image, url, subfolder="controlnet_api"):

    # 获取主机名
    hostname = socket.gethostname()
    url = f"http://{url}/upload/image"

    # 获取主机的 IP 地址
    ip_address = socket.gethostbyname(hostname)

    # Generate a unique identifier for the image name
    unique_id = str(uuid.uuid4())
    image_name = f"{unique_id}.png"

    # Save the image to the specified path with the unique name
    if image is None:
         return None

    image_path = os.path.join(os.getcwd(), image_name)
    image.save(image_path, format='PNG')

    # Prepare the data and files for the request
    data = {"subfolder": subfolder}

    # Open the file and make the POST request to upload the image
    with open(image_path, 'rb') as img_file:
        files = {'image': (image_name, img_file)}
        resp = requests.post(url, files=files, data=data)

    # Check if the upload was successful
    if resp.status_code == 200:
        # If upload successful, delete the local image file
        os.remove(image_path)
    else:
        print(f"Upload failed with status code: {resp.status_code}")

    image_dir = f"./{subfolder}/{image_name}"

    # Return the image name
    return image_dir


# Example usage
if __name__ == "__main__":
    # Create a sample image using PIL (for demonstration purposes)
    img = Image.new('RGB', (100, 100), color='blue')

    # Define the upload URL
    upload_url = "127.0.0.1:8160"

    # Call the function and get the image name
    image_name = upload_image(img, upload_url)
    print(f"Uploaded image name: {image_name}")
