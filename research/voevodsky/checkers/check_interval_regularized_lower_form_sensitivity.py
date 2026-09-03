from __future__ import annotations
import json
from pathlib import Path
import flint
from flint import arb,arb_mat

flint.ctx.prec=160
SOURCE=Path('research/voevodsky/results/regularized_polynomial_coefficients.json')
TAIL=arb('4.36e-13');ETA=arb('1e-8')

def imat(a,r,rows=None):
    if rows is not None:a=a[:rows]
    return arb_mat([[arb(f'{x:.17g} +/- {r:.2g}') for x in row] for row in a])

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
    J=data['candidate_form_matrix'];R=data['residual_legendre_coefficients']
    kappa0=data['derived_inverse_tail_floor'];tests=[]
    for jr in (1e-8,1e-7,1e-6,1e-5,1e-4,3e-4,5e-4,1e-3):
      for rr in (1e-12,1e-11,1e-10,1e-9,1e-8,1e-7,1e-6,1e-5,1e-4):
        Ji=imat(J,jr);Ri=imat(R,rr,160);gram=Ri.transpose()*Ri
        gram=(1+ETA)*gram
        tail_correction=(1+1/ETA)*TAIL*TAIL
        for i in range(25):gram[i,i]+=tail_correction
        kappa=arb(f'{kappa0:.17g} +/- 1.0')
        lower=Ji-kappa*gram
        ok,pivot,failed,least=positive_ldl(lower)
        tests.append({'candidate_form_entry_radius':jr,'residual_coefficient_radius':rr,
          'inverse_tail_floor_radius':1.0,'positive':ok,'stopping_pivot':pivot,
          'failed_pivot_interval':failed,'minimum_ldl_pivot_lower':least})
    passing=[t for t in tests if t['positive']]
    result={'schema':'marici.voevodsky.interval-regularized-lower-form-sensitivity.v1',
      'source':str(SOURCE),'residual_degree_count':160,'analytic_tail_bound':'4.36e-13',
      'tail_split_eta':'1e-8','tests':tests,'passing_test_count':len(passing),
      'candidate_form_continuum_enclosed':False,'residual_coefficients_continuum_enclosed':False,
      'passed':bool(passing)}
    rendered=json.dumps(result,indent=2,sort_keys=True)
    Path('research/voevodsky/results/interval_regularized_lower_form_sensitivity.json').write_text(rendered+'\n',encoding='utf-8')
    print(rendered)
if __name__=='__main__':main()
