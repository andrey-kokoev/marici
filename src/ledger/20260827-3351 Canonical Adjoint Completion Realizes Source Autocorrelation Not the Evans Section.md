# Canonical Adjoint Completion Realizes Source Autocorrelation, Not the Evans Section

For the tail resolvent state

\[
G_z=(D-z)^{-1}B_f(1),
\]

the physical Evans readout is endpoint evaluation `E_0G_z`, which is linear in
the source. Completing the forcing with its canonical transpose instead gives

\[
B_f^\times(D-z)^{-1}B_f,
\]

which is quadratic in the source and equals an ordered autocorrelation or
separation transform.

The two transfers differ already for `f=1` on `[0,1]` at `z=0`: endpoint
evaluation is `1`, while the adjoint return is `1/2`. Their scaling degrees in
the source also differ.

Thus canonical adjoint completion naturally realizes the curvature object
onto which the Green, Clark, and Stieltjes lanes previously collapsed. It does
not realize the Riemann Evans section. Adjoint construction and determinant
identification are separate gates.

The next constructor must place endpoint evaluation and source-adjoint return
as two faces of a larger seam/history correspondence rather than identifying
them.

Research packet:
`research/grothendieck/canonical-adjoint-completion-realizes-source-autocorrelation-not-the-evans-section.md`

Exact checker:
`research/grothendieck/checkers/check_adjoint_transfer_differs_from_evans.py`

The checker passes 6/6 exact tests.
