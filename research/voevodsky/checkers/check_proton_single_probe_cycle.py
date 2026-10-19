"""Exact fixed-probe capabilities, source slot-cycle decoder and metric obstruction.
Imports only arithmetic/source constructors. No upstream producer or store is
rewritten. Rank conclusions are also checked with independent rational arithmetic.
"""
from collections import deque
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
from check_proton_native_task_catalogue import (
    ROOT,ZERO,ONE,eye,mzero,mm,mv,adj,msub,rank,rref,nullspace,parse,sparse,vector,norm,div,mul,sub,
)
from verify_proton_native_task_catalogue import realify,rank as qrank,multiply as qmultiply
from assemble_triangle_arrow_source import assemble
from check_triangle_half_phase import mm as qmm,transpose
from check_twelve_triangle_positive_geometry import inv,C as SLOT_CYCLE


def inverse(a):
    n=len(a);rows,pivots=rref([r+s for r,s in zip(a,eye(n))])
    assert pivots[:n]==list(range(n)) and len(pivots)==n
    return [r[n:] for r in rows]

def source_actions(source,report,ports):
    labels=tuple(source['vertices']);points={v:tuple(F(x) for x in source['vertices'][v]) for v in labels}
    generators=[]
    for cycle in report['derived_cycles']:
        mapping=dict(zip(cycle,cycle[1:]+cycle[:1]));generators.append(tuple(labels.index(mapping.get(v,v)) for v in labels))
    unit=tuple(range(4));words={unit:[]};todo=deque([unit])
    while todo:
        p=todo.popleft()
        for j,g in enumerate(generators):
            q=tuple(g[p[i]] for i in range(4))
            if q not in words:words[q]=words[p]+[j];todo.append(q)
    index={p:i for i,p in enumerate(ports)};frame=transpose([points[v] for v in labels[:3]]);back=inv(frame)
    actions={}
    for p in sorted(words):
        mapping={v:labels[p[i]] for i,v in enumerate(labels)}
        R=qmm(transpose([points[mapping[v]] for v in labels[:3]]),back);U=mzero(36,36)
        for j,(edge,axis) in enumerate(ports):
            target=''.join(mapping[v] for v in edge)
            for a in range(3):U[index[target,'xyz'[a]]][j]=(R[a]['xyz'.index(axis)],F(0))
        actions[p]=U
    return labels,points,generators,words,actions


def main():
    contract_path=ROOT/'research/voevodsky/inputs/proton-single-probe-cycle-v1.json'
    contract=json.loads(contract_path.read_text());source_path=ROOT/contract['source'];baseline_path=ROOT/contract['baseline']
    baseline=json.loads(baseline_path.read_text())
    for name,h in baseline['source_hashes'].items():assert sha256((ROOT/name).read_bytes()).hexdigest()==h,name
    source=json.loads(source_path.read_text());report,records=assemble(source)
    assert records==json.loads((ROOT/'research/nima/results/twelve-triangle-1836-arrows.json').read_text())
    ports,(L,G,N)=parse(records);I=eye(36)
    labels,points,generators,words,actions=source_actions(source,report,ports)
    assert len(actions)==12
    for p,U in actions.items():
        assert mm(adj(U),U)==I
        for T in (L,G,N):assert mm(U,T)==mm(T,U)
        assert mm(U,N)==N
        for g in generators:
            gp=tuple(g[p[i]] for i in range(4));assert mm(actions[g],U)==actions[gp]
    checks=['source_reconstruction_and_full_generated_rotation_action']

    # Corner frames and the source cycle are reconstructed from actual triangles.
    rows={''.join(r['outer_arrow']):r for r in report['triangles_and_transports']}
    A=mzero(36,36);H=mzero(36,36);local_frames={}
    for t in range(12):
        edge=ports[3*t][0];triangle=rows[edge]['triangle'];face=triangle[0].split('_')[1:]
        centre=tuple(sum(points[v][i] for v in face)/3 for i in range(3))
        X=transpose([centre,points[triangle[1]],points[triangle[2]]]);Xi=inv(X)
        At=qmm(qmm(X,SLOT_CYCLE),Xi);Ht=qmm(transpose(Xi),Xi)
        local_frames[edge]={'X':[[str(x) for x in r] for r in X], 'A':[[str(x) for x in r] for r in At]}
        for i in range(3):
            for j in range(3):A[3*t+i][3*t+j]=(At[i][j],F(0));H[3*t+i][3*t+j]=(Ht[i][j],F(0))
    A2=mm(A,A);assert mm(A2,A)==I and A!=I and A2!=I
    for U in actions.values():assert mm(A,U)==mm(U,A)
    omega=(F(-1,2),F(1,2));omegaL=[[mul(omega,z) for z in r] for r in L]
    assert mm(A,L)==omegaL
    checks.append('source_slot_cycle_order_covariance_and_selected_eigenline')

    # One fixed address (AB,x), all source rotations, all genuine native prefix
    # readings; the alignment stage supplies N x, not G x.
    anchor=ports.index(('AB','x'));mate=ports.index(('AB','y'))
    raw_rows=[U[anchor] for U in actions.values()]
    local_rows=[mm(L,U)[anchor] for U in actions.values()]
    collective_rows=[mm(N,U)[anchor] for U in actions.values()]
    O=raw_rows+local_rows+collective_rows
    assert rank(raw_rows)==12 and rank(O)==24
    two_axis=O+[U[mate] for U in actions.values()]+[mm(L,U)[mate] for U in actions.values()]
    assert rank(two_axis)==36
    kernels=nullspace(O);assert len(kernels)==12
    checks.append('one_probe_rank_24_two_axes_rank_36_and_complete_hidden_basis')

    # Repeat returns and reversible phase controls built only from L do not
    # escape span of the raw/local rows. Test a nontrivial exact phase control.
    phase=[[sub(I[i][j],L[i][j]) for j in range(36)] for i in range(36)]
    phase=[[ (phase[i][j][0]+omegaL[i][j][0],phase[i][j][1]+omegaL[i][j][1]) for j in range(36)] for i in range(36)]
    assert mm(adj(phase),phase)==I
    phase_rows=[mm(phase,U)[anchor] for U in actions.values()]
    assert rank(O+phase_rows)==24 and mm(L,N)==mm(G,N)==mm(N,N)==N
    checks.append('native_return_and_local_selection_phase_controls_add_no_rank')

    # Raw-coordinate readings under the commuting source actions U A^k.
    extended=[];reading_labels=[]
    for p,U in actions.items():
        for k,T in enumerate((I,A,A2)):
            extended.append(mm(U,T)[anchor]);reading_labels.append({'permutation':list(p),'generator_word':words[p],'slot_power':k})
    assert rank(extended)==36
    D=inverse(extended);assert mm(D,extended)==I
    mixed=raw_rows+local_rows+[mm(U,A)[anchor] for U in actions.values()]
    mixed_rank=rank(mixed)
    # Preserve all local 3x3 observer certificates: they imply the same result
    # for each of the 36 choices of fixed coordinate address by source covariance.
    local_observer_checks=[]
    for t in range(12):
        for a in range(3):
            j=3*t+a;Q=[[T[j][3*t+i] for i in range(3)] for T in (I,A,A2)]
            assert rank(Q)==3 and mm(inverse(Q),Q)==eye(3)
            local_observer_checks.append({'address':list(ports[j]),'observation':sparse(Q),'inverse':sparse(inverse(Q))})
    w=kernels[0];assert mv(O,w)==[ZERO]*len(O)
    values=mv(extended,w);separating=next(i for i,z in enumerate(values) if z!=ZERO)
    assert reading_labels[separating]['slot_power']!=0
    checks.append('36_reading_inverse_all_basis_vectors_all_local_axes_and_hidden_state_detection')

    # The source cycle is reversible but not native-unitary. Preserve exact
    # witnesses instead of changing the native metric to hide the obstruction.
    native_metric_defect=msub(mm(adj(A),A),I);commutator=msub(mm(A,L),mm(L,A))
    assert rank(native_metric_defect)>0 and rank(commutator)>0
    witness_index=next(i for i in range(36) if norm([r[i] for r in A])!=ONE)
    before=[I[j][witness_index] for j in range(36)];after=mv(A,before)
    assert norm(before)!=norm(after)
    assert mm(mm(adj(A),H),A)==H
    assert mm(H,L)!=mm(adj(L),H)
    # Positive definiteness of H follows from H_t=X_t^-T X_t^-1 with invertible
    # real X_t; it is not inferred from sampled trial norms.
    checks.append('native_nonunitarity_positive_corner_metric_and_projector_incompatibility')

    # Independent rational arithmetic backend on the full saved observations.
    assert qrank(realify(sparse(O)))==48
    assert qrank(realify(sparse(extended)))==72
    assert qmultiply(realify(sparse(D)),realify(sparse(extended)))==realify(sparse(I))
    checks.append('independent_rational_ranks_and_full_decoder_identity')

    files=[contract_path,source_path,baseline_path,Path(__file__),Path(__file__).with_name('check_proton_native_task_catalogue.py'),Path(__file__).with_name('verify_proton_native_task_catalogue.py')]
    result={'schema':'marici.voevodsky.single-probe-cycle-result.v1','status':'passed','verification_passed':True,
      'active_obligation':contract['active_obligation'],'checks':[{'name':c,'passed':True} for c in checks],
      'source_hashes':{p.resolve().relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in files},
      'coordinate_addresses':[list(p) for p in ports],'fixed_probe':list(ports[anchor]),'rotation_group_order':12,
      'native_one_probe':{'raw_rank':12,'all_native_stages_rank':24,'hidden_dimension':12,'two_probe_axes_rank':36,
        'nullspace_basis':[vector(v) for v in kernels],'observation':sparse(O)},
      'slot_cycle':{'operator':sparse(A),'local_frames':local_frames,'order':3,'commutes_with_all_geometric_actions':True,
        'geometric_plus_slot_cycle_group_order':36,'relation_to_L':'A L = omega L, but L A != omega L'},
      'extended_observation':{'labels':reading_labels,'matrix':sparse(extended),'inverse':sparse(D),'rank':36,
        'minimum_independent_scalar_complex_readings':36,'local_axis_certificates':local_observer_checks,
        'rank_of_raw_plus_local_plus_one_slot_power':mixed_rank},
      'counterexample':{'native_invisible_vector':vector(w),'separating_reading':reading_labels[separating],
        'separating_value':vector([values[separating]])},
      'metric_audit':{'native_unitarity_defect_rank':rank(native_metric_defect),'commutator_with_L_rank':rank(commutator),
        'norm_witness_address':list(ports[witness_index]),'norm_before':vector([norm(before)]),'norm_after':vector([norm(after)]),
        'corner_metric':sparse(H),'cycle_is_corner_metric_unitary':True,'L_is_corner_metric_self_adjoint':False,
        'any_common_positive_metric_obstruction':'An M-unitary A preserving im L commutes with its M-orthogonal projector L. The nonzero commutator rules out simultaneously making this A unitary and retaining the existing L as an orthogonal projector in any positive metric.'},
      'physical_access_derived':False,'shared_sources_or_stores_modified':False,'scope':contract['scope']}
    dest=ROOT/'research/voevodsky/results/proton-single-probe-cycle-v1.json';dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'one_probe_native_rank':24,'extended_rank':36,'mixed_rank':mixed_rank,
      'norm_witness':result['metric_audit']['norm_witness_address'],'norm_before':result['metric_audit']['norm_before'],
      'norm_after':result['metric_audit']['norm_after'],'commutator_rank':rank(commutator)},indent=2))

if __name__=='__main__':main()
