"""Witness-bearing closure in a finite groupoid model with C2 automorphisms.
Two path labels are retained. Higher equalities here are discrete (a 1-type).
This is a semantic test, not a proof-assistant implementation of arbitrary HoTT.
"""
from dataclasses import dataclass
from pathlib import Path
import contextlib,io,json
from dependent_container_normalizer import Atom,Binder,normalize,encode,decode
with contextlib.redirect_stdout(io.StringIO()):
    import check_dependent_sigma_pi_full_chains as ground

@dataclass(frozen=True)
class Arrow:
    source: tuple
    target: tuple
    label: int
    def __post_init__(self):
        if self.source!=self.target:raise ValueError('different components')
        if self.label not in (0,1):raise ValueError('not a C2 label')

@dataclass(frozen=True)
class HigherEquality:
    left: Arrow
    right: Arrow
    def __post_init__(self):
        if self.left!=self.right:raise ValueError('no equality between distinct C2 arrows')

def compose(a,b):
    if a.target!=b.source:raise ValueError('noncomposable arrows')
    return Arrow(a.source,b.target,a.label^b.label)

def map_object(x):return ground.outer_first(x)[-1]
def inverse_object(n):return ground.reconstruct(n)
def map_arrow(p):return Arrow(map_object(p.source),map_object(p.target),p.label)
def inverse_arrow(p):return Arrow(inverse_object(p.source),inverse_object(p.target),p.label)

sources=ground.sources()
# This deliberately enriches each finite object with the groupoid BC2.
# It is a new declared semantics for comparison fibres, not an inference
# that the prior discrete set carried these automorphisms.
for x in sources:
    for a in (0,1):
        p=Arrow(x,x,a)
        assert inverse_arrow(map_arrow(p))==p
        for b in (0,1):
            q=Arrow(x,x,b)
            assert map_arrow(compose(p,q))==compose(map_arrow(p),map_arrow(q))
            assert (p==q)==(map_arrow(p)==map_arrow(q))

# The closure record includes both FULL chains and an explicit witness.
# Sigma selects the source; Pi keeps all the named fields together.
branches=[];records=[]
for index,x in enumerate(sources):
    branches.append((index,Binder('Pi',(
        ('outer_chain',Atom(f'outer({index})')),
        ('inner_chain',Atom(f'inner({index})')),
        ('comparison',Atom(f'path({index})'))))))
    out=ground.outer_first(x);inside=ground.inner_first(x)
    assert out[-1]==inside[-1]
    for label in (0,1):
        witness=Arrow(out[-1],inside[-1],label)
        records.append((index,(out,inside,witness)))
normal=normalize(Binder('Sigma',tuple(branches)))
encoded=[encode(normal,r) for r in records]
assert len(set(encoded))==len(records)==36
for r,n in zip(records,encoded):
    assert decode(normal,*n)==r
    assert decode(normal,*n)[1][2] is r[1][2]
# Next record layer explicitly retains first-level records and their identity
# witnesses. The nontrivial label remains available inside the retained source.
next_syntax=Binder('Pi',(('retained_record',Atom('record')),
                       ('left_witness',Atom('arrow')),
                       ('right_witness',Atom('arrow')),
                       ('witness_comparison',Atom('identity_of_arrows'))))
next_normal=normalize(next_syntax)
higher_cases=refused=0
for r in records:
    p=r[1][2]
    gamma=HigherEquality(p,p)
    value=(r,p,p,gamma)
    assert decode(next_normal,*encode(next_normal,value))==value
    higher_cases+=1
    different=Arrow(p.source,p.target,p.label^1)
    try:HigherEquality(p,different)
    except ValueError:refused+=1
    else:raise AssertionError('distinct witnesses collapsed')
report={'passed':True,'model':'18 components, each carrying the one-object groupoid BC2',
 'full_chain_records_with_distinct_comparisons':len(records),
 'normalization_preserves_witness_identity':True,
 'higher_comparison_records_roundtripped':higher_cases,
 'nonexistent_higher_equalities_refused':refused,
 'source_equivalence_lifts_to_arrow_equivalence':True,
 'scope':'Finite 1-type model and opaque proof-field retention. Actual higher-dimensional fillers and arbitrary HoTT records require the general identity-transport proof and a formal backend.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/proof-relevant-container-closure.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
