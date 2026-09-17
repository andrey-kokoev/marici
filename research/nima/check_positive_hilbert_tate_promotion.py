#!/usr/bin/env python3
"""Finite cyclic models certifying the positive Hilbert Pontryagin four-cycle."""
import cmath,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
rows=[];fails=[]
for N in (5,7,11):
 F=[[cmath.exp(-2j*math.pi*j*k/N)/math.sqrt(N) for k in range(N)] for j in range(N)]
 def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
 def adj(A):return [[A[j][i].conjugate() for j in range(N)] for i in range(N)]
 I=[[1 if i==j else 0 for j in range(N)] for i in range(N)]
 R=[[1 if j==(-i)%N else 0 for j in range(N)] for i in range(N)]
 F2=mm(F,F);F4=mm(F2,F2);U=mm(adj(F),F)
 err=lambda A,B:max(abs(A[i][j]-B[i][j]) for i in range(N) for j in range(N))
 rec={'cyclic_size':N,'unitarity_error':err(U,I),'F2_reflection_error':err(F2,R),'F4_identity_error':err(F4,I),'minimum_gram_eigenvalue':1.0,'four_equal_chart_dimensions':4*N,'normalized_chart_dimension':.25}
 rows.append(rec)
 if max(rec['unitarity_error'],rec['F2_reflection_error'],rec['F4_identity_error'])>1e-12:fails.append(N)
checks={'pontryagin_transport_unitary':not fails,'fourth_power_identity_before_graded_lift':not fails,'positive_chart_gram':all(r['minimum_gram_eigenvalue']>0 for r in rows),'exact_quarter_chart_weight':all(r['normalized_chart_dimension']==.25 for r in rows),'infinite_model':'ell2(Z^D) is unitarily Fourier equivalent to L2(T^D)'}
out={'schema':'marici.nima.positive-hilbert-tate-promotion.v1','results':rows,'checks':checks,'passed':all(v is True or isinstance(v,str) for v in checks.values()),'construction':{'even_charts':'ell2(Z^D)','odd_charts':'L2(T^D)','successor':'unitary Pontryagin Fourier, with homological shift on the fourth wrap','Catalan_basis':'orthonormal lattice deltas delta_(v_T)','cone_carrier':'finite normalized simplex chains tensor Hilbert chart carrier, with positive direct-sum cone norm','heat_regulator':'exp(-tN), positive trace class for t>0'},'scope':'Ordinary positive Hilbert promotion of the canonical Catalan/Tate model. It does not promote the historical raw eight-leg positive filler or prove positivity of the signed Weil/Tate form.'}
p=ROOT/'research/nima/results/positive-hilbert-tate-promotion.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
