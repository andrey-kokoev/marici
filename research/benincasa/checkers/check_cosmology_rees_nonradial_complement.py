#!/usr/bin/env python3
"""Find stable five-column complements to the exact radial image."""
import contextlib,io,json,runpy,sys
from pathlib import Path
HERE=Path(__file__).resolve();src=HERE.with_name('check_cosmology_rees_residual_nullspace_basis.py');out=[]
for D in range(20,33):
 old=sys.argv;sys.argv=[str(src),str(D)]
 try:
  with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(src))
 finally:sys.argv=old
 n=D-8;B={};ins=g['ins'];Lop=g['Lop'];add=g['add'];X={(1,0):1};Y={(0,1):1};mul=g['mul']
 for i in range(n):
  q={(i,n-1-i):1};ins(B,add(Lop(mul(X,q),0,1),Lop(mul(Y,q),1,1)))
 radial=len(B);chosen=[]
 for z in (0,1):
  for i in range(n+1):
   if ins(B,Lop({(i,n-i):1},z,1)):chosen.append({'component':z,'x_power':i,'y_power':n-i})
 out.append({'D':D,'radial_rank':radial,'complement_count':len(chosen),'chosen':chosen})
R=HERE.parents[1]/'results';data={'schema':'marici.benincasa.cosmology-rees-nonradial-complement.v1','prime':101,'rows':out};(R/'cosmology_rees_nonradial_complement.json').write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(out,indent=2))
