"""Emit total Agda coverage and universally quantified rejection templates.
No theorem is justified by the planner's cardinality or classifications alone.
"""
from itertools import product
from pathlib import Path
import json
from algebra_formula_search import label
from build_minimality_cover import leaf_count, templates
from check_algebra_synthesis import scalar, agda_term

BASE = Path(__file__).resolve().parents[1]
HEADER = '''{-# OPTIONS --safe --cubical --guardedness #-}
module @MODULE@ where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc; _+_)
open import Cubical.Data.Nat.Order using (_<_; ¬m+n<m)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (isSetBool; false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.List.Base using (List; []; _∷_; _++_)
open import Cubical.Data.Maybe.Base using (Maybe; nothing; just)
open import Cubical.Data.Maybe.Properties using (isOfHLevelMaybe)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Foundations.HLevels using (isOfHLevelLift; isSet×)
open import AlgebraSynthesisSpecification
import BooleanNandEquivalence as B
'''


def raw_expr(shape, values, operation='op'):
    it = iter(values)
    def go(t):
        return next(it) if t is None else f'({operation} {go(t[0])} {go(t[1])})'
    return go(shape)


def equation(shape, values, operation='op'):
    it = iter(values)
    def go(t):
        return next(it) if t is None else f'({operation} {go(t[0])} {go(t[1])})'
    return go(shape[0]) + ' , ' + go(shape[1])


def sides(shape, values, operation):
    it = iter(values)
    def go(t):
        return next(it) if t is None else f'({operation} {go(t[0])} {go(t[1])})'
    return go(shape[0]), go(shape[1])


def natpat(n, tail='zero'):
    for _ in range(n):
        tail = f'(suc {tail})'
    return tail


def mode(table, n):
    if len(set(table)) == 1: return 'constant'
    if all(table[n*x+y] == x for x, y in product(range(n), repeat=2)): return 'left'
    if all(table[n*x+y] == y for x, y in product(range(n), repeat=2)): return 'right'
    return 'table'


def normalize(term, assigned, table, n):
    if type(term) is int:
        return ('c', assigned[term]) if term in assigned else ('v', term)
    a, b = (normalize(t, assigned, table, n) for t in term)
    kind = mode(table, n)
    if kind == 'constant': return ('c', table[0])
    if kind == 'left': return a
    if kind == 'right': return b
    if a[0] == 'c':
        row = table[n*a[1]:n*(a[1]+1)]
        if len(set(row)) == 1: return ('c', row[0])
        if b[0] == 'c': return ('c', row[b[1]])
    return ('o', a, b)


def free(term):
    if term[0] == 'v': return {term[1]}
    if term[0] == 'c': return set()
    return free(term[1]) | free(term[2])


def case_proof(name, left, right, variables, n, table, point, boolean=False, fixed=None):
    assigned = dict(fixed or {})
    args = [i for i in range(variables) if i not in assigned]
    rows = []
    def visit():
        a, b = normalize(left, assigned, table, n), normalize(right, assigned, table, n)
        params = [point(assigned[i]) if i in assigned else f'z{i}' for i in args]
        if not boolean and a == b:
            rows.append('  ' + name + ' ' + ' '.join(params) + ' = refl')
            return
        if boolean and a[0] == b[0] == 'c' and a != b:
            p = '(cong lower p)' if a[1] == 0 else '(sym (cong lower p))'
            rows.append('  ' + name + ' ' + ' '.join(params) + f' p = false≢true {p}')
            return
        remaining = sorted((free(a) | free(b)) - assigned.keys())
        if not remaining:
            raise ValueError(('invalid universal template', name, a, b))
        x = remaining[0]
        for value in range(n):
            assigned[x] = value
            visit()
        del assigned[x]
    visit()
    return rows


LAWS = {
 'commutativity': (((0, 1), (1, 0)), 'commutativity'),
 'double-negation': ((((0, 0), (0, 0)), 0), 'involution'),
 'absorption': ((((0, 0), (0, (1, 1))), 0), 'absorption'),
 'top-independence': (((0, (0, 0)), (1, (1, 1))), 'top-independence'),
}


def support(models):
    out = [HEADER.replace('@MODULE@', 'SynthesisMinimumSupport'), '''
Canonical : Equation → Type
Canonical e = normal zero (leaves (fst e) ++ leaves (snd e)) ≡ true

data Sized : ℕ → Type where
  leaf : ℕ → Sized zero
  fork : {n m : ℕ} → Sized n → Sized m → Sized (suc (n + m))

erase : {n : ℕ} → Sized n → Term
erase (leaf x) = var x
erase (fork a b) = op (erase a) (erase b)
index : (t : Term) → Sized (nodes t)
index (var x) = leaf x
index (op a b) = fork (index a) (index b)
retract : (t : Term) → erase (index t) ≡ t
retract (var x) = refl
retract (op a b) = cong₂ op (retract a) (retract b)
unerase : {n : ℕ} → Sized (suc n) → Equation
unerase (fork a b) = erase a , erase b
index-equation : (e : Equation) → Sized (suc (cost e))
index-equation (a , b) = fork (index a) (index b)
retract-equation : (e : Equation) → unerase (index-equation e) ≡ e
retract-equation (a , b) = cong₂ _,_ (retract a) (retract b)

change-stroke : {ℓ : Level} {A : Type ℓ} {s t : A → A → A}
  → ((x y : A) → s x y ≡ t x y) → (env : ℕ → A) → (e : Term)
  → eval s env e ≡ eval t env e
change-stroke p env (var x) = refl
change-stroke {s = s} p env (op a b) =
  cong₂ s (change-stroke p env a) (change-stroke p env b)
  ∙ p _ _

module Support (ℓ : Level) where
  Two : Type ℓ
  Two = Lift {j = ℓ} Bool
  pattern b0 = lift false
  pattern b1 = lift true
  bn : Two → Two
  bn b0 = b1
  bn b1 = b0
  bm bj : Two → Two → Two
  bm b0 y = b0
  bm b1 y = y
  bj b0 y = y
  bj b1 y = b1
''']
    fields = [
      ('meet-comm', 2, '(bm x0 x1)', '(bm x1 x0)'), ('join-comm', 2, '(bj x0 x1)', '(bj x1 x0)'),
      ('meet-assoc', 3, '(bm (bm x0 x1) x2)', '(bm x0 (bm x1 x2))'),
      ('join-assoc', 3, '(bj (bj x0 x1) x2)', '(bj x0 (bj x1 x2))'),
      ('meet-idem', 1, '(bm x0 x0)', 'x0'), ('join-idem', 1, '(bj x0 x0)', 'x0'),
      ('meet-absorb', 2, '(bm x0 (bj x0 x1))', 'x0'), ('join-absorb', 2, '(bj x0 (bm x0 x1))', 'x0'),
      ('meet-distrib', 3, '(bm x0 (bj x1 x2))', '(bj (bm x0 x1) (bm x0 x2))'),
      ('join-distrib', 3, '(bj x0 (bm x1 x2))', '(bm (bj x0 x1) (bj x0 x2))'),
      ('meet-top', 1, '(bm x0 b1)', 'x0'), ('join-bottom', 1, '(bj x0 b0)', 'x0'),
      ('meet-complement', 1, '(bm x0 (bn x0))', 'b0'), ('join-complement', 1, '(bj x0 (bn x0))', 'b1')]
    for name, arity, left, right in fields:
        out.append(f'  b-{name} : (' + ' '.join(f'x{i}' for i in range(arity)) + f' : Two) → {left} ≡ {right}')
        for values in product(range(2), repeat=arity):
            out.append(f'  b-{name} ' + ' '.join(f'b{x}' for x in values) + ' = refl')
    out += ['  boolean : B.BooleanStructure Two', '  boolean = record',
            '    { carrier-is-set = isOfHLevelLift 2 isSetBool ; bottom = b0 ; top = b1',
            '    ; neg = bn ; meet = bm ; join = bj']
    out += [f'    ; {name} = b-{name}' for name, *_ in fields]
    out += ['    }', '  bop : Two → Two → Two', '  bop = B.ToWolfram.nand boolean',
            '  all0 all1 : ℕ → Two', '  all0 _ = b0', '  all1 _ = b1']
    for i, model in enumerate(models):
        n, table = model['size'], model['table']
        carriers = {2: ('Bool', ['false', 'true'], 'isSetBool'),
                    3: ('Maybe Bool', ['nothing', '(just false)', '(just true)'], '(isOfHLevelMaybe 0 isSetBool)'),
                    4: ('Bool × Bool', ['(false , false)', '(false , true)', '(true , false)', '(true , true)'], '(isSet× isSetBool isSetBool)')}
        carrier, elements, set_proof = carriers[n]
        out += [f'  A{i} : Type ℓ', f'  A{i} = Lift {{j = ℓ}} ({carrier})']
        point = lambda j: f'm{i}c{j}'
        for j in range(n):
            out.append(f'  pattern {point(j)} = lift {elements[j]}')
        out.append(f'  mul{i} : A{i} → A{i} → A{i}')
        kind = mode(table, n)
        if kind == 'constant': out.append(f'  mul{i} _ _ = {point(table[0])}')
        elif kind == 'left': out.append(f'  mul{i} x _ = x')
        elif kind == 'right': out.append(f'  mul{i} _ y = y')
        else:
            for x in range(n):
                row = table[n*x:n*(x+1)]
                if len(set(row)) == 1:
                    out.append(f'  mul{i} {point(x)} _ = {point(row[0])}')
                else:
                    for y in range(n): out.append(f'  mul{i} {point(x)} {point(y)} = {point(row[y])}')
        equation_, law = LAWS[model['obstruction']['law']]
        values = model['obstruction']['assignment']
        out += [f'  failed{i} : Equation', f'  failed{i} = {agda_term(equation_[0])} , {agda_term(equation_[1])}',
                f'  at{i} : ℕ → A{i}']
        if len(values) == 1: out.append(f'  at{i} _ = {point(values[0])}')
        else:
            out += [f'  at{i} zero = {point(values[0])}', f'  at{i} (suc _) = {point(values[1])}']
        result = scalar(equation_[0], values, n, table)
        out.append(f'  distinguish{i} : A{i} → Bool')
        for j in range(n): out.append(f'  distinguish{i} {point(j)} = ' + ('false' if j == result else 'true'))
        args = ' '.join(point(v) for v in values)
        out += [f'  reject{i} : (e : Equation) → Holds e mul{i} → Adequate {{ℓ}} e → ⊥',
                f'  reject{i} e holds adequate =',
                f'    let pair = Adequate.reconstruct adequate A{i} (isOfHLevelLift 2 {set_proof}) {point(0)} mul{i} holds',
                '        structure = fst pair', '        recover = snd pair',
                f'        path = change-stroke recover at{i} (fst failed{i})',
                f'          ∙ Necessary.{law} structure {args}',
                f'          ∙ sym (change-stroke recover at{i} (snd failed{i}))',
                f'    in false≢true (cong distinguish{i} path)']
    return '\n'.join(out) + '\n'


def tree_prefixes(budget):
    """Complete trees below budget, or a prefix ending at its last operation."""
    yield None, budget, False
    if budget == 1:
        yield ('hole', 'hole'), 0, True
        return
    for left, remaining, stopped in tree_prefixes(budget - 1):
        if stopped:
            yield (left, 'hole'), 0, True
        else:
            for right, rest, stop in tree_prefixes(remaining):
                yield (left, right), rest, stop


def emit(cover):
    models = cover['models']
    chunks = {}
    coverage = [HEADER.replace('@MODULE@', 'GeneratedMinimumCoverage'),
        'open import SynthesisMinimumSupport']
    coverage += [f'import GeneratedMinimumShape{i}' for i in range(len(cover['records']))]
    coverage += ['module Coverage (ℓ : Level) where', '  open Support ℓ']
    index_rows, next_id = [], 0
    for shape_id, record in enumerate(cover['records']):
        witnesses = [HEADER.replace('@MODULE@', f'GeneratedMinimumShape{shape_id}'),
            'open import SynthesisMinimumSupport', 'module Witnesses (ℓ : Level) where', '  open Support ℓ']
        masks = {}
        coverage.append(f'  module W{shape_id} = GeneratedMinimumShape{shape_id}.Witnesses ℓ')
        shape = record['shape']
        m = leaf_count(shape)
        args = [f'x{i}' for i in range(m)]
        raw = equation(shape, [f'(var {x})' for x in args])
        coverage += [f'  shape{shape_id} : (' + ' '.join(args) + f' : ℕ) → Canonical ({raw}) → Adequate {{ℓ}} ({raw}) → ⊥']
        for leaf_ in record['leaves']:
            prefix = leaf_['prefix']; p = len(prefix); used = max(prefix, default=-1) + 1
            names = [f'x{i}' for i in range(p, m)]
            patterns = list(map(str, prefix)) + names
            if leaf_['kind'] == 'noncanonical':
                patterns[p] = natpat(leaf_['bound'] + 1, f'x{p}')
                coverage.append(f'  shape{shape_id} ' + ' '.join(patterns) + ' normal adequate = false≢true normal')
                continue
            ident = next_id; next_id += 1
            nat_values = list(map(str, prefix)) + names
            raw = equation(shape, [f'(var {x})' for x in nat_values])
            bind = ('(' + ' '.join(names) + ' : ℕ) → ') if names else ''
            lhs, rhs, variables = templates(shape, prefix, used)
            if leaf_['kind'] == 'constant':
                v = leaf_['value']
                eq0 = label(shape, iter([0] * m))
                leftval = scalar(eq0[0], (v,), 2, (1, 1, 1, 0))
                path = f'(Adequate.valid adequate Two boolean all{v})'
                path = f'(cong lower {path})'
                if leftval: path = f'(sym {path})'
                witnesses += [f'  cut{ident} : {bind}Adequate {{ℓ}} ({raw}) → ⊥',
                              f'  cut{ident} ' + ' '.join(names) + f' adequate = false≢true {path}']
            elif leaf_['kind'] == 'boolean':
                fixed = dict(enumerate(leaf_['values']))
                key = tuple(leaf_['values'])
                if key not in masks:
                    mask_id = len(masks); masks[key] = mask_id
                    witnesses.append(f'  env{mask_id} : ℕ → Two')
                    for j, value in enumerate(key): witnesses.append(f'  env{mask_id} {natpat(j)} = b{value}')
                    witnesses.append(f'  env{mask_id} {natpat(len(key), "rest")} = b0')
                env = f'env{masks[key]}'
                vals = [f'b{fixed[x]}' if x in fixed else f'z{x}' for x in list(prefix) + list(range(used, variables))]
                a, b = sides(shape, vals, 'bop')
                zs = [f'z{x}' for x in range(used, variables)]
                forall = ('(' + ' '.join(zs) + ' : Two) → ') if zs else ''
                witnesses.append(f'  bad{ident} : {forall}PathP (λ _ → Two) {a} {b} → ⊥')
                witnesses += case_proof(f'bad{ident}', lhs, rhs, variables, 2, (1,1,1,0), lambda x:f'b{x}', True, fixed)
                witnesses += [f'  cut{ident} : {bind}Adequate {{ℓ}} ({raw}) → ⊥',
                              f'  cut{ident} ' + ' '.join(names) + f' adequate = bad{ident} ' +
                              ' '.join(f'({env} {x})' for x in names) + f' (Adequate.valid adequate Two boolean {env})']
            else:
                model_id = leaf_['model']; model = models[model_id]
                vals = [f'z{x}' for x in list(prefix) + list(range(used, variables))]
                a, b = sides(shape, vals, f'mul{model_id}')
                witnesses.append(f'  holds{ident} : (' + ' '.join(f'z{x}' for x in range(variables)) + f' : A{model_id}) → {a} ≡ {b}')
                witnesses += case_proof(f'holds{ident}', lhs, rhs, variables, model['size'], model['table'], lambda x:f'm{model_id}c{x}')
                envargs = list(map(str, range(used))) + names
                witnesses += [f'  cut{ident} : {bind}Adequate {{ℓ}} ({raw}) → ⊥',
                              f'  cut{ident} ' + ' '.join(names) + f' = reject{model_id} ({raw}) (λ env → holds{ident} ' +
                              ' '.join(f'(env {x})' for x in envargs) + ')']
            coverage.append(f'  shape{shape_id} ' + ' '.join(patterns) + ' normal adequate = ' + f'W{shape_id}.cut{ident} ' + ' '.join(names) + ' adequate')
        chunks[f'GeneratedMinimumShape{shape_id}.agda'] = '\n'.join(witnesses) + '\n'
        it = iter(args)
        def sized(t):
            if t is None: return '(leaf ' + next(it) + ')'
            n, k = leaf_count(t[0])-1, leaf_count(t[1])-1
            return f'(fork {sized(t[0])} {sized(t[1])})'
        index_rows.append(f"  reject-small {sized(shape)} normal cheap adequate = shape{shape_id} " + ' '.join(args) + ' normal adequate')
    coverage += ['  reject-small : {n : ℕ} (t : Sized (suc n)) → Canonical (unerase t) → n < 6 → Adequate {ℓ} (unerase t) → ⊥']
    coverage += index_rows
    def cutoff(t):
        if t == 'hole': return '_'
        if t is None: return '(leaf _)'
        return f'(fork {cutoff(t[0])} {cutoff(t[1])})'
    for prefix, _, stopped in tree_prefixes(7):
        if stopped:
            coverage.append(f'  reject-small {cutoff(prefix)} normal cheap adequate = ¬m+n<m {{m = 6}} cheap')
    coverage += ['  no-cheaper : (f : Formula) → cost (fst f) < 6 → Adequate {ℓ} (fst f) → ⊥',
      '  no-cheaper (e , normal) cheap adequate =',
      '    reject-small (index-equation e)',
      '      (subst Canonical (sym (retract-equation e)) normal) cheap',
      '      (subst (Adequate {ℓ}) (sym (retract-equation e)) adequate)']
    return chunks, '\n'.join(coverage)+'\n'


def write_changed(path, text):
    if not path.exists() or path.read_text(encoding='utf-8') != text:
        path.write_text(text, encoding='utf-8')


if __name__ == '__main__':
    cover = json.loads((BASE / 'results/minimality-prefix-cover.json').read_text())
    write_changed(BASE / 'agda/SynthesisMinimumSupport.agda', support(cover['models']))
    chunks, coverage = emit(cover)
    for name, text in chunks.items():
        write_changed(BASE / 'agda' / name, text)
    write_changed(BASE / 'agda/GeneratedMinimumCoverage.agda', coverage)
    first = coverage.split('  module W0 =', 1)[1].split('  module W1 =', 1)[0]
    first = '  module W0 =' + first
    first = '\n'.join(line for line in first.splitlines() if not line.startswith('  shape0 0 0 '))
    negative = HEADER.replace('@MODULE@', 'SynthesisMinimumMissingCase')
    negative += '\nopen import SynthesisMinimumSupport\nimport GeneratedMinimumShape0\nmodule Missing (ℓ : Level) where\n  open Support ℓ\n' + first + '\n'
    write_changed(BASE / 'agda/negative/SynthesisMinimumMissingCase.agda', negative)
    negative = HEADER.replace('@MODULE@', 'SynthesisMinimumBadRejection')
    negative += '\nopen import SynthesisMinimumSupport\nmodule Bad (ℓ : Level) where\n  open Support ℓ\n  bad : PathP (λ _ → Two) b0 b0 → ⊥\n  bad p = false≢true (cong lower p)\n'
    write_changed(BASE / 'agda/negative/SynthesisMinimumBadRejection.agda', negative)
    print(json.dumps({'witness_modules': len(chunks), 'witness_lines': sum(len(t.splitlines()) for t in chunks.values()), 'coverage_lines': len(coverage.splitlines())}))
