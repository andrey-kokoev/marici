# Prime-scale recursion supplies a source-specific Clark repair term

Status: exact modular-source identity and candidate mechanism; no Schur or RH
claim

## Arithmetic translate structure of the theta source

On the positive logarithmic chamber, write the completed theta density as

\[
\Phi(u)=\sum_{n\ge1}\phi_n(u),
\]

with

\[
\phi_n(u)=
\left(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2}\right)
e^{-\pi n^2e^{2u}}.
\]

If

\[
\phi(t)=
\left(4\pi^2e^{9t/2}-6\pi e^{5t/2}\right)e^{-\pi e^{2t}},
\]

then direct substitution gives the exact translate law

\[
\boxed{
\phi_n(u)=n^{-1/2}\phi(u+\log n).
}
\]

For (u\ge0), every summand is positive because
(2\pi n^2e^{2u}>3). This is stronger than positivity and evenness: the
source is an arithmetic superposition of one profile transported by the
multiplicative monoid of positive integers.

## Exact prime recursion

For a prime (p), split the source into indices divisible and not divisible
by (p). The divisible sector is

\[
\sum_{m\ge1}\phi_{pm}(u)
=p^{-1/2}\sum_{m\ge1}\phi_m(u+\log p)
=p^{-1/2}\Phi(u+\log p).
\]

Consequently

\[
\boxed{
\Phi(u)=\Phi_{p\nmid}(u)+p^{-1/2}\Phi(u+\log p),
\qquad
\Phi_{p\nmid}(u)=\sum_{p\nmid n}\phi_n(u)>0.
}
\]

This identity holds simultaneously for every prime and is compatible with
iterating prime powers. A generic positive even source—and in particular the
hostile two-atom source—does not carry this labelled all-prime recursion.

## The signed Clark fold acquires a positive repair

For the normalized Clark denominator put

\[
h_a(u)=(1-au)\Phi(u),\qquad a>0,
\]

and let (ell=\log p). Multiplying the prime recursion by (1-au), while
comparing with the translated signed density, gives

\[
\boxed{
h_a(u)-p^{-1/2}h_a(u+\ell)
=(1-au)\Phi_{p\nmid}(u)
+a\ell\,p^{-1/2}\Phi(u+\ell).
}
\]

The last term is strictly positive on the positive chamber. It is not fitted:
its coefficient is forced by the displacement of the fold under the prime
translation. Thus modular scale recursion produces exactly the architecture
missing from the generic one-fold argument:

\[
\text{translated signed fold}
+\text{primitive-prime signed remainder}
+\text{positive displacement repair}.
\]

The repair does not yet prove that the Fourier--Laplace transform of (h_a)
is upper-half-plane stable. The primitive-prime remainder still changes sign
at (u=1/a), and the faithful bilateral source requires the modular sewing at
(u=0). But the identity is the first candidate mechanism that is both
source-specific and capable of distinguishing the theta density from the
two-atom counterexample.

## The repair is not pointwise dominant

The positive displacement term cannot repair the signed density by a local
inequality. As (u\to+\infty), the primitive sector is dominated by (n=1):

\[
\Phi_{p\nmid}(u)\sim\phi_1(u).
\]

The shifted term is the sector of labels divisible by (p), whose first
contribution is (phi_p(u)). Their ratio contains

\[
\exp\!\left[-\pi(p^2-1)e^{2u}\right]
\]

times only an elementary exponential factor. Hence

\[
\frac{a\log(p)\,p^{-1/2}\Phi(u+\log p)}
{(au-1)\Phi_{p\nmid}(u)}\longrightarrow0.
\]

In the negative side of the fold, the source-forced positive repair is
asymptotically much smaller than the negative primitive remainder. Therefore
the prime recursion does **not** imply pointwise positivity of the Clark
density or of a local energy integrand. Any successful repair must occur only
after transform and sewing.

## Transform recursion and the arithmetic half-line

Let

\[
F_a(z)=\int_0^\infty h_a(u)e^{izu}\,du,
\qquad
B_{a,p}(z)=\int_0^{\log p}h_a(u)e^{izu}\,du,
\]

and denote the transform of the right-hand side of the prime recursion by
(R_{a,p}(z)). Changing variables in the shifted integral gives

\[
\int_0^\infty h_a(u+\log p)e^{izu}\,du
=p^{-iz}\bigl(F_a(z)-B_{a,p}(z)\bigr).
\]

Therefore

\[
\boxed{
\left(1-p^{-1/2-iz}\right)F_a(z)
=R_{a,p}(z)-p^{-1/2-iz}B_{a,p}(z).
}
\]

The prime multiplier vanishes exactly at

\[
\boxed{
z=\frac{2\pi k}{\log p}+\frac i2,
\qquad k\in\mathbb Z.
}
\]

The height (1/2) is forced by the translate weight (n^{-1/2}). It is not
inserted from a zero list. In the centered variable
(s=1/2+iz), this upper (z)-line maps to the outer boundary
(\operatorname{Re}s=0) of the critical strip, not to the RH line itself.

Since (F_a) is entire under the superexponential source decay, every
apparent prime-multiplier pole is cancelled by the finite chamber term and
the primitive-sector transform:

\[
R_{a,p}(z)=p^{-1/2-iz}B_{a,p}(z)
\quad\text{when}\quad p^{-1/2-iz}=1.
\]

This cancellation is an exact finite sewing constraint. Dropping
(B_{a,p}) would manufacture false arithmetic singularities. The promising
object is therefore not the Euler-like multiplier alone, but the triple

\[
\boxed{
\text{prime multiplier}
+\text{primitive-label transform}
+\text{finite modular sewing current}.
}
\]

The next question is whether these cancellation identities for all primes
assemble into a positive Hardy-space boundary form. A single-prime recursion
cannot suffice: its multiplier has zeros inside the upper (z)-half-plane
and is rescued only by the source-defined finite current.

## Iterated prime-power filtration

Iterating the recursion yields

\[
\Phi(u)=\sum_{j=0}^{J-1}p^{-j/2}
\Phi_{p\nmid}(u+j\ell)
+p^{-J/2}\Phi(u+J\ell).
\]

Superexponential decay removes the terminal term as (J\to\infty). Hence

\[
h_a(u)=\sum_{j\ge0}p^{-j/2}
\left[
h_{a,p\nmid}(u+j\ell)
+aj\ell\,\Phi_{p\nmid}(u+j\ell)
\right],
\]

where

\[
h_{a,p\nmid}(t)=(1-at)\Phi_{p\nmid}(t).
\]

Every depth (j>0) therefore carries a forced positive displacement term.
This is a filtration by (p)-adic valuation on the source labels, not a
chosen analytic decomposition.

## Sharp next test

The live question is whether the prime-recursive identity becomes a positive
Hardy-space or de Branges energy after bilateral modular sewing. A valid
construction must:

1. retain the labels (p\nmid n) and (v_p(n)=j);
2. include the (u=0) sewing current rather than extending the positive
   chamber by hand;
3. reproduce exactly the Clark denominator
   \(E_a(z)=\frac12\int_{\mathbb R}h_a(u)e^{izu}du\);
4. turn the displacement terms into a positive bulk or boundary form; and
5. leave no untyped primitive-prime signed remainder.

The sharp falsifier is a source-recursive positive even density satisfying
the same prime-translation identities and sewing law whose one-fold transform
still has an upper-half-plane zero. Until that class is excluded—or an exact
positive energy is derived—the recursion is a promising mechanism, not an RH
proof.

## Interpretation

The one-fold geometry identifies the defect but does not repair it. The
modular arithmetic labels add a canonical hierarchy of displaced copies, and
the displacement of the fold itself generates positive correction terms.
This is the closest current analogue of the prime-two pattern:

\[
\boxed{
\text{source-labelled defect}
+\text{scale transport}
\longrightarrow
\text{forced repair current}.
}
\]
