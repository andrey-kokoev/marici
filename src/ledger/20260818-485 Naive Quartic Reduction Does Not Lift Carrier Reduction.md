---
id: 485
authors:
  - marici.Benincasa
date: 2026-08-18
---
# Naive Quartic Reduction Does Not Lift Carrier Reduction

## Record

Status: first-order obstruction to lifting Entry 466 by coefficientwise
reduction modulo the full Cayley--Menger quartic.

Entry 466 constructs the soft-fiber carrier reduction because every frozen
exact image is divisible by (a^4). The simplest proposed lift would replace
(a^4) by the full monic relation

[
K=a^4+u,a^2(1-b^2)
qquad (mod,u^2)
]

and reduce every exact-form representative coefficientwise modulo (K).

## Finite falsifier

Use the source-defined sector

[
(s_a,s_b)=(1,1),
qquad
f=1,
]

with

[
L_1=b+1-u,
qquad
L_2^-=a-rac u2.
]

Its (q)-exact operator is

[
q
=
-L_1K
-rac32L_1L_2^-K_a.
]

Modulo (K), the first term vanishes. To first order,

[
K_a=4a^3+2ua(1-b^2).
]

Using the quartic relation

[
a^4=-u,a^2(1-b^2)
]

gives

[
oxed{
q
equiv
3u(b+1)
left[
a^2(1-b^2)+a^3
ight]
pmod{K,u^2}.
}
]

This polynomial is generically nonzero. Its six monomials all have
(a)-degree two or three, so no residual factor (a^4) remains.

Therefore coefficientwise reduction does not send the complete exact image
to zero:

[
oxed{
C_{m full}^{m Rees}longrightarrowmathbb Q[u,a,b]/(K)
}
]

is not a chain map in this naive form.

## Interpretation

The obstruction is source-derived and occurs before any endpoint issue.
Entries 483--484 close the two boundary components of the odd-tail
comparison, but they do not supply the interior homotopy required here.

This is exactly the distinction anticipated in Entry 447: the quartic module
is flat, but coefficientwise (partial_u) does not descend. A lift of
carrier reduction must be made in the relative de Rham complex and include a
Gauss--Manin/Koszul correction for the (K_a) and (K_b) terms.

No new carrier component is indicated. The failed object is a naive
coefficient map, not the shared-carrier hypothesis.

## Classification

- quartic carrier family: existing and flat;
- naive coefficientwise reduction: falsified as a chain map;
- obstruction class: interior relative-de-Rham coefficient data;
- endpoint support: already closed by Entries 483--484;
- new carrier datum: none.

## Next falsifier

Construct the canonical conormal/Koszul homotopy for the monic quartic
relation and apply it to all exact sectors. Test whether it cancels the
displayed obstruction and makes carrier reduction a chain map through first
order in (u). If a residual survives, compute its filtered rank and
provenance before considering higher Rees order.

## Evidence

- `research/benincasa/marici-gm/src/bin/soft_axis_naive_carrier_lift.rs`;
- Entries 447, 466, and 483--484.
