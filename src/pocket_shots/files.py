from glob import glob
import os
import re


def substitute_specials(filename):
    return re.sub(r'[&*/:`<>?\\|"]', "_", filename)


def thumbnail_pattern(platform, type, name):
    return os.path.join(
        platform.replace(" ", "_"), "Named_" + type, substitute_specials(name) + ".*"
    )


def glob_thumbnails(base_path, platform, type, name):
    return glob(os.path.join(base_path, thumbnail_pattern(platform, type, name)))
