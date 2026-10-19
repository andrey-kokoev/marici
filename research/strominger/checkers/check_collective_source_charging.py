"""Collective extension of source charging: exact bounds before reference readout."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from check_source_gauss_operator_charging import response,read,digest,positive_definite
from check_pentachoron_spin_interfaces import A,CI,S3,mm,adj,scale,add
from check_typed_spin_channels import eye


def occupations(n,m):
    if n==1:
        yield (m,);return
    for k in range(m+1):
        for tail in occupations(n-1,m-k):yield (k,)+tail

def quadratic(C,x):return sum(x[i]*C[i][j]*x[j] for i in range(len(x)) for j in range(len(x)))
def moments(C,rho,M):
    diagonal=sum(rho[i]*C[i][i] for i in range(len(rho)))
    pair=quadratic(C,rho)
    return M*diagonal+M*(M-1)*pair

def main():
    specpath=ROOT/'research/strominger/contracts/collective-source-charging.json';spec=json.loads(specpath.read_text())
    beta,eta=F(spec['beta_fixture']),F(spec['eta_fixture'])
    prior_spec=read(spec['held_out_contract'])
    for p,h in prior_spec['source_hashes'].items():assert digest(p)==h,p
    source=read(spec['source_data'][0])['carriers'];contacts=read(spec['source_data'][1])['carriers'];data={};checks={}
    for name,row in source.items():
        weights=list(map(F,row['metric_weights']));edges=[(i,j,F(w)) for i,j,w in row['edges']];ports=contacts[name]['covered_triangles']
        C=response(len(weights),edges,ports);rho=[w/sum(weights) for w in weights]
        # Orthonormal kinetic zero vector has components sqrt(metric weight).
        assert row['exact_zero_field_intertwining'] and all(w>0 for _,_,w in edges)
        assert positive_definite(C)
        data[name]={'C':C,'rho':rho,'ports':len(ports),'dimension':len(weights)}
    ec=response(4,[(i,j,F(1)) for i in range(4) for j in range(i+1,4)],list(range(4)))
    q=scale(CI/S3,tuple(tuple(A(x) for x in row) for row in ((0,1,1,1),(-1,0,1,-1),(-1,-1,0,1),(-1,1,-1,0))))
    P=scale(A(F(1,2)),add(eye(4),q));K=add(eye(4),scale(A(-1),q))
    assert mm(P,P)==P and mm(K,P)==scale(A(0),eye(4))
    # Normalized first column of P: squared amplitudes = |P_i0|²/P_00.
    rho=[]
    for i in range(4):
        value=P[i][0]*P[i][0].flip(8)/P[0][0]
        assert all(x==0 for x in value.c[1:]);rho.append(value.c[0])
    assert rho==[F(1,2),F(1,6),F(1,6),F(1,6)]
    data['elementary']={'C':ec,'rho':rho,'ports':4,'dimension':4}
    pc=data['proton']['C'];prho=data['proton']['rho']
    assert all(x==F(1,12) for x in prho)
    assert all(sum(row)==1 for row in pc)
    assert {pc[i][i] for i in range(12)}=={F(29,105)}
    assert quadratic(pc,prho)==F(1,12)
    assert quadratic(ec,rho)==F(4,15)
    # Check sharp occupation Gauss energies and the condensate variance
    # using explicit two-particle multinomial probabilities, all three graphs.
    for name,row in data.items():
        C,rho=row['C'],row['rho'];n=len(rho);expect=F(0)
        for occ in occupations(n,2):
            probability=F(2)
            for r,k in zip(rho,occ):
                probability*=r**k
                if k==2:probability/=2
            energy=quadratic(C,occ)
            assert energy>=F(4,row['ports'])
            expect+=probability*energy
        assert expect==moments(C,rho,2)
        checks[name+'_two_particle_quantum_variance']=True
    # Electron sharp minimum of sum n_i² at occupation M uses balanced ints.
    def electron_min(M):
        a,r=divmod(M,4);s=4*a*a+r*(2*a+1)
        return F(M*M+s,5)
    for M in range(1,13):
        assert min(quadratic(ec,x) for x in occupations(4,M))==electron_min(M)
    checks['balanced_integer_bound_verified']=True
    def proton_trial(M):return F(M*M,12)+F(27*M,140)
    assert proton_trial(1)==F(29,105)
    # For M>=2, electron_min>=M²/4 and the gap is
    # M²/4 - proton_trial(M) = M(70M-81)/420 > 0.
    assert F(1,4)-F(1,12)==F(1,6) and F(27,140)==F(81,420) and 2*70>81
    assert proton_trial(1)<electron_min(1)
    checks['same_M_all_positive_coefficients_ordering_proved']=True
    bounds={}
    for name,row in data.items():
        M=row['dimension'];low=electric_low=F(M*M,row['ports'])
        if name=='elementary':electric_low=electron_min(M)
        electric_high=moments(row['C'],row['rho'],M)
        low=beta*electric_low/2+eta*M*M/2;high=beta*electric_high/2+eta*M*M/2
        assert low<=high
        bounds[name]={'occupation':M,'electric_quadratic_lower':str(electric_low),'electric_quadratic_trial':str(electric_high),
                      'ground_energy_lower':str(low),'ground_energy_upper':str(high)}
    # Source-size occupations: even the proton variational upper bound /
    # electron lower bound is at most 9 for every common beta>0, eta>=0.
    electric_ratio=proton_trial(12)/electron_min(4)
    number_ratio=F(12**2,4**2);family_upper=max(electric_ratio,number_ratio)
    assert electric_ratio==F(501,140) and family_upper==9
    # Held-out reference opens only after the construction and family bound.
    ref=prior_spec['held_out_reference'];assert digest(ref['path'])==ref['sha256']
    inputs=read(ref['path'])['inputs'];target=F(inputs['proton_me'])
    assert target>family_upper
    checks['source_size_occupations_fail_joint_mass_test']=True
    report={'status':'passed','disposition':'Collective occupation does not repair this charging branch for equal occupations or source-size occupations.',
            'checks':checks,'same_occupation_theorem':{'domain':'Every integer M>=1, beta>0, eta>=0, symmetric occupation extension of retained K and C',
                'proton_electric_trial':'M^2/12 + 27M/140','elementary_electric_lower':'(M^2+min_{sum n=M} sum n_i^2)/5',
                'result':'E_proton(M) < E_elementary(M); equal eta*M^2/2 cancels',
                'proof_M_ge_2':'M^2/4 - (M^2/12+27M/140) = M(70M-81)/420 > 0',
                'proof_M_1':'29/105 < 2/5'},
            'source_dimension_occupation_bounds':bounds,'source_dimension_proton_ratio_upper_all_coefficients':str(family_upper),
            'held_out_proton_ratio':str(target),'coefficient_fit':False,
            'next_obligation':'Unequal collective occupations or a different kinetic/charging/boundary interaction must be sourced, with charge and statistics retained. Do not choose occupation numbers from the desired ratio.'}
    paths=[specpath,Path(__file__).resolve(),ROOT/spec['held_out_contract'],ROOT/ref['path'],ROOT/'research/voevodsky/checkers/check_source_gauss_operator_charging.py',ROOT/'research/voevodsky/checkers/check_open_flux_common_vacuum.py',ROOT/'research/voevodsky/checkers/check_belt_interface_response.py',ROOT/'research/voevodsky/checkers/check_pentachoron_spin_interfaces.py',ROOT/'research/voevodsky/checkers/check_typed_spin_channels.py']+[ROOT/p for p in spec['source_data']]
    report['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    dest=ROOT/'research/strominger/results/collective-source-charging.json';dest.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='source_hashes'},indent=2))

if __name__=='__main__':main()
