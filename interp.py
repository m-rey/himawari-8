from PIL import Image
import config


def interp(imfile1, imfile2, imfileout, alpha=0.5):
    im1 = Image.open(imfile1)
    im2 = Image.open(imfile2)
    im3 = Image.blend(im1, im2, alpha)
    im3.save(imfileout)  # filetype is determined by extension


def strpad(i):
    if i < 10:
        return "0" + str(i)
    else:
        return str(i)


def main():
    for day in config.days:
        for hour in config.hours:
            for minute in config.minutes:
                if (hour == 2 or hour == 14) and minute == 40:
                    filenamebase = (
                        config.download_dir
                        + "/"
                        + str(config.year)
                        + "-"
                        + strpad(config.month)
                        + "-"
                        + strpad(day)
                        + "T"
                        + strpad(hour)
                        + "-"
                    )
                    filename30 = filenamebase + "30-00_z{}.png".format(config.zoom)
                    filename40 = filenamebase + "40-00_z{}.png".format(config.zoom)
                    filename50 = filenamebase + "50-00_z{}.png".format(config.zoom)
                    interp(filename30, filename50, filename40)
                    print("Fixed " + filename40)


if __name__ == "__main__":
    main()