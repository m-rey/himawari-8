# take a directory of Himawari-8 images 2015-12-01T02-30-00_z1.png, 2015-12-01T02-40-00_z1.png,...
# draw a timestamp on them
# save them as image1.png, image2.png,...

from os import listdir, path, makedirs
from PIL import Image, ImageFont, ImageDraw
import config
from glob import glob
from shutil import rmtree


def main():
    files = listdir(config.download_dir)
    font = ImageFont.truetype(
        "typetogether-tabletgothic-bold-tabular.ttf", config.fontsize
    )

    rmtree(config.image_dir)
    makedirs(config.image_dir)

    files = sorted(
        glob(path.join(config.download_dir, "*.{}".format(config.file_extension)))
    )

    for index, filepath in enumerate(files):
        filename = path.basename(filepath)
        print(filename)
        im = Image.open(filepath)
        if config.output_crop:
            im = im.crop(config.output_crop)
        im = im.resize(config.output_size, Image.LANCZOS)
        # draw = ImageDraw.Draw(im)

        # # make text to draw on image
        # text = filename.replace(
        #     "-00_z{}.{}".format(config.zoom, config.file_extension), ""
        # ).replace("T", " ")
        # date = text.split(" ")[0].split("-")
        # date.reverse()
        # time = text.split(" ")[-1].split("-")
        # hours = int(time[0])

        # hours += config.time_difference_hours
        # if hours > 23:
        #     hours -= 23
        #     date[0] = "{:02d}".format(int(date[0]) + 1)

        # time[0] = "{:02d}".format(hours)

        # text = "{} {}".format(".".join(date), ":".join(time))
        # print(text)

        # draw.text(config.text_position, text, "white", font=font)

        im.save(
            config.image_dir
            + "/"
            + "image{:05d}.{}".format(index + 1, config.file_extension)
        )


if __name__ == "__main__":
    main()
