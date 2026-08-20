"""Embed a length-three quotient basis under labelled K-pole shift.

This prepares probes; it does not assert that any shift is a chain map.
Column labels are rebuilt from the frozen source presentation so low-basis
deduplication and the three normal blocks are handled exactly.
"""

from __future__ import annotations

import argparse
import contextlib
import importlib
import io
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    audit = importlib.import_module("check_rank21_occurrence_reflection_connection")

charts = audit.charts

P = charts.PRIME


def parse_row(line: str) -> dict[int, int]:
    return {
        int(column): int(value) % P
        for term in line.strip().split(",")
        if term
        for column, value in [term.split(":", 1)]
    }


def format_row(row: dict[int, int]) -> str:
    return ",".join(f"{column}:{value}" for column, value in sorted(row.items()) if value % P)


def weight(mode: str, gamma: int, k_pole: int) -> int:
    if mode in {"unscaled", "principal"}:
        return 1
    if mode == "de-rham":
        return (gamma - k_pole) % P
    raise ValueError(mode)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("basis")
    parser.add_argument("output")
    parser.add_argument("--source-depth", type=int, required=True)
    parser.add_argument("--target-depth", type=int, required=True)
    parser.add_argument("--pole-increment", type=int, choices=(0, 1), default=1)
    parser.add_argument("--append", action="store_true")
    parser.add_argument("--ambient", type=int, default=10)
    parser.add_argument("--q-depth", type=int, default=2)
    parser.add_argument("--gamma", type=int, default=5)
    parser.add_argument(
        "--mode",
        choices=("unscaled", "principal", "de-rham"),
        nargs="+",
        required=True,
    )
    args = parser.parse_args()
    if args.target_depth < args.source_depth + args.pole_increment:
        raise ValueError("target depth cannot retain the shifted source labels")
    if args.pole_increment == 0 and any(mode != "unscaled" for mode in args.mode):
        raise ValueError("zero-increment inclusion supports only unscaled mode")

    old = (charts.K_DEPTH, charts.Q_DEPTH, charts.AMBIENT)
    try:
        charts.K_DEPTH, charts.Q_DEPTH, charts.AMBIENT = (
            args.source_depth,
            args.q_depth,
            args.ambient,
        )
        source = charts.presentation(charts.base.fiber_data, charts.SOURCE_POINT, charts.SOURCE_NAMES)
        charts.K_DEPTH = args.target_depth
        target = charts.presentation(charts.base.fiber_data, charts.SOURCE_POINT, charts.SOURCE_NAMES)
    finally:
        charts.K_DEPTH, charts.Q_DEPTH, charts.AMBIENT = old

    source_columns = len(source["ordered_columns"])
    target_columns = len(target["ordered_columns"])
    source_lines = [
        line
        for line in Path(args.basis).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    output_lines = []
    for mode in args.mode:
        for line in source_lines:
            shifted: dict[int, int] = {}
            for global_column, coefficient in parse_row(line).items():
                block, within = divmod(global_column, source_columns)
                label = source["ordered_columns"][within]
                k_pole, *tail = label
                shifted_label = (k_pole + args.pole_increment, *tail)
                target_within = target["columns"][shifted_label]
                target_global = block * target_columns + target_within
                shifted[target_global] = (
                    shifted.get(target_global, 0)
                    + coefficient * weight(mode, args.gamma, k_pole)
                ) % P
            output_lines.append(format_row(shifted))
    output_path = Path(args.output)
    rendered = "\n".join(output_lines) + "\n"
    if args.append:
        with output_path.open("a", encoding="utf-8") as stream:
            stream.write(rendered)
    else:
        output_path.write_text(rendered, encoding="utf-8")
    print(
        f"modes={','.join(args.mode)} probes_per_mode={len(source_lines)} "
        f"pole_increment={args.pole_increment} source_columns={source_columns} "
        f"target_columns={target_columns} append={args.append} output={args.output}"
    )


if __name__ == "__main__":
    main()
