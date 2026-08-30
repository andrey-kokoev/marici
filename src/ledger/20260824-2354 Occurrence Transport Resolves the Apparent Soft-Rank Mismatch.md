# 2354 — Occurrence Transport Resolves the Apparent Soft-Rank Mismatch

## Problem from Entry 2347

In the fixed \(\mathcal G_{12}\) chart, specialized tangent closure of the
literal source gives labelled soft ranks

\[
(20,20,24)
\]

on \((X_1,X_2,X_3)=(0,*,*),(*,0,*),(*,*,0)\).  Does this violate occurrence
covariance?

## Correct naturality square

Occurrence reflection transports more than kinematic coordinates.  Under

\[
\sigma_{23}:\mathcal G_{12}(X_1,X_2,X_3)
\longrightarrow
\mathcal G_{31}(X_1,X_3,X_2),
\]

the literal numerator and residue orientation become

\[
q_{g_{23}}+q_{g_{31}}
\longmapsto
-\bigl(q_{g_{23}}+q_{g_{12}}\bigr).
\]

The minus sign is the ordered Poincare-residue orientation.

At the source soft fiber \((3,0,5)\) and reflected target fiber \((3,5,0)\),
the complete labelled tangent closures satisfy

\[
\dim M_{m src}=20,
\qquad
\dim M_{\rm tgt}=20,
\qquad
\dim\sigma_{23}(M_{\rm src})=20.
\]

Every mapped generator reduces into the target closure:

\[
\boxed{\text{containment failures}=0.}
\]

Hence

\[
\boxed{
\sigma_{23}:M_{m src}^{\rm soft}
\overset{\sim}{\longrightarrow}
M_{\rm tgt}^{\rm soft}.
}
\]

## Interpretation

Entry 2347's rank \(24\) at the same target kinematic coordinates used the
canonical \(\mathcal G_{12}\)-chart source there, not the transported
\(\mathcal G_{31}\)-chart source.  The two numbers therefore describe two
different source sections.  Their mismatch is contextual source dependence,
not a failure of occurrence covariance.

This is a concrete example of the program's faithful-coordinate rule:
kinematic coordinates alone do not identify a labelled relative object.  The
chart, numerator occurrence, and residue orientation are part of its type.

## Remaining scope

The calculation proves one reflected soft-fiber isomorphism over
\(\mathbf F_{32003}\).  It does not yet construct the soft nearby-cycle Rees
module or pair it with the physical relative cycle.

## Artifacts

- `research/benincasa/check_rank26_soft_occurrence_transport.py`
- `research/benincasa/rank26-soft-occurrence-transport.json`

Sequence claim: `seqclaim-fa7d31ae58c88f57d5c9fa94`.
