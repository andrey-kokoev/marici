"""Source-constraint spectral reduction, compared with the 1836 realization.

Forward-realization obligation: construct positive operators from the existing
triangle cycles and shared-edge transports, without taking the old projectors
as inputs. The chiral sector and regular tetrahedral realization remain declared
source data. The complex constraint operator extends ordinary scalar graph LRG.
"""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
import json
from math import exp,sqrt
from check_twelve_triangle_positive_geometry import (
    POINTS,LABELS,C,I,ONE,ZERO,OMEGA,mean,transpose,mm,mv,inv,det,
    rotation,projector,zmv,zmm,zreal,zadd,zmul,zconj,zscale,znorm,boundary,
)
from check_twenty_four_triangle_shared_seed import A,B,closure
from check_collective_four_state_identity import rank

ROOT=Path(__file__).resolve().parents[1]

def eye(n): return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
def add(a,b): return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def scale(a,c): return tuple(tuple(c*x for x in r) for r in a)
def za(a,b): return tuple(tuple(zadd(x,y) for x,y in zip(r,s)) for r,s in zip(a,b))
def zs(a,c): return tuple(tuple(zscale(x,c) for x in r) for r in a)
def dagger(a): return tuple(tuple(zconj(z) for z in r) for r in transpose(a))
def trace(a): return sum(a[i][i] for i in range(len(a)))
def ztrace(a):
    value=ZERO
    for i in range(len(a)): value=zadd(value,a[i][i])
    assert value[1]==0
    return value[0]
def count(a): return sum(z!=ZERO for row in a for z in row)

def characteristic(a):
    n=len(a);unit=eye(n);b=unit;coeff=[F(1)]
    for k in range(1,n+1):
        ab=mm(a,b);c=-trace(ab)/k;coeff.append(c);b=add(ab,scale(unit,c))
    assert b==scale(unit,0)
    return coeff

def divide(poly,root):
    q=[poly[0]]
    for c in poly[1:]: q.append(c+root*q[-1])
    return q[:-1],q[-1]

def spectrum(a):
    p=characteristic(a);found={}
    # All roots of this particular degree-three graph lie in [0,6].
    for root in range(7):
        while len(p)>1:
            q,r=divide(p,F(root))
            if r: break
            found[root]=found.get(root,0)+1;p=q
    assert p==[1],'integer-root fixture exhausted; do not guess remaining roots'
    return found

def source():
    points=dict(POINTS);rows=[]
    for p in sorted(closure((A,B))):
        a,b,c=[LABELS[p[i]] for i in range(3)]
        f='F_'+''.join(sorted((a,b,c)));points[f]=mean([POINTS[k] for k in (a,b,c)])
        rows.append((a+b,(f,a,b),rotation(p)))
    triangles=[r[1] for r in rows]
    assert len(rows)==12 and not boundary(triangles)
    assert {r[0] for r in rows}=={a+b for a in LABELS for b in LABELS if a!=b}
    X=[transpose(tuple(points[k] for k in t)) for _,t,_ in rows]
    assert all(det(x)/6==F(2,9) for x in X)
    assert all(x==mm(r[2],X[0]) for x,r in zip(X,rows))
    assert sum(det(x)/6 for x in X)==F(8,3)
    interfaces=defaultdict(list)
    for i,t in enumerate(triangles):
        for a,b in zip(t,t[1:]+t[:1]): interfaces[tuple(sorted((a,b)))].append(i)
    L=[[F(0)]*12 for _ in rows]
    for ends in interfaces.values():
        assert len(ends)==2;i,j=ends
        L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
    assert len(interfaces)==18 and all(L[i][i]==3 for i in range(12))
    return rows,X,tuple(tuple(r) for r in L)

def local_ground(X,phase):
    cyclic=mm(mm(X,C),inv(X))
    D=tuple(tuple(zadd((cyclic[i][j],F(0)),zscale(phase,-F(i==j))) for j in range(3)) for i in range(3))
    H=zmm(dagger(D),D);H2=zmm(H,H)
    t=ztrace(H);s=(t*t-ztrace(H2))/2
    assert t>0 and s>0
    # Characteristic polynomial lambda*(lambda^2-t*lambda+s).
    assert za(za(zmm(H2,H),zs(H2,-t)),zs(H,s))==tuple((ZERO,)*3 for _ in range(3))
    P=za(za(zreal(I),zs(H,-t/s)),zs(H2,1/s))
    assert zmm(P,P)==P and ztrace(P)==1 and dagger(P)==P
    assert zmm(H,P)==tuple((ZERO,)*3 for _ in range(3))
    return H,P,t,s

def lift(blocks):
    return tuple(tuple(blocks[i//3][j//3][i%3][j%3] for j in range(36)) for i in range(36))

def arrows(matrices):
    result=[]
    for stage,matrix in enumerate(matrices):
        nxt=(stage+1)%len(matrices)
        result.append({((stage,i),(nxt,j)):matrix[j][i]
                       for i in range(len(matrix[0])) for j in range(len(matrix)) if matrix[j][i]!=ZERO})
    return result

def phase_gauge_positive(stages,values):
    # Each edge weight = positive real scalar * endpoint-amplitude ratio.
    # Consequently every closed walk has strictly positive real weight.
    for stage in stages:
        for (a,b),w in stage.items():
            value=zmul(zmul(w,values[a]),zconj(values[b]))
            assert value[1]==0 and value[0]>0

def strongly_connected(stages):
    graph=defaultdict(set)
    for stage in stages:
        for a,b in stage:graph[a].add(b)
    start=next(iter(graph))
    for reverse in (False,True):
        adj=defaultdict(set)
        for a,ends in graph.items():
            for b in ends:adj[b if reverse else a].add(a if reverse else b)
        seen={start};front=[start]
        while front:
            for v in adj[front.pop()]-seen:seen.add(v);front.append(v)
        assert seen==set(graph)


def heat_peaks(energies):
    """Numerical scouting only; exact operator identities do not use these values."""
    def statistics(tau):
        weights=[exp(-tau*e) for e in energies];Z=sum(weights)
        mean=sum(w*e for w,e in zip(weights,energies))/Z
        variance=sum(w*(e-mean)**2 for w,e in zip(weights,energies))/Z
        third=sum(w*(e-mean)**3 for w,e in zip(weights,energies))/Z
        C=tau*tau*variance
        return C,2*C-tau**3*third
    grid=[10**(-4+k/100) for k in range(801)];peaks=[]
    for lo,hi in zip(grid,grid[1:]):
        if statistics(lo)[1]>0 and statistics(hi)[1]<0:
            for _ in range(60):
                mid=sqrt(lo*hi)
                if statistics(mid)[1]>0:lo=mid
                else:hi=mid
            tau=sqrt(lo*hi);C,_=statistics(tau)
            if C<1e-8:continue
            peaks.append({'tau_approx':tau,'specific_heat_approx':C,'cutoff_approx':1/tau,
                          'retained_modes':sum(e<1/tau for e in energies),
                          'distance_to_nearest_cutoff_eigenvalue':min(abs(e-1/tau) for e in energies)})
    return {'method':'C=tau^2 Var(lambda); derivative sign changes on 801 log-spaced samples, followed by bisection.',
            'domain':'1e-4 <= tau <= 1e4; numerical scouting, not a completeness certificate for extrema.',
            'peaks':peaks}


def iterated_lrg(energies):
    stages=[];current=list(energies)
    for _ in range(8):
        if len(current)==1:break
        peaks=heat_peaks(current)['peaks']
        assert peaks,'no detected peak; no cutoff is silently supplied'
        peak=peaks[0];tau=peak['tau_approx'];cut=1/tau
        retained=[e for e in current if e<cut]
        assert 0<len(retained)<len(current)
        stages.append({'input_modes':len(current),'output_modes':len(retained),
                       'tau_approx':tau,'cutoff_approx':cut,
                       'retained_eigenvalues_before_rescaling':retained})
        current=[tau*e for e in retained]
    assert len(current)==1
    return stages


def main():
    rows,X,L=source();spec=spectrum(L)
    assert spec=={0:1,1:3,3:2,4:3,5:3}
    Gscalar=eye(12)
    for lam in spec:
        if lam:Gscalar=mm(Gscalar,add(eye(12),scale(L,-F(1,lam))))
    assert mm(Gscalar,Gscalar)==Gscalar and mm(L,Gscalar)==scale(L,0)
    assert Gscalar==tuple((F(1,12),)*12 for _ in rows)
    # Derive a labelled four-state slow realization, rather than equating rank
    # four with a tetrahedron. A row is tied to the two complementary vertices.
    complementary=[]
    for name,(face,a,b),r in rows:
        c=next(k for k in face[2:] if k not in (a,b))
        d=next(k for k in LABELS if k not in face[2:])
        complementary.append((d,c))
    M=tuple(tuple(F(k==d) for k in LABELS) for d,c in complementary)
    V=tuple(tuple(F(k==c) for k in LABELS) for d,c in complementary)
    ones=tuple((F(1),)*4 for _ in rows)
    assert mm(L,M)==add(M,scale(V,-1))
    assert mm(L,V)==add(scale(V,4),scale(ones,-1))
    # L(aM+bV)=(aM+bV)H and unit row sums force a=3b and a+b=1.
    E=add(scale(M,F(3,4)),scale(V,F(1,4)))
    Q4=tuple((F(1,4),)*4 for _ in range(4));H4=add(eye(4),scale(Q4,-1))
    assert rank(E)==4 and mm(L,E)==mm(E,H4)
    gram_inverse=add(scale(H4,F(2,3)),scale(Q4,F(1,3)))
    readout=mm(gram_inverse,transpose(E))
    assert mm(readout,E)==eye(4) and mm(mm(readout,L),E)==H4
    eig1=eye(12)
    for lam in spec:
        if lam!=1:eig1=mm(eig1,scale(add(L,scale(eye(12),-lam)),F(1,1-lam)))
    assert mm(E,readout)==add(Gscalar,eig1)
    R=[r[2] for r in rows]
    assert all(mm(transpose(r),r)==I and det(r)==1 for r in R)
    G=lift([[zreal(scale(mm(r,transpose(s)),Gscalar[i][j])) for j,s in enumerate(R)] for i,r in enumerate(R)])
    Htransport=lift([[zreal(scale(mm(r,transpose(s)),L[i][j])) for j,s in enumerate(R)] for i,r in enumerate(R)])
    assert zmm(G,G)==G and ztrace(G)==3
    graph_energies=[float(lam) for lam,multiplicity in spec.items() for _ in range(multiplicity)]
    scans={'ordinary_shared_edge_graph':heat_peaks(graph_energies)}
    flows={}
    phases=[]
    for name,phase in [('oriented',OMEGA),('conjugate',zconj(OMEGA)),('unit',ONE)]:
        local=[local_ground(x,phase) for x in X]
        assert len({(t,s) for h,p,t,s in local})==1
        t,s=local[0][2:]
        empty=tuple((ZERO,)*3 for _ in range(3))
        Hlocal=lift([[local[i][0] if i==j else empty for j in range(12)] for i in range(12)])
        P=lift([[local[i][1] if i==j else empty for j in range(12)] for i in range(12)])
        assert zmm(Hlocal,Htransport)==zmm(Htransport,Hlocal)
        N=zmm(G,P)
        assert zmm(P,G)==N and zmm(N,N)==N and ztrace(N)==1
        assert zmm(za(Hlocal,Htransport),N)==tuple((ZERO,)*36 for _ in range(36))
        # Comparison with the old assembled mode occurs only after spectral construction.
        coeff=(ONE,phase,zmul(phase,phase))
        u=tuple(z for x in X for z in zmv(x,coeff))
        assert all(z!=ZERO for z in u)
        assert N==projector(u)
        counts=[count(P),count(G),count(N)]
        assert counts==[108,432,1296]
        ordinary=arrows((P,G,N));assert [len(a) for a in ordinary]==counts
        values={(stage,i):u[i] for stage in range(3) for i in range(36)}
        phase_gauge_positive(ordinary,values);strongly_connected(ordinary)
        # Same exact collective return using identity feedback, in the same fine basis.
        shortcut=arrows((P,G,zreal(eye(36))))
        assert sum(map(len,shortcut))==576
        phase_gauge_positive(shortcut,values);strongly_connected(shortcut)
        # Literal coarse scalar, followed by its lift. No dense feedback edges.
        norm=sum(znorm(z) for z in u)
        coarse_lift=tuple(N[i][0] for i in range(36))
        assert N[0][0][1]==0 and N[0][0][0]>0
        contract=(tuple(zscale(zconj(z),1/N[0][0][0]) for z in coarse_lift),)
        expand=tuple((z,) for z in coarse_lift)
        assert zmm(expand,contract)==N
        factorized=arrows((P,G,contract,expand))
        assert [len(a) for a in factorized]==[108,432,36,36]
        factor_values={(stage,i):coarse_lift[i] for stage in range(3) for i in range(36)}
        factor_values[3,0]=ONE
        phase_gauge_positive(factorized,factor_values);strongly_connected(factorized)
        # A three-step identity-feedback return also equals N at every stage.
        assert zmm(N,G)==N and zmm(P,N)==N
        # The low local eigenvalue is the smaller root of x^2-t*x+s.
        def below_low(x):return x<t/2 and x*x-t*x+s>0
        multiplier=next(m for m in range(1,100) if below_low(F(max(spec),m)))
        cutoff=next(F(k,4) for k in range(4*max(spec)+1,4*max(spec)+100)
                    if below_low(F(k,4*multiplier)))
        if name=='oriented':
            fullE=tuple(tuple(zscale(u[i],x) for x in E[i//3]) for i in range(36))
            assert zmm(za(Hlocal,Htransport),fullE)==zmm(fullE,zreal(H4))
            local_energies=[0.0,(float(t)-sqrt(float(t*t-4*s)))/2,(float(t)+sqrt(float(t*t-4*s)))/2]
            for strength in (1,multiplier):
                energies=[g+strength*l for g in graph_energies for l in local_energies]
                scans['phase_constraint_strength_'+str(strength)]=heat_peaks(energies)
                flows['phase_constraint_strength_'+str(strength)]=iterated_lrg(energies)
        phases.append({'sector':name,'local_nonzero_eigenvalue_polynomial':[str(F(1)),str(-t),str(s)],
                       'local_first_band_separation_at_unit_strength':below_low(F(max(spec))),
                       'smallest_integer_local_strength_for_separation':multiplier,
                       'certified_cutoff_with_that_strength':str(cutoff),
                       'projector_ranks':[12,3,1],'projector_supports':counts,
                       'dense_three_stage_count':sum(counts),'identity_feedback_count':576,
                       'coarse_factorized_count':612,'assembled_squared_norm':str(norm)})
    assert phases[0]['local_nonzero_eigenvalue_polynomial']==['1','-58/3','45']
    assert phases[0]['smallest_integer_local_strength_for_separation']==2
    assert phases[0]['local_first_band_separation_at_unit_strength'] is False
    # Ordinary triangle diffusion does not select a chiral branch.
    plain=add(scale(I,2),scale(add(C,transpose(C)),-1))
    v=(ONE,OMEGA,zmul(OMEGA,OMEGA))
    assert zmv(plain,(ONE,)*3)==(ZERO,)*3
    assert zmv(plain,v)==tuple(zscale(z,3) for z in v)
    assert [step['output_modes'] for step in flows['phase_constraint_strength_1']]==[4,1]
    report={'checks_passed':True,'classification':'spectral_recovery_of_existing_projectors_not_a_unique_1836_derivation',
            'source':{'input_cycles':['ABC','ADB'],'agents':12,'shared_edges':18,'scalar_laplacian_spectrum':spec,
                      'geometry':'Inherited regular tetrahedral realization; twelve positive cones of volume 2/9. Coordinates and frames are retained source records, not inferred from a mode count.',
                      'coefficient_field':'Q(i*sqrt(3))','resolution_parameter':'Spectral/diffusion resolution, no physical-time interpretation supplied.'},
            'construction':{'local':'D_g = X_g C X_g^-1 - sigma I; H_local = blockdiag(D_g^dagger D_g).',
                            'alignment':'Sum squared shared-edge differences psi_g - R_g R_h^T psi_h, one term per geometric edge.',
                            'spectral_method':'Exact characteristic polynomials and zero-eigenvalue projectors; old projectors are comparison targets only.',
                            'joint':'The two positive operators commute. Their common kernel has dimension one.',
                            'LRG_density_limits':'Local density tends to P/12, alignment density to G/3, and joint density to N. Multiplying by kernel ranks gives the amplitude-preserving projectors.',
                            'coarse_laplacian':'Zero on the one-dimensional retained kernel; N is its lifted identity, not the coarse Laplacian.'},
            'sectors':phases,'specific_heat_scans':scans,'iterated_peak_selected_LRG':flows,
            'four_state_slow_realization':{
                'fine_to_complementary_pair':{row[0]:list(pair) for row,pair in zip(rows,complementary)},
                'embedding':'fine_ab = (3/4) q_d + (1/4) q_c, where c completes the oriented face and d is opposite it.',
                'coarse_operator':[[str(x) for x in row] for row in H4],
                'geometry_scope':'Exact weighted K4 incidence on four source-labelled records; this is not a new spatial realization from eigenvalue multiplicity alone.',
                'identities':['L E = E H4','R E = I4','R L E = H4','E R = spectral projector onto eigenvalues 0 and 1'],
                'normalization':'H4 is one quarter of the unit-edge K4 Laplacian; an LRG step additionally multiplies it by its selected resolution.'},
            'ledger_boundary':'Counts are nonzero entries of compiled amplitude maps in the inherited fine-coordinate basis. They do not include the cost of constructing the supplied geometry, frames, or spectral coefficients.',
            'falsifiers':{'ordinary_triangle_LRG':'Ground vector is constant; both chiral modes have eigenvalue 3.',
                          'unit_strength_hierarchy':'Oriented local excitation starts below the top of the alignment band; the local twelve-dimensional image is not an isolated low-energy band.',
                          'unique_1836':'576-arrow identity feedback and 612-arrow scalar factorization yield exactly the same collective return, with positive closed walks and no change to the geometric source records.',
                          'chirality_from_count':'All three cyclic sectors give the same 108+432+1296 support count.'},
            'cycle_scope':{'1836':'Three interfaces, dense one-step collective feedback.',
                           '576':'Three interfaces, identity feedback; not all arrows lie on length-three cycles. Strong connectivity and phase-gauge positivity certify positive closed walks.',
                           '612':'Four interfaces including one scalar coarse port; contraction and lift replace dense feedback.'},
            'not_derived':['a source law requiring one chiral sector','relative constraint strengths selecting the local-first hierarchy',
                           'a rule requiring expanded dense feedback as a separate primitive stage','geometric construction cost from raw pair labels alone','physical mass or charge']}
    path=ROOT/'results/lrg-1836.json';path.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: peak-selected phase-conditioned LRG runs 36 -> 4 -> 1; exact labelled four-state operator is K4 Laplacian / 4.')
    print('PASS: independent source-constraint projectors have supports 108,432,1296; these are not the successive peak-selected cutoffs.')
    print('OBSTRUCTIONS: ordinary LRG does not select chirality; unit-strength coupled operator lacks the claimed local-first band separation.')
    print('COUNTEREXAMPLES: the same collective return has 576-arrow identity feedback or 612-arrow factorized feedback. 1836 is the expanded three-stage realization, not an LRG invariant.')

if __name__=='__main__':main()
