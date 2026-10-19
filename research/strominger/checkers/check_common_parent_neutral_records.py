"""Attach inherited neutral seam records to the signed endpoint parent.

No sector scalar is inserted: local two-state operators are retained. Exact
operator inequalities avoid building the 18*2^21-dimensional belt matrix.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
from assemble_endpoint_charging import ROOT
from check_seam_occupation_energy import local_certificate
from check_pentachoron_spin_interfaces import A,S2,S5,I,add as aadd,scale as ascale,mm,adj
from check_coupled_six_piece_belt import R,Z,ONE,conj,scale,norm
from check_belt_three_by_twelve import decode
from check_constraint_energy_accounting import compose,plus,times,identity,adjoint,trace


def rational_matrix(m):return {ij:(R(x),R()) for ij,x in m.items() if x}
def matrix(rows):return {(i,j):decode(v) for i,j,v in rows}
def difference(a,b):return plus(a,times(-1,b))


def main():
    parentpath=ROOT/'research/strominger/results/common-endpoint-charging.json';parent=json.loads(parentpath.read_text())
    assert parent['status']=='passed'
    for p,h in parent['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    base=ROOT/'research/voevodsky'
    nativepath=base/'results/native_operation_energy_lift_store.json';native=json.loads(nativepath.read_text())['carriers']
    intrinsicpath=base/'results/belt_three_by_twelve_store.json';intrinsic=json.loads(intrinsicpath.read_text())
    weightedpath=base/'results/weighted_matter_link_adapter.json';weighted=json.loads(weightedpath.read_text())
    assert weighted['source_sha256']==hashlib.sha256(nativepath.read_bytes()).hexdigest()
    source=weighted['carriers']['belt'];weights=list(map(F,source['metric_weights']));d=[F(c['d']) for c in intrinsic['coordinates']]
    modes=[decode(c['selected_numerator']) for c in intrinsic['coordinates']]
    V={};decoder={}
    for t in range(18):
        measured=sum((norm(modes[2*t+i])/d[2*t+i] for i in range(2)),R())
        assert measured==weights[t]
        for i in range(2):
            z=modes[2*t+i]
            V[2*t+i,t]=z;decoder[t,2*t+i]=scale(1/(d[2*t+i]*weights[t]),conj(z))
    assert compose(decoder,V)==identity(18)
    K=rational_matrix({(i,j):F(x) for i,row in enumerate(parent['source_operators']['belt']['kinetic_operator']) for j,x in enumerate(row) if F(x)})
    assert compose(compose(decoder,times(F(1,4),matrix(native['belt']['entries']))),V)==K
    Ptotal={};projectors=[];seam_pairs=set()
    for entry in native['belt']['seam_projectors']:
        i,j=entry['triangles'];seam_pairs.add((i,j));gamma=weights[i]*weights[j]/(weights[i]+weights[j])
        P=rational_matrix({(i,i):gamma/weights[i],(i,j):-gamma/weights[i],(j,j):gamma/weights[j],(j,i):-gamma/weights[j]})
        inherited=matrix(entry['entries'])
        assert compose(inherited,V)==compose(V,P)
        assert compose(compose(decoder,inherited),V)==P
        assert compose(P,P)==P and trace(P,18)==1 and adjoint(P,tuple(1/w for w in weights))==P
        assert all(sum(P.get((a,b),Z)[0] for b in range(18))==0 for a in range(18))
        Ptotal=plus(Ptotal,P)
        projectors.append({'triangles':[i,j],'entries':[[a,b,[str(v[0].a),'0','0','0']] for (a,b),v in sorted(P.items())]})
    assert len(projectors)==21
    # K-sum(P_e) is exactly the positive native-alignment edge Laplacian.
    alignment={};remaining=[]
    for i,j,w in source['edges']:
        w=F(w)
        if (i,j) in seam_pairs:
            assert w==weights[i]*weights[j]/(weights[i]+weights[j]);continue
        remaining.append([i,j,str(w)])
        for a,b in ((i,j),(j,i)):
            alignment[a,a]=alignment.get((a,a),F(0))+w/weights[a]
            alignment[a,b]=alignment.get((a,b),F(0))-w/weights[a]
    assert all(F(w)>0 for _,_,w in remaining)
    assert difference(K,Ptotal)==rational_matrix(alignment)
    # In the selected amplitude frame the retained belt state is constant.
    N=rational_matrix({(i,j):weights[j]/sum(weights) for i in range(18) for j in range(18)})
    assert compose(K,N)=={} and compose(Ptotal,N)=={}
    assert compose(compose(decoder,matrix(native['belt']['return_entries'])),V)==N
    assert native['proton']['seam_projectors']==[]
    # Elementary local groups are its four individual rank-one face ports;
    # no pair of distinct native lines lies within one local group.
    groups={'proton':[[i] for i in range(12)],'belt':[list(range(6*s,6*s+6)) for s in range(3)],'electron':[[i] for i in range(4)]}
    assert all(any(i in g and j in g for g in groups['belt']) for i,j in seam_pairs)
    epsilon,J=F(1,4),F(1,2);trials=[]
    for g,rplus,rminus in [(F(0),A(F(3,4)),A(F(1,4))),(F(1,8),S2*S5/4,S2/4),(F(3,8),3*S2/4,S2*S5/4)]:
        cert=local_certificate(epsilon,J,g,rplus,rminus);ev=cert['inactive_ground'];eb=cert['matched_ground'];delta=cert['relative_seam_energy']
        # In each projector sector the 2x2 positive remainders were certified
        # by local_certificate. Tensoring with P, I-P preserves positivity.
        # h_e - ev I >= delta(I-P_e). Different P_e need not commute.
        assert epsilon<J and epsilon<1
        # rplus²-rminus²=4 epsilon J and rplus+rminus>=2J imply 0<delta<=epsilon.
        assert rplus*rplus-rminus*rminus==A(4*epsilon*J)
        assert (eb-ev)==delta
        Hmatched=((A(J),A(-g)),(A(-g),A(epsilon)))
        matched_projector=ascale(rminus.inverse(),aadd(ascale(eb+rminus,I),ascale(A(-1),Hmatched)))
        assert mm(Hmatched,matched_projector)==ascale(eb,matched_projector)
        trials.append({'g':str(g),'relative_energy_per_seam':delta.record(),'belt_ground_energy':(21*delta).record(),
                       'same_empty_reference_per_record':ev.record(),'matched_record_projector':[[x.record() for x in row] for row in matched_projector],
                       'proof':'K=A_align+sum P_e; H_joint-vacuum >= 21delta + A_align +(1-delta)sum P_e + H_endpoint_field. Constant belt mode, zero flux and matched record grounds attain equality.'})
    # Keep the SAME 21-register pool in every sector and the vacuum.
    # Proton/electron have S_e=0 for all records, so each takes its inactive
    # ground ev. Subtract 21ev ONCE across all sectors, not only the belt.
    plo,phi=map(F,parent['sectors']['proton']['ground_interval']);elo,ehi=map(F,parent['sectors']['electron']['ground_interval'])
    belt=21*epsilon
    split=( (belt-phi)/ehi,(belt-plo)/elo )
    assert belt>phi>0
    report={'status':'passed','shared_neutral_record_pool':21,'record_law':'epsilon*n + J*(n-S)^2 - g*X; S=c_belt*(I-P_e); all records retained inactive outside belt',
            'parameters':{'epsilon':str(epsilon),'J':str(J),'seam_coefficient_in_source_K':'1'},'source_local_groups':groups,
            'belt_seams':projectors,'remaining_positive_alignment_edges':remaining,
            'trials':trials,'zero_mixing_comparison':{'proton_ground_interval':[str(plo),str(phi)],'electron_ground_interval':[str(elo),str(ehi)],
                'belt_ground_energy':str(belt),'proton_per_electron_interval':[str(plo/ehi),str(phi/elo)],'belt_minus_proton_per_electron_interval':[str(x) for x in split]},
            'checks':{'native_full_carrier_seams_intertwined':True,'source_K_dominates_seam_sum':True,'native_belt_return_preserved':True,
                'one_record_pool_and_empty_reference':True,'neutral_record_interaction_preserves_external_Gauss':parent['sectors']['belt']['signed_charge']==0,
                'three_joint_ground_energies_certified':True,'no_stage_support_assigned_energy':True},
            'scope':'Common endpoint parent plus existing neutral seam law on supplied local groups. The bound treats noncommuting seams exactly. No fitted offsets, new gaps, or huge joint-matrix truncation.',
            'disposition':'Neutral belt now has positive energy from actual retained record operators. Proton/electron ratio remains 1.163..., so this combined fixture still fails the joint mass comparison.'}
    paths=[Path(__file__).resolve(),parentpath,nativepath,intrinsicpath,weightedpath,base/'checkers/check_seam_occupation_energy.py',base/'checkers/check_constraint_energy_accounting.py',base/'checkers/check_coupled_six_piece_belt.py',base/'checkers/check_belt_three_by_twelve.py']
    report['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    out=ROOT/'research/strominger/results/common-parent-neutral-records.json';out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':report['checks'],'zero_mixing_energies':{'proton':float(plo),'electron':float(elo),'belt':float(belt)},
                      'splitting_per_electron_interval':list(map(float,split))},indent=2))

if __name__=='__main__':main()
