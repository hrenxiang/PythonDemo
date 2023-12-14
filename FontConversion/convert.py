import os
from fontTools.ttLib import TTFont

def otf_to_ttf(otf_path, ttf_path):
    font = TTFont(otf_path)
    font.flavor = None  # 移除风格，以便保存为TTF
    font.save(ttf_path)

def convert_otf_to_ttf(otf_dir, ttf_dir):
    if not os.path.exists(ttf_dir):
        os.makedirs(ttf_dir)

    for root, _, files in os.walk(otf_dir):
        for file in files:
            if file.lower().endswith('.otf'):
                otf_path = os.path.join(root, file)
                ttf_path = os.path.join(ttf_dir, file.lower().replace('.otf', '.ttf'))
                otf_to_ttf(otf_path, ttf_path)

def main():
    otf_directory = './PingFang-OTF'  # OTF文件所在目录
    ttf_directory = './PingFang-TTF'  # 要保存TTF文件的目录
    convert_otf_to_ttf(otf_directory, ttf_directory)

if __name__ == "__main__":
    main()