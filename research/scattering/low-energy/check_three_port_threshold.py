"""C11: fresh exact zero-mode/cyclic checks supporting the analytic threshold proof."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[3]
HOME=ROOT/'research/scattering/low-energy'
OWNER=ROOT/'research/voevodsky'
sys.path.insert(0,str(OWNER/'checkers'))
from check_native_adapter_collective_closure import F,Span,closure,unit
from check_native_port_bound_spectrum import null_vector,sparse

SOURCE=OWNER/'results/native_joint_generator_resolvent.json'
PROOF=HOME/'THREE-PORT-THRESHOLD-PROOF.md'
RESULT=HOME/'results/three-port-threshold.v1.json'


def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def audit():
    source=json.loads(SOURCE.read_text(encoding='utf-8'))
    for path,value in source['source_hashes'].items():assert digest(OWNER/path)==value,path
    K=[[F(*x) for x in row] for row in source['joint_generator']]
    h=[F(*x) for x in source['gram_diagonal']];n=len(K);assert n==11
    assert all(x.positive() for x in h)
    assert all(h[i]*K[i][j]==h[j]*K[j][i] for i in range(n) for j in range(n))
    assert h[:3]==[F('1196/15'),F(20),F(20)]
    rank=Span(n)
    for i,row in enumerate(K):rank.add(row,{'row':i})
    assert len(rank.rows)==10
    v=null_vector(K);port_norm=sum((h[i]*v[i]*v[i] for i in range(3)),F());assert port_norm.positive()
    cyclic=closure([unit(n,i) for i in range(3)],{'K':sparse(K)},n)
    assert len(cyclic.rows)==11
    S=[[F(int(i==j))-2*v[i]*h[j]*v[j]/port_norm for j in range(3)] for i in range(3)]
    assert all(sum((S[k][i]*h[k]*S[k][j] for k in range(3)),F())==(h[i] if i==j else F()) for i in range(3) for j in range(3))
    assert all(sum((S[i][k]*S[k][j] for k in range(3)),F())==int(i==j) for i in range(3) for j in range(3))
    assert sum((S[i][i] for i in range(3)),F())==1
    minus,plus=Span(3),Span(3)
    for i in range(3):
        minus.add([F(int(i==j))-S[i][j] for j in range(3)],{'row':i})
        plus.add([F(int(i==j))+S[i][j] for j in range(3)],{'row':i})
    assert len(minus.rows)==1 and len(plus.rows)==2
    paths={SOURCE,PROOF,Path(__file__),OWNER/'checkers/check_native_adapter_collective_closure.py',OWNER/'checkers/check_native_port_bound_spectrum.py',OWNER/'native-port-scattering.md',OWNER/'native-port-bound-spectrum.md'}|{OWNER/p for p in source['source_hashes']}
    return {'schema':'marici.scattering.three-port-threshold.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in sorted(paths)},
            'core_dimension':n,'core_rank':len(rank.rows),'kernel_dimension':1,
            'kernel_vector':[x.encoded() for x in v],'port_norm_squared':port_norm.encoded(),
            'cyclic_dimension_under_K_alone':len(cyclic.rows),'cyclic_elimination_certificate':cyclic.certificates,
            'coefficient_limit':[[x.encoded() for x in row] for row in S],
            'metric_unitary':True,'involutive':True,'rank_I_minus_S0':1,'rank_I_plus_S0':2,
            'whitened_limit_eigenvalues':[-1,1,1],
            'no_interior_poles_argument':'Imaginary part forces Px=0; an invisible K eigenvector is orthogonal to the full cyclic port span, hence zero.',
            'limit_argument':'Simple-kernel Schur complement i k p+O(k²) with p>0 yields G=uu*/(i k p)+O(1), hence the coefficient Householder limit.',
            'finite_flux_assigned_at_threshold':False,'source_scattering_solver_replayed':False,'physical_outcome':None}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    text=json.dumps(audit(),indent=2)+'\n'
    if args.check:assert RESULT.read_text(encoding='utf-8')==text,'stale C11 certificate'
    else:RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(text,encoding='utf-8')
    print('PASS: C11 exact simple kernel, visible zero mode and K-only cyclic dimension 11; threshold proof supplied.')


if __name__=='__main__':main()
