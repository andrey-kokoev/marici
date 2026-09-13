#!/usr/bin/env python3
"""Check cross-multiplied paired Pfaffian refinement without division."""

import json, random
from pathlib import Path

def pf(gaps,mod=None):
 z=1
 for x in gaps[0::2]:z=z*x if mod is None else z*x%mod
 return z
def main():
 rng=random.Random(20260921);rows=[]
 for mod in (None,6,8,10,12):
  for parity in (0,1):
   for _ in range(50):
    gaps=[rng.randrange(-6,7) for _ in range(parity+3)];i=parity
    a,g,b=[rng.randrange(-6,7) for _ in range(3)];rho=a*g*b
    old=gaps[:];old[i]=rho;new=old[:i]+[a,g,b]+old[i+1:]
    po,pn=pf(old,mod),pf(new,mod)
    if parity==0:
     lhs=rho*pn;rhs=a*b*po
    else:
     lhs=pn;rhs=g*po
    if mod is not None:lhs%=mod;rhs%=mod
    assert lhs==rhs
    rows.append({'modulus':'integers' if mod is None else mod,'old_gap_parity':parity,'identity':True})
 result={'schema':'marici.coherence.ring-generic-paired-pfaffian-correspondence.v1','cases':len(rows),'all_exact':True,'selected_gap_relation':'rho * tau_new = alpha beta * tau_old','unselected_gap_relation':'tau_new = gamma * tau_old','division_used':False,'interpretation':'over a bare ring refinement is a correspondence; localization promotes it to an invertible transition'}
 from pathlib import Path
 Path(__file__).with_name('ring-generic-paired-pfaffian-correspondence.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
