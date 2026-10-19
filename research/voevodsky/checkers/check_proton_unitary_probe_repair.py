"""Preregistered Hermitian/Cayley control recipes, exact native metric audit."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
from check_proton_native_task_catalogue import ROOT,ONE,ZERO,eye,mzero,mm,mv,adj,madd,msub,mul,rank,parse,sparse,vector,norm
from check_proton_single_probe_cycle import inverse,source_actions
from verify_proton_native_task_catalogue import realify,rank as qrank,multiply as qmm
from assemble_triangle_arrow_source import assemble

def restore(packet):
    a=mzero(*packet['shape'])
    for i,j,x,y in packet['entries']:a[i][j]=(F(x),F(y))
    return a

def main():
    contract_path=ROOT/'research/voevodsky/inputs/proton-unitary-probe-repair-v1.json'
    contract=json.loads(contract_path.read_text());prior_path=ROOT/contract['source_result'];prior=json.loads(prior_path.read_text())
    for p,h in prior['source_hashes'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    source_path=ROOT/'research/nima/inputs/proton-six-arrows.json'
    source=json.loads(source_path.read_text());report,records=assemble(source)
    assert records==json.loads((ROOT/'research/nima/results/twelve-triangle-1836-arrows.json').read_text())
    ports,(L,G,N)=parse(records);A=restore(prior['slot_cycle']['operator']);I=eye(36)
    _,_,_,words,actions=source_actions(source,report,ports)
    anchor=ports.index(('AB','x'));b=[row[0] for row in N]
    recipes={'symmetric_cycle':madd(A,adj(A)), 'cycle_gram':mm(adj(A),A)}
    results={}
    for name,H in recipes.items():
        assert H==adj(H)
        sH=[[mul((F(0),F(1)),z) for z in r] for r in H]
        V=mm(msub(I,sH),inverse(madd(I,sH)));V2=mm(V,V)
        assert mm(adj(V),V)==I
        for U in actions.values():assert mm(U,V)==mm(V,U)
        local=[]
        for t in range(12):
            for a in range(3):
                j=3*t+a;Q=[[T[j][3*t+k] for k in range(3)] for T in (I,V,V2)]
                local.append({'address':list(ports[j]),'rank':rank(Q)})
        readings=[mm(U,T)[anchor] for U in actions.values() for T in (I,V,V2)]
        r=rank(readings);assert qrank(realify(sparse(readings)))==2*r
        entry={'hermitian_generator':sparse(H),'unitary_control':sparse(V),'local_axis_ranks':local,
               'observation_rank':r,'hidden_dimension':36-r,'observation':sparse(readings),
               'commutator_L_rank':rank(msub(mm(V,L),mm(L,V))),
               'commutator_N_rank':rank(msub(mm(V,N),mm(N,V))),
               'collective_input_norm':vector([norm(b)]),'collective_output_norm':vector([norm(mv(V,b))]),
               'collective_offline_component':vector(mv(msub(I,N),mv(V,b)))}
        assert norm(mv(V,b))==norm(b)
        if r==36:
            D=inverse(readings);assert mm(D,readings)==I
            assert qmm(realify(sparse(D)),realify(sparse(readings)))==realify(sparse(I))
            entry['decoder']=sparse(D)
        results[name]=entry
    # No target rank is asserted for either recipe: failed conjecture branches
    # remain in the result, while exact algebraic control identities are checked.
    files=[contract_path,prior_path,source_path,Path(__file__),Path(__file__).with_name('check_proton_native_task_catalogue.py'),Path(__file__).with_name('check_proton_single_probe_cycle.py'),Path(__file__).with_name('verify_proton_native_task_catalogue.py')]
    result={'status':'passed','verification_passed':True,'schema':'marici.voevodsky.unitary-probe-repair.v1',
            'active_obligation':contract['active_obligation'],'recipes':results,
            'classification':'recipe_resolved_exact_observation_and_native_metric_audit',
            'source_selected_synthesis':False,'physical_gate_derived':False,'scope':contract['scope'],
            'source_hashes':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in files}}
    out=ROOT/'research/voevodsky/results/proton-unitary-probe-repair-v1.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({name:{k:r[k] for k in ('observation_rank','hidden_dimension','commutator_L_rank','commutator_N_rank')} for name,r in results.items()},indent=2))
if __name__=='__main__':main()
