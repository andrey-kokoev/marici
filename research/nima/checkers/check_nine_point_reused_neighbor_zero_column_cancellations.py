"""Previously sourced neighbors also cancel w6=0 and w8=0 zero-column facets."""
import contextlib,io,json,itertools
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_slope_merge_adjacent_cell_cancellation as slope
 import check_nine_point_cyclic_endpoint_adjacent_cell_cancellation as cyclic
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
slope_neighbor=D.copy();slope_neighbor[1,5]=w6*u
cyclic_neighbor=D.copy();cyclic_neighbor[1,7]=0
assert s.factor(slope.new_density+slope.top.source_density)==0
assert s.factor(cyclic.neighbor_density+cyclic.top.source_density)==0
external=loop.Z8six*loop.Z8six[:6,:].inv()
sets=[('w6_zero',w6,3,slope_neighbor,[('1','1','1','0','1','1','3','2'),
 ('2','3','1','0','2','5','7/2','3/2'),('3','2','2','0','4','2','5','1')]),
 ('w8_zero',w8,5,cyclic_neighbor,[('1','1','1','1','1','0','3','2'),
 ('2','3','1','4','2','0','7/2','3/2'),('3','2','2','1','4','0','5','1')])]
reports=[]
for label,pole,normal,neighbor,samples in sets:
 assert neighbor.subs(pole,0)==D.subs(pole,0)
 controls=[]
 for raw in samples:
  point=dict(zip(vars,[s.Rational(x) for x in raw]))
  assert point[pole]==0 and point[t]>point[u]>0
  assert all(point[v]>0 for v in vars[:6] if v!=pole)
  CA=D.subs(point);CB=neighbor.subs(point);assert CA==CB
  Y=CA*external
  fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
  free=tuple(i for i in range(6) if i not in fixed)
  H=Y[:,list(fixed)];target=H.inv()*Y[:,list(free)]
  def jac(cell):
   cols=[]
   for var in vars:
    derivative=cell.diff(var).subs(point)*external
    dB=H.inv()*(derivative[:,list(free)]-derivative[:,list(fixed)]*target)
    cols.append(s.Matrix(list(dB)))
   return s.Matrix.hstack(*cols)
  JA,JB=jac(D),jac(neighbor)
  assert all(JA[:,j]==JB[:,j] for j in range(8) if j!=normal)
  detA,detB=JA.det(method='domain-ge'),JB.det(method='domain-ge')
  assert detA!=0 and detB!=0
  for V in (JA[:,normal],JA[:,normal]+JA[:,0]/7+JA[:,6 if normal!=6 else 4]/11):
   speedA,speedB=s.factor((JA.inv()*V)[normal]),s.factor((JB.inv()*V)[normal])
   assert speedA!=0 and speedB!=0
   alternateA=JA.copy();alternateA[:,normal]=V
   alternateB=JB.copy();alternateB[:,normal]=V
   assert alternateA==alternateB and s.factor(detA*speedA-detB*speedB)==0
   otherprod=s.prod(point[v] for v in vars[:6] if v!=pole)*point[u]*(point[t]-point[u])
   residueA=s.factor(-s.S.One/(otherprod*detA*speedA))
   residueB=s.factor(s.S.One/(otherprod*detB*speedB))
   assert residueA!=0 and residueA+residueB==0
  controls.append({'source_weights':[str(point[v]) for v in vars],
   'regular_chart':list(fixed),'two_direction_pole_cancellation':True})
 reports.append({'facet':label,'reused_neighbor':('slope_merge_cell' if label=='w6_zero' else 'cyclic_endpoint_cell'),
                 'regular_positive_boundary_controls':controls,
                 'all_su4_local_pole_residues_cancel':True})
report={'schema':'marici.nima.nine-point-reused-neighbor-zero-column-cancellations.v1','passed':True,
 'facets':reports,
 'reason':'The slope-merge neighbor already equals the sourced fourmass cell also when w6=0, because the altered physical column7 vanishes there. The cyclic-endpoint neighbor similarly agrees when w8=0, because altered physical column9 vanishes. Their previously computed top-measure oriented eight-forms have opposite signs; seven shared target-tangent Jacobian columns and Cramer cofactors yield local cancellation for ALL fermionic components.',
 'boundary':'Two additional generic-open local source-facet cancellations. The polar source factors w2 and w7, other intersections, full image form and exhaustive nine-point triangulation remain open.'}
(OUT/'nine-point-reused-neighbor-zero-column-cancellations.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'new_cancelled_facets':[x['facet'] for x in reports],
 'exact_positive_boundary_controls':sum(len(x['regular_positive_boundary_controls']) for x in reports)},indent=2))
