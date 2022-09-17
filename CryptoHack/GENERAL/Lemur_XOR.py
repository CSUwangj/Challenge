from PIL import Image
  
lemur = Image.open("lemur_ed66878c338e662d3473f0d98eedbd0d.png")
flag = Image.open("flag_7ae18c704272532658c10b5faad06d74.png")
  
pixel = lemur.load()
  
width, height = lemur.size

for i in range(width):
    for j in range(height):
        r1, g1, b1 = lemur.getpixel((i, j))
        r2, g2, b2 = flag.getpixel((i, j))
        pixel[i, j] = (r1 ^ r2, g1 ^ g2, b1 ^ b2)

lemur.save("flag.png", format="png")