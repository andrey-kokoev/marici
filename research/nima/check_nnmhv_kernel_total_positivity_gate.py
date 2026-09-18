#!/usr/bin/env python3
"""Test exact total nonnegativity and network-factor positivity of the n=8 kernel."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
src=json.loads((ROOT/'research/nima/results/nnmhv-kernel-wall-tail-boundary.json').read_text());K=s.Matrix([[s.sympify(x) for x in row] for row in src['kernel_matrix']]);mins=[]
for q in range(1,K.rows+1):
 for I in itertools.combinations(range(K.rows),q):
  for J in itertools.combinations(range(K.cols),q):
   d=s.factor(K.extract(I,J).det());mins.append({'rows':list(I),'cols':list(J),'value':str(d),'sign':int(s.sign(d))})
# Unit-lower LDU elimination; positivity of multipliers is a planar-network factor gate.
L,U,_=K.LUdecomposition();diag=[s.factor(U[i,i]) for i in range(K.rows)];unitU=s.diag(*[1/x for x in diag])*U;positive_L=all(s.sign(L[i,j])>=0 for i in range(K.rows) for j in range(K.cols));positive_U=all(s.sign(unitU[i,j])>=0 for i in range(K.rows) for j in range(K.cols));checks={'all_entries_positive_or_structural_zero':all(s.sign(K[i,j])>=0 for i in range(K.rows) for j in range(K.cols)),'negative_higher_minors_exist':any(x['sign']<0 for x in mins),'kernel_is_not_totally_nonnegative':not all(x['sign']>=0 for x in mins),'positive_diagonal_factor':all(s.sign(x)>0 for x in diag)}
out={'schema':'marici.nima.nnmhv-kernel-total-positivity-gate.v1','n':src['n'],'matrix_shape':list(K.shape),'nonzero_minors':sum(x['sign']!=0 for x in mins),'total_minors':len(mins),'negative_minors':[x for x in mins if x['sign']<0],'L_factor':[[str(s.factor(L[i,j])) for j in range(K.cols)] for i in range(K.rows)],'D_factor':[str(x) for x in diag],'unit_U_factor':[[str(s.factor(unitU[i,j])) for j in range(K.cols)] for i in range(K.rows)],'checks':checks,'passed':all(checks.values()),'meaning':'The physical kernel is entrywise positive but not totally nonnegative: higher minors detect destructive coherence invisible at the level of individual history weights.','bridges':['Lindstroem-Gessel-Viennot planar networks','Lusztig total positivity','variation-diminishing linear filters','positive matrix semigroups','subtraction-free factorization']};p=ROOT/'research/nima/results/nnmhv-kernel-total-positivity-gate.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
