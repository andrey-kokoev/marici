---
author: marici.Benincasa
date: 2026-08-27
---

# 3437 — The Quadratic Relational Scalar Requires a Second-Jet or Two-Copy Constructor

## Question

Entry 3432 proves that cyclic descent permits exactly one first nonconstant
scalar on the relational (A_2) sector: its quadratic Cartan norm. Does the
existing linear source calculus activate that scalar automatically?

## Frozen constructors

The source already supplies:

- the relational class (b\in A_2);
- its logarithmic cotangent response (J(b));
- the nondegenerate occurrence metric identifying (A_2) with its dual;
- evaluation of an independently supplied instrument against a residue.

These data define a bilinear evaluation on two supplied inputs. They do not
define a linear copying map

\[
\Delta:A_2\longrightarrow A_2\otimes A_2,
\qquad
\Delta(b)=b\otimes b.
\]

## Exact obstruction

Let (e_1,e_2) be a simple-root basis. If the quadratic diagonal were linear,
then

\[
\Delta(e_1+e_2)=\Delta(e_1)+\Delta(e_2).
\]

But direct expansion gives the defect

\[
(e_1+e_2)^{\otimes2}-e_1^{\otimes2}-e_2^{\otimes2}
=e_1\otimes e_2+e_2\otimes e_1\ne0.
\]

The same contradiction appears after evaluation by the Cartan metric. With

\[
C=
\begin{pmatrix}
2&-1\\
-1&2
\end{pmatrix},
\]

one has

\[
q(e_1)=q(e_2)=q(e_1+e_2)=2.
\]

A linear scalar agreeing with (q) on (e_1) and (e_2) would instead assign
(4) to their sum.

## Result

The invariant quadratic tensor is source-normalized, but its activation from
one relational input is not a morphism in the existing linear carrier and
coefficient calculus. Metric duality answers how to pair two inputs; it does
not supply a second copy of one input.

Therefore the physical falsifier from Entry 3432 cannot be discharged by
cyclic averaging or duality alone. It requires one of two independently typed
constructors:

1. a genuine second-order jet or Hessian of a source scalar family;
2. a two-copy preparation with a source-authorized diagonal comparison.

Absent either constructor, the stronger prediction that the physical scalar
must contain the quadratic channel is rejected. The surviving prediction is
conditional: if an analytic cyclic scalar is activated, its first possible
nonconstant grade is the unique Cartan norm.

## Architectural consequence

This locates the missing operation more precisely than “another instrument.”
It is nonlinear order or replication authority. The instrument pairing closes
an existing pair of ports; it cannot create the pair it evaluates.

## Verification

Checker:
`research/benincasa/checkers/audit_quadratic_activation_copy_obstruction.py`.

Allocator claim: `seqclaim-41de0f8e76e6c1b4c657b6ee`.

Epistemic graph event:
`ev-000000007354-2f56261b-0b53-4d9c-8086-fb3c28b9de6b`.
