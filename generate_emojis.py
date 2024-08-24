from PIL import Image, ImageDraw, ImageFont

img_size = 128
colors = [('#00BFFF', "blue"), ('#FFD700', "gold")]

font_path = "fonts/NewAmsterdam-Regular.ttf"
font_size = img_size

font = ImageFont.truetype(font_path, font_size)

for num in range(1, 100):
    img = Image.new("RGBA", (img_size, img_size), (255, 255, 255, 0))

    draw = ImageDraw.Draw(img)

    num_str = str(num)

    hex, color = colors[1]

    #depreciated -> .textsize()
    text_width, text_height = draw.textsize(num_str, font=font)
    text_x = (img_size - text_width) // 2
    text_y = (img_size - text_height) // 2 - 15

    draw.text((text_x, text_y), num_str, font=font, fill=hex)

    img.save(f"emojis/{color}_{num}.png")

print("Images generated successfully!")
