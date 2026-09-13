#!/usr/bin/env python3
"""Show adjacent hyperbolic reduction requires localization over integral gaps."""

import json, math
from fractions import Fraction
from pathlib import Path

def gcd_all(xs):
 g=0
 for x in xs:g=math.gcd(g,abs(x))
 return g
def main():
 x,y=2,3
 entries=[x,x*y,y]
 alternating_first_invariant=gcd_all(entries)
 adjacent_pivot=x
 # The standard elimination coefficient A_12/A_01 is y/x.
 coefficient=Fraction(y,x)
 assert alternating_first_invariant==1 and adjacent_pivot==2
 assert coefficient.denominator!=1
 result={'schema':'marici.coherence.integral-chain-congruence-localization-obstruction.v1','gaps':[x,y],'upper_entries':entries,'integral_alternating_first_invariant':alternating_first_invariant,'claimed_adjacent_first_block_weight':adjacent_pivot,'standard_elimination_coefficient':str(coefficient),'unimodular_adjacent_normal_form_possible':False,'localized_normal_form_possible':True,'ring_generic_survivors':['Pfaffian polynomial identity','cofactor kernel identity','alternating charge fold'],'requires_selected_gap_units':['adjacent hyperbolic block decomposition','contractibility of each selected pair']}
 Path(__file__).with_name('integral-chain-congruence-localization-obstruction.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
