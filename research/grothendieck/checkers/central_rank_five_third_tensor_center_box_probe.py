"""Probe correlated center-interval boxes for rank-five tensor uniformization."""
import json
from decimal import Decimal as D
from pathlib import Path

import central_rank_five_third_tensor_interval_anchor as T

ROOT = Path(__file__).parents[1]


def main():
    boxes = [
        [('0', '.01')] * 5,
        [('0', '.005')] * 5,
        [('.005', '.01')] * 5,
    ]
    results = []
    for box in boxes:
        try:
            row = T.evaluate(box)
            row['center_box_certified'] = True
        except (ArithmeticError, AssertionError, ValueError, ZeroDivisionError) as error:
            row = {'anchor_interval': box, 'center_box_certified': False,
                   'failure': type(error).__name__ + ': ' + str(error)}
        results.append(row)
    result = {'boxes': results, 'probe_only': True, 'rh_proved': False}
    output = ROOT / 'results' / 'central-rank-five-third-tensor-center-box-probe.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
