from __future__ import annotations
import json
from pathlib import Path
import flint
from flint import arb,arb_mat

flint.ctx.prec=128
SOURCE=Path('research/voevodsky/results/regularized_polynomial_coefficients.json')
TAIL=arb('4.36e-13');ETA=arb('1e-8')

def exact_mat(a):return arb_mat([[arb(repr(x)) for x in row] for row in a])
def radius_mat(a,r):return arb_mat([[arb(f'{x:.17g} +/- {r:.2g}') for x in row] for row in a])

def positive_ldl(A):
 n=A.nrows();L=[[arb(0) for _ in range(n)] for _ in range(n)];D=[arb(0) for _ in range(n)];least=None
 for i in range(n):L[i][i]=arb(1)
 for j in range(n):
  d=A[j,j]
  for k in range(j):d-=L[j][k]*L[j][k]*D[k]
  if not d>0:return False,j,str(d),least
  D[j]=d;least=float(d.lower()) if least is None else min(least,float(d.lower()))
  for i in range(j+1,n):
   v=A[i,j]
   for k in range(j):v-=L[i][k]*L[j][k]*D[k]
   L[i][j]=v/d
 return True,n,None,least

def main():
 data=json.loads(SOURCE.read_text(encoding='utf-8'))
 C80=exact_mat(data['ritz_coefficients']);D=exact_mat(data['tail_map_coefficients'])
 C=arb_mat([[C80[i,j] if i<80 else arb(0) for j in range(25)] for i in range(160)])
 G=C.transpose()*C;Ginv=G.inv();DQ=D-C*(Ginv*(C.transpose()*D));Z=C-DQ
 kappa0=data['derived_inverse_tail_floor'];tests=[]
 for radius in (1e-10,1e-9,1e-8,1e-7,1e-6,3e-6,1e-5):
  H=radius_mat(data['cutoff_form_legendre_matrix'],radius)
  J=Z.transpose()*H*Z;AZ=H*Z;R=AZ-C*(Ginv*(C.transpose()*AZ))
  gram=(1+ETA)*(R.transpose()*R);tail=(1+1/ETA)*TAIL*TAIL
  for i in range(25):gram[i,i]+=tail
  lower=J-arb(f'{kappa0:.17g} +/- 1.0')*gram
  ok,pivot,failed,least=positive_ldl(lower)
  jmax=max(float(J[i,j].rad()) for i in range(25) for j in range(25))
  rmax=max(float(R[i,j].rad()) for i in range(160) for j in range(25))
  tests.append({'cutoff_form_entry_radius':radius,'candidate_form_max_radius':jmax,
   'residual_coefficient_max_radius':rmax,'positive':ok,'stopping_pivot':pivot,
   'failed_pivot_interval':failed,'minimum_ldl_pivot_lower':least})
 passing=[t for t in tests if t['positive']]
 result={'schema':'marici.voevodsky.interval-cutoff-form-matrix-sensitivity.v1','source':str(SOURCE),
  'tests':tests,'largest_passing_cutoff_form_entry_radius':max((t['cutoff_form_entry_radius'] for t in passing),default=None),
  'cutoff_form_continuum_enclosed':False,'passed':bool(passing)}
 rendered=json.dumps(result,indent=2,sort_keys=True)
 Path('research/voevodsky/results/interval_cutoff_form_matrix_sensitivity.json').write_text(rendered+'\n',encoding='utf-8')
 print(rendered)
if __name__=='__main__':main()
