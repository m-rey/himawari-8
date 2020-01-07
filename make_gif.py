import subprocess
import config
import shlex


def main():
    # generate color palette for gif
    args = shlex.split(
        'ffmpeg -v warning -f image2 -i {image_dir}/image%05d.{file_extension} -vf "{filters},palettegen" -y {palette_file}'.format_map(
            {
                "image_dir": config.image_dir,
                "filters": config.filters,
                "palette_file": config.palette_file,
                "file_extension": config.file_extension,
            }
        )
    )

    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print("wrote palette for gif to {}".format(config.palette_file))

    # generate gif
    args = shlex.split(
        'ffmpeg -v warning -f image2 -i {image_dir}/image%05d.{file_extension} -i {palette_file} -lavfi "{filters} [x]; [x][1:v] paletteuse" -y {gif_file}'.format_map(
            {
                "image_dir": config.image_dir,
                "filters": config.filters,
                "palette_file": config.palette_file,
                "gif_file": config.gif_file,
                "file_extension": config.file_extension,
            }
        )
    )

    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print("wrote gif to {}".format(config.gif_file))


if __name__ == "__main__":
    main()
