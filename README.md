# pocket-shots

Creates Analogue Pocket library image collections.

## Prerequisites

### Database and images

This repository has submodules for [libretro-database](https://github.com/libretro/libretro-database), which contains metadata on games, and select collections from [libretro-thumbnails](https://github.com/libretro-thumbnails/libretro-thumbnails), which contains the actual images.

You will need to update submodules after you clone this repository:

```shell
git submodule update --init --recursive --remote
```

### Python runtime

The easiest and best way to run this as well as many other Python-based software is with Astral's [uv](https://docs.astral.sh/uv/).

[Install it](https://docs.astral.sh/uv/getting-started/installation/) if you haven't already.

Other Python tooling likely also works, but getting that running is left as an exercise to the reader. [pyproject.toml](./pyproject.toml) has all the metadata necessary to run the project.

## Usage

To build a Game Boy library of title screens:

```
uv run pocket-shots GB Titles
```

Valid platforms are:

- `GB`: Game Boy and Game Boy Color
- `GBA`: Game Boy Advance
- `GG`: Game Gear

Valid image types are dependent on what is present in the platform's thumbnails collection, but may include:

- `Boxarts`: box art
- `Logos`: logos
- `Snaps`: game screenshots
- `Titles`: game title screens
