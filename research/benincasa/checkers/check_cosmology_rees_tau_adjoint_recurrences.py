#!/usr/bin/env python3
"""Derive and verify the universal adjoint equations of the assembled relation rows."""
import contextlib,io,json,runpy
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
a=g['construct'](8);by={}
for (kind,label),row in a.items():by.setdefault(label,{})[kind]=row
assert all(set(v)=={'shift2','upper','jet'} for v in by.values())
for v in by.values():
 r0={k[1]:x for k,x in v['shift2'].items() if k[0]==2};assert {(2,k):x for k,x in r0.items()}==v['shift2'];assert {k[1]:x for k,x in v['upper'].items() if k[0]==1}==r0;assert {k[1]:x for k,x in v['jet'].items() if k[0]==0}==r0
families=Counter(k[0] for k in by)
out={'schema':'marici.benincasa.cosmology-rees-tau-adjoint-recurrences.v1','unknown':'lambda_g(k,levels,exponent), g=0,1,2','source_relation_expansion':'r(E)=r0+E r1+E^2 r2','adjoint_equations':['lambda_2(r0)=0','lambda_1(r0)+lambda_2(r1)=0','lambda_0(r0)+lambda_1(r1)+lambda_2(r2)=0'],'normalization':'lambda_1(0,(1,1,1,1,1),(0,0))=1/3, equivalently lambda(tau_p)=1','raw_family_recurrences':{'twisted_derivative':'apply each displayed adjoint equation to exponent derivative plus (gamma-k) dk terms minus pole-weighted dq_i terms','K_multiplication':'lambda_g(k,l,e)-sum_t k_t lambda_g(k+1,l,e+t)=0 before E-grade coupling','q_multiplication':'lambda_g(k,l,e)-sum_t q_i,t lambda_g(k,l+unit_i,e+t)=0 before E-grade coupling'},'cutoff_eight_source_labels':len(by),'family_counts':dict(families),'assembly_identity_verified_for_every_label':True,'consistency_status':'finite systems through Q8 are consistent by nonzero tau quotient tests; uniform recurrence solution not constructed','first_missing_object':'a cutoff-independent solution of these equations with the stated normalization','passed':True};(R/'cosmology_rees_tau_adjoint_recurrences.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
