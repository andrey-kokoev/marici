# /// script
# dependencies = ["sympy"]
# ///
"""Bounded common history/simulation semantics; not a cross-foundation translation."""
import copy
import itertools
import json
import subprocess
import sys
from hashlib import sha256
from pathlib import Path
import sympy as S

ROOT = Path(__file__).resolve().parents[3]
NOTE = 'research/voevodsky/mathematical-example-overlap-v1.md'
OUT = 'research/voevodsky/results/mathematical-example-overlap-v1.json'
BRANCH = 'research/conjecture_net/contracts/mathematical-realization-conjecture-net.v1.json'
FINITE = 'research/voevodsky/results/finite-domain-interface-audit-v1.json'
RH = 'research/voevodsky/results/rh-general-interface-binding-v1.json'
INTERFACE = 'research/conjecture_net/contracts/stagewise-mathematical-interface.v1.json'

def load(p):
    return json.loads((ROOT / p).read_text(encoding='utf-8'))

def sha(p):
    return sha256((ROOT / p).read_bytes()).hexdigest()

def require(ok, message):
    if not ok:
        raise ValueError(message)

def run_state(s):
    phase, i, y = s
    require(phase in ('request', 'response') and type(i) is bool, 'bad state')
    if phase == 'request':
        require(y is None, 'request output seed')
        return ('response', i, not i)
    require(type(y) is bool, 'bad response')
    return s

def encode(s):
    phase, i, y = s
    return int(i) if phase == 'request' else 2 + 2*int(i) + int(y)

def decode(k):
    require(type(k) is int and 0 <= k < 6, 'bad view')
    return ('request', bool(k), None) if k < 2 else ('response', bool((k-2)//2), bool((k-2)%2))

def join(h, k):
    require(h['source'] == k['source'], 'cross-source composition')
    require(h['states'][-1] == k['states'][0], 'unmatched endpoint')
    return dict(source=h['source'], states=h['states'] + k['states'][1:])

def history(source, step, start, n):
    states = [start]
    for _ in range(n):
        states.append(step(states[-1]))
    return dict(source=source, states=states)

def validate_registration(branch):
    node = next(n for n in branch['conjectures'] if n['id'] == 'mathematical-realization-example-assembly')
    require(node['status'] == 'resolved' and node['verdict'] == 'constructed', 'unregistered assembly')
    require(node['resolution_kind'] == 'bounded_policy_indexed_semantic_assembly', 'scope drift')
    require(node['outcome'] is None and branch['objective']['outcome'] is None, 'formal outcome not admitted')
    require(node['evidence'] == ['mathematical-example-overlap'], 'missing overlap review')
    for key in ('universal_coverage_proved', 'cross_metatheory_translation_supplied',
                'arbitrary_dependent_payload_action_instantiated', 'parent_discharged'):
        require(node[key] is False, 'unsupported assembly: ' + key)


def main():
    branch = load(BRANCH)
    validate_registration(branch)
    by = {n['id']: n for n in branch['conjectures']}
    for node in ('finite-domain-wg-example', 'rh-mathematical-realization-example'):
        require(by[node]['status'] == 'resolved' and by[node]['verdict'] == 'constructed', 'unreviewed input')
    # Replay RH finite algebra and validate all retained source receipts; do not
    # regenerate the finite proof receipt or claim a new compiler closure.
    for script in ('check_finite_domain_disposition.py', 'check_rh_general_interface_binding.py'):
        r = subprocess.run([sys.executable, str(ROOT / 'research/voevodsky/checkers' / script)],
                           cwd=ROOT, capture_output=True, text=True, timeout=280)
        require(r.returncode == 0, script + '\n' + r.stdout + r.stderr)
    for path in (FINITE, RH):
        receipt = load(path)
        require(receipt['passed'], 'failed evidence')
        for src, expected in receipt['source_sha256'].items():
            require(sha(src) == expected, 'source drift: ' + src)
    interface = load(INTERFACE)
    require(not any(interface['boundaries'].values()), 'interface overclaim')
    states = [('request', i, None) for i in (False, True)] + [
        ('response', i, y) for i, y in itertools.product((False, True), repeat=2)]
    # Independent explicit table includes arbitrary typed responses, not only
    # computed/reachable responses. It is a finite view of the actual compiler.
    table = {0: 3, 1: 4, 2: 2, 3: 3, 4: 4, 5: 5}
    checks = 0
    for state in states:
        require(decode(encode(state)) == state, 'source recovery')
        require(encode(run_state(state)) == table[encode(state)], 'actual step square')
        # Admission of the false-only instance remains an indexed guard.
        require((state[1] is False) == (encode(state) in (0, 2, 3)), 'guard mismatch')
        for n, m in itertools.product(range(5), repeat=2):
            h = history('BooleanCompiler', run_state, state, n)
            k = history('BooleanCompiler', run_state, h['states'][-1], m)
            combined = join(h, k)
            actual = history('BooleanCompiler', run_state, state, n+m)
            view = history('BooleanCompilerView', table.__getitem__, encode(state), n+m)
            require(combined == actual, 'history composition mismatch')
            require(tuple(map(encode, combined['states'])) == tuple(view['states']), 'history simulation mismatch')
            require(tuple(map(decode, view['states'])) == tuple(combined['states']), 'history recovery mismatch')
            checks += 1
    # New discriminating control: typed responses can be supplied independently
    # of requests. An index-only view cannot reconstruct every legal response.
    a = ('response', False, False); b = ('response', False, True)
    require(a[:2] == b[:2] and run_state(a)[2] != run_state(b)[2], 'response-erasure control')
    h1 = history('BooleanCompiler', run_state, ('request', False, None), 1)
    h2 = history('BooleanCompiler', run_state, ('request', False, None), 2)
    require(h1['states'][-1] == h2['states'][-1] and h1 != h2, 'history-erasure control')

    endpoint = 'research/voevodsky/results/full-endpoint-fourier-bridge-v1.json'
    ep = load(endpoint); M = S.Matrix(ep['endpoint_matrix']); J = S.Matrix(ep['full_analytic_attachment'])
    native = S.simplify(J*M*J.inv()); ell = S.ones(1, 4)*J
    Z = ell.col_join(ell*M); T = S.Matrix([[0, 1], [1, 1]])
    require(S.simplify(J.inv()*J) == S.eye(4), 'RH recovery')
    require(S.simplify(native*J-J*M) == S.zeros(4), 'RH one-step square')
    require(S.simplify(native**2*J-J*M**2) == S.zeros(4), 'RH two-step square')
    require(Z*M == T*Z and Z.rank() == 2, 'task quotient square')
    require(all(Z*M*v == S.zeros(2, 1) for v in Z.nullspace()), 'quotient continuation failure')
    require(len(Z.nullspace()) == 2, 'task incorrectly made complete identity')
    # Numerical equality of view endpoints never licenses a cross-source join.
    hostiles = []
    for name, left, right in (
        ('cross-source-history', dict(source='BooleanCompiler', states=[0, 1]), dict(source='RHEndpoint', states=[1, 2])),
        ('wrong-intermediate-state', dict(source='BooleanCompiler', states=[0, 1]), dict(source='BooleanCompiler', states=[2, 3]))):
        try:
            join(left, right)
        except ValueError:
            hostiles.append(name)
        else:
            raise AssertionError('invalid join accepted')
    registration_controls = []
    for key in ('universal_coverage_proved', 'cross_metatheory_translation_supplied',
                'arbitrary_dependent_payload_action_instantiated', 'parent_discharged', 'outcome'):
        bad = copy.deepcopy(branch)
        node = next(n for n in bad['conjectures'] if n['id'] == 'mathematical-realization-example-assembly')
        node[key] = True
        try:
            validate_registration(bad)
        except ValueError:
            registration_controls.append(key)
        else:
            raise AssertionError('assembly promotion accepted')
    paths = [NOTE, BRANCH, FINITE, RH, INTERFACE, endpoint,
             'research/nima/agda/DomainWitnessCompiler.agda',
             Path(__file__).relative_to(ROOT).as_posix()]
    result = dict(schema='marici.mathematical-example-overlap.v1', passed=True,
                  proposed_disposition='bounded_policy_indexed_semantic_assembly',
                  registration_validated=True, registration_controls_rejected=registration_controls,
                  finite_states_covered=6, finite_history_composition_cases=checks,
                  exact_RH_one_and_two_step_squares=True,
                  new_response_erasure_hostile=True, retained_history_erasure_hostile=True,
                  rejected_joins=hostiles,
                  common_semantics=['actual typed operation', 'matching-source matching-endpoint history composition',
                                    'source recovery distinct from continuation-safe task quotient',
                                    'validity indexed by evidence policy', 'supplied/generated law provenance'],
                  exclusions=dict(common_source_constructed=False, cross_metatheory_translation=False,
                                  arbitrary_dependent_payload_action=False, universal_coverage=False,
                                  RH_proved=False, physical_realization=False, parent_discharged=False),
                  finite_formal_receipt_revalidated=True, fresh_Agda_closure=False,
                  source_sha256={p: sha(p) for p in paths})
    (ROOT / OUT).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'source_sha256'}, indent=2))

if __name__ == '__main__':
    main()
