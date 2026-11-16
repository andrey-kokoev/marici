# Intrinsic Ramsey symmetry sectors and the noncanonical quarter-turn

9 November 2026 · Marici / Ramsey · exact finite analysis

## Question

Can the four-phase carrier in the verified 13→17 Ramsey witness be recovered from the old adjacency matrix alone, with neither a prescribed order-four automorphism nor a distinguished rotation center?

## Source and graph

Let \(G\) have vertex set \(\mathbb F_{13}\), with red edges
\(\{x,x+d\}\) for \(d\in\{\pm1,\pm5\}\). Let \(A\) be its 0–1 adjacency matrix. Exact bitset enumeration gives \(\alpha(G)=4\), and \(G\) has 26 red edges and 183 independent subsets (including the empty set). This is the 13-vertex lower-bound witness underlying the prior 13→17 sector construction.

## Result 1: complete symmetry and its 13 possible axes

The full automorphism group is

\[
\mathrm{Aut}(G)=\{x\mapsto b+mx:\ b\in\mathbb F_{13},\ m\in H\},
\qquad H=\{1,5,12,8\}=\langle5\rangle.
\]

It has order 52, with element-order distribution \(1:1,\ 2:13,\ 4:26,\ 13:12\). The 26 order-four elements comprise the two inverse rotations about each of 13 centers. An axis centered at \(c\) has the two directed quarter-turns

\[
\sigma_c^\pm(x)=c+5^{\pm1}(x-c)\pmod{13}.
\]

Every center is equivalent under the translation automorphisms. The full permutation centralizer of \(\mathrm{Aut}(G)\) is the identity alone. Consequently, **no isomorphism-natural deterministic assignment of one nontrivial permutation quarter-turn \(P(A)\) exists**. The full conjugacy family of quarter-turn axes *is* natural.

*Proof of the stronger linear statement.* A real matrix commuting with all translations must be circulant: \(M_{xy}=f(y-x)\). Commutation with multiplication by 5 requires \(f(d)=f(5d)\). The nonzero differences fall into three orbits of length four. Because \(5^2=-1\) modulo 13, each such orbit is stable under \(d\mapsto-d\), so \(M_{xy}=M_{yx}\). Hence **every real equivariant linear map is symmetric**. Any symmetric real \(P\) with \(P^4=I\) has eigenvalues \(\pm1\), so \(P^2=I\). No genuine, order-four equivariant real-linear quarter-turn exists without selecting a frame or supplying additional retained data.

## Result 2: three canonical four-dimensional spectral sectors

The characteristic polynomial, computed exactly over the integers, is

\[
\boxed{\det(tI-A)=(t-4)(t^3+t^2-4t+1)^4.}
\]

The cubic has three distinct real roots. Hence \(\mathbb R^{13}\) decomposes canonically into the \(4\)-eigenspace of dimension one and three pairwise different eigenspaces, each dimension four:

\[
\mathbb R^{13}=E_0\oplus E_1\oplus E_2\oplus E_3,
\qquad(\dim E_0,\dim E_1,\dim E_2,\dim E_3)=(1,4,4,4).
\]

The four-dimensional commutant is exactly \(\mathbb R[A]=\mathrm{span}_{\mathbb R}(I,A,A^2,A^3)\). A convenient exact matrix identity is

\[
A^4-3A^3-8A^2+17A-4I=0.
\]

These **intrinsic spectral sectors are not the same thing as the three four-cycles of vertices** arising after choosing a center. A canonical decomposition into invariant subspaces does not supply an oriented quarter-turn within those subspaces.

## Result 3: complete small orbit-attachment test

For a fixed center 0, consider equivariant attachments of \(q=1,2,4\) new vertices. Their old red neighborhoods are \(S,\sigma S,\ldots,\sigma^{q-1}S\) with \(S\) ranging over all 183 independent old-vertex subsets; the internal red graph is allowed to be any undirected graph invariant under cyclic permutation of the \(q\) new vertices. The exact triangle and independence constraints are applied with \(\alpha\le5\), without feeding the known threshold to the selector.

| New-vertex slots | Internal red patterns tested | Valid labeled attachment choices | Notes |
|---:|---:|---:|---|
| 1 | 1 | 183 | Every independent old neighborhood works. |
| 2 | 2 | 125 | 12 with a blue internal edge, 113 with a red edge. |
| 4 | 4 | 4 | All four use an internal red \(C_4\), and are quarter-turn images of the seed \(\{1,7,11\}\). |

The \(q=2\) count permits degenerate orbits of size dividing 2. No claim is made that these three candidate orbit sizes exhaust all other automorphism types (notably translations of order 13) or all attachment families.

The same complete \(q=4\) search for each of the thirteen axis centers returns four valid seeds per center, hence 52 center–seed pairs. They form **one orbit under the 52-element automorphism group**. The inverse generator simply reverses the new red four-cycle's phase order; it does not create a different unlabelled attachment.

This provides a **source-natural, set-valued carrier generator**: recover every order-four axis, generate all equivariant incidence candidates, test Ramsey compatibility, and quotient the surviving data by graph isomorphism. In the 13-vertex example, it gives one 17-vertex unlabelled completion **conditional on choosing the order-four attachment family**. It does not prove that a universal Ramsey successor must have four new vertices.

## Consequence for the Ramsey generator

The graph intrinsically fixes the \(1+4+4+4\) spectral decomposition. Selecting a particular quarter-turn axis, phase origin, and orientation is symmetry-breaking extra data. The earlier two-dimensional phase plus second-harmonic decoder provides coordinates for a **chosen** oriented sector; it does not independently select one of thirteen axis centers.

A universal global-order-four symmetry rule is also excluded by the previously enumerated 17-vertex Ramsey extremal graphs: six of seven have no order-four automorphism, including one with trivial automorphism group. A candidate general construction must therefore work with **families of local frames and partial transports**, not require a global automorphism on every predecessor.

## Falsifiable next conjecture

*Local-frame groupoid hypothesis.* Recover a canonical family of local cyclic frames from adjacency constraints (including when the full automorphism group is trivial); transport candidate incidence columns among overlapping frames; enforce exact triangle/independence compatibility before quotienting equivalent completed frames. In the 13-vertex case this family reduces to the 13 globally conjugate order-four axes. At 17 vertices it must be defined from source-supported local four-cycles and their overlap maps rather than global automorphisms.

This remains **a conjecture**, not a theorem of Ramsey thresholds. The current results give no formula for \(R(3,k)\), no universal attachment-size selection, and no extremality theorem.

## Reproduction

Run `python ramsey_axis_family_experiment.py` (Python and NetworkX). The checker independently counts all automorphisms and their orders, verifies the centralizer, enumerates every independent old neighborhood and all cyclic-invariant internal graphs at \(q=1,2,4\), and checks all 13 centers using exact integer-bitset independence-number calculations. The characteristic polynomial and displayed matrix polynomial can be verified separately with SymPy using the provided adjacency definition; no floating-point eigensolver is necessary for those identities.

Prior work: `ramsey_matrix_generator_current_position_2026-11-08.md`, `ramsey_quadratic_phase_to_incidence_2026-11-08.md`, `ramsey_partial_orbit_selector_test_2026-11-09.md`.
