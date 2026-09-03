#!/usr/bin/env python3
"""Extract level-supported residual kernel classes at D=26 modulo 101."""
import contextlib,io,json,runpy,sys
from pathlib import Path
D=int(sys.argv[1]) if len(sys.argv)>1 else 26;HERE=Path(__file__).resolve();src=HERE.with_name('check_cosmology_rees_residual_nullspace_basis.py');old=sys.argv;sys.argv=[str(src),str(D)]
try:
 with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(src))
finally:sys.argv=old
P=101;labels=g['labels'];cols=g['cols'];known=g['known'];ins=g['ins']
def null_for(ids):
 A=[[cols[j].get((i,D-i),0) for j in ids] for i in range(D+1)];r=0;piv=[]
 for c in range(len(ids)):
  q=next((i for i in range(r,len(A)) if A[i][c]),None)
  if q is None:continue
  A[r],A[q]=A[q],A[r];iv=pow(A[r][c],-1,P);A[r]=[x*iv%P for x in A[r]]
  for i in range(len(A)):
   if i!=r and A[i][c]:
    z=A[i][c];A[i]=[(x-z*y)%P for x,y in zip(A[i],A[r])]
  piv.append(c);r+=1
 free=[c for c in range(len(ids)) if c not in piv];out=[]
 for f in free:
  v={ids[f]:1}
  for i,p in enumerate(piv):
   if A[i][f]:v[ids[p]]=(-A[i][f])%P
  out.append(v)
 return out
K=[null_for([i for i,x in enumerate(labels) if x[0]==lev]) for lev in (0,1)];individual=[]
for lev in (0,1):
 T={};sum(ins(T,dict(v)) for v in known);individual.append(sum(ins(T,dict(v)) for v in K[lev]))
B={};base=sum(ins(B,dict(v)) for v in known);added=[];reps=[]
for lev in (0,1):
 a=0
 for v in K[lev]:
  if ins(B,dict(v)):a+=1;reps.append({'level':lev,'terms':[{'input':list(labels[i]),'coefficient':c} for i,c in sorted(v.items())]})
 added.append(a)
out={'schema':'marici.benincasa.cosmology-rees-levelwise-residual-classes.v1','prime':P,'D':D,'known_rank':base,'level_kernel_dimensions':[len(x) for x in K],'individual_residual_dimensions':individual,'combined_level_supported_dimension':sum(added),'intersection_dimension':sum(individual)-sum(added),'residual_added_by_level':added,'total_residual_classes':len(reps),'representatives':reps};R=HERE.parents[1]/'results';(R/f'cosmology_rees_levelwise_residual_classes_D{D}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['level_kernel_dimensions','individual_residual_dimensions','combined_level_supported_dimension','intersection_dimension']},indent=2))
