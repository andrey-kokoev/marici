"""Exact source-graph operator-square charging; benchmarks enter only after construction."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
from check_open_flux_common_vacuum import grounded_laplacian,flux_certificate
from check_belt_interface_response import inverse
from check_pentachoron_spin_interfaces import A,CI,S3,mm,adj,scale,add
from check_typed_spin_channels import eye,trace

ROOT=Path(__file__).resolve().parents[3]
BASE='research/voevodsky/'
SPEC=BASE+'contracts/source-gauss-operator-charging.v1.json'
OUT=BASE+'results/source_gauss_operator_charging.v1.json'

def read(p):return json.loads((ROOT/p).read_text())
def digest(p):return sha256((ROOT/p).read_bytes()).hexdigest()
def response(count,edges,ports):
    L=grounded_laplacian(count,edges,ports);C=inverse(L)
    assert all(sum(L[i][k]*C[k][j] for k in range(count))==int(i==j) for i in range(count) for j in range(count))
    # Every sharp occupation has its own retained gradient field/exterior flux.
    columns=[]
    for i in range(count):
        rho=[F(int(k==i)) for k in range(count)];phi=[C[k][i] for k in range(count)]
        assert flux_certificate(count,edges,ports,rho,phi)==C[i][i]/2
        columns.append([phi[b]-phi[a] for a,b,_ in edges]+[phi[a] for a in ports])
    assert all(sum(x*y for x,y in zip(columns[i],columns[j]))==C[i][j] for i in range(count) for j in range(count))
    return C

def positive_definite(matrix):
    """Exact rational LDL test of a real symmetric form."""
    n=len(matrix);d=[];lower=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        pivot=matrix[i][i]-sum(lower[i][k]**2*d[k] for k in range(i))
        if pivot<=0:return False
        d.append(pivot);lower[i][i]=1
        for j in range(i+1,n):lower[j][i]=(matrix[j][i]-sum(lower[j][k]*lower[i][k]*d[k] for k in range(i)))/pivot
    return True

def ground_bounds(K,metric,diagonal,steps=80):
    # K is a positive weighted graph Laplacian. Constant coefficients are its
    # exact kernel, giving a Rayleigh upper bound without any orbit collapse.
    lo=min(diagonal);hi=sum(n*v for n,v in zip(metric,diagonal))/sum(metric)
    for _ in range(steps):
        mid=(lo+hi)/2
        form=[[metric[i]*K[i][j]+(metric[i]*(diagonal[i]-mid) if i==j else 0) for j in range(len(metric))] for i in range(len(metric))]
        if positive_definite(form):lo=mid
        else:hi=mid
    return lo,hi

def construct(beta,eta):
    """No empirical reference is read here."""
    assert beta>0 and eta>=0
    source=read(BASE+'results/weighted_matter_link_adapter.json')['carriers']
    contacts=read(BASE+'results/all_face_contact.json')['carriers'];data={}
    for name,row in source.items():
        assert row['exact_zero_field_intertwining']
        n=list(map(F,row['metric_weights']));edges=[(i,j,F(w)) for i,j,w in row['edges']]
        assert all(w>0 for _,_,w in edges)
        ports=contacts[name]['covered_triangles'];C=response(len(n),edges,ports)
        # Connected positive weighted graph => K>=0 with a simple constant
        # coefficient kernel; M^1/2 transports it to an orthonormal carrier.
        reached={0}
        while True:
            nxt=reached|{j for i,j,_ in edges if i in reached}|{i for i,j,_ in edges if j in reached}
            if nxt==reached:break
            reached=nxt
        assert len(reached)==len(n)
        K=[[F(0) for _ in n] for _ in n]
        for i,j,w in edges:
            K[i][i]+=w/n[i];K[i][j]-=w/n[i];K[j][j]+=w/n[j];K[j][i]-=w/n[j]
        assert all(sum(row)==0 for row in K)
        assert all(n[i]*K[i][j]==n[j]*K[j][i] for i in range(len(n)) for j in range(len(n)))
        data[name]=(n,edges,ports,C,K)
    pn,pe,pp,pc,pk=data['proton'];bn,be,bp,bc,bk=data['belt']
    assert len(pn)==12 and set(pp)==set(range(12)) and len(bn)==18
    pd={pc[i][i] for i in range(12)};assert len(pd)==1;cp=pd.pop()
    # Since Lp=I+Lint >=I, its inverse has cp<=1. Verify the exact diagonal too.
    assert 0<cp<=1
    Ep=beta*cp/2+eta/2
    e_edges=[(i,j,F(1)) for i in range(4) for j in range(i+1,4)]
    ec=response(4,e_edges,list(range(4)))
    assert all(ec[i][j]==F(1+int(i==j),5) for i in range(4) for j in range(4))
    q=scale(CI/S3,tuple(tuple(A(x) for x in row) for row in ((0,1,1,1),(-1,0,1,-1),(-1,-1,0,1),(-1,1,-1,0))))
    assert adj(q)==q and mm(q,q)==eye(4) and trace(q)==0
    # K_e=I-Q has eigenvalues 0,2, each twice; charging diagonal is scalar.
    Ee=beta*F(1,5)+eta/2
    bd=[bc[i][i] for i in range(18)]
    blo,bhi=ground_bounds(bk,bn,[beta*d/2+eta/2 for d in bd])
    assert 0<blo<=bhi and bhi-blo<F(1,10**23)
    rho=[F(1,4)]*4
    classical_e=sum(rho[i]*ec[i][j]*rho[j] for i in range(4) for j in range(4))
    quantum_e=sum(rho[i]*ec[i][i] for i in range(4))
    assert classical_e==F(1,4) and quantum_e==F(2,5)
    assert beta*(quantum_e-classical_e)/2==3*beta/40
    return {'proton_capacitance_diagonal':str(cp),'belt_capacitance_diagonals':list(map(str,bd)),'belt_distinct_diagonal_count':len(set(bd)),'belt_ground_certificate':'full 18-mode weighted rational LDL bisection; no two-density projection',
        'elementary_capacitance_diagonal':'2/5','proton_energy':str(Ep),'elementary_energy':str(Ee),'belt_energy_interval':[str(blo),str(bhi)],
        'proton_per_elementary':str(Ep/Ee),'belt_minus_proton_per_elementary_interval':[str((blo-Ep)/Ee),str((bhi-Ep)/Ee)],
        'classical_elementary_electric_coefficient':'1/8','quantum_elementary_electric_coefficient':'1/5','charge_variance_energy_difference':str(3*beta/40),
        'all_common_coefficients_ratio_upper_bound':str(max(F(1),cp/F(2,5))),
        'coarse_architecture_ratio_upper_bound':'5/2','joint_matter_dimension_including_empty':35}

def main():
    spec=read(SPEC)
    assert spec['beta']=='3/5' and spec['eta']=='1/5' and spec['empty_energy']=='0 in the same direct-sum system'
    for p,h in spec['source_hashes'].items():assert digest(p)==h,p
    beta,eta=F(spec['beta']),F(spec['eta'])
    candidate=construct(beta,eta)
    # Only now open the pinned independent reference. No reference sets a model coefficient.
    ref=spec['held_out_reference'];assert digest(ref['path'])==ref['sha256']
    inputs=read(ref['path'])['inputs'];rp=F(inputs['proton_me']);split=F(inputs['neutron_me'])-rp
    got=F(candidate['proton_per_elementary']);lo,hi=map(F,candidate['belt_minus_proton_per_elementary_interval'])
    bound=F(candidate['all_common_coefficients_ratio_upper_bound'])
    assert got<=bound<=F(5,2)<rp and not lo<=split<=hi
    sources={p:digest(p) for p in list(spec['source_hashes'])+[SPEC,ref['path'],BASE+'checkers/check_source_gauss_operator_charging.py',BASE+'checkers/check_open_flux_common_vacuum.py',BASE+'checkers/check_belt_interface_response.py',BASE+'checkers/check_pentachoron_spin_interfaces.py',BASE+'checkers/check_typed_spin_channels.py']}
    result={'schema':'marici.voevodsky.source-gauss-operator-charging-result.v1','verification_passed':True,
        'candidate_mass_conjecture':'refuted_within_declared_reduced_electrostatic_branch','physical_admission':False,'parameters_fitted_back_into_model':False,
        'constructor':candidate,'held_out':{'proton_per_elementary':str(rp),'splitting_per_elementary':str(split),'joint_match':False},
        'all_common_coefficients_no_go':{'domain':'beta>0, eta>=0, frozen graphs and one-occupation operator-square charging, no offsets or extra mediator',
            'identity':'Ep/Ee=(beta*cp+eta)/(2*beta/5+eta); weighted mean of (5*cp/2) and 1',
            'upper_bound':str(bound),'simultaneous_match_possible':False},
        'checks':{'sharp_occupation_Gauss':True,'full_exterior_flux_and_energy':True,'response_Gram_equals_inverse_laplacian':True,'weighted_source_K_preserved':True,'positive_ground_sector_certificates':True,'classical_quantum_variance_not_erased':True,'benchmarks_loaded_after_construction':True,'both_ratios_tested':True},
        'remaining_source_gap':'No independently sourced collective occupation/capacitance hierarchy with a sharp charge sector and retained full-native quantum parent. Do not fit species offsets to rescue this excluded branch.',
        'source_hashes':sources}
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'verification_passed':True,'disposition':result['candidate_mass_conjecture'],'proton_ratio':float(got),'splitting_interval':[float(lo),float(hi)],'ratio_upper_bound_all_common_coefficients':str(bound)},indent=2))

if __name__=='__main__':main()
