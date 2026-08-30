# Mellin transformation turns the rank-one seam into an Epstein coherence matrix

## Bounded question

What survives if the circle commutator identity is Mellin-transformed before
the seam channel is compressed to its scalar norm?

## Normalization

Let `A` be the nonnegative winding Laplacian

\[
 Ae_n=n^2e_n,
\]

and set

\[
 E_t=e^{-\pi tA/2},
 \qquad
 v_t=E_t\delta_0
 =\sum_{n\in\mathbb Z}e^{-\pi tn^2/2}e_n.
\]

After the harmless rescaling from packet 104, the heat-sandwiched seam balance
is

\[
 -E_t^2+|v_t\rangle\langle v_t|.
\]

Its trace vanishes for every `t>0`.

## Mellin transform before trace compression

Let `P_0^perp` project away from the constant winding mode and put
`v_t^0=P_0^perp v_t`.  For `Re(s)>1`, define on the mean-zero sector

\[
 D_s
 =\int_0^\infty t^{s/2}E_t^2\,\frac{dt}{t},
\]

\[
 M_s
 =\int_0^\infty t^{s/2}|v_t^0\rangle\langle v_t^0|\,\frac{dt}{t}.
\]

The diagonal bulk is

\[
 \langle e_m,D_se_n\rangle
 =\delta_{mn}\,\Gamma(s/2)\pi^{-s/2}|n|^{-s}.
\]

The seam operator instead has the full matrix

\[
 \boxed{
 \langle e_m,M_se_n\rangle
 =\Gamma(s/2)
 \left(\frac{\pi(m^2+n^2)}{2}\right)^{-s/2}}
\]

for `m,n != 0`.  The zero channel and its cross terms are handled separately
by the usual completion endpoint.  Thus Mellin transformation converts a moving family of
rank-one seam states into an infinite coherence matrix governed by the
quadratic form `m^2+n^2`.

## Information erased by the theta trace

On the diagonal,

\[
 \langle e_n,M_se_n\rangle
 =\Gamma(s/2)\pi^{-s/2}|n|^{-s}
 =\langle e_n,D_se_n\rangle.
\]

Hence

\[
 \operatorname{Tr}(M_s-D_s)=0
\]

whenever the interchange is justified.  But only the diagonal cancels.
Every off-diagonal entry of `M_s` remains.  Scalar theta and zeta traces had
discarded precisely these relative-winding correlations.

This yields the exact decomposition

\[
 \boxed{
 M_s=D_s+C_s,
 \qquad \operatorname{diag}C_s=0,}
\]

where `C_s` is the completed seam-coherence operator.  The scalar zeta data
are the common diagonal; the additional source provenance lies in `C_s`.

## Positivity and its limit

For real `s>1`, `M_s` is positive because it is an integral of positive
rank-one operators.  This does not make `C_s=M_s-D_s` positive; a nonzero
Hermitian matrix with zero diagonal cannot be positive.  Therefore the
off-diagonal coherence is an oriented interaction, not another hidden
positive measure.

The full matrix is a two-dimensional Epstein-type object.  Its quadratic
form is

\[
 \langle c,M_sc\rangle
 =\Gamma(s/2)\left(\frac2\pi\right)^{s/2}
 \sum_{m,n}\frac{\overline{c_m}c_n}{(m^2+n^2)^{s/2}},
\]

 with both axes removed and with convergence interpreted first in the stated
 chamber.  It couples the two winding copies that the two-copy theta-curvature
programme had previously introduced by direct expansion.

## Explanatory consequence

The apparent scalar problem is secretly a two-sector matrix problem:

\[
 \text{one circle seam ket at each scale}
 \xrightarrow{\text{Mellin}}
 \text{two-winding Epstein coherence}
 \xrightarrow{\text{diagonal trace}}
 \text{completed zeta readout}.
\]

This is a concrete candidate for the information that hostile self-Fourier
scalar carriers fail to preserve.  They may reproduce the trace and modular
reflection while lacking this exact source-derived off-diagonal matrix.

## Remaining RH gate

No RH conclusion follows yet.  The trace of `M_s-D_s` is identically zero,
not `Xi(s)`, and positivity in the initial real chamber does not survive as a
simple sign after analytic continuation.

The next attack is to apply the completed Clark/endpoint differential to the
operator pair `(M_s,D_s)` and determine whether its relative determinant or a
distinguished vacuum minor equals `Xi`.  The strongest falsifier is a hostile
carrier that admits the same Epstein coherence matrix and completion law but
has an off-critical zero.
