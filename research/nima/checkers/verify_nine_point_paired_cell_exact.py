"""Independent exact replay of algebraic paired cell and image-rank claims."""
import copy,json
from itertools import combinations
from pathlib import Path
import sympy as s
from check_nine_point_no_seven_support_packet import replay
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
def check(frozen,lower,upper,claim):
 assert replay(frozen,lower)==36
 witness=upper['eight_label_source_witness'];labels=witness['retained_labels'];assert labels==claim['retained_source_labels']
 assert witness['deleted_label']==claim['deleted_label']==3
 C=s.Matrix([[s.Rational(v) for v in row] for row in witness['source_rows']])[:,[i-1 for i in labels]]
 Z=s.Matrix([[j**d for d in range(6)] for j in labels]);inv=Z[:6,:].inv()
 k=s.Matrix([list(-Z[6,:]*inv)+[1,0],list(-Z[7,:]*inv)+[0,1]])
 assert k*Z==s.zeros(2,6)
 a,b,c,d,z=s.symbols('a b c d z');variables=(a,b,c,d)
 def L(i,j):
  const=C[0,i]*C[1,j]-C[0,j]*C[1,i]
  linear=a*(k[0,i]*C[1,j]-k[0,j]*C[1,i])+b*(k[1,i]*C[1,j]-k[1,j]*C[1,i])
  linear+=c*(C[0,i]*k[0,j]-C[0,j]*k[0,i])+d*(C[0,i]*k[1,j]-C[0,j]*k[1,i])
  return s.expand(const+linear+z*(k[0,i]*k[1,j]-k[0,j]*k[1,i]))
 pairs=[(labels.index(i),labels.index(j)) for i,j in claim['paired_source_edges']]
 assert len(set(pairs))==4 and set(i for p in pairs for i in p)==set(range(8))
 M,rhs=s.linear_eq_to_matrix([L(*p) for p in pairs],variables);assert M.det()!=0
 solution=list(M.inv()*rhs);sub=dict(zip(variables,solution))
 P=s.Poly(s.together(z-solution[0]*solution[3]+solution[1]*solution[2]),z)
 assert P.degree()==2 and s.expand(P.as_expr()-s.sympify(claim['quadratic_graph_polynomial'],locals={'q':z}))==0
 left,right=map(s.Rational,claim['unique_root_interval']);assert left<right and P.eval(left)*P.eval(right)<0
 nonpairs=set(combinations(range(8),2))-set(pairs);assert len(nonpairs)==24
 bounds=[]
 for p in nonpairs:
  f=s.Poly(s.expand(L(*p).subs(sub)),z);assert f.degree()<=1
  bounds.extend((f.eval(left),f.eval(right)))
 assert min(bounds)>0 and min(bounds)==s.Rational(claim['minimum_rational_endpoint_minor_bound'])
 jac=s.Matrix([s.expand(L(*p).subs(z,a*d-b*c)) for p in pairs]).jacobian(variables)
 det=s.Poly(s.cancel(jac.det().subs(sub)),z)
 assert s.gcd(det,P).degree()==0 and claim['jacobian_graph_polynomial_coprime_to_root_polynomial']
 assert claim['cell_source_dimension']==claim['target_dimension']==8
 return True
def main():
 frozen=json.loads((OUT/'nine-point-support-stress.json').read_text())['first_no_seven_support_target']
 lower=json.loads((OUT/'nine-point-no-seven-support-verification.json').read_text())
 upper=json.loads((OUT/'nine-point-minimum-eight-support.json').read_text())
 claim=json.loads((OUT/'nine-point-paired-cell-exact.json').read_text());assert check(frozen,lower,upper,claim)
 refused=[]
 for defect in ('wrong-isolation-interval','corrupt-positive-bound','repeat-pair','missing-seven-support-exclusion'):
  bad=copy.deepcopy(claim);lo=copy.deepcopy(lower)
  if defect=='wrong-isolation-interval':bad['unique_root_interval'][0]='0'
  if defect=='corrupt-positive-bound':bad['minimum_rational_endpoint_minor_bound']='0'
  if defect=='repeat-pair':bad['paired_source_edges'][1]=bad['paired_source_edges'][0]
  if defect=='missing-seven-support-exclusion':lo['certificates'].pop()
  try:check(frozen,lo,upper,bad)
  except (AssertionError,ValueError,KeyError):refused.append(defect)
  else:raise AssertionError('mutation accepted: '+defect)
 result={'passed':True,'source_support':8,'full_image_rank':8,'matched_pair_constraints':4,
  'positive_other_minors':24,'seven_support_subsets_excluded':36,'mutations_refused':refused,
  'scope':'Fixed positive n=9 target and one exact algebraic candidate cell; physical history-form match and global coverage open.'}
 (OUT/'nine-point-paired-cell-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
