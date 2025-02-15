def expand_platform(platform_shortname) -> str:
    if platform_shortname == "GB":
        return [
            "Nintendo - Game Boy",
            "Nintendo - Game Boy Color",
        ]
    elif platform_shortname == "GBA":
        return [
            "Nintendo - Game Boy Advance",
        ]
    elif platform_shortname == "GG":
        return [
            "Sega - Game Gear",
        ]
    else:
        raise ValueError("unknown platform shortname %r" % platform_shortname)
