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


class StrictTargetColumns(dict):
    """Refuse the silent boundary truncation used by exploratory exporters."""

    def get(self, key, default=None):
        if key not in self:
            raise RuntimeError(f"target column set omits connection-image label {key!r}")
        return super().get(key, default)


class AuditedTargetColumns(dict):
    """Record every requested label while preserving exploratory lookup."""

    def __init__(self, values):
        super().__init__(values)
        self.requested = set()
        self.missing = set()

    def get(self, key, default=None):
        self.requested.add(key)
        if key not in self:
            self.missing.add(key)
        return super().get(key, default)


def descriptors(ambient, source_k_depth):
    levels_all = list(product(range(1, 3), repeat=len(module.NAMES)))
    de_rham = [
        ("de_rham", k_pole, (1,) * len(module.NAMES), exponent, axis)
        for k_pole in range(source_k_depth)
        for axis in range(2)
        for exponent in module.base.monomials_at_most(ambient)
    ]
    principal = [
        ("principal", k_pole, levels, exponent, None)
        for k_pole in range(source_k_depth)
        for levels in levels_all
        for exponent in module.base.monomials_at_most(ambient - 4)
    ]
    marked = [
        ("marked", k_pole, levels, exponent, marked_index)
        for marked_index in range(len(module.NAMES))
        for k_pole in range(source_k_depth + 1)
        for levels in levels_all
        if levels[marked_index] != 2
        for exponent in module.base.monomials_at_most(ambient - 1)
    ]

    previous_depth = source_k_depth - 1
    old = [item for item in de_rham if item[1] < previous_depth]
    old += [item for item in principal if item[1] < previous_depth]
    old += [item for item in marked if item[1] < source_k_depth]
    new_de_rham = [item for item in de_rham if item[1] == previous_depth]
    new_principal = [item for item in principal if item[1] == previous_depth]
    new_marked = [
        item
        for marked_index in range(len(module.NAMES))
        for item in marked
        if item[4] == marked_index and item[1] == source_k_depth
    ]
    return old + new_de_rham + new_principal + new_marked


def write_row(handle, row):
    handle.write(struct.pack("<I", len(row)))
    for column, value in sorted(row.items()):
        handle.write(struct.pack("<II", column, value % P))


def target_columns(ambient, k_depth):
    old = (
        module.charts.AMBIENT,
        module.charts.CUTOFF,
        module.charts.K_DEPTH,
        module.charts.Q_DEPTH,
    )
    module.charts.AMBIENT, module.charts.CUTOFF = ambient, 6
    module.charts.K_DEPTH, module.charts.Q_DEPTH = k_depth, 2
    try:
        return module.charts.presentation(
            module.base.fiber_data, (2, 3, 5), module.charts.SOURCE_NAMES
        )["columns"]
    finally:
        (
            module.charts.AMBIENT,
            module.charts.CUTOFF,
            module.charts.K_DEPTH,
            module.charts.Q_DEPTH,
        ) = old


parser = argparse.ArgumentParser()
parser.add_argument("--ambient", type=int, default=10)
parser.add_argument("--source-k-depth", type=int, default=3)
parser.add_argument(
    "--target-ambient",
    type=int,
    help="target column cutoff; defaults to the source ambient degree",
)
parser.add_argument("--output", type=Path, required=True)
parser.add_argument("--expect-rows", type=int)
parser.add_argument("--census-only", action="store_true")
parser.add_argument("--strict-target", action="store_true")
parser.add_argument("--audit-target-only", action="store_true")
args = parser.parse_args()
target_ambient = args.ambient if args.target_ambient is None else args.target_ambient

ordered = descriptors(args.ambient, args.source_k_depth)
if args.expect_rows is not None and len(ordered) != args.expect_rows:
    raise RuntimeError(
        f"filtered descriptor census {len(ordered)} != expected {args.expect_rows}"
    )
columns = target_columns(target_ambient, args.source_k_depth + 1)
if args.audit_target_only:
    columns = AuditedTargetColumns(columns)
elif args.strict_target:
    columns = StrictTargetColumns(columns)

if args.audit_target_only:
    for descriptor in ordered:
        for tangent in ("T1", "T2"):
            module.normal_image(descriptor, tangent, target_ambient, columns)
    first_complete = None
    for candidate in range(target_ambient, target_ambient + 32):
        candidate_columns = target_columns(candidate, args.source_k_depth + 1)
        if all(label in candidate_columns for label in columns.requested):
            first_complete = candidate
            break
    missing_degrees = [sum(label[-1]) for label in columns.missing]
    audit_result = (
        f'{{"schema":"marici.triangle-wall-target-label-audit.v1",'
        f'"source_ambient":{args.ambient},"source_k_depth":{args.source_k_depth},'
        f'"target_k_depth":{args.source_k_depth + 1},'
        f'"tested_target_ambient":{target_ambient},'
        f'"source_rows":{len(ordered)},"requested_labels":{len(columns.requested)},'
        f'"missing_labels":{len(columns.missing)},'
        f'"missing_min_monomial_degree":{min(missing_degrees) if missing_degrees else 0},'
        f'"missing_max_monomial_degree":{max(missing_degrees) if missing_degrees else 0},'
        f'"first_complete_target_ambient":{first_complete if first_complete is not None else "null"}}}'
    )
    args.output.write_text(audit_result + "\n", encoding="utf-8")
    print(audit_result)
    raise SystemExit(0)

if args.census_only:
    print(
        f'{{"schema":"marici.triangle-wall-filtered-connection-census.v1",'
        f'"source_ambient":{args.ambient},"target_ambient":{target_ambient},'
        f'"rows":{len(ordered)},"target_columns":{len(columns)},'
        f'"strict_target":{str(args.strict_target).lower()}}}'
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
                module.normal_image(descriptor, tangent, target_ambient, columns),
            )
        if (index + 1) % 1000 == 0:
            print(f"exported {index + 1}/{len(ordered)}", file=sys.stderr)

print(
    f'{{"schema":"marici.triangle-wall-filtered-connection-sidecar.v1",'
    f'"source_ambient":{args.ambient},"target_ambient":{target_ambient},'
    f'"rows":{len(ordered)},"target_columns":{len(columns)},'
    f'"strict_target":{str(args.strict_target).lower()},'
    f'"output":"{args.output}"}}'
)
