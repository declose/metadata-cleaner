from PIL import Image

input_file = "input.jpg"
output_file = "cleaned.jpg"

image = Image.open(input_file)

cleaned_image = Image.new(image.mode, image.size)
cleaned_image.putdata(image.get_flattened_data())

cleaned_image.save(output_file)

print("Done! Metadata is deleted.")
print(f"New File: {output_file}")