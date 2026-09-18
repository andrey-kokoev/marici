#!/usr/bin/env python3
"""Source-derived orientation of the two Segre rulings across n."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_spinor_kinematics import adjugate2,momentum_conserving_kinematics,x_interval
from nnmhv_coherence_paths import compile_nnmhv_histories
rows=[]
for n in (7,8,9):
 lam,til,x=momentum_conserving_kinematics([(1,j*j+j+1) for j in range(1,n+1)],[(1,j**3+2*j+1) for j in range(1,n-1)]);shell=[]
 for k,h in enumerate(compile_nnmhv_histories(n)):
  if not h.inner_prefix or h.inner_prefix[0]!=n-1:continue
  vertices=(n,)+h.inner_prefix;M=s.eye(2)
  for q,(a,b) in enumerate(zip(vertices,vertices[1:])):M=s.simplify(M*(x_interval(x,a,b) if q%2==0 else adjugate2(x_interval(x,a,b))))
  image=M.columnspace()[0];kernel=M.nullspace()[0];target=lam[n-1]
  shell.append({'history_index':k,'a1':h.inner_pair[0],'rank':M.rank(),'image_is_inserted_spinor':s.det(s.Matrix.hstack(image,target))==0,'image_P1':[str(s.factor(z)) for z in image],'kernel_P1':[str(s.factor(z)) for z in kernel]})
 distinct_kernels=len({tuple(r['kernel_P1']) for r in shell});rows.append({'n':n,'inserted_edge':n-1,'shell_history_count':len(shell),'distinct_kernel_lines':distinct_kernels,'histories':shell})
checks={'all_new_shell_transports_rank_one':all(h['rank']==1 for r in rows for h in r['histories']),'all_images_equal_inserted_spinor':all(h['image_is_inserted_spinor'] for r in rows for h in r['histories']),'image_fixed_within_each_shell':all(all(s.det(s.Matrix.hstack(s.Matrix([s.sympify(z) for z in r['histories'][0]['image_P1']]),s.Matrix([s.sympify(z) for z in h['image_P1']])))==0 for h in r['histories']) for r in rows),'kernel_varies_with_endpoint':all(r['distinct_kernel_lines']>1 for r in rows),'tested_three_cutoffs':len(rows)==3}
out={'schema':'marici.nima.segre-insertion-reflow-orientation.v1','cutoffs':rows,'checks':checks,'passed':all(checks.values()),'orientation':{'insertion':'image ruling: changing cutoff inserts the new null-edge line [lambda_(n-1)]','reflow':'kernel ruling: at fixed inserted image, endpoint/history variation changes the annihilated input line'},'scope':'Exact source-derived identification on the newly inserted b1=n-1 shell for n=7,8,9.'};p=ROOT/'research/nima/results/segre-insertion-reflow-orientation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
