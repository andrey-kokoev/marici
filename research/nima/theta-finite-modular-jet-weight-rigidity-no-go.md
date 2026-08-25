# Finite modular jets do not orient positive square-mode weights

## Question

Could the extra theta-specific ingredient be reduced to finitely many
reciprocal-seam conditions at \(t=1\)?

For positive square-mode weights \(a_m\), define on the completed chart

\[
\Phi_a(u)=\sum_{m\ge1}a_m\,b(e^{2u},m^2),
\qquad u\ge0,
\]

with

\[
b(t,x)=t^{5/4}x(2\pi tx-3)e^{-\pi tx}.
\]

Even modular sewing across \(u=0\) requires all odd derivatives to vanish.
The standard theta weights satisfy the full infinite system. No finite
subsystem can uniquely select or orient them.

## Finite-kernel theorem

Fix any finite list of seam observables, for example

\[
\Phi_a(0),\quad
\Phi_a'(0),\quad
\Phi_a^{(3)}(0),\ldots,\Phi_a^{(2r-1)}(0).
\]

Choose \(N\) distinct square modes with \(N\) larger than the number of
observables. Their values form a finite matrix \(M\). There exists
\(h\ne0\) with

\[
Mh=0.
\]

Starting from any strictly positive weight vector \(a\), sufficiently small
\(\varepsilon\ne0\) gives

\[
a^\pm=a\pm\varepsilon h>0
\]

and

\[
Ma^+=Ma^-.
\]

Thus the two positive labelled sources have identical checked modular jets
and normalization but different prime/winding weights.

The all-order spectral sign-regularity theorem still holds for both sources:
it is a property of the labelled kernel \(b(t,m^2)\), not of the particular
positive coefficient vector.

## Exact derivative recurrence

Put \(q=\pi x t\). Apart from the positive factor \(x\),

\[
b(t,x)=t^{5/4}e^{-q}P_0(q),
\qquad P_0(q)=2q-3.
\]

Since \(t=e^{2u}\),

\[
\frac d{du}=2\left(t\frac d{dt}\right),
\]

and the derivative polynomials satisfy

\[
\boxed{
P_{k+1}(q)
=2\left[\left(\frac54-q\right)P_k(q)+qP_k'(q)\right].
}
\]

Hence every finite modular-jet constraint is an explicit linear equation in
the weights.

## Finite witness

The checker uses five modes \(m=1,\ldots,5\) and the three observables

\[
\Phi(0),\qquad\Phi'(0),\qquad\Phi^{(3)}(0).
\]

High-precision elimination finds a two-dimensional nullspace. It selects one
nonzero vector \(h\), rescales it so \(\max|h_m|=1\), and forms

\[
a_m^\pm=1\pm\frac14h_m.
\]

Every weight remains at least \(3/4\), while the three seam observables agree
to the declared high-precision tolerance. The two sources differ in their
label weights and therefore away from the checked finite seam data.

## Meaning

Finite modular jets are provenance checks, not an orientation mechanism.
They can falsify a proposed source but cannot uniquely determine the
positive coefficient sequence.

Exact analytic modularity is an infinite coherence law and may be rigid in a
specified automorphic class. Even if it uniquely selects the standard theta
weights, that establishes constructibility, not positivity of the
denominator-free de Branges kernel. The normal-current inequality remains
an additional global interaction law.

## Finite falsifier schema

Given any claimed finite seam certificate:

1. list its linear jet observables;
2. choose more labelled modes than observables;
3. compute a nonzero null vector;
4. perturb a strictly positive weight vector in both directions;
5. verify equal certificate values and unequal labelled weights.

If this succeeds, the certificate cannot carry global orientation authority.

