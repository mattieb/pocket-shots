from sys import stderr
from pocket_shots.parser import parse_dat


def find_item(object, symbol):
    return next((item for item in object[1] if item[0] == symbol), None)


def name_and_crc(datobject):
    name = find_item(datobject, "name")
    if name is None:
        print('skipping game without name', file=stderr)
        return None
    rom = find_item(datobject, "rom")
    if rom is None:
        print('skipping %r which has no rom object' % name, file=stderr)
        return None
    crc = find_item(rom, "crc")
    if crc is None:
        print('skipping %r which has no crc' % name, file=stderr)
        return None

    return (name[1], crc[1].lower())


def names_and_crcs(platform_name):
    datfilename = "metadat/no-intro/%s.dat" % platform_name

    datobjects = parse_dat("libretro-database/%s" % datfilename)

    names_and_crcs = [
        name_and_crc(datobject) for datobject in datobjects if datobject[0] == "game"
    ]

    return filter(lambda i: i is not None, names_and_crcs)
