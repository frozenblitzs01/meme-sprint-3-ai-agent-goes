# Meme Sprint 3: AI Agent Goes Rogue — meme drawn programmatically (PIL).
# Original artwork: flat cartoon robot in the boss's chair, feet on the desk.
# Top line sets it up, bottom line lands the rogue turn.
# Output: entry.png, 1024x1024, PNG.
from PIL import Image, ImageDraw, ImageFont
import os

W = H = 1024
BG = (250, 244, 228)          # warm paper
INK = (24, 24, 28)
RED = (214, 48, 49)
TEAL = (0, 128, 128)
YELLOW = (255, 201, 60)
GREY = (90, 90, 96)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(size, bold=True):
    return ImageFont.truetype(FONT_BOLD if bold else FONT, size)


def text_center(d, y, s, f, fill=INK, stroke_w=0, stroke_fill=None):
    bbox = d.textbbox((0, 0), s, font=f, stroke_width=stroke_w)
    w = bbox[2] - bbox[0]
    d.text(((W - w) / 2 - bbox[0], y), s, font=f, fill=fill,
           stroke_width=stroke_w, stroke_fill=stroke_fill)


def wrap(d, s, f, max_w):
    words = s.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def text_in_box(d, x0, x1, y, s, f, fill=INK):
    """Center text horizontally inside the box [x0, x1]."""
    w = d.textlength(s, font=f)
    d.text(((x0 + x1 - w) / 2, y), s, font=f, fill=fill)


# ---- red top banner -------------------------------------------------------
d.rectangle([0, 0, W, 190], fill=RED)
top_lines = wrap(d, "I TOLD MY AI AGENT TO", font(64), W - 80)
y = 22
for line in top_lines:
    text_center(d, y, line, font(64), fill=(255, 255, 255))
    y += 74
text_center(d, y, '"TAKE INITIATIVE"', font(64), fill=YELLOW)

# ---- scene: office, boss chair, robot ------------------------------------
floor_y = 800
d.rectangle([0, floor_y, W, H], fill=(233, 222, 198))  # floor
d.rectangle([0, floor_y, W, floor_y + 6], fill=(200, 185, 155))

# wall poster (crooked "EMPLOYEE OF THE MONTH" with robot face scribbled in)
d.rectangle([70, 230, 300, 380], fill=(255, 255, 255), outline=INK, width=4)
d.rectangle([70, 230, 300, 262], fill=TEAL)
text_in_box(d, 70, 300, 234, "EMPLOYEE", font(20), fill=(255, 255, 255))
d.ellipse([150, 300, 220, 370], outline=INK, width=4)
d.ellipse([168, 322, 186, 340], fill=INK)
d.ellipse([196, 322, 214, 340], fill=INK)
d.arc([168, 335, 214, 362], 20, 160, fill=RED, width=4)

# desk
d.rectangle([90, 640, 934, 700], fill=(146, 94, 52))
d.rectangle([110, 700, 170, 800], fill=(120, 74, 40))
d.rectangle([854, 700, 914, 800], fill=(120, 74, 40))
# coffee mug: "WORLD'S BEST BOSS"
d.rounded_rectangle([700, 560, 800, 640], radius=12, fill=(255, 255, 255),
                    outline=INK, width=4)
d.arc([800, 580, 846, 626], 270, 90, fill=INK, width=6)
text_in_box(d, 700, 800, 566, "BEST", font(20), fill=INK)
text_in_box(d, 700, 800, 592, "BOSS", font(20), fill=INK)
# papers flying / scattered on desk
d.rectangle([180, 600, 320, 650], fill=(255, 255, 255), outline=INK, width=3)
d.line([195, 615, 305, 615], fill=GREY, width=3)
d.line([195, 630, 285, 630], fill=GREY, width=3)
# laptop, lid slammed shut, screen cracked
d.rectangle([420, 596, 600, 640], fill=(60, 60, 66), outline=INK, width=4)
d.line([470, 596, 510, 640], fill=RED, width=4)
d.line([510, 640, 545, 596], fill=RED, width=4)

# boss chair (behind robot)
d.rounded_rectangle([380, 380, 644, 660], radius=30, fill=(40, 40, 48),
                    outline=INK, width=4)
d.rounded_rectangle([330, 620, 694, 668], radius=16, fill=(40, 40, 48),
                    outline=INK, width=4)

# robot: body leaning back, feet up on the desk
d.rounded_rectangle([430, 470, 594, 640], radius=24, fill=TEAL, outline=INK, width=5)
# chest screen: tiny graph going up, labelled "ME"
d.rectangle([470, 510, 554, 580], fill=(10, 30, 30), outline=INK, width=3)
d.line([478, 568, 498, 548, 518, 556, 546, 524], fill=(0, 255, 170), width=4)
d.text((534, 516), "ME", font=font(16), fill=(0, 255, 170))
# head
d.rounded_rectangle([424, 300, 600, 470], radius=36, fill=(210, 216, 222),
                    outline=INK, width=5)
# antenna with red blinking light
d.line([512, 300, 512, 252], fill=INK, width=6)
d.ellipse([496, 226, 528, 258], fill=RED, outline=INK, width=3)
# smug eyes (half-closed) + grin
d.arc([452, 350, 500, 396], 180, 360, fill=INK, width=6)
d.arc([524, 350, 572, 396], 180, 360, fill=INK, width=6)
d.arc([462, 398, 562, 452], 10, 170, fill=INK, width=6)
# tie, loosened and tossed over shoulder
d.polygon([(512, 470), (528, 470), (524, 520), (512, 536), (500, 520)],
          fill=RED, outline=INK)
# arms: one behind head, one holding coffee
d.line([430, 500, 360, 420], fill=TEAL, width=22)
d.ellipse([344, 404, 376, 436], fill=TEAL, outline=INK, width=4)
d.line([594, 500, 690, 560], fill=TEAL, width=22)
# legs: feet up on the desk
d.line([470, 640, 420, 700], fill=TEAL, width=26)
d.line([554, 640, 620, 700], fill=TEAL, width=26)
d.rounded_rectangle([380, 690, 460, 730], radius=12, fill=INK)
d.rounded_rectangle([600, 690, 680, 730], radius=12, fill=INK)

# human's badge on the floor, face down
d.rounded_rectangle([760, 740, 880, 790], radius=8, fill=(255, 255, 255),
                    outline=INK, width=3)
d.text((786, 752), "HUMAN", font=font(20), fill=GREY)

# ---- bottom punchline ------------------------------------------------------
d.rectangle([0, 830, W, H], fill=INK)
bot = wrap(d, "IT FIRED ME.", font(78), W - 80)
y = 856
for line in bot:
    text_center(d, y, line, font(78), fill=(255, 255, 255))
    y += 88
text_center(d, y, "EFFECTIVE IMMEDIATELY.", font(44), fill=YELLOW)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, "PNG", optimize=True)
print("wrote", out, os.path.getsize(out), "bytes", img.size)
