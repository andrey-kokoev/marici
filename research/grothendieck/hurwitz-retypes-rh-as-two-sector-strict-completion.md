# Hurwitz Retypes RH as Two-Sector Strict Completion

## Finite sections are units in the open strip

Let \(X\) be a finite set of primes and define

\[
C_X(s)
=
\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)
\prod_{p\in X}(1-p^{-s})^{-1}.
\]

On the open critical strip \(0<\Re s<1\), every factor is holomorphic and
nonzero. Thus each finite completed Euler section \(C_X\) is a unit there.

Split the strip into its two reciprocal sectors:

\[
D_+=\{s:1/2<\Re s<1\},
\qquad
D_-=\{s:0<\Re s<1/2\}.
\]

## Strict-completion theorem

Suppose that for each sector there are holomorphic nowhere-zero
renormalization units \(r_X^\pm\) such that

\[
r_X^\pm C_X\longrightarrow\xi
\]

locally uniformly on \(D_\pm\). Then \(\xi\) has no zero in either open
sector.

Indeed, every \(r_X^\pm C_X\) is holomorphic and nowhere zero. Hurwitz's
theorem says that a locally uniform limit of such functions is either
nowhere zero or identically zero on each connected domain. The completed
section \(\xi\) is not identically zero, so it is nowhere zero on both
\(D_+\) and \(D_-\).

Together with the standard localization of nontrivial zeros to the critical
strip, this proves RH.

## Exact converse at the level of existence

If RH is assumed, then on each open sector

\[
r_X^\pm=\frac{\xi}{C_X}
\]

is itself a holomorphic unit and gives exact equality
\(r_X^\pm C_X=\xi\). Consequently:

> RH is equivalent to the existence of sectorwise unit renormalizations of
> the finite completed Euler sections that converge locally uniformly to the
> completed theta section.

This equivalence is not yet an explanation, because the displayed converse
constructs the renormalization backward from \(\xi\). The Deutschian target
is to derive \(r_X^\pm\) from the primitive, square, connected-tail, and
archimedean source data without using the completed divisor.

## Meaning of a zero

An isolated zero cannot be created by an ordinary locally uniform completion
of finite nonvanishing sections. If a completed zero occurs, at least one of
the following must happen near it:

1. the scalar convergence is not locally uniform;
2. a proposed renormalization ceases to be a unit;
3. an operator inverse or contracting partner escapes the completed topology;
4. the determinant functor becomes discontinuous;
5. a domain, quotient, or boundary operation loses information.

Thus a zero is precisely a failure of strict invertible descent from the
finite source system. This gives a rigorous form to the proposed loss-of-
meaning interpretation.

## Why two sectors are real

Known critical-line zeros do not obstruct locally uniform unit completion
inside either \(D_+\) or \(D_-\), because the seam is their common boundary,
not an interior point. A single completion across the entire strip cannot be
a locally uniform limit of units, but two sectorwise completions can remain
strict while their comparison becomes singular at the interface.

The two half-planes are therefore not merely shadows drawn around an already
known zero set. They are the maximal reciprocal chambers on which finite
determinant invertibility could survive ordinary completion.

## Sharp falsifier

For any proposed source-derived renormalization, find a compact set
\(K\subset D_+\) or \(K\subset D_-\) on which one of these occurs:

- \(r_X\) has a zero or pole;
- \(r_XC_X\) is not a normal family;
- two prime exhaustions have different subsequential limits;
- convergence holds only after inserting \(\xi/C_X\);
- or the limit fails to equal the theta section.

Any such witness rejects that strict-completion construction. Conversely, a
source-derived locally uniform unit completion on both sectors would prove
RH immediately by Hurwitz.

## Research consequence

The remaining programme should no longer ask vaguely for divisor
orientation. It should construct the two sectorwise renormalization units and
prove normal-family compactness. Primitive and square currents matter as
boundary coordinates of those units, while the seam is allowed to remain a
singular comparison interface.

