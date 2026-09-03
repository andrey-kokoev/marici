from __future__ import annotations
import json
from pathlib import Path
import flint
from flint import arb,arb_mat

flint.ctx.prec=192
SOURCE=Path('research/voevodsky/results/regularized_polynomial_coefficients.json')

def exact_ball(x): return arb(repr(x))
def contains_zero(x): return x.lower()<=0 and x.upper()>=0

def positive_ldl(A):
    n=A.nrows();L=[[arb(0) for _ in range(n)] for _ in range(n)];D=[arb(0) for _ in range(n)]
    for i in range(n): L[i][i]=arb(1)
    minimum=None
    for j in range(n):
        d=A[j,j]
        for k in range(j): d-=L[j][k]*L[j][k]*D[k]
        if not d>0: return False,j,str(d),minimum
        D[j]=d;minimum=float(d.lower()) if minimum is None else min(minimum,float(d.lower()))
        for i in range(j+1,n):
            v=A[i,j]
            for k in range(j): v-=L[i][k]*L[j][k]*D[k]
            L[i][j]=v/d
    return True,n,None,minimum

def main():
    data=json.loads(SOURCE.read_text(encoding='utf-8'))
    p=data['ritz_coefficients'];d=data['tail_map_coefficients']
    if len(p)!=80 or any(len(r)!=25 for r in p): raise ValueError('Ritz shape is not 80x25')
    if len(d)!=160 or any(len(r)!=25 for r in d): raise ValueError('tail-map shape is not 160x25')
    C=arb_mat([[exact_ball(p[k][j]) for j in range(25)] for k in range(80)])
    D=arb_mat([[exact_ball(d[k][j]) for j in range(25)] for k in range(160)])
    C160=arb_mat([[C[k,j] if k<80 else arb(0) for j in range(25)] for k in range(160)])
    G=C.transpose()*C;ok,pivot,failed,minpivot=positive_ldl(G)
    if not ok: raise ArithmeticError(f'Gram LDL failed at {pivot}: {failed}')
    X=G.inv()*(C160.transpose()*D)
    DQ=D-C160*X
    cross=C160.transpose()*DQ
    cross_fail=[];max_cross_radius=0.
    for i in range(25):
        for j in range(25):
            q=cross[i,j];max_cross_radius=max(max_cross_radius,float(q.rad()))
            if not contains_zero(q): cross_fail.append([i,j,str(q)])
    correction=D-DQ
    correction_upper=0.
    for i in range(160):
        row=0.
        for j in range(25): row+=max(abs(float(correction[i,j].lower())),abs(float(correction[i,j].upper())))
        correction_upper=max(correction_upper,row)
    Z=C160-DQ;ZG=Z.transpose()*Z;z_gram_row_upper=0.
    for i in range(25):
        row=0.
        for j in range(25): row+=max(abs(float(ZG[i,j].lower())),abs(float(ZG[i,j].upper())))
        z_gram_row_upper=max(z_gram_row_upper,row)
    z_operator_norm_upper=z_gram_row_upper**0.5
    result={'schema':'marici.voevodsky.exact-decimal-span.v1','source':str(SOURCE),
      'ritz_shape':[80,25],'tail_map_shape':[160,25],
      'gram_positive':ok,'minimum_ldl_pivot_lower':minpivot,
      'exact_span_tail_orthogonality_enclosed':not cross_fail,
      'cross_gram_failure_count':len(cross_fail),'first_cross_gram_failures':cross_fail[:3],
      'maximum_cross_gram_interval_radius':max_cross_radius,
      'tail_orthogonalization_max_row_sum_upper':correction_upper,
      'z_gram_maximum_absolute_row_sum_upper':z_gram_row_upper,
      'z_operator_norm_upper':z_operator_norm_upper,
      'z_operator_norm_below_11_2':z_operator_norm_upper<11.2,
      'concentration_trace_certified':False,'continuum_bilinear_integrals_certified':False,
      'passed':ok and not cross_fail and z_operator_norm_upper<11.2}
    rendered=json.dumps(result,indent=2,sort_keys=True)
    Path('research/voevodsky/results/interval_polynomial_coefficients.json').write_text(rendered+'\n',encoding='utf-8')
    print(rendered)
if __name__=='__main__': main()
