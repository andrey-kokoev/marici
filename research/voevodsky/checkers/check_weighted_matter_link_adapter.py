"""Adapt the existing matter/link feedback law to actual selected source modes.

Exact source embeddings, edge weights, current, continuity and gauge controls;
weighted exact-subflow feedback tests use Python complex floats explicitly.
No physical charge normalization or quantum vacuum identification is supplied.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from math import pi
from cmath import exp
import json
from check_seam_occupation_energy import matrix
from check_constraint_energy_accounting import identity, plus, times, compose, trace
from check_coupled_six_piece_belt import R, Z, norm, conj, scale
from check_belt_three_by_twelve import decode
from check_geometric_cycle_reversal import geo
from check_reversed_coefficient_attachment import SOURCE
from check_pentachoron_spin_interfaces import A, CI

BASE=Path(__file__).resolve().parents[1]


def real(x):
    assert all(c==0 for c in x.c[1:])
    return x.c[0]


def exact_field_check(n,edges):
    m=len(n);phases=[A(1),CI,A(-1),-CI]
    a=[A(F(i%5+1,7))+CI*F(i%3-1,11) for i in range(m)]
    U=[phases[e%4] for e in range(len(edges))]
    E=[F(e%3-1,1000) for e in range(len(edges))];beta=F(3,5)
    def evaluate(a,U):
        gradient=[A(0) for _ in n];currents=[];energy=A(0)
        for (i,j,gamma),u in zip(edges,U):
            defect=a[j]-u*a[i]
            energy+=gamma*defect.flip(8)*defect
            gradient[i]-=gamma*u.flip(8)*defect
            gradient[j]+=gamma*defect
            current=2*gamma*(a[j].flip(8)*u*a[i])
            currents.append(real((current-current.flip(8))/(2*CI)))
            # d/dA of gamma*|a_j-exp(iA)*a_i|^2 is the same J.
            ddefect=-CI*u*a[i]
            assert real(gamma*(ddefect.flip(8)*defect+defect.flip(8)*ddefect))==currents[-1]
        derivative=[-CI*x/weight for x,weight in zip(gradient,n)]
        rho=[weight*real(x.flip(8)*x) for x,weight in zip(a,n)]
        drho=[weight*real(x.flip(8)*v+v.flip(8)*x) for x,v,weight in zip(a,derivative,n)]
        divergence=[F(0)]*m
        for (i,j,_),J in zip(edges,currents):divergence[i]-=J;divergence[j]+=J
        assert all(x+y==0 for x,y in zip(drho,divergence))
        assert sum(drho)==0
        matter_state_power=sum((real(grad.flip(8)*v+v.flip(8)*grad) for grad,v in zip(gradient,derivative)),F(0))
        assert matter_state_power==0
        return real(energy),currents,rho,drho,derivative
    energy,J,rho,drho,derivative=evaluate(a,U)
    divE=[F(0)]*m
    for (i,j,_),e in zip(edges,E):divE[i]-=e;divE[j]+=e
    background=[r-d for r,d in zip(rho,divE)]
    assert all(x>0 for x in background) and sum(background)==sum(rho)
    divEdot=[F(0)]*m
    for (i,j,_),jcur in zip(edges,J):divEdot[i]+=jcur;divEdot[j]-=jcur
    assert divEdot==drho
    assert sum(jcur*beta*e+beta*e*(-jcur) for jcur,e in zip(J,E))==0
    for shift in (1,2,3):
        gauge=[phases[(shift*i+i//3)%4] for i in range(m)]
        ap=[v*x for v,x in zip(gauge,a)]
        Up=[gauge[j]*u*gauge[i].flip(8) for (i,j,_),u in zip(edges,U)]
        ep,jp,rp,dp,vp=evaluate(ap,Up)
        assert (ep,jp,rp,dp)==(energy,J,rho,drho)
        assert vp==[v*x for v,x in zip(gauge,derivative)]
    return {'continuity':True,'link_force_matches_current':True,'gauss_derivative':True,
            'hamiltonian_power_balance':True,'root_of_unity_gauge_controls':3,
            'fixed_background_total':str(sum(background)),
            'empty_matter_violates_same_closed_graph_gauss':sum(background)!=0}


def numerical_feedback(n,edges):
    n=list(map(float,n));edges=[(i,j,float(w)) for i,j,w in edges]
    beta=.6;m=len(n)
    a0=[complex(F(i%5+1,7),F(i%3-1,11)) for i in range(m)]
    A0=[(0.,pi/2,pi,-pi/2)[i%4] for i in range(len(edges))]
    E0=[float(F(i%3-1,1000)) for i in range(len(edges))]
    def rho(a):return [w*abs(x)**2 for w,x in zip(n,a)]
    def div(E):
        out=[0.]*m
        for (i,j,_),e in zip(edges,E):out[i]-=e;out[j]+=e
        return out
    bg=[x-y for x,y in zip(rho(a0),div(E0))]
    def energy(a,A,E):
        return sum(w*abs(a[j]-exp(1j*phase)*a[i])**2 for (i,j,w),phase in zip(edges,A))+beta*sum(e*e for e in E)/2
    def step(a,A,E,dt):
        for e in range(len(edges)):A[e]+=dt*beta*E[e]/2
        for e in list(range(len(edges)))+list(reversed(range(len(edges)))):
            i,j,gamma=edges[e];u=exp(1j*A[e]);defect=a[j]-u*a[i]
            rate=gamma*(1/n[i]+1/n[j]);factor=(exp(-1j*rate*dt/2)-1)/rate
            old=n[j]*abs(a[j])**2
            a[i]+=factor*(-gamma*u.conjugate()*defect)/n[i]
            a[j]+=factor*gamma*defect/n[j]
            E[e]+=n[j]*abs(a[j])**2-old
        for e in range(len(edges)):A[e]+=dt*beta*E[e]/2
    def run(dt,gauge=None):
        a=a0[:];A=A0[:];E=E0[:]
        if gauge is not None:
            a=[exp(1j*chi)*x for chi,x in zip(gauge,a)]
            A=[x+gauge[j]-gauge[i] for x,(i,j,_) in zip(A,edges)]
        H0=energy(a,A,E);err=0.;gauss=0.
        for _ in range(round(.25/dt)):
            step(a,A,E,dt)
            err=max(err,abs(energy(a,A,E)-H0))
            gauss=max(gauss,max(abs(d-r+b) for d,r,b in zip(div(E),rho(a),bg)))
        assert gauss<1e-10 and abs(sum(rho(a))-sum(rho(a0)))<1e-10
        return a,A,E,err,gauss
    coarse=run(.01);fine=run(.005)
    assert fine[3]<coarse[3]/3
    gauge=[.13*i-.03*(i%3) for i in range(m)];gauged=run(.01,gauge)
    gauge_error=max(max(abs(x-exp(1j*c)*y) for x,y,c in zip(gauged[0],coarse[0],gauge)),
                    max(abs(x-y-gauge[j]+gauge[i]) for x,y,(i,j,_) in zip(gauged[1],coarse[1],edges)),
                    max(abs(x-y) for x,y in zip(gauged[2],coarse[2])))
    assert gauge_error<1e-10
    a,A,E=(x[:] for x in coarse[:3])
    for _ in range(25):step(a,A,E,-.01)
    reversal=max(max(abs(x-y) for x,y in zip(v,w)) for v,w in ((a,a0),(A,A0),(E,E0)))
    assert reversal<1e-10
    changeE=sum((x-y)**2 for x,y in zip(coarse[2],E0))**.5
    changeA=sum((x-y)**2 for x,y in zip(coarse[1],A0))**.5
    assert changeE>1e-4 and changeA>1e-4
    return {'time':.25,'beta':beta,'energy_errors':[coarse[3],fine[3]],
            'gauss_error':coarse[4],'gauge_error':gauge_error,'reversal_error':reversal,
            'electric_change_norm':changeE,'phase_change_norm':changeA,
            'unwrapped_link_phases_retained':True}


def main():
    path=BASE/'results/native_operation_energy_lift_store.json';raw=path.read_bytes()
    store=json.loads(raw)['carriers']
    packet=json.loads(SOURCE.read_bytes());objects=packet['objects']
    geometry=objects[objects[packet['root']]['geometry']]['payload']
    placements=sorted(geometry['triangles_and_transports'],key=lambda row:row['outer_arrow'])
    points=dict(geo.POINTS)
    for face in ('ABC','ABD','ACD','BCD'):points['F_'+face]=geo.mean([points[v] for v in face])
    pmodes=[]
    for row in placements:
        X=geo.transpose(tuple(points[v] for v in row['triangle']))
        pmodes.append([(R(x[0]),R(x[1])) for x in geo.zmv(X,(geo.ONE,geo.OMEGA,geo.zmul(geo.OMEGA,geo.OMEGA)))])
    bsource=json.loads((BASE/'results/belt_three_by_twelve_store.json').read_text())
    z=[decode(c['selected_numerator']) for c in bsource['coordinates']]
    results={}
    for name,modes,d in (('proton',pmodes,(F(1),)*36),('belt',[z[2*t:2*t+2] for t in range(18)],tuple(F(c['d']) for c in bsource['coordinates']))):
        width=len(modes[0]);m=len(modes);V={};decoder={};n=[]
        for t,v in enumerate(modes):
            ns=sum((norm(x)/d[width*t+i] for i,x in enumerate(v)),R())
            assert ns.b==0 and ns.a>0;n.append(ns.a)
            for i,x in enumerate(v):
                if x!=Z:
                    V[width*t+i,t]=x
                    decoder[t,width*t+i]=scale(1/(ns*d[width*t+i]),conj(x))
        assert compose(decoder,V)==identity(m)
        H=times(F(1,4),matrix(store[name]['entries']))
        K=compose(compose(decoder,H),V)
        assert compose(H,V)==compose(V,K)
        Q=compose(V,decoder)
        assert compose(H,Q)==compose(Q,H) and trace(Q,36)==m
        entries={}
        for ij,value in K.items():
            assert value[1]==0 and value[0].b==0;entries[ij]=value[0].a
        edges=[]
        for i in range(m):
            for j in range(i+1,m):
                weight=-n[i]*entries.get((i,j),F(0))
                assert weight==-n[j]*entries.get((j,i),F(0)) and weight>=0
                if weight:edges.append((i,j,weight))
        reconstructed={}
        for i,j,w in edges:
            for u,v in ((i,j),(j,i)):
                reconstructed[u,u]=reconstructed.get((u,u),F(0))+w/n[u]
                reconstructed[u,v]=-w/n[u]
        assert reconstructed==entries
        seams={tuple(row['triangles']) for row in store[name]['seam_projectors']}
        counts={'seam':0,'native_alignment':0}
        for i,j,w in edges:
            if (i,j) in seams:
                assert w==n[i]*n[j]/(n[i]+n[j]);counts['seam']+=1
            else:
                assert n[i]==n[j] and w==n[i]/4;counts['native_alignment']+=1
        assert len(edges)==(24 if name=='proton' else 39)
        assert counts['seam']==(0 if name=='proton' else 21)
        results[name]={'mode_count':m,'metric_weights':list(map(str,n)),
                       'edges':[[i,j,str(w)] for i,j,w in edges],'edge_types':counts,
                       'exact_zero_field_intertwining':True,'complement_retained_dimension':36-m,
                       'exact_controls':exact_field_check(n,edges),
                       'feedback':numerical_feedback(n,edges)}
    report={'verification_passed':True,'reused_law':'research/nima/record-gauge-feedback-loop.md, electric-only specialization',
            'matter_energy':'sum gamma_ij*|a_j-U_ij*a_i|^2',
            'canonical_metric':'i*n_i*dot(a_i)=partial H/partial conjugate(a_i)',
            'current':'J_ij=2*gamma_ij*Im(conjugate(a_j)*U_ij*a_i)',
            'field_law':'dot(A)=beta*E; dot(E)=-J; magnetic coefficient set to zero, no new loop filling assumed',
            'gauss':'B*E-(rho-background), rho_i=n_i*|a_i|^2',
            'carriers':results,'quantum_vacuum_or_mass_derived':False,
            'scope':'Exact weighted adapter on the phase-selected sectors; prior classical matter/link feedback reused. Field phase dynamics outside the selected sectors, magnetic action, physical charge and common vacuum remain unconstructed.',
            'common_empty_vacuum_gate':'At fixed positive-total background, empty matter cannot satisfy Gauss on a closed graph. Changing background between vacuum and particle is not a common-vacuum comparison.',
            'source_sha256':sha256(raw).hexdigest()}
    (BASE/'results/weighted_matter_link_adapter.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({**report,'carriers':{k:{key:value for key,value in v.items() if key not in ('edges','metric_weights')} for k,v in results.items()}},indent=2))


if __name__=='__main__':main()
