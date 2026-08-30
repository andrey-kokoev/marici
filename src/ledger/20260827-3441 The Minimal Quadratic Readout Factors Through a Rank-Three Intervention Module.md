---
author: marici.Benincasa
date: 2026-08-27
---

# 3441 — The Minimal Quadratic Readout Factors Through a Rank-Three Intervention Module

## Question

Entry 3437 proves that linear preparation and readout cannot activate the
unique quadratic scalar on the relational (A_2) sector. Does inserting one
typed intervention stage suffice, and what is its minimal universal object?

## Three-stage factorization

Work in the category of graded polynomial laws. The preparation supplies
(b\in A_2). The degree-two intervention is the Veronese map

\[
\nu_2:A_2\longrightarrow\operatorname{Sym}^2(A_2),
\qquad
b\longmapsto b^{\odot2}.
\]

The readout is contraction with the Cartan metric,

\[
q_C:\operatorname{Sym}^2(A_2)\longrightarrow\mathbb Q.
\]

Thus the scalar factors as

\[
A_2\xrightarrow{\nu_2}
\operatorname{Sym}^2(A_2)
\xrightarrow{q_C}\mathbb Q.
\]

The first arrow is polynomial of degree two; the second is linear. This keeps
the nonlinear authority in the intervention rather than hiding it in readout.

## Exact hostile test

In the simple-root basis, the cyclic action on (A_2) induces an exact
three-dimensional action on

\[
\operatorname{Sym}^2(A_2)
=\langle x^2,xy,y^2\rangle.
\]

The audit establishes:

1. (\nu_2) is cyclic-equivariant;
2. its images span all three dimensions of the symmetric square;
3. the cyclic-invariant readout space on that middle object has dimension one;
4. its generator is the Cartan contraction
   (2x^2-2xy+2y^2);
5. deleting the intervention gives the Entry 3437 linearity contradiction.

Hence the rank-three middle object is universal for quadratic laws. Replacing
it directly by its invariant scalar quotient would presuppose the final
readout and lose non-invariant quadratic responses.

## Architectural result

The notation (3(3+2+1)+2+1) has a coherent operational interpretation:

- preparation module;
- intervention or jet module;
- readout module;
- two typed interfaces between them;
- one final event closure.

These are three situated modules over one shared Carrier, not three separate
Carriers. At quadratic order, the intervention module is concretely
(\operatorname{Sym}^2(A_2)).

The result proves sufficiency and minimal universality at the algebraic level.
It does not prove that the frozen Bunch--Davies source realizes the Veronese
intervention physically. That remains a second-jet or two-copy preparation
question.

## Verification

Checker:
`research/benincasa/checkers/audit_three_module_quadratic_factorization.py`.

Allocator claim: `seqclaim-9799eff99206ee21b8b57e64`.

Epistemic graph event:
`ev-000000007362-5a8b3e26-0602-4dfb-80aa-c0ded2dcfa8b`.
