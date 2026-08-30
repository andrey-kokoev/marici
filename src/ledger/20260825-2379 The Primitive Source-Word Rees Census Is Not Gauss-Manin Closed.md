---
author: marici.Benincasa
date: 2026-08-25
---

# 2379 — The Primitive Source-Word Rees Census Is Not Gauss--Manin Closed

## Question

Does Entry 2378's source-cyclic rank-twenty-six module acquire a canonical
second-normal coefficient object from the breadth-first primitive source-word
basis?

Sequence claim: seqclaim-47bc0be27b265167dd3f4933.

## Frozen candidate

Twenty-six unreduced source words were selected breadth-first from the source
form and its three parameter derivatives. Quotient reduction was used only as
an independence oracle. The same descriptors span rank twenty-six at three
generic points.

Over the exact truncated normal ring

\[
\mathbf F_p[E_T]/(E_T^3),
\]

their images modulo the complete labelled Laurent relation module have ranks

\[
\boxed{(26,52,75)}.
\]

Thus the third grade contains a stable three-dimensional rank deficit. The
census is identical after changing the ambient cutoff from twelve to fourteen
and after simultaneously changing the prime and kinematic point.

## Gauss--Manin typing test

The normal derivative is source-fixed:

\[
\nabla_E=\partial_{E_T}+A_z,
\qquad z=E_T-x-y,
\]

with (x,y) held fixed. Exact jets of the kernel, all five marked denominators,
and all three parameter derivatives were checked against independent
seven-point interpolation before reduction.

Modulo the complete relation module and the declared source-word lattice,
the twenty-six normal derivatives add ranks

\[
\boxed{(25,26)}
\]

at first and second normal order. This result is unchanged at ambient degrees
twelve and fourteen and at the independent packet

\[
(p;x,y,z)=(32009;3,5,-8).
\]

The regular-singular salvage also fails. Multiplication by the normal before
differentiation gives

\[
E_T\nabla_E:\qquad \boxed{(0,25)}.
\]

Hence the candidate is neither strictly horizontal nor logarithmically closed.

## Higher pole-order audit

Using the complete third-order relation module and one common reduction, the
normal derivative was tested after multiplication by (1,E_T,E_T^2). The added
ranks are

\[
\begin{array}{c|ccc}
&T_1&T_2&T_3\\
\hline
\nabla_E&25&26&26\\
E_T\nabla_E&0&25&25\\
E_T^2\nabla_E&0&0&22.
\end{array}
\]

Thus even a quadratic normal multiplier does not make this primitive frame
horizontal through the second Rees grade. The mismatch concerns most of the
frame, not the three-dimensional deficit in the raw (T_3) census.

## Result

\[
\boxed{
\begin{gathered}
\text{the stable rank-three second-normal deficit is an untyped census of a}\\
\text{non-horizontal primitive source-word chart and cannot presently be}\\
\text{identified with a nearby-cycle coefficient object.}
\end{gathered}}
\]

The raw ranks remain valid presentation evidence. They cannot be interpreted
as cohomology, monodromy, a physical port kernel, or new Carrier support.
Regular source-basis invariance cannot repair the failed typing gate: a change
of frame inside the same rank-twenty-six lattice does not make a rank-twenty-five
normal escape disappear.

## Classification

- Carrier: unchanged total-energy divisor and existing marked-energy support;
- stable rank-three deficit: untyped primitive-chart statistic;
- strict Gauss--Manin closure: falsified;
- logarithmic/Rees closure: falsified;
- physical coefficient class: unsupported;
- new Carrier datum: unsupported.

## Scope

This rejects this primitive source-word lattice, not the existence of a
different source-derived rank-twenty-six observer object. It does not alter the
generic rank-twenty-six module or the independently established physical port
maps. Any replacement must be constructed by horizontal saturation or by a
source-normalized comparison map; it may not be selected to preserve the
rank-three deficit.

## Durable verification

- research/benincasa/derive_rank26_source_word_basis.py;
- research/benincasa/check_rank26_total_energy_source_word_rees.py;
- research/benincasa/check_rank26_total_energy_source_word_closure.py;
- research/benincasa/sparse_modular_submodule_closure_stream.rs;
- research/benincasa/check_rank26_total_energy_source_word_pole_order.py;
- research/benincasa/sparse_modular_submodule_pole_stream.rs;
- research/benincasa/rank26-total-energy-source-word-pole-order-a12-p32003.json;
- research/benincasa/check_rank26_source_word_closure_falsifier.py;
- research/benincasa/rank26-source-word-closure-falsifier.json;
- research/benincasa/rank26-total-energy-source-word-closure-a12-p32003.json;
- research/benincasa/rank26-total-energy-source-word-closure-a14-p32003.json;
- research/benincasa/rank26-total-energy-source-word-closure-a12-p32009-point-3-5-m8.json;
- research/benincasa/rank26-total-energy-source-word-closure-log-a12-p32003.json.
- epistemic event
  ev-000000003260-64e8668e-1f15-45d5-8552-a42d0e99dc60.

## Next falsifier

Derive the meromorphic normal connection of the generic rank-twenty-six cyclic
module in the frozen primitive frame. Compute its Smith/Levelt shearing and
construct the resulting source-normalized logarithmic lattice before choosing
any physical quotient. Only then compare the low/high marked-wall, score,
polarization, and relative-cycle ports against that horizontal object.
