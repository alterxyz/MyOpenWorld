import os
from PIL import Image

# pip install pillow


def resize_image(img_path, output_folder, ratio=2):
    """Resizes an image to half its original size and saves it to a subfolder.

    Args:
      img_path: Path to the image file.
      output_folder: Folder to save the resized image.
    """

    try:
        img = Image.open(img_path)

        # Get original dimensions
        original_width, original_height = img.size

        # Calculate new dimensions (half the original size)
        new_width = original_width // ratio
        new_height = original_height // ratio

        # Resize the image using antialiasing
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Create "half" subfolder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Save the resized image with the same filename in the "half" subfolder
        resized_img_path = os.path.join(output_folder, os.path.basename(img_path))
        resized_img.save(resized_img_path)

        print(f"Resized image saved to: {resized_img_path}")

    except Exception as e:
        print(f"Error processing image {img_path}: {e}")


if __name__ == "__main__":
    # 获取当前 Python 文件所在的目录
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 指定包含图像的文件夹（与 Python 文件相同的目录）
    image_folder = script_dir

    # 指定用于调整大小后的图像的子文件夹
    output_folder = os.path.join(image_folder, "half")

    # 循环遍历文件夹中的所有文件
    for filename in os.listdir(image_folder):
        print(
            f"Type you ratio: \n Enter 2 for half size, 4 for quarter size, 8 for eighth size, etc.\nEnter empty for half size(default)"
        )
        # Ask user input ratio, default is 2, have to be integer and greater or equal to 2
        ratio = input()
        if ratio == "":
            ratio = 2
        else:
            try:
                ratio = int(ratio)
                if ratio < 2:
                    print("Ratio must be greater or equal to 2")
                    continue
            except ValueError:
                print("Please enter an integer value")
                continue

        if filename.endswith(".jpg"):
            img_path = os.path.join(image_folder, filename)
            resize_image(img_path, output_folder)
