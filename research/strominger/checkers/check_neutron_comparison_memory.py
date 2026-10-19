"""Derive reversible energy-bearing memory from all 21 actual neutron seams.

Storage task is explicit: remove those live comparisons and retain their full
residual information. This is not a physical splitting or rest-mass claim.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
import numpy as np
from scipy.linalg import eigh
from check_neutron_autonomous_rim_scattering import Contact
from check_neutron_canonical_occupied_closure import ROOT,eye,mm,transpose,inverse,difference,scale,rank,columns,encoded
from check_collective_carrier_spectrum import characteristic


def main():
    root=ROOT/'research/strominger/results'
    paths={k:root/v for k,v in {'source':'neutron-seam-control-transport.json','scattering':'neutron-autonomous-rim-scattering.json'}.items()}
    data={k:json.loads(p.read_text()) for k,p in paths.items()};checks={}
    for obj in data.values():
        assert obj['status']=='passed'
        for p,h in obj['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    source=data['source'];old=data['scattering'];npz=root/'neutron-autonomous-rim-scattering.npz'
    assert hashlib.sha256(npz.read_bytes()).hexdigest()==old['npz_sha256']
    checks['fresh_actual_seams_and_autonomous_fields']=True
    M=[list(map(F,r)) for r in source['metric']];Mi=inverse(M)
    B=[];weights=[];S=[[F(0)]*24 for _ in range(24)]
    for row in source['seam_controls']:
        a,b=row['ordered_triangle_positions'];r=[F(i==a)-F(i==b) for i in range(24)]
        weight=1/(1/M[a][a]+1/M[b][b]);B.append(r);weights.append(weight)
        P=scale(weight,mm(mm(Mi,columns([r])),[r]))
        assert P==[list(map(F,x)) for x in row['projector']]
        S=[[x+y for x,y in zip(v,w)] for v,w in zip(S,P)]
    Gamma=[[weights[i]*F(i==j) for j in range(21)] for i in range(21)]
    assert mm(mm(mm(Mi,transpose(B)),Gamma),B)==S
    assert rank(B)==rank(S)==15
    checks['all_21_normalized_residuals_reproduce_source_seams_exactly']=True
    # Exact native support projector, using independent residual rows rather
    # than an approximate pseudoinverse. Retain all original 21 rows separately.
    independent=[]
    for row in B:
        if rank(independent+[row])>len(independent):independent.append(row)
    Q=mm(mm(mm(Mi,transpose(independent)),inverse(mm(mm(independent,Mi),transpose(independent)))),independent)
    N=difference(eye(24),Q)
    assert mm(Q,Q)==Q and mm(B,N)==[[F(0)]*24 for _ in range(21)]
    A0=scale(F(1,4),[list(map(F,r)) for r in source['native_energy']])
    assert mm(A0,N)==mm(N,A0)
    exact_bright=[list(map(F,r)) for r in old['exact_bright_basis']]
    assert mm(A0,exact_bright)==[[F(0)]*5 for _ in range(24)]
    coherent=[F(1)]*18+[F(0)]*6
    assert all(sum(x*y for x,y in zip(row,coherent))==0 for row in B)
    change=difference(mm(mm(N,A0),N),A0)
    assert rank(change)==10 and mm(change,change)==scale(F(-3,4),change)
    checks['other_native_energy_change_computed_not_assumed_zero']=True
    # Occurrence-memory operator in its rational metric Gamma. Its spectrum
    # is that of the comparison residual, not 21 assigned elementary gaps.
    memory_raw=mm(mm(mm(B,Mi),transpose(B)),Gamma)
    groups={s:[i for i,row in enumerate(source['seam_controls']) if row['ordered_triangle_positions'][0]//6==s] for s in range(3)}
    assert all(len(indices)==7 for indices in groups.values())
    K6=[r[:6] for r in S[:6]];poly6=characteristic(K6)
    for indices in groups.values():
        block=[[memory_raw[i][j] for j in indices] for i in indices]
        assert characteristic(block)==poly6+[F(0)]
        assert all(memory_raw[i][j]==0 for i in indices for j in range(21) if j not in indices)
    checks['exact_memory_characteristic_polynomials_and_six_redundant_slots']=True
    with np.load(npz) as f:
        whitening=f['whitening'];K=f['core_operator'];leadW=f['contact'];bright=f['bright_basis']
        energies=f['energies'];savedS=f['S'];savedcore=f['core'];boundary=f['boundary']
    D=np.diag(np.sqrt(np.array(weights,float)))@np.array(B,float)@np.linalg.inv(whitening)
    Hmem=D@D.T;u,s,vh=np.linalg.svd(D,full_matrices=False)
    assert s[14]>1e-6 and s[15]<1e-10
    W=u[:,:15]@vh[:15,:];Qmem=u[:,:15]@u[:,:15].T
    Nw=np.eye(24)-W.T@W;Nm=np.eye(21)-Qmem
    assert np.linalg.norm(Nw-whitening@np.array(N,float)@np.linalg.inv(whitening))<1e-11
    U=np.block([[Nw,W.T],[W,Nm]])
    assert np.linalg.norm(U.T@U-np.eye(45))<1e-11
    assert np.linalg.norm(W.T@Hmem@W-D.T@D)<1e-11
    checks['full_45D_encoder_is_involutive_with_memory_kernel_retained']=True
    # Recover both native input and the original raw residual from the encoded
    # image; memory amplitudes are polar coordinates, not duplicated residuals.
    J=np.vstack((Nw,W));sqrtmem=(u[:,:15]*s[:15])@u[:,:15].T
    assert np.linalg.norm(J.T@J-np.eye(24))<1e-11
    assert np.linalg.norm(sqrtmem@W-D)<1e-11
    A0w=whitening@np.array(A0,float)@np.linalg.inv(whitening)
    Hafter=np.block([[A0w,np.zeros((24,21))],[np.zeros((21,24)),Hmem]])
    native_change=Nw@A0w@Nw-A0w
    assert np.linalg.norm(J.T@Hafter@J-K-native_change)<1e-11
    assert np.linalg.norm(A0w@bright)<1e-11
    assert np.linalg.norm(Hafter@J@bright-J@K@bright)<1e-11
    checks['actual_scattering_sector_has_exact_energy_intertwiner']=True
    # The contact must follow the encoded amplitude too. Keeping only native
    # ports discards memory contributions and changes the autonomous model.
    encodedW=J@leadW
    assert np.linalg.norm(encodedW.T@encodedW-np.eye(2))<1e-11
    assert np.linalg.norm(W@leadW)>1e-6
    model=Contact(Hafter,encodedW,[.5,.5])
    worst={'S':0.,'state_recovery':0.,'memory_energy':0.,'core_energy':0.,'contact_readout':0.}
    max_untransported_port_error=0.
    for E,oldS,c,a in zip(energies,savedS,savedcore,boundary):
        encoded_state=J@c;native_part=encoded_state[:24];memory=encoded_state[24:]
        recovered=Nw@native_part+W.T@memory
        mem_energy=memory.conj().T@Hmem@memory
        residual_energy=(D@c).conj().T@(D@c)
        worst['state_recovery']=max(worst['state_recovery'],float(np.linalg.norm(recovered-c)))
        worst['memory_energy']=max(worst['memory_energy'],float(np.linalg.norm(mem_energy-residual_energy)))
        worst['core_energy']=max(worst['core_energy'],float(np.linalg.norm(encoded_state.conj().T@Hafter@encoded_state-c.conj().T@K@c)))
        worst['contact_readout']=max(worst['contact_readout'],float(np.linalg.norm(encodedW.T@encoded_state-leadW.T@c)))
        max_untransported_port_error=max(max_untransported_port_error,float(np.linalg.norm(leadW.T@native_part-leadW.T@c)))
        new=model.scatter(float(E));worst['S']=max(worst['S'],float(np.linalg.norm(new['S']-oldS)))
    assert max(worst.values())<1e-8 and max_untransported_port_error>1e-6
    checks['all_201_scattering_matrices_and_full_energy_preserved_after_readout_transport']=True
    checks['native_only_readout_negative_control_detects_lost_memory']=True
    values=eigh(Hmem,eigvals_only=True);positive=values[values>1e-9]
    scale6=np.diag(np.sqrt([float(M[i][i]) for i in range(6)]))
    symmetric6=scale6@np.array(K6,float)@np.linalg.inv(scale6)
    assert np.linalg.norm(symmetric6-symmetric6.T)<1e-12
    eigen6=eigh(symmetric6,eigvals_only=True)
    expected=np.sort(np.repeat(eigen6[eigen6>1e-9],3))
    assert np.max(abs(positive-expected))<1e-10
    output_npz=root/'neutron-comparison-memory.npz'
    np.savez_compressed(output_npz,residual=D,memory_operator=Hmem,encoder=U,ready_embedding=J,
                        native_after=A0w,full_after=Hafter,contact_after=encodedW,memory_raw=np.array(memory_raw,float))
    result={'status':'passed','checks':checks,'storage_task':'Remove all 21 live normalized seam comparisons and store their residuals reversibly. No physical separation or occupied-register charging law is asserted.',
        'source_coordinate_order':source['coordinate_order'],
        'residual_occurrences':[{'edge':r['ordered_triangle_positions'],'actual_triangles':r['actual_native_triangle_indices'],'metric_weight':str(w)} for r,w in zip(source['seam_controls'],weights)],
        'residual_incidence':encoded(B),'memory_metric':encoded(Gamma),'rational_memory_operator':encoded(memory_raw),
        'memory_characteristic_per_seven_occurrence_block':list(map(str,poly6+[F(0)])),
        'memory_slots_retained':21,'independent_residual_dimension':15,'memory_kernel_dimension':6,
        'memory_eigenvalues_model_units':list(map(float,values)),
        'generic_native_energy_change':{'rank':10,'nonzero_eigenvalue':'-3/4','zero_multiplicity':14},
        'scattering_sector':'Its five-dimensional bright core lies in ker(A0). Ready-memory encoding intertwines the full core energy there; all 201 full scattering matrices agree when the contact is co-transported.',
        'maximum_residuals':worst,'untransported_native_only_contact_error':max_untransported_port_error,
        'no_rest_gap':'The coherent neutron has zero seam residual and stores no energy in ready memory. These are residual-memory excitation spectra, not positive occupied-neutron rest energies.',
        'npz_sha256':hashlib.sha256(output_npz.read_bytes()).hexdigest()}
    inputs=list(paths.values())+[npz,Path(__file__).resolve(),ROOT/'research/scattering/high-energy/pentachoron_exit_gate_note.md']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    (root/'neutron-comparison-memory.json').write_text(json.dumps(result,indent=2)+'\n')
    distinct=[]
    for value in values:
        if abs(value)<1e-10:value=0. # Six exact zeros certified by rank/polynomial tests.
        if not distinct or abs(value-distinct[-1]['value'])>1e-8:distinct.append({'value':float(value),'multiplicity':1})
        else:distinct[-1]['multiplicity']+=1
    print(json.dumps({'status':'passed','checks':len(checks),'memory_spectrum':distinct,'maximum_residuals':worst,
                     'native_only_contact_failure':max_untransported_port_error},indent=2))

if __name__=='__main__':main()
