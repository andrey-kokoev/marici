# Ramsey primitive, Golay completion, and the 2^11 cycle: consolidated research note

**Date:** 9 November 2026  
**Status:** exact finite constructions and obstructions, conditional structural theorems, and explicitly unresolved selection rules.  
**Research objective:** derive a *source-generated* Ramsey incidence/obstruction law from the original `R/G/0` rotation–reflection–composition primitive. Matching familiar graphs, code lengths, or group orders is not by itself a solution.

## Executive result

The most elementary mechanism uncovered is **XOR comparison with a cyclic rotation**:

\[
U=I+T\qquad(\text{over }\mathbb F_2).
\]

On a selected irreducible 11-dimensional constituent of the 23-position cyclic system, this is multiplication by a primitive element of \(\mathbb F_{2^{11}}\). It traverses all **2047 nonzero states** in one cycle and fixes zero. Swapping **two successor images**, an additional nonlinear operation, joins the orbit and fixed point into a **2048-state cycle**. The number eleven also appears as the orbit length of Frobenius doubling modulo 23, and the same 11-dimensional vector space is the syndrome space of the binary Golay code.

Three assertions must remain separate:

1. **Proved:** at modulus 23, a particular cyclic algebra admits a primitive `I+T` operator and an explicit 2048-cycle after one splice.
2. **Proved, conditional on a chosen completion rule:** the seven-position rotation quotient can be extended by sixteen quadratic-phase columns to the perfect binary Golay code; its 2048 syndromes, Witt heptads/octads, and Steiner properties are exact.
3. **Not proved:** the original retained `R/G/0` operation selects modulus 23, its degree-11 constituent, perfect-packing saturation, the quadratic phase extension, or the nonlinear zero splice. Nor is there a proved map from Golay incidence to the triangle-free/independence criterion determining \(R(3,k)\).

The third statement is the remaining research problem, not a minor implementation detail.

## I. Original objective and the five-symbol control

For \(R(3,k)\), a red graph on \(n\) vertices must be triangle-free and have independence number below \(k\). Thus \(R(3,5)=14\) is witnessed by a triangle-free 13-vertex graph with independence number four; \(R(3,7)=23\) means no corresponding triangle-free graph with independence number at most six exists on 23 vertices. A code with **23 coordinate positions** is not such a graph.

The five-symbol `RGR00` experiment gives a useful negative control:

- Cyclic translation together with the quarter-turn/reflection action produces the group \(\operatorname{AGL}(1,5)\) of order 20.
- The row orbit has **ten** states, naturally indexed by the unordered pairs of the five positions; the `G` position is the midpoint of the `R` pair.
- If disjointness of `R` pairs is *chosen* as graph adjacency, the result is the Petersen graph (10 vertices, triangle-free, independence number four, automorphism group \(S_5\)). The adjacency decoder is **not** forced by the orbit operations.
- The other invariant admissible decoder is two disjoint five-cycles, up to labeled variants. Neither can be extended, by ordinary induced graph extension, to a 13-vertex Ramsey witness. The Petersen variant reaches only 11 vertices.
- Pure relabelling, rotation and quotienting cannot create genuinely new independent states. Independent-family pairing and line-graph promotion do produce new records, but only after **additional rules** specifying the operands or incidence.

This branch established a methodological constraint: **the generator must derive its next incidence law; attaching recognizable graph-theoretic names to an orbit is not a derivation.**

Reproducible controls: `ramsey_five_symbol_primitive_test.py` and `ramsey_rgr00_source_promotion_audit.py`.

## II. Exact seven-position root

Take the original seven-symbol row `RGRGR00` and make the **explicit binary projection** \(R\mapsto1\), \(G,0\mapsto0\). It gives

\[
x=(1,0,1,0,1,0,0)\in\mathbb F_2^7.
\]

Let \(T\) be cyclic rotation of the seven positions. Direct elimination shows that the seven translates \(x,Tx,\ldots,T^6x\) are linearly independent; their XOR sum is the all-ones vector \(q\). Hence the source-generated invariant line \(\langle q\rangle\) has a six-dimensional quotient

\[
V=\mathbb F_2^7/\langle q\rangle,\qquad\dim V=6.
\]

The seven quotient columns \(h_j=[T^jx]\) have exactly one relation, \(\sum_{j=0}^6 h_j=0\). In particular, distinct subsets of at most three positions have different XOR sums: a collision would give a nonempty dependency involving at most six columns. Counting gives

\[
\sum_{i=0}^3\binom7i=1+7+21+35=64=2^6.
\]

Every quotient coordinate occurs exactly once. This is the perfect radius-three syndrome representation of the binary \([7,1,7]\) repetition code. **The repetition code is obtained from the quotient kernel**, not because the original seven rotated vectors span only one dimension: those vectors have rank **seven**.

**Assumptions:** the binary red-support projection, XOR as comparison composition, and the decision to quotient by the invariant all-ones direction. The geometric three-symbol primitive does not by itself impose all three.

## III. Eleven doubling phases: why 7 and 23 look alike

The map \(j\mapsto2j\pmod n\) partitions the nonzero residue positions into doubling orbits. At \(n=7\), these have lengths three and three; at \(n=23\), eleven and eleven. Negation/reflection exchanges the two nonzero orbits:

\[
7=1+3+3,\qquad23=1+11+11.
\]

For modulus 23, one orbit is

\[
1,2,4,8,16,9,18,13,3,6,12,1.
\]

The second is its negative. Equivalently, over \(\mathbb F_2\),

\[
X^{23}+1=(X+1)f(X)f^*(X),
\]
\[
f(X)=X^{11}+X^9+X^7+X^6+X^5+X+1,
\]
\[
f^*(X)=X^{11}+X^{10}+X^6+X^5+X^4+X^2+1.
\]

The two degree-11 factors are interchanged by reversal. At modulus seven, the analogous factors have degrees three and three.

**Crucial distinction:** the original seven-mark *perfect quotient* is six-dimensional, incorporating both three-dimensional constituents; the 23-position Golay *syndrome* is one selected eleven-dimensional constituent. The `3 -> 11` sector analogy does not itself define a morphism from seven positions to 23 positions. Reflection exchanges the two possible choices rather than choosing one.

## IV. The simple `I+T` mechanism and the 2047-state orbit

Work in the field \(K=\mathbb F_2[X]/(f)\), where \(f\) is the degree-eleven factor above. Put \(\zeta=[X]\), so \(\zeta^{23}=1\) and \(\zeta\ne1\), and take rotation as multiplication by \(\zeta\):

\[
T(v)=\zeta v,\qquad U(v)=(I+T)v=(1+\zeta)v.
\]

Write \(g=1+\zeta\). Exact arithmetic in \(K\) gives

\[
g^{2047}=1,\qquad g^{23}\ne1,\qquad g^{89}\ne1,
\]

and \(2047=23\cdot89\), with both factors prime. Thus \(g\) has multiplicative order **2047**. Its orbit on any nonzero vector exhausts \(K^\times\). Zero is fixed:

\[
0\mapsto0,\qquad1\mapsto g\mapsto g^2\mapsto\cdots\mapsto g^{2046}\mapsto1.
\]

The eleven-phase Frobenius relation is consistent with this longer orbit:

\[
U^{2^j}=I+T^{2^j},\qquad U^{2048}=U,\qquad U^{2047}=I.
\]

The last equality by itself establishes only a divisor bound; the two explicit proper-divisor tests above establish *exact* order 2047.

The same phenomenon has a lower-level control at modulus seven: on a selected degree-three cyclic constituent, `I+T` has nonzero orbit length seven, plus fixed zero, for a total of eight field states. These are **constituent sizes**, not the full six-dimensional, 64-syndrome quotient of Section II.

**What is simple here:** the operator is the sum of the identity and rotation in characteristic two. **What has not been derived:** why the original row operations should choose \(K\) and precisely this irreducible constituent.

## V. Joining the isolated zero: a 2048-cycle, but with an added rule

A linear map fixes zero, so \(U\) cannot be a single permutation cycle on all 2048 states. A minimal successor swap yields one:

\[
F(v)=\begin{cases}
1,&v=0,\\
0,&v=g^{-1},\\
g v,&\text{otherwise}.
\end{cases}
\]

The exact orbit is

\[
0\to1\to g\to g^2\to\cdots\to g^{2046}\to0.
\]

The checker visits **all 2048 states once** and returns to zero. The changed transitions are the two former outgoing edges from 0 and \(g^{-1}\). Such a swap is the minimum change required to join two disjoint permutation cycles. But **the splice point is selected externally**; any choice of a nonzero state can be used as the join.

The splice is nonlinear and is not obtained from linear rotation, reflection, quotienting, or the known retained-history compiler. No affine self-map of \(\mathbb F_2^{11}\) can have a 2048-cycle: representing an affine map as a homogeneous 12-by-12 binary matrix, its 2-power-order part is unipotent and has order at most \(2^4=16\). A 2048-cycle therefore demands a genuinely nonlinear or otherwise enlarged successor operation.

**Interpretation:** zero is a demonstrable *linear fixed-point obstruction*. It is not yet a Ramsey obstruction. A 2048-cycle can be produced by many unrelated permutations, so the cycle count alone is weak evidence for a distinguished Ramsey generator.

New exact checker: `check_ramsey_golay_2048_cycle.py`.

## VI. Golay's 2048 syndromes are a separate, intrinsic structure

The 23 field columns \(\zeta^j\), \(j=0,\ldots,22\), define an 11-by-23 parity-check map by expanding in the basis \(1,\zeta,\ldots,\zeta^{10}\). All subsets of at most three columns have **distinct** sums. Their number is

\[
1+23+\binom{23}{2}+\binom{23}{3}=2048=2^{11}.
\]

Hence the map exhausts the full syndrome space and its kernel is a binary \([23,12,7]\) perfect code: the binary Golay code. This result does **not** require the nonlinear splice from Section V. The 2048 syndromes exist even if zero stays fixed under the chosen linear dynamics.

Another 2048-set occurs in the extended \([24,12,8]\) Golay code: quotient the 4096 codewords by the all-ones word/complementation. Its complementary classes split as \(1+759+1288=2048\), comprising the zero/full class, octad/16-set pairs, and pairs of dodecads. This is **not the same quotient** as the 23-coordinate syndrome space unless an additional identification is given.

The exact Golay weight enumeration yields 253 weight-seven codewords. Their supports form \(S(4,7,23)\): every four-subset lies in a unique heptad. After parity extension, the 759 octads form \(S(5,8,24)\): every five-subset lies in a unique octad. The automorphism group of the latter design is \(M_{24}\). These are established Golay consequences, not a derivation of Ramsey numbers.

Checker: `check_golay_from_cyclic_squaring.py`.

## VII. A direct *conditional* construction of Golay from the seven-position root

The more geometrically relevant route starts not by specifying 23 positions, but with the six-dimensional space \(V\) of Section II. If we strengthen the source symmetries to the **full** permutation group on the seven distinguished directions, there is a canonical nondegenerate alternating form and quadratic refinement characterized by

\[
B(h_i,h_j)=1\quad(i\ne j),\qquad Q(h_i)=1.
\]

This is a plus-type six-dimensional quadratic space, isometric to the exterior-square coefficient space \(\Lambda^2\mathbb F_2^4\). Choosing an isometry, set

\[
\nu_2(z)=(z_1z_2,z_1z_3,z_2z_3,z_1z_4,z_2z_4,z_3z_4)
\quad(z\in\mathbb F_2^4).
\]

Attach all sixteen new columns

\[
g_z=(\nu_2(z),1,z)\in\mathbb F_2^6\oplus\mathbb F_2\oplus\mathbb F_2^4
\]

alongside seven old columns \((h_i,0,0)\). This gives

\[
7+2^4=23\text{ positions},\qquad6+1+4=11\text{ syndrome directions}.
\]

The constructor is **exactly** perfect: no nonzero dependency among the 23 columns has size six or less, while the original seven columns form a dependency. Therefore the kernel is a \([23,12,7]\) perfect code. Full enumeration recovers the Golay weight distribution and both Witt designs.

This is a constructive bridge from the seven-position *quotient* to Golay that does not insert a 23-column matrix. However, **adding the sixteen phase points with the quadratic map is an explicit new constructor**, not a theorem about the original `R/G/0` operations. Moreover, promoting cyclic/dihedral source symmetry to full \(S_7\) symmetry is an assumption, not a result of rotations and reflection alone.

Checker: `ramsey_heptad_quadratic_golay_constructor.py`.

## VIII. What is forced, and what is not

### Under *perfect three-mark saturation*, 7 -> 23 is forced

If an \(n\)-position binary syndrome system represents every subset of at most three marked positions **exactly once**, then

\[
\sum_{i=0}^3\binom ni=2^r
\quad\Longleftrightarrow\quad
(n+1)(n^2-n+6)=6\cdot 2^r.
\]

For \(n\ge7\), this equation permits only \(n=7\) and \(n=23\). A short proof: put \(a=n+1\), \(b=a^2-3a+8\). Since \(ab=3\cdot2^{r+1}\), both factors are products of powers of 2 and at most one factor 3. If \(16\mid a\), then \(b\equiv8\pmod{16}\) and so \(b=8\) or 24, impossible for \(a\ge16\). Therefore \(a\in\{1,2,4,8,3,6,12,24\}\); checking these values yields the result. Thus the **next larger perfect** system after seven has 23 positions and 11 syndrome dimensions.

### Under perfect saturation and old-quotient retention, `1+4` is forced

Assume the 23-column rank-11 system contains the original six-dimensional seven-column subspace. The projections of the sixteen new columns to the five-dimensional quotient must be distinct, nonzero and three-sum-free. A 16-element sum-free subset of \(\mathbb F_2^5\) is necessarily an affine hyperplane. In suitable coordinates its points are exactly \((1,z)\), \(z\in\mathbb F_2^4\). Hence the **parity bit + four phase coordinates** are forced under these assumptions.

### The quadratic decoder and perfect saturation are **not** forced by the source

An eight-position extension exists that retains all seven source columns and all their \(S_7\) symmetry, while preserving collision-freedom for configurations of at most three marks: simply append the column \((0,1)\) to \(V\oplus\mathbb F_2\). It has **93** distinct syndromes in a 128-state space. Therefore symmetry + retention + uniqueness do **not** force a sixteen-position jump; the missing premise is *saturation*.

Even after saturation selects the affine 16-point projection, the six-coordinate function \(f:\mathbb F_2^4\to V\) is not proved unique. Collision-freedom requires that each affine parallelogram second difference \(D_aD_b f(z)\) be a nonzero isotropic vector for the specified quadratic form. The quadratic choice \(f=\nu_2\) works: these differences are \(a\wedge b\). Thirty restricted single-coordinate cubic/quartic perturbations fail, but that is not an exhaustive uniqueness theorem.

A different failed shortcut is to combine two independent six-dimensional seven-position fields and quotient away one shared direction to obtain eleven dimensions. Every nonzero one-dimensional quotient creates a collision among at-most-three-mark syndromes: the 470 such syndromes from the fourteen columns have differences covering the entire 12-dimensional space.

Checker: `check_seven_frame_completion_necessity.py`.

## IX. Orientation and group action: a promising clue, not a mechanism

A Golay heptad has stabilizer \(2^4:A_7\) in \(M_{23}\), with the normal \(2^4\) acting regularly on the other sixteen points. The group-theoretic orbit decomposition matches the constructed \(7+16\) geometry. A seven-cycle is an even permutation of the heptad; a seven-position reflection, fixing one position and swapping three pairs, is odd. Therefore that reflection cannot be an **internal** symmetry of a fixed Golay heptad within this stabilizer.

This suggests an **orientation-sensitive selection** between mirror-related presentations. It does not demonstrate that the native retained comparison algebra detects the relevant obstruction, nor that the mismatch *forces* the quadratic map or the 2048-cycle splice. An arbitrary coordinate relabelling can carry a code to an equivalent code without being an automorphism of the fixed labeled heptad.

## X. Where this stands relative to Ramsey

The exact algebra presently explains two independent phenomena:

- a canonical six-dimensional quotient of one **chosen binary reading** of the seven-symbol primitive, perfectly representing all three-mark configurations;
- a **conditional** quadratic completion that produces the Golay code, together with a selected 11-dimensional cyclic constituent carrying an elementary 2047-state linear cycle and an optional nonlinear full 2048-cycle.

It does **not** explain \(R(3,7)=23\). In fact, for that Ramsey number, the 23rd vertex is where triangle-free/independence-\(\le6\) realizations become impossible; it is not the size of a valid extremal witness. Any proposed bridge must encode an **obstruction** at 23 or construct an admissible graph on 22 vertices and prove 23 impossible. It must not simply identify Golay coordinate positions with graph vertices.

There is no corresponding derivation of \(R(3,8)=28\), much less a general formula for \(R(3,k)\).

## XI. The most economical next decisive test

Test only the original retained-comparison composition interface; do **not** import a Golay parity-check matrix, a perfect-packing rule or an arbitrary nonlinear cycle repair.

1. **Infer the actual binary operation, if any.** Does typed composition on source histories descend to XOR on the seven-dimensional red-support representation? If it does not, the current algebraic branch is a model choice rather than a generated mechanism.
2. **Infer the next-state admission law.** Does composition require all comparison states to be occupied (perfect saturation), or does it allow the explicit eight-position/93-of-128 counterexample? This is the first falsifier of the proposed forced Golay jump.
3. **If saturation follows, infer the comparison tensor.** Show that source operations imply \(D_aD_b f(z)=a\wedge b\), rather than only the weaker nonzero-isotropic condition. This would select the quadratic decoder up to affine gauge.
4. **Only then test the zero-state successor.** Determine whether the retained zero/empty configuration has a uniquely typed closure transition; absent such a law, the 2048-cycle remains a deliberately spliced permutation.
5. **Finally require a Ramsey readout.** Derive binary adjacency satisfying the red-triangle and blue-\(K_k\) requirements, without graph edges or target Ramsey values supplied as input. Check 22/23 at \(k=7\), then the independent next threshold 28 at \(k=8\).

**Single most valuable question:** *Does the source-defined retained-comparison law force perfect three-mark saturation or a specific zero-closure transition?* These are two mathematically distinct claims, and either can be falsified before attempting another large construction.

## Evidence and reproduction

All checked finite results in this note can be reproduced from the scripts already created in the Ramsey research session:

```sh
python check_ramsey_golay_2048_cycle.py
python ramsey_five_symbol_primitive_test.py
python ramsey_rgr00_source_promotion_audit.py
python ramsey_heptad_quadratic_golay_constructor.py
python check_golay_from_cyclic_squaring.py
python check_seven_frame_completion_necessity.py
```

Earlier research notes: `ramsey_five_symbol_source_orbit_and_missing_vertex_operation_2026-11-09.md`, `ramsey_golay_cyclic_squaring_test_2026-11-09.md`, `ramsey_seven_frame_quadratic_golay_completion_2026-11-09.md`, `ramsey_golay_completion_necessity_2026-11-09.md`.

Related Marici source-defined constructors (repository `andrey-kokoev/marici`): `research/nima/recursive-independent-family-comparison.md`, `research/nima/promotion-factor-independence.md`, `research/nima/record4-spectral-promotion.md`, `research/nima/spectral-record-successor-constructor-search.md`, `research/nima/triangle-comparison-feedback-cycles.md`. Their joint lesson is that grouping and re-promotion do not by themselves create independent operands; independent comparison and higher-order incidence require admitted, typed rules. The 2048 splice is **not** an existing verified native constructor in these inspected sources.

### Evidence labels

- **Exact:** proved algebraically and/or checked by exhaustive finite arithmetic in the listed scripts (orbit cardinalities, code dimensions, syndrome uniqueness, weight distributions, Steiner counts, 2047 orbit and 2048 splice).
- **Conditional theorem:** the 23-length and 16-point affine hyperplane results, *assuming* perfect three-mark saturation and old-quotient retention.
- **Model choice:** binary red-support projection, XOR composition, full \(S_7\) symmetry, quadratic sixteen-point promotion, the choice of irreducible 11-dimensional sector, and the nonlinear splice.
- **Open:** selection of those choices by the original retained operation, and any logically sufficient link to Ramsey thresholds.
