# The cited finite Gram diagnostics do not establish the claimed continuum limit

## Frozen explanatory question

Does the literal construction in `continuum-embedding-construction.md`, supported
by its actual cited implementations, reproduce a constant metric and establish
the claimed continuum convergence?

The active SCC obligation is SOURCE-TO-CONTINUUM FORWARD REALIZATION. Hold fixed
the whole cubic grid, epsilon=1/L, the stated radial weights, and the supplied
Euclidean coordinate embedding. Keep both existing implementations:
`checkers/check_machian_metric_larger.py` AND the stronger explicitly named
`checkers/check_continuum_limit.py`. Do not replace them by a smaller carrier,
normalized hats, tensor-product interpolation or an assumed physical metric.

The radial-hat counterexample was already written in
`relative-anchor-coordinate-prior-clues.md`. This turn's remaining uncertainty
is whether the actual implementation supersedes that defective paper formula,
and which current completion claims its evidence warrants.

**Conjecture:** this is a source/comparison defect, not merely insufficient
carrier size. The finite diagnostics do not implement the proposed interpolant,
and that interpolant fails even for the paper's expressly allowed flat metric.

**Rivals:** a stronger cited implementation supplies the missing interpolation;
the error disappears away from boundaries or under refinement; or the finite
Gram calculations themselves are invalid.

**Risky consequences:** rerun the actual finite implementations without writing
their old receipt paths; preserve their matrices and carrier data. Compare their
index types with the claimed metric. Evaluate the stated interpolant at the
SAME point x=(1/2,1/2,1/2) along odd and even L, not at a moving boundary.
Retain a derivation for all L; positive finite samples are not a limit theorem.

**Closure condition:** an exact admissible failure of constant reproduction or
pointwise convergence closes this construction negatively. An actually
implemented, proved stronger map would instead supersede the defective formula
at its own assumptions. Mere interior-count convergence or a positive Gram
spectrum is not acceptance. Do not reopen either existing finite construction
when asking for a distinct continuum theorem.

## Actual implementation comparison

The original and current computations agree exactly. Their types differ:

| Implementation | Actual object | Nonzero eigenvalues |
|---|---|---|
| `check_machian_metric_larger.py`, S3 | 6-by-6 Gram indexed by stabilizer permutations, using numeric labels and a supplied dot product | 6, 6, 72 |
| Same implementation, D4 | 8-by-8 Gram indexed by permutations of the supplied planar grid | 240, 240, 1024 |
| `check_continuum_limit.py` | 6-by-6 Gram of the ALREADY GIVEN Euclidean vectors plus/minus e1,e2,e3 | 2, 2, 2 |

The last Gram is V*V^T with V^T*V=2*I3. Neither implementation produces a
three-dimensional tangent frame, the stated radial interpolant, or a map from the
permutation-indexed Gram to a spatial metric. Equal positive rank does not
supply such a map. In particular, even the two 6-by-6 matrices are unequal.
The original diagnostics have no required-property assertions; their printed
conclusions were not checked continuum theorems.

The exact grid count also survives:

\[
\frac{|X_L^\circ|}{L^3}
=\frac{(L-2)^3}{L^3}\longrightarrow 1.
\]

The old `sym_rank` field is merely the neighbor count, not a computed
stabilizer. An increasing fraction of six-neighbor points is compatible with
the failure below; it does not control an interpolated tensor field.

## All-refinement obstruction at a fixed interior point

Keep the paper's input g(p)=I3 and its exact formula

\[
g_L(x)=\sum_p\max(0,1-\lVert x-p/L\rVert/(1/L))\,I_3.
\]

At x=(1/2,1/2,1/2), for every odd L>=3 the eight nearest grid displacements
in grid units are (plus/minus 1/2, plus/minus 1/2, plus/minus 1/2).
Their squared norms are 3/4. Every other squared norm is at least 11/4,
outside the support. Hence

\[
g_L(x)=(8-4\sqrt3)I_3 \qquad (L\ge3,\ L\in2\mathbb Z+1).
\]

For every even L>=4 the point is a grid vertex. Its own weight is one and
all others vanish, so g_L(x)=I3. The SAME fixed point lies strictly inside the
carrier hull on both subsequences. The discrepancy

\[
\lVert g_L(x)-I_3\rVert_{\rm op}=7-4\sqrt3>0
\]

persists on the odd subsequence. There is no pointwise limit along all L,
let alone the claimed uniform O(L^-2) estimate. This is an all-L support
argument, not extrapolation from the executed L=3,...,8 controls.

Nor does selecting only dyadic grids rescue UNIFORM convergence. For every
L>=3 choose the cell centre whose three coordinates are
(floor(L/2)+1/2)/L. It lies in the fixed compact cube [1/3,2/3]^3 and has
exactly the same eight weights. The supremum error on that cube is therefore
at least 7-4*sqrt(3) for every such L, along any refinement subsequence.

The unscaled hat also does not tend to a Dirac distribution. Its total mass is

\[
4\pi\int_0^\varepsilon r^2(1-r/\varepsilon)\,dr
=\pi\varepsilon^3/3\longrightarrow0.
\]

Pairing with a bounded compactly supported test function is bounded by this
mass times its supremum norm. Thus the distributional limit is zero. This does
NOT refute properly normalized discrete-measure limits; those are different
objects and neither cited implementation tests them.

## Disposition and visible supersession

**Closed negatively:** the advertised source-to-continuum construction fails,
and the stronger cited checker does not rescue it. The rivals “only a coarse
mesh/boundary problem” and “an implemented stronger interpolant” are eliminated.
The finite matrix and grid calculations survive at their stated supplied inputs;
wholesale invalidity of those computations is rejected.

The original construction, both original scripts and four downstream entry
points are byte-preserved in `quarantine/20261007-continuum-evidence/manifest.json`.
No old receipt existed at either named output path. The live diagnostic scripts
retain their computations but now emit `finite_diagnostic_only`, not continuum
or intrinsic-metric conclusions. Leading corrections at the original construction,
Gram README, session summary, foundational compendium and ADM packet withdraw
the dependent completion/“only admission remains” claims. Other physical claims
in those historical compilations are not certified by this correction.

`barycentric-refinement-coherence.md` is a stronger, distinct finite preservation
theorem, with two validated geometric refinements and an explicit separate
infinite-refinement boundary. It is not contradicted, rerun or weakened here.
The rotor phase/HJ/clock, full Bool Tick and six-port closures are untouched.

No replacement interpolation was fitted. A separately justified reconstruction
operator and its convergence estimate would be a NEW candidate, not a reason to
reopen this negative closure or repeat the same Gram spectra on larger grids.
This turn stops before an ADM comparison; a supplied Hamiltonian does not become
a first-class Hamiltonian constraint merely by renaming it.

## Execution and verification

The combined NumPy/SymPy command was refused by the execution policy. The
inspected policy admits separate SciPy and SymPy profiles. Consequently:

1. `collect_continuum_diagnostics.py` executes the original and live numerical
   scripts, suppressing only their inspected receipt-write statements. It keeps
   their matrices and complete grid records and hashes all four sources.
2. `check_continuum_embedding_evidence_boundary.py` checks those hashes, compares
   the complete data, and performs the exact spectrum/interpolation calculation.

The first exact run failed because the old np.zeros buffers serialize exact
integer entries as floats. Diagnostic `e_38524_1791395219433987400_46` confirms
the predicted exact spectra after value-preserving rational conversion.
The corrected boundary refuses EVERY nonintegral entry; it uses no tolerance or
rounding. The old freezes and failed challenge remain preserved. That execution
failure was not scientific survival of the continuum claim.

Successful frozen challenge: `e_38524_1791395266041763600_48`, freeze
`nima-continuum-embedding-evidence-boundary.c8c078bfff473cc0.json`.
Collection: `e_38524_1791395123506044600_43`. Exact result:
`results/continuum-embedding-evidence-boundary.json`; transported source data:
`results/continuum-diagnostic-transport.json`. The final fresh producer run
`e_38524_1791395594859890900_49` and exact scoped headless check
`e_38524_1791395615563269100_50` pass. Integrity check
`e_38524_1791395701019276600_51` confirms all eight receipt inputs and seven
original snapshots, with historical receipt paths still absent.

Graph closure and supersession:
`ev-000000015820-47a45924-3947-422a-a713-614c219a96b1`, proposal
`ep_d5bdfdcb-4cab-4f2d-b5b1-c81073424329`. Admission records provenance, not truth.
The accumulated audit/correction interval [15815,15820] remains uncommitted.
No commit, push or publication occurred.

No native formal proof, source-selected manifold, GR derivation or general
continuum impossibility theorem is claimed.
