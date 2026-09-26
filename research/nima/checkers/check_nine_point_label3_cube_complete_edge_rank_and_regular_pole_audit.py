"""Audit all 12 edges of oriented eight-cell label3 cube in the target."""
import contextlib,io,json,itertools
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_label3_oriented_eight_cell_cube as cube
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
vars=cube.vars;w2,w4,w5,w6,w7,w8,t,u=vars
cells={**cube.E,**cube.F};orient=cube.orient
edges=[]
for suffix in ('','_B','_C','_D'):edges.append(('E'+suffix,'F'+suffix,w2))
for prefix in ('E','F'):
 for left,right,normal in (('', '_B',w4),('', '_C',t),('_C','_D',w4),('_B','_D',t)):
  edges.append((prefix+left,prefix+right,normal))
assert len(edges)==12
Z=cube.Z
rows=[]
for L,R,normal in edges:
 if normal==w2:raw=(0,1,1,1,1,1,3,2)
 elif normal==w4:raw=(1,0,1,1,1,1,3,2)
 else:raw=(1,1,1,1,1,1,2,2)
 slope=s.symbols('slope')
 if normal==t:
  parameters=vars[:6]+(slope,u)
  p=dict(zip(parameters,list(map(s.Rational,raw[:6]))+[s.S.Zero,s.Rational(raw[7])]))
  CL,CR=(cells[name].subs(t,u+slope) for name in (L,R));n=6
 else:
  parameters=vars;p=dict(zip(parameters,map(s.Rational,raw)))
  CL,CR=cells[L],cells[R];n=parameters.index(normal)
 assert CL.subs(p)==CR.subs(p)
 assert orient[L]==-orient[R]
 Y=CL.subs(p)*Z
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(i for i in range(6) if i not in fixed)
 H=Y[:,list(fixed)];B=H.inv()*Y[:,list(free)]
 def jac(C):
  return s.Matrix.hstack(*[s.Matrix(list(H.inv()*(delta[:,list(free)]-
                   delta[:,list(fixed)]*B))) for delta in
                   (C.diff(v).subs(p)*Z for v in parameters)])
 JA,JB=jac(CL),jac(CR)
 assert all(JA[:,j]==JB[:,j] for j in range(8) if j!=n)
 rankA,rankB=JA.rank(),JB.rank()
 assert rankA==rankB
 row={'edge':L+'/'+R,'normal':str(normal),'rank_A':rankA,'rank_B':rankB,
      'full_boundary_matrix_and_fermionic_numerator_agree':True,
      'opposite_oriented_source_residues':True}
 if rankA==8:
  da,db=JA.det(method='domain-ge'),JB.det(method='domain-ge')
  assert da!=0 and db!=0
  other=s.prod(p[x] for x in vars[:6] if x!=normal)*p[u]
  if normal!=t:other*=p[t]-p[u]
  assert other!=0
  for direction in (JA[:,n],JA[:,n]+JA[:,(n+1)%8]/7+JA[:,(n+3)%8]/11):
   sa=s.factor((JA.inv()*direction)[n]);sb=s.factor((JB.inv()*direction)[n])
   assert sa!=0 and sb!=0 and s.factor(da*sa-db*sb)==0
   residueA=s.factor(orient[L]/(other*da*sa))
   residueB=s.factor(orient[R]/(other*db*sb))
   assert residueA!=0 and s.factor(residueA+residueB)==0
  row['full_local_superform_pole_cancels_two_transverse_directions']=True
 else:
  assert rankA==7 and normal==t and (L,R) in (('E_B','E_D'),('F_B','F_D'))
  row['full_local_superform_pole_cancels_two_transverse_directions']=False
  row['exceptional_rank_collapsed_edge']=True
 rows.append(row)
regular=[z for z in rows if z['rank_A']==8]
exceptional=[z for z in rows if z['rank_A']==7]
assert len(regular)==10 and len(exceptional)==2
report={'schema':'marici.nima.nine-point-label3-cube-complete-edge-rank-and-regular-pole-audit.v1',
 'passed':True,'edges':rows,'regular_full_superpole_cancelled_edges':len(regular),
 'exceptional_rank_seven_edges':len(exceptional),
 'scope':'Complete 12-edge LOCAL rank classification at exact positive moment-curve controls; two transverse target directions verify all-component nonlinear pushed simple-pole cancellation on ten regular edges. The two exceptional t-u edges admit no ordinary rank8 pushed residue certificate. This is not target triangulation, full arbitrary-Y image form or coverage.'}
(OUT/'nine-point-label3-cube-complete-edge-rank-and-regular-pole-audit.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'regular_edges_full_superpole_cancelled':len(regular),
 'exceptional_rank7_edges':[x['edge'] for x in exceptional]},indent=2))
