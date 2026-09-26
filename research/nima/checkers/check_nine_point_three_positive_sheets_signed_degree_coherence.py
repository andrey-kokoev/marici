"""Check whether three positive cube sheets require a fourth for LOCAL signed-degree coherence."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_eight_cell_positive_supported_multiplicity as x
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
cube=x.new.cube;trace=x.prior.trace;five=x.five
rows=[]
for e in (s.Rational(1,20),s.Rational(1,2),s.S.One):
 p=dict(zip(x.vars,(e,1,1,1,1,1,3,2)))
 Y=trace.D.subs(p)*x.Z
 B=Y[:,:2].inv()*Y[:,2:]
 z=x.Z[:,2:]-x.Z[:,:2]*B
 cells=[]
 for name in ('E','E_B','F_B'):
  if name=='E':
   cell=cube.E[name][:,list(x.new.retained)]
   point=next(q for _,q in trace.G.fibre(trace.D.subs(p),x.Z)
              if all(q[v]>0 for v in x.vars[:6]) and q[x.u]>0 and q[x.t]>q[x.u])
  elif name=='E_B':
   cell=cube.E[name][:,list(x.new.retained)]
   point=trace.inverse_one_sheet(Y,trace.bir.square.source[name],trace.bir.zero_sets[name])
  else:
   cell=cube.F[name][:,list(x.new.retained)]
   point,_,_=five.inverse_at(e)
  positive=all(point[v]>0 for v in x.vars[:6]) and point[x.u]>0 and point[x.t]>point[x.u]
  J=s.Matrix.hstack(*[s.Matrix(list(cell.diff(v).subs(point)*z)) for v in x.vars]).det(method='domain-ge')
  assert J!=0
  cells.append({'cell':name,'positive':bool(positive),
                'oriented_local_degree':int(cube.orient[name]*s.sign(J)) if positive else 0,
                'target_jacobian_sign':int(s.sign(J)),
                'calibrated_cell_orientation':int(cube.orient[name])})
 total=sum(c['oriented_local_degree'] for c in cells)
 assert total==1
 rows.append({'E_ray_e':str(e),'positive_source_sheet_count_among_E_EB_FB':sum(c['positive'] for c in cells),
              'signed_local_degree_among_E_EB_FB':total,'cells':cells})
assert [r['positive_source_sheet_count_among_E_EB_FB'] for r in rows]==[1,3,3]
assert x.report['complete_eight_cell_positive_source_sheet_count']==3
assert [c['oriented_local_degree'] for c in rows[-1]['cells']]==[1,-1,1]
assert any(z['wall']=='lower' for z in five.prior.rows)
assert any(q['boundary']=='interior_E_target_lower_wall' and
           q['two_transverse_target_direction_full_superpole_cancellations']
           for q in five.neighbor.checks)
report={'schema':'marici.nima.nine-point-three-positive-sheets-signed-degree-coherence.v1',
 'passed':True,'positive_E_target_ray_controls':rows,
 'complete_eight_cell_at_e_one':{'positive_sheet_count':3,'signed_local_degree':1,
                                 'individual_oriented_degrees':{'E':1,'E_B':-1,'F_B':1}},
 'lower_internal_wall':'The lower E_B/F_B positive-entry wall has coincident source boundary inverse and opposite oriented local pushed superpole residues, previously independently checked; across its positive E target ray controls two positive sheets enter together with cancelling signed local mapping degrees (-1,+1), retaining local degree +1.',
 'consequence':'There is NO forced fourth positive sheet from LOCAL integer oriented-degree coherence: the observed three positive sheets already contribute net +1, matching the adjacent one-sheet sector. This is not a global image-degree theorem or a correct physical contour.',
 'scope':'Exact positive controls e=1/20,1/2,1 on one E target ray; complete eight-cell positivity and degree at e=1. Other cells/target regions, supersymmetric gluing and full nine-point form open.'}
(OUT/'nine-point-three-positive-sheets-signed-degree-coherence.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'one_to_three_positive_sheets':True,
 'oriented_degree_before_and_after':[r['signed_local_degree_among_E_EB_FB'] for r in rows],
 'fourth_sheet_for_local_degree_required':False},indent=2))
