from cloudinary import uploader, config
from fastapi import UploadFile, HTTPException, status
from secrets import token_hex
from PIL import Image

from app.core.conf import settings

ALLOWED_TYPES = ["image/jpeg", "image/png", "image/webp", "image/avif"]

config(
    cloud_name=settings.cloud_name,
    api_key=settings.api_key,
    api_secret=settings.api_secret,
)


def save_img_files(file: UploadFile, location: str, size: int) -> str:

    if not file.content_type or file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unsupported file type"
        )

    try:
        image = Image.open(file.file)
        image.verify()

        file.file.seek(0)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid image file"
        )

    file.file.seek(0, 2)
    file_size = file.file.tell()
    file.file.seek(0)

    if file_size > size:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Image too large (max 5MB)"
        )

    public_id = f"{location}/{token_hex(4)}"

    result = uploader.upload(file.file, public_id=public_id, format="webp")

    return result["secure_url"]


def delete_image(image_url: str):
    try:
        parts = image_url.split("/")
        public_id_with_ext = "/".join(parts[-2:])
        public_id = public_id_with_ext.rsplit(".", 1)[0]
        uploader.destroy(public_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to delete image"
        )
