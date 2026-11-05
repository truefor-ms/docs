"""Build the complete primary B logo from font outlines and handoff measurements.

No approved logo SVG, PNG, or path string is read. The icon comes from the
independent parametric reconstruction; the letters and period come from the
pinned upstream Nimbus Roman font. Requires fontTools (see requirements file).
"""

import hashlib
import importlib.util
import json
from pathlib import Path
import xml.etree.ElementTree as ET

from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "reconstruction-sources/nimbus-roman"
OUTPUT = ROOT / "recreated"
FONT_SHA256 = "fd41669443616a7ae890c42e53a58f47fa24a940fd1e367acaff665cf5b6e9d8"
AFM_SHA256 = "e476212c416039aa9805f20d945e2b3a522be5de15125cb566d257482379ccd9"
FONT_SIZE = 125.13888888888889
EXTRA_GAPS = (5.0, 4.0, 4.5, 3.0, 4.0, 4.0, 6.5, 3.5)
ICON_SCALE = 0.75
ICON_WORDMARK_GAP = 28.5
MARGIN = 0.01
WORD = "trueforms"
DOT_CENTER_LOCAL = (361.4328472222222, -28.78194444444444)


def read_pinned(path, digest):
    content = path.read_bytes()
    if hashlib.sha256(content).hexdigest() != digest:
        raise ValueError(f"Unexpected source version: {path.name}")
    return content


def glyph_bounds(glyphs, name):
    pen = BoundsPen(glyphs)
    glyphs[name].draw(pen)
    return pen.bounds


def union(bounds):
    return [min(b[0] for b in bounds), min(b[1] for b in bounds),
            max(b[2] for b in bounds), max(b[3] for b in bounds)]


def main():
    font_path = SOURCES / "NimbusRoman-Regular.otf"
    read_pinned(font_path, FONT_SHA256)
    metrics = read_pinned(SOURCES / "NimbusRoman-Regular.afm", AFM_SHA256)
    font = TTFont(font_path)
    glyphs = font.getGlyphSet()
    scale = FONT_SIZE / font["head"].unitsPerEm
    kerning = {}
    for line in metrics.decode("ascii").splitlines():
        if line.startswith("KPX "):
            _, left, right, adjustment = line.split()
            kerning[left, right] = float(adjustment)

    # The period is not inserted into this word's advance-width sequence.
    letters, boxes = [], []
    cursor = extra = 0.0
    for index, letter in enumerate(WORD):
        x = cursor * scale + extra
        xmin, ymin, xmax, ymax = glyph_bounds(glyphs, letter)
        boxes.append((x + xmin * scale, -ymax * scale,
                      x + xmax * scale, -ymin * scale))
        letters.append({"letter": letter, "offset": x,
                        "added_spacing": extra,
                        "following_kern_font_units": kerning.get((letter, WORD[index + 1]), 0)
                        if index + 1 < len(WORD) else 0})
        cursor += glyphs[letter].width
        if index < len(EXTRA_GAPS):
            cursor += kerning.get((letter, WORD[index + 1]), 0)
            extra += EXTRA_GAPS[index]

    local = union(boxes)
    icon_width = 102.5 * ICON_SCALE
    icon_height = 134.5 * ICON_SCALE
    baseline_x = MARGIN + icon_width + ICON_WORDMARK_GAP - local[0]
    baseline_y = MARGIN + icon_height / 2 - (local[1] + local[3]) / 2
    width = baseline_x + local[2] + MARGIN
    height = icon_height + MARGIN * 2

    def outline(name, x, y):
        pen = SVGPathPen(glyphs, ntos=lambda value: format(value, ".12g"))
        glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, x, y)))
        return pen.getCommands()

    paths = [f'    <path d="{outline(item["letter"], baseline_x + item["offset"], baseline_y)}"/>'
             for item in letters]
    px0, py0, px1, py1 = glyph_bounds(glyphs, "period")
    period_center_x = (px0 + px1) * scale / 2
    period_center_y = -(py0 + py1) * scale / 2
    dot_x = baseline_x + DOT_CENTER_LOCAL[0] - period_center_x
    dot_y = baseline_y + DOT_CENTER_LOCAL[1] - period_center_y
    dot = outline("period", dot_x, dot_y)

    module_spec = importlib.util.spec_from_file_location("recreated_icon", ROOT / "scripts/recreate-icon.py")
    icon_module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(icon_module)
    ns = {"svg": "http://www.w3.org/2000/svg"}
    icon_root = ET.fromstring(icon_module.build_svg())
    icon_paths = "\n".join(f'    <path d="{p.attrib["d"]}"/>'
                           for p in icon_root.findall(".//svg:path", ns))
    wordmark_paths = "\n".join(paths)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {width:.12g} {height:.12g}" width="{width:.12g}" height="{height:.12g}"
     role="img" aria-label="Trueforms">
  <g transform="translate({MARGIN} {MARGIN}) scale({ICON_SCALE})"
     fill="none" stroke="#16765C" stroke-width="6.5"
     stroke-linecap="round" stroke-linejoin="round">
{icon_paths}
  </g>
  <g fill="#183C32">
{wordmark_paths}
  </g>
  <g fill="#AFBDB0" aria-hidden="true">
    <path d="{dot}"/>
  </g>
</svg>
'''
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "trueforms-logo.svg").write_text(svg, encoding="utf-8", newline="\n")
    report = {
        "variant": "B", "wordmark": WORD,
        "method": "Outline upstream Nimbus Roman Regular glyphs; apply AFM kerning and handoff pair adjustments; independently place the period and reconstructed icon.",
        "reads_approved_logo_assets": False,
        "font_sha256": FONT_SHA256, "afm_sha256": AFM_SHA256,
        "font_units_per_em": font["head"].unitsPerEm,
        "font_size": FONT_SIZE, "letters": letters,
        "wordmark_local_bounds": local,
        "baseline_normalized": [baseline_x, baseline_y],
        "icon_wordmark_gap": ICON_WORDMARK_GAP,
        "dot_center_normalized": [baseline_x + DOT_CENTER_LOCAL[0], baseline_y + DOT_CENTER_LOCAL[1]],
        "dot_size": [(px1 - px0) * scale, (py1 - py0) * scale],
        "viewBox": [0, 0, width, height],
        "colors": {"icon": "#16765C", "wordmark": "#183C32", "dot": "#AFBDB0"},
    }
    (OUTPUT / "logo-construction.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(report, indent=2))
    font.close()


if __name__ == "__main__":
    main()
