# Theta Evans residual is a forward versus backward Poisson comparison

## Bounded question

Can the oscillatory separation residual be placed inside a transform with an
automatic positivity domain, so the exact missing continuation law becomes
visible?

## Autocorrelation

For the positive half-line source (f), define

\[
A(r)=\int_0^\infty f(q)f(q+r)\,dq,
\qquad r\ge0.
\]

Extend it evenly to the real line. This is an autocorrelation kernel, so its
Fourier transform is nonnegative:

\[
\widehat A(t)=|\widehat f(t)|^2\ge0.
\]

## Forward Poisson transform

For \(\lambda>0\), put

\[
C(\lambda,t)
=\int_0^\infty e^{-\lambda r}\cos(tr)A(r)\,dr.
\]

The even kernel (e^{-\lambda|r|}) has a positive Fourier transform.
Consequently (C(\lambda,t)) is, up to normalization, the Poisson convolution
of \(|\widehat f|^2\) and is nonnegative for every forward height
\(\lambda>0\).

At the boundary,

\[
C(0,t)=\frac12|\widehat f(t)|^2\ge0.
\]

This positivity is universal and uses no modular arithmetic.

## Backward continuation

The completed theta source decays fast enough that (C(\lambda,t)) continues
to negative \(\lambda\) in the required finite range. The Evans residual from
packet 231 satisfies

\[
R_f(a+it)
=2\left(C(a,t)-C(-a,t)\right).
\]

Thus the unresolved sign is a comparison between:

- the forward Poisson evolution (C(a,t)), controlled by positivity;
- its backward analytic continuation (C(-a,t)), which is not controlled by
  the Poisson semigroup.

Backward Poisson evolution is ill-posed for generic boundary data. Rapid theta
decay makes it exist, but existence does not orient it.

## Equivalence of the apparent lanes

The following are now the same problem in different coordinates:

1. sign of the doubled Evans forcing residual;
2. orientation of the positive separation-measure transform;
3. vertical monotonicity of the completed theta modulus;
4. comparison of forward and backward Poisson continuation.

This explains why repeated Green, curvature, and de Branges calculations kept
returning the same obstruction.

## Exact missing theorem

The needed modular statement is a backward-Poisson comparison law for the
specific theta autocorrelation:

\[
\operatorname{sgn}
\left(C(a,t)-C(-a,t)\right)
=-\operatorname{sgn}a
\]

with the sign adjusted to the chosen Green orientation. Equivalently, the
completed source must select a direction of vertical evolution that generic
positive boundary spectra do not possess.

This theorem must be derived from reciprocal theta sewing or arithmetic label
coherence. Positivity of \(|\widehat f|^2\), rapid decay, and evenness are
insufficient.

## Hostile falsifier

Choose a nonnegative spectral density concentrated near two separated
frequencies. Its forward Poisson extension remains positive, while its backward
continuation can reverse the required comparison at a finite height. Any
candidate theorem that depends only on nonnegative boundary spectrum and
entire continuation is therefore false.

## Scope

This packet rewrites the exact Evans residual as a forward-versus-backward
Poisson comparison and identifies it with the earlier vertical-modulus
obstruction. It does not prove the theta-specific comparison law or RH.
