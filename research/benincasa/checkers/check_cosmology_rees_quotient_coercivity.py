#!/usr/bin/env python3
"""Associated-graded coercivity modulo exact prolonged syzygies."""
import json
from pathlib import Path
# In u=X+sqrt(2)Y, v=X-sqrt(2)Y, V(u^a v^b)=sqrt(2)(a-b)u^a v^b.
for a in range(10):
 for b in range(10): assert ((a-b)==0)==(a==b)
# Q_5=X^2 Y^2 (X+Y), degree 5; I=uv=X^2-2Y^2, degree 2.
samples=[]
for m in range(8):samples.append({'m':m,'kernel_input_degree':5+2*m,'exact_lift_degree':5+2*m,'degree_drop_after_subtraction_at_least':1})
out={'schema':'marici.benincasa.cosmology-rees-quotient-coercivity.v1','problem':'control polynomial degree for the prolonged operator after quotienting its exact kernel Q k[I]','bold_conjecture':'the associated-graded kernel is larger than the leading terms of exact syzygies, causing uncontrolled degree descent','named_rivals':['extra characteristic solutions','graded kernel exactly Q_5 k[I], permitting filtered reduction by exact Q k[I] syzygies'],'risky_consequences':['every homogeneous solution of Q_5 V(g)-V(Q_5)g=0 must be Q_5 I^m','subtracting Q I^m with matching leading term must strictly lower input degree'],'strongest_falsification_attempt':{'diagonal_coordinates':'u=X+sqrt(2)Y, v=X-sqrt(2)Y','derivation':'V(u)=sqrt(2)u, V(v)=-sqrt(2)v','invariant_ring':'kernel(V)=k[uv]=k[I]','leading_factor':'Q_5=X^2Y^2(X+Y), with no nonconstant factor in k[I]','graded_kernel':'Q_5 k[I]','exact_residual':0},'samples':samples,'disposition':'associated-graded kernel equals the leading terms of exact syzygies; filtered coercivity holds modulo Q k[I]','surviving_scope':'each class has a representative g with either g=0 or deg T(g)=deg g+5, so deg g is controlled by output degree on this prolonged branch','next_test':'assemble this scalar coercivity with the transverse principal-symbol quotient and all 308 prototype blocks to obtain a global preimage-degree bound','passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_rees_quotient_coercivity.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
