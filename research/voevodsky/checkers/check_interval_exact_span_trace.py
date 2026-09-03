from __future__ import annotations
import json,math
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import spherical_jn
import flint
from flint import arb,arb_mat

flint.ctx.prec=160
SOURCE=Path('research/voevodsky/results/regularized_polynomial_coefficients.json')

def concentration_matrix(nodes_per_half_panel=160):
    L=.35;edges=(0.,1.,2.,4.,8.,16.,32.,64.,100.);z,w=leggauss(nodes_per_half_panel)
    us=[];ws=[]
    for a,b in zip(edges[:-1],edges[1:]):
        q=(a+b)/2+(b-a)*z/2;v=(b-a)*w/2
        us.extend((-q[::-1]).tolist());ws.extend(v[::-1].tolist());us.extend(q.tolist());ws.extend(v.tolist())
    u=np.asarray(us);wu=np.asarray(ws);n=np.arange(80)
    j=spherical_jn(n[None,:],L*np.abs(u)[:,None])
    parity=np.where(u[:,None]<0,(-1.)**n[None,:],1.)
    phi=2*L*np.sqrt((2*n+1)/(2*L))[None,:]*j*parity*((-1j)**n)[None,:]
    H=np.real(phi.conj().T@(wu[:,None]*phi))/(2*math.pi)
    return (H+H.T)/2

def imat(A,r):
    return arb_mat([[arb(f'{A[i,j]:.17g} +/- {r:.2g}') for j in range(A.shape[1])] for i in range(A.shape[0])])

def main():
    data=json.loads(SOURCE.read_text(encoding='utf-8'));p=data['ritz_coefficients']
    C=arb_mat([[arb(repr(p[i][j])) for j in range(25)] for i in range(80)])
    G=C.transpose()*C;H=concentration_matrix();tests=[]
    for radius in (1e-10,1e-9,1e-8,1e-7,1e-6,2e-6):
        K=C.transpose()*imat(H,radius)*C
        captured=G.inv()*K;tr=sum((captured[i,i] for i in range(25)),arb(0))
        rho=arb(70)/arb.pi()-tr
        floor=(1-130*rho)/40
        residual_ok=float(rho.upper()) < float((arb(1)/130).lower())
        floor_ok=float(floor.lower()) > 0
        tests.append({'concentration_entry_radius':radius,'captured_trace_interval':str(tr),
          'trace_residual_interval':str(rho),'trace_residual_below_1_over_130':residual_ok,
          'derived_tail_floor_interval':str(floor),'derived_tail_floor_positive':floor_ok,
          'derived_inverse_tail_floor_interval':str(1/floor) if floor_ok else None})
    result={'schema':'marici.voevodsky.interval-exact-span-trace.v1',
      'status':'exact_decimal_span_conditional_concentration_enclosure',
      'source':str(SOURCE),'concentration_matrix_dimension':80,
      'frequency_panels':[0,1,2,4,8,16,32,64,100],
      'nodes_per_half_panel':160,
      'analytic_gauss_remainder_bound':1.873e-61,
      'analytic_gauss_remainder_source':'geometric-panels-make-the-gauss-remainder-negligible-conditional-on-one-standard-theorem.md',
      'tests':tests,'gauss_remainder_bound_attached':True,
      'floating_center_roundoff_mechanically_enclosed':False,
      'continuum_concentration_entries_certified':False,
      'largest_passing_entry_radius':max((t['concentration_entry_radius'] for t in tests if t['derived_tail_floor_positive']),default=None),
      'passed':any(t['derived_tail_floor_positive'] for t in tests)}
    rendered=json.dumps(result,indent=2,sort_keys=True)
    Path('research/voevodsky/results/interval_exact_span_trace.json').write_text(rendered+'\n',encoding='utf-8')
    print(rendered)
if __name__=='__main__':main()
