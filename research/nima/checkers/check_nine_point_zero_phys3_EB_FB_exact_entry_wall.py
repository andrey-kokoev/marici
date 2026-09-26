"""Find exact positive-entry wall for the outside-cube zero-phys3 EB/FB pair."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_zero_phys3_neighbor_pair_second_target as prior
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
first=prior.first;old=first.old;cube=first.cube;Z,K=first.Z,first.K
vars=first.vars;w2,w4,w5,w6,w7,w8,t,u=vars
e=s.symbols('e',positive=True)
a,b,c,d,q=first.a,first.b,first.c,first.d,first.q;T=first.T
p=dict(zip(old.inside.vars,(e,1,1,1,1,1,3,2)))
Y=cube.E['E'].subs(p)*old.Z9
start=(Y*Z[:6,:].inv()).row_join(s.zeros(2,2))
rows=[];points={}
for name in ('E_B','F_B'):
 C=(cube.E if name.startswith('E') else cube.F)[name][:,first.old_columns]
 def lifted(i,j):
  P=s.Poly(old.minor(start+T*K,i,j),a,b,c,d)
  assert P.coeff_monomial(a*d)==-P.coeff_monomial(b*c)
  return P.coeff_monomial(1)+sum(P.coeff_monomial(v)*v for v in (a,b,c,d))+P.coeff_monomial(a*d)*q
 M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in first.zeros[name]],(a,b,c,d))
 assert M.rank()==4
 left=[s.factor((v.T*rhs)[0]) for v in M.T.nullspace()]
 active=next(v for v in left if s.diff(v,q)!=0)
 qr=s.factor(-active.subs(q,0)/s.diff(active,q))
 assert all(s.factor(v.subs(q,qr))==0 for v in left)
 sol=M.gauss_jordan_solve(rhs.subs(q,qr))[0]
 assert s.factor(qr-sol[0]*sol[3]+sol[1]*sol[2])==0
 source=start+T.subs(dict(zip((a,b,c,d),sol)))*K
 gauge=source[:,[0,2]].inv()*source
 point=dict(zip(vars,(gauge[0,1] if name.startswith('E') else gauge[1,1],
            gauge[1,3],-gauge[0,4],-gauge[0,5],-gauge[0,6],-gauge[0,7],
            -gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
 assert all(s.factor(v)==0 for v in gauge-C.subs(point))
 points[name]=point
 rows.append({'cell':name,'w2_inverse':str(s.factor(point[w2])),
              'all_inverse_source_parameters':{str(v):str(s.factor(point[v])) for v in vars}})
shared_roots=set(s.solve(points['E_B'][w2],e)) & set(s.solve(points['F_B'][w2],e))
positive_roots=[r for r in shared_roots if r.is_real and r>0]
assert len(positive_roots)==1
root=positive_roots[0]
assert all(s.factor(points['E_B'][v].subs(e,root)-points['F_B'][v].subs(e,root))==0 for v in vars)
wallpoint=points['E_B']
assert wallpoint[w2].subs(e,root)==0
assert all(s.factor(wallpoint[v].subs(e,root))>0 for v in (w4,w5,w6,w7,w8,u))
assert s.factor((wallpoint[t]-wallpoint[u]).subs(e,root))>0
# Compare against the independently derived zero-physical2 EB/FB entry wall.
chamber=first.support.five.prior.chamber
assert root==chamber.threshold_low
Ywall=cube.E['E'].subs(p).subs(e,root)*old.Z9
trace=first.support.prior.trace
old_EB=trace.inverse_one_sheet(Ywall,trace.bir.square.source['E_B'],
                                trace.bir.zero_sets['E_B'])
old_FB,_,_=first.support.five.inverse_at(root)
assert all(s.factor(old_EB[v]-old_FB[v])==0 for v in vars)
assert all(s.factor(old_EB[v]-points['E_B'][v].subs(e,root))==0 for v in vars)
assert all(s.factor(old_EB[v]-points['F_B'][v].subs(e,root))==0 for v in vars)
# All four cells (two zero-column families times EB/FB) have the
# SAME two-zero-column source matrix at this exact positive facet.
def embed_zero3(C):return s.Matrix.hstack(C[:,:2],s.zeros(2,1),C[:,2:])
assert cube.E['E_B'].subs(old_EB)==cube.F['F_B'].subs(old_EB)
assert cube.E['E_B'].subs(old_EB)==embed_zero3((cube.E['E_B'][:,first.old_columns]).subs(old_EB))
assert cube.E['E_B'].subs(old_EB)==embed_zero3((cube.F['F_B'][:,first.old_columns]).subs(old_EB))
samples=[]
for val in (s.Rational(1,20),root,s.Rational(1,2),s.S.One):
 signs={name:{str(v):str(s.sign(s.radsimp(point[v].subs(e,val)))) for v in vars[:6]}
          for name,point in points.items()}
 for name,point in points.items():
  signs[name]['u']=str(s.sign(point[u].subs(e,val)))
  signs[name]['t-u']=str(s.sign((point[t]-point[u]).subs(e,val)))
 samples.append({'e':str(val),'cells':{name:{'positive':all(z=='1' for z in src.values()),
                   'w2_sign':src['w2']} for name,src in signs.items()}})
report={'schema':'marici.nima.nine-point-zero-phys3-EB-FB-exact-entry-wall.v1',
 'passed':True,'symbolic_E_source_e_ray':'(e,1,1,1,1,1,3,2)',
 'unique_shared_positive_w2_zero_entry_root':str(root),
 'same_complete_source_facet_preimage_at_root':True,
 'common_wall_equals_independent_zero_phys2_cube_EB_FB_entry_root':True,
 'four_cells_from_two_cube_families_share_identical_two_zero_column_source_matrix_at_wall':True,
 'interior_other_source_parameters_at_root':True,
 'inverse_source_rational_functions':rows,'exact_positive_controls':samples,
 'scope':'Four-cell source-facet coincidence and simultaneous paired positive entry across two zero-column families on one exact E target ray. Cross-family normal-cone gluing, pushed superform residues or physical contour weights not proved.'}
(OUT/'nine-point-zero-phys3-EB-FB-exact-entry-wall.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'common_positive_entry_root':str(root),
 'controls':[{'e':r['e'],'positive':[n for n,z in r['cells'].items() if z['positive']]} for r in samples]},indent=2))
