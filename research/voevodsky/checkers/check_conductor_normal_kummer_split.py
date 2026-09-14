#!/usr/bin/env python3
"""Verify first-order splitting of conductor Kummer roots normal to E=0."""
from hashlib import sha256
from pathlib import Path
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / 'research/voevodsky/conductor_total_energy_normal_splits_the_two_kummer_parameters_at_first_order.md'
PARAM = ROOT / 'research/voevodsky/common_kummer_parameter_exists_on_total_energy_specialization.md'
RESULT = ROOT / 'research/voevodsky/results/conductor_normal_kummer_split.json'
x, y, E = s.symbols('x y E', nonzero=True)
D1 = 4*x*(x*y**2 + 2*E*x*y - E**2*(x + 2*y - E))
D2 = 4*y*(x**2*y + 2*E*x*y - E**2*(2*x + y - E))
diff = s.factor(D1-D2)
d_diff = s.simplify(s.diff(diff, E).subs(E, 0))
Y0 = 2*x*y
root_split = s.simplify(d_diff/(2*Y0))
text = PACKET.read_text(encoding='utf-8')
checks = {
    'difference_factorization': s.simplify(diff - 4*E*(x-y)*(E**2-E*(x+y)+2*x*y)) == 0,
    'common_special_fiber': s.simplify(D1.subs(E, 0)-4*x**2*y**2) == 0 and s.simplify(D2.subs(E, 0)-4*x**2*y**2) == 0,
    'normal_discriminant_split': d_diff == 8*x*y*(x-y),
    'oriented_root_split': root_split == 2*(x-y),
    'generic_split_nonzero': s.simplify(root_split.subs({x: 2, y: 1})) != 0,
    'symmetric_locus_exception': s.simplify(root_split.subs(x, y)) == 0,
    'different_specialization_retained': 'different specialization and cannot be silently added' in text,
    'two_copy_gate': 'two relative nearby-cycle maps with separate' in text,
}
checks = {k: bool(v) for k, v in checks.items()}
result = {
    'schema': 'marici.voevodsky.conductor-normal-kummer-split.v1',
    'packet_sha256': sha256(PACKET.read_bytes()).hexdigest(),
    'parameter_packet_sha256': sha256(PARAM.read_bytes()).hexdigest(),
    'discriminant_difference': str(diff),
    'normal_difference_at_E0': str(d_diff),
    'oriented_root_difference_at_E0': str(root_split),
    'checks': checks,
    'passed': all(checks.values()),
    'disposition': {
        'conductor_normal_coordinate': 'E',
        'single_common_kummer_normal_lift': 'obstructed for x!=y',
        'required_model': 'two wall-labelled relative normal maps glued on special fiber',
    },
}
RESULT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'passed': result['passed'], 'checks': checks, 'disposition': result['disposition']}))
raise SystemExit(0 if result['passed'] else 1)
