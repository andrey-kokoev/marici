"""Falsify naive specialization of sourced psi at two external bracket walls."""
import contextlib,functools,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_four_mass_complete_component_companion_trace as psi
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
eps=s.symbols('eps')
families=[
 ('1234',s.Matrix([[eps,1,1,1],[0,1,0,0],[0,0,1,0],[0,0,0,1],
                   [1,2,1,4],[2,3,5,7],[3,5,7,11],[5,8,13,21]])),
 ('5678',s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],
                   [10+eps,16,25,39],[2,3,5,7],[3,5,7,11],[5,8,13,21]]))]
rows=[]
for name,z in families:
 def makebr(at):
  data=z.subs(eps,at)
  @functools.lru_cache(None)
  def br(i,j,k,l):return data[[i-1,j-1,k-1,l-1],:].det(method='domain-ge')
  return br
 b=makebr(0);scale=s.factor(makebr(eps)(*map(int,name))/eps)
 assert scale!=0 and s.cancel(makebr(eps)(*map(int,name))-scale*eps)==0
 e0,e1=b(8,5,6,3),b(8,5,6,4)
 f0,f1=b(5,6,3,7),b(5,6,4,7)
 n0,n1=b(1,2,7,3),b(1,2,8,3)
 d0,d1=b(4,1,2,7),b(4,1,2,8)
 A=e0*d1+e1*n1;B=e0*d0+e1*n0-f0*d1-f1*n1;C=-f0*d0-f1*n0
 assert A!=0 and B*B-4*A*C!=0
 T=s.Matrix([[0,-C/A],[1,-B/A]]);I=s.eye(2)
 beta_den=d0*I+d1*T
 singular=[]
 if beta_den.det()==0:singular.append('auxiliary_beta_denominator')
 else:
  beta=(n0*I+n1*T)*beta_den.inv()
  def aux(seq):
   return b(*(3 if x=='B' else x for x in seq))*I+b(*(4 if x=='B' else x for x in seq))*beta
  Bfactors=[aux(seq) for seq in (('B',5,6,7),(6,7,8,'B'),(7,8,'B',5),(8,'B',5,6))]
  singular.extend('B_cyclic_'+str(i) for i,F in enumerate(Bfactors) if F.det()==0)
 assert singular
 if name=='1234':assert 'auxiliary_beta_denominator' in singular
 else:assert len(singular)==4
 rows.append({'wall':name,'bracket_scale':str(scale),'quadratic_discriminant_nonzero':True,
              'additional_nonunits_before_trace':singular,
              'simple_pole_by_single_denominator_is_not_certified':True})
report={'schema':'marici.nima.four-mass-external-pole-wall-admissibility.v1','passed':True,
 'tested_walls':rows,
 'result':'At both exact independent one-parameter external four-bracket walls the naive recipe remove 1/<I>, set eps=0, and trace fails: the auxiliary beta chart is nonunit at <1234>=0; four other B five-bracket denominators are nonunits at <5678>=0. The quadratic discriminants remain nonzero. One must first compute the complete rational two-sheet trace in a suitable chart or use a controlled local Laurent/residue algebra, then specialize.',
 'boundary':'A denominator-admissibility obstruction, NOT proof of a pole, pole cancellation or residue in the complete rational invariant. The prior intrinsic source w2-pole remains distinct.'}
(OUT/'four-mass-external-pole-wall-admissibility.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'walls':[r['wall'] for r in rows],
 'additional_nonunits':[r['additional_nonunits_before_trace'] for r in rows],
 'external_pole_claimed':False},indent=2))
