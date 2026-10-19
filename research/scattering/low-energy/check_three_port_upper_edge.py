"""Upper-edge corollary: exact full-core inverse with explicit scope boundaries."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_three_port_threshold as lower

ROOT=Path(__file__).resolve().parents[3]
HOME=Path(__file__).resolve().parent
PROOF=HOME/'THREE-PORT-UPPER-EDGE.md'
RESULT=HOME/'results/three-port-upper-edge.v1.json'
F=lower.F


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def eye(n):return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def mm(A,B):return [[sum((a*b for a,b in zip(row,col)),F()) for col in zip(*B)] for row in A]


def inverse(A):
    n=len(A);rows=[row[:]+unit for row,unit in zip(A,eye(n))]
    for j in range(n):
        p=next((i for i in range(j,n) if rows[i][j]),None)
        assert p is not None,'singular upper-threshold block'
        rows[j],rows[p]=rows[p],rows[j];factor=rows[j][j].inverse();rows[j]=[v*factor for v in rows[j]]
        for i in range(n):
            if i!=j and rows[i][j]:
                c=rows[i][j];rows[i]=[a-c*b for a,b in zip(rows[i],rows[j])]
    return [row[n:] for row in rows]


def verify_inverse(A,B):assert mm(A,B)==mm(B,A)==eye(len(A)),'wrong full-core inverse'


def build():
    source_audit=lower.audit() # Fresh source binding, K-only and metric checks.
    source=json.loads(lower.SOURCE.read_text(encoding='utf-8'))
    K=[[F(*v) for v in row] for row in source['joint_generator']]
    h=[F(*v) for v in source['gram_diagonal']];n=len(K);assert n==11
    M=[[F(4*int(i==j))-K[i][j]-F(2*int(i==j and i<3)) for j in range(n)] for i in range(n)]
    assert all(h[i]*M[i][j]==h[j]*M[j][i] for i in range(n) for j in range(n))
    G=inverse(M);verify_inverse(M,G)
    assert all(h[i]*G[i][j]==h[j]*G[j][i] for i in range(n) for j in range(n))
    controls=[]
    for name in ('omit-contact-diagonal','perturb-inverse'):
        try:
            if name=='omit-contact-diagonal':
                wrong=[[v+F(int(i==j and i<3)) for j,v in enumerate(row)] for i,row in enumerate(M)]
                verify_inverse(wrong,G)
            else:
                wrong=copy.deepcopy(G);wrong[0][0]=wrong[0][0]+1;verify_inverse(M,wrong)
        except AssertionError:controls.append(name)
        else:raise AssertionError('upper-edge hostile accepted: '+name)
    # Whitening makes G Hermitian: trace(G^2) is its squared Frobenius norm.
    norm_squared=sum((G[i][j]*G[j][i] for i in range(n) for j in range(n)),F())
    assert norm_squared.positive()
    A=1
    while not (F(A*A)-norm_squared).positive():A*=2
    assert A==8,'review the documented source-specific constants before regenerating'
    paths={PROOF,Path(__file__),Path(lower.__file__),HOME/'THREE-PORT-COMPLETENESS-PROOF.md',HOME/'test_three_port_upper_edge.py'}
    paths.update(ROOT/p for p in source_audit['source_sha256'])
    return {'schema':'marici.scattering.low-energy-three-port-upper-edge.v1','status':'pass',
        'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in sorted(paths)},
        'core_dimension':11,'upper_block':'4I-K-2P','upper_block_rank':11,
        'upper_block_inverse':[[v.encoded() for v in row] for row in G],
        'port_compression_inverse':[[G[i][j].encoded() for j in range(3)] for i in range(3)],
        'weighted_self_adjoint':True,'coefficient_limit':'I3','endpoint_amplitude_limit':'-I3',
        'squared_whitened_frobenius_norm':norm_squared.encoded(),
        'certified_inverse_norm_upper_bound':A,
        'certified_energy_window_width':str(min(Q(1),Q(1,16*A*A))),
        'certified_packet_probability_constant':16*A*A,
        'uniform_coefficient_bound':'||S_hat-I3||<=4a*sqrt(4-E), a=||M4^-1||_H',
        'energy_window':'0<4-E<min(1,1/(16a^2))',
        'single_incident_port_packet_other_port_probability_bound':'16a^2*epsilon',
        'finite_flux_assigned_at_threshold':False,'analytic_argument_machine_formalized':False,
        'source_nonsingularity_already_used_by':'C2 full-space bound-count proof',
        'new_live_proposition_admitted':False,'C12_protocol_renewed':False,
        'physical_outcomes_admitted':False,'hostile_controls_refused':controls}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale upper-edge receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','upper_block_rank','coefficient_limit','endpoint_amplitude_limit','certified_inverse_norm_upper_bound','certified_energy_window_width','certified_packet_probability_constant','new_live_proposition_admitted','hostile_controls_refused')}))


if __name__=='__main__':main()
