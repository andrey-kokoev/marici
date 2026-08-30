# RH zero-to-dagger promotion is the Schur–Evans comparison cell

## Candidate audit

The existing source packets close three apparent shortcuts.

- The doubled tail domain is universal and admits positive off-seam hostile
  zeros.
- The exact staircase Green identity does not turn scalar nullity into
  reciprocal adjointness.
- Elementary antiunitary real structures either select the wrong phases or
  preserve an entire phase family.

The boundary-control Evans system does achieve one essential result: its
endpoint determinant vanishes exactly when the source-derived one-way system
has a nonzero two-ended state. But that one-way system has a nonzero adjoint
residual.

## Why naive dagger completion fails

At finite cutoff write the reciprocal block system as

\[
\mathcal L_{z,X}
=
\begin{pmatrix}
A_{z,X}&B_{+,X}\\
B_{+,X}^*&C_{z,X}
\end{pmatrix}.
\]

The adjoint return channel repairs the off-diagonal dagger defect. Its kernel,
however, is governed by the Schur complement

\[
S_X(z)
=
C_{z,X}-B_{+,X}^*A_{z,X}^{-1}B_{+,X},
\]

not by the original endpoint Evans function (F_X(z)).

Thus dagger completion changes the spectral equation unless a separate
comparison theorem identifies the two.

## The actual promotion constructor

The zero-to-dagger promotion is exactly the following source cell:

\[
S_X(z)=u_X(z)F_X(z),
\]

where (u_X) is explicit and nowhere zero on the admitted domain.

If this identity is constructed with:

- (B_{-,X}=B_{+,X}^*) in the actual source metrics;
- (C_{z,X}) derived independently from endpoint, primitive, square, seam,
  and archimedean currents;
- cutoff-natural comparison units (u_X);
- completion-stable domains and determinants;

then an Evans zero becomes a kernel state of the dagger reciprocal
colligation. That is precisely the missing promotion.

## Fitting obstruction

For scalar blocks, one can always define

\[
C=B^*A^{-1}B+F
\]

and force Schur–Evans equality. This is algebraically empty if (C) was
chosen after reading (F).

The checker uses (A=2), (B=3), and (F(z)=z). The independent fixture
(C(z)=5+z) gives

\[
S(z)=z+\frac12,
\]

so the Evans zero at zero is not a dagger-colligation zero. The fitted choice
(C(z)=9/2+z) gives (S(z)=z) exactly, demonstrating why equality alone is
not source authority.

## DPC verdicts

1. Promoted: the scalar block and return incidence are source-derived, and
   Schur–Evans agreement holds up to a completion-stable unit.
2. Adjoint residual: the return channel fails to equal the Hilbert adjoint in
   the declared topology.
3. Divisor mismatch: the dagger colligation exists but its Schur determinant
   has different zeros from the Evans endpoint determinant.
4. Fitted block: agreement holds only because (C) was defined from (F) or
   its zeros.
5. Completion mismatch: every finite cutoff agrees but the units or domains
   collapse in the limit.

## Remaining source calculation

The scalar block (C_{z,X}) is now the narrow target. It must be assembled
from the typed boundary currents before the Schur complement is computed.
The first decisive output is not positivity: it is the prime-by-prime residual

\[
C_{z,X}
-B_{+,X}^*A_{z,X}^{-1}B_{+,X}
-u_X(z)F_X(z).
\]

A nonzero residual closes this promotion route. Exact vanishing advances to
the Green orientation and completion gates.

## Cross-sector reading

This is the same structural issue Benincasa found in dimensional transport:
the low specialized fibers do not themselves supply the chain map mixing the
high exact sector with the boundary costalk. Here the endpoint Evans system
and the dagger colligation are valid neighboring structures, but their
comparison requires an independently authorized boundary block.

## Verification

Run:

```powershell
python research/nima/checkers/check_rh_schur_evans_promotion.py
```
