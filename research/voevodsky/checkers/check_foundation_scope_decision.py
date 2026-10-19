"""Exact semantic and quantifier controls for the parent scope decision."""
import itertools
import json
from hashlib import sha256
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
NOTE = 'research/voevodsky/foundation-scope-decision-v1.md'
OUT = 'research/voevodsky/results/foundation-scope-decision-v1.json'

P = ('atom',)
BOTTOM = ('bottom',)
NOT_P = ('imp', P, BOTTOM)
LEM = ('or', P, NOT_P)

# The two-world reflexive/transitive chain. Persistent valuations only.
WORLDS = (0, 1)
FUTURE = {0: (0, 1), 1: (1,)}
VALUATIONS = (frozenset(), frozenset({1}), frozenset({0, 1}))

def forces(formula, world, valuation):
    tag = formula[0]
    if tag == 'atom': return world in valuation
    if tag == 'bottom': return False
    if tag == 'or': return forces(formula[1], world, valuation) or forces(formula[2], world, valuation)
    if tag == 'imp':
        return all(not forces(formula[1], v, valuation) or forces(formula[2], v, valuation) for v in FUTURE[world])
    raise ValueError('unsupported formula')

def classical(formula, value):
    tag = formula[0]
    if tag == 'atom': return value
    if tag == 'bottom': return False
    if tag == 'or': return classical(formula[1], value) or classical(formula[2], value)
    if tag == 'imp': return not classical(formula[1], value) or classical(formula[2], value)
    raise ValueError('unsupported formula')

def require(ok, msg):
    if not ok: raise ValueError(msg)

def classify_relation(bits):
    holds = lambda f, p: bits[2*f+p]
    per_foundation = all(any(holds(f,p) for p in (0,1)) for f in (0,1))
    one_common = any(all(holds(f,p) for f in (0,1)) for p in (0,1))
    return per_foundation, one_common

def main():
    # Verify persistence, not just a hand-picked list labelled Kripke.
    require(all(all(w not in val or v in val for w in WORLDS for v in FUTURE[w])
                for val in VALUATIONS), 'nonpersistent valuation')
    semantic_rows = []
    for val in VALUATIONS:
        row = dict(atom_worlds=sorted(val), LEM=[forces(LEM,w,val) for w in WORLDS],
                   not_p=[forces(NOT_P,w,val) for w in WORLDS])
        semantic_rows.append(row)
    require(all(classical(LEM,b) for b in (False,True)), 'classical tautology control')
    growing = frozenset({1})
    require(not forces(P,0,growing) and not forces(NOT_P,0,growing)
            and not forces(LEM,0,growing) and forces(LEM,1,growing), 'two-world separation')
    require(all(forces(('imp',P,P),w,val) for w in WORLDS for val in VALUATIONS), 'positive implication control')
    # Strength comparison for all binary two-foundation/two-process relations.
    relations = list(itertools.product((False,True), repeat=4))
    results = [classify_relation(bits) for bits in relations]
    require(all(not common or per for per,common in results), 'common does not imply per-foundation')
    separators = [bits for bits in relations if classify_relation(bits) == (True,False)]
    require((True,False,False,True) in separators, 'missing diagonal quantifier countermodel')
    # Literal truth-value invariance cannot hold for the identity-on-formulas
    # policy that identifies these two semantics. This excludes only that policy.
    erased_tag_equivalence = all(classical(LEM,b) for b in (False,True)) == all(
        forces(LEM,w,val) for w in WORLDS for val in VALUATIONS)
    require(not erased_tag_equivalence, 'validity tags incorrectly interchangeable')
    paths = [NOTE, 'research/conjecture_net/contracts/common-foundations-formulation-candidate.v1.json',
             'research/conjecture_net/contracts/bounded-foundation-profile.v1.json',
             'research/conjecture_net/contracts/common-foundations-conjecture-net.v1.json',
             Path(__file__).relative_to(ROOT).as_posix()]
    result = dict(schema='marici.foundation-scope-decision.v1', passed=True,
                  classical_LEM_truth_table=[classical(LEM,b) for b in (False,True)],
                  two_world_models=semantic_rows, binary_relations_checked=len(relations),
                  quantifier_separating_relations=len(separators),
                  identity_on_formulas_validity_erasure_rejected=True,
                  arbitrary_interpretations_refuted=False,
                  decision='retain_Root_F_K_E_as_parameterized_candidate; neither universal scope selected',
                  formulation_gate_discharged=False, physical_realization_admitted=False,
                  source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))

if __name__ == '__main__': main()
