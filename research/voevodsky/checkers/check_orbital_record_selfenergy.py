"""Distinct orbital-record scalar three-object vertex and its self-energy.
Antisymmetric internal and orbital factors form a symmetric whole-object state.
Exact exterior-power moments and rational continuum box bounds.
"""
from fractions import Fraction as Q
from itertools import combinations,permutations
from math import comb
from pathlib import Path
from hashlib import sha256
import json
from check_multiobject_orbital_selfenergy import matvec,dot,positive_definite,solve,enclose_g
from check_multiobject_onband import pi_bounds,radius_bounds,root_bounds,SCALE,Interval
from check_typed_spin_channels import vector_norm,exchange,tensor_generator,kron,eye,decode,trace
from check_pentachoron_spin_interfaces import A,pauli,scale,CI,mm,add

BASE=Path(__file__).resolve().parents[1]

def exterior_model(L):
    labels=list(combinations(range(L),3));index={v:i for i,v in enumerate(labels)}
    H=[[Q(6 if i==j else 0) for j in range(len(labels))] for i in range(len(labels))]
    for j,source in enumerate(labels):
        for slot,x in enumerate(source):
            for y in (x-1,x+1):
                if y<0 or y>=L or y in source:continue
                target=list(source);target[slot]=y
                # Nearest-neighbor hops cannot cross an occupied position.
                assert target==sorted(target)
                H[index[tuple(target)]][j]-=1
    e=[Q(v==(0,1,2)) for v in labels]
    return labels,H,e

def egf_product(a,b,N):
    return [sum(comb(n,j)*a[j]*b[n-j] for j in range(n+1)) for n in range(N+1)]
def exterior_moments(N):
    # Entries are the moments <a|h^n|b>, a,b=0,1,2. Differentiate
    # det(<a|exp(t h)|b>): the Slater endpoint's exact generating function.
    entries={}
    for b in range(3):
        v=[0]*(N+4);v[b]=1
        for n in range(N+1):
            for a in range(3):entries.setdefault((a,b),[]).append(v[a])
            v=[2*v[j]-(v[j-1] if j else 0)-(v[j+1] if j+1<len(v) else 0) for j in range(len(v))]
    out=[0]*(N+1)
    for pi in permutations(range(3)):
        sign=(-1)**sum(pi[i]>pi[j] for i in range(3) for j in range(i+1,3))
        term=egf_product(egf_product(entries[0,pi[0]],entries[1,pi[1]],N),entries[2,pi[2]],N)
        out=[x+sign*y for x,y in zip(out,term)]
    return out

def square_range(a,b):return (0 if a<=0<=b else min(a*a,b*b)),max(a*a,b*b)
def density_at_center(n,pl,ph):
    # rho_A(6)=1/6 integral Delta(x,y,6-x-y)^2 rho1(x)rho1(y)rho1(6-x-y) dxdy.
    shift=3*n//2;radii=[radius_bounds(i,i+1,n) for i in range(n)]
    low=high=0
    for i,(a,b) in enumerate(radii):
        for j,(c,d) in enumerate(radii):
            f,g=radius_bounds(shift-i-j-2,shift-i-j,n)
            if not g:continue
            dl=dh=1
            for u,v in ((i-j-1,i-j+1),(2*i+j-shift,2*i+j+3-shift),(i+2*j-shift,i+2*j+3-shift)):
                l,h=square_range(u,v);dl*=l;dh*=h
            low+=root_bounds(a*c*f)[0]*dl
            high+=root_bounds(b*d*g)[1]*dh
    factor=Q(128*4096,6*n**11*SCALE)
    return factor*low/ph**3,factor*high/pl**3

def main():
    orbital_path=BASE/'results/multiobject_orbital_selfenergy.json';typed_path=BASE/'results/typed_spin_channels.json'
    for path in (orbital_path,typed_path):
        r=json.loads(path.read_text(encoding='utf-8'));assert r['verification_passed']
        for name,digest in r['source_hashes'].items():assert sha256((BASE/name).read_bytes()).hexdigest()==digest
    typed=json.loads(typed_path.read_text(encoding='utf-8'))
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    decorated={tuple(v['object_indices']):decode(v['amplitude']) for v in typed['decorated_scalar_three_object_state']}
    check('retained_scalar_orbital_vertex_norm_one',vector_norm(decorated)==1)
    check('retained_vertex_whole_object_exchange',all(exchange(decorated,p)==decorated for p in permutations(range(3))))
    collapsed={}
    for key,value in decorated.items():
        spins=tuple(x//3 for x in key);collapsed[spins]=collapsed.get(spins,A())+value
    check('one_orbital_collapse_erases_vertex',all(value==0 for value in collapsed.values()))
    triple_map=tuple(tuple(decode(x) for x in row) for row in typed['three_output_map'])
    spin_labels=[(i,j,k) for i in range(3) for j in range(3) for k in range(3)]
    epsilon=lambda key:0 if len(set(key))<3 else (-1)**sum(key[i]>key[j] for i in range(3) for j in range(i+1,3))
    check('scalar_and_previous_vector_triple_orthogonal',all(sum((epsilon(key)*triple_map[row][column] for row,key in enumerate(spin_labels)),A())==0 for column in range(4)))
    paulis=[pauli(tuple(A(i==j) for i in range(3))) for j in range(3)]
    for index,sigma in enumerate(paulis):
        T=scale(-CI/2,sigma)
        L=tuple(tuple(trace(mm(paulis[i],add(mm(T,paulis[j]),scale(A(-1),mm(paulis[j],T)))))/2 for j in range(3)) for i in range(3))
        check('retained_vertex_rotation_scalar_'+str(index),tensor_generator(kron(L,eye(3)),decorated)=={})
    # Exact determinant expansion gives orbital normalization, without treating
    # three distinct records as independent identical endpoint attachments.
    N=384;ms=exterior_moments(N)
    check('Slater_spectral_measure_mass_one',ms[0]==1)
    check('Slater_mean_and_variance',ms[1]==6 and ms[2]-ms[1]**2==1)
    check('all_endpoint_moments_positive',all(x>0 for x in ms))
    labels,H,e=exterior_model(6);n=len(labels)
    check('finite_exterior_dimension',n==comb(6,3)==20)
    check('exterior_H_positive',positive_definite(H))
    check('exterior_H_upper_band',positive_definite([[12*(i==j)-H[i][j] for j in range(n)] for i in range(n)]))
    v=e[:];actual=[]
    for order in range(8):actual.append(dot(e,v));v=matvec(H,v)
    check('finite_vs_infinite_determinant_moments',actual==ms[:8])
    # Reflection x->12-x follows from staggering of all orbitals; the Slater
    # vertex picks up a phase only. Verify initial reflected moments exactly.
    check('spectral_reflection_moments',all(sum(comb(n,j)*12**(n-j)*(-1)**j*ms[j] for j in range(n+1))==ms[n] for n in range(16)))
    enclosures=[]
    for s in (1,2,4):
        lo,hi,error=enclose_g(3,s,ms,N)
        check('certified_below_band_'+str(s),-Q(1,s)<=lo<hi<0 and error<Q(1,10**12))
        enclosures.append({'z':str(-s),'g':Interval(lo,hi).record(),'tail_bound':str(error),'terms':N+1})
    pl,ph=pi_bounds();refinements=[]
    for mesh in (128,256,512):
        density=Interval(*density_at_center(mesh,pl,ph))
        check('positive_scalar_triple_density_'+str(mesh),density.low>0)
        refinements.append({'grid_per_coordinate':mesh,'rho_A_at_6':density.record()})
    check('center_density_bounds_refine',all(Q(b['rho_A_at_6']['upper'])-Q(b['rho_A_at_6']['lower'])<Q(a['rho_A_at_6']['upper'])-Q(a['rho_A_at_6']['lower']) for a,b in zip(refinements,refinements[1:])))
    check('center_density_width_control',density.high-density.low<Q(1,10))
    width=2*Interval(pl,ph)*density
    check('positive_retarded_scalar_triple_width',width.low>0)
    # Low-edge Laguerre/Selberg coefficient: divide product Gamma factors by
    # 3! pi^3 Gamma(21/2). Rational part is 32/(14549535 pi^2).
    odd_product=1
    for x in range(1,20,2):odd_product*=x
    coefficient=Q(135,16)*Q(2**10,6*odd_product)
    check('low_threshold_coefficient_control',coefficient==Q(32,14549535))
    result={'verification_passed':all(checks.values()),'checks':checks,
        'orbital_H':'sum_a h_a on wedge^3 ell2(N0), embedded with internal epsilon in Sym^3(ell2(N0) tensor W)',
        'orbital_vertex':'b_A=|0 wedge 1 wedge 2>, norm one; distinct records retained',
        'internal_vertex':'epsilon_ijk/sqrt(6), a rotation scalar; combined amplitude epsilon_ijk epsilon_abc/6',
        'core_vertex':'B_A x=lambda_A b_A tensor epsilon/sqrt(6) times <vec(I),x>/sqrt(2); Gram=lambda_A^2 P_scalar',
        'spectral_joint_measure':'(1/6) product_a rho1(E_a) times product_(a<b)(E_a-E_b)^2 dE1 dE2 dE3',
        'energy_density':'rho_A(E)=integral joint_measure delta(E-sum E_a)',
        'selfenergy':'Sigma_A(z)=lambda_A^2 g_A(z) P_scalar, g_A(z)=integral rho_A(E)/(z-E) dE',
        'band':[0,12],'center_retarded':'g_A(6+i0)=-i pi rho_A(6), Re=0 by spectral reflection',
        'threshold':'rho_A(E)~32 E^(19/2)/(14549535 pi^2), and reflected upper-edge law',
        'finite_control':{'sites':6,'dimension':n,'orbitals':[list(v) for v in labels],
            'Hamiltonian':[[str(x) for x in row] for row in H],'endpoint_moments':list(map(str,actual))},
        'infinite_moments_first_twelve':ms[:12],'certified_below_band_g':enclosures,
        'center_density_refinements':refinements,'center_unit_coupling_Gamma':width.record(),
        'scalar_core_extension':'Sigma_s=lambda_in^2 g2 + lambda_2^2 g2 + lambda_A^2 g_A; input, two-output and scalar three-output share a genuine scalar sector',
        'qualifications':['Antisymmetric orbital sector alone is not declared fermion statistics: its internal partner makes whole objects bosonic.',
            'One endpoint copy cannot reproduce this vertex; Vandermonde vanishes when orbital energies coincide.',
            'Free dispersion, three adjacent orbital sites and lambda_A are declared, not geometry-derived physical inputs.',
            'This new channel is orthogonal internally to the prior vector triple channel; no interference term between them is silently added.',
            'Native full-spinor core attachment, on-band scattering with this new vertex, and physical channel identification remain open.'],
        'source_hashes':{str(p.relative_to(BASE)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in
            (orbital_path,typed_path,Path(__file__),BASE/'checkers/check_multiobject_onband.py',BASE/'checkers/check_multiobject_orbital_selfenergy.py')}}
    (BASE/'results/orbital_record_selfenergy.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verification_passed':True,'check_count':len(checks),'rho_A_at_6':density.record()['decimal_view'],
        'endpoint_mean':ms[1],'endpoint_variance':ms[2]-ms[1]**2,
        'below_band_g':[{'z':v['z'],'g':v['g']['decimal_view']} for v in enclosures]},indent=2))

if __name__=='__main__':main()
