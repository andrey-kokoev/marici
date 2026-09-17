#!/usr/bin/env python3
"""Exact finite prime-power inventory for every compact support window."""
import argparse,json,math
from pathlib import Path

def von_mangoldt(n):
 for p in range(2,int(math.sqrt(n))+2):
  if n%p==0:
   m=n
   while m%p==0:m//=p
   return math.log(p) if m==1 else 0.0
 return math.log(n) # n is prime

def inventory(L):
 cutoff=math.exp(2*L);items=[]
 for n in range(2,int(math.floor(cutoff))+1):
  lam=von_mangoldt(n)
  if lam:
   items.append({'n':n,'shift':math.log(n),'lambda':lam,'coefficient':lam/math.sqrt(n),'threshold_half_length':math.log(n)/2})
 return items

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--max-L',type=float,default=2.0);a=ap.parse_args();items=inventory(a.max_L);checks={'L055':[x['n'] for x in inventory(.55)]==[2,3],'L075':[x['n'] for x in inventory(.75)]==[2,3,4],'coeff4':abs(next(x['coefficient'] for x in items if x['n']==4)-math.log(2)/2)<1e-15};out={'schema':'marici.voevodsky.prime-power-support-inventory.v1','max_half_length':a.max_L,'support_cutoff':math.exp(2*a.max_L),'count':len(items),'items':items,'checks':checks,'passed':all(checks.values()),'rh_proved':False};p=Path(__file__).parents[1]/'results'/'prime_power_support_inventory.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'count':len(items),'first':[x['n'] for x in items[:12]],'checks':checks,'passed':out['passed']},indent=2));assert out['passed']
if __name__=='__main__':main()
