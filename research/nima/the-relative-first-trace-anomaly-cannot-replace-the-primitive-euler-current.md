# The relative first-trace anomaly cannot replace the primitive Euler current

## Finite trace formula

On a finite prime cutoff, let

\[
L(s)e_p=p^{-s}e_p
\]

and let the primitive incidence column be

\[
b_p(s)=p^{-s}u_{p,1}.
\]

The seam coefficient metric contributes the forced adjoint weight
\((\log p)^{-1}\).  With \(G(s)=D_0(s)^{-1}\), cyclicity gives

\[
\operatorname{Tr}K_{{\rm rel},X}(s)
=
\sum_{p\le X}
\frac{p^{-2s}}{(1-p^{-s})\log p}
\left\langle u_{p,1},G(s)u_{p,1}\right\rangle
+	ext{square and connected terms}.
\]

This formula follows from

\[
K_{\rm rel}=(I-L)^{-1}B^\dagger GB
\]

and uses only diagonal entries of the return; cross-prime terms do not enter
the trace.

## Centered seam

At \(s=1/2\), boundedness of \(G\) and the label-independent cut norm give

\[
\left|
\operatorname{Tr}K_{\rm rel}(1/2)
\right|
\le
C\sum_p
\frac{1}{p(1-p^{-1/2})\log p}
<\infty.
\]

Thus the centered first trace is a genuine boundary-loop quantity.

## Different arithmetic order

The primitive Euler cumulant is

\[
\operatorname{Tr}L_X(s)=\sum_{p\le X}p^{-s}.
\]

The relative first trace begins instead at arithmetic order

\[
\frac{p^{-2s}}{\log p},
\]

up to the bounded Green diagonal and the resolvent factor.  It therefore has:

- twice the primitive exponent;
- an additional forced \((\log p)^{-1}\);
- dependence on the boundary propagator.

Consequently no source identity can identify
\(\operatorname{Tr}K_{\rm rel}\) with \(\operatorname{Tr}L\) on this carrier.
Equal scalar regularization order does not erase their distinct coefficient
asymptotics.

## Reciprocal-overlap divergence

For \(\operatorname{Re}s<1/2\), the model trace budget

\[
\sum_p\frac{p^{-2\operatorname{Re}s}}{\log p}
\]

is no longer trace-class at the same threshold.  This explains why the open
reciprocal overlap uses \(\det_2\): the first relative trace cannot be retained
as an independently convergent scalar there.

The order-two determinant removes that local trace.  Its transition anomaly
must be treated as a determinant-line clutching term between reciprocal
charts, not as a globally defined exponential of
\(\operatorname{Tr}K_{\rm rel}\).

## Correct separation

The finite expression

\[
\exp\left(-\operatorname{Tr}K_{{\rm rel},X}\right)
\det_2(I-K_{{\rm rel},X})
\]

is the ordinary finite Schur determinant.  In the completed overlap its two
factors need not converge separately.  Only their chartwise determinant-line
combination is authorized.

The primitive and square Euler currents remain paired with the bare
\(\det_3\) line.  The relative first-trace anomaly belongs solely to the
boundary-cone clutching line.

## G4 consequence

One proposed shortcut is eliminated: the relative \(\det_2\) anomaly cannot
supply or cancel the primitive Euler cumulant.  The completed compiler must
glue two distinct lines:

1. the Euler \(\det_3\) line with its primitive and square boundary currents;
2. the reciprocal relative \(\det_2\) line with its own transition anomaly.

Their tensor product may still differ from the Xi line by a unit, but that unit
requires a source-derived clutching isomorphism.  Scalar cancellation of the
two first traces is unavailable.  No RH conclusion is authorized.
