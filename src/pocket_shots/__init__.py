from os import mkdir
import os

from tqdm import tqdm
from pocket_shots.data import names_and_crcs
from pocket_shots.files import glob_thumbnails
from pocket_shots.image import convert_image
from pocket_shots.platforms import expand_platform
from sys import argv, stderr


def main() -> None:
    platform_shortname = argv[1]
    type = argv[2]

    platforms = expand_platform(platform_shortname)

    mkdir(platform_shortname)

    for platform in platforms:
        multiple = 0
        not_found = 0
        images = 0
        exists = 0

        for name_and_crc in tqdm(
            list(names_and_crcs(platform)), desc=platform, unit="games"
        ):
            name = name_and_crc[0]

            files = glob_thumbnails("libretro-thumbnails", platform, type, name)

            if len(files) > 1:
                multiple += 1
                continue

            elif len(files) < 1:
                not_found += 1
                continue

            crc = name_and_crc[1]

            dest = os.path.join(platform_shortname, crc + ".bin")

            if os.path.exists(dest):
                exists += 1
                continue

            convert_image(files[0], dest)
            images += 1

        print(
            "wrote %d images (skipped %d not found, %d multiple matches, %d duplicate crcs)"
            % (images, not_found, multiple, exists),
            file=stderr,
        )
