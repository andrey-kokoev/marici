# Coherent packet growth and irreducible hidden channels

## Results

Fixed-position insertion and label deletion preserve every order of the route-signature filtration. Their observer updates are explicit integer linear maps on signature coordinates. The resulting packet-growth maps satisfy the source composition identities.

The kernel growth separates into inherited hidden information and new correlations between insertion slots:

| growth | signature order | old hidden dimension | inherited across all slots | new cross-slot dimension | new total hidden dimension |
|---|---:|---:|---:|---:|---:|
| 4→5 | 1 | 6 | 30 | 40 | 70 |
| 5→6 | 1 | 70 | 420 | 170 | 590 |
| 5→6 | 2 | 0 | 0 | 90 | 90 |

Every one of the ninety six-prime degree-two hidden modes vanishes under deletion of any label. These are genuine six-label correlations in this signature kernel.

As an S₆ representation, this kernel is induced from the sign character on three independent pair reversals. It has seven irreducible types. We construct and exactly certify all seven central isotypic projectors.

## 1. Source spaces and observations

For a finite label set L, let V_L be the complex vector space with basis all linear orders of L. A basis element is a full route through the Boolean cube on L. Give it the orthonormal route-counting metric.

Let A_(L,k) record ordered-edge signatures through degree k, including total mass at degree zero. Set

\[
K_{L,k}=\ker A_{L,k},\qquad Q_{L,k}=V_L/K_{L,k}.
\]

Q is the observable quotient, canonically isomorphic to the image of A. Under the counting metric it is also canonically represented by K-perp.

Relabelling L permutes the route basis and the edge-signature coordinates. Hence K and Q carry unitary actions of the label-permutation group.

For |L|=d, write V_d, K_(d,k), and Q_(d,k) after fixing the standard labels 0,…,d−1.

## 2. Fixed-slot insertion preserves and reflects invisibility

Let a be a new label and s∈{0,…,d}. Define

\[
I_s^a(w_1\cdots w_d)
=w_1\cdots w_s\,a\,w_{s+1}\cdots w_d.
\]

Let D_a delete a from every route and extend linearly. Then

\[
D_aI_s^a=\operatorname{id}.
\tag{1}
\]

### Deletion preserves signature order

On edge letters, deletion maps an a-edge to zero and every other edge (S,j) to (S minus {a},j). Applying this alphabet map tensorwise sends each source signature to the signature of the deleted route. Thus every degree-r observation after deletion is a linear combination of degree-r observations before deletion.

Consequently

\[
D_a K_{d+1,k}\subseteq K_{d,k}.
\tag{2}
\]

### Insertion preserves signature order

Consider one degree-r target coordinate, a prescribed tuple of r observed edges.

If it contains no a-edge, remove a from its source masks. The resulting old edges must be on the correct side of the fixed insertion slot. Compatible tuples give an old degree-r coordinate; incompatible ones give zero.

If it contains an a-edge (S,a), its mask requires that the old route pass through S at cut s. The other r−1 edges pull back as above. For s<d, the cut event is the sum of its mutually exclusive outgoing edge events:

\[
1_{\text{cut state }S}
=\sum_{j\in L\setminus S}1_{\text{edge }(S,j)}.
\tag{3}
\]

Multiplying these cylinder constraints and discarding incompatible tuples gives a linear combination of old signature coordinates of degree at most r. Repeated identical edge constraints are idempotent. At the terminal cut the mask is fixed and the extra constraint is scalar.

Therefore there is an explicit coordinate map R_s such that

\[
A_{d+1,k}I_s^a=R_s A_{d,k}.
\tag{4}
\]

It follows that

\[
I_s^aK_{d,k}\subseteq K_{d+1,k}.
\]

Combining this with (1)–(2) gives the exact equivalence

\[
\boxed{x\in K_{d,k}\iff I_s^a x\in K_{d+1,k}.}
\tag{5}
\]

A fixed-slot insertion preserves both visibility and invisibility at the same signature order.

### Executable coordinate compiler

`prime_packet_signature_transport.py` implements the pullbacks:

- `insertion_pullback(feature, old_count, slot)`;
- `deletion_pullback(feature, old_count)`.

Each returns an integer linear combination of old/source signature coordinates. The checker certifies every order-zero, order-one, and order-two coordinate in the five-to-six transition, for all six insertion slots and all 120 old and 720 new routes. There are 621 old and 2623 new coordinates including mass. Every compiled update preserves the degree bound.

These identities hold on the admitted signature image. Redundant raw coordinate arrays represent a source packet only when they satisfy the image relations.

## 3. Composition coherence

Insert a at slot s and then b at slot t. An equivalent construction inserts b first:

\[
I_t^b I_s^a=
\begin{cases}
I_{s+1}^a I_t^b,&t\le s,\\
I_s^a I_{t-1}^b,&t>s.
\end{cases}
\tag{6}
\]

Both sides produce exactly the same labelled word. The identity is proved by tracking the two inserted positions. Repeated application compares any two schedules producing the same final labelled order.

Because these maps preserve K, all identities descend to Q. Higher comparison consistency follows from equality of the source word maps. The checker exercises all 720 two-insertion comparisons starting from four-label routes.

The induced observer system therefore has source-compatible insertion, deletion, relabelling, and their composition laws at each fixed signature order.

## 4. The growth exact sequence

Every (d+1)-route has a unique position for the new label a. Consequently

\[
V_{d+1}\cong\bigoplus_{s=0}^{d}I_s^a V_d.
\tag{7}
\]

The inherited hidden subspace is

\[
H=\bigoplus_{s=0}^{d}I_s^a K_{d,k}\subseteq K_{d+1,k}.
\]

Define the new cross-slot space

\[
B_{d,k}=K_{d+1,k}/H.
\]

Quotienting (7) gives the exact sequence

\[
\boxed{
0\longrightarrow B_{d,k}
\longrightarrow\bigoplus_{s=0}^{d}Q_{d,k}
\xrightarrow{R}Q_{d+1,k}
\longrightarrow0.
}
\tag{8}
\]

Here R combines the fixed-slot insertion maps. If r_(d,k)=dim Q_(d,k), then

\[
\dim B_{d,k}=(d+1)r_{d,k}-r_{d+1,k}.
\tag{9}
\]

Each summand map Q_d→Q_(d+1) is injective by (5). Kernel vectors of the combined map therefore express correlations among different insertion slots.

Substituting the certified ranks gives the table at the beginning. In particular, the six five-prime second-order observable blocks have dimension 6×120=720. Combining them into six-prime second-order observation gives dimension 630 and a ninety-dimensional cross-slot kernel.

## 5. Canonical metric splitting and bounds

Use the route-counting quotient metrics. The direct-sum identification (7) is unitary. Since H⊂K, there is an orthogonal decomposition

\[
K=H\oplus(K\cap H^\perp).
\]

Thus B has the canonical representative K∩H-perp, and (8) becomes

\[
\boxed{
\bigoplus_s Q_{d,k}
\cong Q_{d+1,k}\oplus B_{d,k}
}
\tag{10}
\]

by a unitary decomposition of H-perp. R is the orthogonal projection onto K-perp and is a coisometry: RR*=I.

This gives a recursive observer architecture:

1. retain the old observable packet in each insertion slot;
2. combine its visible part into the next packet;
3. retain the orthogonal cross-slot component as the new channels.

The energy identity is

\[
\|q_{slots}\|^2
=\|Rq_{slots}\|^2+\|P_Bq_{slots}\|^2.
\tag{11}
\]

These norms are the intrinsic quotient norms. The unweighted redundant signature-coordinate norm is a separately chosen measurement metric.

Fixed-slot insertion is an isometry on V, so its quotient map has norm at most one. D_a has norm sqrt(d+1), since its d+1 insertion positions are orthogonal and D_aD_a*=(d+1)I. Its quotient map has the same upper bound. From D_aI_s=I,

\[
\frac1{\sqrt{d+1}}\|q\|
\le\|\overline I_s q\|\le\|q\|.
\tag{12}
\]

Thus the single-slot recursive maps have explicit intrinsic stability bounds. Coordinate conditioning enters when these quotient representations are expressed through a chosen measurement matrix.

## 6. Every deletion kills the six-prime hidden modes

The degree-two six-prime kernel has basis h_B indexed by ordered triples of unordered pairs. Within a block,

\[
h_B=\sum_{\epsilon\in\{0,1\}^3}(-1)^{|\epsilon|}p_{B,\epsilon}.
\]

Fix any label a. It lies in one of the three pairs. The two orders of that pair become the same route after deleting a, while their coefficients have opposite signs. Therefore

\[
\boxed{D_a h_B=0\quad\text{for every label }a.}
\tag{13}
\]

All ninety modes vanish under every five-label marginal, and hence under all further deletions. They are six-label interactions in this particular signature kernel. The statement identifies a subspace of the common deletion kernel; it does not classify every possible deletion-invisible vector in the full route space.

The checker builds all six deletion matrices and verifies (13) on the entire ninety-column kernel basis.

## 7. Symmetry type of the ninety channels

Let H=(S₂)^3 be the subgroup reversing the three positional pairs of a reference route. Relabelling prime indices acts transitively on the ordered-pair blocks, with the internal reversal sign. Therefore

\[
\boxed{
K_{6,2}\cong\operatorname{Ind}_{(S_2)^3}^{S_6}
(\operatorname{sgn}\boxtimes\operatorname{sgn}\boxtimes\operatorname{sgn}).
}
\tag{14}
\]

Its dimension is 6!/8=90. The basis h_B/√8 is orthonormal, and relabelling acts by signed permutation matrices.

For a permutation with t disjoint transpositions and 6−2t fixed points, the character is

\[
\chi(t)=(-1)^t\frac{3!}{(3-t)!}\frac{(6-2t)!}{2^{3-t}}.
\]

Every other cycle type has character zero: an invariant two-element block permits only fixed points and transpositions. In order t=0,1,2,3 the values are 90,−18,6,−6.

Taking inner products with the irreducible characters gives:

| partition λ | irreducible dimension | multiplicity | isotypic dimension |
|---|---:|---:|---:|
| (3,3) | 5 | 1 | 5 |
| (3,2,1) | 16 | 2 | 32 |
| (3,1,1,1) | 10 | 1 | 10 |
| (2,2,2) | 5 | 1 | 5 |
| (2,2,1,1) | 9 | 3 | 27 |
| (2,1,1,1,1) | 5 | 2 | 10 |
| (1,1,1,1,1,1) | 1 | 1 | 1 |

The irreducible characters are computed by the Murnaghan–Nakayama recurrence, with exact class-size inner products and a full orthogonality check of the S₆ character table. The resulting dimensions sum to 90.

### Explicit spectral projectors

Let ρ(g) be the signed-permutation action in the parity basis. For each partition in the table define

\[
P_\lambda=\frac{\dim V_\lambda}{720}
\sum_{g\in S_6}\chi_\lambda(g^{-1})\rho(g).
\tag{15}
\]

The checker constructs all seven integer numerator matrices 720P_λ and verifies exactly:

\[
P_\lambda^2=P_\lambda,
\quad P_\lambda^*=P_\lambda,
\quad P_\lambda P_\mu=0\ (\lambda\ne\mu),
\quad\sum_\lambda P_\lambda=I.
\]

Their ranks are the isotypic dimensions in the table. These give canonical symmetry-organized hidden channels. Choosing individual bases within multiplicity spaces is an additional coordinate choice.

## 8. Restriction, deletion, and first-order birth types

Restricting the symmetry group from S₆ to the S₅ fixing one label keeps the same ninety-dimensional space. The branching rule gives

\[
\operatorname{Res}^{S_6}_{S_5}K_{6,2}
\cong
3V_{(3,2)}\oplus3V_{(3,1,1)}
\oplus6V_{(2,2,1)}\oplus6V_{(2,1,1,1)}
\oplus3V_{(1^5)}.
\tag{16}
\]

Physical label deletion maps these six-step route combinations into the five-step source space and sends this kernel to zero by (13). The two operations have distinct domains and purposes: (16) organizes symmetry, while (13) computes a source marginal.

The lower-order growth also has an explicit character formula. If g∈S_d has c cycles and f fixed labels, the edge permutation representation has character f·2^(c−1), and the vertex permutation representation has character 2^c. The boundary sequence gives

\[
\chi_{Q_{d,1}}(g)=f2^{c-1}-2^c+2.
\tag{17}
\]

Indeed, Q_(d,1) is the edge-chain space with boundary proportional to the fixed top-minus-bottom vector. Its character is edge minus vertex plus two trivial characters. The hidden character is the regular character minus (17).

For growth with one distinguished new label, (8) yields under the old S_d action

\[
\chi_{B_{d,1}}(g)
=(d+1)\chi_{Q_{d,1}}(g)
-\chi_{Q_{d+1,1}}(g\text{ fixing the new label}).
\tag{18}
\]

This gives

\[
B_{4,1}\cong6V_{(3,1)}\oplus2V_{(2,2)}\oplus6V_{(2,1,1)},
\quad \dim B_{4,1}=40,
\]

and

\[
B_{5,1}\cong12V_{(4,1)}\oplus6V_{(3,2)}
\oplus12V_{(3,1,1)}\oplus4V_{(2,2,1)},
\quad \dim B_{5,1}=170.
\]

The checker independently verifies (17) against the explicitly computed seventy-dimensional five-prime kernel, and computes the multiplicities in (18) exactly.

## 9. What is now reusable

The construction supplies a coherent family at every fixed signature order:

- a source route space;
- a hidden subspace and observable quotient;
- compiled insertion and deletion maps;
- exact source comparison identities;
- an inherited/new-channel exact sequence;
- a canonical counting-metric splitting;
- symmetry projectors on the new six-prime channels.

For the five-to-six second-order transition, the old slot-resolved packet has 720 coordinates. Its canonical split consists of 630 next-packet observable coordinates and ninety new hidden coordinates. The previously implemented Walsh observer reads precisely the latter, up to its declared normalization.

With the half-parity readout b=K^Tx/2, the normalized hidden coefficient is b/√2 and the hidden energy is ||b||²/2. This agrees with the orthogonal splitting (10) and the earlier balanced-completion Gram calculation.

The S_d symmetry used here relabels the combinatorial source indices. An arithmetic realization with numerical prime-dependent weights requires its own intertwiners. Operators commuting with the source symmetry preserve the isotypic blocks (15); other source operators are represented by the corresponding inter-block maps.

## 10. Verification and files

Run:

```
uv run --with python-flint python research/voevodsky/checkers/check_prime_packet_coherent_growth.py
```

Files:

- `research/voevodsky/prime_packet_signature_transport.py`: reusable integer coordinate compiler;
- `research/voevodsky/checkers/check_prime_packet_coherent_growth.py`: exact transport and character/projector checks;
- `research/voevodsky/results/prime-packet-coherent-growth.json`: ranks, characters, multiplicities, and verification results.

All tests use exact integer/rational arithmetic. The proofs above establish filtration preservation, the growth sequence, metric bounds, deletion cancellation, and representation identification. The finite checks certify the declared packet instances and the implemented coordinate updates.
