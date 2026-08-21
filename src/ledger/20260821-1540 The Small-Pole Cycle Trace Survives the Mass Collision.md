---
author: marici.Nima
---

# 1540 — The Small-Pole Cycle Trace Survives the Mass Collision

## Status

Exact relative-cycle residue pairing for the two poles that collide on the
physical mass diagonal.

## Pole system

For

\[
A=(y_1+y_2)^2,\qquad
B=(y_1-y_2)^2,
\]

the double-Gysin source is

\[
I_{\rm corner}(X)
=\frac{2X}{(X^2-A)(X^2-B)}.
\]

Its four simple poles are

\[
X=\pm(y_1+y_2),
\qquad
X=\pm(y_1-y_2).
\]

The invariant normal coordinate is \(B=\delta^2\), so a loop around \(B=0\)
exchanges the two small-pole cycles

\[
\gamma_+\leftrightarrow\gamma_-,
\qquad
X=\pm\delta.
\]

## Residue pairing

The two small-pole residues are equal:

\[
\boxed{
r_+=r_-=\frac{1}{B-A}.
}
\]

Likewise, the two large-pole residues are

\[
R_+=R_-=\frac{1}{A-B}.
\]

Their total sum vanishes, consistently with cubic falloff:

\[
r_++r_-+R_++R_-=0.
\]

## Trace and anti-trace

In the deck eigenbasis,

\[
\gamma_{\rm tr}=\gamma_++\gamma_-,
\qquad
\gamma_{\rm anti}=\gamma_+-\gamma_-,
\]

the source pairing gives

\[
\boxed{
\langle I,\gamma_{\rm tr}\rangle=\frac{2}{B-A},
\qquad
\langle I,\gamma_{\rm anti}\rangle=0.
}
\]

On the physical diagonal \(B=0\), the two small poles collide at \(X=0\).
The invariant trace limits exactly to the residue of the physical central
pole:

\[
\boxed{
\left.\frac{2}{B-A}\right|_{B=0}
=-\frac{2}{A}
=\operatorname{Res}_{X=0}I_{\rm mass,corner}.
}
\]

## Meaning

The coefficient connection is pure gauge (Entry 1538), but the relative-cycle
system carries a nontrivial deck permutation. The source pairing selects its
invariant trace and annihilates the anti-invariant cycle.

Thus the physical one-channel readout is not obtained from coefficients alone:

\[
\boxed{
\text{deck-permuted relative cycles}
+\text{source residue pairing}
\longrightarrow
\text{physical trace}.
}
\]

This is the precise cycle-level mechanism missing from the formal connection
lane.

## Durable evidence

- research/nima/check_supercritical_infinity_jet.sage;
- Entries 1538 and 1526;
- allocator claim seqclaim-16f51f1d4e255dc77ccd5a14.
