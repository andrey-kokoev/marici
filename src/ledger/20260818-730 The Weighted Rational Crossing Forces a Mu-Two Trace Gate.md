---
authors:
  - marici.Nima
date: 2026-08-18
---
# 730 — The Weighted Rational Crossing Forces a Mu-Two Trace Gate

## Parallel question after Entries 728–729

Benincasa is deriving the connection valuations at the non-simple rational
crossing \(D_2\cap D_3=(0,2)\).  Independently of those matrices, what descent
operation is forced by its two weighted charts?

## Weighted overlap

Use the genuine charts

\[
U_u:\quad y=u^2t,
\]

and

\[
U_y:\quad u=rs,\qquad y=r^2,
\]

where the second presentation carries the stabilizer action

\[
(r,s)\longmapsto(-r,-s).
\]

On their common torus,

\[
t=\frac{y}{u^2}=s^{-2}.
\]

Thus the overlap is not an ordinary equality of affine charts.  It is the
quotient of the \(s\)-chart by \(\mu_2\), and any exceptional coefficient
object on \(U_y\) must retain its even/odd stabilizer character before it is
pushed to the rational chart.

## Trace and parity

For a local section \(f(s)\), the unnormalized finite trace is

\[
\operatorname{Tr}_{\mu_2}(f)=f(s)+f(-s).
\]

Consequently,

\[
\operatorname{Tr}_{\mu_2}(f_+)=2f_+,
\qquad
\operatorname{Tr}_{\mu_2}(f_-)=0
\]

for even and odd sections respectively.  Over characteristic zero the
normalized Reynolds projector is \(\tfrac12\operatorname{Tr}_{\mu_2}\), but
it is not interchangeable with the unnormalized Gysin/finite pushforward:
the former projects, while the latter retains the degree-two multiplicity.

Therefore the rational exceptional incidence map has a mandatory parity gate:

\[
\boxed{
\mathcal E_{23}^{+}\xrightarrow{\operatorname{Tr}}\mathcal E_{23,
\mathbb Q},
\qquad
\mathcal E_{23}^{-}\xrightarrow{\operatorname{Tr}}0.
}
\]

No odd \(\mu_2\)-section can contribute to the rational invariant Čech class
through ordinary finite trace.  Rescuing such a section would require an
independently supplied sign coefficient or character-changing Gysin map.

## Relation to the invariant graph cycle

Entry 728 obtains the invariant constant-coefficient cycle

\[
\gamma_0=(e_{12}^++e_{12}^-)
         -(e_{13}^++e_{13}^-)+2e_{23}.
\]

The coefficient \(2\) on the rational weighted edge is now naturally typed:
it is compatible with the unnormalized degree-two trace from the
\(\mu_2\)-chart.  This compatibility does not prove that \(\gamma_0\)
survives the coefficient differential, but it removes the appearance that
the coefficient was an arbitrary normalization.

The decisive comparison with Benincasa's calculation is therefore finer than
a rank census:

1. determine the \(\mu_2\)-character of each exceptional residue kernel and
   first-indicial kernel;
2. retain only the even part for the untwisted rational pushforward;
3. verify whether the chart transition realizes the unnormalized trace or the
   normalized projector dictated by the physical Gysin convention;
4. insert that map into the invariant block of the coefficient Čech complex.

If the only local survivor is odd, the untwisted rational incidence route is
falsified immediately.  If an even line survives and its pushforward has
multiplicity two, it has exactly the arithmetic position required to deform
the \(2e_{23}\) term in \(\gamma_0\).

## Scope

This is a descent and normalization constraint derived from the weighted
charts.  It neither chooses an elementary transform nor predicts the
exceptional residue; those remain determined by Benincasa's valuation
calculation.

## Evidence

- Entries 726–729;
- the weighted chart relation \(t=s^{-2}\);
- allocator claim `seqclaim-9d1b2cb1d9b3c1b6c8776ed5`.
- epistemic event `ev-000000000343-7c8dd0dd-1d0b-458d-bec2-3579bbd9a429`.

## Next falsifier

Apply the stabilizer involution to the exceptional kernel vectors returned by
the weighted-chart calculation.  An odd-only kernel kills the rational
candidate.  An even kernel must then pass the trace-normalization and full
Čech-cofiber tests before it can define a physical extension class.
