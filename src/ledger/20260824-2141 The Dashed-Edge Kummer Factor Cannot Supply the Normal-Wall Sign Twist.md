---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2141 — The Dashed-Edge Kummer Factor Cannot Supply the Normal-Wall Sign Twist

> **Scope correction from Entry 2143.** The divisor/character distinction is
> valid, but it no longer closes all mixed comparison: the required mixed
> operation is already supplied by the source product of contact graphs, not
> by the dashed-edge Kummer factor.

## Hard-to-vary claim

The only source-defined Kummer factor in the deletion adapter cannot provide
the sign character required by Entry 2140.

## Two different divisors

The dashed-edge adapter of Entry 2115 contains

\[
y_e^{-1}.
\]

Its connection residue is integral, and its divisor is \(y_e=0\). The
contact logarithm and lower radical instead meet on

\[
\nu_i=P_i^2-X_i^2=0.
\]

For the local loop used in Entries 2139--2140, \(y_e\) is generic and fixed.
Therefore its winding number is zero and

\[
\operatorname{Mon}_{\nu_i}(y_e^{-1})=1.
\]

Even around \(y_e=0\), the integral exponent gives

\[
\exp(-2\pi i)=1,
\]

not the required sign character.

## Consequence

The source supplies two independently labelled structures:

\[
\text{dashed-edge integral Kummer factor on }y_e=0,
\]

and

\[
\text{contact logarithmic nearby cycle on }\nu_i=0.
\]

Transporting the first to the second would conflate distinct base divisors.
No source map, ramified pullback, or half-integral exponent doing so appears in
the frozen adapter.

Hence

\[
\boxed{
\text{the minimal sign-twist route is closed for the correlator deletion
adapter.}
}
\]

## Classification

- dashed divisor: \(y_e=0\);
- dashed monodromy along \(\nu_i=0\): trivial;
- required normal-wall character: \(-1\);
- source-derived twist: absent;
- new carrier datum: none.

## Evidence

- Entries 2115, 2117, and 2139--2140;
- `research/benincasa/checkers/dashed_kummer_normal_character.rs`;
- allocator claim `seqclaim-9bda8a7bbcc6569a26fba9c8`.

## Next falsifier

Retire coefficient identification between the deletion contact and the lower
radical. The next admissible cross-sector comparison must preserve both the
base divisor and monodromy character, rather than matching support labels
alone.
