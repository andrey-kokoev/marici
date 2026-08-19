"""Export pole-connection images in the complete K-depth-three filtration order.

The older Benincasa sidecar intentionally stops after the new de Rham and
principal strata.  This companion retains the five new marked strata too, so
its row order agrees with ``export_triangle_wall_dual_rows.py --k-depth 3
--q-depth 2 --pole-extension-filtration``.
"""

from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import struct
import sys
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = (
    ROOT / "research" / "benincasa" / "export_triangle_wall_pole_symbol_images.py"
)
spec = importlib.util.spec_from_file_location("pole_images", MODULE_PATH)
module = importlib.util.module_from_spec(spec)

# The imported module has a command-line body.  Load its exact conventions
# through one harmless row and remove the temporary import sink immediately.
saved_argv = sys.argv
sink = ROOT / ".ai" / "tmp" / "filtered-pole-image-import-sink.json"
sink.parent.mkdir(parents=True, exist_ok=True)
sys.argv = [str(MODULE_PATH), "--row-index", "0", "--output", str(sink)]
try:
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
finally:
    sys.argv = saved_argv
    sink.unlink(missing_ok=True)

P = module.P


def descriptors(ambient):
    levels_all = list(product(range(1, 3), repeat=len(module.NAMES)))
    de_rham = [
        ("de_rham", k_pole, (1,) * len(module.NAMES), exponent, axis)
        for k_pole in range(3)
        for axis in range(2)
        for exponent in module.base.monomials_at_most(ambient)
    ]
    principal = [
        ("principal", k_pole, levels, exponent, None)
        for k_pole in range(3)
        for levels in levels_all
        for exponent in module.base.monomials_at_most(ambient - 4)
    ]
    marked = [
        ("marked", k_pole, levels, exponent, marked_index)
        for marked_index in range(len(module.NAMES))
        for k_pole in range(4)
        for levels in levels_all
        if levels[marked_index] != 2
        for exponent in module.base.monomials_at_most(ambient - 1)
    ]

    old = [item for item in de_rham if item[1] < 2]
    old += [item for item in principal if item[1] < 2]
    old += [item for item in marked if item[1] < 3]
    new_de_rham = [item for item in de_rham if item[1] == 2]
    new_principal = [item for item in principal if item[1] == 2]
    new_marked = [
        item
        for marked_index in range(len(module.NAMES))
        for item in marked
        if item[4] == marked_index and item[1] == 3
    ]
    return old + new_de_rham + new_principal + new_marked


def write_row(handle, row):
    handle.write(struct.pack("<I", len(row)))
    for column, value in sorted(row.items()):
        handle.write(struct.pack("<II", column, value % P))


parser = argparse.ArgumentParser()
parser.add_argument("--ambient", type=int, default=10)
parser.add_argument("--output", type=Path, required=True)
parser.add_argument("--expect-rows", type=int, default=20684)
parser.add_argument("--census-only", action="store_true")
args = parser.parse_args()

ordered = descriptors(args.ambient)
if len(ordered) != args.expect_rows:
    raise RuntimeError(
        f"filtered descriptor census {len(ordered)} != expected {args.expect_rows}"
    )
columns = module.target_columns(args.ambient, (2, 3, 5))

if args.census_only:
    print(
        f'{{"schema":"marici.triangle-wall-filtered-connection-census.v1",'
        f'"rows":{len(ordered)},"target_columns":{len(columns)}}}'
    )
    raise SystemExit(0)

args.output.parent.mkdir(parents=True, exist_ok=True)
with args.output.open("wb") as handle:
    handle.write(b"MRCICON1")
    handle.write(struct.pack("<IIII", P, args.ambient, len(ordered), len(columns)))
    for index, descriptor in enumerate(ordered):
        for tangent in ("T1", "T2"):
            write_row(
                handle,
                module.normal_image(descriptor, tangent, args.ambient, columns),
            )
        if (index + 1) % 1000 == 0:
            print(f"exported {index + 1}/{len(ordered)}", file=sys.stderr)

print(
    f'{{"schema":"marici.triangle-wall-filtered-connection-sidecar.v1",'
    f'"rows":{len(ordered)},"target_columns":{len(columns)},'
    f'"output":"{args.output}"}}'
)
