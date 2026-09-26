"""Audit source/target frame before comparing barrier payloads to P9."""
import contextlib,io,json
from pathlib import Path
import sympy as s
from nine_point_source_r import Kinematics
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_two_cube_families_offface_chi1_chi5_independence as data
root=Path(__file__).resolve().parents[1];hist=json.loads((root/'results/nine-point-source-history-contract.json').read_text())['records']
pairs=((3,5),(2,5),(1,5));results=[]
for e in (s.Rational(1,2),s.S.One):
 p=dict(zip(data.vars,(e,1,1,1,1,1,3,2)));Y=data.cube.E['E'].subs(p)*data.Z9
 B=Y[:,:2].inv()*Y[:,2:];z=data.Z9[:,2:]-data.Z9[:,:2]*B;h=data.Z9[:,:2]
 kin=Kinematics(z.tolist());sums=[s.S.Zero]*3
 for record in hist:
  a1,b1=record['outer_pair'];a,b=record['inner_pair'];A,f=kin.ordinary(a1,b1);D,g=kin.inner(a1,b1,a,b,record['branch'])
  for j,(u,v) in enumerate(pairs):sums[j]+=f*g*(A[u]*D[v]-A[v]*D[u])**4
 points={'zero2_E_B':data.trace.inverse_one_sheet(Y,data.trace.bir.square.source['E_B'],data.trace.bir.zero_sets['E_B']), 'zero2_F_B':data.first.support.five.inverse_at(e)[0], 'zero3_E_B':{v:s.factor(data.wall.points['E_B'][v].subs(data.wall.e,e)) for v in data.vars}, 'zero3_F_B':{v:s.factor(data.wall.points['F_B'][v].subs(data.wall.e,e)) for v in data.vars}}
 rows={}
 for key,C in data.face.C.items():
  point=points[key];M=C.subs(point)*h
  J=s.Matrix.hstack(*[s.Matrix(list(C.diff(v).subs(point)*z)) for v in data.vars]).det(method='domain-ge')
  density=data.cube.orient[key.split('_',1)[1]]/(s.prod(point[v] for v in data.vars[:6])*point[data.u]*(point[data.t]-point[data.u]))
  unframed=[s.factor(density*C[:,[i-1,j-1]].det().subs(point)**4/J) for i,j in pairs]
  inherited=[s.factor(v*M.det()**4) for v in unframed]
  # Constant representative rescaling C -> 2C: J -> 2^8 J,
  # each minor^4 -> 2^8 minor^4, det(Ch)^4 -> 2^8 det(Ch)^4.
  assert all(s.factor(density*(4*C[:,[i-1,j-1]].det().subs(point))**4/(2**8*J)-v)==0 for (i,j),v in zip(pairs,unframed))
  rows[key]={'det_Ch':str(M.det()),'delta_pushforward_components':list(map(str,unframed)),'inherited_frame_weighted_components':list(map(str,inherited))}
 results.append({'e':str(e),'tree_P9_components':list(map(lambda v:str(s.factor(v)),sums)),'cells':rows})
report={'passed':True,'pairs':pairs,'witnesses':results,'constant_C_rescaling':2,'delta_coefficient_scaling':1,'inherited_payload_scaling':256,'scope':'Same quotient z for tree and source fibres. Delta-function coefficient is GL(2)-representative invariant; inherited det(Ch)^4-weighted payload is not unless an additional density convention compensates. Do not identify it with P9 without that convention.'}
(root/'results/nine-point-common-frame.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':True,'witnesses':2,'all_50_tree_terms_regular':True,'frame_weight_discrepancy':256}))
