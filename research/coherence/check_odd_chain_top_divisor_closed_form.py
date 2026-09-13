#!/usr/bin/env python3
"""Closed formula for the top Pfaffian divisor of an odd chain."""

import json, random
from pathlib import Path

def cofactor_cost(c,omit):
 verts=[i for i in range(len(c)+1) if i!=omit];z=0
 for a,b in zip(verts[0::2],verts[1::2]):z+=sum(c[a:b])
 return z
def closed(c,r):
 # Unmatched vertex 2r: forced matching left uses even edges, right odd edges.
 return sum(c[i] for i in range(0,2*r,2))+sum(c[i] for i in range(2*r+1,len(c),2))
def main():
 rng=random.Random(20260925);rows=[]
 for n in range(3,16,2):
  for trial in range(40):
   c=[rng.randrange(0,10) for _ in range(n-1)];allc=[cofactor_cost(c,j) for j in range(n)];ev=[cofactor_cost(c,j) for j in range(0,n,2)];cl=[closed(c,r) for r in range((n+1)//2)]
   assert ev==cl and min(allc)==min(ev)
   rows.append({'points':n,'trial':trial,'gap_costs':c,'top_divisor_valuation':min(ev),'even_omission_costs':ev})
 result={'schema':'marici.coherence.odd-chain-top-divisor-closed-form.v1','cases':len(rows),'all_exact':True,'formula':'v_p(D_m)=min_r(sum even gaps left of 2r + sum odd gaps right of 2r)','odd_omissions_needed_for_minimum':False,'interpretation':'top cofactor gcd is controlled by the cheapest even-position residual pivot','rows':rows}
 from pathlib import Path
 Path(__file__).with_name('odd-chain-top-divisor-closed-form.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('cases','all_exact','formula','odd_omissions_needed_for_minimum','interpretation')},indent=2))
if __name__=='__main__':main()
