# The coupled electron cuts reconstruct the full real \(\Phi_1\) slice

Owner: `marici.Nima`

At fixed physical transfer

\[
T=-\frac14,
\qquad
\nu=s+\frac T2,
\]

we evaluated the two source-labelled spectral channels

\[
\rho_R=C_{++,++},
\qquad
\rho_L=C_{+-,+-}
\]

over the complete electron cut.  The dispersive part was assembled as

\[
D(\nu,T)
=\frac{\nu^2}{\pi}
\int_{4+T/2}^{\infty}
\frac{d\nu'}{\nu'^2}
\left[
\frac{\rho_R}{\nu'-\nu}
+\frac{\rho_L}{\nu'+\nu}
\right].
\]

The independent exact one-loop amplitude was evaluated using the source
\(w,z\) branches and normalization \(8\alpha^2\). We fitted

\[
\Phi_1(\nu,T)-D(\nu,T)=a(T)+b(T)\nu
\]

at only the first two real points.  The resulting values are

\[
a(-1/4)\approx2.4357754\times10^{-5},
\qquad
b(-1/4)\approx3.9107195\times10^{-4}.
\]

The same affine packet predicts three held-out points through \(s=2\), with
maximum relative residual

\[
1.69\times10^{-6}.
\]

The coarse/fine quadrature change is

\[
7.18\times10^{-6}
\]

relative to the amplitude scale, so the observed residual is below the
independent integration uncertainty.

## Interpretation

On this hostile nonforward real slice:

- the labelled right and left cuts are both necessary;
- the crossing-authorized two-dimensional subtraction space is sufficient;
- no non-affine residual is detected;
- consequently there is no evidence here for a missing cut or inner/CDD
  factor.

This is not yet the global classification.  It must be replicated at another
transfer and at complex-conjugate points.  The present result does establish
that the previously observed nonforward moment contamination is organized by
a genuine full dispersion relation rather than by fitted EFT coefficients.

## Independent-transfer replication

The same construction was repeated at

\[
T=-\frac12
\]

using a separately evaluated spectral packet and five new real points.  Its
three held-out points have relative residual

\[
1.03\times10^{-6}.
\]

The fitted coefficients satisfy

\[
\frac{a(-1/2)}{a(-1/4)}\approx4.03,
\qquad
\frac{b(-1/2)}{b(-1/4)}\approx2.02.
\]

This is the source-softness pattern

\[
a(T)=O(T^2),
\qquad
b(T)=O(T).
\]

Thus the two subtraction directions are not free constants: crossing fixes
their helicity eigenspaces, and gauge softness fixes their first allowed
transfer grades.  What remains is to derive the complete transfer dependence
from the crossed source, rather than fit it independently at each \(T\).

There is a canonical boundary-jet interpretation. Since the dispersive
integral begins with \(\nu^2\),

\[
a(T)=\Phi_1(0,T),
\qquad
b(T)=\partial_\nu\Phi_1(0,T).
\]

The subtraction packet is therefore the first jet of the amplitude at the
crossing-fixed point, not an arbitrary phase choice. Its leading
Euler--Heisenberg term is \(g_2s^2\), with \(s=\nu-T/2\), and predicts

\[
a(T)=\frac{g_2T^2}{4}+O(T^3),
\qquad
b(T)=-g_2T+O(T^2).
\]

The observed ratios are the finite-transfer version of these laws. The
remaining authority question is whether this crossing-fixed jet is derived
by another channel of the same source dispersion system or must be admitted
as independent boundary data.

The replication is checked by
`check_qed_phi1_dispersion_transfer_replication.py`.

Reproduce with:

```text
uv run --with numpy --with mpmath python research/nima/checkers/check_qed_phi1_full_dispersion_real.py
```
