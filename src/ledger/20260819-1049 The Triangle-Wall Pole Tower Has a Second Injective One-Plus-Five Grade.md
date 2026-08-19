# 1049 — The Triangle-Wall Pole Tower Has a Second Injective One-Plus-Five Grade

## Question

Entries 1039 and 1045 established an injective pole-depth transition

\[
E_2^{K\le2}\hookrightarrow E_2^{K\le3},
\qquad 7\hookrightarrow13,
\]

whose six-dimensional cokernel has the intrinsic source filtration
\(1+5\): one de Rham direction followed by five principal-coherence
directions, with no contribution from the five new marked-divisor strata.
The next sharp test is whether this is transient or repeats at the next
Cayley--Menger pole depth.

## Depth-four census

At the same finite-field point \((X_1,X_2,X_3)=(2,3,5)\), ambient
relation degree ten, marked pole depth two, and characteristic \(32003\),
the exact-valuation-two ranks are

\[
\dim E_2^{K\le2}=7,
\qquad
\dim E_2^{K\le3}=13,
\qquad
\dim E_2^{K\le4}=19.
\]

The intrinsic depth-four source filtration is

\[
13\xrightarrow{\text{new de Rham}}14
\xrightarrow{\text{new principal}}19
\xrightarrow{\text{five new marked strata}}19.
\]

Thus the new grade again has associated-graded dimensions

\[
\boxed{1+5,}
\]

and the marked strata again add no exact-valuation-two direction.

## Direct transition gate

A source-tracked basis of all thirteen depth-three classes was embedded
blockwise into the depth-four presentation and reduced against the full
target valuation-zero and valuation-one subspace.  The result is

\[
\boxed{
\operatorname{rank}=13,
\qquad
\dim\ker=0,
\qquad
\dim\operatorname{coker}=6.
}
\]

All thirteen representatives have zero reduction remainder.  Therefore
the repeated rank growth is genuine:

\[
\boxed{
E_2^{K\le2}\hookrightarrow E_2^{K\le3}
\hookrightarrow E_2^{K\le4},
\qquad
7\hookrightarrow13\hookrightarrow19.
}
\]

This is evidence for a filtered pole-depth tower, not a stabilized finite
coefficient space.

## Scalar pole-shift obstruction

The repetition does not come from naive multiplication by \(1/K\).  A
diagonal shift \(e_k\mapsto a_ke_{k+1}\) must satisfy

\[
a_{k+1}(\gamma-k)=a_k(\gamma-k-1)
\]

to intertwine the source de Rham relation, whereas the retained principal
relation \(e_k-Ke_{k+1}\) requires

\[
a_{k+1}=a_k.
\]

For \(\gamma=5\), the de Rham ratios at \(k=2,3\) are respectively
\(2/3\) and \(1/2\), while principal coherence requires ratio one.
Hence no nonzero scalar pole shift intertwines both relation families.

The next object must therefore be a coherence-retaining mapping cone or
filtered extension.  The dimensions alone do not canonically identify or
split consecutive six-planes.

## Scope and correction

An earlier chat-only status update momentarily mistook the depth-four
`first_normal_rank` \(9\) for the exact-valuation-two rank.  The relevant
`second_normal_rank` is \(19\).  The incorrect value was never admitted to
the ledger or epistemic graph.

This entry does not assert a stable recurrence for every pole depth, a
canonical splitting of either six-plane, or a finite connection module.

## Durable verification

- generalized staged exporter:
  `research/nima/export_triangle_wall_dual_rows.py`;
- transition-capable exact rank engine:
  `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- compact transition packet:
  `research/nima/triangle-wall-kdepth4-transition.json`;
- scalar-shift checker and packet:
  `research/nima/check_triangle_wall_scalar_pole_shift.py`,
  `research/nima/triangle-wall-scalar-pole-shift.json`;
- allocator claim: `seqclaim-a06f11ed978e4ccde8a6fa71`.
- epistemic event:
  `ev-000000000677-ce7b5362-c05b-4531-82eb-945ef2143f9f`.
