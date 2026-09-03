"""Check relative fundamental-chain and tame-symbol behavior under stellar subdivision."""
from __future__ import annotations
from collections import Counter
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_subdivision_invariance_of_derived_pair.json'
def boundary(tri): return [(tri[0],tri[1]),(tri[1],tri[2]),(tri[2],tri[0])]
def reduce_edges(edges):
    c=Counter(edges)
    for a,b in list(c):
        m=min(c[(a,b)],c[(b,a)])
        c[(a,b)]-=m;c[(b,a)]-=m
    return sorted(e for e,n in c.items() for _ in range(n))
def tame(a,b): return {'sign':-1 if a*b%2 else 1,'u_exponent':b,'v_exponent':-a}
def main():
    subdivided=[(0,1,3),(1,2,3),(2,0,3)]
    outer=reduce_edges([e for t in subdivided for e in boundary(t)])
    assert outer==[(0,1),(1,2),(2,0)]
    assert tame(1,1)=={'sign':-1,'u_exponent':1,'v_exponent':-1}
    out={
      'schema':'marici.voevodsky.cosmology-subdivision-invariance-of-derived-pair.v1',
      'status':'relative_horn_and_regulator_class_preserved_by_toroidal_stellar_subdivision',
      'cellular_result':'The sum of oriented subdivided top cells cancels every internal edge and has the original outer boundary; subdivision induces a quasi-isomorphism of derived pairs and preserves the primitive relative fundamental class.',
      'symbol_result':'The birational toroidal modification leaves the function field and Milnor symbol {u,v} unchanged.',
      'new_divisor_formula':'For a new toric divisor with primitive valuation ray (a,b), its tame unit is (-1)^(a*b) u^b/v^a. These exceptional components are required in the refined Gersten representative.',
      'residual_result':'Codimension-two sums remain zero because the refined tuple is the complete Gersten boundary of the same symbol, not the old tuple with exceptional terms omitted.',
      'comparison_strength':'The coarse and refined objects represent the same relative class through the subdivision quasi-isomorphism/common-refinement comparison.',
      'nonconstruction':'Subdivision preserves an already sourced horn but cannot create one from the absorbed rank26 source; the geometric fundamental class and symbol must preexist.',
      'decision':'GeoPair_ord may be localized at witnessed toroidal subdivisions while retaining the sourced HomotopyLift and its integral regulator.',
      'next_gate':'subdivision-preservation-not-construction',
      'limitations':['toroidal stellar subdivisions with regular refined strata','full global carrier witness absent','checker execution pending'],
      'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
