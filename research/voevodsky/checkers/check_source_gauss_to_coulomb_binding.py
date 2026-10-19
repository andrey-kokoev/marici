"""Finite one-bridge Gauss obstruction and external-physics Coulomb ground.
Standard-library exact rational/algebraic arithmetic. Shared inputs read only.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
import json,sys
from check_proton_electron_single_link_potential import ROOT,decode,parse
from check_electron_tetrahedral_spinor import D,G0,gm,gmm,act,adj,ident,sm
from check_projector_fold_sheets import parameters,verify as verify_atlas
from check_spinor_potential_link_bridge import construct,reconstruct,flag
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from assemble_endpoint_charging import geometry,quadratic,matmul,inverse


def effective(R,a,b):return R[a][a]+R[b][b]-2*R[a][b]
def weighted_graph(count,edges):
    L=[[F(0) for _ in range(count)] for _ in range(count)]
    for a,b,w in edges:
        L[a][a]+=w;L[b][b]+=w;L[a][b]-=w;L[b][a]-=w
    J=[[F(1,count)]*count for _ in range(count)]
    inv=inverse([[L[i][j]+J[i][j] for j in range(count)] for i in range(count)])
    R=[[inv[i][j]-J[i][j] for j in range(count)] for i in range(count)]
    assert matmul(L,R)==[[F(i==j)-F(1,count) for j in range(count)] for i in range(count)]
    return L,R

def clean(p):return {k:v for k,v in p.items() if v}
def add(p,q):
    out=dict(p)
    for k,v in q.items():out[k]=out.get(k,F(0))+v
    return clean(out)
def scale(p,a):return clean({k:v*a for k,v in p.items()})
def shift(p,k):return {i+k:v for i,v in p.items()}
def derivative(p,b):
    # derivative of sum c_k r^k exp(-b r); integer powers may be negative.
    return add({k-1:v*k for k,v in p.items() if k},scale(p,-b))
def radial_laplacian(p,b):return add(derivative(derivative(p,b),b),scale(shift(derivative(p,b),-1),2))
def exp_integral_power(k,b):
    # Integral0^infty r^k exp(-b r)dr=k!/b^(k+1), b>0.
    assert k>=0 and b>0
    return F(factorial(k))/b**(k+1)


def main():
    base=ROOT/'research/voevodsky';cp=base/'inputs/source-gauss-to-coulomb-binding-v1.json';contract=json.loads(cp.read_text())
    paths={k:ROOT/contract[k] for k in ('charging_contract','charging_receipt','proton','electron','potential','bridge')}
    parent_contract=json.loads(paths['charging_contract'].read_text());parent=json.loads(paths['charging_receipt'].read_text());assert parent['status']=='passed'
    assert parent_contract['charges']['proton']==1 and parent_contract['charges']['electron']==-1
    graphs={}
    for name in ('proton','electron'):
        source=parent['source_operators'][name];count=len(source['metric'])
        graph=geometry(count,source['internal_edges'],source['exterior_ports'])
        assert graph['resistance']==[[F(x) for x in row] for row in source['internal_resistance']]
        graphs[name]=graph
    np,ne=graphs['proton']['dimension'],graphs['electron']['dimension'];assert (np,ne)==(12,4)
    beta=F(parent_contract['beta']);graph_tests=[]
    for a,b in ((0,0),(np-1,ne-1),(4,2)):
        for conductance in (F(1,2),F(1),F(2)):
            edges=[(i,j,F(1)) for i,j in graphs['proton']['edges']]
            edges.extend((np+i,np+j,F(1)) for i,j in graphs['electron']['edges']);edges.append((a,np+b,conductance))
            L,R=weighted_graph(np+ne,edges);energy=[]
            for i in range(np):
                row=[]
                for j in range(ne):
                    rho=[F(0)]*(np+ne);rho[i]=1;rho[np+j]=-1
                    phi=[sum(x*y for x,y in zip(rr,rho)) for rr in R]
                    assert [sum(x*y for x,y in zip(rr,phi)) for rr in L]==rho
                    electric_norm=sum(w*(phi[x]-phi[y])**2 for x,y,w in edges)
                    assert electric_norm==quadratic(R,rho)
                    expected=effective(graphs['proton']['resistance'],i,a)+1/conductance+effective(graphs['electron']['resistance'],b,j)
                    assert electric_norm==expected
                    # Every unit charge crosses the only bridge; its energy
                    # cannot be interpreted as a 3D spreading Coulomb field.
                    assert conductance*(phi[a]-phi[np+b])==1
                    row.append(beta*electric_norm/2)
                energy.append(row)
            for i in range(np):
                for j in range(ne):assert energy[i][j]-energy[i][0]-energy[0][j]+energy[0][0]==0
            graph_tests.append({'attachment':[a,b],'bridge_conductance':str(conductance),
                'neutral_pair_electric_energy':[[str(x) for x in row] for row in energy],
                'all_48_Gauss_sources_verified':True,'mixed_energy_differences_zero':True})
    # Continuum3D Maxwell kernel: outside origin radial Laplacian1/r=0,
    # flux through radius r is -4pi independently of r (stored without pi).
    assert radial_laplacian({-1:F(1)},F(0))=={}
    for r in (F(1,3),F(1),F(7)):
        derivative_kernel=-1/(r*r)
        assert r*r*derivative_kernel==-1
    # Derive COM reduction from the supplied two masses, not native energies.
    continuum=[]
    for mp,me,hbar,kappa in ((F(2),F(1),F(1),F(1)),(F(7),F(3),F(2),F(5)),(F(5),F(2),F(3),F(1,2))):
        mu=mp*me/(mp+me);M=mp+me
        # grad_p=(mp/M)grad_R+grad_r; grad_e=(me/M)grad_R-grad_r.
        assert (mp/M)**2/mp+(me/M)**2/me==1/M
        assert 1/mp+1/me==1/mu and (mp/M)/mp-(me/M)/me==0
        A=hbar*hbar/(2*mu);b=kappa/(2*A);radius=1/b;E0=-A*b*b
        assert E0==-mu*kappa*kappa/(2*hbar*hbar)
        orbital={0:F(1)}
        Hpsi=add(scale(radial_laplacian(orbital,b),-A),scale(shift(orbital,-1),-kappa))
        assert Hpsi==scale(orbital,E0)
        # Cartesian normalization: N²= b³/pi, 4piN² integral r²e^-2br=1.
        assert 4*b**3*exp_integral_power(2,2*b)==1
        inverse_r=4*b**3*exp_integral_power(1,2*b);r_mean=4*b**3*exp_integral_power(3,2*b)
        kinetic=A*b*b;potential=-kappa*inverse_r
        assert inverse_r==b and r_mean==F(3,2)*radius
        assert kinetic+potential==E0 and 2*kinetic+potential==0
        # Ground-state lower bound: expand A||grad psi+b rhat psi||².
        # Cross term after integration by parts is -2Ab/r |psi|²,
        # since divergence(rhat)=2/r. This equals -kappa/r.
        assert 2*A*b==kappa and -A*b*b==E0
        # Exact Schr equation for the stationary ground phase exp(-iE0t/hbar).
        assert hbar*(E0/hbar)==E0
        continuum.append({'external_controls':{'mp':str(mp),'me':str(me),'hbar':str(hbar),'kappa':str(kappa)},
            'mu':str(mu),'A':str(A),'b':str(b),'radius':str(radius),'ground_energy':str(E0),
            'kinetic_expectation':str(kinetic),'potential_expectation':str(potential),
            'mean_radius':str(r_mean),'ground_residual_zero':True,'normalization_and_virial_exact':True})
    # Spin-independent continuation respects the native electron encoder and
    # keeps the entire ground doublet and all existing fold witnesses.
    native_e=json.loads(paths['electron'].read_text());faces=tuple(tuple(tuple(decode(x) for x in row) for row in f) for f in native_e['face_projectors']);E=tuple(row for f in faces for row in f);ell=E[0]
    native_ops={s:[[G0]*8 for _ in range(8)] for s in 'LGN'}
    for arrow in native_e['arrows']:native_ops[arrow['stage']][arrow['target']][arrow['source']]=decode(arrow['weight'])
    for op in native_ops.values():assert gmm(op,E)==E
    assert gmm(adj(E),E)==sm(2,ident(2))
    ports,pops=parse(json.loads(paths['proton'].read_text()))
    pi=ports.index(('AB','x'));pcol=tuple((D(row[pi][0]),D(0,row[pi][1])) for row in pops[2])
    assert any(x!=G0 for x in pcol)
    packet=json.loads(paths['potential'].read_text());verify_atlas(packet)
    p0,normal,recovery=parameters(packet['source']);p=tuple(tuple((D(a),D(0,b)) for a,b in row) for row in p0)
    bridge=json.loads(paths['bridge'].read_text());assert bridge['passed'];host=(D(F(1,3)),)*3;owners=[]
    for w in bridge['interior_witness_for_every_fold']:
        seed=tuple(decode(x) for x in w['seed']);r=construct(seed,host,ell,p)
        assert flag(r['potential'])==tuple(w['owner']) and reconstruct(r,ell,p)==seed
        # Linearity: each nonzero orbital amplitude scales norm/link but not
        # spin ray or mode. Exact controls verify the codec; exp(-r/a)>0 is
        # handled by the analytic orbital proof, not approximated by rationals.
        for amplitude in (F(1,7),F(1,2),F(2)):
            local=tuple(gm((D(amplitude),D()),x) for x in seed);rr=construct(local,host,ell,p)
            assert rr['potential']==r['potential'] and rr['mode']==r['mode'] and reconstruct(rr,ell,p)==local
        owners.append(list(w['owner']))
    assert len({tuple(x) for x in owners})==24
    dark=(tuple(-x for x in ell[1]),ell[0])
    dark_records=[]
    for phase in ((D(1),D()),(D(),D(1)),(D(-1),D()),(D(),D(-1))):
        seed=tuple(gm(phase,x) for x in dark);rr=construct(seed,host,ell,p)
        assert rr['link']==G0
        if dark_records:
            assert rr['potential']==dark_records[0]['potential'] and rr['mode']==dark_records[0]['mode'] and rr['norm_squared']==dark_records[0]['norm_squared']
        dark_records.append(rr)
    assert dark_records[0]['dark_phase_witness']!=dark_records[1]['dark_phase_witness']
    result={'schema':'marici.source-gauss-to-coulomb-binding.v1','passed':True,
      'classification':'finite_source_obstruction_and_externally_supplied_nonrelativistic_Coulomb_ground',
      'source_graph_audit':{'source_graph_dimensions':[np,ne],'selected_graph_kinetics_identified_with_native_spinor':False,
        'electric_bridge_identified_with_coefficient_arrow':False,'tests':graph_tests,'neutral_charge_sources_checked':48*len(graph_tests),
        'bridge_resistance_identity':'R_pair(i,j)=R_p(i,a)+1/w+R_e(b,j)',
        'pair_internal_electric_potential_is_separable':True,'relative_R3_or_Coulomb_kernel_source_selected':False},
      'external_physics':contract['external_physics'],
      'Coulomb':{'Green_kernel':'1/(4pi epsilon r)','interaction':'q_p q_e/(4pi epsilon r)=-kappa/r',
        'self_energies_subtracted':True,'coefficient_assembly_derived_Maxwell_kernel':False,
        'ground_orbital':'(pi a^3)^(-1/2) exp(-r/a)','a':'hbar^2/(mu kappa)',
        'ground_energy':'-mu kappa^2/(2 hbar^2)','reduced_mass':'mp me/(mp+me)',
        'ground_lower_bound':'<psi,(H-E0)psi>=A integral |grad psi+b rhat psi|^2 >=0',
        'ground_spin_degeneracy':2,'binding_for_every_kappa_positive':True,'calibrated_constants_used':False,'controls':continuum},
      'native_retention':{'electron_stage_intertwiners':True,'proton_port_still_a_readout':True,
        'all_24_folds_have_ground_doublet_witnesses':True,'original_single_arrow_dark_phase_resolved_by_Coulomb':False},
      'physical_law_and_scales_derived_from_native_sources':False,'numerical_hydrogen_prediction_from_arrows':False,
      'source_stores_modified':False,'scope':contract['scope']}
    bound=[cp,*paths.values(),Path(__file__),ROOT/'research/strominger/checkers/assemble_endpoint_charging.py',base/'checkers/check_spinor_potential_link_bridge.py',base/'checkers/check_electron_tetrahedral_spinor.py',base/'checkers/check_projector_fold_sheets.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in bound}
    (base/'results/source-gauss-to-coulomb-binding-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':True,'neutral_graph_Gauss_cases':48*len(graph_tests),'single_bridge_energy_separable':True,'continuum_ground_checks':len(continuum),'ground_potential_folds':24,'Coulomb_and_mass_source_derived':False},indent=2))
if __name__=='__main__':main()
