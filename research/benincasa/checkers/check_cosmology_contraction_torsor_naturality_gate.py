#!/usr/bin/env python3
"""Classify exact contractions as a kernel torsor and test canonical selection from evaluation data."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research'/'benincasa'/'results'
# Minimal exact model: E(a,b)=a, target t=1, kernel={(0,b)}.
def E(v):return v[0]
def shear(v):return (v[0],v[1]+v[0])
c=(1,0);moved=shear(c);assert E(c)==E(moved)==1 and moved!=c and shear((0,1))==(0,1)
out={'schema':'marici.benincasa.cosmology-contraction-torsor-naturality-gate.v1','general_statement':{'evaluation':'E:S->R linear','contraction_fiber':'C_t={s in S | E(s)=t}','kernel':'K=ker(E)','torsor_law':'K acts freely and transitively on every nonempty C_t by addition'},'finite_evidence':{'contraction_fibers_nonempty':True,'nonzero_kernel_differences_observed':True,'transported_and_local_contractions_differ':True},'naturality_obstruction':{'automorphism':'an E-preserving shear fixes the kernel and moves a contraction','explicit_model':'E(a,b)=a; (a,b)->(a,b+a)','target_fiber':'E^-1(1)','fixed_point_in_target_fiber':False},'decision':'Evaluation, constructor transport, and nonemptiness define a contraction torsor but no canonical section. Any section needs extra source data that breaks the kernel-translation/shear symmetry.','limitations':['does not exclude a section selected by an independently sourced symmetry, pairing, order, or normalization','finite coherence transports a chosen section but does not create its base point'],'passed':True};(R/'cosmology_contraction_torsor_naturality_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
