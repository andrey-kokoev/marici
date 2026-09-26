"""Finite linear interface prototype, NOT a port-level interaction-net implementation.
Pole records and off-face values are separate observations, not interchangeable.
"""
import contextlib, io, itertools, json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_two_cube_families_offface_chi1_chi5_independence as data
ROOT=Path(__file__).resolve().parents[3]
alpha,beta=s.symbols('alpha beta')
weights={'zero2':alpha,'zero3':beta}
components=((2,4),(1,4)) # physical chi3^4chi5^4, chi2^4chi5^4
records={}
for key,C in data.face.C.items():
 p=data.points[key]
 J=s.Matrix.hstack(*[s.Matrix(list(C.diff(v).subs(p)*data.z)) for v in data.vars]).det(method='domain-ge')
 scale=s.factor(data.cube.orient[key.split('_',1)[1]]*(C.subs(p)*data.h).det()**4/
     (s.prod(p[v] for v in data.vars[:6])*p[data.u]*(p[data.t]-p[data.u])*J))
 records[key]={'family':key.split('_',1)[0], 'members':frozenset([key]),
  'pole':s.Rational(data.face.report['calibrated_oriented_normalized_superpole_residue_factors'][key]),
  'value':tuple(s.factor(scale*C[:,list(pair)].det().subs(p)**4) for pair in components)}
def observe(state):
 return tuple(s.factor(sum(weights[r['family']]*r['value'][i] for r in state.values())) for i in range(2))
def reduce_pair(state,family):
 keys=[family+'_E_B',family+'_F_B']
 assert all(k in state for k in keys), 'consumed pair cannot be reused'
 a,b=(state[k] for k in keys)
 assert a['family']==b['family'] and not (a['members'] & b['members'])
 assert a['pole']+b['pole']==0
 result={k:v for k,v in state.items() if k not in keys}
 result[family+'_remainder']={'family':family,'members':a['members']|b['members'],
  'pole':s.S.Zero,'value':tuple(s.factor(x+y) for x,y in zip(a['value'],b['value']))}
 assert observe(result)==observe(state)
 return result
initial=observe(records);finals=[]
for order in itertools.permutations(weights):
 state=dict(records)
 for family in order:state=reduce_pair(state,family)
 finals.append(state)
assert finals[0]==finals[1]
assert initial[0]!=0 and initial[1]!=0
assert s.diff(initial[0],beta)==0 and s.diff(initial[1],alpha)==0
assert s.diff(initial[0],alpha)!=0 and s.diff(initial[1],beta)!=0
try:
 reduce_pair(finals[0],'zero2')
except AssertionError:
 reuse_rejected=True
else:
 raise AssertionError('linear consumption failed')
# A residue-only erasure is confluent too, but violates both future observations.
assert observe({})!=initial
# Two coefficient choices have identical vanishing poles yet distinct observations.
assert tuple(v.subs({alpha:1,beta:0}) for v in initial)!=tuple(v.subs({alpha:1,beta:1}) for v in initial)
report={'passed':True,'model':'finite linear pair-rewrite interface; no runtime copying or port-net claim',
 'input':'four exact positive sheet values at e=1 plus separately certified shared-wall normalized residues',
 'tested_orders':2,'normal_forms_equal':True,'all_steps_preserve_two_component_observer':True,
 'consumed_pair_reuse_rejected':reuse_rejected,'residue_only_erasure_fails_observer':True,
 'contour_weights_remain_free':['alpha','beta'],
 'observed_components':[str(x) for x in initial],
 'scope':'Witness for a two-component finite continuation interface, not full fermionic sufficiency, all-target semantics or physical contour selection.'}
(ROOT/'research/nima/results/four-cell-continuation-rewrite-probe.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='observed_components'},indent=2))
