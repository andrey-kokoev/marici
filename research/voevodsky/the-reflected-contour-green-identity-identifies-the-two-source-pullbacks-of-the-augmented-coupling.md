# The reflected contour Green identity identifies the two source pullbacks of the augmented coupling

## Common analytic core

Let \(\mathcal C_S\) be the finite-character Mellin--Schwartz source core whose
transforms extend analytically to the open strip

\[
|\operatorname{Im}z|<\frac12
\]

and admit the completed endpoint traces at \(z=\pm i/2\). For \(g,h\in\mathcal
C_S\), put

\[
F_{g,h}(z)=m_g(z)\overline{m_h(\bar z)}.
\]

## One reflected differential

Use

\[
\Omega_S(z)
=
\frac1{2i}\partial_z\log\frac{M_S(z)}{M_S^\#(z)}
+
\varepsilon_{end}\frac{2z}{z^2+1/4}.
\]

On the real boundary, its first term is the gamma--prime connection
\(V_{loc,S}\). Its rational term has residues at \(\pm i/2\) equal to the two
completed endpoint evaluations.

Cauchy deformation on a finite indented strip, followed by the admitted
Schwartz boundary limit, gives

\[
\boxed{
\frac1{2\pi i}
\int_{\partial\mathfrak S}
F_{g,h}(z)\Omega_S(z)\,dz
=
\langle m_g,V_{loc,S}m_h\rangle
+
E_{end,S}(g,h).}
\]

The same contour integral is the Fourier image of the physical Green boundary
form obtained by integration by parts in logarithmic position. Therefore

\[
\boxed{
B_S^{spectral}(g,h)=B_S^{graph}(g,h)}
\]

on \(\mathcal C_S\).

## Endpoint polarization

Writing

\[
e_g=
\begin{pmatrix}m_g(i/2)\\m_g(-i/2)\end{pmatrix},
\qquad
J_{end}=
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

the residue term is

\[
E_{end,S}(g,h)=e_h^*J_{end}e_g
\]

with the global orientation fixed by the explicit formula. Thus the contour
identity identifies the complete even/odd endpoint swap form, not only its
diagonal values.

## Extension to the augmented carrier

The spectral term is bounded on the phase-energy completion because

\[
\mathcal A_S=M_{V_{loc,S}/e_S}
\]

is bounded there. The endpoint and value/flux traces are bounded on the
second-order relative graph completion. Hence both sides of the boxed source
identity are continuous in the augmented norm

\[
\mathscr K_S=
\mathscr E_S\oplus\mathscr H_{end,S}.
\]

Density of \(\mathcal C_S\) gives a unique bounded extension

\[
B_S:\mathscr E_S\to\mathscr H_{end,S}
\]

in the source-generated closure, and the graph and spectral definitions agree
there.

## Successor compatibility

Adjoining a prime changes \(\Omega_S\) by

\[
\frac1{2i}\partial_z\log\frac{m_q}{m_q^\#}\,dz.
\]

The increment is additive, while the endpoint rational differential is
unchanged. Therefore the coupling obeys the same affine connection law as the
Euler successor and preserves the single endpoint bundle. Seam translation is
isometric in the translated graph metric. Consequently the extended coupling
is natural under the admitted prime and seam successors.

## Result

The formerly conditional block

\[
\mathbb G_S=
\begin{pmatrix}
\mathcal A_S&B_S^*\\
B_S&J_{end}
\end{pmatrix}
\]

is now identified on a common source core and extends as a bounded
self-adjoint operator on the source-generated augmented carrier.

This closes the signed mixed Green identification. It does not prove positivity
of \(\mathbb G_S\); after parity reduction, that remains the Schur inequality
for its odd endpoint block.

## Analytic qualifications

The statement uses the already admitted contour deformation and endpoint
normalization. At Euler zeros on the strip boundary, contours are indented and
the prescribed local principal-value limit is taken. No claim of an ordinary
upper-half-plane Herglotz function is made.
