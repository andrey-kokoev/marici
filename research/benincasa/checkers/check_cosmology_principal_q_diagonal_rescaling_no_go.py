#!/usr/bin/env python3
"""Classify diagonal rescalings of the q-based Gysin candidate."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
prior=json.loads((R/'cosmology_principal_q_Gysin_denominator_fiber_dependence.json').read_text());assert prior['passed']
def coeffs(a,b,c):return ((a-c)**2,(b-c)**2,2*(c*c-a*b-a*c-b*c))
# Deliberate finite failures supplement the symbolic implication.
tests=[]
for a in range(-4,5):
 for b in range(-4,5):
  for c in range(-4,5):
   if a and b and c:
    z=coeffs(a,b,c);assert z!=(0,0,0);tests.append({'abc':[a,b,c],'Lambda_coefficients':list(z)})
# If all coefficients vanished over Q, first two squares force a=c and b=c;
# the cross coefficient then equals -4*c^2, forcing a=b=c=0.
out={'schema':'marici.benincasa.cosmology-principal-q-diagonal-rescaling-no-go.v1','conjecture':'nonzero rational diagonal rescalings cancel fiber dependence in the q-based Gysin denominator','assignment':'(s1,s2,s3)=(a*A,b*B,c*(A+B))','Lambda_coefficients':{'A^2':'(a-c)^2','B^2':'(b-c)^2','A*B':'2*(c^2-a*b-a*c-b*c)'},'zero_Lambda_implication':['a=c','b=c','-4*c^2=0','a=b=c=0'],'nonzero_abc_has_nonzero_Lambda':True,'denominator_if_nonzero':'a*b*c*A*B*(A+B)*Lambda, homogeneous fiber degree 5','nonzero_denominator_base_independent':False,'bounded_nonzero_triples_tested':len(tests),'bounded_failures':0,'conjecture_disposition':'falsified for all rational diagonal rescalings','degenerate_escape':'a*b*c=0 or Lambda=0 makes the Gysin denominator identically zero, not a valid support pullback','source_authority_supplied':False,'next_conjecture':'an arbitrary nondegenerate homogeneous linear assignment from the two fiber functions to (s1,s2,s3) can yield a base-only Gysin denominator','next_falsifier':'use homogeneity in the fiber variables to prove every nonzero pulled denominator has total fiber degree five','passed':True};(R/'cosmology_principal_q_diagonal_rescaling_no_go.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
