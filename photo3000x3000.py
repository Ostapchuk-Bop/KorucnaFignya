from PIL import Image
import os

# Define input and output file paths
input_files = [
    r"C:\Users\Igor Nimec\Desktop\Enchanted_Sword_(item).webp",
    r"C:\Users\Igor Nimec\Desktop\Star_Wrath.webp",
    r"C:\Users\Igor Nimec\Desktop\Seedler.webp"
]

# Set target size
target_size = (3000, 3000)

# Resize and save images
output_paths = []
for file_path in input_files:
    img = Image.open(file_path)
    img_resized = img.resize(target_size, Image.NEAREST)  # NEAREST to preserve pixel style
    output_file_path = file_path.replace(".webp", "_resized.webp")
    img_resized.save(output_file_path)
    output_paths.append(output_file_path)

output_paths
