# Autocorrelation polarization is RH-equivalent and cannot select a spectral factor

## Exact equivalence

The continuous positive-real theorem proves that at every zero of the completed
transform,

\[
\operatorname{sign}\operatorname{Re}J(z)
=-operatorname{sign}\operatorname{Re}z.
\]

Consequently,

\[
\text{all zeros lie on the seam}
\quad\Longleftrightarrow\quad
\operatorname{Re}J(z)=0
\text{ at every zero}.
\]

Thus “zero-state polarization” is not yet an independently weaker lemma. In
the absence of a separate source constructor forcing it, it is RH rewritten in
current coordinates.

## The current is globally scalar-derived

The half-form is reconstructed from the boundary modulus:

\[
2\operatorname{Re}A(it)=|X(it)|^2.
\]

The Herglotz/Poisson reconstruction determines `A` up to the fixed imaginary
normalization, and then `J=A(z)-A(-z)`. Therefore this current is pointwise
transverse to the ideal `(X)` at a zero but globally carries no information
beyond the scalar boundary modulus.

This distinction is essential:

- pointwise nondivisibility makes `J` a useful radial detector;
- global scalar reconstructibility prevents `J` from selecting the physical
  spectral factor.

## Smallest spectral-factor ambiguity

Take

\[
P(w)=1+2w,
\qquad
P^\#(w)=2+w.
\]

On the unit circle,

\[
|P(w)|^2=|P^\#(w)|^2=5+2(w+w^{-1}).
\]

Both have the same autocorrelation coefficients,

\[
C_0=5,
\qquad
C_1=2,
\]

and therefore the same half-form and oriented current,

\[
A(w)=\frac52+2w,
\qquad
J(w)=2(w-w^{-1}).
\]

Yet their zeros are

\[
w=-\frac12,
\qquad
w=-2.
\]

One lies inside and one outside the unit circle. The common current evaluates
with opposite normal signs at those reciprocal zeros, but the boundary
autocorrelation data do not choose which factor is the source readout.

More generally, reversing any finite real coefficient packet preserves every
autocorrelation coefficient while reciprocating its nonzero divisor.

## Meaning

Before reciprocal completion, a missing phase-bearing port must distinguish a
factor from its reverse. Theta arithmetic may supply that information through:

- labelled source order;
- an oriented endpoint or seam incidence;
- a noncommutative primal-dual comparison;
- or another constructor distinguishing a factor from its reciprocal reverse.

Any proposed proof using only `|X|^2`, autocorrelation, its positive-real
half-form, or the derived current cannot supply that selection. It accepts both
members of the smallest hostile pair.

## Revised programme

The current theorem remains valuable: once an independently authorized factor
is selected, it reads radial displacement perfectly. But the next task is no
longer “prove current positivity” or “prove current polarization.” It is:

> Construct the theta-labelled phase port that distinguishes the completed
> factor from its reciprocal spectral-factor mate, and prove that this port
> is compatible with modular sewing.

That is a necessary pre-completion distinction, but it is not sufficient for
RH. A palindromic positive factor can equal its reverse and still have off-unit
zeros. Ledger 3617 records the corrected post-completion target: interval
stability of the reciprocal quotient.
