import os
import sys
import requests
import urllib.request


var_client_id = '<insert_your_twitch_client_id_here>'
var_basepath = 'tmp/'
var_full_url = sys.argv[1]
var_slug = var_full_url.rpartition('/')[-1]

clip_info = requests.get("https://api.twitch.tv/helix/clips?id=" + var_slug, headers={"Client-ID": var_client_id}).json()

thumb_url = clip_info['data'][0]['thumbnail_url']
var_mp4_url = thumb_url.split("-preview",1)[0] + ".mp4"
var_out_filename = var_slug + ".mp4"
output_path = (var_basepath + var_out_filename)

def dl_progress(count, block_size, total_size):
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%" % percent)
    sys.stdout.flush()

# create the basepath directory
if not os.path.exists(var_basepath):
    os.makedirs(var_basepath)

urllib.request.urlretrieve(var_mp4_url, output_path, reporthook=dl_progress)