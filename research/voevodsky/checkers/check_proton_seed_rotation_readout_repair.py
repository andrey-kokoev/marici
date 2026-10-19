"""Source-derived geometric probe extension; no new interaction coefficients."""
from pathlib import Path
from collections import deque
from fractions import Fraction as F
from hashlib import sha256
import json
from check_proton_native_task_catalogue import ROOT,ZERO,ONE,eye,mzero,mm,mv,adj,rank,rref,parse,sparse,vector
from verify_proton_native_task_catalogue import realify,rank as rational_rank,multiply as rational_multiply
from assemble_triangle_arrow_source import assemble
from check_triangle_half_phase import mm as qmm,transpose
from check_twelve_triangle_positive_geometry import inv

def zvector(v):return [(F(a),F(b)) for a,b in v]
def from_sparse(p):
    a=mzero(*p['shape'])
    for i,j,x,y in p['entries']:a[i][j]=(F(x),F(y))
    return a

def inverse(a):
    n=len(a);rows,pivots=rref([row+identity for row,identity in zip(a,eye(n))])
    assert pivots[:n]==list(range(n))
    return [row[n:] for row in rows]

def main():
    contract_path=ROOT/'research/voevodsky/inputs/proton-seed-rotation-readout-repair-v1.json'
    contract=json.loads(contract_path.read_text());source_path=ROOT/contract['source'];baseline_path=ROOT/contract['baseline']
    baseline=json.loads(baseline_path.read_text())
    for name,h in baseline['source_hashes'].items():assert sha256((ROOT/name).read_bytes()).hexdigest()==h
    source=json.loads(source_path.read_text());report,records=assemble(source)
    assert records==json.loads((ROOT/'research/nima/results/twelve-triangle-1836-arrows.json').read_text())
    ports,(L,G,N)=parse(records);index={p:i for i,p in enumerate(ports)};labels=tuple(source['vertices'])
    generators=[]
    for cycle in report['derived_cycles']:
        mapping=dict(zip(cycle,cycle[1:]+cycle[:1]));generators.append(tuple(labels.index(mapping.get(v,v)) for v in labels))
    unit=tuple(range(4));words={unit:[]};todo=deque([unit])
    while todo:
        p=todo.popleft()
        for j,g in enumerate(generators):
            q=tuple(g[p[i]] for i in range(4))
            if q not in words:words[q]=words[p]+[j];todo.append(q)
    assert len(words)==12
    points={v:tuple(F(x) for x in source['vertices'][v]) for v in labels}
    frame=transpose([points[v] for v in labels[:3]]);frame_inverse=inv(frame)
    actions={}
    for p in words:
        mapping={v:labels[p[i]] for i,v in enumerate(labels)}
        R=qmm(transpose([points[mapping[v]] for v in labels[:3]]),frame_inverse)
        U=mzero(36,36)
        for j,(edge,axis) in enumerate(ports):
            target=''.join(mapping[v] for v in edge)
            for a in range(3):U[index[target,'xyz'[a]]][j]=(R[a]['xyz'.index(axis)],F(0))
        assert mm(adj(U),U)==eye(36)
        assert all(mm(U,A)==mm(A,U) for A in (L,G,N))
        assert mm(U,N)==N
        actions[p]=U
    for p,U in actions.items():
        for j,g in enumerate(generators):
            q=tuple(g[p[i]] for i in range(4))
            assert mm(actions[g],U)==actions[q]
    seed=baseline['seed_face_counterexample'];anchors=seed['observed_addresses'];seed_edges={ports[j][0] for j in anchors}
    all_edges={p[0] for p in ports};complement=all_edges-seed_edges
    candidates=[]
    for p,word in words.items():
        mapping={v:labels[p[i]] for i,v in enumerate(labels)}
        if {''.join(mapping[v] for v in e) for e in seed_edges}==complement:candidates.append(p)
    assert candidates
    chosen=min(candidates,key=lambda p:(len(words[p]),words[p]));U=actions[chosen]
    I=eye(36);O=[A[j] for A in (I,L,N) for j in anchors];OU=mm(O,U)
    B=from_sparse(baseline['local_mode_encoder'])
    assert rank(O)==19 and rank(O+OU)==36
    assert rank(mm(O,B))==7 and rank(mm(O+OU,B))==12
    x,y,b=map(zvector,(seed['input_x'],seed['input_y'],seed['collective_vector']))
    assert mv(O,x)==mv(O,y) and mv(OU,x)!=mv(OU,y)
    # Retain only six local-mode seed readings and one collective reading,
    # then select exactly five independent rows of the rotated raw seed probe.
    seed_triangles=sorted({j//3 for j in anchors})
    base_rows=[I[3*t] for t in seed_triangles]+[N[anchors[0]]]
    comparison=mm(base_rows,B);assert rank(comparison)==7
    selected=[];chosen_rows=list(base_rows)
    for j in anchors:
        candidate=U[j]
        trial=mm(chosen_rows+[candidate],B)
        if rank(trial)>len(chosen_rows):
            chosen_rows.append(candidate);selected.append(j)
    assert len(selected)==5 and len(chosen_rows)==12
    M=mm(chosen_rows,B);D=inverse(M)
    assert mm(D,M)==eye(12)
    # These controls disallow passive-coordinate and post-return explanations.
    assert mm(mm(O,adj(U)),U)==O
    assert mm(OU,N)==mm(O,N)
    assert mv(mm(OU,N),x)==mv(mm(OU,N),y)
    separating=[j for j in anchors if mv([U[j]],x)!=mv([U[j]],y)]
    assert separating
    # Independent arithmetic backend: realify to rational matrices, and check
    # both ranks and the complete local-amplitude decoder without field helpers.
    assert rational_rank(realify(sparse(O+OU)))==72
    assert rational_rank(realify(sparse(mm(O+OU,B))))==24
    assert rational_multiply(realify(sparse(D)),realify(sparse(M)))==realify(sparse(eye(12)))
    files=[contract_path,source_path,baseline_path,Path(__file__),Path(__file__).with_name('check_proton_native_task_catalogue.py'),Path(__file__).with_name('verify_proton_native_task_catalogue.py')]
    result={'schema':'marici.voevodsky.seed-rotation-readout-repair-result.v1','status':'passed','verification_passed':True,
       'active_obligation':contract['active_obligation'],'extended_readout_grammar':contract['extended_readout_grammar'],
       'source_cycles':report['derived_cycles'],'group_order':12,
       'selected_vertex_permutation':{v:labels[chosen[i]] for i,v in enumerate(labels)},
       'source_generator_word_in_application_order':[report['derived_cycles'][j] for j in words[chosen]],
       'action':sparse(U),'all_twelve_actions_unitary_and_intertwine_native_maps':True,'all_generator_compositions_verified':True,
       'observer_ranks':{'native_seed':19,'with_rotated_seed':36,'native_seed_on_local_modes':7,'with_rotated_seed_on_local_modes':12},
       'five_additional_reading_addresses':[list(ports[j]) for j in selected],
       'locally_admitted_measurement':sparse(chosen_rows),'local_amplitude_measurement':sparse(M),'local_amplitude_decoder':sparse(D),
       'separating_pair_reading':{'address':list(ports[separating[0]]),'x':vector(mv([U[separating[0]]],x)),'y':vector(mv([U[separating[0]]],y))},
       'minimum_additional_independent_complex_readings_for_local_modes':5,
       'passive_transport_adds_no_information':True,'post_return_rotation_adds_no_information':True,
       'independent_rational_realification_checks_passed':True,'physical_rotation_gate_or_probe_derived':False,
       'source_hashes':{p.resolve().relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in files},
       'shared_sources_or_stores_modified':False}
    output=ROOT/'research/voevodsky/results/proton-seed-rotation-readout-repair-v1.json';output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','source_generator_word_in_application_order','selected_vertex_permutation','observer_ranks','five_additional_reading_addresses','separating_pair_reading')},indent=2))
if __name__=='__main__':main()
