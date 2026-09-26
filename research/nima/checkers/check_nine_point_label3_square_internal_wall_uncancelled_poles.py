"""Differentiate lower uncancelled and upper nonpositive-sheet-cancelled E_B interior poles."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_EB_internal_support_walls_fermionic_vanishing as wall
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
chamber=wall.chamber;trace=chamber.trace
D,vars=trace.D,trace.vars
w2,w4,w5,w6,w7,w8,t,u=vars
rows=[]
for label,root,normal,component in [('lower',chamber.threshold_low,w2,'chi1^4 chi5^4'),
                                     ('upper',chamber.threshold_high,w4,'chi3^4 chi4^4')]:
 p=dict(zip(vars,(root,1,1,1,1,1,3,2)));Y=D.subs(p)*trace.Z
 H=Y[:,:2];B=H.inv()*Y[:,2:]
 z=trace.Z[:,2:]-trace.Z[:,:2]*B;h=trace.Z[:,:2]
 sheets={}
 for kernel_root,point in trace.G.fibre(D.subs(p),trace.Z):
  sheets.setdefault('E',[]).append({'root':str(kernel_root),'point':point})
 assert len(sheets['E'])==2
 for name in ('E_B','E_C','E_D'):
  cell=trace.bir.square.source[name]
  point=trace.inverse_one_sheet(Y,cell,trace.bir.zero_sets[name])
  sheets[name]=[{'point':point}]
 def regular(cell,point):
  J=s.Matrix.hstack(*[s.Matrix(list(cell.diff(v).subs(point)*z)) for v in vars]).det(method='domain-ge')
  return all(point[v]!=0 for v in vars[:6]) and point[u]!=0 and point[t]-point[u]!=0 and J!=0 and (cell.subs(point)*h).det()!=0
 assert all(regular(D,q['point']) for q in sheets['E'] if q['root']=='0')
 assert all(regular(trace.bir.square.source[name],sheets[name][0]['point'])
            for name in ('E_C','E_D'))
 assert sheets['E_B'][0]['point'][normal]==0
 others=[q for q in sheets['E'] if q['root']!='0']
 assert len(others)==1
 E_alt=others[0]['point']
 if label=='lower':
  assert regular(D,E_alt)
  assert wall.order_at(wall.bosonic*wall.point[w4]**4,root)==-1
  outcome='genuine uncancelled chi1^4 chi5^4 pole of four-cell meromorphic sum'
 else:
  assert E_alt[w4]==0 and all(E_alt[v]!=0 for v in (w2,w5,w6,w7,w8,u))
  EB=sheets['E_B'][0]['point']
  assert all(s.factor(E_alt[v]-EB[v])==0 for v in vars)
  assert D.subs(E_alt)==trace.bir.square.source['E_B'].subs(EB)
  def jac(cell,point):
   return s.Matrix.hstack(*[s.Matrix(list(cell.diff(v).subs(point)*z)) for v in vars])
  JE=jac(D,E_alt);JB=jac(trace.bir.square.source['E_B'],EB)
  assert JE.det(method='domain-ge')!=0 and JB.det(method='domain-ge')!=0
  assert all(JE[:,j]==JB[:,j] for j in range(8) if j!=1)
  # An arbitrary transverse target direction gives the same
  # determinant-normal-speed product on the common regular face.
  for direction in (JE[:,1],JE[:,1]+JE[:,0]/7+JE[:,5]/11):
   speedE=s.factor((JE.inv()*direction)[1]);speedB=s.factor((JB.inv()*direction)[1])
   assert speedE!=0 and speedB!=0
   assert s.factor(JE.det(method='domain-ge')*speedE-
                   JB.det(method='domain-ge')*speedB)==0
   other=s.prod(E_alt[v] for v in (w2,w5,w6,w7,w8))*E_alt[u]*(E_alt[t]-E_alt[u])
   residueE=s.factor(1/(other*JE.det(method='domain-ge')*speedE))
   residueB=s.factor(-1/(other*JB.det(method='domain-ge')*speedB))
   assert residueE!=0 and s.factor(residueE+residueB)==0
  outcome='E nonpositive sheet and E_B pole cancel on common regular w4 face in all components'
 rows.append({'wall':label,'E_positive_source_e':str(root),'component':component,
              'E_B_source_facet':str(normal)+'=0',
              'other_E_sheet_on_same_source_facet':bool(label=='upper'),
              'E_C_and_E_D_complete_sheets_regular':True,
              'meromorphic_four_cell_pole_outcome':outcome})
report={'schema':'marici.nima.nine-point-label3-square-internal-wall-uncancelled-poles.v2',
 'passed':True,'exact_interior_wall_controls':rows,
 'consequence':'LOWER E_B w2=0 wall inside regular positive E image leaves a genuine uncancelled chi1^4 chi5^4 simple pole of the E,E_B,E_C,E_D MEROMORPHIC four-cell sum: both E sheets and E_C/E_D are regular. UPPER E_B w4=0 wall behaves differently: E has a SECOND, NONPOSITIVE algebraic sheet on the identical source facet, and their opposite oriented full-superform residues cancel in two target directions. Source-supported positive sheets alone miss this upper cancellation.',
 'scope':'Two exact target walls on one positive E curve, meromorphic subcomplex versus positive-supported source distinctions. Other cells may cancel lower pole; full nine-point canonical form unresolved.'}
(OUT/'nine-point-label3-square-internal-wall-uncancelled-poles.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'interior_wall_outcomes':rows},indent=2))
