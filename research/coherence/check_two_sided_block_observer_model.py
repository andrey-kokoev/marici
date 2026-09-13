#!/usr/bin/env python3
"""Exact finite toy block with past/future tails and zero exterior boundary."""
import json, random
from fractions import Fraction
from pathlib import Path

def tails(u,rho):
 n=len(u);past=[Fraction(0)]*n;future=[Fraction(0)]*n
 for i in range(n):past[i]=u[i]+(rho*past[i-1] if i else 0)
 for i in range(n-1,-1,-1):future[i]=u[i]+(rho*future[i+1] if i+1<n else 0)
 return past,future
def main():
 rng=random.Random(20260930);rho=Fraction(3,5);cases=[]
 for trial in range(100):
  u=[Fraction(rng.randrange(-9,10),rng.randrange(1,10)) for _ in range(21)];past,future=tails(u,rho)
  from_past=[past[i]-(rho*past[i-1] if i else 0) for i in range(len(u))]
  from_future=[future[i]-(rho*future[i+1] if i+1<len(u) else 0) for i in range(len(u))]
  assert from_past==u==from_future
  rp,rf=tails(list(reversed(u)),rho);assert rp==list(reversed(future)) and rf==list(reversed(past))
  cases.append({'trial':trial,'events':len(u),'two_sided_reconstruction':True,'reflection_swaps_tails':True})
 result={'schema':'marici.coherence.two-sided-block-observer-model.v1','rho':str(rho),'cases':len(cases),'all_exact':True,'left_boundary':'past before first event = 0','right_boundary':'future after last event = 0','past_recurrence':'P_n=u_n+rho P_(n-1)','future_recurrence':'F_n=u_n+rho F_(n+1)','local_consistency':'u_n=P_n-rho P_(n-1)=F_n-rho F_(n+1)','reflection':'reverses events and swaps past/future tails'}
 Path(__file__).with_name('two-sided-block-observer-model.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
