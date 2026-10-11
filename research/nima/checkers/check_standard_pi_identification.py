"""Bind the written standard-real interpretation to fresh operational kernel evidence.

Finite exact checks do not kernel-verify the classical analysis in the written proof.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import subprocess
import sys
from check_half_turn_coefficients import ROOT, REPO, digest

sys.path.insert(0, str(REPO / 'research/conjecture_net'))
from outcome_reference import load, resolve


def multiply(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])


def cayley(q):
    return ((1-q*q)/(1+q*q), 2*q/(1+q*q))


def exact_audit():
    a, b = F(1, 5), F(1, 239)
    lower = 4*(a-a**3/3)-b
    assert 0 < lower < F(4, 5) < 1
    z = cayley(a)
    square = multiply(z, z)
    fourth = multiply(square, square)
    assert z == (F(12, 13), F(5, 13))
    assert square == (F(119, 169), F(120, 169))
    assert fourth == (F(-239, 28561), F(28560, 28561))
    assert fourth == multiply((F(0), F(1)), cayley(b))
    for q in (a, b):
        term = q
        for n in range(17):
            assert term == (-1)**n * q**(2*n+1)/F(2*n+1)
            term = -term*q*q*F(2*n+1, 2*n+3)
    for q in (F(0), a, b, F(1, 2), F(1)):
        for n in range(17):
            polynomial = sum((-1)**j*q**(2*j) for j in range(n+1))
            remainder = (-1)**(n+1)*q**(2*n+2)/(1+q*q)
            assert polynomial+remainder == 1/(1+q*q)
    return {'status': 'pass', 'theta_strict_lower_bound': str(lower),
            'theta_strict_upper_bound': '4/5', 'rational_machin_rotation_checked': True,
            'recurrence_fixture_cutoffs': [0, 16],
            'boundary': 'Fixtures support the written induction and finite geometric identity; not a proof of classical completeness, integration, or all-index induction.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--timeout', type=int, default=1200)
    args = parser.parse_args()
    proof = 'research/nima/standard-pi-identification.md'
    pointer_path = 'research/nima/contracts/imports/standard-local-lift.pointer.v1.json'
    pointer = load(REPO, pointer_path)
    imported = resolve(REPO, pointer)
    exported = load(REPO, pointer['export']['path'])
    sources = dict(exported['artifact_sha256'])
    for path in [proof, pointer_path, pointer['head'], pointer['export']['path'],
                 'research/nima/checkers/check_standard_pi_identification.py',
                 'research/nima/spectral-whole-return-proof.md', 'research/nima/uniform-local-core-proof.md']:
        sources[path] = digest(REPO / path)
    stages = []
    external = {}
    for checker, receipt_name in [('check_machin_endpoints.py', 'machin-endpoints-fresh.json'),
                                  ('check_machin_reference_series.py', 'machin-reference-series-fresh.json')]:
        run = subprocess.run([sys.executable, str(ROOT / 'checkers' / checker), '--timeout', str(args.timeout)],
                             capture_output=True, timeout=args.timeout + 60)
        if run.returncode:
            raise RuntimeError((run.stdout + run.stderr).decode('utf-8', errors='replace'))
        path = ROOT / 'results' / receipt_name
        receipt = json.loads(path.read_text(encoding='utf-8'))
        assert receipt['status'] == 'pass' and receipt['fresh_closure_completed']
        sources.update(receipt['source_sha256'])
        sources[path.relative_to(REPO).as_posix()] = digest(path)
        external.update(receipt['external_dependency_sha256'])
        external[receipt['command'][0]] = receipt['compiler_sha256']
        stages.append(path.relative_to(REPO).as_posix())
    audit = exact_audit()
    assert all(digest(REPO / p) == h for p, h in sources.items())
    assert all(digest(Path(p)) == h for p, h in external.items())
    result = {
        'schema': 'marici.nima.standard-pi-identification-result.v1',
        'claim': 'completion-pi-half-turn', 'scope_id': 'operational-completion-standard-pi-half-turn',
        'component': 'standard-real-identification-written', 'status': 'pass',
        'verification_level': 'written classical-real interpretation and identification; fresh safe Agda operational endpoints and convergence',
        'proof': proof, 'fresh_kernel_stages': stages, 'sources_stable': True,
        'written_standard_real_identification_proved': True,
        'standard_pi_identification_kernel_proved': False,
        'operational_endpoints_kernel_proved': True, 'reference_series_convergence_kernel_proved': True,
        'mixed_level_acceptance_required': True, 'outcome': None,
        'full_claim_promoted': False, 'unitary_half_turn_proved': False,
        'imported_reference_outcome': imported['outcome'],
        'exact_arithmetic_audit': audit,
        'source_sha256': sources, 'external_dependency_sha256': external,
    }
    (ROOT / 'results/standard-pi-identification.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ['status', 'written_standard_real_identification_proved',
                                         'standard_pi_identification_kernel_proved', 'mixed_level_acceptance_required']}))


if __name__ == '__main__':
    main()
