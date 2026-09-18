#!/usr/bin/env python3
"""Exact robustness audit of the (2,3) full-sum history support rule."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r
from dual_spinor_kinematics import momentum_conserving_kinematics,transport_spinor
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
eps=s.Matrix([[0,1],[-1,0]])
families={'q2_q3':(lambda j:j*j+j+1,lambda j:j**3+2*j+1),'q2_q4':(lambda j:j*j+2*j+2,lambda j:j**4+j+1),'q3_q2':(lambda j:j**3+j+1,lambda j:j*j+3*j+1)}
def predicted(h):return h.branch=='left-nested' and h.outer_pair[0]==2 and h.inner_pair[0]==3
rows=[];false_positive=[];false_negative=[]
for name,(lf,tf) in families.items():
 for n in range(6,11):
  lam,til,x=momentum_conserving_kinematics([(1,lf(j)) for j in range(1,n+1)],[(1,tf(j)) for j in range(1,n-1)]);oc={};actual=0
  for h in compile_nnmhv_histories(n):
   if h.outer_pair not in oc:oc[h.outer_pair]=generalized_r(lam,x,n,(),h.outer_pair,lam[h.outer_pair[0]-1].T*eps,lam[h.outer_pair[1]].T*eps)[1]
   o=oc[h.outer_pair];st=terminal_r_state(h);i=generalized_r(lam,x,n,h.inner_prefix,h.inner_pair,transport_spinor(lam,x,st.lower_spinor.vertices),transport_spinor(lam,x,st.upper_spinor.vertices))[1];w=s.factor(o['xi_coefficients'].get(2,0)*i['xi_coefficients'].get(3,0)-o['xi_coefficients'].get(3,0)*i['xi_coefficients'].get(2,0));nz=w!=0;actual+=nz
   rec={'family':name,'n':n,'outer':list(h.outer_pair),'inner':list(h.inner_pair),'branch':h.branch}
   if predicted(h) and not nz:false_positive.append(rec)
   if nz and not predicted(h):false_negative.append(rec)
  expected=(n-5)*(n-4)//2;rows.append({'family':name,'n':n,'total_histories':len(compile_nnmhv_histories(n)),'actual_nonzero':actual,'predicted_nonzero':expected})
checks={'three_independent_families':len(families)==3,'all_sections_6_through_10':len(rows)==15,'no_predicted_history_vanishes':not false_positive,'no_unpredicted_history_contributes':not false_negative,'all_counts_triangular':all(r['actual_nonzero']==r['predicted_nonzero'] for r in rows)}
out={'schema':'marici.nima.nnmhv-component-support-rule.v1','component':'product_A eta_2^A eta_3^A','rule':'left-nested and a1=2 and a2=3','sections':rows,'false_positives':false_positive,'false_negatives':false_negative,'checks':checks,'passed':all(checks.values()),'scope':'Exact audit of every history for three generic coherent families and n=6..10; strong finite evidence, not a symbolic all-n proof.'}
p=ROOT/'research/nima/results/nnmhv-component-support-rule.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
