from os import path

download_dir = path.join(path.dirname(path.realpath(__file__)), "download")
image_dir = path.join(path.dirname(path.realpath(__file__)), "images")
gif_file = path.join(path.dirname(path.realpath(__file__)), "out.gif")

# zoom is between 1 and 20
zoom = 16

year = 2020
month = 1
days = range(1, 2)
hours = range(0, 24)
minutes = [10 * x for x in range(0, 6)]

fontsize = zoom * 20
text_position = (10, 520)

palette_file = path.join(path.dirname(path.realpath(__file__)), "palette.png")
filters = "fps=24,scale={}:-1:flags=lanczos".format(zoom * 550)

