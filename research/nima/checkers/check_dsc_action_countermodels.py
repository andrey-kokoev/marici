"""Check core action examples and a stronger free-segment composition test.
The actual DSC substitution theorem is checked in Agda, not simulated here.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import check_graph_action_selection as P

BASE = Path(__file__).resolve().parents[1]
x, y, z, parameter = [P.variable(i) for i in range(4)]

def substitute(poly, coordinates):
    out = {}
    for exponents, coefficient in poly.items():
        term = P.const(coefficient)
        for coord, exponent in zip(coordinates, exponents):
            term = P.multiply(term, P.power(coord, exponent))
        out = P.add(out, term)
    return out

def segment(p, length):
    length = F(length)
    if length <= 0:
        raise ValueError('segment length must be positive')
    difference = P.add(z, P.scale(-1, x))
    return length, P.scale(1/(p*length**(p-1)), P.power(difference, p))

def compose(left, right):
    l1, s1 = left
    l2, s2 = right
    sleft = substitute(s1, [x, y, y, parameter])
    sright = substitute(s2, [y, y, z, parameter])
    total = P.add(sleft, sright)
    middle = P.scale(1/(l1+l2), P.add(P.scale(l2, x), P.scale(l1, z)))
    coordinates = [x, middle, z, parameter]
    # Check the selected seam is actually stationary, as a polynomial in
    # arbitrary endpoints, not just at one numerical sample.
    residual = substitute(P.derivative(total, 1), coordinates)
    assert residual == {}
    reduced = substitute(total, coordinates)
    return l1+l2, reduced

rows = []
for p in (2, 4):
    for l1, l2 in [(F(1), F(1)), (F(1), F(2)), (F(1, 2), F(2, 3)), (F(3), F(4))]:
        reduced = compose(segment(p, l1), segment(p, l2))
        assert reduced == segment(p, l1+l2)
    for lengths in [(F(1), F(1), F(1)), (F(1), F(2), F(3)), (F(1, 2), F(2, 3), F(3, 4))]:
        a, b, c = [segment(p, l) for l in lengths]
        left = compose(compose(a, b), c)
        right = compose(a, compose(b, c))
        assert left == right == segment(p, sum(lengths))
    _, s = segment(p, F(1))
    shifted = substitute(s, [P.add(x, parameter), y, P.add(z, parameter), parameter])
    assert shifted == s
    reversed_s = substitute(s, [z, y, x, parameter])
    assert reversed_s == s
    homogeneous = substitute(s, [P.multiply(parameter, x), y, P.multiply(parameter, z), parameter])
    assert homogeneous == P.multiply(P.power(parameter, p), s)
    rows.append({'degree': p, 'stationary_composition_closed': True,
                 'bracketing_equalities': 3, 'symbolic_endpoint_pair_checks': 4,
                 'shift_and_reversal': True})

# Wrong seam selection passes ordinary function substitution, but does not
# pass the ENRICHED stationarity check.
total = P.add(substitute(segment(4, 1)[1], [x, y, y, parameter]),
              substitute(segment(4, 1)[1], [y, y, z, parameter]))
wrong_seam = substitute(P.derivative(total, 1), [x, x, z, parameter])
assert wrong_seam != {}
assert P.evaluate(wrong_seam, [0, 0, 2, 0]) == -8
# Do not conflate degree-four homogeneity with degree-two homogeneity.
s4 = segment(4, 1)[1]
dilated4 = substitute(s4, [P.multiply(parameter, x), y, P.multiply(parameter, z), parameter])
assert dilated4 != P.multiply(P.power(parameter, 2), s4)
# Check the specific nonstationary execution used by the Agda fixture:
# q=2 => phi_1=1; derivative of 8S with respect to q is 4*dS/dphi_1.
quad = P.action(P.PHI)[0]
residual = 4*P.evaluate(P.derivative(quad, 1), [0, 1, 0, 0])
assert residual == 8

files = [Path(__file__), BASE/'agda/DSCActionCountermodels.agda',
         BASE/'agda/GraphAction.agda', BASE/'checkers/check_graph_action_selection.py',
         BASE.parent/'voevodsky/resolution-net-v1/agda/ResolutionNetDependentSubstitution.agda']
packet = {
    'status': 'DSC-selection-countermodels-supported',
    'core_scope': 'Actual DSC laws checked separately by Agda; both action models type and a nonstationary output executes',
    'strengthened_interface': 'Source-free positive-length segments, stationary elimination with a derived/verified seam; not all sourced field actions',
    'families': rows,
    'nonstationary_scaled_residual': str(residual),
    'wrong_seam_rejected': True,
    'quartic_is_not_quadratic': True,
    'associativity_scope': 'Positive segment lengths only; no zero-length unit asserted',
    'conclusion': 'Core DSC does not force stationarity or quadraticity. This particular stationary-composition interface does not force quadraticity either.',
    'sha256': {str(p.relative_to(BASE.parent.parent)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
}
(BASE/'results/dsc-action-countermodels.json').write_text(json.dumps(packet, indent=2)+'\n', encoding='utf-8')
print('DSC action audit: nonstationarity remains typeable; quadratic AND quartic free-segment families pass stationary composition.')
