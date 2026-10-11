"""Source-only channel elimination versus the added common-reference model.

Extract exact local port response polynomials on every retained shared edge.
Check genuine source Schur elimination and contact-dependence separately.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from math import comb
from hashlib import sha256
import json
from check_common_contact_dressing import port_projector, rational_response, add_poly
from check_collective_carrier_spectrum import polynomial_product
from check_belt_interface_response import evaluate, inverse
from check_seam_occupation_energy import matrix
from check_constraint_energy_accounting import identity, plus, times, compose, trace
from check_coupled_six_piece_belt import R, norm
from check_reversed_coefficient_attachment import SOURCE
from check_geometric_cycle_reversal import geo

BASE=Path(__file__).resolve().parents[1]


def shifted(p,c):
    degree=len(p)-1;out=[F(0)]*len(p)
    for i,value in enumerate(p):
        power=degree-i
        for k in range(power+1):out[degree-k]+=value*comb(power,k)*c**(power-k)
    return out


def main():
    spectrum=json.loads((BASE/'results/collective_carrier_spectrum.json').read_text())
    store=json.loads((BASE/'results/native_operation_energy_lift_store.json').read_text())['carriers']
    packet=json.loads(SOURCE.read_bytes());objects=packet['objects']
    geometry=objects[objects[packet['root']]['geometry']]['payload']
    placements=sorted(geometry['triangles_and_transports'],key=lambda r:r['outer_arrow'])
    points=dict(geo.POINTS)
    for face in ('ABC','ABD','ACD','BCD'):points['F_'+face]=geo.mean([points[v] for v in face])
    modes=[]
    for row in placements:
        X=geo.transpose(tuple(points[v] for v in row['triangle']))
        modes.append([(R(x[0]),R(x[1])) for x in geo.zmv(X,(geo.ONE,geo.OMEGA,geo.zmul(geo.OMEGA,geo.OMEGA)))])
    Hp=times(F(1,4),matrix(store['proton']['entries']))
    phase=plus({(i,j):v for (i,j),v in Hp.items() if i//3==j//3},times(-1,identity(36)))
    align=plus(Hp,times(-1,phase));roots=[F(0),F(1,2),F(1),F(3,2)]
    Ps=[]
    for root in roots:
        P=identity(36)
        for other in roots:
            if root!=other:P=compose(P,times(1/(root-other),plus(align,times(-other,identity(36)))))
        Ps.append(P)
    proton=[]
    for a,b in combinations(range(12),2):
        if len(set(placements[a]['triangle'])&set(placements[b]['triangle']))!=2:continue
        W=port_projector({3*t+i:v for t in (a,b) for i,v in enumerate(modes[t])},(F(1),)*36)
        weights=[trace(compose(W,P),36) for P in Ps]
        assert weights[0]==F(1,6)
        numerator,denominator=rational_response(roots,weights)
        proton.append((a,b,numerator,denominator,weights))
    assert len(proton)==18
    K=[[F(x) for x in row] for row in spectrum['belt_reduced_matrix']]
    n=list(map(F,spectrum['belt_modal_norms']))
    D=[(-1)**i*F(c) for i,c in enumerate(spectrum['belt_reduced_characteristic_descending'])]
    belt=[]
    for edge in store['belt']['seam_projectors']:
        a,b=edge['triangles']
        if b>=6:continue
        v=[F(i in (a,b)) for i in range(6)];moments=[]
        for k in range(6):
            moments.append((n[a]*v[a]+n[b]*v[b])/(n[a]+n[b]))
            v=[sum(K[i][j]*v[j] for j in range(6)) for i in range(6)]
        N=[sum(D[i]*(-1)**(k-i)*moments[k-i] for i in range(k+1)) for k in range(6)]
        Ds,Ns=shifted(D,F(3,4)),shifted(N,F(3,4))
        denominator=polynomial_product(D,Ds)
        numerator=[x/3 for x in add_poly(polynomial_product(N,Ds),[2*x for x in polynomial_product(Ns,D)])]
        r0=(n[a]+n[b])/(3*sum(n))
        assert numerator[-1]!=0 and denominator[-1]==0
        for t in (F(1,10),F(1)):
            direct=F(0)
            for shift,weight in ((F(0),F(1,3)),(F(3,4),F(2,3))):
                inv=inverse([[K[i][j]+(t+shift)*int(i==j) for j in range(6)] for i in range(6)])
                direct+=weight*(n[a]*(inv[a][a]+inv[a][b])+n[b]*(inv[b][a]+inv[b][b]))/(n[a]+n[b])
            assert evaluate(numerator,t)/evaluate(denominator,t)==direct
        belt.append((a,b,numerator,denominator,r0,moments[1]+F(1,2)))
    report={}
    certificates=[];unresolved=[];reversed_samples=[]
    for a,b,pn,pd,pweights in proton:
        for c,d,bn,bd,r0,m1 in belt:
            difference=add_poly(polynomial_product(pn,bd),[-x for x in polynomial_product(bn,pd)])
            entry={'proton':[a,b],'belt':[c,d]}
            if all(x>=0 for x in difference) and any(x>0 for x in difference):certificates.append(entry)
            else:
                signs=[]
                for t in (F(1,1000),F(1,10),F(1,4),F(1,2),F(3,4),F(1),F(2),F(3),F(5),F(10),F(1000)):
                    diff=evaluate(pn,t)/evaluate(pd,t)-evaluate(bn,t)/evaluate(bd,t)
                    signs.append((str(t),str(diff)))
                if any(F(value)<0 for _,value in signs):reversed_samples.append({**entry,'samples':signs})
                else:unresolved.append(entry)
    cross_face_pairs=[entry for entry in certificates
                      if placements[entry['proton'][0]]['triangle'][0]!=placements[entry['proton'][1]]['triangle'][0]
                      and entry['belt']==[0,3]]
    assert len(cross_face_pairs)==6
    assert len(certificates)+len(unresolved)+len(reversed_samples)==126
    # Exact source Schur identity: Sigma(-t)=h00+t-1/R(t).
    # Every source contact overlaps the coherent zero state, so R(t)~r0/t
    # and Sigma(0)=h00. No rest offset is generated by eliminating these modes.
    rows=[]
    for name,contacts in (('proton',proton),('belt',belt)):
        for row in contacts:
            a,b,N,D=row[:4]
            if name=='proton':
                r0=row[4][0];h00=sum(e*w for e,w in zip(roots,row[4]))
            else:r0,h00=row[4:]
            # Direct residue of N(t)/D(t); all denominators have one zero.
            assert D[-1]==0 and D[-2]!=0 and N[-1]/D[-2]==r0
            assert r0>0
            rows.append({'carrier':name,'edge':[a,b],'coherent_residue':str(r0),
                         'bare_contact_energy':str(h00),'source_self_energy_at_zero':str(h00),
                         'source_effective_energy_at_zero':'0'})
    report={'verification_passed':True,'proton_edges':len(proton),'belt_representative_edges':len(belt),
            'contact_pairs':len(proton)*len(belt),'globally_certified_proton_response_larger':len(certificates),
            'cross_face_typed_comparisons_all_certified':cross_face_pairs,
            'source_sha256':{str(p.relative_to(BASE.parent)):sha256(p.read_bytes()).hexdigest() for p in (SOURCE,BASE/'results/collective_carrier_spectrum.json',BASE/'results/native_operation_energy_lift_store.json')},
            'reversed_sample_pair_count':len(reversed_samples),'uncertified_pair_count':len(unresolved),
            'reversed_sample_pairs':reversed_samples,'uncertified_pairs':unresolved,
            'source_only_channel_elimination':rows,
            'source_only_conclusion':'Extracting an internal channel from the same retained positive carrier does not supply the previously added auxiliary law: its bare contact term and static self-energy cancel, preserving zero energy.',
            'scope':'Exact contact response audit and source Schur identity; no new physical field or mass normalization.'}
    (BASE/'results/contact_source_closure.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ('source_only_channel_elimination','reversed_sample_pairs','uncertified_pairs')},indent=2))


if __name__=='__main__':main()
