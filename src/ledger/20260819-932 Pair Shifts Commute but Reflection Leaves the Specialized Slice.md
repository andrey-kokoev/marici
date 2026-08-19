# 932 — Pair Shifts Commute but Reflection Leaves the Specialized Slice

## Coherence test

Entry 931 derived the rank-eight integer-shift closure and proposed two tests:
commutativity of the pair shifts and compatibility with occurrence reflection.
The first is internal to the specialized symbol packet; the second requires a
label audit before computation.

## Strict shift cocycle

Apply

\[
T_{24}:B_{24}\mapsto-B_{24},
\qquad
T_{34}:B_{34}\mapsto-B_{34}
\]

to every exact component of the source row \(r\). Direct symbolic reduction
gives

\[
\boxed{
T_{24}T_{34}r=T_{34}T_{24}r.
}
\]

Thus the four-character closure is a strict representation of
\((\mathbf Z/2)^2\). It needs no associator or correction cell.

## Reflection type gate

The reflection used in Entry 920 is \(\tau=(24)\). On the unspecialized
six-point monodromy labels it acts by

\[
A_2\leftrightarrow A_4,
\qquad
A_3\mapsto A_3,
\]

and

\[
B_{23}\leftrightarrow B_{34},
\qquad
B_{24}\mapsto B_{24}.
\]

Consequently the current tangential slice

\[
\{A_2,A_3,B_{24},B_{34}\}
\]

is transported to

\[
\{A_4,A_3,B_{24},B_{23}\}.
\]

Only two coordinates remain in the original slice. Therefore reflection is
not an internal operator on Entry 931's specialized four-character module.

## Correction

The final sentence of Entry 931 suggested comparing reflection with an
exchange \(B_{24}\leftrightarrow B_{34}\). That exchange is not the source
label action and is withdrawn. Performing it would conflate tangential and
normal variables after maximal-flag specialization.

The correct architecture is

\[
\boxed{
\text{unspecialized occurrence atlas}
\xrightarrow{\tau}
\text{unspecialized occurrence atlas}
\xrightarrow{\operatorname{gr}_{F}}
\text{chartwise shift modules}.
}
\]

Reflection covariance must be checked before, and then transported through,
the associated-grade specialization.

## Narrow result

The discrete coefficient system passes its internal flatness test:

\[
[T_{24},T_{34}]=0.
\]

Occurrence covariance remains untested rather than failed. Its current
specialized formulation was mistyped; no new carrier or coefficient defect
has been found.

## Next falsifier

Lift the source row construction to the six unspecialized labels

\[
A_2,A_3,A_4,B_{23},B_{24},B_{34},
\]

construct the reflected maximal-flag grade independently, and test the square

\[
\operatorname{gr}_{\tau F}\circ\tau
\stackrel?=
\tau_F\circ\operatorname{gr}_F.
\]

Only after this Beck--Chevalley square is typed may the four character
components be compared across occurrence charts.

## Durable verification

- checker:
  research/benincasa/marici-gm/src/bin/string_six_point_shift_coherence.rs;
- packet:
  research/benincasa/string-six-point-shift-coherence.json;
- allocator claim:
  seqclaim-50e6eb306289363d827e802b.
- epistemic event:
  ev-000000000549-c87519db-705a-423f-a48c-00714acbc9a2.
