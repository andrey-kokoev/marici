"""Collective spectrum on the retained 36-dimensional carriers; no new qubits.

Exact invariant-sector identities and a rational six-mode characteristic
polynomial certify the reduction. Jacobi eigenvalues/vectors are explicitly
numerical diagnostics with residual controls, not exact mass predictions.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from math import sqrt, copysign
import json
from check_seam_occupation_energy import matrix
from check_constraint_energy_accounting import identity, plus, times, compose, adjoint, trace
from check_coupled_six_piece_belt import R, Z, ONE, mul, conj, norm, scale
from check_belt_three_by_twelve import decode

BASE = Path(__file__).resolve().parents[1]


def jacobi(original):
    n = len(original)
    a = [row[:] for row in original]
    v = [[float(i==j) for j in range(n)] for i in range(n)]
    for iteration in range(10000):
        p,q = max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda ij:abs(a[ij[0]][ij[1]]))
        if abs(a[p][q])<1e-14:
            break
        tau = (a[q][q]-a[p][p])/(2*a[p][q])
        t = copysign(1/(abs(tau)+sqrt(1+tau*tau)),tau)
        c = 1/sqrt(1+t*t);s=t*c
        a[p][p] -= t*a[p][q];a[q][q] += t*a[p][q]
        a[p][q]=a[q][p]=0.
        for k in range(n):
            if k not in (p,q):
                x,y=a[k][p],a[k][q]
                a[k][p]=a[p][k]=c*x-s*y
                a[k][q]=a[q][k]=s*x+c*y
            x,y=v[k][p],v[k][q]
            v[k][p],v[k][q]=c*x-s*y,s*x+c*y
    else:
        raise AssertionError('Jacobi iteration did not converge')
    order=sorted(range(n),key=lambda j:a[j][j])
    values=[a[j][j] for j in order]
    vectors=[[v[i][j] for i in range(n)] for j in order]
    residual=max(abs(sum(original[i][k]*vec[k] for k in range(n))-lam*vec[i])
                 for lam,vec in zip(values,vectors) for i in range(n))
    orthogonality=max(abs(sum(vectors[i][k]*vectors[j][k] for k in range(n))-int(i==j))
                      for i in range(n) for j in range(n))
    assert residual<1e-11 and orthogonality<1e-12
    return values,vectors,residual,orthogonality


def characteristic(a):
    n=len(a)
    B=[[F(i==j) for j in range(n)] for i in range(n)]
    coefficients=[F(1)]
    for k in range(1,n+1):
        C=[[sum(a[i][r]*B[r][j] for r in range(n)) for j in range(n)] for i in range(n)]
        coefficient=-sum(C[i][i] for i in range(n))/k
        coefficients.append(coefficient)
        B=[[C[i][j]+coefficient*int(i==j) for j in range(n)] for i in range(n)]
    assert all(x==0 for row in B for x in row)  # exact Cayley-Hamilton
    return coefficients


def polynomial_product(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def sturm_count(coefficients,left,right):
    def trim(p):
        while p and p[0]==0:p=p[1:]
        return p
    sequence=[coefficients,[x*(len(coefficients)-1-i) for i,x in enumerate(coefficients[:-1])]]
    while sequence[-1]:
        remainder=sequence[-2][:];divisor=sequence[-1]
        while remainder and len(remainder)>=len(divisor):
            q=remainder[0]/divisor[0]
            for i,x in enumerate(divisor):remainder[i]-=q*x
            remainder=trim(remainder)
        if not remainder:break
        sequence.append([-x for x in remainder])
    def variations(x):
        signs=[]
        for p in sequence:
            value=F(0)
            for c in p:value=value*x+c
            if value:signs.append(1 if value>0 else -1)
        return sum(a!=b for a,b in zip(signs,signs[1:]))
    return variations(left)-variations(right)


def main():
    path=BASE/'results/native_operation_energy_lift_store.json'
    raw=path.read_bytes();store=json.loads(raw)['carriers']
    source_path=BASE/'results/belt_three_by_twelve_store.json'
    source_raw=source_path.read_bytes();source=json.loads(source_raw)
    belt=store['belt'];d=tuple(map(F,belt['metric_denominators']))
    z=[decode(c['selected_numerator']) for c in source['coordinates']]
    H=times(F(1,4),matrix(belt['entries']))
    Hnative=times(F(1,4),matrix(belt['native_energy_entries']))
    K=plus(*(matrix(row['entries']) for row in belt['seam_projectors']))
    T={(((s+1)%3)*12+j,s*12+j):ONE for s in range(3) for j in range(12)}
    G=times(F(1,3),plus(identity(36),T,compose(T,T)))
    alignment=times(F(3,4),plus(identity(36),times(-1,G)))
    phase=plus(Hnative,times(-1,alignment))
    assert H==plus(phase,alignment,K)
    norms=[];Q={};V={}
    for t in range(18):
        ns=sum((norm(z[2*t+i])/d[2*t+i] for i in range(2)),R())
        assert ns.b==0 and ns.a>0
        norms.append(ns.a)
        for i in range(2):
            V[2*t+i,t%6]=z[2*t+i]
            for j in range(2):
                value=scale(1/(ns*d[2*t+j]),mul(z[2*t+i],conj(z[2*t+j])))
                if value!=Z:Q[2*t+i,2*t+j]=value
    assert norms==norms[:6]*3
    assert z==z[:12]*3 and d==d[:12]*3
    assert compose(Q,Q)==Q and trace(Q,36)==18
    assert compose(phase,Q)=={} and compose(K,Q)==K and compose(Q,K)==K
    assert compose(Q,G)==compose(G,Q)
    assert compose(H,G)==compose(G,H)
    decoder={(j,i):scale(1/(3*norms[j]*d[i]),conj(v)) for (i,j),v in V.items()}
    assert compose(decoder,V)==identity(6)
    aligned=compose(V,decoder)
    assert aligned==compose(Q,G) and trace(aligned,36)==6
    reduced=compose(compose(decoder,H),V)
    assert compose(H,V)==compose(V,reduced)  # exact no-leakage identity
    assert compose(H,aligned)==compose(aligned,H)
    assert adjoint(reduced,tuple(1/n for n in norms[:6]))==reduced
    a=[[F(0) for _ in range(6)] for _ in range(6)]
    for (i,j),v in reduced.items():
        assert v[1]==0 and v[0].b==0
        a[i][j]=v[0].a
    assert all(sum(row)==0 for row in a)
    # Recover this matrix directly as the normalized, weighted seam Laplacian.
    predicted=[[F(0) for _ in range(6)] for _ in range(6)]
    edges=[]
    for row in belt['seam_projectors']:
        i,j=row['triangles']
        if j>=6:continue
        edges.append((i,j))
        for u,v in ((i,j),(j,i)):
            w=norms[v]/(norms[u]+norms[v])
            predicted[u][u]+=w;predicted[u][v]-=w
    assert a==predicted and len(edges)==7
    coefficients=characteristic(a)
    assert coefficients[-1]==0 and coefficients[-2]!=0  # exactly one zero mode
    assert all(a[(i+3)%6][(j+3)%6]==a[i][j] for i in range(6) for j in range(6))
    even=[[a[i][j]+a[i][j+3] for j in range(3)] for i in range(3)]
    odd=[[a[i][j]-a[i][j+3] for j in range(3)] for i in range(3)]
    assert all(odd[i][j]-even[i][j]==int(i==j==0) for i in range(3) for j in range(3))
    even_polynomial,odd_polynomial=characteristic(even),characteristic(odd)
    even_roots=[F(0),F(4485,3292),F(5391,3292)]
    expected=[F(1)]
    for root in even_roots:expected=polynomial_product(expected,[F(1),-root])
    assert even_polynomial==expected
    assert polynomial_product(even_polynomial,odd_polynomial)==coefficients
    soft_interval=[F('0.172938631059'),F('0.172938631060')]
    assert sturm_count(odd_polynomial,*soft_interval)==1
    assert sturm_count(odd_polynomial,F(0),F(1))==1
    assert sturm_count(odd_polynomial,F(1),F(3))==2
    symmetric=[[float(a[i][j])*sqrt(float(norms[i]/norms[j])) for j in range(6)] for i in range(6)]
    assert max(abs(symmetric[i][j]-symmetric[j][i]) for i in range(6) for j in range(6))<1e-12
    values,vectors,residual,orthogonality=jacobi(symmetric)
    assert abs(values[0])<1e-12 and values[1]>0
    assert all(abs(vectors[1][i]+vectors[1][i+3])<1e-12 for i in range(3))
    # The phase-orthogonal triangle modes form the other 18 carrier dimensions.
    beta=[];expected_phase={}
    for t in range(18):
        indices=[2*t,2*t+1]
        b=sum((phase.get((i,i),Z)[0].a for i in indices),F(0))
        beta.append(b)
        block_I={(i,i):ONE for i in indices}
        block_Q={(i,j):v for (i,j),v in Q.items() if i in indices and j in indices}
        expected_phase=plus(expected_phase,times(b,plus(block_I,times(-1,block_Q))))
    assert phase==expected_phase and beta==beta[:6]*3
    belt_spectrum=[]
    for family,roots in [('selected_phase_collective',values),('orthogonal_phase',list(map(float,beta[:6])))]:
        for j,value in enumerate(roots):
            for shift,multiplicity in ((0.,1),(.75,2)):
                belt_spectrum.append({'family':family,'mode':j,'energy':value+shift,'multiplicity':multiplicity})
    assert sum(r['multiplicity'] for r in belt_spectrum)==36
    assert abs(sum(r['energy']*r['multiplicity'] for r in belt_spectrum)-float(trace(H,36)))<1e-10

    # Proton: recover the local phase operator and the native A4 alignment
    # operator, rather than postulating their tensor-product multiplicities.
    proton=store['proton'];Hp=times(F(1,4),matrix(proton['entries']))
    B=plus({(i,j):v for (i,j),v in Hp.items() if i//3==j//3},times(-1,identity(36)))
    Aalign=plus(Hp,times(-1,B))
    assert compose(B,Aalign)==compose(Aalign,B)
    B2=compose(B,B)
    t,p=F(29,6),F(45,16)
    assert plus(compose(B2,B),times(-t,B2),times(p,B))=={}
    roots=[F(0),F(1,2),F(1),F(3,2)];multiplicities=[1,3,3,5]
    annihilator=identity(36)
    for root in roots:
        annihilator=compose(annihilator,plus(Aalign,times(-root,identity(36))))
    assert annihilator=={}
    power=identity(36)
    for k in range(4):
        moment=sum(m*r**k for r,m in zip(roots,multiplicities))
        assert trace(power,36)==3*moment
        assert trace(compose(B,power),36)==t*moment
        assert trace(compose(B2,power),36)==(t*t-2*p)*moment
        power=compose(power,Aalign)
    # Commutation, annihilating polynomials and joint moments determine the
    # joint multiplicities, hence this full spectrum, without a floating rank.
    local=[0.,(29-2*sqrt(109))/12,(29+2*sqrt(109))/12]
    proton_spectrum=[{'local_phase_mode':j,'alignment_energy':str(r),'energy':b+float(r),'multiplicity':m}
                     for j,b in enumerate(local) for r,m in zip(roots,multiplicities)]
    assert sum(row['multiplicity'] for row in proton_spectrum)==36
    report={
        'verification_passed':True,'added_record_qubits':0,'carrier_dimensions':{'proton':36,'belt':36},
        'energy_unit':'pi*hbar/tau, using the previously declared native-operation defect Hamiltonian',
        'belt_aligned_phase_sector_dimension':6,'belt_aligned_phase_excited_modes':5,
        'belt_aligned_sector_exactly_closed':True,
        'belt_modal_norms':list(map(str,norms[:6])),
        'belt_reduced_matrix':[[str(x) for x in row] for row in a],
        'belt_reduced_characteristic_descending':list(map(str,coefficients)),
        'belt_face_even_energies_exact':list(map(str,even_roots)),
        'belt_face_odd_characteristic_descending':list(map(str,odd_polynomial)),
        'belt_soft_mode_exact_isolating_interval':list(map(str,soft_interval)),
        'belt_soft_mode_face_exchange_parity':-1,
        'belt_collective_eigenvalues_numerical':values,
        'belt_collective_vectors_in_sqrt_norm_coordinates_numerical':vectors,
        'numerical_residual':residual,'numerical_orthogonality_error':orthogonality,
        'belt_orthogonal_phase_energies_exact':list(map(str,beta[:6])),
        'belt_full_spectrum':belt_spectrum,'proton_full_spectrum':proton_spectrum,
        'proton_local_phase_energies':'0, (29-2*sqrt(109))/12, (29+2*sqrt(109))/12',
        'proton_alignment_energies_and_multiplicities':[[str(r),m] for r,m in zip(roots,multiplicities)],
        'lowest_positive_excitation':{'proton':min(r['energy'] for r in proton_spectrum if r['energy']>1e-10),
                                     'belt':min(r['energy'] for r in belt_spectrum if r['energy']>1e-10)},
        'ground_energies':{'proton':0,'belt':0},
        'interpretation':'These are eigenmodes of the existing finite carriers, not independent oscillator factors. No zero-point sum, electron identification or neutron mass follows without an additional physical construction.',
        'source_sha256':{'energy_store':sha256(raw).hexdigest(),'belt_coordinates':sha256(source_raw).hexdigest()}}
    (BASE/'results/collective_carrier_spectrum.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ('belt_full_spectrum','proton_full_spectrum','belt_collective_vectors_in_sqrt_norm_coordinates_numerical')},indent=2))


if __name__=='__main__':
    main()
