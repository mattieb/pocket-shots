import struct
from PIL import Image


# based on <https://www.analogue.co/developer/docs/library#sample-code>
def convert_image(source_filename, dest_filename):
    source = Image.open(source_filename)
    dest = open(dest_filename, "wb")
    width, height = source.size
    bpp = 4

    rgb = source.convert("RGBA")

    out = rgb.rotate(90, expand=True)

    pixels = out.getdata()

    image = []
    image.append(bpp * 8)  # Header Magic (32-bit)
    image.append(0x49)
    image.append(0x50)
    image.append(0x41)
    image.append(width & 0xFF)  # Header Width (16-bit)
    image.append((width >> 8) & 0xFF)
    image.append(height & 0xFF)  # Header Height (16-bit)
    image.append((height >> 8) & 0xFF)

    for i in range(width * height):
        image.append(pixels[i][2])  # Blue Byte
        image.append(pixels[i][1])  # Green Byte
        image.append(pixels[i][0])  # Red Byte
        image.append(pixels[i][3])  # Alpha Byte

    for i in range((width * height * bpp) + 8):
        dest.write(struct.pack("B", image[i]))  # Write Header + Pixels

    dest.close()
