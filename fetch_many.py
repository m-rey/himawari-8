import hi8fetch as hi8
from os import path, makedirs
import config


def strpad(i):
    if i < 10:
        return "0" + str(i)
    else:
        return str(i)


def main():
    if not path.exists(config.download_dir):
        makedirs(config.download_dir)

    for day in config.days:
        for hour in config.hours:
            for minute in config.minutes:
                namestr = (
                    str(config.year)
                    + "-"
                    + strpad(config.month)
                    + "-"
                    + strpad(day)
                    + "T"
                    + strpad(hour)
                    + ":"
                    + strpad(minute)
                    + ":00"
                )
                filename = (
                    config.download_dir
                    + "/"
                    + namestr.replace(":", "-")
                    + "_z"
                    + str(config.zoom)
                    + ".png"
                )
                if path.exists(filename):
                    print("{} already exists".format(namestr))
                else:
                    print(namestr)
                    hi8.fetch(namestr, config.zoom, filename)

if __name__ == "__main__":
    main()