from os import path

download_dir = path.join(path.dirname(path.realpath(__file__)), "download")
image_dir = path.join(path.dirname(path.realpath(__file__)), "images")
gif_file = path.join(path.dirname(path.realpath(__file__)), "out.mp4")
file_extension = "jpg"

# zoom is between 1 and 20
zoom = 16

year = 2020
month = 1
days = range(4, 5)
hours = range(0, 24)
minutes = [10 * x for x in range(0, 6)]

output_crop = (4474, 6988, 4474 + 1006, 6988 + 555)
output_width = 800
ratio = output_width / (output_crop[2] - output_crop[0])
output_size = (output_width, int((output_crop[3] - output_crop[1]) * ratio))
fontsize = 20
text_position = (10, output_size[1] - fontsize - 10)

time_difference_hours = 11

source_fps = 6
output_fps = 60

palette_file = path.join(path.dirname(path.realpath(__file__)), "palette.png")
filters_palette = "fps={},scale={}:-1:flags=lanczos".format(output_fps, output_size[0])
# filters = "fps=60,setpts=2*PTS,scale={}:-2:flags=lanczos".format(
#     output_size[0]
# )
filters = "minterpolate='fps={}:mi_mode=blend:mc_mode=aobmc:me_mode=bilat:vsbmc=1',scale={}:-2:flags=lanczos".format(
    output_fps, output_size[0]
)

# filters = "minterpolate='fps={}:mi_mode=blend:mc_mode=aobmc:me_mode=bidir:vsbmc=1',scale={}:-2:flags=lanczos".format(
#     output_fps, output_size[0]
# )

filters_test = [
    "minterpolate='fps={}:mi_mode=mci:mc_mode=obmc:me_mode=bilat:vsbmc=0',scale={}:-2:flags=lanczos".format(
        output_fps, output_size[0]
    ),
    "minterpolate='fps={}:mi_mode=mci:mc_mode=obmc:me_mode=bidir:vsbmc=0',scale={}:-2:flags=lanczos".format(
        output_fps, output_size[0]
    ),
    "minterpolate='fps={}:mi_mode=mci:mc_mode=obmc:me_mode=bidir:vsbmc=1',scale={}:-2:flags=lanczos".format(
        output_fps, output_size[0]
    ),
    "minterpolate='fps={}:mi_mode=mci:mc_mode=aobmc:me_mode=bilat:vsbmc=0',scale={}:-2:flags=lanczos".format(
        output_fps, output_size[0]
    ),
    "minterpolate='fps={}:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=0',scale={}:-2:flags=lanczos".format(
        output_fps, output_size[0]
    ),
    "minterpolate='fps={}:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1',scale={}:-2:flags=lanczos".format(
        output_fps, output_size[0]
    ),
]
filters_test.reverse()
