# The first two-by-two-by-four arithmetic window has coherent faces and a noninvertible stage seam

## Question and operator direction

The operator proposed a local window with axes (k,k+1), covariance direction, and four presentations. Can its edges, faces, and cubes be constructed from the existing arithmetic source?

The tested conjecture is that source-preserving presentations and duality extend the two-prime diamond into the three-prime cube coherently, while keeping the cycle port. The rival interprets this stage extension as an invertible four-phase return. A separate rival drops cycles because all theta histories of addition paths coincide.

Active SCC obligation: finite source realization, attachment transport, and mixed stage/presentation/duality coherence. This is a concrete window instance, not identification of every proposed axis with its ultimate meaning. In this instance k indexes prime-cutoff extension; its identification with the operator's full-cycle counter remains a source comparison. The four presentations below are not claimed to be the four canonical Fourier charts.

## Source and four presentations

Let E_0 be the four-dimensional edge source for primes {2,3}, and E_1 the twelve-dimensional edge source for {2,3,5}, both with initial multiplicative label 2. Inclusion I sends each old prime-labelled edge to the identical edge in the enlarged graph. It is not selected from determinant data.

At each stage use these four realized presentations:

1. labelled edge coefficients;
2. reduced endpoint boundary plus chord-cycle coefficients;
3. common-refinement interval coefficients plus chord-cycle coefficients;
4. actual theta history plus chord-cycle coefficients.

The endpoint boundary drops the final vertex row, whose value is forced by total boundary sum zero. Each stage uses a specified greedy spanning tree and retains all its chords. The interval/cycle dimensions are (3,1) at stage zero and (7,5) at stage one.

The fourth presentation is the finite image of the recorded theta interval functions. Their independence follows from the recorded theta injectivity theorem, as in the preceding diamond and cube packets. A coefficient matrix can coincide with that of presentation three without making the analytical maps identical: presentation four realizes those coefficients as functions. The checker uses coordinates in this proven independent basis, not numerical theta samples.

Write A_ki for the invertible coefficient realization from E_k to presentation i. Set

\[
Q_{k,i}=A_{k,i+1}A_{k,i}^{-1},\qquad
V_i=A_{1,i}IA_{0,i}^{-1}.
\]

These construct the six internal covariant chart edges and four stage edges from source maps. Their duals reverse arrows on the contravariant sheet. This is genuinely co/contravariance, not two copies of the same directed lattice.

## Pairing edges and their metric boundary

Declare the source counting metric on labelled edges. Pull it through each realization:

\[
G_{k,i}=A_{k,i}^{-*}A_{k,i}^{-1}.
\]

This supplies the Riesz comparison to the dual sheet. It is a mathematical source-pulled metric, not a claim that the native theta L2 metric or physical Green metric equals it. The real rational fixture uses transpose; the complex formulation uses conjugate transpose and anti-linear Riesz maps.

The cross-sheet faces are pullback-pairing identities, not assertions that a rectangular map is invertible:

\[
Q_{k,i}^*G_{k,i+1}Q_{k,i}=G_{k,i},\qquad
V_i^*G_{1,i}V_i=G_{0,i}.
\]

The second identity uses I*I=I on the smaller labelled source, which holds for the declared coordinate inclusion.

## Sixteen faces and three cubes

There are sixteen vertices in the two-by-two-by-four node window. Its sixteen elementary faces are:

- three stage/chart squares on the covariant sheet;
- three dual stage/chart squares;
- six chart/pairing faces, three at each stage;
- four stage/pairing faces.

The covariant stage/chart relation is

\[
V_{i+1}Q_{0,i}=Q_{1,i}V_i.
\]

Each of the three adjacent chart intervals gives one elementary cube. Its two pullback routes obey

\[
V_i^*Q_{1,i}^*G_{1,i+1}Q_{1,i}V_i
=
Q_{0,i}^*V_{i+1}^*G_{1,i+1}V_{i+1}Q_{0,i}
=G_{0,i}.
\]

Thus all face and cube identities follow from source naturality and pairing transport. They are a strict finite model; no independently fitted higher coherencer is used.

## Fourth-to-first seam and its falsifier

Construct the seam from the actual stage inclusion:

\[
R_{0,3\to1,0}=I A_{0,3}^{-1}.
\]

Its composition with the three internal presentation arrows equals I. The full four-arrow route therefore realizes the declared source extension, not identity closure.

Its shape is twelve by four and its rank is four. The dual route restricts covectors in the opposite direction. One has

\[
I^*I=I_{E_0},\qquad II^*\ne I_{E_1}.
\]

Any newly added edge supplies a nonzero witness killed by I*. Hence neither duality nor commuting cubes turns this seam into an equivalence. If the intended cycle counter requires an invertible successor, this prime-cutoff window does not realize that requirement. A stable/localized enlargement would need independent source justification.

## Determinant consequence

There is no ordinary scalar determinant of the twelve-by-four seam. The source supplies instead the exact sequence

\[
0\to E_0\xrightarrow{I}E_1\to E_1/I(E_0)\to0,
\qquad \dim(E_1/I(E_0))=8.
\]

Its determinant functor gives

\[
\det E_1\simeq\det E_0\otimes\det(E_1/I(E_0)).
\]

The labelled new-edge complement supplies a concrete ordered frame for the quotient. The checker tests the adapted basis matrix has determinant plus or minus one. This is source exact-sequence sewing, not a fitted scalar continuation and not yet an Euler determinant increment. The quotient dimension eight is a graph dimension difference, not evidence identifying it with an amplituhedron chart.

## Noncollapse and disposition

A nonzero diamond cycle is invisible to every interval history. The cycle-augmented fourth presentation detects it, and source inclusion preserves it at the next stage. This rejects the history-only rival on the same source used by the window.

Constructed: one finite two-stage/co-contra/four-presentation window, all its internal edges, sixteen mixed faces, three cubes, a source-induced seam, and its relative determinant exact sequence. The cycle counter, Fourier-chart comparison, native metric comparison, Euler grades, and completed infinite-stage interpretation are not supplied by these finite identities. No physical-time meaning is assigned to stage transport.

Verification: `uv run --with sympy python research/nima/checkers/check_two_by_two_by_four_arithmetic_window.py`, exit 0. Fifteen grouped checks pass, covering all sixteen faces and all three cubes. Result: `research/nima/results/two-by-two-by-four-arithmetic-window.json`. The theta basis uses the recorded analytical theorem; theta integrals were not numerically evaluated.
