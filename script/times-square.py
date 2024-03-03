#!/usr/bin/env python3

import time
from datetime import datetime, timedelta
from earth_cam_downloader import EarthCamDownloader
import argparse


# It can only work at hour granualrity
# time to start downloading archived footage from
START = datetime(2024, 3, 1, 10, 0, 0)

# time to end downloading archived footage from
END = datetime(2024, 3, 1, 10, 59, 0)

# camera names and ids to download
CAMERAS = {
    "Ireland_Templebar": "24322",
    " Chicago_WrigleyField " : "13661"
#    "times-square-4k": "hdtimes10",
#    "crossroads": "15559",
#    "south-view": "4017timessquareHD1",
}

FILE_FORMAT = "mp4"
OUTPUT_DIR = "earthcam_data"

# when called, get the archieve data for last hour
def main():

    hr_before = datetime.now() - timedelta(hours=1)
    START = hr_before.replace(minute=0)
    END = hr_before.replace(minute=59)
    
    started_at = time.time()
    for cam_name, cam_id in CAMERAS.items():
        EarthCamDownloader(
            cam_id, cam_name, START, END, FILE_FORMAT, OUTPUT_DIR
        ).download()
    ended_at = time.time()
    print(f"Downloaded temple bar and wringlyfields files in {round((ended_at -  started_at) / 60, 2)} minutes.")


if __name__ == "__main__":
    main()
