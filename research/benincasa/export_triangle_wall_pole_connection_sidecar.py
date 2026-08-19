"""Export degree-plus-one pole-connection images for every source relation.

The row order is exactly the pole-extension-stage-two order used by
``export_triangle_wall_dual_rows.py`` at source K-depth three.  Each record
contains one length-three normal-jet image for each wall tangent.  The images
live in the target K-depth-four ambient module.  This is a sidecar, not a
cohomology map: the Rust reducer must transport it through the identical
source elimination before taking the exact-valuation quotient.
"""

from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "research" / "benincasa" / "export_triangle_wall_pole_symbol_images.py"
spec = importlib.util.spec_from_file_location("pole_images", MODULE_PATH)
module = importlib.util.module_from_spec(spec)

# The imported exporter has a command-line main body.  Supply one harmless
# selected row and a temporary sink while loading its exact conventions.
saved_argv = sys.argv
sink = ROOT / ".ai" / "tmp" / "pole-image-import-sink.json"
sink.parent.mkdir(parents=True, exist_ok=True)
sys.argv = [str(MODULE_PATH), "--row-index", "0", "--output", str(sink)]
try:
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
finally:
    sys.argv = saved_argv
    sink.unlink(missing_ok=True)

P = module.P


def write_row(handle, row):
    handle.write(struct.pack("<I", len(row)))
    for column, value in sorted(row.items()):
        handle.write(struct.pack("<II", column, value % P))


parser = argparse.ArgumentParser()
parser.add_argument("--ambient", type=int, default=10)
parser.add_argument("--limit", type=int)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()

ordered = module.descriptors(args.ambient)
if args.limit is not None:
    ordered = ordered[: args.limit]
columns = module.target_columns(args.ambient, (2, 3, 5))

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
    f'{{"schema":"marici.triangle-wall-pole-connection-sidecar.v1",'
    f'"rows":{len(ordered)},"target_columns":{len(columns)},'
    f'"output":"{args.output}"}}'
)
