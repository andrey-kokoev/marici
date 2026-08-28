# The Odd Seam-Jet Tower Is Global Reflection in Germ Form

## Statement

Let \(R\) be real analytic on a connected reflection-invariant domain containing
the seam \(u=0\). Then the following are equivalent:

1. every odd seam derivative vanishes,
   \[
   R^{(2j+1)}(0)=0
   \qquad
   (j\geq0);
   \]
2. the analytic germ of \(R\) at the seam is even;
3. \(R\) obeys global reflection symmetry,
   \[
   R(u)=R(-u)
   \]
   throughout that connected domain.

## Proof

The Taylor series at zero is

\[
R(u)=\sum_{k\geq0}\frac{R^{(k)}(0)}{k!}u^k.
\]

All odd coefficients vanish exactly when this series is unchanged by
\(u\mapsto-u\). Hence \(R(u)=R(-u)\) near zero. Both sides are analytic on the
connected common domain, so the identity theorem extends the equality
globally. The reverse implications are immediate.

## Consequence for seam repair

The boundary hierarchy

\[
R'(0),\ R'''(0),\ R^{(5)}(0),\ldots
\]

is not an accidental infinite list. In the analytic source category it is a
complete coordinate system for the failure of reciprocal reflection.

Therefore a finite primitive repair can remove only finitely many asymptotic
boundary channels. Closing the entire tower is equivalent to installing a
global reflection law. For the theta source, that law is precisely what
modular completion supplies.

This retypes the earlier perturbative failure:

- the dominant primitive controls the positive chamber pointwise;
- the small tail carries the missing reflection coherence;
- every unmatched odd derivative is a finite-resolution witness of that same
  global defect.

The tail is small as a value but not small as coherence data.

## What this does not prove

Evenness alone does not imply the RH orientation. Hostile even sources remain
possible. The theorem explains why no finite seam-jet repair can replace
modular sewing; it does not show that modular sewing confines zeros.

## Falsifier

The claim fails outside the analytic category. A smooth function can be flat
at the seam, have every derivative there equal to zero, and still fail global
reflection symmetry. Any use of the theorem must therefore establish
analyticity on a connected reflection-invariant domain before promoting germ
data to global coherence.
