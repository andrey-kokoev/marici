"""Independent Pluecker-coordinate replay of exact local paired-cell pushforwards."""
import copy,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
def verify(report):
 labels=[1,2,4,5,6,7,8,9];Z=s.Matrix([[j**r for r in range(6)] for j in labels])
 ws=s.symbols('w2 w4 w5 w6 w7 w8');t,u=s.symbols('t u');variables=(*ws,t,u)
 C=s.Matrix([[1,ws[0],0,0,-ws[2],-ws[3],-ws[4],-ws[5]],
             [0,0,1,ws[1],ws[2]*t,ws[3]*t,ws[4]*u,ws[5]*u]])
 assert report['passed'] and len(report['rows'])==2
 for row in report['rows']:
  vals=[s.Rational(z) for z in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]
  point=dict(zip(variables,vals));Y=(C*Z).subs(point)
  assert vals[6]>vals[7]>0 and all(v>0 for v in vals[:6])
  def p(M,i,j):return M[0,i]*M[1,j]-M[0,j]*M[1,i]
  bottom=p(Y,0,1);assert bottom!=0
  derivatives=[]
  for v in variables:
   dY=(C.diff(v)*Z).subs(point);dp=dY[0,0]*Y[1,1]+Y[0,0]*dY[1,1]-dY[0,1]*Y[1,0]-Y[0,1]*dY[1,0]
   entries=[]
   for rownum in range(2):
    for j in range(2,6):
     i=1 if rownum==0 else 0;sgn=-1 if rownum==0 else 1
     delta=p(Y,i,j);ddelta=dY[0,i]*Y[1,j]+Y[0,i]*dY[1,j]-dY[0,j]*Y[1,i]-Y[0,j]*dY[1,i]
     entries.append(sgn*(ddelta*bottom-delta*dp)/bottom**2)
   derivatives.append(s.Matrix(entries))
  det=s.Matrix.hstack(*derivatives).det()
  assert det==s.Rational(row['target_chart_jacobian']) and det!=0
  residue=-s.S.One/(s.prod(vals[:6])*vals[7]*(vals[6]-vals[7]))
  assert residue==s.Rational(row['source_form_coefficient'])
  assert residue/det==s.Rational(row['pushed_local_target_coefficient'])
  assert len(row['branches'])==2 and sum(b['positive_paired_cell'] for b in row['branches'])==1
 return True
def main():
 report=json.loads((OUT/'nine-point-paired-pushforward-samples.json').read_text());assert verify(report)
 refused=[]
 for defect in ('wrong-jacobian','wrong-source-factor','wrong-pushforward','double-positive-branch'):
  bad=copy.deepcopy(report);first=bad['rows'][0]
  if defect=='wrong-jacobian':first['target_chart_jacobian']='1'
  if defect=='wrong-source-factor':first['source_form_coefficient']='1'
  if defect=='wrong-pushforward':first['pushed_local_target_coefficient']='1'
  if defect=='double-positive-branch':first['branches'][0]['positive_paired_cell']=True
  try:verify(bad)
  except (AssertionError,ValueError):refused.append(defect)
  else:raise AssertionError('mutation accepted')
 result={'passed':True,'exact_local_pushforward_samples':2,'mutations_refused':refused,
  'scope':'Two exact local target-form coefficients, not a global canonical-form identity or sourced physical history.'}
 (OUT/'nine-point-paired-pushforward-samples-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
