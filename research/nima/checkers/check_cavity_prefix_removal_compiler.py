"""Exact source-bound component compilation; never runs foreign main/writers."""
import ast
import json
import runpy
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ASPECT = 'research/aspect/checkers/reciprocal_lossy_cavity_plant.py'
GEOMETRY = 'research/nima/checkers/check_physics_geometric_candidate.py'
PROTOCOL = 'research/nima/cavity-prefix-removal-compiler-protocol.md'
SCRIPT = 'research/nima/checkers/check_cavity_prefix_removal_compiler.py'
SOURCES = [ASPECT, GEOMETRY, PROTOCOL, SCRIPT,
           'research/nima/physics-geometric-candidate-v1.md',
           'research/nima/left-trim-suffix-transport-prior-review.md']


def require(ok, why):
    if not ok:
        raise AssertionError(why)


def hashes():
    return {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in SOURCES}


def transpose(a):
    return [list(row) for row in zip(*a)]


def main():
    before = hashes()
    source = runpy.run_path(str(ROOT / ASPECT))
    g = runpy.run_path(str(ROOT / GEOMETRY))
    # Execute only the already inspected assignment prefix that constructs the
    # actual component matrices. main, assertions and result writers never run.
    tree = ast.parse((ROOT / ASPECT).read_text(encoding='utf-8'))
    main_node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
    prefix = []
    for n in main_node.body:
        require(isinstance(n, ast.Assign), 'component source interface changed')
        prefix.append(n)
        if any(isinstance(t, ast.Name) and t.id == 'dilation' for t in n.targets):
            break
    else:
        raise AssertionError('missing source dilation')
    env = dict(source)
    exec(compile(ast.Module(body=prefix, type_ignores=[]), ASPECT, 'exec'), env)
    require(all(k in env for k in ('m1', 'm2', 'loss', 'dilation')), 'missing components')
    mm, eye, lift_column, lift_state, inner, basis, weight = (
        g[k] for k in ('mm', 'eye', 'lift_column', 'lift_state', 'inner', 'basis', 'weight'))
    permutation = [[F(j == (0, 2, 1, 3)[i]) for j in range(4)] for i in range(4)]

    def embed(a, k):
        slots = (1 + 3*k, 0, 2 + 3*k, 3 + 3*k)
        w = eye()
        for i, row in enumerate(slots):
            for j, col in enumerate(slots):
                w[row][col] = F(a[i][j])
        return w

    def product(word):
        out = eye()
        for _, a in word:
            out = mm(a, out)
        return out

    def inverse(word):
        return [(label + '^-1', transpose(a)) for label, a in reversed(word)]

    def discrepancy(a, b):
        entries = [(i, j, a[i][j]-b[i][j]) for i in range(10) for j in range(10) if a[i][j] != b[i][j]]
        return {'nonzero_entries': len(entries),
                'first': None if not entries else [entries[0][0], entries[0][1], str(entries[0][2])]}

    rounds = []
    components = [('m1', env['m1']), ('m2', env['m2']), ('loss', env['loss']), ('output-rewire', permutation)]
    wiring_controls = []
    for k in range(3):
        word = [(f'round{k}:{name}', embed(a, k)) for name, a in components]
        rounds.append(word)
        target = g['round_map'](k)
        require(product(word) == target, 'component-to-round mismatch')
        require(mm(transpose(target), target) == eye(), 'round is not orthogonal')
        bad = discrepancy(product(word[:-1]), target)
        require(bad['nonzero_entries'] > 0, 'omitted rewiring escaped')
        wiring_controls.append(bad)

    cases = []
    total_columns = total_metric_entries = 0
    for i, j in ((0, 1), (0, 2), (1, 2)):
        first = rounds[i]
        suffix = [item for k in range(i+1, j+1) for item in rounds[k]]
        original = first + suffix
        correction = inverse(suffix) + inverse(first) + suffix
        A, S, V, D = map(product, (first, suffix, original, correction))
        require(V == mm(S, A), 'chronological source convention')
        require(D == mm(S, mm(transpose(A), transpose(S))), 'compiled correction formula')
        require(product(original + correction) == S, 'full corrected operation square')
        require(mm(D, V) == S, 'independent full matrix comparison')
        record = [label for label, _ in original + correction]
        require(record != [label for label, _ in suffix], 'execution genealogy erased')
        per_sector = {}
        for n in (0, 1, 2):
            bs = basis(n)
            corrected_columns = []
            for b in bs:
                staged = lift_state(D, lift_column(V, b))
                expected = lift_column(S, b)
                require(staged == expected, 'lifted full-state square')
                require(inner(staged, staged) == weight(b), 'factorial norm')
                corrected_columns.append(staged)
                total_columns += 1
            for p, bp in enumerate(bs):
                for q, bq in enumerate(bs):
                    require(inner(corrected_columns[p], corrected_columns[q]) == (weight(bp) if p == q else 0), 'factorial Gram identity')
                    total_metric_entries += 1
            per_sector[str(n)] = len(bs)
        bad_inverse = [(label + ':wrong-inverse', transpose(a)) for label, a in suffix]
        bad_word = bad_inverse + [(label + ':wrong-inverse', transpose(a)) for label, a in first] + suffix
        wrong_order = discrepancy(product(original + bad_word), S)
        bare_action = mm(transpose(A), V)
        bare = discrepancy(bare_action, S)
        require(wrong_order['nonzero_entries'] > 0 and bare['nonzero_entries'] > 0, 'inverse hostile escaped')
        cases.append({'segment': [i, j], 'original_word': [s for s, _ in original],
                      'appended_correction_word': [s for s, _ in correction],
                      'expected_suffix_word': [s for s, _ in suffix],
                      'sector_columns': per_sector, 'wrong_inverse_order': wrong_order,
                      'bare_first_inverse': bare, 'full_state_square': True})
        if (i, j) == (0, 1):
            # The untouched mode-9 observer agrees on EVERY input despite the wrong full action.
            require(bare_action[9] == S[9] and bare_action != S, 'scalar-only hostile absent')
            scalar_control = {'observer': 'row 9, untouched spectator amplitude',
                              'agrees_on_every_input': True, 'full_action_residual': bare}
    require(hashes() == before, 'source changed during execution')
    result = {'schema': 'marici.nima.cavity-prefix-removal-compiler.v1', 'passed': True,
              'verdict': 'constructed_at_conditional_component_model_scope',
              'round_component_squares': 3, 'round_input_columns': 30,
              'segment_cases': cases, 'lifted_columns': total_columns,
              'factorial_metric_entries': total_metric_entries,
              'omitted_rewiring_controls': wiring_controls, 'scalar_only_control': scalar_control,
              'physical_control_authorized': False, 'interval_encoding_constructed': False,
              'detectors_included': False,
              'scope': 'Frozen three-round p=q=1 model, full ten-mode carrier, transposed component controls assumed. Exact finite-sector verification; all-sector extension uses the written symmetric-power theorem.',
              'source_sha256': before}
    dest = ROOT / 'research/nima/results/cavity-prefix-removal-compiler.json'
    dest.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k not in ('source_sha256', 'segment_cases')}, indent=2))


if __name__ == '__main__':
    main()
