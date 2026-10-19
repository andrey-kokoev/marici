# Iteration 3: full Fourier transport through six reductions

## Question and fixed obligation

Does Strominger's existing six-step generator descent also carry the full
order-four source permutation, and hence iteration 1's analytic Fourier orbit?
The SCC obligation is route compatibility of all intermediate reductions, not
merely agreement of the final source and target.

Reconstruct the source C12, D12=C12-C12^T, metric, form and energy from the
existing source constructor. Keep the same direct projection P, visible
embedding E and schedule 12->11->10->9->8->6->4. No analytic factors or
bottom generator are used to construct the source.

## Why generator reduction is not enough

The original reducing frame separates two hidden rotor pairs from four hidden
stationary directions. On a stationary direction D12=0, but C12 may act by
+1 or -1. An arbitrary mixture of these characters is stationary for D12
without spanning a C12-invariant line.

For each original frame prefix E_m, the checker computes the actual
metric-adjoint P_m and N_m=I-E_m P_m. The decisive full-tick residual is
P_m C12 N_m. The output records its exact rank and a hidden-input witness
where nonzero. Each prefix is compared directly with the source; after a
failure, we do not pretend its compressed matrix is a valid intermediate tick.

The original frame passes the generator test at every audited prefix, but
full-tick leakage ranks at dimensions 11,10,9,8,6,4 are respectively
1,2,1,0,0,0. Thus its first 12->11 removal already fails Fourier transport.
This does not invalidate the original generator-only theorem.

## Parity-resolved frame

The source itself supplies the projectors

  Q_+=(I+C12+C12^2+C12^3)/4,
  Q_-=(I-C12+C12^2-C12^3)/4.

Let N=I-EP. The ranges of Q_+N and Q_-N each have dimension two. Retain the
original first eight frame columns (four visible coordinates and the two
hidden rotor pairs), then append rational bases of these two stationary
character spaces. This gives an invertible frame B_fix without changing E.

Every one-dimensional stationary removal now lies in a single full-tick
character. The last two steps still remove whole rotor pairs. For each step
(n,m), the checker constructs the prior Hamiltonian WG witness and verifies
additionally

  P_(n,m) C_n=C_m P_(n,m),
  C_n E_(n,m)=E_(n,m) C_m,
  N_(n,m) C_n=C_n N_(n,m), C_m^4=I.

It checks metric preservation by the tick and preservation of the inherited
form and energy, as well as generator descent and hidden reconstruction. The
complete list of original prefix outcomes and the new rational frame are in
the result JSON, not inferred from a sampled orbit.

## Connection to the analytic construction

The composite of the six projections in the new frame is EXACTLY the original
P. Thus the analytic attachment R_a=B_a J P from iteration 1 is unchanged.
It satisfies R_a C12=F R_a whether reached directly or through all six steps.
Composing with the existing oriented radial and Mellin representation gives
the same gamma-matrix/reflection operator and Hurwitz/polylogarithm ports.
The analytic identities are imported from the prior derivations; the new
checks establish the finite transport into their domain.

All six steps in the parity-resolved frame pass the exact checks. This frame
resolves the previously named intermediate Fourier-transport gate.
It does not change iteration 2's fact that the native history tick has order
three while the Fourier tick has order four. Their active continuous generators
are connected by the existing adapter, not by identifying discrete ticks.

## Retention and scope

Each discarded coordinate is retained in its hidden record. Reconstruction
uses x=E_step(P_step x)+N_step x at each step. Hidden energy is not assigned
zero merely because it becomes invisible. The new frame is a declared
reversible coordinate transformation, not an admitted physical preparation,
actuator, clock or erasure protocol.

The four analytic ports still use a chosen shifted-comb seed, and their
coefficient Gram is transported rather than identified with an independently
measured analytic Hilbert Gram. No RH or native zeta-computation claim follows.

## Verification

Run `uv run research/voevodsky/checkers/check_fourier_six_step_descent.py`.
It validates iteration 1 source hashes, audits the original frame, constructs
the stationary parity split, runs all six original Hamiltonian WG gates with
additional permutation checks, and compares the final projection, generator,
energy and analytic attachment exactly.

Artifacts: `results/fourier-six-step-descent-v1.json` and the owner-local SCC
manifest. Source-owner files are read only.
