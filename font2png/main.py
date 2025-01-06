# coding=utf-8
from PIL import Image, ImageDraw, ImageFont


def generate_symbol_image(font_path, symbol, size, output_path):
    # 创建空白图像，RGBA模式意味着支持透明背景
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))

    try:
        # 加载字体，设置字体大小
        font = ImageFont.truetype(font_path, size)

        # 创建ImageDraw对象，用来在图片上绘制
        drawing = ImageDraw.Draw(image)

        # 计算符号的宽高，确保符号居中
        w, h = drawing.textsize(symbol, font=font)
        text_position = ((size - w) / 2, (size - h) / 2)

        # 绘制符号到图像中
        drawing.text(text_position, symbol, font=font, fill=(0, 0, 0, 255))  # 使用黑色填充符号

        # 保存图像为PNG格式
        image.save(output_path, format='PNG')

        print(output_path)

    except Exception as e:
        print(e)


# 使用示例：生成一个包含字符 'A' 的符号图像
font_path = 'C:\\Windows\\Fonts\\ARIALN.TTF'  # 替换为你的.ttf字体文件路径
symbol = 'A'  # 你想要绘制的符号
size = 100  # 图像的宽高
output_path = 'C:\\Users\\admin\Desktop\\temp\\output_symbol.png'  # 输出图像的路径

# 调用函数生成图像
generate_symbol_image(font_path, symbol, size, output_path)
