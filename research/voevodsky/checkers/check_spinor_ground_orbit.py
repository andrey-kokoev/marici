"""Global fixed-flux pure-state minimum and exact binary rotation transport.

Symbolic determinant/cofactor identities support the critical-point exhaustion
proved in the accompanying note. Exact rational brackets compare every low
critical family at the frozen field coefficients; no numerical optimizer is
used to assert globality. Run with: uv run --with sympy python THIS_FILE.
"""
from fractions import Fraction as F
from itertools import combinations, product
from hashlib import sha256
from pathlib import Path
import json
import sympy as sp
from check_spinor_matter_link_adapter import decode
from check_electron_tetrahedral_spinor import D, G0, G1, GI, ident, adj, sm, ma, trace, gmm, gm, gc, gs, gt
from check_electron_charge_spin_frontier import spin, qm

BASE=Path(__file__).resolve().parents[1]


def act(a,v):return tuple(gt(gm(x,y) for x,y in zip(row,v)) for row in a)


def main():
    beta,eta=F(3,5),F(1,5);c=beta/10
    path=BASE/'results/electron_tetrahedral_spinor_store.json'
    raw=path.read_bytes();store=json.loads(raw)
    face=[tuple(tuple(decode(z) for z in row) for row in p) for p in store['face_projectors']]
    local=[tuple(p[i][0] for i in range(2)) for p in face]
    metric=[gt(gm(gc(z),z) for z in v)[0] for v in local]
    v=tuple(tuple(local[j][i%2] if i//2==j else G0 for j in range(4)) for i in range(8))
    decoder=tuple(tuple(gs(D(1)/n,gc(v[i][j])) for i in range(8)) for j,n in enumerate(metric))
    n=tuple(tuple(gs(F(1,2),gmm(face[i//2],face[j//2])[i%2][j%2]) for j in range(8)) for i in range(8))
    k=sm(2,ma(ident(4),sm(-1,gmm(decoder,gmm(n,v)))))
    # A diagonal gauge puts the source conference matrix in this form.
    a=sp.Matrix([[0,1,1,1],[-1,0,1,-1],[-1,-1,0,1],[-1,1,-1,0]])
    assert a*a==-3*sp.eye(4)
    q=sp.I*a/sp.sqrt(3)
    for i,j,l in combinations(range(4),3):
        source=gs(D(0,3),trace(gmm(gmm(face[i],face[j]),face[l])))
        expected=sp.simplify(3*sp.sqrt(3)*q[i,j]*q[j,l]*q[l,i])
        assert expected==(sp.I if source==GI else -sp.I)
    ds=sp.symbols('d0:4',real=True)
    determinant=sp.expand((sp.diag(*ds)-q).det())
    expected=sp.prod(ds)-sum(ds[i]*ds[j] for i,j in combinations(range(4),2))/3+1
    assert sp.simplify(determinant-expected)==0
    cof=[sp.diff(determinant,d) for d in ds]
    for i,j in combinations(range(4),2):
        other=[x for x in range(4) if x not in (i,j)]
        assert sp.simplify(cof[i]-cof[j]-(ds[j]-ds[i])*(ds[other[0]]*ds[other[1]]-sp.Rational(1,3)))==0
    aa,bb=sp.symbols('a b',real=True)
    assert sp.simplify(determinant.subs(dict(zip(ds,(aa,bb,bb,bb))))-(bb**2-1)*(aa*bb-1))==0
    paired=determinant.subs(dict(zip(ds,(aa,aa,bb,bb))))
    assert sp.simplify(paired-((aa*bb-1)**2-(aa-bb)**2/3))==0
    assert sp.simplify(determinant.subs(dict(zip(ds,(aa,bb,0,0))))-(1-aa*bb/3))==0
    assert sp.simplify(sum(cof).subs(dict(zip(ds,(aa,bb,0,0))))+aa+bb)==0
    assert c*c<27  # exceptional three-distinct-density case is impossible
    # Multiple zero eigenvalues would force uniform density in a coherent
    # or dark doublet. Both have pure-state site purity 1/3, not 1/4.
    xx=sp.symbols('x0:4',real=True)
    for sign in (-1,1):
        basis=(q-sign*sp.eye(4)).nullspace()
        assert len(basis)==2
        z=basis[0]*(xx[0]+sp.I*xx[1])+basis[1]*(xx[2]+sp.I*xx[3])
        densities=[sp.expand_complex(sp.conjugate(t)*t).expand() for t in z]
        assert sp.simplify(sum(t*t for t in densities)-sum(densities)**2/3)==0
    # Exhausted low critical families: 1:3, 2:2, or zero-address coherent.
    lo,hi=F(0),F(1)
    poly=lambda r:3*r**4+6*c*r**3-2*c*r-3
    for _ in range(100):
        mid=(lo+hi)/2
        if poly(mid)<0:lo=mid
        else:hi=mid
    r=(lo+hi)/2
    kinetic=lambda r:(r-1)**2/(1+r*r)
    field=lambda r:c*(1+(r**4+F(1,3))/(1+r*r)**2)+eta/2
    # Kinetic decreases and field increases on the root bracket.
    assert lo*lo>F(1,3) and hi<1
    axis_interval=(kinetic(hi)+field(lo),kinetic(lo)+field(hi))
    ylo,yhi=F(0),F(1)
    paired_poly=lambda y:2*y*y-(1-c*y/2)**2*(3-y*y)
    for _ in range(100):
        mid=(ylo+yhi)/2
        if paired_poly(mid)<0:ylo=mid
        else:yhi=mid
    # At the stationary root eliminate its radical. This expression is
    # strictly decreasing on [0,1] at 0<c<1.
    assert 0<c<1
    paired_energy=lambda y:1-y/3-F(2,3)*y/(1-c*y/2)+c*(1+y*y/3)/4+c+eta/2
    pair_interval=(paired_energy(yhi),paired_energy(ylo))
    coherent=2*beta/15+eta/2
    assert axis_interval[1]<pair_interval[0]<pair_interval[1]<coherent
    # High phase branches have kinetic >=1-1/sqrt(3)>0.4, already above
    # every low-family total. Verify the exact rational inequality.
    from check_electron_tetrahedral_spinor import pos
    assert pos(D(1)-D(0,F(1,3))-F(2,5))
    assert axis_interval[1]<F(2,5)
    # Exact source action transports the axis trial formula for ANY r.
    # Thus the identity holds at the algebraic minimizing root as well.
    quats=set()
    for address in range(4):
        for sign in (-1,1):quats.add(tuple(F(sign if i==address else 0) for i in range(4)))
    quats.update(tuple(F(s,2) for s in signs) for signs in product((-1,1),repeat=4))
    actions={};permutations={}
    for quat in quats:
        u=spin(quat)
        perm=[face.index(gmm(gmm(u,p),adj(u))) for p in face]
        t8=tuple(tuple(u[i%2][j%2] if i//2==perm[j//2] else G0 for j in range(8)) for i in range(8))
        t4=gmm(decoder,gmm(t8,v))
        assert gmm(t4,k)==gmm(k,t4)
        actions[quat]=t4;permutations[quat]=perm
        for address in range(4):
            e=tuple(G1 if i==address else G0 for i in range(4))
            target=perm[address]
            ee=tuple(G1 if i==target else G0 for i in range(4))
            multiplier=t4[target][address]
            assert act(t4,e)==tuple(gm(multiplier,z) for z in ee)
            assert gm(gc(multiplier),multiplier)[0]*metric[target]==metric[address]
            # Checking e and K e separately proves polynomial/root transport.
            assert act(t4,act(k,e))==tuple(gm(multiplier,z) for z in act(k,ee))
    for first in quats:
        for second in quats:assert gmm(actions[first],actions[second])==actions[qm(first,second)]
    central=(-F(1),F(0),F(0),F(0))
    assert actions[central]==sm(-1,ident(4))
    # All four minimizing rays span four coordinates for r !=1:
    # columns ((r+1)I-K)e_i, determinant (r+1)^2*(r-1)^2.
    assert poly(F(1))>0 and hi<1
    density=r*r/(1+r*r)
    result={
        'verification_passed':True,'source_sha256':sha256(raw).hexdigest(),
        'field_fixture':{'beta':str(beta),'eta':str(eta)},
        'global_minimum_proof':'Compact pure-state domain; stationary cofactor identities exhaust one-to-three and two-to-two density families, zero-address coherent states and higher phase branches. Exact intervals select one-to-three.',
        'global_minimum_interval':list(map(str,axis_interval)),
        'global_minimum_interval_decimal':list(map(float,axis_interval)),
        'paired_stationary_energy_interval_decimal':list(map(float,pair_interval)),
        'zero_address_coherent_energy':str(coherent),
        'ground_state_rays':4,
        'ground_state_formula':'psi_i proportional to ((r+1)I-K_e)e_i; 3*r^4+6*c*r^3-2*c*r-3=0, c=beta/10.',
        'root_interval':list(map(str,(lo,hi))),
        'density_pattern':[float(density)]+[float((1-density)/3)]*3,
        'dark_fraction':float(kinetic(r)/2),
        'exact_binary_rotations_checked':24,
        'exact_group_compositions_checked':576,
        'central_full_rotation_action':'-I_4 on source amplitudes; each minimizing lift changes sign',
        'ground_orbit_transport':'Every binary tetrahedral rotation maps a minimizing ray to the ray at the permuted face, with its source-computed phase retained.',
        'span_of_ground_orbit':4,
        'linear_ground_doublet':False,
        'reason':'The nonlinear minima are four rays, not all superpositions in a two-dimensional eigenspace. Their column map has nonzero determinant (r+1)^2*(r-1)^2.',
        'elementary_with_one_unit_occupation_interval':list(map(float,(1+axis_interval[0],1+axis_interval[1]))),
        'scope':'Global proof for the four negative-face classical amplitudes at the specified hard-flux fixture; not a quantized interacting particle Hilbert-space result.',
        'next_gate':'Quantize or otherwise construct the interacting ground-sector carrier and its state space; retain the four-ray nonlinear orbit rather than relabelling it a logical doublet.',
    }
    out=BASE/'results/spinor_ground_orbit.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
