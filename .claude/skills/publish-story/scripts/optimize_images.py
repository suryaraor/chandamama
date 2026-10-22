"""Resize and compress story images for the web.

Usage: python optimize_images.py <dest_dir> <image> [<image> ...]

Each image is rotated per its EXIF data, scaled so its longest side is at
most 1600px, and saved into <dest_dir> as a progressive JPEG (PNG if it has
transparency). File names are lowercased with spaces turned into hyphens.
Prints one line per image: <output path> <width>x<height> <KB>.
"""
import re
import sys
from pathlib import Path

from PIL import Image, ImageOps

MAX_SIDE = 1600


def web_name(src: Path, ext: str) -> str:
    stem = re.sub(r"[^a-z0-9]+", "-", src.stem.lower()).strip("-") or "image"
    return stem + ext


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    dest = Path(sys.argv[1])
    dest.mkdir(parents=True, exist_ok=True)
    for arg in sys.argv[2:]:
        src = Path(arg)
        with Image.open(src) as im:
            im = ImageOps.exif_transpose(im)
            im.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
            has_alpha = im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info)
            if has_alpha:
                out = dest / web_name(src, ".png")
                im.save(out, optimize=True)
            else:
                out = dest / web_name(src, ".jpg")
                im.convert("RGB").save(out, "JPEG", quality=82, optimize=True, progressive=True)
            print(f"{out.as_posix()} {im.width}x{im.height} {out.stat().st_size // 1024}KB")


if __name__ == "__main__":
    main()
