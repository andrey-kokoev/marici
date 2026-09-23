"""Construct one sourced n=7 rank-two positroid chart and test its CZ differential."""
import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima';source=json.loads((N/'results/seven-point-positroid-compiler.json').read_text());match=json.loads((N/'results/seven-point-history-parity-cell-matching.json').read_text())
assert source['passed'] and match['passed']
cell=source['cells'][0];assert cell['history_index']==0 and cell['simplex']==next(x['simplex'] for x in match['matches'] if x['history_index']==0)
omit=[int(v.split('(')[1].split(',')[0]) for v in cell['vanishing_cyclic_minors']];assert omit==[2,5]
# Adjacent parallel pairs 2=3, 5=6; positive remaining pair minors.
classes=[0,1,1,2,3,3,4];values=[s.Integer(0),s.Integer(1),s.Integer(2),s.Symbol('u',positive=True),s.Symbol('v',positive=True)]
weights=[s.Integer(1)]+[s.Symbol('w'+str(j),positive=True) for j in range(2,8)]
C=s.Matrix([[w for w in weights],[weights[j]*values[classes[j]] for j in range(7)]])
params=list(weights[1:])+[values[3],values[4]]
# The fixed t1,t2,t4 normalize projective row gauge; 2<u<v is the positive chamber.
Z=s.Matrix([[s.Integer(j)**k for k in range(6)] for j in range(1,8)])
assert all(s.det(Z.extract(list(idx),list(range(6))))>0 for idx in __import__('itertools').combinations(range(7),6))
point={**{w:s.Integer(1) for w in weights[1:]},values[3]:s.Integer(3),values[4]:s.Integer(4)}
Cp=C.subs(point);Y=C*Z;Yp=Y.subs(point)
minors={(i+1,j+1):s.factor(s.det(C[:,[i,j]])) for i in range(7) for j in range(i+1,7)}
assert {p for p,f in minors.items() if f==0}=={(2,3),(5,6)}
assert all(f.subs(point)>0 for f in minors.values() if f!=0)
# An affine coordinate chart of G(2,6): use first two target columns as row gauge.
A=Y[:,[0,1]];assert A.subs(point).det()!=0
B=A.inv()*Y[:,2:];jac=B.reshape(8,1).jacobian(params).subs(point)
assert jac.det()!=0
# Explicitly test physical intersections in target with *other* rank tables later;
# this is a local immersion, not a history-form identification.
report={'schema':'marici.nima.seven-point-positive-chart.v1','history_index':0,'vanishing_minors':list(map(list,sorted(p for p,f in minors.items() if f==0))),
 'chart':'C_i=w_i(1,t_class(i)), classes=[0,1,1,2,3,3,4], t=(0,1,2,u,v), w1=1; all w_i>0 and 2<u<v',
 'positive_external_data':'Z_j=(1,j,j^2,j^3,j^4,j^5), j=1..7',
 'sample':{'weights':[1]*7,'u':3,'v':4,'all_nonvanishing_source_minors_positive':True,'target_chart_jacobian_determinant':str(s.factor(jac.det()))},
 'claims':'Explicit eight-parameter positive rank-two source chart with locally nondegenerate CZ image at one positive Z. No canonical-form match or global overlap/coverage established.'}
p=N/'results/seven-point-positive-chart.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
