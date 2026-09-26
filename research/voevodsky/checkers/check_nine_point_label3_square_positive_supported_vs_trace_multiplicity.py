"""Classify positive-supported inverse sheets separately from four-cell meromorphic traces."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_label3_square_full_chi3_target_trace as trace
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
D,vars=trace.D,trace.vars
w2,w4,w5,w6,w7,w8,t,u=vars
rows=[]
for label,raw in [('first',(1,1,1,1,1,1,3,2)),
                  ('second',(2,3,1,4,2,5,s.Rational(7,2),s.Rational(3,2)))]:
 p=dict(zip(vars,map(s.Rational,raw)));Y=D.subs(p)*trace.Z
 H=Y[:,:2];B=H.inv()*Y[:,2:]
 z=trace.Z[:,2:]-trace.Z[:,:2]*B;h=trace.Z[:,:2]
 def signs(point):
  out={str(v):str(s.sign(s.radsimp(point[v]))) for v in vars[:6]}
  out['u']=str(s.sign(s.radsimp(point[u])))
  out['t-u']=str(s.sign(s.radsimp(point[t]-point[u])))
  assert set(out.values())<= {'-1','0','1'}
  return out
 sheets={}
 for root,point in trace.G.fibre(D.subs(p),trace.Z):
  support=signs(point)
  sheets.setdefault('E',[]).append({'kernel_root':str(root),'positive':all(v=='1' for v in support.values()),
                                    'positivity_signs':support,
                                    'chi3_component':str(trace.pushed(D,point,1,z,h))})
 for name,pairs in trace.bir.zero_sets.items():
  point=trace.inverse_one_sheet(Y,trace.bir.square.source[name],pairs)
  support=signs(point)
  sheets[name]=[{'positive':all(v=='1' for v in support.values()),
                 'positivity_signs':support,
                 'chi3_component':str(trace.pushed(trace.bir.square.source[name],point,
                                                 trace.bir.square.sign[name],z,h))}]
 positive_counts={name:sum(q['positive'] for q in sheets[name]) for name in sheets}
 supported_component=s.factor(sum(s.Rational(q['chi3_component']) for name in sheets
                             for q in sheets[name] if q['positive']))
 meromorphic=s.factor(sum(s.Rational(q['chi3_component']) for name in sheets for q in sheets[name]))
 assert meromorphic==s.Rational(next(r['complete_four_cell_chi3_power4_chi5_power4']
                                   for r in trace.rows if r['target']==label))
 rows.append({'target':label,'positive_preimages_per_cell':positive_counts,
              'all_inverse_sheet_signs':sheets,
              'positive_supported_chi3_power4_chi5_power4_value':str(supported_component),
              'full_meromorphic_four_cell_chi3_power4_chi5_power4_value':str(meromorphic),
              'supported_and_meromorphic_differ':supported_component!=meromorphic})
report={'schema':'marici.nima.nine-point-label3-square-positive-supported-vs-trace-multiplicity.v1',
 'passed':True,'exact_common_positive_target_controls':rows,
 'scope':'Positive source preimage counts and source-restricted versus algebraic meromorphic chi3 component for four explicit label3 square cells at two targets. This is NOT the global positive image form, physical contour or all-cell coverage.'}
(OUT/'nine-point-label3-square-positive-supported-vs-trace-multiplicity.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'rows':[{'target':r['target'],
 'positive_preimages_per_cell':r['positive_preimages_per_cell'],
 'supported_and_meromorphic_differ':r['supported_and_meromorphic_differ']} for r in rows]},indent=2))
