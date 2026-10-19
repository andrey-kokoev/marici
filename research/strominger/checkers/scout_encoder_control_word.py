"""Bounded numerical word scout. Its output is NOT an accuracy certificate."""
from pathlib import Path
import argparse
import hashlib
import json
import numpy as np
from scipy.optimize import minimize

BASE=Path(__file__).resolve().parents[1]


def main(layers,iterations,output_name):
    assert Path(output_name).name==output_name and output_name.endswith('.json')
    names={'source':'neutron-seam-control-transport.json','memory':'neutron-comparison-memory.json',
           'scattering':'neutron-autonomous-rim-scattering.json','orbit':'encoder-conjugated-bank-controls.json'}
    raw={k:(BASE/'results'/v).read_bytes() for k,v in names.items()}
    data={k:json.loads(v) for k,v in raw.items()}
    def array(x):
        from fractions import Fraction
        return np.array([[float(Fraction(v)) for v in row] for row in x])
    M=array(data['source']['metric']);G=array(data['memory']['memory_metric'])
    B=array(data['memory']['residual_incidence']);E=array(data['scattering']['exact_bright_basis'])
    C=np.linalg.cholesky(M).T;Cm=np.linalg.cholesky(G).T
    Cg=np.linalg.cholesky(E.T@M@E).T
    Eorth=C@E@np.linalg.inv(Cg)
    D=Cm@B@np.linalg.inv(C)
    left,s,right=np.linalg.svd(D,full_matrices=False)
    assert s[14]>1e-6 and s[15]<1e-10
    W=left[:,:15]@right[:15,:]
    target=np.vstack(((np.eye(24)-W.T@W)@Eorth,W@Eorth)).astype(complex)
    initial=np.vstack((Eorth,np.zeros((21,5)))).astype(complex)
    Cfull=np.zeros((45,45));Cfull[:24,:24]=C;Cfull[24:,24:]=Cm
    directions=array(data['orbit']['directions'])@Cfull.T
    directions/=np.linalg.norm(directions,axis=1)[:,None]
    rng=np.random.default_rng(202610)
    order=np.concatenate([rng.permutation(39) for _ in range(layers)])
    ds=directions[order]
    def loss(theta, gradient=True):
        phases=np.exp(-1j*theta)
        state=initial.copy()
        coeffs=[]
        for d,z in zip(ds,phases):
            coeff=d@state
            coeffs.append(coeff)
            state+=(z-1)*d[:,None]*coeff[None,:]
        residual=state-target
        cost=float(np.vdot(residual,residual).real/2)
        if not gradient:return cost,state
        grad=np.empty(len(theta))
        for k in range(len(theta)-1,-1,-1):
            d,z=ds[k],phases[k]
            dual=d@residual
            grad[k]=np.vdot(dual,(-1j*z)*coeffs[k]).real
            residual+=(np.conj(z)-1)*d[:,None]*dual[None,:]
        return cost,grad
    theta=rng.normal(scale=.5,size=len(order))
    # Numerical finite-difference hostile detects a wrong reverse-mode sign.
    value,grad=loss(theta)
    for i in (0,len(order)//2,len(order)-1):
        step=np.zeros(len(order));step[i]=1e-6
        fd=(loss(theta+step,False)[0]-loss(theta-step,False)[0])/2e-6
        assert abs(fd-grad[i])<1e-6
    result=minimize(loss,theta,jac=True,method='L-BFGS-B',options={'maxiter':iterations,'maxcor':30,'ftol':1e-15,'gtol':1e-10,'maxls':30})
    cost,state=loss(result.x,False)
    # Map each numerical phase to the exact source stereographic parameter.
    # z(t) uses +i sqrt(3), while the optimizer uses exp(-i theta).
    bits=36
    controls=[]
    for i,angle in zip(order,result.x):
        t=-np.tan(angle/2)/np.sqrt(3)
        numerator=int(round(float(t)*2**bits))
        controls.append({'conjugate_direction':int(i),'t_numerator':str(numerator),'t_denominator':str(2**bits)})
    report={'status':'scout_only','layers':layers,'optimization_iterations':int(result.nit),
        'optimizer_message':str(result.message),'numerical_frobenius_error':float(np.linalg.norm(state-target)),
        'numerical_operator_error':float(np.linalg.norm(state-target,ord=2)),
        'controls':controls,'phase_parameter_bits':bits,
        'source_hashes':{str((BASE/'results'/names[k]).relative_to(BASE.parents[1])).replace('\\','/'):hashlib.sha256(v).hexdigest() for k,v in raw.items()},
        'scope':'Numerical scout and dyadic phase proposal only. Requires independent exact-metric certification. Bounded failure does not refute existential synthesis.'}
    report['source_hashes'][Path(__file__).resolve().relative_to(BASE.parents[1]).as_posix()]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (BASE/'results'/output_name).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['status','layers','optimization_iterations','optimizer_message','numerical_frobenius_error','numerical_operator_error']}))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--layers',type=int,default=8);p.add_argument('--iterations',type=int,default=1500)
    p.add_argument('--output',default='encoder-control-word-scout.json')
    a=p.parse_args();main(a.layers,a.iterations,a.output)
