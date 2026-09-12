#!/usr/bin/env python3
"""Verify that geometric reversal induces the residual Clifford swap exactly."""

import json, random
from fractions import Fraction
from pathlib import Path
import check_typed_residual_recurrence as residual


def reverse_inverse_coordinates(y):return [1/x for x in reversed(y)]
def main():
 rng=random.Random(20260912);rows=[]
 for n in (1,3,5,7,9):
  for trial in range(20):
   gaps=[Fraction(rng.randrange(1,9),rng.randrange(9,18)) for _ in range(n-1)];y=[Fraction(1)]
   for g in gaps:y.append(y[-1]*g)
   u,qout,qin=residual.typed(y)
   yr=reverse_inverse_coordinates(y);ur,qout_r,qin_r=residual.typed(yr)
   assert ur==list(reversed(u))
   assert qout_r==qin and qin_r==qout
   rows.append({'size':n,'trial':trial,'cofactor_reverses_exactly':True,'charges_swap_exactly':True})
 result={'schema':'marici.coherence.pfaffian-residual-clifford-intertwiner.v1','cases':len(rows),'all_cofactor_reversals_exact':True,'all_charge_swaps_exact':True,'identity':'Retype(Rev_pf X)=R_Cl Retype(X)','phase':'none for odd rank with inverse-coordinate geometric reversal'}
 Path(__file__).with_name('pfaffian-residual-clifford-intertwiner.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
