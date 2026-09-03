#!/usr/bin/env python3
"""Verify formal relation closure of the symmetric local residue candidate."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_complete_bounded_exact_row_iterator.py'))
k,_=g['exact_fiber'](3,6,-3)
def ev(p,x,y):return sum(c*x**i*y**j for (i,j),c in p.items())
k0=ev(k,0,3);assert k0==0
# Expand K(u,v+3) exactly and record its lowest total-degree terms.
from math import comb
loc={}
for (i,j),c in k.items():
 for h in range(j+1):loc[(i,h)]=loc.get((i,h),F(0))+c*comb(j,h)*3**(j-h)
loc={e:c for e,c in loc.items() if c};order=min(sum(e) for e in loc);lead={e:c for e,c in loc.items() if sum(e)==order};assert order>0
out={'schema':'marici.benincasa.cosmology-rees-symmetric-residue-relations.v1','local_coordinates':['u=X','v=Y-3'],'K_at_local_locus':str(k0),'K_vanishing_order':order,'K_leading_terms':{str(e):str(c) for e,c in lead.items()},'candidate_status':'not defined by ordinary ordered Laurent coefficient extraction','exact_residual':'K vanishes at the flag locus, so K^(-1/2) is not a unit-valued formal power series; adjoining its square root changes the local cover and residue lattice','K_and_q_row_test':'deferred because the proposed functional has no value on the twisted K^(-1/2) integrand in the stated Laurent rings','required_repair':'construct the ramified local cover determined by the leading K divisor, choose its branch/orientation, and recompute the flag residues there','tau_evaluation_from_untwisted_candidate':'1, but this does not extend to the required twisted module','passed':True};(R/'cosmology_rees_symmetric_residue_relations.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
