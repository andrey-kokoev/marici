# Reference synchronization is a cohomological error-correcting code

## Question

What structure lies beneath the action-groupoid account of relational
objectivity, and what does it say about the possibility of correcting
reference faults?

## Construction

For a connected graph and an abelian gauge group, vertex frames form

\[
C^0 \xrightarrow{\delta} C^1 \xrightarrow{H} Z,
\]

where edge records are in (C^1), \(\delta\) forms relative transitions, and
(H) records products around an independent family of cycles. The defining
identity is

\[
H\delta=0.
\]

Consequently, cycle syndromes depend only on the class of an edge record
modulo vertex-frame changes. A fault (e\in C^1) is invisible to every cycle
check exactly when it lies in the kernel of (H). For the complete cycle
check on a connected graph,

\[
\ker H=\operatorname{im}\delta.
\]

Thus an undetectable reference fault is not absent. It is observationally
equivalent to a change of local frames.

## Deeper DPC

The proposal predicts:

1. Reference synchronization is an error-correcting code on edge relations,
   but only modulo vertex gauge.
2. Cycle closure is the syndrome map.
3. A tree has no cycle checks and therefore no intrinsic fault-detection
   capacity.
4. A triangle detects a single bad edge but cannot locate it because all
   single-edge columns of its syndrome map coincide.
5. The complete graph on four vertices has three independent cycle checks.
   Its six single-edge syndrome columns are distinct, so it locates one bad
   edge.
6. Its smallest nonzero invisible edge fault is a three-edge vertex cut. Its
   reference-code distance is therefore three and it corrects one edge fault.
7. No amount of cycle redundancy can distinguish a coboundary fault from an
   actual vertex-frame reassignment. That distinction requires an anchored
   vertex port, source dynamics, or another independently authorized carrier.
8. For nonabelian gauge groups, the same architecture survives with groupoid
   cocycles and conjugacy-typed holonomy, but stabilizer multiplication—not
   merely stabilizer cardinality—must be retained.

## Exact resolution

The checker verifies the binary case over the field with two elements.

- The triangle has one syndrome bit and three identical nonzero edge columns.
- The complete four-vertex graph has a rank-three syndrome matrix and six
  distinct nonzero edge columns.
- Exhaustive enumeration finds minimum undetectable nonzero weight three.
- Every coboundary has zero syndrome.
- The kernel of the syndrome map equals the coboundary image.
- Every single-edge fault in the complete four-vertex graph is uniquely
  decoded.

This resolves the finite architecture. The minimum system for fault-correcting
relational objectivity is not merely two carriers plus a relationship. It is a
reference complex with enough independent cycles, plus an explicit choice of
what counts as gauge and what is anchored physical state.

## Claim boundary

The theorem is exact for finite binary reference graphs. It does not assert
that every sector has binary gauge, that every physical reference network is a
graph, or that source dynamics supplies the required anchor. Nonabelian and
higher-cell systems require their own typed construction.

## Disposition

The deeper DPC passes. Relational objectivity factorizes into cohomological
consistency, coding distance, and source incidence. Groupoid descent explains
gauge objectivity; the cochain complex explains which reference faults can be
detected or corrected.

