from wand.image import Image
from wand.color import Color


def convert_pdf_to_png(file_address):
    with Image(filename="../" + file_address + ".pdf", resolution=600) as img:
        with Image(width=img.width, height=img.height, background=Color("white")) as bg:
            bg.composite(img, 0, 0)
            bg.save(filename=file_address + ".png")


def main():
    convert_pdf_to_png("MUSE_20180323_153150_73000")


if __name__ == "__main__":
    main()