# Cubic Dyson Keldysh-ratio pilot

## Frozen algebraic pilot

Work in a translation-invariant, convolution-collapsed closed-time-path
algebra.  Write

\[
G=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad a+d=b+c.
\]

The identity is the standard largest-time/CTP relation.  Linearization of
the cubic self-energy along Entry 1577's common statistical tangent gives

\[
\delta\Sigma=
2\begin{pmatrix}a&-b\\-c&d\end{pmatrix}.
\]

The correctly typed Dyson composition is ordinary matrix contraction

\[
\delta G_{\rm out}=G\,\delta\Sigma\,G.
\]

No additional contour metric is inserted: the two vertex signs are already
present in (\delta\Sigma).

## Exact result

Symbolica verifies

\[
\delta G^{++}_{\rm out}+\delta G^{--}_{\rm out}
-\delta G^{+-}_{\rm out}-\delta G^{-+}_{\rm out}=0.
\]

An extra metric insertion instead produces a generically nonzero CTP defect,
so it double-counts the contour variance.

Define

\[
F=\frac{b+c}{2},
\qquad
\rho=c-b,
\qquad
G^R=a-b.
\]

For

\[
H=3a^2+b^2+c^2-3ab-3ac+bc,
\]

the exact output is

\[
\boxed{
F_{\rm out}=2HF,
\qquad
\rho_{\rm out}=2H\rho,
\qquad
G^R_{\rm out}=2(G^R)^3.
}
\]

Therefore

\[
\boxed{
\frac{F_{\rm out}}{\rho_{\rm out}}
=\frac{F}{\rho}
}
\]

where the ratio is defined.

## Scope

This is an exact contour-algebra theorem for the convolution-collapsed
pilot.  It does not prove the corresponding statement for the full
time-dependent integral kernel: there, the three propagator factors carry
different time arguments and need not share one pointwise (H).

## Next finite falsifier

Restore one internal-time convolution while retaining symbolic Wightman
labels.  Test whether the statistical and spectral outputs still admit the
same integral kernel before momentum integration.  Equality proves
integrand-level preservation of the occupation ratio; inequality localizes
the first genuine channel-mixing term.

