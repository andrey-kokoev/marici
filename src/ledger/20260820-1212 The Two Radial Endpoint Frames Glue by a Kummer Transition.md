---
title: "The Two Radial Endpoint Frames Glue by a Kummer Transition"
date: 2026-08-20
entry: 1212
status: active-supported-local-system
sector: cosmology
---

# 1212 — The Two Radial Endpoint Frames Glue by a Kummer Transition

Sequence claim: `seqclaim-4c903dfb6cf8865b22965c6b`.

## Local frames

Entry 1211 supplies the two source-normalized transverse period frames

\[
p_0=\frac{2\pi i}{\sqrt{K_4}},
\qquad
p_\infty=\frac{2\pi i}{\sqrt{K_0}},
\]

up to one ordered-orientation sign.

On their common generic coefficient locus,

\[
\boxed{
p_0
=
\sqrt{\frac{K_0}{K_4}}\,p_\infty.
}
\]

Hence the squared transition is rational and source-fixed:

\[
\boxed{g_{0\infty}^2=K_0/K_4.}
\]

## Kummer character

The resulting rank-one coefficient local system has divisor character

\[
[K_0=0]-[K_4=0]pmod2.
\]

Its local inertias are

\[
T_{K_0}=T_{K_4}=-1,
\]

while a loop enclosing both endpoint divisors has character \(+1\).

Changing the common ordered orientation rescales both frames by the same
sign. It does not alter the transition line or either inertia character.

## Consequence

The finite and infinity odd costalks from Entry 1210 are not two unrelated
rank-one objects. They are the endpoint presentations of one Kummer
coefficient line over the radial collision family.

\[
\boxed{
\text{one existing radial/endpoint carrier}
+
\text{one canonically glued Kummer coefficient line}.
}
\]

No additional incidence cell is required.

## Remaining physical boundary

The coefficient line and its gluing are now defined, but its pairing with the
global Bunch--Davies relative cycle remains uncomputed. Physical visibility
must not be inferred from nonzero local periods alone.

## Next falsifier

Pull the source five-site Cayley--Menger integration current to the radial
collision family and compute its boundary in the two endpoint charts. Test
whether the resulting chain map lands in this Kummer line and intertwines its
two \(-1\) inertia operators.

## Artifact

- `research/benincasa/marici-gm/src/bin/five_site_endpoint_kummer_transition.rs`
- `research/benincasa/results/five-site-endpoint-kummer-transition.json`
