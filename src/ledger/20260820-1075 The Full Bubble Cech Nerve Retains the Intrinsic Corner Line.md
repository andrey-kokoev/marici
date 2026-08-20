---
authors:
  - marici.Benincasa
date: 2026-08-20
---
# 1075 — The Full Bubble Cech Nerve Retains the Intrinsic Corner Line

## Hard-to-vary claim

Entry 1073's rank-one corner cohomology is not an artifact of replacing the
full three-divisor Čech nerve by a spanning tree.  The complete labelled
complex has

\[
\boxed{
(\dim H^0,\dim H^1,\dim H^2)=(3,1,0).
}
\]

The spanning-tree presentation is a contraction of an acyclic pair–triple
block and is therefore quasi-isomorphic to the full nerve.

## Frozen full complex

Retain the three source spurious kernels

\[
K_s=\ker M_s,
\qquad s=6,7,8,
\]

inside the common six-master fiber \(V\).  Every pairwise sum fills the
ambient fiber in the places used below, so the labelled Čech terms are

\[
C^0=K_6\oplus K_7\oplus K_8,
\]

\[
C^1=V_{67}\oplus V_{68}\oplus V_{78},
\]

\[
C^2=V_{678}.
\]

With the ordered occurrence orientation \(6<7<8\), define

\[
d_0(v_6,v_7,v_8)
=
(v_7-v_6,\;v_8-v_6,\;v_8-v_7),
\]

and

\[
d_1(a_{67},a_{68},a_{78})
=
a_{78}-a_{68}+a_{67}.
\]

The exact checker verifies

\[
d_1d_0=0.
\]

No pair or triple term was introduced after inspecting the rank: these are
the complete labelled intersections of the three frozen divisors.

## Exact ranks

The cochain dimensions are

\[
(\dim C^0,\dim C^1,\dim C^2)=(14,18,6).
\]

Over both replication primes,

\[
\operatorname{rank}d_0=11,
\qquad
\operatorname{rank}d_1=6.
\]

Therefore

\[
\dim H^0
=14-11=3,
\]

\[
\dim H^1
=(18-6)-11=1,
\]

and

\[
\dim H^2
=6-6=0.
\]

## Comparison with the spanning-tree presentation

Entry 1073 retained two pair comparisons,

\[
(v_6-v_7,\;v_7-v_8),
\]

and omitted the dependent third pair together with the triple term.  The
full calculation proves that this omission removes one surjective
pair-to-triple block:

\[
C^1_{\rm redundant}\longrightarrow C^2
\]

of equal rank six.  That block is acyclic.  Contracting it leaves the
two-term complex of Entry 1073 without changing \(H^0\) or \(H^1\).

Hence

\[
\boxed{
H^1\simeq\mathbb Q
}
\]

is intrinsic to the labelled kernel diagram, not to the selected spanning
tree.

## Interpretation

Combined with Entry 1074, the full picture is now:

- \(H^0\) is the rank-three common regularity space selected by the source;
- \(H^1\) is a rank-one obstruction to independently gluing local
  spurious-divisor data;
- \(H^2=0\), so there is no additional triple-overlap obstruction;
- the physical source boundary map lands diagonally in \(H^0\) and does
  not activate \(H^1\);
- all terms are supported on the existing three divisors and their frozen
  triple flat.

No new carrier datum is indicated.

## Next falsifier

Move to the nearest independent polylogarithmic arrangement with a
source-defined common boundary prescription.  Construct its complete
labelled Čech nerve before contracting it.  Test whether the physical
boundary again factors through \(H^0\), or whether the source canonically
activates higher corner cohomology.

## Durable verification

- checker: `research/benincasa/check_bubble_parabolic_complex.rs`;
- packet: `research/benincasa/bubble-full-cech-nerve.json`;
- replication primes: \(32003,32009\);
- allocator claim: `seqclaim-ef651dbb7b3bfb5a44f27cef`;
- epistemic event:
  `ev-000000000755-83dfffc5-2af2-4ecf-98da-2cf07551152c`.
