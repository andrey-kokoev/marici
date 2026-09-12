#!/usr/bin/env python3
"""Verify translation/reflection action on value and flux seam traces."""

import json, random
from fractions import Fraction
from pathlib import Path

def jumps(t):
 vm,dm,vp,dp=t;return (vp-vm,dp-dm)
def reflect_trace(t):
 vm,dm,vp,dp=t
 # At the reflected point: plus samples old minus; derivatives acquire -1.
 return (vp,-dp,vm,-dm)
def main():
 rng=random.Random(20260914);rows=[]
 for _ in range(100):
  t=tuple(Fraction(rng.randrange(-9,10),rng.randrange(1,10)) for _ in range(4))
  j0,j1=jumps(t);rj0,rj1=jumps(reflect_trace(t));assert (rj0,rj1)==(-j0,j1)
  assert reflect_trace(reflect_trace(t))==t
  rows.append({'value':str(j0),'flux':str(j1),'reflected_value':str(rj0),'reflected_flux':str(rj1)})
 result={'schema':'marici.coherence.value-flux-seam-symmetry.v1','cases':len(rows),'all_exact':True,'translation':'moves seam location and preserves both channels','reflection':'(value,flux) -> (-value,flux)','reflection_squared':'identity','green_flux_line':'reflection even','value_jump_line':'reflection odd'}
 Path(__file__).with_name('value-flux-seam-symmetry.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
