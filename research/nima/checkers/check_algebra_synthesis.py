"""Independent scalar certificate audit and a held-out, cached adequacy backend.

The target occurs HERE, never in the candidate generator. The adequacy backend
reuses the existing quantified Agda proof; it is not a new theorem prover.
"""
from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path
import argparse
import hashlib
import io
import json
import unittest

if not __debug__:
    raise RuntimeError('Certificate auditing requires assertions; optimized Python is unsupported')

BASE = Path(__file__).resolve().parents[1]
TARGET = ((((0, 1), 2), (0, ((0, 2), 0))), 2)


def freeze(t):
    if type(t) is int and 0 <= t <= 8:
        return t
    if isinstance(t, (tuple, list)) and len(t) == 2:
        return freeze(t[0]), freeze(t[1])
    raise ValueError('invalid term')


def scalar(term, assignment, size, table):
    if type(term) is int:
        return assignment[term]
    return table[size * scalar(term[0], assignment, size, table) + scalar(term[1], assignment, size, table)]


def direct_holds(left, right, variables, size, table):
    return all(scalar(left, a, size, table) == scalar(right, a, size, table)
               for a in product(range(size), repeat=variables))


def check_model(model):
    n, table = model['size'], model['table']
    assert type(n) is int and 2 <= n <= 6
    assert len(table) == n * n and all(type(v) is int and 0 <= v < n for v in table)
    op = lambda a, b: table[n * a + b]
    failure = model['obstruction']
    assignment = failure['assignment']
    assert all(type(x) is int and 0 <= x < n for x in assignment)
    if failure['law'] == 'commutativity':
        x, y = assignment
        assert op(x, y) != op(y, x)
    elif failure['law'] == 'double-negation':
        x, = assignment
        assert op(op(x, x), op(x, x)) != x
    elif failure['law'] == 'absorption':
        x, y = assignment
        assert op(op(x, x), op(x, op(y, y))) != x
    elif failure['law'] == 'top-independence':
        x, y = assignment
        assert op(x, op(x, x)) != op(y, op(y, y))
    else:
        raise ValueError('unknown necessary law')


def catalan(n):
    return comb(2 * n, n) // (n + 1)


@lru_cache(None)
def completions(slots, used):
    return 1 if slots == 0 else used * completions(slots - 1, used) + completions(slots - 1, used + 1)


def unrank_pattern(length, rank):
    assert 0 <= rank < completions(length - 1, 1)
    result, used = [0], 1
    for slots in range(length - 2, -1, -1):
        for value in range(used + 1):
            block = completions(slots, used + (value == used))
            if rank < block:
                result.append(value)
                used += value == used
                break
            rank -= block
    return result


def unrank_tree(nodes, rank):
    assert 0 <= rank < catalan(nodes)
    if nodes == 0:
        return None
    for left in range(nodes):
        right = nodes - 1 - left
        block = catalan(left) * catalan(right)
        if rank < block:
            a, b = divmod(rank, catalan(right))
            return unrank_tree(left, a), unrank_tree(right, b)
        rank -= block
    raise AssertionError('unreachable tree rank')


def unrank(cost, ordinal):
    shape_index, pattern_index = divmod(ordinal, completions(cost + 1, 1))
    shape = unrank_tree(cost + 1, shape_index)
    pattern = unrank_pattern(cost + 2, pattern_index)
    labels = iter(pattern)
    def build(t):
        return next(labels) if t is None else (build(t[0]), build(t[1]))
    equation = build(shape)
    return equation[0], equation[1], max(pattern) + 1


def audit_lower(packet, bound=6):
    """Reconstruct all cheaper identities independently by Catalan/Bell unranking."""
    models = packet['countermodels']
    for model in models:
        check_model(model)
    rejects = {}
    for cost, ordinal, witness in packet['rejections']:
        assert all(type(x) is int for x in (cost, ordinal, witness))
        assert 0 <= cost <= packet['max_cost'] and 0 <= witness < len(models)
        assert 0 <= ordinal < catalan(cost + 1) * completions(cost + 1, 1)
        assert (cost, ordinal) not in rejects
        rejects[cost, ordinal] = witness
    opens = {(s['cost'], s['ordinal']): s for s in packet['survivors']}
    assert len(opens) == len(packet['survivors'])
    assert not set(opens).intersection(rejects)
    unresolved, levels = [], []
    for cost in range(bound):
        count = catalan(cost + 1) * completions(cost + 1, 1)
        false_count = rejected = open_count = 0
        for ordinal in range(count):
            left, right, variables = unrank(cost, ordinal)
            key = cost, ordinal
            if not direct_holds(left, right, variables, 2, (1, 1, 1, 0)):
                assert key not in opens and key not in rejects
                false_count += 1
            elif key in rejects:
                model = models[rejects[key]]
                assert direct_holds(left, right, variables, model['size'], model['table']), key
                rejected += 1
            else:
                assert key in opens, ('missing lower obligation', key)
                item = opens[key]
                assert (freeze(item['left']), freeze(item['right']), item['variables']) == (left, right, variables)
                unresolved.append(key)
                open_count += 1
        expected = {'cost': cost, 'enumerated': count, 'boolean_invalid': false_count,
                    'countermodel_rejected': rejected, 'open': open_count}
        assert packet['levels'][cost] == expected
        levels.append(expected)
    return {'levels': levels, 'unresolved': unresolved,
            'minimality_status': 'unresolved' if unresolved else 'finite-rejection-audit-complete-not-agda-proof',
            'kernel_checked_minimality': False, 'agda_sigma_package_constructed': False}


def audit_supplement(minimum, supplement):
    remaining = set(map(tuple, minimum['unresolved']))
    seen, checked = set(), []
    for report in supplement['reports']:
        key = report['cost'], report['ordinal']
        assert key in remaining and key not in seen, 'unrelated or duplicate supplementary obligation'
        seen.add(key)
        if report['status'] != 'countermodel-replayed':
            assert report['status'] in ('budget-exhausted-not-a-refutation', 'no-model-in-declared-family-not-a-refutation')
            continue
        model = report['model']
        check_model(model)
        left, right, variables = unrank(*key)
        assert direct_holds(left, right, variables, model['size'], model['table']), key
        checked.append({'coordinate': key, 'model': model})
    remaining.difference_update(tuple(item['coordinate']) for item in checked)
    return {**minimum, 'base_unresolved': minimum['unresolved'], 'unresolved': sorted(remaining),
            'supplementary_rejections': checked,
            'minimality_status': 'unresolved' if remaining else 'exhaustive-rejection-certificate-replayed',
            'runtime_certificate_package_constructed': not remaining,
            'kernel_checked_minimality': False, 'agda_sigma_package_constructed': False}


def select_cached_adequacy(packet):
    matches = [s for s in packet['survivors'] if (freeze(s['left']), freeze(s['right'])) == TARGET]
    assert len(matches) == 1, 'held-out target was not independently enumerated exactly once'
    found = matches[0]
    assert found['cost'] == 6
    assert unrank(found['cost'], found['ordinal']) == (*TARGET, 3)
    return found


def agda_term(term):
    return f'(var {term})' if type(term) is int else f'(op {agda_term(term[0])} {agda_term(term[1])})'


def lower_formal_source(supplement):
    reports = supplement['reports']
    models = []
    for report in reports:
        assert report['status'] == 'countermodel-replayed'
        model = report['model']
        check_model(model)
        assert model['size'] == 4 and model['obstruction']['law'] == 'commutativity'
        if model not in models:
            models.append(model)
    lines = ['{-# OPTIONS --safe --cubical --guardedness #-}',
        '-- Generated explicit countermodels; no solver answer is a proof primitive.',
        'module GeneratedLowerRefutations where',
        'open import Cubical.Foundations.Prelude',
        'open import Cubical.Foundations.HLevels using (isSet×; isOfHLevelLift)',
        'open import Cubical.Data.Bool.Base using (Bool; false; true)',
        'open import Cubical.Data.Bool.Properties using (isSetBool; false≢true)',
        'open import Cubical.Data.Nat.Base using (ℕ; zero; suc)',
        'open import Cubical.Data.Sigma.Base using (_×_)',
        'open import Cubical.Data.Empty.Base using (⊥)',
        'open import AlgebraSynthesisSpecification', '', 'module Models (ℓ : Level) where',
        '  Four : Type ℓ', '  Four = Lift {j = ℓ} (Bool × Bool)',
        '  pattern f0 = lift (false , false)', '  pattern f1 = lift (true , false)',
        '  pattern f2 = lift (false , true)', '  pattern f3 = lift (true , true)',
        '  environment : Four → Four → Four → Four → ℕ → Four',
        '  environment a b c d zero = a', '  environment a b c d (suc zero) = b',
        '  environment a b c d (suc (suc zero)) = c',
        '  environment a b c d (suc (suc (suc _))) = d', '']
    for i, model in enumerate(models):
        table = model['table']
        lines.append(f'  table{i} : Four → Four → Four')
        for a, b in product(range(4), repeat=2):
            lines.append(f'  table{i} f{a} f{b} = f{table[4 * a + b]}')
        x, y = model['obstruction']['assignment']
        left, right = table[4*x+y], table[4*y+x]
        projection = 'fst' if left % 2 != right % 2 else 'snd'
        firstbit = left % 2 if projection == 'fst' else left // 2
        path = f'(recover f{x} f{y} ∙ Necessary.commutativity boolean f{x} f{y} ∙ sym (recover f{y} f{x}))'
        projected = f'(cong (λ z → {projection} (lower z)) {path})'
        if firstbit:
            projected = f'(sym {projected})'
        lines += [f'  reject{i} : (e : Equation) → Holds e table{i} → Adequate {{ℓ}} e → ⊥',
                  f'  reject{i} e law adequate =',
                  f'    let pair = Adequate.reconstruct adequate Four (isOfHLevelLift 2 (isSet× isSetBool isSetBool)) f0 table{i} law',
                  '        boolean = fst pair', '        recover = snd pair',
                  f'    in false≢true {projected}', '']
    for i, report in enumerate(reports):
        left, right, variables = unrank(report['cost'], report['ordinal'])
        assert variables <= 4
        model_index = models.index(report['model'])
        table = f'table{model_index}'
        args = [f'a{j}' for j in range(variables)]
        env = '(environment ' + ' '.join(args + ['f0'] * (4 - variables)) + ')'
        lines += [f"  -- Coordinate ({report['cost']}, {report['ordinal']}).",
                  f'  equation{i} : Equation',
                  f'  equation{i} = {agda_term(left)} , {agda_term(right)}',
                  f'  formula{i} : Formula', f'  formula{i} = equation{i} , refl',
                  f"  cost{i} : cost equation{i} ≡ {report['cost']}", f'  cost{i} = refl',
                  f'  law{i} : (' + ' '.join(args) + ' : Four)',
                  f'    → eval {table} {env} (fst equation{i}) ≡ eval {table} {env} (snd equation{i})']
        for assignment in product(range(4), repeat=variables):
            lines.append(f'  law{i} ' + ' '.join(f'f{x}' for x in assignment) + ' = refl')
        lines += [f'  refute{i} : Adequate {{ℓ}} equation{i} → ⊥',
                  f'  refute{i} = reject{model_index} equation{i} (λ env → law{i} ' + ' '.join(f'(env {j})' for j in range(variables)) + ')', '']
    return '\n'.join(lines) + '\n'


def formal_source(found):
    equation = agda_term(freeze(found['left'])) + ' , ' + agda_term(freeze(found['right']))
    return '''{-# OPTIONS --safe --cubical --guardedness #-}
-- Generated from the search artifact, then checked against a cached proof.
module DiscoveredWolframFormula where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import AlgebraSynthesisSpecification
import GeneratedLowerRefutations
import BooleanNandEquivalence as B

found-equation : Equation
found-equation = @EQUATION@
found-formula : Formula
found-formula = found-equation , refl
found-cost : cost found-equation ≡ 6
found-cost = refl

valid : {ℓ : Level} (A : Type ℓ) (boolean : B.BooleanStructure A)
  → Holds found-equation (B.ToWolfram.nand boolean)
valid A boolean env = B.ToWolfram.wolfram boolean (env 0) (env 1) (env 2)

module Recover {ℓ : Level} (A : Type ℓ) (setA : isSet A) (e : A)
  (stroke : A → A → A) (law : Holds found-equation stroke) where
  env : A → A → A → ℕ → A
  env a b c zero = a
  env a b c (suc zero) = b
  env a b c (suc (suc _)) = c
  W : (a b c : A) → stroke (stroke (stroke a b) c) (stroke a (stroke (stroke a c) a)) ≡ c
  W a b c = law (env a b c)
  module R = B.FromWolfram A setA e stroke W

adequate : {ℓ : Level} → Adequate {ℓ} found-equation
adequate = record
  { valid = valid
  ; reconstruct = λ A setA e stroke law →
      Recover.R.boolean A setA e stroke law , Recover.R.recovered-operation A setA e stroke law }

-- No inhabitant of Goal.Result is asserted: the finite minimum certificate is
-- replayed in Python; its enumeration coverage and reflection are not proved here.
'''.replace('@EQUATION@', equation)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--emit', action='store_true', help='emit source before a separate fresh compiler check')
    args = parser.parse_args()
    source = BASE / 'results/algebra-formula-search.json'
    packet = json.loads(source.read_text(encoding='utf-8'))
    generator = BASE / 'checkers/algebra_formula_search.py'
    assert packet['generator_sha256'] == hashlib.sha256(generator.read_bytes()).hexdigest()
    assert packet['schema'] == 'marici.algebra-formula-search.v1' and packet['max_cost'] == 6
    found = select_cached_adequacy(packet)
    formal_path = BASE / 'agda/DiscoveredWolframFormula.agda'
    if args.emit:
        formal_path.write_text(formal_source(found), encoding='utf-8')
        supplement = json.loads((BASE / 'results/algebra-finite-sat.json').read_text(encoding='utf-8'))
        (BASE / 'agda/GeneratedLowerRefutations.agda').write_text(lower_formal_source(supplement), encoding='utf-8')
        print('Emitted actual enumerated candidate:', found['display'], 'ordinal', found['ordinal'])
        return
    assert formal_path.read_text(encoding='utf-8') == formal_source(found)
    from agda_receipt_audit import verify_receipt
    formal = verify_receipt('DiscoveredWolframFormula', 'algebra-synthesis',
                            ['SynthesisBadFormula', 'SynthesisBadNormalization', 'SynthesisBadCountermodel'])
    supplement_path = BASE / 'results/algebra-finite-sat.json'
    supplement = json.loads(supplement_path.read_text(encoding='utf-8'))
    assert (BASE / 'agda/GeneratedLowerRefutations.agda').read_text(encoding='utf-8') == lower_formal_source(supplement)
    minimum = audit_supplement(audit_lower(packet), supplement)
    minimum['supplementary_refutations_kernel_checked'] = len(supplement['reports'])
    assert supplement['source_sha256'] == hashlib.sha256(source.read_bytes()).hexdigest()
    assert supplement['backend_sha256'] == hashlib.sha256((BASE / 'checkers/algebra_finite_sat.py').read_bytes()).hexdigest()
    stream = io.StringIO()
    suite = unittest.defaultTestLoader.discover(str(BASE / 'checkers'), pattern='test_algebra_synthesis.py')
    tests = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    (BASE / 'results/algebra-synthesis-tests.log').write_text(stream.getvalue(), encoding='utf-8')
    assert tests.wasSuccessful(), stream.getvalue()
    result = {'schema': 'marici.algebra-synthesis-audit.v1',
              'status': ('extracted-adequacy-checked-finite-minimum-audited' if not minimum['unresolved']
                         else 'automated-extraction-with-reused-adequacy-proof-minimality-open'),
              'formula': {**{k: v for k, v in found.items() if k != 'status'},
                          'generation_status': found['status'], 'adequacy_status': 'kernel-checked-with-reused-proof'},
              'formal': formal, 'minimality': minimum,
              'tests_run': tests.testsRun,
              'sha256': {name: hashlib.sha256((BASE / name).read_bytes()).hexdigest() for name in
                  ['checkers/algebra_formula_search.py', 'checkers/algebra_finite_sat.py',
                   'checkers/check_algebra_synthesis.py', 'checkers/test_algebra_synthesis.py']}, 
              'total_enumerated': sum(level['enumerated'] for level in packet['levels']),
              'search_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'supplement_sha256': hashlib.sha256(supplement_path.read_bytes()).hexdigest(),
              'adequacy_backend': 'existing quantified Agda theorem, not newly synthesized proof',
              'runtime_boundary': 'Python enumeration, JSON, scalar audit and unranking are tested, not extracted from Agda',
              'residuals': ['no kernel-checked minimality witness',
                            'no general adequate-axiom prover', 'no theorem connecting this search runtime to the prior Layer4 machine']}
    (BASE / 'results/algebra-synthesis-audit.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'enumerated': result['total_enumerated'],
                      'cheaper_unresolved': len(minimum['unresolved']), 'tests': tests.testsRun,
                      'kernel_checked_supplementary_refutations': minimum['supplementary_refutations_kernel_checked'],
                      'formula': found['display']}))


if __name__ == '__main__':
    main()
