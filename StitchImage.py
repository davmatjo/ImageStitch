from PIL import Image

def get_img_res(resolutions):
    highest_y = 0
    total_x = 0
    for i in range(len(resolutions)):
        total_x += resolutions[i][0]

        if resolutions[i][1] > highest_y:
            highest_y = resolutions[i][1]

    return (total_x, highest_y)


img_num = int(input("Number of monitors"))
resolutions = []

for i in range(img_num):
    print("Monitor", str(i + 1))
    resolutions.append((int(input("width:")), int(input("height:"))))

final_img_res = get_img_res(resolutions)

images = []

for i in range(img_num):
    images.append(Image.open("img" + str(i + 1) + ".jpg"))

offsets = []
for i in range(img_num):
    offsets.append(int(input("Offset for image " + str(i + 1) + ", from the top")))

final_img = Image.new("RGB", final_img_res, "black")

resolutions = [[0, 0]] + resolutions

for i in range(img_num):
    final_img.paste(images[i], (resolutions[i][0], offsets[i]))

final_img.save("output.jpg")