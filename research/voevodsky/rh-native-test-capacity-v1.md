# Iteration6: the finite native form cannot carry the complete test domain

## Answer refined by a capacity witness

The bare triangles still compute a cyclic permutation of coefficient
amplitudes, not a prime/gamma/zero algorithm. Their raw common edge identifies
the opposite occurrences AB and BA with BA=-AB.

The **added RH evaluators** act on one common analytic test:

- Arithmetic: endpoint moments + gamma integral - weighted prime translations.
- Spectral: half the full signed zero divisor, with multiplicities and complex
  nodes (rho-1/2)/i.

The decorated seam identifies test descriptors, coefficient polarization and
normalization. The known explicit formula gives equality; RH-bearing positivity
requires the complete test domain, not merely equal outputs.

The previous three-test comparison survives in both native structures. A
stronger answer about the complete domain is now available: **neither inherited
signed form admits a fixed complex-linear encoding even of the15-test positive
span constructed here**. Thus neither can carry the full source criterion by
that encoding mechanism. This statement is about the retained form and linear
amplitude semantics, not every imaginable RH model or readout.

## 1. Fresh positive15-test witness

Fix t=1/10 and frequency centres

    14,21,25,30,33,37,41,43,48,50,53,56,59,61,65.

These are rational test descriptors, not root values supplied to the producer.
All15 logarithmic Gaussian features belong to the same admissible analytic
source class used in iterations4–5. The source theorem and its evenization/
half-divisor convention apply to their products without a new normalization.

The independent spectral evaluator:

1. certifies N(150)=52, constant near the cutoff;
2. proposes roots and gives52 disjoint critical-line brackets with opposite
   certified completed-xi signs;
3. combines root existence with the total multiplicity count to prove complete
   window coverage and simplicity;
4. computes all120 polarized coefficients at their actual complex nodes;
5. adds the unconditional Jensen/Gaussian tail bound, allowing off-critical
   zeros beyond150;
6. performs interval LDL on the resulting15-by15 full-divisor enclosure.

The infinite-tail bound is the iteration5 derived estimate using
N(v)<=(v+3)^2 for v>=13, not an extrapolation of a positive-zero scout.
Every tail is below1e-300. All15 interval pivots are strictly positive.
Consequently the exact full-divisor form is positive definite on this span,
without assuming RH outside the verified window.

The120-entry arithmetic matrix is **not independently generated numerically
in this iteration**. Its analytic equality with the spectral matrix follows
from the inspected classical explicit formula for these admissible Gaussian
products. The index obstruction already follows from the spectral form alone.

## 2. Exact native inertia, including the neutron metric

Let L,G,N be the commuting metric-orthogonal native projectors. Put

    A=L-N, B=G-N, AB=0.

Their ranks are(11,2,1) for(A,B,N) in the protonlike carrier and(2,11,1) in the
neutron carrier. The untouched native complement has dimension22.
Let W be the inherited108-dimensional three-stage transfer operator, M_s its
positive three-stage metric, and

    H=(M_s W+W* M_s)/2, K=M_s^-1 H.

Do not treat neutron numerator coordinates as Euclidean amplitudes.

The checker constructs exact metric-self-adjoint eigenprojectors of K:

- On A, stages raw/local give one +1/2 and one -1/2 direction per A mode;
  the aligned copy is null.
- On B, stages local/aligned give the same pair per B mode; raw is null.
- On N, the three-cycle gives eigenvalues1,-1/2,-1/2.
- The remaining native complement is null in every stage.

Explicit projector formulas are verified against fresh native coefficients:
idempotency, metric self-adjointness, eigenprojector equations and completeness.
Their exact traces are their ranks. The resulting multiplicities are

| Eigenvalue of K | Multiplicity, both carriers |
|---|---:|
| 1 | 1 |
| +1/2 | 13 |
| -1/2 | 15 |
| 0 | 79 |

Since M_s is positive, H has inertia **(14 positive,15 negative,79 null)** in
both carriers. This is an exact weighted calculation, not a numerical
near-zero eigenvalue classification.

## 3. The obstruction does not depend on arithmetic coefficient algebraicity

Suppose one complex-linear amplitude encoder

    E:C^15 -> C^108

preserves the full-divisor form:

    E* H E=S15.

S15 is strictly positive definite, so E is injective and its image is a
15-dimensional subspace on which H is positive. But H has maximum positive
subspace dimension14. This contradicts Sylvester's positive-index bound.

The argument allows arbitrary complex entries in E, including transcendental
ones. Supplying analytic amplitudes therefore does not remove this particular
capacity obstruction. It is distinct from iteration4's algebraic-generator
obstruction.

A linear encoding of the entire source test domain would restrict to an E on
this span, so it is excluded as well. Even separately preserving the spectral
form is impossible; jointly preserving arithmetic and spectral forms cannot
be easier. Preserving only their identically zero difference would discard
the RH-bearing sign information and is not a substitute.

## 4. What this does and does not invalidate

It does **not** invalidate:

- the certified three-test arithmetic/full-divisor comparison;
- its exact signed midpoint attachments in both native carriers;
- the native source/sink affine-lift composition checks;
- the abstract classical explicit-formula identity.

It does prevent silently upgrading a small packet attachment into a fixed
linear encoding of all tests using the same H. A query-dependent state can
encode an already calculated value, but that is not a coherent full-domain
encoder or an arithmetic algorithm derived from the seed.

The result does not rule out another readout, nonlinear encodings, larger
carriers, tensor extensions, test/dual completions or an imported classical
processor. Those must be explicitly identified as additional structure.
The different stage ranks still obstruct finite invertible stage-preserving
processing equivalence; equal inertia does not eliminate that difference.

## 5. Verification and continuation

    python research/voevodsky/checkers/check_rh_native_test_capacity.py

Artifacts:

- `inputs/rh-native-test-capacity-v1.json`.
- `results/rh-native-test-capacity-v1.json`.
- `scc-models/rh-native-test-capacity-v1.json`.

Shared native stores remain read-only. The positive15-test witness proves a
representation obstruction, not positivity on every test or RH.

Next: specify an operation-bearing **infinite analytic test/dual completion**,
with a fixed Hermitian pairing and actual endpoint/gamma/prime/divisor
operators. Determine what can be attached consistently beside either native
carrier, and keep that enlargement separate from finite native face execution.
