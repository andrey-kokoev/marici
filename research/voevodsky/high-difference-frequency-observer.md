# High-difference frequency observer

## Question

What frequency region is actually observed by the near-null polynomial and its equivalent high finite difference?

## Claim boundary

The observer has an exact Fourier-cosine representation with a unique computable frequency saddle. This replaces coefficient and derivative norms by a localized multiplier problem. No bound on the prime cosine sum is proved.

## Heat atom transform

For \(a,t>0\),

\[
\int_0^\infty
e^{-t\xi^2}
\cos(2\sqrt a\,\xi)
\,d\xi
=
\frac{\sqrt\pi}{2\sqrt t}e^{-a/t}.
\]

With

\[
a_n=\frac{(\log n)^2}{4},
\]

this becomes

\[
t^{-1/2}e^{-(\log n)^2/(4t)}
=
\frac2{\sqrt\pi}
\int_0^\infty
e^{-t\xi^2}
\cos(\xi\log n)
\,d\xi.
\]

Applying \(q\) finite differences multiplies the Fourier heat factor by

\[
(1-e^{-h\xi^2})^q.
\]

Thus the exact frequency filter is

\[
W_{q,t,h}(\xi)
=
e^{-t\xi^2}(1-e^{-h\xi^2})^q.
\]

For \(p_m(y)=(1-y)^m\), one has \(q=2m+1\).

## Saddle location

Set \(r=\xi^2\). Then

\[
w(r)=e^{-tr}(1-e^{-hr})^q.
\]

Its logarithmic derivative is

\[
\frac{d}{dr}\log w(r)
=
-t+
\frac{qh}{e^{hr}-1}.
\]

The unique maximum occurs at

\[
r_*
=
\frac1h
\log\left(1+\frac{qh}{t}\right).
\]

Therefore the observed frequency is centered at

\[
\xi_*^2
=
\frac1h
\log\left(1+\frac{qh}{t}\right).
\]

The logarithmic curvature at the maximum is

\[
\left.
\frac{d^2}{dr^2}
\log w(r)
\right|_{r=r_*}
=
-rac{t(t+qh)}q.
\]

This supplies both the center and the concentration scale for a saddle analysis.

## Fixed scaled mesh

For \(h=\kappa t\),

\[
\xi_*^2
=
\frac{
\log(1+q\kappa)
}{
\kappa t
}.
\]

Increasing rank therefore moves the observer only logarithmically in \(q\) relative to the base heat frequency \(t^{-1/2}\):

\[
\xi_*
\asymp
\sqrt{
\frac{\log q}{t}
}.
\]

This explains the \(\log\log m\) gamma correction: the archimedean symbol grows like \(\log\xi_*\).

## Prime-side reformulation

Formally inserting the prime weights gives a filtered cosine sum of the form

\[
\int_0^\infty
W_{q,t,h}(\xi)
\left[
\sum_{n\geq2}
\Lambda(n)n^{-1/2}
\cos(\xi\log n)
\right]
\,d\xi.
\]

The bracket is not to be treated as an absolutely convergent pointwise series on the critical boundary. It requires the source-defined distributional or regularized interpretation inherited from the heat kernel. Interchanging the prime sum and the frequency integral without that control would reintroduce a defect.

## Coherence consequence

Three observers coincide:

1. the polynomial observer \((1-y)^m\);
2. the high-difference observer \(\Delta_h^{2m+1}\);
3. the frequency observer with multiplier \(W_{2m+1,t,h}\).

The Vandermonde and Fourier identities are their coherencers, and both have zero algebraic residue. The remaining residue is a localized analytic estimate of the regularized prime cosine distribution against \(W_{q,t,h}\).

## Disposition

The rank-uniform problem is now localized near the explicit frequency \(\xi_*\). A useful theorem must compare the regularized prime translation form with the logarithmic archimedean multiplier in the weighted norm defined by \(W_{q,t,h}\), uniformly over \(q,t,h\). This is sharper than coefficientwise, Euclidean, or global derivative bounds.

## Verification

- `research/voevodsky/checkers/check_high_difference_frequency_observer.py`
- `research/voevodsky/results/high_difference_frequency_observer.json`
