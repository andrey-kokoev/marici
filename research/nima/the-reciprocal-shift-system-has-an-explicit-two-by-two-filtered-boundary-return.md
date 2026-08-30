# The reciprocal shift system has an explicit two-by-two filtered boundary return

## Boundary control realization

Let \(A\) be the right-shift generator on the half-line and let \(B\) be the canonical boundary injection into its extrapolation space:

\[
Bb=b\delta_0.
\]

For \(\operatorname{Re}z>0\), the boundary Poisson state is

\[
(z-A)^{-1}Bb
=
b e^{-zt}
\]

with the sign convention adjusted to the frozen generator orientation.

Define the theta observation

\[
C_\Phi f
=
\int_0^\infty\Phi(t)f(t)\,dt.
\]

Then the scalar transfer is exactly

\[
C_\Phi(z-A)^{-1}B
=
\int_0^\infty\Phi(t)e^{-zt}\,dt
=
m_\Phi(z).
\]

Thus the abstract finite-rank sewing maps are no longer free at the analytic level:

\[
U=B,
\qquad
V^*=C_\Phi,
\qquad
G(z)=m_\Phi(z).
\]

Boundary injection comes from endpoint incidence; observation comes from the independently fixed completed theta density.

## Reciprocal double

Introduce direct and reciprocal channels. Their one-sided returns are

\[
m_+(z)=m_\Phi(z),
\qquad
m_-(z)=m_\Phi(-z),
\]

where the second is understood by the entire continuation supplied by rapid theta decay and by the opposite-sector chart.

In the oriented sheet basis, the return is diagonal:

\[
G_{\mathrm{sheet}}(z)
=
\begin{pmatrix}
m_+(z)&0\\
0&m_-(z)
\end{pmatrix}.
\]

On the seam, reality of \(\Phi\) gives

\[
m_-(i\omega)
=
\overline{m_+(i\omega)}.
\]

Each sheet propagation is outer in its own open half-plane.

## Wall--jump basis

Apply the normalized Hadamard transform

\[
H_2
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\]

The return becomes

\[
G_{\mathrm{wj}}(z)
=
H_2G_{\mathrm{sheet}}(z)H_2^*
=
\begin{pmatrix}
a(z)&b(z)\\
b(z)&a(z)
\end{pmatrix},
\]

where

\[
a(z)
=
\frac{m_+(z)+m_-(z)}2,
\qquad
b(z)
=
\frac{m_+(z)-m_-(z)}2.
\]

The two entries have the required reciprocal characters:

\[
a(-z)=a(z),
\qquad
b(-z)=-b(z).
\]

On the seam,

\[
a(i\omega)=\operatorname{Re}m_\Phi(i\omega),
\]

and

\[
b(i\omega)=i\operatorname{Im}m_\Phi(i\omega).
\]

Thus the even completed theta section and the odd Wronskian or flux coordinate are the two components of one source-derived return matrix.

## Completed scalar shadow

In the conventional normalization,

\[
\Xi(\omega)
=
m_\Phi(i\omega)+m_\Phi(-i\omega)
=
2a(i\omega).
\]

Therefore a scalar completed zero is

\[
a(i\omega)=0.
\]

It does not imply \(m_+(i\omega)=0\) or \(m_-(i\omega)=0\). At such a point the two outer sheet returns are nonzero and opposite in real projection, while the odd return \(b(i\omega)\) may remain nonzero.

This gives the exact operator meaning of reciprocal boundary cancellation.

## The return is not yet the spectral pencil

The matrix \(G_{\mathrm{wj}}\) is the propagated boundary return. A spectral collision still requires a source constitutive relation \(C_{\mathrm{arith}}(z)\):

\[
I-C_{\mathrm{arith}}(z)G_{\mathrm{wj}}(z).
\]

Choosing \(C_{\mathrm{arith}}\) after inspecting \(\Xi\) would fit the zero divisor and be circular.

The remaining arithmetic theorem must derive \(C_{\mathrm{arith}}\) from:

- primitive and square Euler coefficients;
- the complete weighted Hadamard pushforward;
- reciprocal sewing;
- archimedean endpoint attachment;
- the source determinant-line normalization.

## Exact determinant formula

Write

\[
C_{\mathrm{arith}}
=
\begin{pmatrix}
c_{ww}&c_{wj}\\
c_{jw}&c_{jj}
\end{pmatrix}.
\]

Then the boundary defect is explicitly

\[
D_\partial
=
I-C_{\mathrm{arith}}
\begin{pmatrix}
a&b\\
b&a
\end{pmatrix}.
\]

Its determinant is

\[
\det D_\partial
=
1
-
a\operatorname{tr}C_{\mathrm{arith}}
-
b(c_{wj}+c_{jw})
+
\det(C_{\mathrm{arith}})(a^2-b^2).
\]

Since

\[
a^2-b^2=m_+m_-,
\]

the four possible scalar contributions are now separated:

- even return \(a\);
- odd return \(b\);
- reciprocal product \(m_+m_-\);
- constant unit term.

This is the smallest coefficient comparison capable of testing a proposed arithmetic sewing law.

## Symmetry constraints

If reciprocal reflection is represented by

\[
R=\begin{pmatrix}1&0\\0&-1\end{pmatrix}
\]

in wall--jump coordinates, covariance of the pencil requires the declared transformation law relating

\[
C_{\mathrm{arith}}(-z)
\quad\text{and}\quad
RC_{\mathrm{arith}}(z)R.
\]

A reciprocal-even constitutive law forces its off-diagonal entries to be odd in \(z\). A constant diagonal law cannot by itself convert the even return into the completed zeta determinant without also producing the reciprocal-product term.

These coefficient constraints provide immediate falsifiers before any operator completion estimate.

## Minimality

The boundary input \(B=\delta_0\) is the canonical cyclic input for the shift semigroup. The theta observation is outer, so the reciprocal observation has no exact dark state. Hence the two-channel realization is minimal on the shift support, although it is not uniformly observable.

This is sufficient for determinant identification up to a nowhere-zero realization unit; it is not a five-margin coercivity theorem.

## Frontier contraction

The analytic return is now explicit and source-authorized:

\[
G_{\mathrm{wj}}(z)
=
\begin{pmatrix}
a(z)&b(z)\\
b(z)&a(z)
\end{pmatrix}.
\]

The next irreducible calculation is purely arithmetic:

> Derive the two-by-two constitutive matrix \(C_{\mathrm{arith}}(z)\) from the complete primitive--square wall--jump pushforward and compare the four coefficients in \(\det(I-C_{\mathrm{arith}}G_{\mathrm{wj}})\) with the source completed determinant section.

This is the first finite matrix where determinant identification can be proved or falsified without fitting the analytic propagation.
