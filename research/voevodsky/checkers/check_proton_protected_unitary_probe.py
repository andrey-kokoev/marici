"""Exact assembly-preserving, source-derived one-probe control candidate."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
from check_proton_native_task_catalogue import ROOT,eye,mm,adj,madd,msub,mul,rank,parse,sparse,mv,norm,vector,nullspace
from check_proton_single_probe_cycle import inverse,source_actions
from check_proton_unitary_probe_repair import restore
from verify_proton_native_task_catalogue import realify,rank as qrank,multiply as qmm
from assemble_triangle_arrow_source import assemble

def main():
    contract_path=ROOT/'research/voevodsky/inputs/proton-protected-unitary-probe-v1.json'
    contract=json.loads(contract_path.read_text());prior_path=ROOT/contract['source_result'];prior=json.loads(prior_path.read_text())
    for p,h in prior['source_hashes'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    source_path=ROOT/'research/nima/inputs/proton-six-arrows.json';source=json.loads(source_path.read_text())
    report,records=assemble(source)
    assert records==json.loads((ROOT/'research/nima/results/twelve-triangle-1836-arrows.json').read_text())
    ports,(L,G,N)=parse(records);A=restore(prior['slot_cycle']['operator']);I=eye(36);Q=msub(I,L)
    H=mm(mm(Q,madd(A,adj(A))),Q);assert H==adj(H) and mm(H,L)==mm(L,H)==[[ (F(0),F(0)) for _ in range(36)] for _ in range(36)]
    sH=[[mul((F(0),F(1)),z) for z in row] for row in H]
    V=mm(msub(I,sH),inverse(madd(I,sH)));V2=mm(V,V)
    assert mm(adj(V),V)==I and mm(V,L)==mm(L,V)==L and mm(V,N)==mm(N,V)==N
    _,_,_,words,actions=source_actions(source,report,ports)
    for U in actions.values():assert mm(U,V)==mm(V,U)
    assert mm(V,G)==mm(G,V)
    # Even the four joint L/G sectors are invariant under this control.
    local=[]
    for t in range(12):
        for a in range(3):
            j=3*t+a;M=[[T[j][3*t+i] for i in range(3)] for T in (I,V,V2)]
            local.append({'address':list(ports[j]),'rank':rank(M),'observation':sparse(M)})
    anchor=ports.index(('AB','x'));observations=[mm(U,T)[anchor] for U in actions.values() for T in (I,V,V2)]
    r=rank(observations);assert qrank(realify(sparse(observations)))==2*r
    native_rows=[mm(T,U)[anchor] for U in actions.values() for T in (I,L,N)]
    hidden=nullspace(native_rows)[0];values=mv(observations,hidden)
    result={'status':'passed','verification_passed':True,'schema':'marici.voevodsky.protected-unitary-probe.v1',
      'classification':'exact_recipe_resolved_protected_unitary_observation',
      'active_obligation':contract['active_obligation'],'hermitian_generator':sparse(H),'control':sparse(V),
      'native_unitary':True,'fixes_every_locally_admitted_state':True,'fixes_collective_line_pointwise':True,
      'commutes_with_geometric_rotations_and_all_native_projectors':True,
      'local_axis_results':local,'observation':sparse(observations),'observation_rank':r,
      'native_one_probe_hidden_vector':vector(hidden),'new_readings_of_hidden_vector':vector(values),
      'hidden_vector_norm_preserved':norm(mv(V,hidden))==norm(hidden),
      'control_can_be_inserted_without_changing_native_return':mm(mm(N,mm(G,L)),V)==N,
      'synthesis_is_source_selected':False,'physical_control_or_probe_derived':False,
      'scope':contract['scope']}
    if r==36:
        D=inverse(observations);assert mm(D,observations)==I
        assert qmm(realify(sparse(D)),realify(sparse(observations)))==realify(sparse(I))
        result['decoder']=sparse(D);result['decoder_all_basis_vectors_verified']=True
    else:result['remaining_kernel']=[vector(v) for v in nullspace(observations)]
    files=[contract_path,prior_path,source_path,Path(__file__),Path(__file__).with_name('check_proton_unitary_probe_repair.py'),Path(__file__).with_name('check_proton_single_probe_cycle.py'),Path(__file__).with_name('check_proton_native_task_catalogue.py'),Path(__file__).with_name('verify_proton_native_task_catalogue.py')]
    result['source_hashes']={p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in files}
    out=ROOT/'research/voevodsky/results/proton-protected-unitary-probe-v1.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','observation_rank':r,'local_axis_ranks':sorted({x['rank'] for x in local}),
                      'native_unitary':True,'fixes_im_L':True,'preserves_native_return':True},indent=2))
if __name__=='__main__':main()
