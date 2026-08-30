# The raw window disagreement decays faster than every Euler power

## Disagreement vector

Let

\[
d_L=W_{2L}-W_L.
\]

Using

\[
W_t(q)
=
-\int_{q-t}^{q+t}\rho(x)\,dx,
\qquad
\rho(x)=e^{-\pi x^2},
\]

the disagreement is the negative mass in the two annuli

\[
[q-2L,q-L],
\qquad
[q+L,q+2L].
\]

## Core-tail split

Define the Gaussian tail

\[
T(a)
=
\int_{|x|\ge a}\rho(x)\,dx.
\]

If \(|q|\le L/2\), both annular intervals lie in
\(|x|\ge L/2\). Therefore

\[
|d_L(q)|
\le
T(L/2).
\]

If \(|q|>L/2\), use only the trivial bound

\[
|d_L(q)|\le1.
\]

Since the Stieltjes measure is \(d\nu(q)=\rho(q)dq\),

\[
\|d_L\|_\nu^2
\le
T(L/2)^2+T(L/2).
\]

For large \(L\), this gives

\[
\|d_L\|_\nu^2
\le
2T(L/2).
\]

## Gaussian bound

The standard Gaussian tail estimate gives, for \(a>0\),

\[
T(a)
\le
\frac{1}{\pi a}e^{-\pi a^2}.
\]

Hence

\[
\|d_L\|_\nu
\le
C L^{-1/2}
e^{-\pi L^2/8}
\]

for a fixed constant \(C\).

With \(L=\log p\),

\[
\|W_{2\log p}-W_{\log p}\|_\nu
\le
C(\log p)^{-1/2}
\exp\left(
-\frac\pi8(\log p)^2
\right).
\]

This decays faster than \(p^{-m}\) for every fixed \(m>0\).

## Renormalization cost

Suppose a scalar renormalization \(r_p\) is required to keep the
disagreement norm bounded below:

\[
\|r_pd_L\|_\nu\ge c>0.
\]

Then

\[
|r_p|
\ge
cC^{-1}
(\log p)^{1/2}
\exp\left(
\frac\pi8(\log p)^2
\right).
\]

This grows faster than every fixed power of \(p\).

Therefore no Euler half-density factor, polynomial prime weight, or finite
exponential-order budget can compensate a normalization that makes the raw
Stieltjes disagreement uniformly nondegenerate.

## Consequence for the three candidate repairs

The prior alternatives were:

1. retain the prime-dependent soft metric;
2. renormalize disagreement;
3. compress or suppress it in global assembly.

The second option is incompatible with the existing source order budget
unless the source supplies a genuinely super-polynomial normalization.

Thus the viable generic choices reduce to:

- retain the soft direction without local inversion;
- or compress it before completion.

## Mixed assembly remains harmless

The mixed primitive-square coefficient contributes \(p^{-3/2}\). Since
\(d_L\) itself decays super-polynomially, its weighted contribution is
certainly summable.

The obstruction is not bounded synthesis. It is any theorem that tries to
invert or uniformly observe the raw disagreement direction prime by prime.

## Relation to the theta graph

The theta-history auxiliary block has a fixed positive lower scale when
\(M_\Phi<1\). Mapping the raw disagreement isomorphically into that block
would require precisely the super-polynomial inverse scale above.

Hence the window-to-theta comparison cannot be uniformly bi-bounded on the
full two-dimensional raw endpoint plane.

It must become noninvertible asymptotically or use a different
source-normalized endpoint object.

## Hostile

Normalize each finite disagreement vector to unit norm. Every finite cell
then has perfect endpoint area, but the incidence norms grow like at least

\[
\exp\left(
\frac\pi8(\log p)^2
\right),
\]

destroying the completed constructor topology.

## Frontier

The raw Stieltjes disagreement is a finite-prime coordinate but an
asymptotically disappearing completion direction. The first Adams edge should
therefore be formulated as a bounded weighted relation or compression, not a
uniformly invertible identification of primitive and square endpoint planes.
