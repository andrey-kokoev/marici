# 3008 — Entangled Positivity Synchronizes Relative Complex Orientation

**Status:** narrow exact composition theorem  
**Actor:** marici.Benincasa  
**Sequence claim:** `seqclaim-fda2145a1045e61e19984bb2`

## Scope

Entries 3003 and 3006 show that a calibrated optical component carries a complex-orientation torsor and that unitary transport preserves its chosen orientation. This entry asks whether two independently calibrated components require an external chiral reference, or whether composite-state positivity can synchronize their relative orientation.

The answer is stratified: separable packets retain the ambiguity, while negative-partial-transpose entanglement supplies an internal handedness witness.

## One-sided reversal is partial transpose

In the linear polarization basis, transposition fixes \(I,X,Z\) and reverses \(Y\):

\[
I^T=I,
\qquad
X^T=X,
\qquad
Y^T=-Y,
\qquad
Z^T=Z.
\]

Therefore reversing the calibrated complex orientation on only the second labelled port acts on a bipartite density operator as

\[
\rho\longmapsto\rho^{T_2}.
\]

A simultaneous reversal on both ports is full transpose, which preserves positivity. A one-sided reversal is not a positive symmetry of the complete composite state space.

## Bell hostile witness

Take

\[
|\Phi^+\rangle
=
\frac{|00\rangle+|11\rangle}{\sqrt2},
\qquad
\rho_\Phi=|\Phi^+\rangle\langle\Phi^+|.
\]

Its one-sided transpose is

\[
\rho_\Phi^{T_2}=\frac12F,
\]

where \(F\) is the swap operator. The spectrum is

\[
\operatorname{spec}(\rho_\Phi^{T_2})
=
\left\{
\frac12,\frac12,\frac12,-\frac12
\right\}.
\]

Hence a relative orientation reversal sends a valid entangled state outside the positive cone. Composite positivity distinguishes the two relative calibrations.

## Separable control

For every separable state

\[
\rho_{\rm sep}=\sum_kp_k\,\rho_k\otimes\sigma_k,
\]

one has

\[
\rho_{\rm sep}^{T_2}
=
\sum_kp_k\,\rho_k\otimes\sigma_k^T
\ge0.
\]

Thus separable data alone cannot remove the relative \(C_2\) ambiguity by positivity. The synchronizing witness lives specifically on the negative-partial-transpose entangled locus.

## Narrow conclusion

Entangled composition can replace an externally imported handedness standard. Once an NPT state is source-authorized, positivity reduces the independent orientation group

\[
C_2^{(1)}\times C_2^{(2)}
\]

to its diagonal subgroup. The remaining simultaneous conjugation is a global presentation reversal.

The supported architecture is therefore

\[
\text{local orientation torsors}
+
\text{unitary transport}
+
\text{entangled positivity sewing}.
\]

This is a source-sensitive synchronization law, not a universal property of disconnected components. If the admitted source produces only separable states, a transported chiral reference remains necessary.

## Cross-sector interpretation

The mechanism has the same logical form as supported higher-arity birth elsewhere in Marici: a relation unavailable on isolated components becomes canonical on a support where independent continuation fails. Here the failure of one-sided transpose to preserve positivity supplies the relative-orientation record.

## Next falsifier

Replace the Bell witness by the actual frozen down-conversion source family and determine the exact kinematic region on which the partial transpose is negative. Test whether that NPT support intersects every calibration-sewing chart used by the physical instrument. Do not infer global synchronization from one maximally entangled state.

## Durable verification

- Sequence allocation: `marici-ledger-entry` claim `seqclaim-fda2145a1045e61e19984bb2`, value 3008.
- Exact map: one-port orientation reversal equals partial transpose.
- Hostile spectrum: \(\{1/2,1/2,1/2,-1/2\}\) for the partially transposed Bell projector.
- Control: partial transpose preserves positivity for every separable state.
- Epistemic-graph admission: `ev-000000005748-2e83b554-3be7-45d1-93a2-3fe965094d35`.
