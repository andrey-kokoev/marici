# Does a parity-closed heptagon force eight-qubit compression?

## Status

**Follow-up:** `heptagon-normal-form-theorem.md` now gives a catalogue-independent, computer-assisted proof of the exact 22-vertex claim, with independently checked DRAT certificates. The investigation below records the preceding counterexample and the initially inconclusive probe.

**Not from parity closure, triangle-freeness, independence number at most six, and 6-regularity alone.** An explicit graph on **21** vertices satisfies all those conditions and needs **nine** qubits. This is not a counterexample to the precise 22-vertex theorem.

## A catalogue-independent counterexample

Take vertices in Z/21Z and join i to j exactly when

    j - i ∈ {±1, ±4, ±6} mod 21.

This graph is 6-regular.

### Triangle-free

Let D={1,4,6,15,17,20}. A triangle would require a,b,a+b in D. Direct addition modulo 21 gives D ∩ (D+D)=∅.

### No independent seven-set: a short gap proof

Suppose seven selected vertices were independent. Let their seven clockwise gaps be g_1,...,g_7, with sum 21.

1. Each gap is at least 2, since distance 1 is an edge. No gap is 4 or 6.
2. Two consecutive gaps cannot both be 2: their endpoints would have distance 4. They cannot both be 3: their endpoints would have distance 6.
3. Let a count gaps equal to 2, b count gaps equal to 3, and c count all other gaps (which are at least 5). On a cyclic list of length seven, the preceding prohibition gives a≤3 and b≤3.
4. Since a+b+c=7, the gap sum is at least 2a+3b+5c=21−a+2c. Thus a≥2c, so c≤1.
5. If c=0, then a+b=7 contradicts a,b≤3. If c=1, then a=b=3, and the seventh gap must be 21−3·2−3·3=6, also forbidden.

Therefore no independent seven-set exists. The vertices {0,2,5,7,10,12} form an independent six-set, so the independence number is exactly six.

### Three parity-closed heptagons

Each residue class modulo 3 induces a seven-cycle, traversed in steps of +6. Every vertex of the entire graph has **exactly two** neighbors in each residue class: two of its six allowed jumps land in each class. Thus all three cycles are parity-closed.

Their supports are disjoint and partition the vertex set. They give three independent kernel vectors. The all-vertices relation is their sum, not an additional independent relation. Direct induced-cycle search confirms these are the only parity-closed induced seven-cycles in this graph.

### Exactly nine qubits: a circulant proof

Over F₂, the circulant adjacency map is multiplication by

    p(x)=x+x⁴+x⁶+x¹⁵+x¹⁷+x²⁰

on F₂[x]/(x²¹+1). For multiplication by p modulo f, the kernel dimension is deg gcd(p,f): writing p=d·p' and f=d·f' with coprime p',f', the condition f | p·v is equivalent to f' | v. Here the Euclidean algorithm gives

    gcd(p(x),x²¹+1)=x³+1.

Hence nullity=3, rank=21−3=18, and the minimum Pauli register has **nine qubits**. The three cycle relations are the entire kernel; no hidden additional relations are available. The script verifies the polynomial gcd independently of binary matrix elimination and constructs the nine-qubit operators.

## Why 22 is a genuine boundary

A graph-only lemma follows from the original hypotheses, without a catalogue or SAT solver.

Let S be a parity-closed induced C7 in a triangle-free graph with no independent seven-set. Every outside vertex has an independent neighborhood in S. Since α(C7)=3 and this neighborhood has even size, it has **zero or two** vertices. Also every graph vertex has degree at most six, since its neighborhood is independent.

Write z for the number of vertices outside S with no neighbor on S, and n for the graph order. Counting edges across S gives

    2(n−7−z) = ∑_{v∈S}(deg(v)−2) ≤ 7·4 = 28,
    therefore z ≥ n−21.

Consequences:

- At n=21, z=0 is possible; the circulant counterexample realizes it.
- At n=22, **at least one vertex is completely nonadjacent to the heptagon**.
- At n=22, if z=1, equality forces every vertex on the heptagon to have degree six. It does not by itself force every outside vertex to have degree six.

The two known eight-qubit examples have z=1 for each of their four parity-closed heptagons. Proving that the 22-vertex assumptions force z=1 and then force the extra parity dependencies was the missing step at this stage. The subsequent normal-form computation supplies a computer-assisted proof; a short human-only derivation remains unavailable here.

## The 21-vertex example cannot simply be extended

There is now a simpler analytic obstruction: the starting graph is 6-regular. If a new vertex has an old neighbor, that old vertex has seven neighbors, which must be independent if triangle-freeness is maintained. If the new vertex is isolated, it joins an existing independent six-set. Either way avoidance fails.

The earlier finite verification remains a useful cross-check: it finds 112 independent six-sets. A new vertex can preserve triangle-freeness only if its neighborhood is independent, and it can avoid an independent seven-set only if that neighborhood meets every existing independent six-set.

The graph has 1,821 independent subsets, including the empty set. None meets all 112 six-sets: every candidate misses at least 26. Thus **no one-vertex extension preserves Ramsey avoidance**. This is an exhaustive finite certificate, not part of the analytic gap proof. The JSON stores a disjoint six-set witness for every candidate neighborhood.

For growth after changing existing relations, see `ramsey-extension-repair.md`: deletion alone is still insufficient, but an optimal eleven-change repair enables a 22nd vertex. Requiring a 6-regular destination raises the minimum to thirteen old-edge changes.

## Bounded 22-vertex SAT probe

`heptagon_forcing_probe.py` encodes:

- an induced C7 on the first seven vertices;
- triangle-freeness and exclusion of every independent seven-set;
- outside incidence types consisting of zero or two nonadjacent cycle vertices;
- maximum degree six (a redundant consequence of the Ramsey assumptions);
- safe symmetry breaking by sorting outside vertices by their cycle-neighborhood type.

The `two-zero` query asks whether two or more outside vertices can have zero neighbors on the cycle. It has 2,184 variables and 100,907 clauses. A 60-second Glucose4 run returned **UNKNOWN_TIMEOUT**, not UNSAT. This supplies neither a proof nor a counterexample. The run's statistics and CNF digest are saved in `heptagon-two-zero-probe.json`.

The baseline encoding is tested against a relabelled known 22-vertex example; the zero-count and sparse-graph restrictions are separately checked to reject that fixed example. These checks do not constitute a completeness proof of the SAT encoding.

## Reproduce

```sh
python research/chatgpt/ramsey/heptagon_near_extremal_counterexample.py
python -m unittest discover -s tests -p "test_heptagon_forcing.py"
uv run --with python-sat==1.9.dev22 -- python -m unittest discover -s tests -p "test_heptagon_forcing.py"
uv run --with python-sat==1.9.dev22 -- python research/chatgpt/ramsey/heptagon_forcing_probe.py --mode two-zero --seconds 60
```

The SAT package is optional and run in uv's isolated dependency environment. The counterexample, gap proof, polynomial calculation, and extension verification use only the Python standard library.

## Interpretation

The cheap examples are not explained merely by having seven-cycles with even incidence, nor by regularity. **Exact order and how the cycle relations overlap matter:** three disjoint cycles in the 21-vertex example exhaust a three-dimensional kernel; the overlapping cycles of the 22-vertex examples coexist with six independent relations. The subsequent `heptagon-normal-form-theorem.md` establishes the forced pattern and extra relations by a finite, independently checked computation. The earlier timeout recorded above is retained as historical evidence, not the final status.
