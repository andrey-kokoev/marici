"""A shared zero-background Gauss model with explicit exterior flux.

Reuses the weighted matter/link law. Boundary attachment and a positive
exterior charging coefficient are declared inputs. Fixed-norm classical
sector minima are not quantum rest masses or electromagnetic charge IDs.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
from check_belt_interface_response import inverse

BASE=Path(__file__).resolve().parents[1]


def mv(a,v):return [sum(x*y for x,y in zip(row,v)) for row in a]


def grounded_laplacian(count,edges,ports):
    L=[[F(0) for _ in range(count)] for _ in range(count)]
    for i,j,_ in edges:
        L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
    for i in ports:L[i][i]+=1
    return L


def flux_certificate(count,edges,ports,rho,phi):
    # Every lead is oriented from the common exterior vertex toward a port.
    # The original incoming-incidence sign convention is retained.
    E=[phi[j]-phi[i] for i,j,_ in edges]+[phi[i] for i in ports]
    incidence=[(i,j) for i,j,_ in edges]+[(count,i) for i in ports]
    divergence=[F(0)]*(count+1)
    for (i,j),e in zip(incidence,E):divergence[i]-=e;divergence[j]+=e
    assert divergence==rho+[-sum(rho)]
    # E=B^T phi is orthogonal to every divergence-free circulation; hence
    # it is the unique minimum-norm field with this full retained charge.
    assert sum(e*e for e in E)==sum(x*y for x,y in zip(rho,phi))
    return sum(e*e for e in E)/2


def main():
    path=BASE/'results/weighted_matter_link_adapter.json'
    raw=path.read_bytes();source=json.loads(raw)['carriers']
    contacts=json.loads((BASE/'results/all_face_contact.json').read_text())['carriers']
    data={}
    for name,row in source.items():
        n=list(map(F,row['metric_weights']))
        edges=[(i,j,F(w)) for i,j,w in row['edges']]
        ports=contacts[name]['covered_triangles']
        assert len(ports)==12
        L=grounded_laplacian(len(n),edges,ports)
        Linv=inverse(L)
        # An explicit zero state satisfies the SAME full Gauss law.
        assert flux_certificate(len(n),edges,ports,[F(0)]*len(n),[F(0)]*len(n))==0
        data[name]=(n,edges,ports,L,Linv)
    pn,pe,pp,PL,PI=data['proton'];bn,be,bp,BL,BI=data['belt']
    assert len(pn)==12 and set(pp)==set(range(12))
    assert len(bn)==18 and set(bp)=={i for i in range(18) if i%3!=1}
    assert len(set(pn))==1
    outer=bn[0];middle=bn[1]
    assert bn==[outer,middle,outer]*6
    gamma=outer*middle/(outer+middle)
    across_types=[(i,j,w) for i,j,w in be if (i in bp)!=(j in bp)]
    assert len(across_types)==12 and all(w==gamma for _,_,w in across_types)
    assert all(sum(i==v or j==v for i,j,_ in across_types)==(1 if v in bp else 2) for v in range(18))
    rho_p=[F(1,12)]*12;phi_p=mv(PI,rho_p)
    assert phi_p==rho_p
    assert flux_certificate(12,pe,pp,rho_p,phi_p)==F(1,24)
    joint_edges=[(i,j) for i,j,_ in pe]+[(i+12,j+12) for i,j,_ in be]+[(30,i) for i in pp]+[(30,i+12) for i in bp]
    assert len(joint_edges)==87
    def joint_gauss(rp,rb):
        phi=mv(PI,rp)+mv(BI,rb)+[F(0)]
        E=[phi[j]-phi[i] for i,j in joint_edges]
        divergence=[F(0)]*31
        for (i,j),e in zip(joint_edges,E):divergence[i]-=e;divergence[j]+=e
        assert divergence==rp+rb+[-sum(rp)-sum(rb)]
        return sum(e*e for e in E)/2
    assert joint_gauss([F(0)]*12,[F(0)]*18)==0
    assert joint_gauss(rho_p,[F(0)]*18)==F(1,24)

    # For any common outer/inner density, all exact field equations reduce
    # to phi_outer=1/12, phi_inner=1/12+rho_inner/2.
    def belt_state(t):
        D=12*outer+6*middle*t*t
        rho=[(outer if i in bp else middle*t*t)/D for i in range(18)]
        phi=[F(1,12)+(rho[i]/2 if i not in bp else 0) for i in range(18)]
        assert sum(rho)==1 and mv(BL,phi)==rho and mv(BI,rho)==phi
        field=flux_certificate(18,be,bp,rho,phi)
        y=6*rho[1]
        assert field==F(1,24)+y*y/24
        assert joint_gauss([F(0)]*12,rho)==field
        amplitudes=[F(1) if i in bp else t for i in range(18)]
        matter=sum(w*(amplitudes[i]-amplitudes[j])**2 for i,j,w in be)/D
        assert matter==12*gamma*(1-t)**2/D
        return y,matter,field
    for t in (F(0),F(1,2),F(1)):belt_state(t)
    A=gamma/outer;B=2*gamma/middle
    assert A==F(2099,3292) and B==F(1193,1646)
    eta=F(1,5);results=[]
    for beta in (F(3,5),F(1),F(6)):
        # Convex density functional yields a unique global minimum. The
        # two-density ansatz satisfies the FULL Euler equations at its root:
        # all outer gradients coincide and all inner gradients coincide.
        def derivative_y(t):
            y,_,_=belt_state(t)
            return B*(1-1/t)-A*(1-t)+beta*y/12
        def polynomial(t):
            return beta*middle*(outer+middle)*t**3-12*(1-t)*(2*outer+middle*t)*(2*outer+middle*t*t)
        lo=F(0);hi=F(1)
        for _ in range(70):
            t=(lo+hi)/2
            if polynomial(t)<0:lo=t
            else:hi=t
        assert 0<lo<hi<1 and derivative_y(lo)<0<derivative_y(hi)
        t=(lo+hi)/2
        ylo,mlo,flo=belt_state(lo);yhi,mhi,fhi=belt_state(hi)
        y,matter,field=belt_state(t)
        F_lo=mlo+beta*(flo-F(1,24));F_hi=mhi+beta*(fhi-F(1,24))
        # Convex supporting tangents provide a certified lower bound; any
        # evaluated trial gives an upper bound on the global minimum.
        lower=max(F_lo+derivative_y(lo)*(yhi-ylo),F_hi+derivative_y(hi)*(ylo-yhi))
        upper=matter+beta*(field-F(1,24))
        assert 0<lower<=upper
        coherent_y,coherent_matter,coherent_field=belt_state(F(1))
        assert coherent_matter==0 and upper<beta*(coherent_field-F(1,24))
        # Full density gradients at the approximate root reduce to two
        # rational values, so the scalar stationary equation is not a
        # symmetry assumption about the full 18-vertex graph.
        D=12*outer+6*middle*t*t
        rho=[(outer if i in bp else middle*t*t)/D for i in range(18)]
        phi=mv(BI,rho);amp=[F(1) if i in bp else t for i in range(18)]
        grad=[beta*v for v in phi]
        for i,j,w in be:
            grad[i]+=w/bn[i]*(1-amp[j]/amp[i])
            grad[j]+=w/bn[j]*(1-amp[i]/amp[j])
        assert len({grad[i] for i in bp})==1
        assert len({grad[i] for i in range(18) if i not in bp})==1
        assert grad[1]-grad[0]==derivative_y(t)
        proton=beta/24+eta/2
        results.append({'beta':str(beta),'exterior_eta':str(eta),
                        'amplitude_ratio_interval':list(map(str,(lo,hi))),
                        'middle_density_fraction':float(y),
                        'proton_sector_energy_exact':str(proton),
                        'belt_sector_energy_upper':float(proton+upper),
                        'belt_minus_proton_interval':list(map(str,(lower,upper))),
                        'belt_minus_proton_decimal':float((lower+upper)/2),
                        'belt_matter_energy':float(matter),
                        'belt_electric_energy':float(beta*field),
                        'exterior_charge':-1,'exterior_energy_exact':str(eta/2)})
    # Control: same alternative rule on both carriers, one exterior lead at
    # EVERY mode vertex. A coherent belt trial then already lies below the
    # proton minimum. Do not hide boundary-attachment dependence.
    total=sum(bn);rho=[x/total for x in bn]
    alternative_E=[F(0)]*len(be)+rho
    alternative_edges=[(i,j) for i,j,_ in be]+[(18,i) for i in range(18)]
    alternative_div=[F(0)]*19
    for (i,j),e in zip(alternative_edges,alternative_E):alternative_div[i]-=e;alternative_div[j]+=e
    assert alternative_div==rho+[F(-1)]
    trial_field=sum(x*x for x in alternative_E)/2
    assert trial_field<F(1,24)  # exact feasible bound, not an optimized value
    report={
        'verification_passed':True,
        'prior_reused':['record-gauge-feedback-loop.md: matter/link energy and Gauss law','mass-history-retaining-locking-interaction.md: retain exterior charge and energy accounts'],
        'common_graph':{'matter_vertices':30,'exterior_vertices':1,'internal_links':63,'boundary_leads':24,'total_links':87},
        'boundary_rule':'One identical electric lead from each cross-face-contact endpoint to a common exterior charge coordinate; twelve leads per carrier.',
        'gauss_law':'B_full E=(rho_proton,rho_belt,q_ext), q_ext=-(Q_proton+Q_belt); fixed background identically zero',
        'hamiltonian':'H_matter,p+H_matter,b+(beta/2)*sum E^2+(eta/2)*q_ext^2',
        'same_vacuum_admitted':True,'vacuum_energy':0,
        'charge_interpretation':'Q_s=sum n_i|a_i|^2 is an internal conserved norm-charge, not electric charge. Both tested particle sectors have internal charge one.',
        'proton_minimum':'beta/24+eta/2 in sector (Qp,Qb)=(1,0)',
        'belt_minimum':'beta/24+eta/2 + min_[0,1] ([sqrt(A)*sqrt(1-y)-sqrt(B)*sqrt(y)]^2+beta*y^2/24), A=2099/3292, B=1193/1646',
        'global_minimum_argument':'Density energy is convex (negative geometric means plus a positive-definite electric quadratic). The displayed density obeys the full constrained stationarity equations; strict electric convexity gives uniqueness.',
        'strict_belt_excess_for_selected_boundary_rule':True,
        'illustrative_minima':results,
        'alternative_boundary_rule':'One identical lead at every mode vertex, on both carriers.',
        'alternative_belt_electric_trial_coefficient':str(trial_field),
        'alternative_proton_minimum_coefficient':'1/24',
        'alternative_boundary_rule_reverses_order':True,
        'scope':'Classical fixed-norm common-vacuum completion with full boundary energy. Attachment rule, beta, eta and unit-charge sector are declared; no quantum particle gap, physical electric charge or mass calibration is derived.',
        'source_sha256':{'weighted_adapter':sha256(raw).hexdigest(),'contact_addresses':sha256((BASE/'results/all_face_contact.json').read_bytes()).hexdigest()}}
    (BASE/'results/open_flux_common_vacuum.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
