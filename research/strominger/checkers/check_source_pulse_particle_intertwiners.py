"""Preflight exact operation intertwiners, not a new Hamiltonian.

Reconstruct Nima's published six-port exchange, import the live seed registry,
and compare its valid AB,BA loop to current particle operation algebras.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from check_natural_tower_return import PACKETS
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from assemble_relative_geometry import assemble,apply,determinant


def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def transpose(a):return list(map(list,zip(*a)))
def difference(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def rank(a):
    rows=[list(r) for r in a];r=0
    for c in range(len(rows[0])):
        p=next((i for i in range(r,len(rows)) if rows[i][c]),None)
        if p is None:continue
        rows[r],rows[p]=rows[p],rows[r];v=rows[r][c];rows[r]=[x/v for x in rows[r]]
        for i in range(r+1,len(rows)):
            v=rows[i][c];rows[i]=[x-v*y for x,y in zip(rows[i],rows[r])]
        r+=1
        if r==len(rows):break
    return r

def geometric_group(source):
    result=assemble(source);vs=[tuple(map(F,p)) for p in result['vertices']];ix={p:i for i,p in enumerate(vs)};generators=[]
    for g in source['generators']:
        action=(tuple(tuple(map(F,row)) for row in g['matrix']),tuple(map(F,g['translation'])))
        generators.append(tuple(ix[apply(action,p)] for p in vs))
    ident=tuple(range(len(vs)));seen={ident};frontier=[ident]
    while frontier:
        p=frontier.pop()
        for g in generators:
            nxt=tuple(g[p[i]] for i in range(len(vs)))
            if nxt not in seen:seen.add(nxt);frontier.append(nxt)
        if len(seen)>512:raise ValueError('Finite group resource bound exceeded')
    return {'generated_group_order':len(seen),'generator_vertex_permutations':generators,'generated_vertices':len(vs)}


def main():
    labels=[p[0] for p in PACKETS];ends={label:(a,b) for label,a,b in PACKETS}
    assert set(labels)=={'AB','BC','CA','BA','AD','DB'}
    G=[[F(10*int(i==j)+1) for j in range(4)] for i in range(4)]
    H=[[G[i//4][j//4]*G[i%4][j%4] for j in range(16)] for i in range(16)]
    indices=[4*'ABCD'.index(a)+'ABCD'.index(b) for _,a,b in PACKETS]
    features=[[F(int(i==indices[j]),11) for j in range(6)] for i in range(16)]
    D=mm(mm(transpose(features),H),features)
    gram=[[F(i==j)+D[i][j] for j in range(6)] for i in range(6)]
    assert all(D[i][i]==1 for i in range(6)) and determinant(gram)>0
    M=[H[i]+[F(0)]*6 for i in range(16)]+[[F(0)]*16+eye(6)[i] for i in range(6)]
    B=features+[[-F(i==j) for j in range(6)] for i in range(6)]
    assert rank(B)==6 and mm(mm(transpose(B),M),B)==gram
    source_ops={};compressed={}
    for i,label in enumerate(labels):
        direction=[row[i] for row in B]
        mismatch=[-sum(features[k][i]*H[k][j] for k in range(16)) for j in range(16)]+[F(i==j) for j in range(6)]
        E=[[F(a==b)+direction[a]*mismatch[b] for b in range(22)] for a in range(22)]
        R=[[F(a==b)-(gram[i][b] if a==i else 0) for b in range(6)] for a in range(6)]
        assert mm(E,E)==eye(22) and mm(mm(transpose(E),M),E)==M
        assert mm(E,B)==mm(B,R)
        assert mm(R,R)==eye(6) and mm(mm(transpose(R),gram),R)==gram
        source_ops[label]=E;compressed[label]=R
    # AB followed by BA is a valid closed source path. Its powers remain
    # valid composable paths; we do not use a noncomposable pulse word.
    assert ends['AB'][1]==ends['BA'][0] and ends['BA'][1]==ends['AB'][0]
    loop=mm(compressed['BA'],compressed['AB'])
    trace=sum(loop[i][i] for i in range(6));plane_trace=trace-4
    overlap=D[labels.index('AB')][labels.index('BA')]
    assert overlap==F(1,121) and plane_trace==overlap**2-2 and plane_trace.denominator!=1
    assert rank(difference(loop,eye(6)))==2 and determinant(loop)==1
    comm=difference(mm(compressed['AB'],compressed['BA']),loop);assert rank(comm)==2
    # Source trace is rational but NOT integer. Any finite-order matrix has
    # roots of unity as eigenvalues: its trace is an algebraic integer.
    # A rational algebraic integer is an integer => this loop has infinite order.
    groups={};paths=[]
    for name,filename in [('proton','relative-proton.json'),('neutron','mode-neutron.json'),('electron','relative-electron.json')]:
        path=ROOT/'research/voevodsky/inputs'/filename;paths.append(path);groups[name]=geometric_group(json.loads(path.read_text()))
    assert [groups[k]['generated_group_order'] for k in ('proton','neutron','electron')]==[12,3,5]
    verification=ROOT/'research/strominger/results/common-three-carrier-protocol/verification.json';v=json.loads(verification.read_text());assert v['status']=='passed'
    for p,h in {**v['source_hashes'],**v['packet_hashes']}.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    target_rows={}
    for name in groups:
        measure=v['carriers'][name];n=measure['raw_complex_coordinates'];rL=measure['local_rank'];rG=measure['alignment_rank'];rN=measure['return_rank']
        dimensions=[rN,rL-rN,rG-rN,n-rL-rG+rN]
        sectors=[i for i,d in enumerate(dimensions) if d]
        # Signs of I-2L and I-2G on both/L-only/G-only/neither sectors.
        signatures={tuple(((-1 if i in (0,1) else 1)**a)*((-1 if i in (0,2) else 1)**b) for i in sectors) for a in range(2) for b in range(2)}
        assert len(signatures)==4
        target_rows[name]={'raw_coefficient_dimension':n,'geometric_operations':groups[name],
                          'reflected_local_alignment_group_order':len(signatures),
                          'literal_projector_stage_adapter':'rejected: idempotent target cannot intertwine nonidentity involution through an injection',
                          'reflected_stage_adapter':'rejected: target operations commute; source pulse commutator has rank two',
                          'geometric_action_adapter':'rejected: finite target group cannot represent the infinite-order source AB,BA loop faithfully'}
    # Controls: the active source reduction IS an exact faithful intertwiner.
    # Matched states give a trivial 16D fixed sector, but remove all pulses.
    fixed=eye(16)+mm(transpose(features),H)
    assert rank(fixed)==16
    assert all(mm(E,fixed)==fixed for E in source_ops.values())
    checks={'live_six_arrow_registry_used':True,'all_six_original_exchange_involutions_and_metrics':True,
            'faithful_six_dimensional_source_reduction':True,'AB_BA_is_composable_closed_source_history':True,
            'infinite_order_proved_by_nonintegral_rational_trace':True,'source_pulses_noncommuting':True,
            'three_finite_geometric_groups_enumerated':True,'common_stage_receipts_current':True,
            'trivial_fixed_sector_control_retains_no_active_pulse':True}
    result={'status':'passed','checks':checks,'source':{'labels':labels,'full_dimension':22,'active_dimension':6,'fixed_dimension':16,
                'active_metric':[[str(x) for x in r] for r in gram],
                'active_pulses':{k:[[str(x) for x in r] for r in R] for k,R in compressed.items()},
                'valid_loop':['AB','BA'],'loop_trace':str(trace),'rotating_plane_trace':str(plane_trace),'loop_order':'infinite'},
            'targets':target_rows,'scope':'Excludes injective operation intertwiners into the existing finite geometric actions or L/G-derived stages. Does not exclude a larger dynamical record carrier or additional noncommuting target operations.',
            'next_required_data':'Source-addressed target pulse generators and dynamical records with this Gram/action structure; passive history labels and matching return projectors do not suffice.'}
    sources=paths+[Path(__file__).resolve(),verification,ROOT/'research/nima/checkers/check_natural_tower_return.py',ROOT/'research/nima/checkers/check_seed_port_exchange_binding.py',ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    out=ROOT/'research/strominger/results/source-pulse-particle-intertwiners.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':checks,'source_loop_trace':str(trace),'source_loop_order':'infinite','target_geometric_group_orders':{k:g['generated_group_order'] for k,g in groups.items()},'disposition':'No faithful intertwiner into any tested existing target operation algebra.'},indent=2))

if __name__=='__main__':main()
