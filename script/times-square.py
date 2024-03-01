#!/usr/bin/env python3

import time
from datetime import datetime

from earth_cam_downloader import EarthCamDownloader

# It can only work at hour granualrity
# time to start downloading archived footage from
START = datetime(2023, 12, 28, 11, 0, 0)

# time to end downloading archived footage from
END = datetime(2023, 12, 28, 12, 0, 0)

# camera names and ids to download
CAMERAS = {
    "Ireland_Templebar": "24322",
    " Chicago_WrigleyField " : "13661"
#    "times-square-4k": "hdtimes10",
#    "crossroads": "15559",
#    "south-view": "4017timessquareHD1",
}

FILE_FORMAT = "mp4"

OUTPUT_DIR = "output"


def main():
    started_at = time.time()
    for cam_name, cam_id in CAMERAS.items():
        EarthCamDownloader(
            cam_id, cam_name, START, END, FILE_FORMAT, OUTPUT_DIR
        ).download()
    ended_at = time.time()
    print(f"Downloaded times square files in {round((ended_at -  started_at) / 60, 2)} minutes.")


if __name__ == "__main__":
    main()
