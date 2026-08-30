# The Tate phase current is minus twice the Riemann–Siegel phase current

Define the Riemann–Siegel theta function by

\[
\vartheta(t)
=
\operatorname{Im}\log\Gamma\left(\frac14+\frac{it}{2}\right)
-\frac t2\log\pi,
\]

with the branch continuous from \(t=0\).

On the critical seam,

\[
\chi_\infty(1/2+it)
=
\pi^{it}
\frac{\Gamma(1/4-it/2)}{\Gamma(1/4+it/2)}.
\]

Since the numerator and denominator are conjugate,

\[
\arg\chi_\infty(1/2+it)
=
-2\vartheta(t).
\]

Therefore the phase-current identity from event 10277 sharpens to

\[
\theta_\infty'(t)
=
-2\vartheta'(t).
\]

Indeed,

\[
\vartheta'(t)
=
\frac12
\operatorname{Re}\psi\left(\frac14+\frac{it}{2}\right)
-\frac12\log\pi,
\]

which gives

\[
-2\vartheta'(t)
=
\log\pi
-
\operatorname{Re}\psi\left(\frac14+\frac{it}{2}\right).
\]

## Zero-counting scope

The smooth archimedean density in the Riemann–von Mangoldt count is

\[
\rho_\infty(t)
=
\frac1\pi\vartheta'(t).
\]

Hence

\[
\theta_\infty'(t)
=
-2\pi\rho_\infty(t).
\]

This is the precise source-native linking identity available from the gamma
cell.

It must not be overstated. The full zero-counting current also contains the
arithmetic argument contribution. Schematically,

\[
dN
=
\rho_\infty(t)\,dt+dS(t)+\text{endpoint terms}.
\]

Thus the Tate phase identifies the smooth archimedean zero-section current,
not the complete zero current.

## Constructor consequence

The three proposed odd ports now have a scoped hierarchy:

1. Tate phase/Wronskian gamma port:
   \[
   d\arg\chi_\infty=-2\,d\vartheta;
   \]
2. smooth zero-section port:
   \[
   d\vartheta=\pi\rho_\infty(t)\,dt;
   \]
3. full zero-section port:
   requires adding the arithmetic argument current \(dS\).

Therefore a theorem equating the causal-history odd current directly with
the full zero current would omit a source component. The correct first
intertwiner is with the archimedean smooth current. Arithmetic prime
incidence must supply the residual argument current through a separate
constructor.

The high-frequency asymptotic becomes the familiar density law

\[
\rho_\infty(t)
=
\frac1{2\pi}\log\frac{|t|}{2\pi}
+O(t^{-2}),
\]

while

\[
\theta_\infty'(t)
=
-\log\frac{|t|}{2\pi}
+O(t^{-2}).
\]

This also explains why the Tate phase current is logarithmically unbounded:
it is the negative twice-\(\pi\) multiple of the smooth zero density.

The next compatibility square should therefore compare the arithmetic
argument current from the Euler constructor with the residual
\(dN-\rho_\infty dt\), rather than asking the gamma cell to reproduce all
zeros.
