from PIL import Image
import os

def get_photo(address):
    folder_path = address
    image_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            image_list.append(image)
    return image_list

def get_love(address):
    with open(f'{address}\\photo_story.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        line = line.strip()  # 去除行尾的换行符或空格
        elements = line.split(':')  # 使用逗号分隔每行的两个字符串
        if len(elements) == 2:  # 检查是否有两个元素
            data.append(elements)
    return data
#my_love_to_liling
def output_photo(image_list, data, address):
    # 创建 HTML 文件并打开
    html_file = open(f"{address}\\my_love_to_liling.html", "w")
    html_file.write("<html><head><style>")
    html_file.write("body { background-image: url('background.jpg'); background-size: cover; backdrop-filter: blur(5px); display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; padding: 20px;}")
    html_file.write(".image-container { position: relative; text-align: center; margin-bottom: 20px;}")
    html_file.write(".image-container img { max-width: 300px; max-height: 300px; display: block; margin: 0 auto;}")
    html_file.write(".image-container p { text-align: center;}")
    html_file.write("</style></head><body>")

    # 遍历图片和字符串列表，并输出到 HTML 文件中
    html_file.write("<div style='display: flex; flex-direction: column; align-items: center;'>") # 添加容器样式，使内容从上到下排列
    for i, image in enumerate(image_list):
        image_path = f"image{i}.jpg"
        image.save(os.path.join(address, image_path))  # 将图片保存到本地

        html_file.write("<div class='image-container'>")
        html_file.write(f"<img src='{image_path}'>")
        html_file.write(f"<p>{data[i][0]} {data[i][1]}</p>")
        html_file.write("</div>")

    html_file.write("</div>") # 结束容器标签
    # 关闭 HTML 文件
    html_file.write("</body></html>")
    html_file.close()

address = "D:\\OneDrive - 知行汽车科技(苏州)股份有限公司\\Desktop\\程序for_my_LLLP\\photo_story"
address_2="D:\\OneDrive - 知行汽车科技(苏州)股份有限公司\\Desktop\\程序for_my_LLLP\\image"
image_list = get_photo(address)
data = get_love(address)
output_photo(image_list, data, address_2)