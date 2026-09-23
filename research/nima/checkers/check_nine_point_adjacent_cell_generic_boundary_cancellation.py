"""Generic shared-boundary cofactor identity for two oriented positive eight-cells."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_adjacent_cell_positive_pole_cancellation as previous
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,variables=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=variables
adjacent=D.copy();adjacent[0,3]=-w4/t
assert adjacent.subs(w4,0)==D.subs(w4,0)
assert s.factor(previous.residue_B+previous.top.source_density)==0
external=loop.Z8six*loop.Z8six[:6,:].inv()
assert external[:6,:]==s.eye(6)
source_inputs=[('first',('1','0','1','1','1','1','3','2')),
               ('second',('2','0','1','4','2','5','7/2','3/2')),
               ('third',('3','0','2','1','4','2','5','1'))]
checks=[]
for name,values in source_inputs:
 point=dict(zip(variables,[s.Rational(v) for v in values]))
 assert point[t]>point[u]>0 and all(point[v]>0 for v in (w2,w5,w6,w7,w8))
 CA=D.subs(point);CB=adjacent.subs(point)
 assert CA==CB
 Y=CA*external;H=Y[:,4:6];assert H.det()!=0
 target=H.inv()*Y[:,:4]
 def jacobian(cell):
  cols=[]
  for variable in variables:
   dY=cell.diff(variable).subs(point)*external
   dB=H.inv()*(dY[:,:4]-dY[:,4:6]*target)
   cols.append(s.Matrix(list(dB)))
  return s.Matrix.hstack(*cols)
 JA=jacobian(D);JB=jacobian(adjacent)
 assert all(JA[:,j]==JB[:,j] for j in range(8) if j!=1)
 detA=JA.det(method='domain-ge');detB=JB.det(method='domain-ge')
 assert detA!=0 and detB!=0
 # Any target-chart transverse direction V has w4-speed computed by
 # Cramer's rule. Replacing column 1 eliminates the ONLY differing
 # Jacobian column, so detA*speedA=detB*speedB identically.
 for label,V in (('normal',JA[:,1]),('mixed',JA[:,1]+JA[:,0]/7+JA[:,6]/11)):
  velocityA=JA.inv()*V;velocityB=JB.inv()*V
  speedA=s.factor(velocityA[1]);speedB=s.factor(velocityB[1])
  assert speedA!=0 and speedB!=0
  replacedA=JA.copy();replacedA[:,1]=V
  replacedB=JB.copy();replacedB[:,1]=V
  assert replacedA==replacedB
  assert s.factor(detA*speedA-detB*speedB)==0
  otherprod=s.prod(point[v] for v in (w2,w5,w6,w7,w8))*point[u]*(point[t]-point[u])
  residueA=s.factor(-s.S.One/(otherprod*detA*speedA))
  residueB=s.factor(s.S.One/(otherprod*detB*speedB))
  assert residueA!=0 and residueA+residueB==0
 checks.append({'source_data':name,'both_cell_target_jacobians_invertible':True,
  'seven_common_tangent_columns_identical':True,
  'normal_and_mixed_target_direction_residue_cancellations':True})
report={'schema':'marici.nima.nine-point-adjacent-cell-generic-boundary-cancellation.v1','passed':True,
 'source_boundary_positive_controls':checks,
 'universal_cofactor_proof':'At every w4=0 source point the two cell maps and full fermionic matrices agree. Seven of their eight target-chart Jacobian columns (all source directions EXCEPT w4) agree exactly; only the transverse w4 column changes. For any transverse target direction V, Cramer gives det(J)*dw4/dV = det(J with its w4 column replaced by V), which is therefore IDENTICAL for the two cells. Their cyclic-top-form boundary densities have exactly opposite orientation. Hence wherever both Jacobians and w4-speeds are regular nonzero, the shared-boundary pole residues cancel identically in ALL fermionic components, not merely at one witness.',
 'boundary':'This is a local generic-open theorem about the shared seven-dimensional source boundary, with three independent exact positive parameter controls and two directions each. It does NOT show that the two cells exhaust the full n9 image, that all their other poles cancel, or that a global canonical triangulation exists.'}
(OUT/'nine-point-adjacent-cell-generic-boundary-cancellation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'positive_boundary_witnesses':len(checks),
 'local_cancellation_generic_open':True},indent=2))
