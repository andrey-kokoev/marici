#!/usr/bin/env python3
"""Resolve boundary-update interference by type-A simple-root controls."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
src=json.loads((ROOT/'research/nima/results/nnmhv-kernel-wall-tail-boundary.json').read_text());K=s.Matrix([[s.sympify(x) for x in row] for row in src['kernel_matrix']]);K0=s.Matrix([[s.sympify(x) for x in row] for row in src['kernel_without_upper_boundary_transport']]);B=K-K0
def negmins(A):
 out=[]
 for q in range(1,4):
  for I in itertools.combinations(range(3),q):
   for J in itertools.combinations(range(3),q):
    d=s.factor(A.extract(I,J).det())
    if s.sign(d)<0:out.append((I,J))
 return out
configs=[]
for mask in itertools.product((0,1),repeat=3):
 A=K0+s.diag(*[mask[i]*B[i,i] for i in range(3)]);configs.append({'active_simple_roots':[i+1 for i,x in enumerate(mask) if x],'negative_minor_count':len(negmins(A)),'negative_minors':[{'rows':list(I),'cols':list(J)} for I,J in negmins(A)]})
target=s.factor(K[1,0]*K[2,1]-K[1,1]*K[2,0]);root_relation={'K_[1,2]':str(K[1,0]),'K_alpha2':str(K[1,1]),'K_[1,3]':str(K[2,0]),'K_[2,3]':str(K[2,1]),'witness':'K_[1,2] K_[2,3] - K_alpha2 K_[1,3]','value':str(target)};checks={'boundary_correction_is_cartan_diagonal':all(B[i,j]==0 for i in range(3) for j in range(3) if i!=j),'alpha2_active_iff_negative_minor':all((2 in x['active_simple_roots'])==(x['negative_minor_count']==1) for x in configs),'alpha1_alpha3_alone_preserve_total_nonnegativity':all(x['negative_minor_count']==0 for x in configs if 2 not in x['active_simple_roots']),'witness_is_composite_root_relation':target<0}
out={'schema':'marici.nima.nnmhv-simple-root-interference-control.v1','type':'A_3','boundary_cartanan_correction':[str(s.factor(B[i,i])) for i in range(3)],'root_relation':root_relation,'toggle_experiment':configs,'checks':{k:bool(v) for k,v in checks.items()},'passed':all(bool(v) for v in checks.values()),'meaning':'Boundary transport acts in the simple-root/Cartan sector. The alpha_2 correction alone controls the sign of a relation among the four composite-root amplitudes [1,2], alpha_2, [1,3], and [2,3].','bridges':['Cartan control of root amplitudes','simple-to-composite coherence transfer','Pluecker-like root minor','localized boundary generator','oriented-matroid chamber controlled by one simple root']};p=ROOT/'research/nima/results/nnmhv-simple-root-interference-control.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
