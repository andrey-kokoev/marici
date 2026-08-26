# Theta completed shear is invertible at every scalar zero

## Normal convergence of the transfer coefficient

Assume the source (f) has every positive exponential moment. This holds for
the completed theta tail because of its superexponential decay. Define

\[
 F_L(s)=\int_0^L f(v)e^{sv}\,dv,
 \qquad
 F(s)=\int_0^\infty f(v)e^{sv}\,dv.
\]

For a compact spectral set (K), choose (M) with

\[
 \Re s\le M
\]

for every (s\in K). Then

\[
 \sup_{s\in K}|F(s)-F_L(s)|
 \le
 \int_L^\infty |f(v)|e^{Mv}\,dv,
\]

and the right-hand side tends to zero. Thus (F_L\to F) normally on the
complex plane.

## Completed shear

The cutoff transport matrices are

\[
 S_L(s)=\begin{pmatrix}1&F_L(s)\\0&1\end{pmatrix}.
\]

They converge locally uniformly, hence in finite-dimensional operator norm,
to

\[
 S(s)=\begin{pmatrix}1&F(s)\\0&1\end{pmatrix}.
\]

Their inverses converge in the same topology:

\[
 S_L(s)^{-1}=\begin{pmatrix}1&-F_L(s)\\0&1\end{pmatrix},
 \qquad
 S(s)^{-1}=\begin{pmatrix}1&-F(s)\\0&1\end{pmatrix}.
\]

Therefore the completed transfer is entire and invertible for every spectral
parameter.

## Meaning of a zero

At a scalar zero (s_0),

\[
 F(s_0)=0,
 \qquad
 S(s_0)=I.
\]

The full relational transport does not become singular. Its off-diagonal
transmission coefficient vanishes, so the source input produces no endpoint
displacement. In the Rosenbrock pencil, this is an invariant or transmission
zero obtained after imposing both boundary ports. It is not a puncture of the
complete shear geometry.

This gives a precise form to the distinction between loss of scalar meaning
and loss of the underlying relationship. At a zero, the larger source
comparison remains fully defined and invertible; only one compressed channel
becomes silent.

## Terminal-state convergence

The terminal amplitude for the infinite tail is

\[
 \beta_L(s)=c e^{-sL}\int_L^\infty f(v)e^{sv}\,dv.
\]

Superexponential source decay makes this tend to zero for every fixed (s).
Hence the algebraic boundary cocycle and its terminal coordinate have a
well-defined pointwise completion without invoking reciprocal boundedness.

## Separation from the reciprocal completion

The transfer completion exists for every (s), whereas the full reciprocal
moving-cut norm from packet 202 is bounded only on the critical seam. They are
therefore different completions of different capabilities:

- the shear topology preserves endpoint transfer and scalar continuation;
- the reciprocal topology preserves both valuation orientations and their
  full tail--seam relationship energy.

Scalar nullity belongs naturally to the first topology. It does not
automatically acquire the second. Packet 204's domain obstruction is thus not
a failure of convergence; it is a mismatch between two independently useful
completed structures.

## RH-bearing requirement

To constrain transmission zeros, one needs a source theorem coupling these
two structures. In system language, the missing property could be a
conservative or passive colligation whose metric is derived from the complete
boundary currents and whose transfer coefficient is (F). Neither the
determinant-one shear nor its normal convergence supplies that metric.

The correct question is no longer whether the full transport can become
singular. It cannot. The question is why its source-authorized scalar
transmission channel can become silent only when the reciprocal transport is
lossless.

## Falsifier

The convergence theorem fails if the source lacks the required exponential
moments or if the completed coefficient is not the normal limit of its cutoff
integrals. Any proposed RH coupling fails if it uses only invertibility or
determinant one of the shear, since both properties hold at every scalar zero
and for hostile sources with off-seam zeros.

## Scope

This completes the finite shear cocycle as an entire invertible transfer
system and identifies scalar zeros as silent transmission coefficients. It
does not construct a conservative metric coupling, confine those zeros, or
prove RH.
