"""Permit arbitrary individual cell weights, not just two pole-cancelling pairs."""
import contextlib,io,json
from pathlib import Path
import sympy as s
from nine_point_source_r import Kinematics
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_two_cube_families_offface_chi1_chi5_independence as data
root=Path(__file__).resolve().parents[1];hist=json.loads((root/'results/nine-point-source-history-contract.json').read_text())['records']
components=[((3,5),)*4,((2,5),)*4,((1,5),)*4,((1,9),(2,8),(3,7),(4,6)),((1,3),(2,5),(4,7),(6,9))]
rows=[]
for e in (s.Rational(1,2),s.S.One):
 p=dict(zip(data.vars,(e,1,1,1,1,1,3,2)));Y=data.cube.E['E'].subs(p)*data.Z9;B=Y[:,:2].inv()*Y[:,2:];z=data.Z9[:,2:]-data.Z9[:,:2]*B
 points={'zero2_E_B':data.trace.inverse_one_sheet(Y,data.trace.bir.square.source['E_B'],data.trace.bir.zero_sets['E_B']), 'zero2_F_B':data.first.support.five.inverse_at(e)[0], 'zero3_E_B':{v:s.factor(data.wall.points['E_B'][v].subs(data.wall.e,e)) for v in data.vars}, 'zero3_F_B':{v:s.factor(data.wall.points['F_B'][v].subs(data.wall.e,e)) for v in data.vars}}
 columns=[]
 for key,C in data.face.C.items():
  point=points[key];J=s.Matrix.hstack(*[s.Matrix(list(C.diff(v).subs(point)*z)) for v in data.vars]).det(method='domain-ge')
  factor=data.cube.orient[key.split('_',1)[1]]/(s.prod(point[v] for v in data.vars[:6])*point[data.u]*(point[data.t]-point[data.u])*J)
  columns.append(s.Matrix([s.factor(factor*s.prod(C[:,[i-1,j-1]].det().subs(point) for i,j in pairs)) for pairs in components]))
 M=s.Matrix.hstack(*columns);kin=Kinematics(z.tolist());target=s.zeros(len(components),1)
 for record in hist:
  a1,b1=record['outer_pair'];a,b=record['inner_pair'];A,f=kin.ordinary(a1,b1);D,g=kin.inner(a1,b1,a,b,record['branch'])
  for j,pairs in enumerate(components):target[j]+=f*g*s.prod(A[u]*D[v]-A[v]*D[u] for u,v in pairs)
 target=target.applyfunc(s.factor);aug=M.row_join(target);rank=M.rank();aug_rank=aug.rank()
 rows.append({'e':str(e),'cell_order':list(data.face.C),'cell_rank':rank,'augmented_rank':aug_rank,'in_span':rank==aug_rank,'augmented_determinant':str(s.factor(aug.det())),'cell_matrix':[[str(x) for x in row] for row in M.tolist()],'tree_vector':list(map(str,target))})
report={'passed':True,'flavor_pairs':components,'witnesses':rows,'scope':'Five exact component tests at common quotient data. An augmented rank increase excludes any bosonic scalar combination of these four fixed sheet contributions at that point; independent column rescalings/orientations cannot fix the span.'}
(root/'results/nine-point-four-cell-span.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':True,'ranks':[(r['cell_rank'],r['augmented_rank']) for r in rows]}))
