#!/usr/bin/env python3
"""Out-of-sample test of c_log=p*sum(m_j)-6."""
import json,math,sys,time
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from coherence_chain_toy import connected_chain
cases={'p2_m0124':(2,(0,1,2,4)),'p2_m0135':(2,(0,1,3,5)),'p3_m0124':(3,(0,1,2,4)),'p2_m0236':(2,(0,2,3,6))};ks=(20,30,40,50,60);rows={};start=time.perf_counter()
for name,(p,powers) in cases.items():
 ys=[]
 for k in ks:
  n=3*k+2;xs=[s.Integer(i**p+i) for i in range(1,n+1)];cols=[[x**m for m in powers] for x in xs];h,_,c=connected_chain(k,xs,cols);v=h.component(c);ys.append(float(s.N(-s.log(abs(v)),18))/k)
 X=s.Matrix([[math.log(k),1.0,math.log(k)/k,1.0/k] for k in ks]);Y=s.Matrix(ys);clog,d,elog,e=[float(v) for v in (X.T*X).inv()*X.T*Y];expected=p*sum(powers)-6;rows[name]={'spacing_power':p,'embedding_powers':list(powers),'predicted':expected,'observed':clog,'error':clog-expected,'extensive_constant':d,'log_k_over_k':elog,'one_over_k':e}
checks={'all_mixed_cases_within_tolerance':all(abs(r['error'])<0.08 for r in rows.values()),'cases_are_out_of_sample_combinations':len(rows)==4,'predictions_span_multiple_coefficients':len({r['predicted'] for r in rows.values()})>=3}
out={'schema':'marici.nima.combined-kinematic-scaling-law.v1','law':'c_log=p*sum(m_j)-6','finite_sections':list(ks),'mixed_cases':rows,'checks':checks,'passed':all(checks.values()),'scope':'Out-of-sample exact finite-section tests on mixed generalized moment curves; numerical evidence for the leading law, not a proof for arbitrary positive configurations.'}
pth=ROOT/'research/nima/results/combined-kinematic-scaling-law.json';pth.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
