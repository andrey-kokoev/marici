# Native degree-two contraction: executed test and corrected acceptance criteria

Date: 2026-10-30  
Source snapshot: `andrey-kokoev/marici@cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c`  
Status: exact finite computations and algebraic counterexamples; no derived nuclear-shell or neutron-count law.

## Result

Two different constructions must be separated.

1. A degree-lowering map can be constructed by deleting exact native backtracks from reader histories. Its quadratic kernel has dimension five for eight root markings, but its cubic kernel has dimension fourteen, not seven. The other sixteen root markings already fail the quadratic count.
2. The root's three active coefficient modes can be transported consistently inside the complete five-slot native packet. If their symmetric polynomial algebra and standard quadratic contraction are then supplied, the resulting contraction commutes with native transport. This is a compatible induced construction, not a derivation of polynomial states or a trace operation from square-link fillings.

A further control corrects the proposed success criterion: the dimensions `5,7,9,...` alone do not establish the rotational harmonic representation. Even the one-axis operator `d²/dx²` on three-variable homogeneous polynomials has these kernel dimensions.

## 1. Source and execution

Ten source modules were extracted from the retained native-source archive. Their Git blob hashes were recomputed and matched the pinned manifest. The source modules were not edited.

New checks ran on Node.js 22.16.0 and Python 3.13.5, with SymPy 1.14.0 for exact rational matrix ranks. All 24 bijective root markings were tested. No isotope numbers or desired oscillator dimensions were used to generate paths.

The native-history experiment exhausts every rooted history of exactly zero through five operations for each marking. This is a complete bounded experiment, not an enumeration of all unbounded assemblies. A separate transport experiment visits every complete packet reachable within five operations and checks every outgoing transfer from packets at distance less than five.

## 2. First candidate: native histories

Let `W_k` be the rational vector space freely spanned by rooted native reader histories of exactly `k` operations. Every visited reader retains its chart, absolute origin, and full five-coordinate permutation. Length is an explicit candidate grading; it is not assumed to equal a physical excitation number.

Two populations were measured separately:

- all valid reader histories;
- histories for which the union of visited packets passes `rules.describe`, so occupied species and global C/M roles coexist consistently.

The latter need not yet be exit-certified. These are spaces of histories, not declared physical state spaces. Linearization over the rationals is an explicit construction.

### An available degree-two reduction

The pair

```text
P[0] --PN--> N[0] --inverse-PN--> P[0]
```

returns to the identical complete packet. This includes chart, origin, and coefficient permutation, not merely the same occupied cell. The reverse two-step pair, where composable, also returns to its starting packet.

Define `Q_k : W_k -> W_(k-2)` by summing over every deletion of an adjacent exact backtrack. Each deletion has coefficient one. This is a specified natural linearization of a native inverse pair; the source does not contain this linear operator as a primitive, and does not identify the two histories or occupied assemblies.

For `p=(v_0,...,v_k)`, delete the two edges at position `i` only when `v_i=v_(i+2)` as full packet IDs. A resulting history has the same start and end packets and unchanged absolute endpoint origin. Each shortened history was checked against the independently enumerated shorter level.

The only two-step complete returns encountered were PN/inverse-PN and inverse-PN/PN. Two reader phase advances are not a backtrack: even when chart and permutation repeat, the absolute origin has increased by two.

### Exact results

| Marking class | Number of markings | Degree | History dimension | Rank of Q | Kernel dimension |
|---|---:|---:|---:|---:|---:|
| Square-winding compatible | 8 | 1 | 2 | — | — |
| Square-winding compatible | 8 | 2 | 6 | 1 | 5 |
| Square-winding compatible | 8 | 3 | 16 | 2 | 14 |
| Square-winding compatible | 8 | 4 | 42 | 6 | 36 |
| Square-winding compatible | 8 | 5 | 110 | 16 | 94 |
| Other markings | 16 | 1 | 2 | — | — |
| Other markings | 16 | 2 | 4 | 1 | 3 |
| Other markings | 16 | 3 | 6 | 2 | 4 |
| Other markings | 16 | 4 | 10 | 4 | 6 |
| Other markings | 16 | 5 | 16 | 6 | 10 |

For comparison, three-variable homogeneous polynomial dimensions at degrees 1, 2 and 3 are 3, 6 and 10. The Laplacian ranks at degrees 2 and 3 are 1 and 3, with kernels 5 and 7.

All histories through degree three pass the native coexistence check, so those discrepancies cannot be attributed to inconsistent intermediate occupancy. In the eight-marking class, coexistence reduces dimensions at degrees four and five from 42 and 110 to 41 and 106; ranks remain 6 and 16. The corresponding kernels are 35 and 90. The sixteen-marking class is unchanged through degree five.

For the canonical marking, the six degree-two words are:

```text
PN, inverse-PN
PN, NE
PN, NN-phase-advance
PN, reader-phase-advance
reader-phase-advance, PN
reader-phase-advance, reader-phase-advance
```

In this order, `Q_2=[1,0,0,0,0,0]`. Its five-dimensional kernel is therefore a direct count of the five non-returning words, not a demonstrated traceless rank-two tensor space.

The eight-marking class is exactly the class whose root C-pair aligns with the retained octahedral diagonal partition `{0,2}|{1,3}`. This was checked for all 24 markings.

### Equal endpoints do not repair the construction

At degree three, identifying histories with the same complete endpoint reduces the canonical dimension from 16 to 14, not to 10. Endpoint equality is only a diagnostic quotient here; the native source retains alternative histories.

Moreover, the unit-weight deletion operator does not descend to that quotient at degree four. In temporal order, write `a=PN`, `b=inverse-PN`, and `t=NN-phase-advance`. The valid histories

```text
p1 = a b a t
p2 = a t b a
```

have exactly the same complete endpoint. Let `q=a t`. The first history has two deletable backtracks, while the second has one:

```text
Q(p1) = 2 q
Q(p2) = q.
```

Thus endpoint identification would identify inputs with unequal outputs. This is a counterexample to this operator descending through this quotient, not a theorem excluding every possible weighted operator or coherence quotient.

## 3. A native three-mode candidate does exist, but is not the local active face at every phase

The source defines active coefficient slots as follows:

```text
P: {0,1,2}
N: {1,2,3}
E: {3,2,4}
```

PN, inverse-PN and NE carry the full three-dimensional active subspace to the next active subspace. Reader phase advances and NN advances do not:

| Transfer | Source coordinates used by target active slots | Rank after restricting inputs to source-active modes |
|---|---|---:|
| PN | 1,2,0 | 3 |
| inverse-PN | 3,1,2 | 3 |
| NE | 3,2,1 | 3 |
| P reader advance | 2,3,0 | 2 |
| N reader advance | 3,4,1 | 2 |
| NN advance | 3,4,1 | 2 |

P phase advance brings source slot 3 into the active face; N phase advance brings source slot 4 into it. These are retained context slots, not newly created modes. Projecting to the instantaneous active face after each step therefore loses information.

### Transported boundary subspace

There is a precise alternative. Let `U_0` be the span of the root's three active coordinate basis vectors. A packet carries a permutation `pi`, with current slot `j` reading root slot `pi[j]`. Define

```text
U_p = span { e_j : pi[j] is in {0,1,2} }.
```

Every complete packet has a three-dimensional `U_p`. Every native transfer sends `U_p` exactly to `U_target`; the full packet data make this construction unambiguous, including absolute origins. The remaining two root-coordinate directions are still present in the full five-dimensional system and are not erased.

The check verified this on 1,088 native transfers across all 24 markings within the stated depth bound. At terminal E packets, projection of `U_p` onto the instantaneous active E face can have rank 1, 2 or 3. The transported three-mode subspace must not be conflated with the instantaneous readout.

### Conditional contraction

On each transported `U_p`, choose the root-induced coordinate pairing, and take homogeneous polynomial functions of degree `k`. This produces spaces of dimensions `binomial(k+2,2)` and a transported second-derivative contraction. In sorted local bases, transport is a permutation of three coordinates. It therefore commutes with the chosen Laplacian.

This was checked at degrees two and three on all 1,088 transfers, for a total of 17,408 monomial equivariance checks. Root mode identities, charts and absolute origins remain distinct throughout.

This is a positive compatibility result. It does not settle the original conjecture:

- These are coefficient modes, not an identified three-dimensional spatial vector representation.
- The symmetric polynomial algebra is an added observable construction; it is not the graded history space counted above.
- Transport compatibility permits any initial symmetric pairing to be transported in the same way. It does not uniquely select the isotropic pairing.
- No square-link filling was used to produce the degree-lowering operation.
- The full native source still has five coefficient directions. Selecting the root-active three-dimensional sector does not prove that all relevant physical states lie in it.

The exact computations are over rational coordinate bases. They extend to complex coefficients, but a complex bilinear contraction is not the same construction as a Hermitian norm or a physical angular-momentum action.

## 4. Why the earlier rank criterion was insufficient

For homogeneous degree-`k` polynomials in `x,y,z`, consider only

```text
D = d²/dx².
```

A basis of its kernel consists of monomials with x-exponent zero or one:

```text
f(y,z) + x g(y,z),
```

where `f` has degree `k` and `g` degree `k-1`. Hence

```text
dim ker D = (k+1) + k = 2k+1.
```

It is surjective onto degree `k-2`: each target monomial has a preimage obtained by increasing the x-exponent by two and dividing by the resulting second-derivative coefficient. Thus it has exactly the same ranks and kernel dimensions as the isotropic three-dimensional Laplacian, at every degree.

The experiment checked these three operators through degree six:

| Operator | Rank of its quadratic coefficient tensor | Kernel dimensions at k=2,...,6 |
|---|---:|---|
| `d²/dx² + d²/dy² + d²/dz²` | 3 | 5,7,9,11,13 |
| `d²/dx² + d²/dy²` | 2 | 5,7,9,11,13 |
| `d²/dx²` | 1 | 5,7,9,11,13 |

The rank of `D_k` as a map between polynomial spaces and the rank of the underlying 3-by-3 quadratic tensor are different quantities.

An even more general algebraic observation is that any nonzero constant-coefficient homogeneous quadratic differential operator is surjective between these homogeneous polynomial degrees over characteristic zero. Under the factorial-weighted monomial pairing, it is adjoint to multiplication by its nonzero quadratic symbol; multiplication is injective in the polynomial ring. The explicit one-axis example already suffices to invalidate rank-only acceptance.

Correct acceptance tests must include the actual symmetry action and pairing, not only the sequence `2k+1`.

## 5. What a single native square determines geometrically

The canonical four-sector square was reconstructed again directly from the pinned rules, not copied from an old drawing. Its four-step NN route returns to the same chart and permutation with origin increased by four.

In an orthonormal coordinate frame with z along its retained internal diagonal, the sum of outer products of its four centered equatorial vertices is

```text
M_square = diag(2,2,0).
```

This particular natural quadratic construction has rank two. It supplies a plane metric, not by itself a full isotropic three-dimensional one.

The coordinate-permutation symmetry preserving the chosen octahedral subdivision has eight elements. Solving for invariant symmetric quadratic tensors gives

```text
G = diag(a,a,b).
```

Thus even this full unmarked subdivision symmetry leaves two independent coefficients. Adding complete marks or an attached P cannot justify treating all tetrahedral permutations as symmetries of that fixed subdivision.

For comparison, all 24 vertex permutations of the unmarked regular tetrahedral seed leave only scalar multiples of the identity. Its four centered vertex vectors satisfy

```text
sum_i v_i v_i^T = I_3
```

in the source scale used here. The supplied regular Euclidean seed therefore already supports a metric trace. This does not establish that a square-link operation generates the trace, or that coefficient modes and spatial vectors are the same representation.

## 6. Conclusion and next precise requirement

The direct history/backtrack construction fails the proposed harmonic correspondence at degree three and is marking-dependent already at degree two. Equal-endpoint identification neither fixes the dimensions nor preserves the tested deletion operator.

A transported three-mode coefficient bundle is available and supports a compatible polynomial trace once the polynomial algebra and pairing are chosen. The unresolved part is now explicit: derive a native algebra of observables and a quadratic pairing, rather than inferring them from numerical dimensions.

A useful next construction would give a native observable map that:

1. identifies which three coefficient combinations, if any, transform as spatial vector modes;
2. derives the degree-two symmetric products and their relations from composition;
3. selects a nondegenerate isotropic pairing and shows that the native square operation induces its trace;
4. retains full phase/origin data and passes the cubic test before generalization.

These are not four independent numerical fits. They are the missing structure needed to interpret the existing transport-compatible polynomial construction as an intrinsic shell-state model.

No neutron excess, nuclear magic number, spin degree of freedom, energy ordering, or stability criterion is derived by this test.

## Reproduction

The accompanying ZIP contains the unmodified ten-module source snapshot, source hashes, new scripts, raw matrices, summary receipts and this note.

From its root:

```sh
node run/check_contraction.mjs
python run/analyze_contraction.py
node run/check_active_modes.mjs
```

Python requires SymPy; the executed version was 1.14.0. Scripts use paths relative to their own locations.

Principal outputs:

```text
run/native_contraction_raw.json
run/native_contraction_analysis.json
run/active_mode_analysis.json
```

## References and provenance

The new path counts, contraction matrices, counterexamples and symmetry calculations are original computations recorded in the accompanying receipts. Standard harmonic-polynomial and trace facts can be compared with:

- Sheldon Axler and Wade Ramey, *Harmonic Polynomials and Dirichlet-Type Problems*, Proceedings of the AMS 123 (1995), 3765–3773. Author page: https://axler.net/HarmonicPolynomials.html
- Christian J. Burnham and Niall J. English, *A New Relatively Simple Approach to Multipole Interactions in Either Spherical Harmonics or Cartesians, Suitable for Implementation into Ewald Sums*, International Journal of Molecular Sciences 21 (2020), 277. https://pmc.ncbi.nlm.nih.gov/articles/PMC7017380/
- Native source: https://github.com/andrey-kokoev/marici/blob/cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c/research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs
- Native phase protocol: https://github.com/andrey-kokoev/marici/blob/cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c/research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs
