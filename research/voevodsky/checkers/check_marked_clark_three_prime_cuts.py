"""Exact three-prime marked cut diagram; no analytic metric descent claim."""
from itertools import permutations, product
from collections import defaultdict
from pathlib import Path
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
LEVELS = ((), (1,), (2,), (1, 2))
ENDPOINTS = (2, 4, 6, 10, 12, 20, 30, 60)
POSITION = {n: i for i, n in enumerate(ENDPOINTS)}
MASKS = tuple(product((0, 1), repeat=3))


def vertices(route):
    out = [2]
    for p in route:
        out.append(out[-1]*p)
    return tuple(out)


def observe(vs, mask, cuts):
    letters = [tuple(range(min(POSITION[a], POSITION[b]), max(POSITION[a], POSITION[b])))
               if keep else (None,) for a, b, keep in zip(vs, vs[1:], mask)]
    bounds = (0,) + cuts + (3,)
    out = defaultdict(int)
    for chosen in product(*letters):
        blocks = tuple(tuple(i for i in chosen[a:b] if i is not None)
                       for a, b in zip(bounds, bounds[1:]))
        out[(tuple(vs[c] for c in cuts), blocks)] += 1
    return dict(out)


def forget_key(key, source, target):
    labels, blocks = key
    out = [blocks[0]]
    for position, block in zip(source, blocks[1:]):
        if position in target:
            out.append(block)
        else:
            out[-1] += block
    return tuple(labels[source.index(c)] for c in target), tuple(out)


def push(column, function):
    out = defaultdict(int)
    for key, coefficient in column.items():
        out[function(key)] += coefficient
    return {k: v for k, v in out.items() if v}


def reverse_key(key):
    labels, blocks = key
    return labels[::-1], tuple(word[::-1] for word in blocks[::-1])


def gram(columns):
    # Real rational coordinate Gram is only a rank-computation device.
    # It is not the Clark metric.
    return s.Matrix(len(columns), len(columns), lambda i, j:
                    sum(v*columns[j].get(k, 0) for k, v in columns[i].items()))


def feature_words(cap):
    return [word for n in range(cap+1) for word in product(range(4), repeat=n)]


def signed_record_tests():
    C = s.SparseMatrix(s.Matrix([[0,0,-1,1],[0,0,-1,1],[-1,-1,0,0],[1,1,0,0]])/2)
    tau = s.Rational(1, 2)
    powers = [s.SparseMatrix([[1]])]
    for n in range(3):
        powers.append(s.SparseMatrix(s.kronecker_product(powers[-1], tau**2*C)))
    keys, forms = {}, {}
    for cuts in LEVELS:
        bounds = (0,) + cuts + (3,)
        caps = tuple(b-a for a, b in zip(bounds, bounds[1:]))
        keys[cuts] = tuple(product(*(feature_words(cap) for cap in caps)))
        factors = [s.SparseMatrix(s.diag(*powers[:cap+1])) for cap in caps]
        form = factors[0]
        for factor in factors[1:]:
            form = s.SparseMatrix(s.kronecker_product(form, factor))
        forms[cuts] = form
    joins = {}
    for source in LEVELS:
        for target in LEVELS:
            if source == target or not set(target) < set(source):
                continue
            index = {k:i for i,k in enumerate(keys[target])}
            entries = {}
            for j, blocks in enumerate(keys[source]):
                _, output = forget_key((tuple(source), blocks), source, target)
                entries[index[output], j] = 1
            J = s.SparseMatrix(len(keys[target]), len(keys[source]), entries)
            joins[source, target] = J
            # Mate is the sum over all allowed degree splittings, not inverse.
            assert J.T*forms[target] == forms[source]*J.T
    full = (1, 2)
    for middle in ((1,), (2,)):
        assert joins[middle, ()]*joins[full, middle] == joins[full, ()]
        assert joins[full, middle].T*joins[middle, ()].T == joins[full, ()].T

    # Polarity on the actual four-port letters, with tensor-slot reversal.
    swap = (1, 0, 3, 2)
    reversals = {}
    for cuts in LEVELS:
        reflected = tuple(sorted(3-c for c in cuts))
        index = {k:i for i,k in enumerate(keys[reflected])}
        entries = {}
        for j, blocks in enumerate(keys[cuts]):
            output = tuple(tuple(swap[a] for a in word[::-1]) for word in blocks[::-1])
            entries[index[output], j] = 1
        R = s.SparseMatrix(len(keys[reflected]), len(keys[cuts]), entries)
        reversals[cuts] = R
        parity = s.SparseMatrix(len(keys[reflected]), len(keys[reflected]),
            {(i,i):(-1)**sum(map(len,k)) for i,k in enumerate(keys[reflected])})
        lower = parity*forms[reflected]
        assert R.T*lower*R == forms[cuts].conjugate()
        assert R.T*forms[reflected]*R != forms[cuts]  # hostile: missing lower sign
    for (source, target), J in joins.items():
        rs = tuple(sorted(3-c for c in source))
        rt = tuple(sorted(3-c for c in target))
        assert reversals[target]*J == joins[rs,rt]*reversals[source]
        assert reversals[source]*J.T == joins[rs,rt].T*reversals[target]

    # Creation mate at total record depth three, independent complex feature.
    words = feature_words(3)
    index = {w:i for i,w in enumerate(words)}
    g = s.Matrix([1+s.I, 2-s.I, -1+2*s.I, 3])
    cg = C*g
    creation, mate = {}, {}
    for word in words:
        if len(word) < 3:
            for j in range(4):
                creation[index[word+(j,)], index[word]] = g[j]
                mate[index[word], index[word+(j,)]] = tau**2*s.conjugate(cg[j])
    creation = s.SparseMatrix(85,85,creation)
    mate = s.SparseMatrix(85,85,mate)
    assert creation.conjugate().T*forms[()] == forms[()]*mate
    assert mate*creation != s.eye(85)
    return {"record_dimensions": {str(k):len(v) for k,v in keys.items()},
            "all_rejoin_green_mates": True, "mate_composition": True,
            "oriented_four_port_polarity_and_wrong_sign_hostile": True,
            "polarity_commutes_with_rejoins_and_mates": True,
            "complex_creation_green_mate_at_depth_three": True,
            "mates_asserted_invertible": False}


def main():
    routes = tuple(vertices(p) for p in permutations((2,3,5)))
    packets = [(vs, mask) for vs in routes for mask in MASKS]
    columns = {cuts:[observe(vs, mask, cuts) for vs,mask in packets] for cuts in LEVELS}
    results = {}
    for cuts in LEVELS:
        G = gram(columns[cuts])
        kernel = G.nullspace()
        for vector in kernel:
            combined = defaultdict(int)
            for c, column in zip(vector, columns[cuts]):
                for key, v in column.items():
                    combined[key] += c*v
            assert all(v == 0 for v in combined.values())
        results[str(cuts)] = {
            "rank":48-len(kernel), "nullity":len(kernel),
            "occupied_coordinates":len(set().union(*(set(c) for c in columns[cuts]))),
            "kernel_basis_sparse": [{str(i):str(v) for i,v in enumerate(vec) if v} for vec in kernel],
        }
        reflected = tuple(sorted(3-c for c in cuts))
        for (vs, mask), column in zip(packets, columns[cuts]):
            assert push(column, reverse_key) == observe(vs[::-1], mask[::-1], reflected)
            assert push(push(column, reverse_key), reverse_key) == column
    assert [results[str(c)]["rank"] for c in LEVELS] == [26, 36, 36, 48]

    rejoin_count = 0
    for source in LEVELS:
        for target in LEVELS:
            if not set(target) <= set(source):
                continue
            for column, expected in zip(columns[source], columns[target]):
                assert push(column, lambda k:forget_key(k, source, target)) == expected
            # Basiswise, not just on the 48 observed linear combinations.
            for key in set().union(*(set(c) for c in columns[source])):
                rs = tuple(sorted(3-c for c in source))
                rt = tuple(sorted(3-c for c in target))
                assert reverse_key(forget_key(key, source, target)) == forget_key(reverse_key(key), rs, rt)
            rejoin_count += 1
    for key in set().union(*(set(c) for c in columns[(1,2)])):
        direct = forget_key(key, (1,2), ())
        for middle in ((1,), (2,)):
            assert forget_key(forget_key(key, (1,2), middle), middle, ()) == direct

    # Joint observation at both one-cut levels, without their common refinement.
    joint = [{(cuts,key):v for cuts in ((1,), (2,)) for key,v in columns[cuts][i].items()}
             for i in range(48)]
    joint_gram = gram(joint)
    joint_rank = joint_gram.rank()
    # Six-edge cycle in the bipartite graph of first/second cut vertices.
    signs = (-1, 1, 1, -1, -1, 1)
    ghost0 = s.Matrix([signs[i//8] if sum(MASKS[i%8]) == 0 else 0 for i in range(48)])
    ghost1 = s.Matrix([signs[i//8] if sum(MASKS[i%8]) == 1 else 0 for i in range(48)])
    assert joint_rank == 46
    assert s.Matrix.hstack(ghost0, ghost1).rank() == 2
    full_gram = gram(columns[(1,2)])
    for ghost in (ghost0, ghost1):
        assert joint_gram*ghost == s.zeros(48,1)
        assert full_gram*ghost != s.zeros(48,1)
    unmarked = []
    for route in range(6):
        total = defaultdict(int)
        for col in columns[()][8*route:8*route+8]:
            for key,v in col.items():
                total[key] += v
        unmarked.append(dict(total))
    unmarked_rank = gram(unmarked).rank()
    assert unmarked_rank == 6
    result = {
        "schema":"marici.voevodsky.marked-clark-three-prime-cuts.v1", "passed":True,
        "shell_endpoints":ENDPOINTS, "routes":routes,
        "packet_order":"route-major, then lexicographic Boolean masks 000 through 111",
        "levels":results, "joint_one_cut_rank":joint_rank,
        "joint_one_cut_kernel_basis_sparse":[{str(i):str(v) for i,v in enumerate(g) if v} for g in (ghost0,ghost1)],
        "joint_kernel_description":"Alternating route cycle, on 000 and on the sum of 001,010,100; both survive the full two-cut observation.",
        "unmarked_terminal_rank":unmarked_rank,
        "cut_forgetting_checks_including_identities":rejoin_count,
        "basiswise_rejoin_coherence":True, "reflected_opposite_naturality":True,
        "signed_record_tests":signed_record_tests(),
        "scope":"Exact coefficient cut diagram and graded signed record identities. Analytic transfer uses the previously proved feature injectivity/bounds. No physical source access, nondegenerate metric, reciprocal spatial identification, or derived Clark functor is certified.",
    }
    out = ROOT/"research/voevodsky/results/marked-clark-three-prime-cuts.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    compact = {**result, "levels":{k:{a:b for a,b in v.items() if a!="kernel_basis_sparse"} for k,v in results.items()}}
    print(json.dumps(compact,indent=2))


if __name__ == "__main__":
    main()
