"""Independent state-index transport using existing shared-leg DG generators.

No new witnesses: h_i,k_j and their products come from the existing checker.
Distinguishes natural leg witnesses from canonical reference differences.
"""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import hashlib
import json
import runpy
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with redirect_stdout(StringIO()):
    M = runpy.run_path(str(HERE/'check_witnessed_reference_reanchoring.py'))
plus, minus, mul, delta, word = (M[k] for k in ('plus', 'minus', 'mul', 'delta', 'word'))
anchors, hs = M['anchors'], M['hs']


def difference(a, b): return plus(a, minus(b))
def h(i): return word(f'sh{i}') if i else {}
def k(j): return word(f'sk{j}') if j else {}
def x(i): return word(f'sx{i}')
def y(j): return word(f'sy{j}')
def D(i, j): return anchors[f's:{i}:{j}']
def H(i, j): return hs[f's:{i}:{j}']


def main():
    counts = {'left_changes': 0, 'right_changes': 0, 'mixed_squares': 0,
              'nonzero_mixed_witness_boundaries': 0, 'reference_comparison_fillers': 0}
    for i in range(4):
        for j in range(4):
            for g in range(4):
                ip = i ^ g
                a = difference(h(ip), h(i))
                left = mul(y(j), a)
                right = mul(difference(k(j ^ g), k(j)), x(i))
                assert delta(left) == difference(D(ip, j), D(i, j))
                assert delta(right) == difference(D(i, j ^ g), D(i, j))
                assert (ip ^ j) == ((i ^ j) ^ g)
                assert (i ^ (j ^ g)) == ((i ^ j) ^ g)
                if g:
                    assert left and right
                    assert delta(left) and delta(right)
                counts['left_changes'] += 1
                counts['right_changes'] += 1
                # Direct reference changes can also cross q-fibres.
                old = M['reanchor'](M['initial'], f's:{i}:{j}')
                for target in ((ip, j), (i, j ^ g)):
                    new = M['reanchor'](old, f's:{target[0]}:{target[1]}')
                    direct = M['reanchor'](M['initial'], f's:{target[0]}:{target[1]}')
                    assert M['payload'](new) == M['payload'](direct)
                for g2 in range(4):
                    ipp = ip ^ g2
                    assert plus(left, mul(y(j), difference(h(ipp), h(ip)))) == mul(y(j), difference(h(ipp), h(i)))
                    jp = j ^ g2
                    b = difference(k(jp), k(j))
                    left_then_right = plus(left, mul(b, x(ip)))
                    right_then_left = plus(mul(b, x(i)), mul(y(jp), a))
                    filler = mul(b, a)
                    assert delta(filler) == difference(right_then_left, left_then_right)
                    assert delta(delta(filler)) == {}
                    assert delta(left_then_right) == difference(D(ip, jp), D(i, j))
                    assert delta(right_then_left) == difference(D(ip, jp), D(i, j))
                    reference = difference(H(ip, jp), H(i, j))
                    # The source's first-route H convention chooses a based comparison.
                    assert difference(left_then_right, reference) == delta(mul(k(j), a))
                    assert difference(right_then_left, reference) == delta(mul(k(jp), a))
                    counts['mixed_squares'] += 1
                    counts['reference_comparison_fillers'] += 2
                    if g and g2:
                        assert filler and delta(filler)
                        counts['nonzero_mixed_witness_boundaries'] += 1
                    else:
                        assert filler == {} and left_then_right == right_then_left
    assert counts['nonzero_mixed_witness_boundaries'] == 144
    report = {
        'schema': 'marici.nima.state-endpoint-transport.v1', 'status': 'passed',
        'counts': counts,
        'source': 'Existing shared-leg DG state generators sh_i,sk_j and their products; baseline reanchoring audit rerun.',
        'left_boundary': 'delta(y_j (h_ip-h_i))=D_ip,j-D_i,j',
        'right_boundary': 'delta((k_jp-k_j) x_i)=D_i,jp-D_i,j',
        'mixed_cell': 'delta((k_jp-k_j)(h_ip-h_i))=right_then_left-left_then_right',
        'natural_leg_witnesses_commute_strictly': False,
        'natural_leg_witnesses_have_existing_degree2_comparison': True,
        'canonical_reference_changes_compose_strictly_on_current_payloads': True,
        'cross_q_transport_exists_in_declared_model': True,
        'distinguished_q_selected': False,
        'boundary': 'Does not construct physical endpoint operations, a universal-source derivation, a full DG action, or a lattice realization of the mixed fillers.',
        'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in
                          (Path(__file__).resolve(), HERE/'check_shared_leg_dg_realization.py',
                           HERE/'check_witnessed_reference_reanchoring.py')},
    }
    out = HERE.parent/'results'/'state-endpoint-transport.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print('PASS: '+str(counts))
    print('Cross-q left/right witnesses exist. Natural mixed routes differ by an existing degree-two boundary.')
    print('Canonical reference routes are strict on current payloads; no distinguished q or higher lattice map inferred.')


if __name__ == '__main__': main()
