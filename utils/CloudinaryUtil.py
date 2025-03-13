import cloudinary
from cloudinary.uploader import upload

#cloundinary configuration
cloudinary.config(
    cloud_name = "dgtxgxufe",
    api_key="434514998299256",
    api_secret="434514998299256"
)

#util functionn...



async def upload_image(image):
    result = upload(image)
    print("cloundianry response,",result)
    return result["secure_url"] #string
    