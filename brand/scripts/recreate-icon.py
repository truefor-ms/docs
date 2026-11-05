"""Reconstruct the Trueforms icon from measured geometry, without reading assets.

Source measurements: master handoff v2, sections 03-05 (PDF pages 5-7).
Run with Python 3; only the standard library is required.
"""

from pathlib import Path


STROKE = 6.5
PAGE_WIDTH = 96.0
PAGE_HEIGHT = 128.0
PAGE_CORNER = 10.0
FOLD_SIZE = 32.0
FOLD_CORNER = 8.0
RIGHT_EDGE_HEIGHT = 78.0
BOTTOM_EDGE_WIDTH = 46.0
ROW_INSET = 20.0
ROW_PITCH = 20.0
ROW_LENGTHS = (26.0, 56.0, 56.0, 26.0)
CHECK_SHORT_RUN = 14.0
CHECK_LONG_RUN = 26.0
COLOR = "#16765C"


def number(value):
    return format(value, ".12g")


def point(x, y):
    return f"{number(x)},{number(y)}"


def rounded_turn(start, control, end):
    """Represent the specified quadratic turn as an equivalent cubic curve."""
    first = tuple(a + (b - a) * 2 / 3 for a, b in zip(start, control))
    second = tuple(a + (b - a) * 2 / 3 for a, b in zip(end, control))
    return f"C {point(*first)} {point(*second)} {point(*end)}"


def build_svg():
    # Normalize the entire construction to its painted bounds, including paths.
    # Half a stroke separates the page centerline from the canvas edges.
    left = top = STROKE / 2
    right, bottom = left + PAGE_WIDTH, top + PAGE_HEIGHT
    fold_x, fold_y = right - FOLD_SIZE, top + FOLD_SIZE

    # Trace from the open right endpoint toward the open bottom endpoint.
    outline = [
        f"M {point(right, top + RIGHT_EDGE_HEIGHT)}",
        f"L {point(right, fold_y)} {point(fold_x, top)}",
        f"L {point(left + PAGE_CORNER, top)}",
        rounded_turn((left + PAGE_CORNER, top), (left, top),
                     (left, top + PAGE_CORNER)),
        f"L {point(left, bottom - PAGE_CORNER)}",
        rounded_turn((left, bottom - PAGE_CORNER), (left, bottom),
                     (left + PAGE_CORNER, bottom)),
        f"L {point(left + BOTTOM_EDGE_WIDTH, bottom)}",
    ]
    fold = [
        f"M {point(fold_x, top)} L {point(fold_x, fold_y - FOLD_CORNER)}",
        rounded_turn((fold_x, fold_y - FOLD_CORNER), (fold_x, fold_y),
                     (fold_x + FOLD_CORNER, fold_y)),
        f"L {point(right, fold_y)}",
    ]
    rows = []
    for index, length in enumerate(ROW_LENGTHS):
        x, y = left + ROW_INSET, fold_y + index * ROW_PITCH
        rows.append(f"M {point(x, y)} L {point(x + length, y)}")

    check_bottom_x = right - CHECK_LONG_RUN
    check = [
        f"M {point(check_bottom_x - CHECK_SHORT_RUN, bottom - CHECK_SHORT_RUN)}",
        f"L {point(check_bottom_x, bottom)}",
        f"L {point(right, bottom - CHECK_LONG_RUN)}",
    ]
    groups = (outline, fold, rows, check)
    paths = "\n".join(f'    <path d="{" ".join(commands)}"/>' for commands in groups)
    width, height = PAGE_WIDTH + STROKE, PAGE_HEIGHT + STROKE
    return f'''<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {number(width)} {number(height)}" width="{number(width)}" height="{number(height)}"
     role="img" aria-label="Trueforms">
  <g fill="none" stroke="{COLOR}" stroke-width="{number(STROKE)}"
     stroke-linecap="round" stroke-linejoin="round">
{paths}
  </g>
</svg>
'''


if __name__ == "__main__":
    destination = Path(__file__).resolve().parents[1] / "recreated/trueforms-icon.svg"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(build_svg(), encoding="utf-8", newline="\n")
    print(destination)
