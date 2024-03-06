from PIL import Image


def rgba_to_svg(im):
    s = """<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d">\n""" % (im.width, im.height)

    for y in range(im.height):
        for x in range(im.width):
            rgba = im.getpixel((x, y))
            if rgba[3] == 0:
                continue
            s += """  <rect x="%d" y="%d" width="1" height="1" style="fill:rgba%s;" />\n""" % (
                x, y, rgba[:3])
        print("Converting pixels: " + str(y * 100 / im.height) + "%")

    s += """</svg>\n"""
    return s


def png_to_svg(input_path, output_path):
    im = Image.open(input_path).convert("RGBA")
    svg_content = rgba_to_svg(im)
    with open(output_path, "w") as f:
        f.write(svg_content)


def main():
    # 使用示例
    png_to_svg('home_active.png', 'home_active.svg')


if __name__ == "__main__":
    img = Image.open('apply_active.png')
    print(img.mode)  # 输出图像模式
    print(img.getpixel((0, 0)))  # 检查像素值
    main()
