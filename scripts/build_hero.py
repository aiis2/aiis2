from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).parents[1]
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "ai-systems-lab-source.png"
OUTPUT = ASSETS / "ai-systems-lab.gif"
WIDTH, HEIGHT = 1200, 420
CORE = (942, 208)
FRAMES = 24


def load_font(size: int, *, mono: bool = False, cjk: bool = False) -> ImageFont.FreeTypeFont:
    if cjk:
        candidates = [Path("C:/Windows/Fonts/msyh.ttc"), Path("C:/Windows/Fonts/msyhbd.ttc")]
    elif mono:
        candidates = [Path("C:/Windows/Fonts/consola.ttf"), Path("C:/Windows/Fonts/cascadiamono.ttf")]
    else:
        candidates = [Path("C:/Windows/Fonts/bahnschrift.ttf"), Path("C:/Windows/Fonts/arialbd.ttf")]

    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default(size=size)


def regular_polygon(center: tuple[int, int], radius: float, sides: int, angle: float = 0) -> list[tuple[float, float]]:
    cx, cy = center
    return [
        (
            cx + math.cos(angle + index * math.tau / sides) * radius,
            cy + math.sin(angle + index * math.tau / sides) * radius,
        )
        for index in range(sides)
    ]


def glow_ellipse(
    layer: Image.Image,
    box: tuple[int, int, int, int],
    color: tuple[int, int, int],
    alpha: int,
    blur: int,
) -> None:
    glow = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse(box, fill=(*color, alpha))
    layer.alpha_composite(glow.filter(ImageFilter.GaussianBlur(blur)))


def build_source() -> Image.Image:
    rng = random.Random(20260714)
    image = Image.new("RGBA", (WIDTH, HEIGHT), (2, 7, 12, 255))
    draw = ImageDraw.Draw(image, "RGBA")

    for y in range(HEIGHT):
        strength = int(18 * y / HEIGHT)
        draw.line((0, y, WIDTH, y), fill=(2, 8 + strength // 3, 14 + strength, 255))

    glow_ellipse(image, (710, -30, 1190, 450), (0, 198, 255), 54, 86)
    glow_ellipse(image, (825, 88, 1060, 323), (65, 255, 190), 42, 44)
    draw = ImageDraw.Draw(image, "RGBA")

    for x in range(0, WIDTH + 1, 40):
        alpha = 24 if x % 200 else 46
        draw.line((x, 0, x, HEIGHT), fill=(24, 108, 131, alpha), width=1)
    for y in range(20, HEIGHT, 40):
        alpha = 22 if y % 200 else 42
        draw.line((0, y, WIDTH, y), fill=(24, 108, 131, alpha), width=1)

    for _ in range(34):
        y = rng.randint(34, HEIGHT - 34)
        start = rng.randint(560, 760)
        end = rng.randint(860, 1160)
        mid = rng.randint(start + 20, max(start + 21, end - 20))
        color = (14, 195, 230, rng.randint(45, 105))
        draw.line((start, y, mid, y), fill=color, width=1)
        draw.line((mid, y, min(end, mid + 28), y + rng.choice((-16, 16))), fill=color, width=1)
        node_x = min(end, mid + 28)
        node_y = y + rng.choice((-16, 16))
        draw.ellipse((node_x - 2, node_y - 2, node_x + 2, node_y + 2), fill=(67, 255, 191, 145))

    for radius, alpha, width in ((128, 45, 1), (98, 80, 1), (68, 155, 2)):
        points = regular_polygon(CORE, radius, 6, math.pi / 6)
        draw.line(points + [points[0]], fill=(0, 214, 255, alpha), width=width, joint="curve")

    for radius in (44, 30, 16):
        points = regular_polygon(CORE, radius, 6, math.pi / 6)
        fill = (4, 26 + radius, 43 + radius, 220)
        draw.polygon(points, fill=fill, outline=(76, 255, 198, 210))

    for radius in (150, 166):
        draw.arc(
            (CORE[0] - radius, CORE[1] - radius, CORE[0] + radius, CORE[1] + radius),
            start=205,
            end=335,
            fill=(0, 204, 247, 72),
            width=1,
        )

    draw.rectangle((28, 24, WIDTH - 28, HEIGHT - 24), outline=(17, 181, 211, 48), width=1)
    draw.line((28, 62, 28, 24, 66, 24), fill=(57, 255, 196, 180), width=2)
    draw.line((WIDTH - 66, HEIGHT - 24, WIDTH - 28, HEIGHT - 24, WIDTH - 28, HEIGHT - 62), fill=(0, 207, 255, 130), width=2)

    image.convert("RGB").save(SOURCE, optimize=True)
    return image


def overlay_identity(frame: Image.Image) -> None:
    veil = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    veil_draw = ImageDraw.Draw(veil)
    for x in range(760):
        alpha = max(0, 165 - int(x / 760 * 165))
        veil_draw.line((x, 0, x, HEIGHT), fill=(0, 5, 9, alpha))
    frame.alpha_composite(veil)

    draw = ImageDraw.Draw(frame, "RGBA")
    cyan = (79, 224, 255, 255)
    green = (90, 255, 185, 255)
    white = (236, 249, 252, 255)
    muted = (144, 179, 188, 255)

    draw.text((70, 58), "SYSTEM ID  //  AIIS2-02", font=load_font(15, mono=True), fill=cyan)
    draw.text((67, 91), "AIIS2", font=load_font(73), fill=white, stroke_width=1, stroke_fill=(255, 255, 255, 110))
    draw.line((72, 180, 278, 180), fill=green, width=3)
    draw.text((298, 146), "// AI SYSTEMS LAB", font=load_font(30), fill=cyan)
    draw.text(
        (71, 213),
        "FULL-STACK AI ENGINEERING  /  INTELLIGENT SYSTEMS",
        font=load_font(17, mono=True),
        fill=white,
    )
    draw.text((70, 250), "全栈 AI 工程 · 智能系统实验室", font=load_font(18, cjk=True), fill=muted)
    draw.ellipse((71, 315, 79, 323), fill=green)
    draw.text((91, 307), "SYSTEM ONLINE", font=load_font(14, mono=True), fill=green)
    draw.text((245, 307), "SHANGHAI  /  2026", font=load_font(14, mono=True), fill=muted)

    draw.text((70, 363), "BUILDING SIGNALS FROM DATA TO EXPERIENCE", font=load_font(12, mono=True), fill=(86, 151, 164, 220))
    draw.text((1040, 363), "02:AI", font=load_font(12, mono=True), fill=(74, 229, 255, 210))


def build_frame(source: Image.Image, index: int) -> Image.Image:
    phase = index / FRAMES
    frame = source.copy()
    dynamic = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(dynamic, "RGBA")

    pulse = (math.sin(phase * math.tau) + 1) / 2
    radius = int(74 + pulse * 14)
    glow_ellipse(
        dynamic,
        (CORE[0] - radius, CORE[1] - radius, CORE[0] + radius, CORE[1] + radius),
        (0, 232, 255),
        int(32 + pulse * 42),
        20,
    )
    draw = ImageDraw.Draw(dynamic, "RGBA")

    orbit_angle = phase * math.tau
    for offset, orbit_radius in ((0, 103), (math.pi, 128), (math.pi / 2, 155)):
        x = CORE[0] + math.cos(orbit_angle + offset) * orbit_radius
        y = CORE[1] + math.sin(orbit_angle + offset) * orbit_radius * 0.56
        draw.ellipse((x - 3, y - 3, x + 3, y + 3), fill=(72, 255, 190, 220))

    scan_x = int((phase * (WIDTH + 260)) - 130)
    for distance in range(-32, 33):
        alpha = max(0, 42 - abs(distance))
        draw.line((scan_x + distance, 25, scan_x + distance, HEIGHT - 25), fill=(0, 220, 255, alpha))

    rng = random.Random(404)
    for particle in range(18):
        lane_y = 46 + particle * 18
        speed = 0.7 + (particle % 5) * 0.11
        x = 545 + ((phase * speed + rng.random()) % 1) * 530
        length = 7 + particle % 4 * 4
        draw.line((x, lane_y, x + length, lane_y), fill=(74, 238, 255, 85 + particle % 3 * 35), width=1)

    frame.alpha_composite(dynamic)
    overlay_identity(frame)
    return frame


def build_animation() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    source = build_source()
    rgba_frames = [build_frame(source, index) for index in range(FRAMES)]
    palette = rgba_frames[0].convert("RGB").quantize(colors=96, method=Image.Quantize.MEDIANCUT)
    gif_frames = [palette]
    gif_frames.extend(
        frame.convert("RGB").quantize(palette=palette, dither=Image.Dither.FLOYDSTEINBERG)
        for frame in rgba_frames[1:]
    )
    gif_frames[0].save(
        OUTPUT,
        save_all=True,
        append_images=gif_frames[1:],
        duration=110,
        loop=0,
        optimize=True,
        disposal=1,
    )


if __name__ == "__main__":
    build_animation()
