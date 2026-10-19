# /// script
# dependencies = ["sympy"]
# ///
"""Bind the scoped RH package to the general interface; no RH proof import."""
import copy
import json
import subprocess
import sys
from hashlib import sha256
from pathlib import Path
import sympy as S

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = 'research/conjecture_net/contracts/rh-bounded-mathematical-example.v1.json'
INTERFACE = 'research/conjecture_net/contracts/stagewise-mathematical-interface.v1.json'
BASELINE = 'research/aspect/contracts/theta-rh-interaction-net-state.v20.json'
NOTE = 'research/voevodsky/rh-general-interface-binding-v1.md'
OUT = 'research/voevodsky/results/rh-general-interface-binding-v1.json'

def load(p):
    return json.loads((ROOT / p).read_text(encoding='utf-8'))

def sha(p):
    return sha256((ROOT / p).read_bytes()).hexdigest()

def require(ok, msg):
    if not ok:
        raise ValueError(msg)

def validate_claim(c):
    require(c['validity'] == 'owner-qualified classical analysis and exact finite algebra', 'validity promotion')
    require(c['dependent_transport'] == 'source-indexed archives and typed analytic maps; not arbitrary Cubical payload action', 'transport promotion')
    require(c['task_reader'] == 'Z=[ell;ell M]', 'unsafe scalar identity')
    require(c['normalization'] == 'c Lambda, c xi and c/2 endpoint; no per-state division', 'answer fitting')
    require(c['unchanged_Evans'] == 'rejected_for_tested_criterion', 'legacy rejection lost')
    require(not any(c['boundaries'].values()), 'unsupported conclusion')

def validate_registration(branch):
    node = next(n for n in branch['conjectures'] if n['id'] == 'rh-mathematical-realization-example')
    require(node['status'] == 'resolved' and node['verdict'] == 'constructed', 'missing reviewed disposition')
    require(node['resolution_kind'] == 'bounded_mathematical_example_binding', 'disposition scope drift')
    require(node['outcome'] is None, 'formal outcome not admitted')
    require(node['evidence'] == ['rh-general-interface-binding'], 'missing separate binding evidence')
    for key in ('RH_proved', 'physical_realization_admitted', 'universal_coverage_proved',
                'arbitrary_dependent_payload_action_instantiated'):
        require(node[key] is False, 'unsupported registration: ' + key)
    artifact = next(a for a in branch['artifacts'] if a['id'] == 'rh-general-interface-binding')
    require(artifact['receipt'] == OUT and artifact['note'] == NOTE, 'wrong binding artifact')


def main():
    branch = load('research/conjecture_net/contracts/mathematical-realization-conjecture-net.v1.json')
    validate_registration(branch)
    package = load(PACKAGE)
    interface = load(INTERFACE)
    baseline = load(BASELINE)
    require(package['baseline'] == BASELINE, 'shared source drift')
    run = subprocess.run([sys.executable, str(ROOT / 'research/voevodsky/checkers/check_rh_mathematical_example_package.py')],
                         cwd=ROOT, capture_output=True, text=True, timeout=240)
    require(run.returncode == 0, 'package validation failed\n' + run.stdout + run.stderr)
    require(not any(interface['boundaries'].values()), 'general interface changed')
    legacy = baseline['transverse_unchanged_evans']
    certificate = load(legacy['certificate'])
    require(legacy['status'] == 'rejected_for_tested_criterion' and legacy['strictly_negative'], 'legacy gate lost')
    require(certificate['status'] == 'certified_strictly_negative' and certificate['all_dependency_checks_passed'], 'missing residual certificate')
    require(certificate['combined_upper_arb'] == legacy['certified_residual_enclosure'], 'residual mismatch')
    for path, expected in certificate['artifacts_sha256'].items():
        require(sha(path) == expected, 'legacy certificate source drift: ' + path)
    require(not certificate['rh_proved'] and not baseline['claim_boundary']['rh_implication'], 'legacy RH promotion')

    # Recompute the actual licensed endpoint continuation, not a toy observer.
    endpoint_path = 'research/voevodsky/results/full-endpoint-fourier-bridge-v1.json'
    ep = load(endpoint_path)
    M = S.Matrix(ep['endpoint_matrix'])
    J = S.Matrix(ep['full_analytic_attachment'])
    ell = S.ones(1, 4) * J
    require(ell == S.Matrix([[2, 2, 0, 0]]), 'readout convention drift')
    Z = ell.col_join(ell * M)
    T = S.Matrix([[0, 1], [1, 1]])
    require(Z * M == T * Z, 'task not continuation closed')
    x = S.Matrix([1, 0, 0, 0]); y = S.Matrix([1, 0, 1, 0])
    require(ell*x == ell*y == S.Matrix([2]), 'equal-current-readout premise')
    require(ell*M*x == S.Matrix([2]) and ell*M*y == S.Matrix([4]), 'actual continuation hostile lost')
    native = S.simplify(J*M*J.inv())
    F = S.zeros(4)
    for i in range(4):
        F[(i+1)%4, i] = 1
    require(S.simplify(native-F) != S.zeros(4) and S.simplify(native*J-J*M) == S.zeros(4), 'native operation substitution')
    require(S.simplify((Z*J.inv())*native-T*(Z*J.inv())) == S.zeros(2, 4), 'analytic task transport mismatch')
    claim = dict(validity='owner-qualified classical analysis and exact finite algebra',
                 dependent_transport='source-indexed archives and typed analytic maps; not arbitrary Cubical payload action',
                 task_reader='Z=[ell;ell M]',
                 normalization='c Lambda, c xi and c/2 endpoint; no per-state division',
                 unchanged_Evans=legacy['status'],
                 boundaries=dict(RH_assumed_true=False, RH_proved=False, physical_realization=False,
                                 universal_coverage=False, classical_Cubical_translation=False,
                                 same_source_compatibility=False, Weil_form_pullback=False))
    validate_claim(claim)
    mutations = {'validity': 'formally checked universal theorem',
                 'dependent_transport': 'arbitrary Cubical payload action',
                 'task_reader': 'ell alone', 'normalization': 'divide every state by c',
                 'unchanged_Evans': 'constructed'}
    rejected = []
    for key, value in mutations.items():
        bad = copy.deepcopy(claim); bad[key] = value
        try:
            validate_claim(bad)
        except ValueError:
            rejected.append(key)
        else:
            raise AssertionError('mutation accepted: ' + key)
    bad = copy.deepcopy(claim); bad['boundaries']['RH_proved'] = True
    try:
        validate_claim(bad)
    except ValueError:
        rejected.append('RH-promotion')
    else:
        raise AssertionError('RH promotion accepted')
    for key in ('RH_proved', 'physical_realization_admitted', 'universal_coverage_proved',
                'arbitrary_dependent_payload_action_instantiated', 'outcome'):
        bad = copy.deepcopy(branch)
        node = next(n for n in bad['conjectures'] if n['id'] == 'rh-mathematical-realization-example')
        node[key] = True
        try:
            validate_registration(bad)
        except ValueError:
            rejected.append('registration:' + key)
        else:
            raise AssertionError('registration promotion accepted: ' + key)
    paths = [PACKAGE, INTERFACE, BASELINE, NOTE, endpoint_path, legacy['certificate'],
             'research/voevodsky/results/rh-bounded-mathematical-example-v1.json',
             Path(__file__).relative_to(ROOT).as_posix()]
    result = dict(schema='marici.rh-general-interface-binding.v1', passed=True,
                  proposed_disposition='bounded_mathematical_example_binding',
                  registration_validated=True,
                  claim=claim, routes=[r['id'] for r in package['routes']],
                  stage_count=len(package['stage_ids']), map_count=len(package['map_ids']),
                  required_cell_count=len(package['required_cells']),
                  continuation_control=dict(current=[2, 2], next=[2, 4], predictive_reader_rank=Z.rank()),
                  exact_native_and_predictive_squares_recomputed=True,
                  legacy_certificate_hashes_verified=True, legacy_interval_suite_rerun=False,
                  arbitrary_dependent_payload_action_instantiated=False,
                  package_validator_returncode=run.returncode, mutations_rejected=rejected,
                  source_sha256={p: sha(p) for p in paths})
    (ROOT / OUT).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('passed', 'proposed_disposition', 'stage_count', 'map_count',
                                           'required_cell_count', 'continuation_control', 'mutations_rejected')}, indent=2))

if __name__ == '__main__':
    main()
