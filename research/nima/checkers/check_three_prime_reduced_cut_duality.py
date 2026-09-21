"""Exact reduced signed cut complexes and contragredient naturality.

Two signed coordinates are a fiber algebra fixture, not an injective model
of the seven-dimensional analytical chamber feature space.
"""
from itertools import permutations, product
from pathlib import Path
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
LEVELS = ((), (1,), (2,), (1,2))
ENDS = (2,4,6,10,12,20,30,60)
POS = {n:i for i,n in enumerate(ENDS)}
TAU = s.Rational(1,2)


def route(primes):
    vertices = [2]
    for p in primes:
        vertices.append(vertices[-1]*p)
    return tuple(vertices)


def words(cap):
    return tuple(w for n in range(cap+1) for w in product(range(2),repeat=n))


def adjoint(A):
    return A.conjugate().T


def clean(A):
    return A.applyfunc(s.expand)


def main():
    routes = tuple(route(p) for p in permutations((2,3,5)))
    masks = tuple(product((0,1),repeat=3))
    keys, index, Q, Qinv, joins, mates = {}, {}, {}, {}, {}, {}
    opposite_keys = {}
    for cuts in LEVELS:
        labels = sorted({tuple(v[c] for c in cuts) for v in routes})
        bounds = (0,)+cuts+(3,)
        caps = tuple(b-a for a,b in zip(bounds,bounds[1:]))
        keys[cuts] = tuple((label,block) for label in labels
                          for block in product(*(words(cap) for cap in caps)))
        index[cuts] = {k:i for i,k in enumerate(keys[cuts])}
        opposite_labels = sorted({tuple(v[::-1][c] for c in cuts) for v in routes})
        opposite_keys[cuts] = tuple((label,block) for label in opposite_labels
                                   for block in product(*(words(cap) for cap in caps)))
        entries = {i:TAU**(2*sum(map(len,blocks)))*(-1)**sum(map(sum,blocks))
                   for i,(_,blocks) in enumerate(keys[cuts])}
        Q[cuts] = s.SparseMatrix(len(entries),len(entries),{(i,i):v for i,v in entries.items()})
        Qinv[cuts] = s.SparseMatrix(len(entries),len(entries),{(i,i):1/v for i,v in entries.items()})
        assert Qinv[cuts]*Q[cuts] == s.eye(len(entries))

    for source in LEVELS:
        for target in LEVELS:
            if not set(target) <= set(source):
                continue
            entries = {}
            for j,(labels,blocks) in enumerate(keys[source]):
                output = [blocks[0]]
                for cut,block in zip(source,blocks[1:]):
                    if cut in target:
                        output.append(block)
                    else:
                        output[-1] += block
                out_labels = tuple(labels[source.index(c)] for c in target)
                entries[index[target][out_labels,tuple(output)],j] = 1
            A = s.SparseMatrix(len(keys[target]),len(keys[source]),entries)
            joins[source,target] = A
            sharp = Qinv[source]*adjoint(A)*Q[target]
            mates[source,target] = sharp
            assert sharp == A.T
            # beta_source A^sharp = A^vee beta_target
            assert Q[source]*sharp == adjoint(A)*Q[target]
            # D Cone(A) = Fib(A^vee); under beta the differential is -A^sharp.
            assert -adjoint(A)*Q[target] == Q[source]*(-sharp)

    # Every commutative arrow square of this cut poset, not only terminal cones.
    squares = 0
    for (src,tgt), A in joins.items():
        for (src2,tgt2), B in joins.items():
            if (src,src2) not in joins or (tgt,tgt2) not in joins:
                continue
            U, V = joins[src,src2], joins[tgt,tgt2]
            Us, Vs = mates[src,src2], mates[tgt,tgt2]
            As, Bs = mates[src,tgt], mates[src2,tgt2]
            assert B*U == V*A  # Cone chain map in degrees -1,0.
            assert Us*(-Bs) == (-As)*Vs  # Reflected fiber chain map in degrees 0,1.
            assert adjoint(U)*Q[src2] == Q[src]*Us
            assert adjoint(V)*Q[tgt2] == Q[tgt]*Vs
            squares += 1
    triples = 0
    for a in LEVELS:
        for b in LEVELS:
            for c in LEVELS:
                if (a,b) in joins and (b,c) in joins:
                    assert joins[b,c]*joins[a,b] == joins[a,c]
                    assert mates[a,b]*mates[b,c] == mates[a,c]
                    triples += 1

    # Lower-sheet orientation and slot reversal; real permutation matrices
    # implement the antilinear map after coefficient conjugation.
    reversal = {}
    for cuts in LEVELS:
        reflected = tuple(sorted(3-c for c in cuts))
        entries = {}
        for j,(labels,blocks) in enumerate(keys[cuts]):
            out = (labels[::-1],tuple(tuple(1-a for a in w[::-1]) for w in blocks[::-1]))
            # Opposite labels are reverse tuples of forward labels; use a
            # separately indexed opposite carrier, not a false forward route.
            opposite_index = {k:i for i,k in enumerate(opposite_keys[reflected])}
            entries[opposite_index[out],j] = 1
        R = s.SparseMatrix(len(keys[reflected]),len(keys[cuts]),entries)
        reversal[cuts] = R
        # The opposite carrier has its own vertex tuples; signature blocks
        # have the same ordering and repeat once for each admitted tuple.
        lower = s.SparseMatrix(len(keys[reflected]),len(keys[reflected]),{
            (i,i):Q[reflected][i,i]*(-1)**sum(map(len,blocks))
            for i,(_,blocks) in enumerate(keys[reflected])})
        assert R.T*lower*R == Q[cuts]

    # Opposite rejoining uses reflected indices AND reversed vertex tuples.
    # Construct it independently on the reflected coordinate lists.
    opposite_joins = {}
    for (src,tgt), A in joins.items():
        rs = tuple(sorted(3-c for c in src))
        rt = tuple(sorted(3-c for c in tgt))
        src_keys = opposite_keys[rs]
        tgt_index = {key:i for i,key in enumerate(opposite_keys[rt])}
        entries = {}
        for j,(labels,blocks) in enumerate(src_keys):
            out = [blocks[0]]
            for cut,block in zip(rs,blocks[1:]):
                if cut in rt:
                    out.append(block)
                else:
                    out[-1] += block
            label = tuple(labels[rs.index(c)] for c in rt)
            entries[tgt_index[label,tuple(out)],j] = 1
        op = s.SparseMatrix(len(keys[rt]),len(keys[rs]),entries)
        opposite_joins[src,tgt] = op
        assert reversal[tgt]*A == op*reversal[src]
        assert reversal[src]*mates[src,tgt] == op.T*reversal[tgt]

    # Actual event incidence, evaluated in independent complex sheet fixtures.
    features = [(1+(i+1)*s.I, i+2-s.I) for i in range(7)]
    # Endpoint-block embedding and prescribed dual-observation extraction.
    local_embedding, local_extraction = {}, {}
    for a in ENDS:
        for p in (2,3,5):
            b = a*p
            if b not in POS or (a//2) % p == 0:
                continue
            g = s.Matrix([sum(features[k][j] for k in range(POS[a],POS[b])) for j in range(2)])
            norm = s.simplify((adjoint(g)*g)[0])
            embed = s.Matrix([[1,0],[0,g[0]],[0,g[1]]])
            extract = s.Matrix([[1,0,0],[0,s.conjugate(g[0])/norm,s.conjugate(g[1])/norm]])
            assert clean(extract*embed) == s.eye(2)
            local_embedding[a,b], local_extraction[a,b] = embed, extract
    assert len(local_embedding) == 12
    # Every path block, including typed identities, in the three-prime cube.
    paths = []
    def enumerate_paths(vs):
        paths.append(vs)
        for a,b in local_embedding:
            if a == vs[-1]:
                enumerate_paths(vs+(b,))
    for a in ENDS:
        enumerate_paths((a,))
    marked_count = 0
    for vs in paths:
        embed, extract = s.ones(1), s.ones(1)
        for edge in zip(vs,vs[1:]):
            embed = s.kronecker_product(embed,local_embedding[edge])
            extract = s.kronecker_product(extract,local_extraction[edge])
        assert clean(extract*embed) == s.eye(2**(len(vs)-1))
        marked_count += 2**(len(vs)-1)
    assert len(paths) == 38 and marked_count == 128
    full = (1,2)
    entries = {}
    chosen = {}
    for r,vs in enumerate(routes):
        event_features = [tuple(sum(features[k][j] for k in range(POS[a],POS[b]))
                                for j in range(2)) for a,b in zip(vs,vs[1:])]
        for m,mask in enumerate(masks):
            col = 8*r+m
            slots = [(((),1),) if not keep else tuple(((j,),g[j]) for j in range(2))
                     for keep,g in zip(mask,event_features)]
            for selection in product(*slots):
                block = tuple(w for w,c in selection)
                coefficient = s.expand(s.prod(c for w,c in selection))
                row = index[full][(vs[1:3],block)]
                entries[row,col] = coefficient
            picked = tuple((0,) if keep else () for keep in mask)
            row = index[full][vs[1:3],picked]
            chosen[col,row] = 1/entries[row,col]
    observation = s.SparseMatrix(len(keys[full]),48,entries)
    left_inverse = s.SparseMatrix(48,len(keys[full]),chosen)
    assert clean(left_inverse*observation) == s.eye(48)
    signs = (-1,1,1,-1,-1,1)
    ghosts = [s.Matrix([signs[i//8] if sum(masks[i%8])==degree else 0 for i in range(48)])
              for degree in (0,1)]
    signature = s.SparseMatrix(len(keys[full]),len(keys[full]),{
        (i,i):(-1)**sum(map(sum,blocks)) for i,(_,blocks) in enumerate(keys[full])})
    positive_hilbert = Q[full]*signature
    marginal = s.SparseMatrix.vstack(joins[full,(1,)], joins[full,(2,)])
    marginal_form = s.SparseMatrix(s.diag(Q[(1,)], Q[(2,)]))
    marginal_mate = Qinv[full]*adjoint(marginal)*marginal_form
    assert marginal_mate == s.SparseMatrix.hstack(mates[full,(1,)], mates[full,(2,)])
    assert -adjoint(marginal)*marginal_form == Q[full]*(-marginal_mate)
    dual_witness_norms = []
    ghost_images = []
    for g in ghosts:
        x = clean(observation*g)
        assert x != s.zeros(len(keys[full]),1)
        ghost_images.append(x)
        assert clean(marginal*x) == s.zeros(marginal.rows,1)
        eta = signature*x  # Prescribed signed-dual observation, not a fitted form.
        value = s.simplify((adjoint(x)*Q[full]*eta)[0])
        assert value == s.simplify((adjoint(x)*positive_hilbert*x)[0])
        assert value > 0
        dual_witness_norms.append(str(value))
        for cut in ((1,),(2,),()):
            assert clean(joins[full,cut]*x) == s.zeros(len(keys[cut]),1)
            assert clean(adjoint(x)*Q[full]*mates[full,cut]) == s.zeros(1,len(keys[cut]))

    cross = s.Matrix(2,2,lambda i,j:s.simplify((adjoint(ghost_images[i])*Q[full]*signature*ghost_images[j])[0]))
    assert cross == s.diag(*(s.sympify(n) for n in dual_witness_norms))

    # Independent complex marked-arrow differential and its wrong-sign control.
    ws = words(3)
    wi = {w:i for i,w in enumerate(ws)}
    feature = (1+2*s.I,3-s.I)
    creation = s.SparseMatrix(15,15,{(wi[w+(j,)],wi[w]):feature[j]
        for w in ws if len(w)<3 for j in range(2)})
    sharp = clean(Qinv[()]*adjoint(creation)*Q[()])
    direct = s.SparseMatrix(15,15,{(wi[w],wi[w+(j,)]):TAU**2*(-1)**j*s.conjugate(feature[j])
        for w in ws if len(w)<3 for j in range(2)})
    assert sharp == direct
    assert -adjoint(creation)*Q[()] == Q[()]*(-sharp)
    assert -adjoint(creation)*Q[()] != Q[()]*sharp

    result = {
        "schema":"marici.nima.three-prime-reduced-cut-duality.v1", "passed":True,
        "fixture_dimensions_with_typed_label_summands":{str(k):len(v) for k,v in keys.items()},
        "nondegenerate_signed_forms":True,
        "contragredient_squares_and_dual_cone_signs":len(joins),
        "commutative_arrow_squares_and_dual_fiber_chain_maps":squares,
        "composition_checks_including_identities":triples,
        "opposite_rejoin_and_mate_naturality":True,
        "explicit_full_cut_left_inverse_on_48_marked_paths":True,
        "source_generated_local_extractions":len(local_embedding),
        "split_analytic_path_block_checks":{"typed_paths":len(paths),"marked_paths":marked_count},
        "fixture_typed_analytic_path_algebra_dimension":8+12*3+12*3**2+6*3**3,
        "both_marginal_ghosts_retained_then_killed_only_by_compression":True,
        "joint_dual_observers_outside_sum_of_marginal_mate_images":True,
        "stacked_marginal_cone_fiber_and_two_independent_dual_class_witnesses":True,
        "fixture_dual_witness_pairings_equal_positive_hilbert_norms":dual_witness_norms,
        "complex_creation_contraction_and_wrong_cone_sign_hostile":True,
        "scope":"Reduced signed fiber algebra, exact typed cut complexes, and local event-map fixture. The two-sheet fixture does not model injectivity of seven chamber vectors at one spectral point. Analytical faithfulness and finite derived extension are arguments in the accompanying note; no fully faithful stable functor, terminal isometry, or positive metric is claimed.",
    }
    out=ROOT/"research/nima/results/three-prime-reduced-cut-duality.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))


if __name__ == "__main__":
    main()
