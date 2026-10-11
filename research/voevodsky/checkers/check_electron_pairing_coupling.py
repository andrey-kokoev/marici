"""Audit the retained phase attachment and a declared spinor pair vertex.
The former is source-bound and complex-linear. The latter is an explicit
new bilinear operation, not an inferred electromagnetic interaction.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_retained_phase_attachment import solve,geo,SOURCE,verify,ONE,conj,div,weight,times,ZERO
from check_electron_charge_spin_frontier import ga,gs,gm,gc,gt,gmm,spin,qm,G0,G1,GI

BASE=Path(__file__).resolve().parents[1]
def adj(a):return tuple(tuple(gc(x) for x in row) for row in zip(*a))
def trans(a):return tuple(zip(*a))
def neg(a):return tuple(tuple(gs(-1,x) for x in row) for row in a)
def ident(n):return tuple(tuple(G1 if i==j else G0 for j in range(n)) for i in range(n))
def act(a,v):return tuple(gt(gm(x,y) for x,y in zip(row,v)) for row in a)
def pair(a,b):return ga(gm(a[0],b[1]),gs(-1,gm(a[1],b[0])))
def norm(v):return gt(gm(gc(x),x) for x in v)[0]
def gdiv(a,b):return gs(1/(b[0]*b[0]+b[1]*b[1]),gm(a,gc(b)))
def rank(rows):
    a=[list(row) for row in rows];pivot=0
    for c in range(len(a[0])):
        k=next((k for k in range(pivot,len(a)) if a[k][c]!=G0),None)
        if k is None:continue
        a[pivot],a[k]=a[k],a[pivot];d=a[pivot][c];a[pivot]=[gdiv(x,d) for x in a[pivot]]
        for k in range(pivot+1,len(a)):
            d=a[k][c]
            if d!=G0:a[k]=[ga(x,gs(-1,gm(d,y))) for x,y in zip(a[k],a[pivot])]
        pivot+=1
        if pivot==len(a):break
    return pivot

def main():
    raw=SOURCE.read_bytes();source=json.loads(raw);verified,rows=verify(source)
    geometry=source['objects'][source['objects'][source['root']]['geometry']]['payload']
    pts=dict(geo.POINTS)
    for f in ('ABC','ABD','ACD','BCD'):pts['F_'+f]=geo.mean([pts[k] for k in f])
    coeff=(ONE,geo.OMEGA,times(geo.OMEGA,geo.OMEGA));v={}
    for t in geometry['triangles_and_transports']:v[t['outer_arrow']]=geo.zmv(geo.transpose(tuple(pts[k] for k in t['triangle'])),coeff)
    ports=sorted({tuple(p) for r in rows for p in (r['source'],r['target'])})
    D={p:div(v[p[1]]['xyz'.index(p[2])],conj(v[p[1]]['xyz'.index(p[2])])) for p in ports}
    edges=[(tuple(r['source']),tuple(r['target']),div(weight(r),conj(weight(r)))) for r in rows]
    phases,tree,defects=solve(edges,('raw','AB','x'))
    assert verified['verified'] and len(rows)==1836 and len(phases)==108 and not defects
    assert all(times(weight(r),D[tuple(r['source'])])==times(D[tuple(r['target'])],conj(weight(r))) for r in rows)
    failures=0
    for p,d in D.items():
        w=v[p[1]]['xyz'.index(p[2])];reversed_mode=conj(w)
        got=times(d,times(geo.OMEGA,reversed_mode))
        assert got==times(geo.OMEGA,w)
        failures+=got!=times(conj(geo.OMEGA),w)
    assert failures==108
    # Retain the primitive common phase instead of treating D as a frozen,
    # neutral frame. This is a distinct state-dependent attachment contract.
    # D(z v)=(z/conj(z))D(v), so D carries phase weight two.
    root=('raw','AB','x');normalization_controls=0
    for z in (ONE,geo.OMEGA,(F(2),F(1))):
        Dz={}
        for p in ports:
            w=v[p[1]]['xyz'.index(p[2])];state=times(z,w)
            Dz[p]=div(state,conj(state))
            assert Dz[p]==times(div(z,conj(z)),D[p])
            assert times(Dz[p],times(conj(z),conj(w)))==state
        assert all(div(Dz[p],Dz[root])==div(D[p],D[root]) for p in ports)
        assert all(times(weight(r),Dz[tuple(r['source'])])==times(Dz[tuple(r['target'])],conj(weight(r))) for r in rows)
        normalization_controls+=1
    # Nonzero fixed linear arrows enforce equal endpoint phase weights.
    # Connectedness proves that the entire retained network has one uniform
    # scalar weight, not a choice of opposite weights at the matched ports.
    assert len(tree)==107 and all(weight(r)!=ZERO for r in rows)
    E=((G0,G1),(gs(-1,G1),G0));I=ident(2)
    quats=set()
    for k in range(4):
        for s in (-1,1):quats.add(tuple(F(s if i==k else 0) for i in range(4)))
    quats.update(tuple(F(s,2) for s in signs) for signs in product((-1,1),repeat=4))
    basis=[tuple(tuple(G1 if (i,j)==(a,b) else G0 for j in range(2)) for i in range(2)) for a in range(2) for b in range(2)]
    bilinear_rows=[];linear_rows=[]
    for q in quats:
        U=spin(q);assert gmm(gmm(trans(U),E),U)==E
        bcols=[];lcols=[]
        for X in basis:
            bx=gmm(gmm(trans(U),X),U);lx=gmm(U,X);xr=gmm(X,U)
            bcols.append([ga(bx[i][j],gs(-1,X[i][j])) for i in range(2) for j in range(2)])
            lcols.append([ga(lx[i][j],gs(-1,xr[i][j])) for i in range(2) for j in range(2)])
        bilinear_rows.extend(zip(*bcols));linear_rows.extend(zip(*lcols))
    assert rank(bilinear_rows)==rank(linear_rows)==3
    def C(z):return act(neg(E),tuple(map(gc,z)))
    samples=((G1,G0),(G0,G1),(G1,GI),((F(3,5),F(4,5)),G1))
    phase=(F(3,5),F(4,5))
    for z in samples:
        assert C(C(z))==tuple(gs(-1,x) for x in z)
        assert pair(z,C(z))==(norm(z),F(0))
        assert C(tuple(gm(phase,x) for x in z))==tuple(gm(gc(phase),x) for x in C(z))
        assert C(tuple(gm(phase,x) for x in z))!=tuple(gm(phase,x) for x in C(z))
        for q in quats:assert C(act(spin(q),z))==act(spin(q),C(z))
    # Antilinear spin reversal is a state relation, not a deterministic
    # one-spinor quantum channel. Its transpose-map Choi matrix has a negative
    # eigenvalue. This does not prohibit charge conjugation on an enlarged
    # particle/antiparticle field space.
    swap=tuple(tuple(G1 if (i//2,i%2)==(j%2,j//2) else G0 for j in range(4)) for i in range(4))
    K=tuple(tuple(E[i%2][j%2] if i//2==j//2 else G0 for j in range(4)) for i in range(4))
    choi=tuple(tuple(gs(F(1,2),x) for x in row) for row in gmm(gmm(K,swap),adj(K)))
    witness=(G1,G0,G0,G1)
    assert act(choi,witness)==tuple(gs(-F(1,2),x) for x in witness)
    singlet=(G0,G1,gs(-1,G1),G0)
    effect=tuple(tuple(gs(F(1,2),gm(gc(x),y)) for y in singlet) for x in singlet)
    assert gmm(effect,effect)==effect and gt(effect[i][i] for i in range(4))==G1
    # Exact Ward identities on a nonzero pairing. The all-phase theorem is
    # scalar homogeneity: linear gluing needs q_e=q_p, a neutral pair q_e=-q_p.
    p=(G1,G0);e=(G0,G1);assert pair(p,e)==G1
    linear_allowed=[];pair_allowed=[]
    for qe in range(-4,5):
        qp=1
        if qe==qp:linear_allowed.append(qe)
        ward=ga(pair(tuple(gs(qp,x) for x in p),e),pair(p,tuple(gs(qe,x) for x in e)))
        assert ward==gs(qp+qe,pair(p,e))
        if ward==G0:pair_allowed.append(qe)
    assert linear_allowed==[1] and pair_allowed==[-1]
    # The source proton is central-even. One old proton and one spinor cannot
    # contract to a rotational scalar: the central action changes its sign.
    # A declared tensor spin lift repairs the type but duplicates source arrows.
    doubled_ports={(tuple(port),s) for port in ports for s in (0,1)}
    doubled_arrows=[(tuple(r['source'])+(s,),tuple(r['target'])+(s,),weight(r)) for r in rows for s in (0,1)]
    assert len(doubled_ports)==216 and len(doubled_arrows)==3672
    # Spinor fixture's raw pair vertex has 36 proton mode coordinates times
    # four full 2x2 face blocks. Its arity differs from the old linear arrows.
    spin_path=BASE/'results/electron_tetrahedral_spinor_store.json';spinraw=spin_path.read_bytes();store=json.loads(spinraw)
    assert len(store['face_projectors'])==4
    assert all(any(F(a)!=0 for part in z for a in part) for P in store['face_projectors'] for row in P for z in row)
    raw_pair_monomials=36*sum(len(P)*len(P[0]) for P in store['face_projectors'])
    assert raw_pair_monomials==576
    # If the only species mass vertex is this neutral off-diagonal pair,
    # the diagnostic matrix has degenerate singular values, with free scale g.
    scales=[]
    for g in (G1,(F(2),F(0)),(F(3),F(4))):
        M=((G0,g),(g,G0));m2=gm(gc(g),g)
        assert gmm(adj(M),M)==tuple(tuple(m2 if i==j else G0 for j in range(2)) for i in range(2))
        scales.append(str(m2[0]))
    checks={
        'all_1836_retained_attachment_constraints_reconstructed':len(rows)==1836 and not defects,
        'source_attachment_is_connected_on_108_typed_ports':len(phases)==108,
        'all_108_ports_reject_interpreting_frozen_D_as_phase_conjugation':failures==108,
        'state_dependent_primitive_D_has_phase_weight_two':normalization_controls==3,
        'retaining_common_D_phase_matches_conjugate_amplitudes_on_all_arrows':True,
        'root_normalization_erases_the_charged_common_phase':True,
        'one_spinor_reversal_is_not_a_completely_positive_channel':True,
        'singlet_pair_contraction_has_a_valid_projector_effect':gmm(effect,effect)==effect,
        'spinor_bilinear_invariant_unique_up_to_scalar':rank(bilinear_rows)==3,
        'spinor_linear_intertwiner_also_unique_up_to_scalar':rank(linear_rows)==3,
        'pseudoreal_C_is_equivariant_antilinear_and_squares_to_minus_I':True,
        'neutral_pair_Ward_identity_requires_opposite_weights':pair_allowed==[-1],
        'old_linear_attachment_requires_equal_weights':linear_allowed==[1],
        'spin_lifting_old_proton_doubles_typed_source_support':len(doubled_arrows)==3672,
        'raw_bilinear_pair_retains_576_nonzero_monomials':raw_pair_monomials==576,
        'single_off_diagonal_mass_trial_has_equal_singular_values_and_free_scale':scales==['1','4','25'],
        'sources_unchanged':SOURCE.read_bytes()==raw and spin_path.read_bytes()==spinraw,
    }
    report={'verification_passed':all(checks.values()),'checks':checks,
        'obligation':'attachment transport before charge readout',
        'source_attachment':{'contract':'h D_s=D_t conjugate(h); D acts complex-linearly on field amplitudes',
            'phase_test':'D(omega conjugate(v))=omega v, not conjugate(omega) v',
            'opposite_phase_failures':failures,'ports':len(ports),'arrows':len(rows),
            'conclusion':'Conjugating fixed mode coefficients changes circulation, not the gauge weight of the freely varying amplitude.',
            'retained_phase_rival':{'law':'D(p)_a=p_a/conjugate(p_a); D(zv)=(z/conjugate(z))D(v)',
                'phase_weight':'2 if p has weight 1',
                'matching':'D(p) e=p is solved by e=conjugate(p), with opposite variable phase',
                'normalization':'Dividing by the root D(p) removes this common phase, while all 1836 coefficient constraints remain unchanged.',
                'selection_residual':'Frozen neutral D and state-dependent charged D both satisfy the retained arrow constraints; those constraints do not choose the contract.'}}, 
        'candidate_coupling':{'type':'new bilinear vertex S_p tensor S_e -> neutral scalar port',
            'formula':'B(p,e)=p_0 e_1-p_1 e_0 = p^T epsilon e',
            'uniqueness':'one-dimensional invariant space for the binary tetrahedral spinor representation',
            'phase_law':'B(exp(i q_p theta)p,exp(i q_e theta)e)=exp(i(q_p+q_e)theta)B(p,e)',
            'conditional_charge':'If an independently neutral output and q_p=+1 are supplied, q_e=-1 follows.',
            'rival':'The linear invariant T=cI gives equal phase weights and also respects rotations.',
            'duality_map':'C=-epsilon K, C^2=-I; this reverses variable amplitude phase, unlike frozen D.',
            'quantum_operation_test':'As a map on an unknown individual spinor density, C induces a transpose channel with normalized Choi eigenvalue -1/2. Pair contraction is instead a valid singlet effect; the two operations are not interchangeable.',
            'logical_bilinear_terms':2,'raw_bilinear_monomials':raw_pair_monomials,
            'not_present':'No binary neutral-output vertex is present in the existing linear L/G/N arrow grammar.'},
        'proton_type':{'old':'central-even vector coherent line','pairing_obstruction':'A single central-odd electron cannot pair with it to a central-even scalar.',
            'declared_repair':'Tensor the old proton coherent line with a spinor doublet.',
            'repaired_coherent_rank':2,'repaired_typed_ports':len(doubled_ports),'repaired_transfer_support':len(doubled_arrows),
            'status':'Explicit source enlargement, not a cost-free spin label or an inferred physical proton.'},
        'mass_and_statistics':{'minimal_mass_trial':'M=[[0,g],[g,0]] gives M* M=|g|^2 I. It yields equal mass parameters, not a proton/electron hierarchy, and g is free.',
            'scope':'This is a diagnostic quadratic mass interpretation, not a derived relativistic dynamics.',
            'exchange':'Antisymmetry of the spin contraction does not impose fermionic statistics on distinct proton/electron species.'},
        'disposition':'The primitive attachment formula supplies a charge-two phase-link candidate when evaluated on the field and its common phase is retained. The existing arrow constraints also admit the neutral frozen-frame contract and cannot select between them. A declared neutral bilinear spinor vertex fixes opposite relative charges but requires a spinorial proton and a neutral output. Neither candidate supplies mass or statistics.',
        'first_missing_source_object':'A source rule selecting the state-dependent charged-phase attachment rather than its frozen normalized rival; for the spinor pair route, a typed binary neutral-output vertex and its retained embeddings.',
        'stop':'No electrical-charge or mass claim is promoted from the old flux. Do not infer this missing vertex from the desired charges.',
        'source_sha256':{'proton':sha256(raw).hexdigest(),'retained_phase_checker':sha256((BASE/'checkers/check_retained_phase_attachment.py').read_bytes()).hexdigest(),'spinor_store':sha256(spinraw).hexdigest()},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/electron_pairing_coupling.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not report['verification_passed']:raise SystemExit(1)

if __name__=='__main__':main()
