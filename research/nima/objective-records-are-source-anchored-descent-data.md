# Objective records are source-anchored descent data

## Result

An objective record across multiple observers is not merely the repetition of a
local value. It is a global section obtained by gluing local closed interfaces.

Let each observer carry a local record/control closure. On every overlap, a
typed comparison states how the two local records correspond. Objective closure
requires:

- each local record is admitted;
- every overlap comparison is source-authorized;
- the comparisons have trivial holonomy around every loop;
- the resulting global section is anchored when the target claim distinguishes
  a source value;
- overlap witnesses survive the declared fault model.

This is a descent condition. Local readability and pairwise agreement do not by
themselves construct a global objective record.

## Exact three-observer hostile

Let observers \(A,B,C\) carry local bits. Suppose the overlap relations require

```text
B agrees with A
C agrees with B
A disagrees with C
```

Every individual overlap is satisfiable, and every two-edge subsystem is
satisfiable. But the product of transition signs around the triangle is
negative. No global assignment of three bits satisfies all overlaps.

The obstruction is the loop holonomy. It is the Boolean form of a nontrivial
first cohomology class.

If all three overlaps require agreement, two global sections remain: all zeros
and all ones. A source anchor selects one when the claim carries a distinguished
origin. Gluing establishes existence; source authority establishes the
operative choice.

## GHZ interpretation

In a redundant GHZ record, every nonempty proper fragment carries the same
classical pointer label. Those local labels descend to a global classical
record. Relative phase, however, is absent from every proper fragment and lives
only in the global relationship. It therefore has no local descent datum on the
fragment cover.

This explains the asymmetric code structurally:

- pointer information is locally repeatable and descends;
- conjugate phase is globally relational and does not descend;
- local objectivity of one channel is paid for by local loss of the other.

## Fault boundary

Trivial holonomy is a coherence condition, not a fault theorem. A Byzantine
observer may supply inconsistent overlap values to different neighbors.
Objective authority additionally requires quorum or authentication assumptions
strong enough to guarantee at least one honest witness on the relevant
overlaps.

## Falsifier

The three-edge parity loop with odd total parity is the smallest global
falsifier. Any compiler that infers a global record from pairwise satisfiability
alone is rejected with `nontrivial_descent_holonomy`.

