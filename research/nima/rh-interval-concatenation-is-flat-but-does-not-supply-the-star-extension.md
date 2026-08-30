# RH interval concatenation is flat but does not supply the star extension

## Correction to the proposed finite test

The translated (2)-(3)-(6) interval square does not test the missing
star-extension theorem. Ordinary centered interval incidence satisfies
concatenation identically.

For

\[
B_L(z)=\int_0^L A(v)e^{izv}\,dv,
\]

one has

\[
B_{L+M}(z)
=
B_L(z)
+
e^{izL}B_M[A_L](z),
\]

where (A_L(u)=A(L+u)). Reversing the partition gives the same integral over
([0,L+M]). This is true for every integrable source and every spectral
parameter. The prime-order square is therefore universally flat.

It certifies correct interval bookkeeping, not critical-line orientation.

## Ordinary extension already exists

The centered prime samples are obtained by restricting the explicit
continuous tail

\[
R_L(z)=-\int_L^\infty A(v)e^{izv}\,dv.
\]

Thus a continuous extension without star structure exists for every (z) in
the source domain. Essential-image membership in the unstarred restriction
functor is automatic and cannot confine zeros.

The earlier categorical formulation must therefore retain the star condition
as the entire nontrivial content.

## The actual residual

Reciprocal transport and Hilbert adjunction compare

\[
B_L(-z)
\quad\text{and}\quad
B_L(-\overline z).
\]

Their difference is the star residual

\[
S_L(z)=B_L(-z)-B_L(-\overline z).
\]

For positive (A), vanishing for every (L>0) forces (z=\overline z), which
is the critical seam in the centered Fourier coordinate.

The checker gives an exact off-seam witness. Take (A=1) on
([0,\log2]) and (z=i). Then the reciprocal value is one, the adjoint value
is one half, and the residual is one half. Ordinary interval concatenation
still remains perfectly flat.

## Correct categorical DPC

Let \(\mathsf{Rec}\) and \(\mathsf{Adj}\) be the reciprocal and Hilbert-adjoint
transports on the continuous boundary-cocycle category. The missing object is
a source-derived comparison cell

\[
\eta:\mathsf{Rec}\Rightarrow\mathsf{Adj}
\]

on the zero-induced completed state.

The DPC verdicts are now:

1. Star comparison constructed: the zero-state bridge supplies \(\eta\) on
   the complete continuous cocycle; the seam theorem applies.
2. Star residual: some (S_L(z)\ne0); the state has ordinary extension but no
   star-compatible lift.
3. Discrete-only alias: star equality holds on the sampled prime lengths but
   not on the continuous family.
4. Completion failure: finite comparison cells exist but do not extend
   continuously.
5. Circular comparison: \(\eta\) is declared only after assuming the
   parameter lies on the seam.

## Why zeros do not currently supply the cell

A scalar zero makes exceptional arithmetic currents summable. It does not
identify reciprocal transport with adjunction. Off-seam hostile zeros can
share the same summability upgrade while retaining a nonzero continuous star
residual.

Therefore the essential-image route has not bypassed the mixed Green problem.
It has re-expressed the same missing orientation as a natural transformation
between two source transports.

## Next source question

Which operation, applied before scalar projection, could force the zero-state
boundary packet to carry this reciprocal-adjoint comparison? The candidate
must act on the representation-valued continuous cocycle, survive completion,
and reject hostile symmetric multipliers. Flat interval concatenation,
multiplicative incidence, and summability are already proved insufficient.

## Verification

Run:

```powershell
python research/nima/checkers/check_rh_interval_flatness_vs_star_residual.py
```
