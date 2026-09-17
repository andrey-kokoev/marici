#!/usr/bin/env python3
"""Arb interval certificate for Re psi(1/4+iu/2) >= log(u/2)-3/2 on a compact core."""
import json,sys,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_flint'))
from flint import arb,acb,ctx
ctx.prec=192;I=acb(0,1);accepted=[];failed=[];evals=0
def F(a,b):
 global evals
 m=(a+b)/2;r=(b-a)/2;u=arb(f'[{m:.17g} +/- {r:.17g}]');z=acb(arb(1)/4)+I*u/2;evals+=1
 return z.digamma().real-(u/2).log()+arb(3)/2
def visit(a,b,d=0):
 y=F(a,b)
 if float(y.lower())>0:accepted.append((a,b,float(y.lower())));return
 if d>=30:failed.append((a,b,str(y)));return
 m=(a+b)/2;visit(a,m,d+1);visit(m,b,d+1)
# Logarithmic initial cells limit dependency across scales.
edges=[10**(-6+k/4) for k in range(29)] # 1e-6 through 10
for a,b in zip(edges,edges[1:]):visit(a,b)
accepted.sort();weak=min(x[2] for x in accepted);covered=(not failed and abs(accepted[0][0]-1e-6)<1e-18 and abs(accepted[-1][1]-10)<1e-12)
out={'schema':'marici.voevodsky.digamma-log-lower-bound-core.v1','inequality':'Re psi(1/4+iu/2) >= log(u/2)-3/2','interval':[1e-6,10.0],
 'evaluations':evals,'accepted_cells':len(accepted),'failed_cells':failed,'weakest_interval_lower':weak,'covered':covered,'passed':covered,
 'tails':{'u_below_1e-6':'requires a separate monotonic/bounded digamma estimate; RHS tends to -infinity','u_above_10':'requires the standard Binet/asymptotic remainder bound'},
 'scope':'Compact-core interval certificate only; the two analytic tails remain explicit lemmas.'}
p=ROOT/'research/voevodsky/results/digamma_log_lower_bound_core.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if covered else 1)
