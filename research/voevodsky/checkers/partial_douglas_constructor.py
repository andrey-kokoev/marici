"""Finite-packet partial Douglas constructor.

Input JSON (optional argv[1]): {"A_S": [[...]], "A_B": [[...]], "tol": 1e-10}.
Complex entries may be numbers or strings accepted by complex().  With no input,
runs one feasible and one hostile fixture.  The output either contains C and F or
a normalized witness p for failure.
"""
import json, sys
from pathlib import Path
try:
    import numpy as np
except ModuleNotFoundError:
    sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
    import numpy as np

def matrix(rows):
    return np.array([[complex(x) for x in row] for row in rows], dtype=complex)

def pack(a):
    a=np.real_if_close(a, tol=1000)
    if np.isrealobj(a): return np.asarray(a).tolist()
    return [[[float(z.real),float(z.imag)] for z in row] for row in np.asarray(a)]

def construct(AS,AB,tol=1e-10):
    if AS.shape[1] != AB.shape[1]: raise ValueError('A_S and A_B must have the same source dimension')
    # Kernel inclusion: inspect nullspace of A_S.
    u,s,vh=np.linalg.svd(AS,full_matrices=True)
    rank=int(np.sum(s > tol*(s[0] if len(s) and s[0] else 1.0)))
    null=vh[rank:].conj().T
    if null.shape[1]:
        vals=np.linalg.norm(AB@null,axis=0)
        j=int(np.argmax(vals))
        if vals[j] > tol:
            p=null[:,j]/np.linalg.norm(null[:,j])
            return {'status':'REFUSED_KERNEL','witness_p':pack(p.reshape(1,-1)),'norm_AS_p':float(np.linalg.norm(AS@p)),'norm_AB_p':float(np.linalg.norm(AB@p))}
    C0=AB@np.linalg.pinv(AS,rcond=tol)
    residual=np.linalg.norm(C0@AS-AB)
    cnorm=float(np.linalg.svd(C0,compute_uv=False)[0]) if C0.size else 0.0
    if cnorm > 1+tol:
        # Right singular vector gives a target-range norm witness; pull back minimally.
        _,_,vhc=np.linalg.svd(C0)
        x=vhc[0].conj();p=np.linalg.pinv(AS,rcond=tol)@x
        if np.linalg.norm(p): p/=np.linalg.norm(p)
        return {'status':'REFUSED_NORM','operator_norm_C0':cnorm,'factorization_residual':float(residual),'witness_p':pack(p.reshape(1,-1)),'norm_AS_p':float(np.linalg.norm(AS@p)),'norm_AB_p':float(np.linalg.norm(AB@p))}
    defect=np.eye(C0.shape[1])-C0.conj().T@C0
    lam,U=np.linalg.eigh((defect+defect.conj().T)/2)
    lam=np.maximum(lam,0)
    D=(U*np.sqrt(lam))@U.conj().T
    F=D@AS
    gram_res=np.linalg.norm(F.conj().T@F-(AS.conj().T@AS-AB.conj().T@AB))
    return {'status':'CONSTRUCTED','C':pack(C0),'F':pack(F),'operator_norm_C':cnorm,'factorization_residual':float(residual),'gram_residual':float(gram_res)}

def run_fixture():
    feasible=construct(matrix([[1,0],[0,1]]),matrix([[.5,0],[0,.25]]))
    hostile=construct(matrix([[0,0]]),matrix([[1,0]]))
    return {'feasible_fixture':feasible,'hostile_fixture':hostile,'universal_claim':False,'rh_proved':False}

if __name__=='__main__':
    if len(sys.argv)>1:
        data=json.loads(Path(sys.argv[1]).read_text());out=construct(matrix(data['A_S']),matrix(data['A_B']),float(data.get('tol',1e-10)))
        print(json.dumps(out,indent=2))
    else:
        out=run_fixture();p=Path(__file__).parents[1]/'results'/'partial-douglas-constructor-fixtures.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
