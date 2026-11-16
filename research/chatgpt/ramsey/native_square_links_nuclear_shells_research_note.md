# Research note: native square links, triangular state spaces, and nuclear shell structure

**Date:** 2026-10-30  
**Status:** exploratory; arithmetic and standard shell-model identities verified; the proposed native-to-shell correspondence is unproved.

## Question

Can the involution-related square links in Marici's P/E/N construction induce a natural *contraction* of triangular state spaces, thereby explaining nuclear shell multiplicities and possibly neutron excess without introducing target counts as rules?

Three distinct numerical phenomena must remain separate:

1. **Atomic electron principal-shell capacity:** \(2n^2=2,8,18,32,50,72,\ldots\), a count of available single-electron states for principal quantum number \(n\).
2. **Conventional nuclear magic numbers:** \(2,8,20,28,50,82,126\), cumulative proton or neutron shell closures.
3. **Neutron excess:** \(N-Z\), determined mainly by competing nuclear contributions to energy, with shell, pairing, and other corrections. The earlier \(0,0,4,12,24\) sequence belongs to selected abundant noble-gas isotopes, not to universal nuclear shell closures or maximum neutron numbers.

## A. What the original planar construction counts

Take two length-\(n\) paths and triangulate their product grid. Every comparison square gives two triangular faces, so

\[
K_n=\operatorname{Tri}(\Gamma_n\times\Gamma_n),\qquad f_2(K_n)=2n^2.
\]

Exchanging the two factors gives an involution \(J(i,j)=(j,i)\); reversing a path order yields an involution on directed histories. The rhombus is divided into two reflected triangular halves with \(n^2\) small triangles each.

This explains the **combinatorics** of \(2n^2\), not electronic spin, nuclear particles, or energetic stability. In particular, local comparison squares are not automatically native commuting squares: the relation

\[
E_{i+1,j}\circ P_{i,j}=P_{i,j+1}\circ E_{i,j}
\]

is an additional condition until derived from native composition.

The total number of internal edges of this triangular tiling is \(3n^2-2n\). Interpreting every P–E shared edge as a potential neutron gives \(1,8,21,40,65,\ldots\), **not** the chosen isotope neutron sequence \(2,10,22,48,78\).

## B. Established nuclear oscillator counting

For the three-dimensional isotropic oscillator, degree-\(k\) states are indexed by nonnegative triples

\[
a+b+c=k.\]

Define the real polynomial state space

\[
V_k=\operatorname{Sym}^k(\mathbb R^3),\qquad
\dim V_k=\binom{k+2}{2}.
\]

There are two spin projections per orbital state for a fixed nucleon species. Thus the spin-inclusive capacity is

\[
g_k=2\dim V_k=(k+1)(k+2).
\]

| \(k\) | Spatial states \(\dim V_k\) | With spin \(g_k\) | Cumulative (one nucleon species) |
|---:|---:|---:|---:|
| 0 | 1 | 2 | 2 |
| 1 | 3 | 6 | 8 |
| 2 | 6 | 12 | 20 |
| 3 | 10 | 20 | 40 |
| 4 | 15 | 30 | 70 |
| 5 | 21 | 42 | 112 |
| 6 | 28 | 56 | 168 |

The first three closures, \(2,8,20\), agree with the conventional nuclear magic numbers. The remaining oscillator closures do not. A strong **spin–orbit interaction** changes the energetic ordering of the single-particle levels.

### Angular-momentum decomposition

In the standard oscillator representation, degree \(k\) includes the orbital sectors

\[
\ell=k,k-2,k-4,\ldots.
\]

The highest-\(\ell\) sector has \(2k+1\) spatial states. Coupling \(\ell=k\) to spin \(s=1/2\) yields

\[
 j=k+\tfrac12:\quad 2j+1=2k+2,
\qquad
 j=k-\tfrac12:\quad 2j+1=2k.
\]

The conventional shell-model ordering lowers the high-\(j\) branch; the resulting large shell gaps can be summarized as follows:

| Filled nuclear shell | Capacity | Cumulative |
|---|---:|---:|
| Oscillator \(k=0\) | 2 | 2 |
| Oscillator \(k=1\) | 6 | 8 |
| Oscillator \(k=2\) | 12 | 20 |
| High-\(j\) \(k=3\) (\(f_{7/2}\)) | 8 | 28 |
| Remainder of \(k=3\) plus high-\(j\) \(k=4\) (\(g_{9/2}\)) | 12 + 10 = 22 | 50 |
| Remainder of \(k=4\) plus high-\(j\) \(k=5\) (\(h_{11/2}\)) | 20 + 12 = 32 | 82 |
| Remainder of \(k=5\) plus high-\(j\) \(k=6\) (\(i_{13/2}\)) | 30 + 14 = 44 | 126 |

This reproduces the conventional magic sequence **when the known spin–orbit level ordering is supplied**. Multiplicities alone do not predict the size or placement of the energy gaps. Exotic neutron-rich nuclei may have modified closures.

## C. Exact contraction test

The usual Laplacian provides a degree-lowering map on polynomial spaces:

\[
\Delta_k=\partial_x^2+\partial_y^2+\partial_z^2:
V_k\longrightarrow V_{k-2}.
\]

For \(k\ge2\), this map is surjective over characteristic zero, so

\[
\dim\ker\Delta_k
=\binom{k+2}{2}-\binom{k}{2}=2k+1.
\]

The kernel consists of degree-\(k\) harmonic polynomials. It carries the orbital angular-momentum \(\ell=k\) representation. The full space decomposes as

\[
V_k=\mathcal H_k\oplus r^2\mathcal H_{k-2}\oplus
r^4\mathcal H_{k-4}\oplus\cdots,
\qquad \mathcal H_k=\ker\Delta_k.
\]

An integer-matrix rank calculation (monomial bases, exact arithmetic) gives:

| \(k\) | \(\dim V_k\) | \(\operatorname{rank}\Delta_k\) | \(\dim\ker\Delta_k\) |
|---:|---:|---:|---:|
| 0 | 1 | 0 | 1 |
| 1 | 3 | 0 | 3 |
| 2 | 6 | 1 | 5 |
| 3 | 10 | 3 | 7 |
| 4 | 15 | 6 | 9 |
| 5 | 21 | 10 | 11 |
| 6 | 28 | 15 | 13 |

**Established result:** the triangular integer-state spaces possess a natural contraction whose kernels have the correct rotational multiplicities \(2k+1\). The oscillator's wider \(U(3)\)/\(SU(3)\) symmetry organizes these spaces.

**Unproved hypothesis:** Marici square-link composition itself induces this map, rather than requiring the Laplacian to be imported. An involution \(J^2=I\) is degree-preserving; \(\Delta\) lowers degree by two. These are **not the same operator**. A native construction would have to build the degree-lowering map from composition or incidence data, then establish its kernel and symmetry.

## D. Native square-link evidence and obstruction

The earlier native P/E/N investigation established the following on the pinned source grammar:

- Native operations include PN, inverse-PN, NE, same-body reader phase advance, and NN phase advance, with full C/M marks, coefficient permutations, and absolute origins retained.
- The canonical four-sector winding has a geometric four-cycle around the internal diagonal of an octahedron. Opposite hemispherical triangular surfaces share the same equatorial square boundary; together they enclose four primitive tetrahedral sectors.
- In the certified patch, those sectors are **three N and one E**. The closed surface does not supply an additional, independently counted neutron.
- Complete native reader paths can converge, but the earlier search found no two-operation commuting diamonds through depth 11 over 24 root markings. A four-step geometric return has origin advanced by four and is **not** a closed native reader loop.
- The extra N obtained from one alternative path has exposed faces. It is not independently established as a filler of a closed square.

Source grammar: [`local-reference-rules.mjs`](https://github.com/andrey-kokoev/marici/blob/cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c/research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs); source-winding explanation: [`native-winding-patch-v1.md`](https://github.com/andrey-kokoev/marici/blob/cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c/research/strominger/native-winding-patch-v1.md).

The experimental off-diagonal-square face count \(2(n-1)(n-2)=0,0,4,12,24,\ldots\) was obtained by **adding** two extra fillings to chosen involution-paired squares. It matched excesses in selected isotopes but was not derived from native composition. A planar triangulated disk alone has no nonzero closed 2-cycles.

## E. Independent neutron-excess test: the mass formula

For fixed total nucleon number \(A=N+Z\), retain the two terms of the semi-empirical binding-energy formula that depend on \(Z\):

\[
B(A,Z)=\mathrm{const}
-a_C\frac{Z(Z-1)}{A^{1/3}}
-a_A\frac{(A-2Z)^2}{A}.
\]

With the illustrative coefficients \(a_C=0.714\,\mathrm{MeV}\), \(a_A=23.2\,\mathrm{MeV}\), maximizing this binding-only expression over **continuous** \(Z\) gives

\[
Z_*(A)=\frac{4a_A+a_CA^{-1/3}}{8a_A/A+2a_CA^{-1/3}},
\qquad N_*(A)=A-Z_*(A).
\]

| Nuclide | \(A\) | Actual \(Z\) | Actual \(N\) | Calculated \(N_*(A)\) |
|---|---:|---:|---:|---:|
| He-4 | 4 | 2 | 2 | 2.03 |
| Ne-20 | 20 | 10 | 10 | 10.51 |
| Ar-40 | 40 | 18 | 22 | 21.61 |
| Kr-84 | 84 | 36 | 48 | 47.34 |
| Xe-132 | 132 | 54 | 78 | 76.89 |
| Pb-208 | 208 | 82 | 126 | 126.01 |

These figures have been recomputed from the displayed formula; they correct the slightly different approximations reported earlier. This is a **binding-only continuous optimum**, not an exact beta-stability prediction: the neutron–hydrogen mass difference, integer \(Z\), pairing, shell corrections, and changes in nuclear shape are omitted. The values of \(A\) are provided; they are not predictions of the most abundant isotope.

The mass formula explains why increasing Coulomb repulsion competes with symmetry energy to favor \(N>Z\) at larger masses. It offers an independent benchmark for any proposed native energy functional.

## F. Research conjecture and falsification test

**Conjecture (not established):** Native involution-related square-link coherence induces graded spaces \(W_k\) and a canonical, symmetry-compatible map \(Q_k:W_k\to W_{k-2}\), which is equivalent to the harmonic contraction \(\Delta_k\) under a geometrically justified identification \(W_k\cong V_k\).

A decisive test requires:

1. **Construct states without assuming the answer.** Define \(W_k\) solely from finite native P/E/N composition and its actual reader/face-incidence data. Do not set its dimension to \(\binom{k+2}{2}\) by definition.
2. **Derive the operator.** Construct \(Q_k\) from genuine native square-link relations and show \(Q_k\) reduces degree by two. An arbitrary involution or imposed triangulated square is insufficient.
3. **Prove coherence.** Check identical complete boundary data, chart, five-coordinate permutation, and absolute origin. Repeated spatial coordinates are not enough.
4. **Compute ranks and symmetries.** Test \(\dim W_k\), \(\operatorname{rank}Q_k\), and \(\dim\ker Q_k\) for \(k=0,\ldots,6\); test rotational equivariance instead of imposing it.
5. **Separate multiplicities from dynamics.** Derive or independently justify an operator that selects the \(j=\ell+1/2\) energies and a binding-energy rule that predicts neutron occupation. Compare against nuclear magic numbers, isotope masses, and changing closures in neutron-rich nuclei.

**Falsifiers:** inability to produce a degree-lowering map from native rules; failure of the expected ranks; unclosed native squares after tracking origins; extra faces without distinct interiors; or a required energy ordering inserted only to force magic numbers.

## Bottom line

The triangular oscillator construction, Laplacian contraction, and conventional spin–orbit shell counting are mathematically established. The semi-empirical mass formula accounts for the broad neutron-excess trend. **There is currently no derived map from native P/E/N square links to the harmonic contraction, and no native energy operator selecting nuclear shell closures or neutron numbers.** That map is the next mathematical question, not a result of the present analysis.

## References

1. Maria Goeppert Mayer and the nuclear shell model, American Physical Society: https://www.aps.org/apsnews/2008/08/goeppert-mayer-nuclear-shell-model
2. Otsuka, *Emerging Concepts in Nuclear Structure Based on the Shell Model*, *Physics* 4 (2022): https://www.mdpi.com/2624-8174/4/1/18
3. Brown, *The Nuclear Shell Model towards the Drip Lines*, *Physics* 4 (2022): https://www.mdpi.com/2624-8174/4/2/35
4. Fradkin, *Three-Dimensional Isotropic Harmonic Oscillator and SU(3)*, *American Journal of Physics* 33 (1965): https://doi.org/10.1119/1.1971373
5. Nuclear binding-energy model and mass formula, National University of Singapore lecture material: https://phyweb.physics.nus.edu.sg/pc3232/restricted/docs/nucleus/nucleus_05_binding-energy.html
6. Marici native generator (source snapshot): https://github.com/andrey-kokoev/marici/blob/cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c/research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs
7. Marici native winding patch: https://github.com/andrey-kokoev/marici/blob/cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c/research/strominger/native-winding-patch-v1.md
