from fontTools.ttLib import TTFont


def print_font_names(file_path):
    font = TTFont(file_path)
    name_table = font['name']
    for record in name_table.names:
        name_id = record.nameID
        if name_id in [1, 2, 4, 6]:  # Font Family, Font Subfamily, Full Font Name, Postscript Name
            print(f"Name ID {name_id}: {record.toUnicode()}")


if __name__ == '__main__':
    print_font_names('STSongti-SC-Regular.otf')
