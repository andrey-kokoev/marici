# FCC Gaussian grains: boundary responses

## Question

The operator redirects the investigation from a scale-invariant nearest-neighbor Hamiltonian to recursively manageable boundary representations, prioritizing exact tetrahedral and octahedral responses, adjoining grains, then three refinement levels. The conjecture is controlled representation complexity across indefinitely many scales, not finite-range closure.

**Coherence obligation:** route/coherencer compatibility. Compare elimination orders on the same labelled fine-scale quadratic form, with the same external variables and Lebesgue measures. This is not readout descent and does not supply a refinement map from an arbitrary coarse response.

## Claim boundary

A centered finite Gaussian region with labelled ports is represented by

\[
B=(P,S,e,d),\qquad A_B(x_P)=(2\pi)^{e/2}d^{-1/2}\exp(-x_P^TSx_P/2).
\]

Here the rational symmetric positive-definite kernel is retained in full, together with the number of integrated variables and their block determinant. Port identification is part of the type. On overlapping ports, add the two kernels using the prescribed embeddings, multiply normalization factors, then integrate the ports designated internal. This class is closed under Gaussian gluing, port elimination and relabelling. It is a sufficient class for centered source-free Gaussian amplitudes, not a claimed smallest universal quantum class. Linear sources would require additional linear and constant response terms; singular/massless operators require zero-mode conventions.

A cut must retain an interface factorization or microscopic action allocation. The exterior response alone does not canonically recover its interior cut. Likewise no intrinsic operation refining an arbitrary boundary matrix follows from Schur elimination. The microscopic hierarchical presentation is extra data. Composition success must not be reported as closure under those inverse reconstruction operations.

### Geometry and action ownership

Use FCC coordinates with even coordinate sum and squared nearest-neighbor distance two. The tetrahedron has vertices `000,110,101,011`; the adjoining octahedron is centered at `111`, with vertices obtained by adding the six signed coordinate unit vectors. Their common face is `110,101,011`. At level `l`, multiply parent coordinates by `2^l` while keeping the microscopic FCC spacing fixed. Enumerate all elementary tetrahedra and octahedra contained in each parent; check their counts against `T -> 4T+O`, `O -> 8T+6O`.

Each elementary cell contributes

\[
K_c=I_{V(c)}/14+L_{E(c)}/4.
\]

An infinite FCC vertex belongs to eight tetrahedra and six octahedra, and an edge to two of each. Summing cells therefore gives the unit-mass, unit-spring FCC action in the bulk. On a finite complex this defines a free-boundary, cell-additive action. It is not the induced-subgraph action with a full mass placed separately on every patch vertex. Shared contributions are added, not duplicated and later subtracted by an unspecified convention.

There is no microscopic coupling matching or field rescaling across levels in this experiment. Raw response equality tests unchanged cell couplings only.

### Two port conventions

1. **Full boundary:** all vertices on exterior triangular faces. Newly created edge and face vertices remain explicit. This is the interface used for joining refined neighbors.
2. **Inherited ports:** only the original four or six corner vertices. Integrate the other boundary vertices as well. This supports response comparison on a fixed port set, but is not a complete geometric face interface for arbitrary later gluing.

The artifacts retain both conventions. Integrating a shared fine face vertex separately inside each grain would replace one variable by independent copies and is not an admissible gluing.

## Falsification protocol

- **Bold conjecture:** full boundary responses admit a reusable exact representation whose cost has a controlled law across refinement levels.
- **Rivals:** dense Schur kernels grow without useful compression; symmetry compresses values but rational bit lengths dominate; fixed-corner compression only appears efficient because it discards interface ports.
- **Risky consequences:** exact staged and direct pair kernels and determinant factors agree; symmetry acts on every retained port; complexity measurements include coefficient bit lengths, not only matrix dimensions.
- **Hostile:** add a spurious shared-interface mass and require the resulting amplitude to differ. Compare full matrices and normalization factors, not a scalar statistic.
- **Bound:** levels zero through three for individual grains; adjoining-pair tests at scales one, two and four. These samples cannot establish an indefinite-scale compression theorem.

## Response-only refinement hostile

`check_gaussian_response_refinement_descent.py` supplies a separate, generic positive weighted-graph counterexample—not an FCC factor-two counterexample. Two three-vertex actions have exactly the same two-port kernel `[[2,-1],[-1,2]]` and the same normalization `sqrt(2*pi)/2`. Replace every spring by two springs of unchanged strength, keep old vertex masses, and assign zero mass to the new midpoint vertices. Eliminating all internal vertices gives respectively

\[
S'_1=\begin{pmatrix}31/24&-11/24\\-11/24&31/24\end{pmatrix},\qquad
S'_2=\begin{pmatrix}27/20&-9/20\\-9/20&7/5\end{pmatrix}.
\]

The corresponding normalizations are `(2*pi)^2/sqrt(18)` and `(2*pi)^2/sqrt(20)`. Therefore this specified microscopic subdivision does not descend to a function of the original boundary amplitude alone. A refined microscopic presentation, or a proven restriction making refinement insensitive to that presentation, is necessary. The example does not refute a response-preserving tuned subdivision or the operator's existence conjecture for a suitably specified honeycomb theory.

## Complexity baseline

Let `L=2^level`, with `V=O(L^3)` microscopic vertices and `B=O(L^2)` geometric boundary ports. This particular action has integer matrix `A=28K` and row absolute sums at most 700. The determinant of an interior block of size `I` is at most `700^I`; the bordered minors defining Schur entries have absolute value at most `700^(I+1)`. Their numerator and denominator bit lengths are therefore `O(V)`. This gives a coarse exact dense boundary-storage bound `O(B^2 V)=O(L^7)` bits, even without compression. Keeping the original bounded-degree network instead uses `O(V log V)` bits with explicit labels, but defers elimination cost to each boundary-response query.

Thus “some controlled growth law” alone is too weak to distinguish a discovery from existing elimination bounds. A stronger target needs a declared storage/query-cost baseline—for example near-linear boundary storage with exact composition costs—and must count coefficient bit lengths. A fixed finite symmetry group can reduce matrix entries by orbit factors, but does not by itself make storage per port bounded.

## Measured results

All eight grain cases and three adjoining-pair routes pass exact checks. Levels `0,1,2,3` correspond to scales `1,2,4,8`. Each grain kernel passes all 24 full tetrahedral or 48 full octahedral symmetry maps, including improper transformations. This is stronger symmetry than A4 and supplies no A4-specific observable.

| Grain | Level | Boundary ports | Nonzero upper entries | Distinct rational values | Maximum entry bits | Encoding bit proxy |
|---|---:|---:|---:|---:|---:|---:|
| T | 0 | 4 | 10 | 2 | 10 | 26 |
| T | 1 | 10 | 34 | 5 | 10 | 193 |
| T | 2 | 34 | 184 | 9 | 13 | 2,446 |
| T | 3 | 130 | 3,820 | 95 | 111 | 67,603 |
| O | 0 | 6 | 18 | 3 | 8 | 57 |
| O | 1 | 18 | 108 | 6 | 18 | 563 |
| O | 2 | 66 | 1,860 | 41 | 68 | 15,149 |
| O | 3 | 258 | 31,908 | 661 | 678 | 706,367 |

Entry bits count numerator and denominator bit lengths. The encoding proxy counts a dictionary of rational values, fixed-width upper-triangle value indices, and determinant bits. It excludes geometry, metadata and implementation; it is neither actual JSON byte length nor optimal compression. `analysis.json` also records actual JSON bytes and the proxy per port. Both increase per port over the tested levels; this does not establish an asymptotic lower bound.

The pair tests retain common interfaces with 3, 6 and 15 vertices at scales 1, 2 and 4. Respectively 0, 0 and 3 shared vertices become strictly internal to the assembled region. Independently reducing the pieces and then integrating the internal interface gives exactly the same full kernel and normalization as reducing the assembled microscopic action. Spurious interface mass is rejected in all cases. At scale four the normalization is `(2*pi)^(23/2)/sqrt(23791481689798270095923925)`.

### Fixed inherited-corner family

At unchanged couplings, neither refined grain reproduces its original corner response. Allowing two effective couplings, the tetrahedral four-corner matrix stays in the mass-plus-complete-graph family at every tested level; this is forced by full tetrahedral permutation symmetry and does not preserve the full face interface. The octahedral six-corner matrix leaves its original mass-plus-edge-Laplacian family already at level one: the opposite-vertex entry is `-24794/410241`, whereas every member of the original two-parameter family has zero there. Thus even corner-only two-parameter closure cannot hold simultaneously for both grain types under this action. No field/coupling-rescaling fixed-point search was performed.

## Disposition

Execution and quantitative results are recorded in `results/fcc-gaussian-boundary-direct/verification.json`. Full rational kernels use a lossless rational-value dictionary and an index matrix. This encoding is not an optimality claim: the matrix indices themselves are part of the representation cost. Determinants are exact rationals, with powers of `2*pi` symbolic.

Reproduce with `python research/strominger/checkers/check_fcc_gaussian_boundary.py`. Analyze the saved matrices with `python research/strominger/checkers/analyze_fcc_gaussian_boundary.py`; the generic refinement-descent hostile runs with `python research/strominger/checkers/check_gaussian_response_refinement_descent.py`. The checker is dependency-free and uses symmetric fraction-free Bareiss elimination. Source identity is hashed in the receipt. Inherited-port kernels are reduced directly from the original integer-scaled action, avoiding common-denominator growth from eliminating an already rational boundary matrix. The earlier exploratory `results/fcc-gaussian-boundary/` directory is not the authoritative result set. No maintained Chamon or reader-interface verdict is changed by this Gaussian experiment.

Reshetikhin–Vertman and BFK are literature leads supplied by the operator; their original texts have not been independently checked in this execution. Gaussian composition here follows finite-dimensional block elimination directly, not a claimed new gluing theorem or an attribution-dependent result.
