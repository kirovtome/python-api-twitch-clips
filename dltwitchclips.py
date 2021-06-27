import os
import sys
import requests
import urllib.request
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-c", "--clip")
args = parser.parse_args()

if len(sys.argv) == 1:
    print("Usage: python3 dltwitchclips.py --clip <paste_clip_url_here>")
    sys.exit()


client_id = 'Your Client ID'
basepath = 'tmp/'
slug = args.clip.rpartition('/')[-1]

clip_info = requests.get("https://api.twitch.tv/kraken/clips/" + slug, headers={"Client-ID": client_id, "Accept":"application/vnd.twitchtv.v5+json"}).json()

thumb_url = clip_info['thumbnails']['medium']
mp4_url = thumb_url.split("-preview",1)[0] + ".mp4"
out_filename = slug + ".mp4"
output_path = (basepath + out_filename)


def dl_progress(count, block_size, total_size):
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%" % percent)
    sys.stdout.flush()

# create the basepath directory
if not os.path.exists(basepath):
    os.makedirs(basepath)

try:
    urllib.request.urlretrieve(mp4_url, output_path, reporthook=dl_progress)
except:
    print("An exception occurred")
