#!/usr/bin/env python3
"""Exact arbitrary-input census for the sourced one-loop BCFW term-count formula."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
rows=[];passed=True
for n in range(4,51):
 for k in range(2,n-1):
  count=math.comb(n-2,k)*math.comb(n-2,k-2)
  parity_k=n-k
  parity_count=math.comb(n-2,parity_k)*math.comb(n-2,parity_k-2)
  checks={'nonnegative_integer':isinstance(count,int) and count>=0,'parity_symmetric':count==parity_count,'mhv_specialization':k!=2 or count==(n-2)*(n-3)//2,'anti_mhv_specialization':k!=n-2 or count==(n-2)*(n-3)//2}
  ok=all(checks.values());passed &= ok;rows.append({'n':n,'k':k,'parity_k':parity_k,'terms':count,'checks':checks,'passed':ok})
out={'schema':'marici.nima.arbitrary-nk-one-loop-bcfw-term-count.v1','source':'arXiv:1212.5605 acquired TeX, one-loop count following the Kermit construction','formula':'binom(n-2,k) binom(n-2,k-2)','convention':'MHV has k=2','range':{'n':[4,50],'all_physical_k':True},'typed_instances':len(rows),'results':rows,'passed':passed,'scope':'Combinatorial count of nonvanishing one-loop BCFW contributions; no construction or equality check for k>2.'}
p=ROOT/'research/nima/results/arbitrary-nk-one-loop-bcfw-term-count.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':passed,'typed_instances':len(rows),'largest':rows[-1]},indent=2));raise SystemExit(0 if passed else 1)
