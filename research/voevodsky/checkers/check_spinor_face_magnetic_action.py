"""Source face-loop magnetic action and its finite-stiffness preservation test.

Reuses the existing cosine magnetic law on actual tetrahedral face boundaries.
Exact incidence, current, power and constrained-force checks; numerical complete
weighted subflows are secondary reversible/convergence controls.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from itertools import combinations
from cmath import exp
from math import sin, cos, sqrt
import json
from check_spinor_matter_link_adapter import decode, evaluate
from check_electron_tetrahedral_spinor import D, G0, G1, GI, gc, gm, ga, gs, gt, gmm, trace, pos, encode

BASE=Path(__file__).resolve().parents[1]


def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def transpose(a): return list(map(list,zip(*a)))
def mv(a,v): return [sum(x*y for x,y in zip(row,v)) for row in a]
def real(x): return float(x.a)+sqrt(3)*float(x.b) if isinstance(x,D) else float(x)
def complex_value(z): return complex(real(z[0]),real(z[1]))


def numerical(norms,hops,pairs,b,c):
    # Use orthonormal line coordinates; all edge magnitudes equal 1/sqrt(3).
    n=[real(x) for x in norms]
    u0=[complex_value(h)/abs(complex_value(h)) for h in hops]
    gamma=1/sqrt(3); onsite=1-sqrt(3)
    beta,kappa,q=0.6,1.0,-1
    a0=[complex(sqrt(x/2)) for x in n]
    rho0=[abs(z)**2 for z in a0]
    e0=mv(transpose(b),[q*(x-0.25)/4 for x in rho0])
    def gauss(a,e):return [x-q*abs(z)**2 for x,z in zip(mv(b,e),a)]
    original_gauss=gauss(a0,e0)
    def energy(a,A,e):
        matter=onsite*sum(abs(z)**2 for z in a)
        matter+=sum(gamma*abs(a[j]-u*exp(1j*q*phase)*a[i])**2
                    for (i,j),u,phase in zip(pairs,u0,A))
        return matter+beta*sum(x*x for x in e)/2+kappa*sum(1-cos(x) for x in mv(c,A))
    def step(a,A,e,dt):
        def drift(t):
            for k in range(6):A[k]+=beta*e[k]*t
        def magnetic(t):
            force=mv(transpose(c),[kappa*sin(x) for x in mv(c,A)])
            for k in range(6):e[k]-=force[k]*t
        def link(k,t):
            i,j=pairs[k];u=u0[k]*exp(1j*q*A[k])
            old=abs(a[j])**2
            defect=a[j]-u*a[i]
            factor=(exp(-2j*gamma*t)-1)/(2*gamma)
            a[i]+=factor*(-gamma*u.conjugate()*defect)
            a[j]+=factor*gamma*defect
            e[k]+=q*(abs(a[j])**2-old)
        drift(dt/2);magnetic(dt/2)
        for k in range(6):link(k,dt/2)
        for k in reversed(range(6)):link(k,dt/2)
        factor=exp(-1j*onsite*dt)
        for i in range(4):a[i]*=factor
        magnetic(dt/2);drift(dt/2)
    reports=[]
    for dt in (0.01,0.005):
        a=a0[:];A=[0.0]*6;e=e0[:]
        initial=energy(a,A,e);err=0.0;gerr=0.0
        steps=round(0.1/dt)
        for _ in range(steps):
            step(a,A,e,dt)
            err=max(err,abs(energy(a,A,e)-initial))
            gerr=max(gerr,max(abs(x-y) for x,y in zip(gauss(a,e),original_gauss)))
        deviation=max(abs(x) for x in mv(c,A))
        assert deviation>1e-6
        for _ in range(steps):step(a,A,e,-dt)
        reversal=max([abs(x-y) for x,y in zip(a,a0)]+[abs(x) for x in A]+[abs(x-y) for x,y in zip(e,e0)])
        assert reversal<1e-11 and gerr<1e-11
        reports.append({'dt':dt,'maximum_energy_error':err,'maximum_Gauss_error':gerr,
                        'source_face_flux_deviation':deviation,'reversal_error':reversal})
    assert reports[1]['maximum_energy_error']<reports[0]['maximum_energy_error']/3
    return reports


def main():
    path=BASE/'results/electron_tetrahedral_spinor_store.json'
    raw=path.read_bytes();store=json.loads(raw)
    face=[tuple(tuple(decode(z) for z in row) for row in p) for p in store['face_projectors']]
    local=[tuple(p[i][0] for i in range(2)) for p in face]
    norms=[gt(gm(gc(z),z) for z in v)[0] for v in local]
    pairs=list(combinations(range(4),2))
    hops=[gt(gm(gc(zj),zi) for zi,zj in zip(local[i],local[j])) for i,j in pairs]
    b=[[F(0) for _ in pairs] for _ in range(4)]
    for k,(i,j) in enumerate(pairs):b[i][k]=-1;b[j][k]=1
    # Boundary of [0,1,2,3]; all four faces use outward chain orientation.
    oriented=[((1,2,3),1),((0,2,3),-1),((0,1,3),1),((0,1,2),-1)]
    c=[];source_flux=[]
    for (i,j,k),sign in oriented:
        row=[F(0) for _ in pairs]
        for tail,head in ((i,j),(j,k),(k,i)):
            edge=tuple(sorted((tail,head)))
            row[pairs.index(edge)]+=sign*(1 if tail<head else -1)
        c.append(row)
        loop=gs(D(0,3),gc(trace(gmm(gmm(face[i],face[j]),face[k]))))
        if sign==-1:loop=gc(loop)
        assert loop==GI
        source_flux.append(encode(loop))
    assert mm(b,transpose(c))==[[0]*4 for _ in range(4)]
    assert [sum(col) for col in zip(*c)]==[0]*6
    hodge=mm(transpose(b),b)
    curl=mm(transpose(c),c)
    assert [[x+y for x,y in zip(ar,br)] for ar,br in zip(hodge,curl)]==[[4*F(i==j) for j in range(6)] for i in range(6)]
    assert mm(c,transpose(c))==[[4*F(i==j)-1 for j in range(4)] for i in range(4)]
    # Exact nonlinear magnetic force fixtures, including signed matter action.
    kappa,beta=F(1),F(3,5)
    phases=(G1,GI,gs(-1,G1),gs(-1,GI),G1,GI)
    wilson=[]
    for row in c:
        product=G1
        for power,phase in zip(row,phases):
            if power:product=gm(product,phase if power==1 else gc(phase))
        wilson.append(product)
    magnetic_gradient=mv(transpose(c),[kappa*z[1] for z in wilson])
    assert mv(b,magnetic_gradient)==[0]*4
    a=((F(1,3),F(1,5)),(F(-2,7),F(1,4)),(F(3,8),F(-1,6)),(F(1,2),F(2,9)))
    efield=[F(1,7),F(-2,5),F(3,11),F(1,3),F(-1,9),F(2,7)]
    for q in (-1,1):
        signed_phases=phases if q==1 else tuple(gc(z) for z in phases)
        _,current,dr,div=evaluate(a,signed_phases,norms,pairs,hops)
        force=[-q*j-m for j,m in zip(current,magnetic_gradient)]
        assert all(x-q*d==0 for x,d in zip(mv(b,force),dr))
        matter_power=sum(q*j*beta*e for j,e in zip(current,efield))
        electric_power=sum(beta*e*f for e,f in zip(efield,force))
        magnetic_power=sum(m*beta*e for m,e in zip(magnetic_gradient,efield))
        assert matter_power+electric_power+magnetic_power==0
    # Native coherent logical spin e0: coefficients all 1, divided by sqrt(2).
    _,raw_current,dr,div=evaluate((G1,)*4,(G1,)*6,norms,pairs,hops)
    assert dr==div==[0]*4
    current=[x/2 for x in raw_current]
    norm2=sum(x*x for x in current)
    assert norm2==F(1,9)
    assert mv(curl,current)==[4*x for x in current]
    multipliers=[-x/4 for x in mv(c,current)]  # charge +1; flip for -1
    assert mv(transpose(c),multipliers)==[-x for x in current]
    for spin in ((G1,G0),(G0,G1),((F(3,5),F(0)),(F(0),F(4,5))),
                 ((F(3,5),F(0)),(F(4,5),F(0)))):
        coefficients=tuple(gs(D(1)/norm,ga(gm(p[0][0],spin[0]),gm(p[0][1],spin[1])))
                           for p,norm in zip(face,norms))
        assert sum(norm*gm(gc(z),z)[0] for norm,z in zip(norms,coefficients))==2
        energy,jj,dd,bb=evaluate(coefficients,(G1,)*6,norms,pairs,hops)
        assert energy==0 and dd==bb==[0]*4
        assert sum(j*j/4 for j in jj)==F(1,9)
    # Source projector geometry makes the circulation norm independent of spin.
    normals=[[D(F(a),F(b)) for a,b in row] for row in store['normals']]
    cross=lambda x,y:(x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
    vectors=[cross(normals[i],normals[j]) for i,j in pairs]
    assert [[sum(v[i]*v[j] for v in vectors) for j in range(3)] for i in range(3)]==[[F(16,9) if i==j else 0 for j in range(3)] for i in range(3)]
    flat_threshold=(D(0,1)-1+beta/120)/4
    assert pos(flat_threshold)
    result={
        'verification_passed':True,'source_sha256':sha256(raw).hexdigest(),
        'edges':pairs,'oriented_faces':[{'vertices':list(f),'orientation':s} for f,s in oriented],
        'face_edge_incidence':[[int(x) for x in row] for row in c],
        'source_oriented_Wilson_phases':source_flux,
        'boundary_of_boundary_zero':True,'independent_face_constraints':3,
        'magnetic_law':'kappa*sum_f[1-Re(conj(Omega_source,f)*Omega_total,f)]=kappa*sum_f[1-cos((C*A)_f)]',
        'source_magnetic_energy':'0','fully_cancelled_source_flux_magnetic_energy':'4*kappa',
        'complete_field_force':'E_dot=-q*J_matter-kappa*C^T*sin(C*A)',
        'signed_Gauss_and_total_power_exact':True,
        'coherent_spinor_current_squared_norm':'1/9 for every pure logical spin',
        'finite_stiffness_preserves_exact_source_flux':False,
        'finite_stiffness_falsifier':'At A=0 the magnetic gradient is zero but q*J !=0; along delta_A=-q*J the energy derivative is -1/9 for every finite kappa.',
        'stiff_field_frozen_matter_leading_shift':'delta_A=-q*J/(4*kappa); energy lowering=-1/(72*kappa)+O(kappa^-2), not a full matter-relaxed ground expansion',
        'flat_rival_threshold_at_beta_3_over_5':real(flat_threshold),
        'threshold_scope':'Only compares coherent source and fully flattened rival; does not certify global preservation.',
        'hard_flux_sector':{'constraint':'C*A=0 mod 2*pi',
                            'native_kinetic_doublet_retained_up_to_gauge':True,
                            'coherent_circulation_multiplier':'lambda=-q*C*J/4',
                            'exact_reaction_force_cancels_circulation':True,
                            'fully_coupled_electric_density_relaxation_still_to_test':True},
        'numerical_feedback':numerical(norms,hops,pairs,b,c),
        'numerical_background_scope':'Closed four-vertex control with fixed compensating background; not used for the common exterior vacuum comparison.',
        'next_gate':'Compare the hard source-flux sector or construct its finite physical stiffness; then relax charged density with that flux retained. Do not claim a finite cosine penalty exactly protects the source doublet.',
    }
    out=BASE/'results/spinor_face_magnetic_action.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
