## Himawari-8 GIF animation

These are some scripts to generate Himawari-8 GIFs using `python` and `ffmpeg`.

Here is an example of the output you can expect: https://imgur.com/Zonhp5y

Original idea: https://gist.github.com/celoyd/b92d0de6fae1f18791ef

The main difference between the original and this version is that this version works on Windows because it is almost entirely written in `python`. For generating the GIF from the image sequence, `ffmpeg` is called from a very simple batch file, that can be rewritten as a shell script for Linux users.

## Installation

Needs at least Python 3.6 and ffmpeg (`brew install ffmpeg`)

1. `python3 -m venv venv` (creates a new virtual environment)
2. `source venv/bin/activate` (activates virtual environment)
3. `pip install -r requirements.txt` (installs dependencies)

## Running

1. Edit `config.py` with the date range and zoom you want.
2. Run `python run.py`. This runs a couple of scripts.

### Various scripts

1. `fetch_many.py`. This downloads all the source images
2. `interp.py` substitutes the "no image"-images at 14:40 and 2:40 with an interpolation of the images before and after the gap.
3. `label_and_rename.py`. Here you can determine how the timestamp should look. The images will be saved as "image1.png", "image2.png", because that makes life easier for step 4.
4. `make_gif.py` creates the GIF!
