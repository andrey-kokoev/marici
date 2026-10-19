"""Unique degree-two comparisons for actual DG context composition.

Uses the owner's basis and differential. No boundary-zero cycle is discarded.
"""
import contextlib
from collections import defaultdict
from dataclasses import dataclass
from functools import lru_cache
import io
import json
from pathlib import Path
import runpy
ROOT=Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    c=runpy.run_path(str(ROOT/'research/strominger/checkers/check_relation_continuation_context.py'))
S=c['S']; a=c['a']; owner=c['owner']; delta=a['delta']; clean=c['clean']
base=owner['word']('abase')

@lru_cache(None)
def cached_images(C): return c['generator_images'](C)
def images(C): return cached_images(S.ImmutableMatrix(C))
def T(C,chain): return c['substitute'](chain,images(C))
def plus(*chains):
    out=defaultdict(lambda:S.Integer(0))
    for chain in chains: c['add_scaled'](out,chain,1)
    return clean(out)
def minus(chain): return {p:-v for p,v in chain.items()}

basis2=a['bases'][2]
# Each h_i k_j boundary has a UNIQUE -x_i k_j pivot (i,j nonroot).
pivots={path:(path[0][0]+'x'+path[0][2:],path[1]) for path in basis2}
assert len(basis2)==len(set(pivots.values()))==109
all_pivots=set(pivots.values())
for path,pivot in pivots.items():
    boundary=delta(owner['word'](*path))
    assert boundary[pivot]==-1 and set(boundary)&all_pivots=={pivot}

def fill(cycle):
    assert not delta(cycle), 'not a cycle'
    result=clean({path:-cycle.get(pivot,0) for path,pivot in pivots.items()})
    assert delta(result)==cycle, 'cycle not filled in the declared owner complex'
    return result

@dataclass(frozen=True)
class Comparison:
    first: object
    second: object
    composite: object
    defect: dict
    filler: dict

@lru_cache(None)
def comparison(M,N):
    # Pullback convention: T_M after T_N compares to T_(N M).
    defect=plus(T(M,T(N,base)),minus(T(N*M,base)))
    return Comparison(M,N,S.ImmutableMatrix(N*M),defect,fill(defect))
def compare(M,N): return comparison(S.ImmutableMatrix(M),S.ImmutableMatrix(N))

def validate(witness):
    assert witness==compare(witness.first,witness.second)
    assert delta(witness.filler)==witness.defect

contexts=tuple(S.ImmutableMatrix(C) for C in c['contexts'])
checks={}
actual=compare(c['M'],c['N'])
assert actual.defect==c['defect'] and len(actual.defect)==47
validate(actual)
checks['actual47_term_cycle_has_retained_degree_two_filler']=bool(actual.filler)
checks['degree_two_boundary_is_injective_by109_distinct_pivots']=True
# Owner build checks rank(d1)=137 and rank(d2)=109; C1 has246 generators.
assert len(a['bases'][1])==246 and len(a['bases'][0])==138
checks['owner_H1_zero_dimension_witness']=246-137-109==0

for M in contexts:
    assert not compare(c['I'],M).filler and not compare(M,c['I']).filler
    for N in contexts:
        validate(compare(M,N))
        # All non-base generators compose strictly, hence homotopy support
        # is exactly abase; state base is unchanged.
        for name in a['arrows']:
            if name=='abase': continue
            assert T(M,T(N,owner['word'](name)))==T(N*M,owner['word'](name))
        assert T(N,base).get(('abase',),0)==1
checks['twenty_five_pair_fillers_and_units']=True
checks['comparison_homotopy_supported_only_on_arrow_base']=True

triple_count=0
for L in contexts:
    for M in contexts:
        for N in contexts:
            # Two comparisons from T_L T_M T_N to T_(N M L).
            # H_LM(T_N abase)=H_LM(abase), since its base coefficient is1.
            left=plus(compare(L,N*M).filler,T(L,compare(M,N).filler))
            right=plus(compare(M*L,N).filler,compare(L,M).filler)
            assert left==right
            triple_count+=1
checks['all125_triple_comparisons_agree_as_degree_two_chains']=True

@dataclass(frozen=True)
class CoherentStep:
    before: object
    after: object
    comparison: Comparison

def advance(packet,command):
    result=c['step'](packet,command)
    witness=compare(packet.context,c['matrix_for'](command))
    assert result.context==witness.composite and result.parent is packet
    validate(witness)
    return CoherentStep(packet,result,witness)

packet=c['initial']; retained=[]
for command in c['commands']:
    result=advance(packet,command)
    retained.append(result)
    packet=result.after
assert all(s.after.parent is s.before for s in retained)
checks['actual_context_updates_retain_predecessor_and_composition_witness']=True

# A zero or sign-reversed substitute for the actual filler is not accepted.
assert actual.defect
assert delta({})!=actual.defect and delta(minus(actual.filler))!=actual.defect
checks['zero_and_reversed_filler_hostiles_rejected']=True
assert all(checks.values())
out={'schema':'marici.context-composition-fillers.v1','status':'pass','checks':checks,
     'actual_defect_terms':len(actual.defect),'actual_filler_terms':len(actual.filler),
     'actual_filler':[{ 'path':list(path),'coefficient':str(value)} for path,value in sorted(actual.filler.items())],
     'degree_two_pivots':len(pivots),'pair_cases':25,'triple_cases':triple_count,
     'general_argument':'H1=0 gives existence for each context-composition cycle; injective d2 gives uniqueness, units and triple coherence when the declared chain-map/strict-nonbase premises hold',
     'verification_scope':'exact actual-source calculations; universal algebraic argument stated separately, no new Agda proof or recorder-seam map'}
(ROOT/'research/strominger/results/context-composition-fillers-v1.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
