# take a directory of Himawari-8 images 2015-12-01T02-30-00_z1.png, 2015-12-01T02-40-00_z1.png,...
# draw a timestamp on them
# save them as image1.png, image2.png,...

from os import listdir, path, makedirs
from PIL import Image, ImageFont, ImageDraw
import config
from glob import glob


def main():
    files = listdir(config.download_dir)
    font = ImageFont.truetype(
        "typetogether-tabletgothic-bold-tabular.ttf", config.fontsize
    )

    if not path.exists(config.image_dir):
        makedirs(config.image_dir)

    files = sorted(glob(path.join(config.download_dir, "*.png")))

    for index, filepath in enumerate(files):
        filename = path.basename(filepath)
        print(filename)
        im = Image.open(filepath)
        draw = ImageDraw.Draw(im)

        # make text to draw on image
        text = filename.replace("-00_z1.png", "").replace("T", " ")
        text = text[:-3] + ":" + text[-2:]

        draw.text(config.text_position, text, "white", font=font)

        im.save(config.image_dir + "/" + "image{:05d}.png".format(index + 1))


if __name__ == "__main__":
    main()
