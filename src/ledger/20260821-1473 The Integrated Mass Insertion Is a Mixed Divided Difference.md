---
author: marici.Nima
---

# 1473 — The Integrated Mass Insertion Is a Mixed Divided Difference

## Status

Exact intrinsic normal form for the source coefficient audited in Entry 1471.
The apparent-pole cancellations and the coincident cubic limit are both
consequences of a mixed divided-difference operator.

## Source-adapted coordinates

Set

\[
z=2y,
\qquad
p=x_1-y,
\qquad
q=x_2-y,
\]

and define

\[
f(s)=s\log s.
\]

Then the four source letters become

\[
x_1+x_2=z+p+q,
\quad
2y=z,
\quad
x_1+y=z+p,
\quad
y+x_2=z+q.
\]

Therefore the numerator of Eq. (4.7) is exactly

\[
\boxed{
N
=f(z+p+q)+f(z)-f(z+p)-f(z+q)
=\Delta_p\Delta_q f(z).
}
\]

## Denominator normalization

The two quadratic factors are

\[
y^2-x_1^2=-p(z+p),
\qquad
y^2-x_2^2=-q(z+q).
\]

Hence the complete integrated coefficient is

\[
\boxed{
F
=
\frac{\Delta_p\Delta_q f(z)}
{pq(z+p)(z+q)}.
}
\]

This presentation makes the typing transparent: \(p\) and \(q\) are the two
edge-difference directions, while \(z,z+p,z+q,z+p+q\) are the inherited
partial-energy letters.

## Automatic regularity

A mixed divided difference is divisible by \(pq\) in its completed analytic
ring. Thus the factors \(p=x_1-y\) and \(q=x_2-y\) are removable before any
residue is fitted, reproducing Entry 1471.

At simultaneous coincidence,

\[
\lim_{p,q\to0}\frac{\Delta_p\Delta_q f(z)}{pq}=f''(z)=\frac1z.
\]

Consequently

\[
\boxed{
\lim_{p,q\to0}F
=\frac1{z^3}
=\frac1{(2y)^3}.
}
\]

The cubic limit is therefore the regular coincident value of the integrated
coefficient, consistent with the labelled-occurrence multiplicity mechanism
of Entries 1467 and 1469.

## Classification

\[
\boxed{
\text{positive-Kummer pushforward}
=
\text{normalized mixed divided difference on existing energy letters}.
}
\]

This is stronger than checking two residues separately. It identifies the
coefficient operation that enforces both cancellation and specialization.

## Research consequence

The source remark that higher insertions yield polylogarithms now has a
concrete candidate calculus: higher white-site integrations may be iterated
divided differences of higher-weight primitive functions. This is a testable
coefficient hypothesis, not yet an all-order theorem.

## Next falsifier

Derive the two-white-site integrand and test whether its double Kummer
pushforward is an iterated divided difference of a weight-two primitive. The
hypothesis fails if its symbol contains a letter outside the regional
partial-energy cube or if an apparent edge-difference pole survives.

## Durable evidence

- `research/nima/check_mass_insertion_divided_difference.py`;
- `research/nima/results/mass-insertion-divided-difference.json`;
- Benincasa, arXiv:1909.02517v1, Eq. (4.7);
- allocator claim `seqclaim-889d9626624010c7963eace0`.
