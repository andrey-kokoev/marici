"""Adaptive dyadic box-cover experiment for Chart 1."""
import argparse
import json
import time
from fractions import Fraction as F
from pathlib import Path

from theta_fixedpoint_interval import (
    FixedDual, FixedInterval, scaled_derivative_numerators)

Q0, Q1 = F(3, 10), F(7, 16)
Y0, Y1 = F(1, 1000), F(1, 28)


def evaluate(box):
    q0, q1, y0, y1, depth = box
    q = FixedDual(FixedInterval.enclosing(q0, q1), dq=1)
    y = FixedDual(FixedInterval.enclosing(y0, y1), dy=1)
    try:
        nq, ny = scaled_derivative_numerators(q, y)
    except ValueError:
        return None
    return nq.lo, ny.hi


def children(box):
    q0, q1, y0, y1, depth = box
    q_relative = (q1 - q0) / (Q1 - Q0)
    y_relative = (y1 - y0) / (Y1 - Y0)
    if q_relative >= y_relative:
        mid = (q0 + q1) / 2
        return [(q0, mid, y0, y1, depth + 1),
                (mid, q1, y0, y1, depth + 1)]
    mid = (y0 + y1) / 2
    return [(q0, q1, y0, mid, depth + 1),
            (q0, q1, mid, y1, depth + 1)]


def run(max_evaluations):
    stack = [(Q0, Q1, Y0, Y1, 0)]
    accepted = []
    evaluations = 0
    max_depth = 0
    started = time.perf_counter()
    while stack and evaluations < max_evaluations:
        box = stack.pop()
        enclosure = evaluate(box)
        evaluations += 1
        max_depth = max(max_depth, box[4])
        if enclosure is not None and enclosure[0] > 0 and enclosure[1] < 0:
            accepted.append((box, enclosure[0], enclosure[1]))
        else:
            stack.extend(children(box))
    elapsed = time.perf_counter() - started
    worst_q_record = min(accepted, key=lambda x: x[1], default=None)
    worst_y_record = max(accepted, key=lambda x: x[2], default=None)
    worst_q = None if worst_q_record is None else worst_q_record[1]
    worst_y = None if worst_y_record is None else worst_y_record[2]
    box_text = lambda record: None if record is None else [str(v) for v in record[0]]
    return {
        "status": "complete" if not stack else "budget_exhausted",
        "evaluations": evaluations,
        "accepted_cells": len(accepted),
        "pending_cells": len(stack),
        "max_depth": max_depth,
        "elapsed_seconds": elapsed,
        "evaluations_per_second": evaluations / elapsed,
        "worst_accepted_dq_lower_scaled": None if worst_q is None else str(worst_q),
        "worst_accepted_dq_cell": box_text(worst_q_record),
        "worst_accepted_dy_upper_scaled": None if worst_y is None else str(worst_y),
        "worst_accepted_dy_cell": box_text(worst_y_record),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-evaluations", type=int, default=5000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.max_evaluations)
    text = json.dumps(result, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n")
    print(text)
