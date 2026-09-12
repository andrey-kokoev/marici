#!/usr/bin/env python3
"""Verify normalized odd residual charges are alternating gap products."""

import json, random
from fractions import Fraction
from pathlib import Path
import check_typed_residual_recurrence as core

def product(xs):
 z=Fraction(1)
 for x in xs:z*=x
 return z
def main():
 rng=random.Random(20260912);rows=[]
 for n in (1,3,5,7,9):
  for trial in range(20):
   gaps=[Fraction(rng.randrange(1,9),rng.randrange(1,9)) for _ in range(n-1)];y=[Fraction(1)]
   for g in gaps:y.append(y[-1]*g)
   u=core.cof(core.matrix(y))
   right_profile=[y[-1]/yi for yi in y] # cross column to a unit point after unit gap
   left_profile=y[:]                    # cross row from a unit point before unit gap
   qout=sum(ui*ri for ui,ri in zip(u,right_profile))
   qin=sum(li*ui for li,ui in zip(left_profile,u))
   expected_out=product(gaps[0::2]);expected_in=product(gaps[1::2])
   assert qout==expected_out and qin==expected_in
   rows.append({'points':n,'trial':trial,'qout':str(qout),'qin':str(qin)})
 result={'schema':'marici.coherence.odd-block-alternating-charges.v1','cases':len(rows),'all_charge_formulas_exact':True,'outgoing':'product of gaps with even index','incoming':'product of gaps with odd index','singleton_charges':'both empty products equal one','sewing':'qout(left) * separating_gap * qin(right)'}
 Path(__file__).with_name('odd-block-alternating-charges.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
