"""C9 source/polynomial audit supporting the explicit analytic spectral-measure proof."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[3]
HOME=ROOT/'research/scattering/low-energy'
OWNER=ROOT/'research/voevodsky'
sys.path.insert(0,str(OWNER/'checkers'))
from check_native_adapter_collective_closure import F
SOURCE=OWNER/'results/native_joint_generator_resolvent.json'
PROOF=HOME/'NO-SINGULAR-CONTINUOUS-PROOF.md'
RESULT=HOME/'results/no-singular-continuous.v1.json'


def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def add(*polys):
    out=[0]*max(map(len,polys))
    for p in polys:
        for i,x in enumerate(p):out[i]+=x
    return trim(out)

def mul(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):out[i+j]+=x*y
    return trim(out)

def free(n,m):
    if n==0:return [0]
    out=[0]*(n+m)
    for r in range(min(n,m)):out[abs(n-m)+1+2*r]=1
    return trim(out)


def audit():
    source=json.loads(SOURCE.read_text(encoding='utf-8'))
    for p,h in source['source_hashes'].items():assert digest(OWNER/p)==h,p
    K=[[F(*x) for x in row] for row in source['joint_generator']];metric=[F(*x) for x in source['gram_diagonal']]
    assert len(K)==11 and all(h.positive() for h in metric)
    assert all(metric[i]*K[i][j]==metric[j]*K[j][i] for i in range(11) for j in range(11))
    I=[[F(int(i==j)) for j in range(11)] for i in range(11)]
    P=[[F(int(i==j and i<3)) for j in range(11)] for i in range(11)]
    pencil=[I,[[K[i][j]-2*I[i][j]+P[i][j] for j in range(11)] for i in range(11)],
            [[I[i][j]-P[i][j] for j in range(11)] for i in range(11)]]
    assert pencil[0]==I  # det L(0)=det I=1, hence finitely many roots.
    for n in range(1,9):
        for m in range(1,9):
            # Multiply the free resolvent recurrence by w to avoid Laurent terms.
            lhs=add(mul([1,0,1],free(n,m)),mul([0,-1],free(n-1,m)),mul([0,-1],free(n+1,m)))
            assert lhs==([0,1] if n==m else [0])
            assert free(n,m)==free(m,n)
    for n in range(1,9):assert free(n,1)==[0]*n+[1]
    paths={SOURCE,PROOF,Path(__file__),OWNER/'checkers/check_native_adapter_collective_closure.py',OWNER/'native-port-scattering.md'}|{OWNER/p for p in source['source_hashes']}
    return {'schema':'marici.scattering.no-singular-continuous.v1','status':'pass','C9_disposition':'established',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in sorted(paths)},
            'core_dimension':11,'lead_count':3,'schur_pencil_coefficients':[[[v.encoded() for v in row] for row in block] for block in pencil],
            'determinant_constant_term':1,'determinant_degree_upper_bound':22,
            'free_resolvent_exact_recurrence_controls':64,'real_branch_points':[0,4],
            'argument':'All finite-support scalar resolvents are rational in the algebraic Weyl function. Their measures are absolutely continuous away from finitely many exceptional energies; any measure on that finite set is atomic. Density eliminates the singular-continuous projection on the full space.',
            'finite_rank_alone_used_as_proof':False,'point_spectrum_count_claimed':False,
            'wave_operator_completeness_claimed':False,'machine_checked_measure_theory':False,'physical_outcome':None}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    text=json.dumps(audit(),indent=2)+'\n'
    if args.check:assert RESULT.read_text(encoding='utf-8')==text,'stale C9 certificate'
    else:RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(text,encoding='utf-8')
    print('PASS: C9 analytic rational-Weyl proof with exact source/polynomial controls; C2 remains separate.')


if __name__=='__main__':main()
