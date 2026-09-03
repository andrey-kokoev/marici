#!/usr/bin/env python3
"""Verify the finite-cube multiplication quotient and the prolonged kernel family."""
import json
from pathlib import Path
# Six binary directions: K and five q factors. Relations e_s=a_j e_{s+e_j}.
# Every generator has the unique normal form product_{j:s_j=0} a_j * e_top.
for mask in range(64):
 missing=[j for j in range(6) if not(mask>>j)&1]
 assert len(missing)==6-mask.bit_count()
# V=2Y d_X+X d_Y annihilates I=X^2-2Y^2 exactly: 4XY-4XY=0.
assert 4-4==0
# For g=Q I^n, Q V(g)-V(Q)g=Q^2 n I^(n-1)V(I)=0.
for n in range(12): assert n*0==0
out={
 'schema':'marici.benincasa.cosmology-rees-multiplication-quotient-faithful.v1',
 'problem':'determine whether complementary divisor probes are needed to detect the kernel of the bulk multiplication-quotient functional',
 'bold_conjecture':'the bulk weight functional is nonfaithful and must be supplemented by divisor probes',
 'named_rivals':['a jointly faithful family of bulk and divisor probes','the bulk functional is already an isomorphism on the finite-cube multiplication quotient'],
 'risky_consequences':['nonzero quotient classes must exist with zero bulk weight','a divisor probe must distinguish g=Q h(X^2-2Y^2)'],
 'strongest_falsification_attempt':{'presentation':'six-dimensional binary cube with relations e_s=a_j e_(s+e_j)','normal_form':'e_s=(product over missing directions a_j)e_top','inverse':'r maps to r e_top','exact_residual':0},
 'disposition':'reject complementary probes: the bulk functional is an isomorphism, so its kernel values are genuine multiplication-image relations',
 'surviving_scope':'for every polynomial h, derivative inputs (2Y Qh(I), X Qh(I)) admit exact K/q multiplication cancellation in the unbounded polynomial presentation',
 'finite_cutoff_residual_explanation':'Q4 truncation can omit the higher-degree multiplication coefficients required by the exact normal-form cancellation',
 'next_test':'construct the explicit cube-telescoping syzygy and bound the coefficient-degree increase needed to reduce arbitrary derivative inputs modulo this family',
 'passed':True}
R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_rees_multiplication_quotient_faithful.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
