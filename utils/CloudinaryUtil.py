import cloudinary
from cloudinary.uploader import upload
import os

#cloundinary configuration
cloudinary.config(
    cloud_name = "dgtxgxufe",
    api_key="434514998299256",
    api_secret="sQSZaxl-3dAMd5C-2NfKwYoUFNI"
)

#util functionn...

# async def upload_image(image):
#     result = upload(image)
#     print("cloundianry response,",result)
#     return result["secure_url"] #string
    
async def upload_image(file_path: str):
    try:
        upload_result = cloudinary.uploader.upload(file_path)
        os.remove(file_path)  # Remove local file after uploading
        return upload_result["secure_url"]
    except Exception as e:
        print(f"Cloudinary Upload Error: {str(e)}")
        return None