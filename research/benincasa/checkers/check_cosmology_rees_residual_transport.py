#!/usr/bin/env python3
"""Compute X/Y transport from residual quotient degree 26 to 27."""
import contextlib,io,json,runpy,sys
from pathlib import Path
P=101;HERE=Path(__file__).resolve();src=HERE.with_name('check_cosmology_rees_residual_nullspace_basis.py')
def load(D):
 old=sys.argv;sys.argv=[str(src),str(D)]
 try:
  with contextlib.redirect_stdout(io.StringIO()):return runpy.run_path(str(src))
 finally:sys.argv=old
a=load(26);b=load(27);labels26=a['labels'];labels27=b['labels'];idx27={x:i for i,x in enumerate(labels27)};known=b['known'];res26=a['residual'];res27=b['residual'];ins=b['ins']
def shift(v,z):
 out={}
 for i,c in v.items():
  kp,ax,x,y=labels26[i];lab=(kp,ax,x+(z==0),y+(z==1));out[idx27[lab]]=c
 return out
B={};knownrank=sum(ins(B,dict(v)) for v in known);rx=[];ry=[]
for v in res26:
 if ins(B,shift(v,0)):rx.append(v)
afterx=len(B)
for v in res26:
 if ins(B,shift(v,1)):ry.append(v)
afterxy=len(B);missing=0
for v in res27:missing+=ins(B,dict(v))
out={'schema':'marici.benincasa.cosmology-rees-residual-transport.v1','prime':P,'source_degree':26,'target_degree':27,'source_quotient_dimension':len(res26),'target_quotient_dimension':len(res27),'known_target_rank':knownrank,'X_transport_rank':afterx-knownrank,'Y_rank_added_after_X':afterxy-afterx,'combined_XY_transport_rank':afterxy-knownrank,'target_cokernel_after_transport':missing,'surjective':missing==0};R=HERE.parents[1]/'results';(R/'cosmology_rees_residual_transport.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
