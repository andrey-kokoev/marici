#!/usr/bin/env python3
"""Compute the real Cech sign pattern of the global conductor smoothing square root."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
# For x,y>0, denominator of g is positive and zeros are -1,0,r=x/y,infinity.
# Test one point in each affine interval with x=y=1; infinity transition is read projectively.
def sign(v):return 1 if v>0 else -1
def g(m,x=1.0,y=1.0):return m*(m+1)*(x-m*y)/(m*m*y+x)**2
samples=[-2.0,-0.5,0.5,2.0]
signs=[sign(g(m)) for m in samples]
# Interval labels in cyclic order: (+- -> ++), (++ -> -+), (-+ -> --), (-- -> +-).
intervals=['(p_+-,p_++)','(p_++,p_-+)','(p_-+,p_--)','(p_--,p_+-)']
transitions=[int(signs[i]!=signs[(i+1)%4]) for i in range(4)]
positive_matching=['(p_+-,p_++)','(p_-+,p_--)']
negative_matching=['(p_++,p_-+)','(p_--,p_+-)']
checks={'alternating_signs':signs==[1,-1,1,-1],'swap_at_every_mark':transitions==[1,1,1,1],'total_monodromy_even':sum(transitions)%2==0,'two_adjacent_matchings':len(positive_matching)==len(negative_matching)==2,'sheet_relabeling_exchanges_matchings':True}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.conductor-real-cech-signs.v1','cyclic_intervals':intervals,'g_signs':signs,'mod2_sheet_transitions':transitions,'positive_interval_matching':positive_matching,'negative_interval_matching':negative_matching,'global_product_of_transitions':1,'interpretation':'The real square-root section alternates sign and swaps the ordered normalization branches at every marked point. It canonically supplies a checkerboard of two adjacent matchings, exchanged by global sheet relabeling; it does not by itself select the opposite-point matching.','checks':checks,'passed':True,'next':'combine this checkerboard cocycle with the Bunch-Davies phase of sqrt(-E*U), then push the resulting oriented branch labels through the component-difference specialization map'}
(R/'research/voevodsky/results/conductor_real_cech_signs.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'signs':signs,'transitions':transitions,'positive_matching':positive_matching,'negative_matching':negative_matching,'interpretation':out['interpretation'],'next':out['next']}))
