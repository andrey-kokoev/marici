# Local endpoint phase covariance of tensor comparisons

## Endpoint representation

Retain the full complex4-by4 tensor x_ab. Choose endpoint phase lists chi_A
and chi_B, acting by x_ab -> exp(i(chi_B[b]-chi_A[a])) x_ab. Denote the diagonal
16-dimensional matrix by D. This is a Hom-like endpoint representation choice;
it is not selected by the original real scalar-potential prototype. The137
record coordinates w_i are chosen gauge-neutral.

Use the raw tensor Gram K=G4 tensor G4. A comparison feature v_i has normalized
vector u_i=v_i/sqrt(v_i^dagger K v_i) and readout a_i=u_i^dagger K x. Its exchange is

    x_next = x + u_i(w_i-a_i),
    w_i_next = a_i.

The invariant budget is x^dagger K x + sum_i |w_i|^2. The exchange mismatch is
w_i-a_i.

## Covariance law

Transform all representation data:

    x -> D x,
    v_i -> D v_i,
    K -> D K D^dagger,
    w_i -> w_i.

Then normalized u_i transforms by D, a_i is unchanged, and the entire exchange
commutes with the transformation. Both budget and mismatch are invariant.
The tensor isotropic covariance K^-1 transforms compatibly.

Keeping K fixed generally violates budget invariance: the off-diagonal Gram
entries couple coordinates with different endpoint phases. Thus a local phase
change here must transform the metric/overlap data as well as state and
comparison features. This is covariance between presentations of the model,
not an internal symmetry of all fixed numerical matrices.

## Connection data

For the combined state z=(x,w) let S=diag(D,I137). If i dot(z)=H z, the
transformed generator under a time-dependent frame is

    H_next = S H S^-1 + i dot(S) S^-1.

The second term is the temporal frame connection needed for consistent time
evolution. A dynamical field law for it has not been constructed here.

Conjugating the Gram by endpoint phases produces pure representation changes:
K_ab K_bc K_ca is unchanged on every coordinate triangle. Since the original
Gram entries are positive real, these phase dressings alone generate no
nontrivial loop phase. Independent curvature would require additional
connection data and a law governing it, as in the separate gauge-feedback
trial. That extra physical data is not supplied by a change of frame.

## Structural result

The full tensor and records admit a concrete local endpoint phase-covariant
adapter when the Gram and comparison directions are transported together.
This replaces the failed rank-one product-state adapter. It also preserves
the mismatch observable used in the137 normalization study.

The adapter supplies transformation laws, not the matter/link Hamiltonian or
its coupling coefficients. Local charge interpretation, independent field
curvature, physical propagation, and normalization remain open. Identifying
covariant readouts with electromagnetic observables is a further step.

## Verification

    uv run research/nima/checkers/check_137_local_phase_covariance.py

Twelve deterministic pseudorandom endpoint phase assignments test all137
exchanges (1644 cases), metric/readout covariance, record neutrality, invariant
budget and mismatch, isotropic inverse transport, and selected triangle products.
A negative control keeps the Gram fixed and finds changed budget. The general
identities follow algebraically from unitarity of D; finite tests are regression.
