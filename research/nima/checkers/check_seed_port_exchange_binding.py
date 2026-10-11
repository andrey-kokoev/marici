"""Conditional occurrence-sensitive binding to the EXISTING exchange model.

Each native primitive a->b selects existing tensor-state slot (a,b), not
an endpoint-difference feature for an entire path. The tail/head assignment
is a declared adapter policy. It is not selected by the native seed alone.
Exact rational unwhitened calculations, plus comparison to original U.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io
import json
import runpy
import numpy as np
import sympy as S

HERE = Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    seed = runpy.run_path(str(HERE/'check_seed_typed_execution.py'))
    old = runpy.run_path(str(HERE/'check_137_closed_record_stationarity.py'))
registry = seed['registry']
labels = tuple(registry)
assert set(labels) == {'AB', 'BC', 'CA', 'AD', 'DB', 'BA'}
vertices = {v: i for i, v in enumerate('ABCD')}
G = 10*S.eye(4)+S.ones(4)
H = S.kronecker_product(G, G)
features = S.Matrix.hstack(*(S.eye(16)[:, 4*vertices[a]+vertices[b]]/11
                            for a, b in (registry[label] for label in labels)))
metric = S.diag(H, S.eye(6))
checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


operators = {}
for i, label in enumerate(labels):
    f = features[:, i]
    # delta=r_i - f^T H y; q_white=L^T y.
    mismatch = (-f.T*H).row_join(S.eye(6)[i, :])
    direction = f.col_join(-S.eye(6)[:, i])
    E = S.eye(22)+direction*mismatch
    operators[label] = E
    check('unit-existing-feature/'+label, (f.T*H*f)[0] == 1)
    check('involution/'+label, E*E == S.eye(22))
    check('counting-budget/'+label, E.T*metric*E == metric)
    anchor = S.eye(16).row_join(features)
    check('conserved-retained-anchor/'+label, anchor*E == anchor)

    a, b = registry[label]
    port = 121+4*vertices[a]+vertices[b]
    expected = old['L'].T @ np.array(f, dtype=float).ravel()
    check('original-137-port-feature/'+label, np.max(np.abs(expected-old['U'][port])) < 1e-12)

# Test the same full update against original whitened coordinates, with
# unused records retained unchanged rather than silently discarded.
z = S.Matrix([S.Rational(i % 7-3, 5) for i in range(22)])
for i, label in enumerate(labels):
    numeric = np.zeros(153)
    numeric[:16] = old['L'].T @ np.array(z[:16, :], dtype=float).ravel()
    for k, name in enumerate(labels):
        a, b = registry[name]
        numeric[16+121+4*vertices[a]+vertices[b]] = float(z[16+k])
    a, b = registry[label]
    port = 121+4*vertices[a]+vertices[b]
    delta = numeric[16+port]-old['U'][port]@numeric[:16]
    numeric[:16] += old['U'][port]*delta
    numeric[16+port] -= delta
    exact = operators[label]*z
    check('original-full-exchange-carrier/'+label, np.max(np.abs(numeric[:16]-old['L'].T@
          np.array(exact[:16, :], dtype=float).ravel())) < 1e-12)
    for k, name in enumerate(labels):
        a, b = registry[name]
        check('original-record/'+label+'/'+name,
              abs(numeric[16+121+4*vertices[a]+vertices[b]]-float(exact[16+k])) < 1e-12)


def execute(word, value):
    path = seed['validate'](seed['execute'](word))
    current = value
    history = []
    for occurrence in path:
        before = current
        current = operators[occurrence[3]]*current
        history.append((occurrence, before, current))
    return current, tuple(history)


# Existing actual parallel paths, not invented surrogate edges.
paths = [('AB',), ('AD', 'DB'), ('BA',), ('BC', 'CA')]
excited = S.zeros(22, 1)
excited[16+labels.index('AB')] = 1
outputs = {}
for word in paths:
    out, history = execute(word, excited)
    outputs[word] = out
    recovered = out
    for occurrence, before, after in reversed(history):
        recovered = operators[occurrence[3]]*recovered
        check('inverse-occurrence/'+str(word)+'/'+occurrence[3], recovered == before)
    check('whole-path-recovery/'+str(word), recovered == excited)
    check('path-budget/'+str(word), (out.T*metric*out)[0] == 1)
check('direct-indirect-forward-distinguished', outputs[('AB',)] != outputs[('AD', 'DB')])
# The AB-only preparation leaves BOTH return protocols idle. Preserve this
# failed universal-discrimination control instead of tuning the preparation.
check('return-paths-equal-on-AB-only-preparation', outputs[('BA',)] == outputs[('BC', 'CA')])
return_difference = operators['BA']-operators['CA']*operators['BC']
check('return-operators-distinct-on-full-domain', return_difference != S.zeros(22))
first, h1 = execute(('AB', 'BA'), excited)
second, h2 = execute(('AB', 'BA'), excited)
check('repeated-path-occurrences-retained', first == second and h1 != h2)

# Endogenous back-action is computed from current carrier/record mismatch.
B = (-features.T*H).row_join(S.eye(6))
K = S.eye(6)+features.T*H*features
for i, label in enumerate(labels):
    check('cross-response/'+label, B*operators[label] == B-K[:, i]*B[i, :])
check('nonzero-off-port-response', any(K[j, labels.index('AB')] != 0
      for j in range(6) if j != labels.index('AB')))
fixed_y = S.ones(16, 1)
fixed = fixed_y.col_join(features.T*H*fixed_y)
check('matched-baseline-not-excited', all(E*fixed == fixed for E in operators.values()))
check('zero-baseline-not-excited', all(E*S.zeros(22, 1) == S.zeros(22, 1) for E in operators.values()))

# Port chart covariance under every vertex renaming. The excluded arrow
# marking of the old 121 block does not enter these 16 state-block ports.
from itertools import permutations
for perm in permutations(range(4)):
    P = S.Matrix(4, 4, lambda i, j: int(i == perm[j]))
    T = S.kronecker_product(P, P)
    check('metric-frame/'+str(perm), T.T*H*T == H)
    for k, label in enumerate(labels):
        a, b = registry[label]
        moved = S.eye(16)[:, 4*perm[vertices[a]]+perm[vertices[b]]]/11
        check('port-frame/'+str(perm)+'/'+label, T*features[:, k] == moved)

# This protocol is ordered; no equal-effect face between these two native
# parallel paths is fabricated. They have the same source/target ports,
# not an established equality of full numerical effects.
result = {
    'schema': 'marici.nima.seed-port-exchange-binding.v1', 'status': 'pass', 'checks': checks,
    'port_binding': {label: 121+4*vertices[a]+vertices[b] for label, (a, b) in registry.items()},
    'policy': 'primitive tail/head pair selects tensor-state slot; each actual occurrence executes its exchange and retains its before/after record',
    'carrier': 'existing 16-dimensional tensor carrier with G tensor G; six selected persistent records embedded in all 137 records',
    'exact_feature': 'f_ab=(e_a tensor e_b)/11; f_ab^T (G tensor G) f_ab=1',
    'source_reused': 'existing seed registry, execution occurrence allocator, validator and ordered path composition',
    'preparation': 'unit AB-record excitation is supplied; matched and zero preparations remain fixed',
    'failed_universal_discriminator': 'AB-only preparation does not distinguish BA from BC,CA numerically; their full operators differ and their occurrence histories remain distinct',
    'scope': 'conditional native-port adapter to an existing exchange law, not a source-selected metric, feature encoding or occurrence law',
    'not_closed': ['native preparation/selection', 'identification of mode exchange with physical charge/mass/recoil',
                   'physical position and time readouts', 'interpretation of any additional native equality or higher witness'],
}
(HERE.parent/'results/seed-port-exchange-binding.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(f'PASS: {len(checks)} exact/fixture port-binding checks')
print('Actual primitive paths execute existing exchanges without collapsing direct/indirect histories.')
print('Conditional tail/head tensor-slot policy; no excitation from matched baseline or physical impulse identification.')
