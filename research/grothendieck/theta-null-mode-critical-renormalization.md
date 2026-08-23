# Exact null-mode critical renormalization at the quarter center

## Canonical half-line splitting

For \(u\ge0\), the renormalized precursor has the exact form

\[
K(u)=\frac12e^{-u/2}-R_\theta(u),
\]

where

\[
\boxed{
R_\theta(u)=
e^{u/2}\sum_{n\ge1}e^{-\pi n^2e^{2u}}>0.
}
\]

The first term is the decaying null mode of
\(1/4-\partial_u^2\). The theta remainder is positive and
superexponentially decaying.

Let \(c=1/4\), \(w=z^2\), and define

\[
I(w)=\int_0^\infty K(u)\cosh(zu)\,du.
\]

Inside \(|\Re z|<1/2\),

\[
\int_0^\infty\frac12e^{-u/2}\cosh(zu)\,du
=\frac{1}{4(c-w)}.
\]

Put

\[
T(w)=\int_0^\infty R_\theta(u)cosh(\sqrt w\,u)\,du.
\]

Because \(R_\theta\) decays superexponentially, \(T\) is entire in \(w\).
Therefore

\[
\boxed{
I(w)=\frac{1}{4(c-w)}-T(w).
}
\]

## Exact completed function

Under the half-line normalization used for the angular current,

\[
C(w)=(c-w)I(w).
\]

Substitution gives the entire identity

\[
\boxed{
C(w)=\frac14+(w-c)T(w).
}
\]

This identity is first derived in the convergence strip, then extends to all
\(w\) by analyticity. The completion factor cancels the entire divergent null
mode to the constant \(1/4\); every nonconstant contribution lies in the
superexponentially convergent theta transform \(T\).

Thus the critical renormalization is exact:

\[
\boxed{
\text{divergent precursor mass}
\xrightarrow{\;c-w\;}
\text{finite endpoint constant}.
}
\]

## Angular current after subtraction

Differentiation gives

\[
C'(w)=T(w)+(w-c)T'(w),
\]

and hence

\[
\boxed{
H(w)=(w-c)
\frac{T(w)+(w-c)T'(w)}{1/4+(w-c)T(w)}.
}
\]

This formula is entire-source and globally meaningful away from zeros of the
displayed denominator. It contains no divergent precursor integral.

At the threshold,

\[
\boxed{H(c)=0,\qquad H'(c)=4T(c)>0.}
\]

Since \(T(c)>0\) follows directly from its positive theta integral, diagonal
Loewner positivity holds strictly at the source-forced center and therefore
on some open real neighborhood of it.

This is local, not global, and it does not establish any coupled Loewner
minor.

## Meaning of the threshold coincidence

The same null mode produces:

1. the decay exponent \(1/2\) of \(K\);
2. the precursor convergence boundary \(|\Re z|=1/2\);
3. the squared threshold \(w=c=1/4\);
4. the completion multiplier \(c-w\);
5. the constant endpoint term \(1/4\); and
6. the center of the angular characteristics.

The probability measure fails at the threshold because its mass escapes to
infinity, while the completed invariant stays finite because the source
operator annihilates precisely that escaping null mode.

## New source-side opportunity

The entire transform \(T\) comes from a positive superexponential kernel.
Unlike the precursor transform \(I\), it has no convergence wall. The global
Gram problem may therefore be attacked using

\[
C=\frac14+(w-c)T
\]

rather than analytic continuation of a divergent probability measure.

But positivity of the real-space theta remainder does not by itself prove the
Herglotz property. The denominator mixes the positive constant with the
centered transform, and generic positive superexponential kernels can fail
the required Loewner inequalities. The source-specific target is a coupled
inequality for \(T,T'\), not mere positivity of \(T\).

The exact denominator-free current and Loewner kernel now split into a linear
endpoint--theta channel and a quadratic theta--theta channel. The endpoint
term seeds positive orientation at the threshold, but the two terms must be
controlled as a coupled block; see
`theta-endpoint-remainder-coupled-loewner-decomposition.md`.

## Falsifiers

1. Any normalization inconsistent with \(C(c)=1/4\) falsifies the splitting.
2. A negative Loewner minor of the exact rational expression in \(T\)
   falsifies global positivity.
3. A proposed proof that discards the constant \(1/4\) discards the completed
   null-mode contribution and is inadmissible.
