from os import path

download_dir = path.join(path.dirname(path.realpath(__file__)), "download")
image_dir = path.join(path.dirname(path.realpath(__file__)), "images")
file_extension = "jpg"

# zoom is one of 1, 4, 8, 16, or 20
zoom = 16

year = 2020
month = 1
days = range(4, 5)
hours = range(0, 24)
minutes = [10 * x for x in range(0, 6)]

output_crop = (4474, 6988, 4474 + 1006, 6988 + 555)
output_width = 1000
ratio = output_width / (output_crop[2] - output_crop[0])
output_size = (output_width, int((output_crop[3] - output_crop[1]) * ratio))
fontsize = 20
text_position = (10, output_size[1] - fontsize - 10)

time_difference_hours = 11

# best = 0, worst = 51, default = 23
quality = 23

palette_file = path.join(path.dirname(path.realpath(__file__)), "palette.png")
filters_palette = "scale={}:-1:flags=lanczos".format(output_size[0])


video_settings = [
    # {
    #     "filters": "minterpolate='fps=60:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1',scale={}:-2:flags=lanczos".format(
    #         output_size[0]
    #     ),
    #     "arguments": "-crf 5",
    #     "source_fps": 15,
    #     "filename": "out-wildfeuer-short.mp4",
    # },
    # {
    #     "filters": "minterpolate='fps=60:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1',scale={}:-2:flags=lanczos".format(
    #         output_size[0]
    #     ),
    #     "arguments": "-crf {}".format(quality),
    #     "source_fps": 10,
    #     "filename": "out-wildfeuer-medium.mp4",
    # },
    {
        "filters": "minterpolate='fps=60:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1',scale={}:-2:flags=lanczos".format(
            output_size[0]
        ),
        "arguments": "-crf {} -b:v -c:v libvpx-vp9".format(quality),
        "source_fps": 10,
        "filename": "out-wildfeuer-medium.webm",
    },
    # {
    #     "filters": "minterpolate='fps=60:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1',scale={}:-2:flags=lanczos".format(
    #         output_size[0]
    #     ),
    #     "arguments": "-crf {quality}".format(quality),
    #     "source_fps": 7,
    #     "filename": "out-wildfeuer-long.mp4",
    # },
]
