---
id: 20260827-3269
date: 2026-08-27
status: tested-candidate-boundary-audit
---

# 3269 — The Candidate Sole Double Pole Matches the Source Rees Location but Not Its Recorded Sign

## Question

Does the exact reconstructed rank-twelve final-block candidate use the
second total-energy normal grade already forced by Entries 292--293, or does
it introduce an unauthorized higher pole?

Use the homogeneous chart

\[
u=E/X_1,
\qquad
v=(X_1+X_2-X_3)/X_1,
\qquad X_1=1,
\]

and the ordered target basis \((e_6,e_7,e_8,e_9)\) and source quotient basis
\((q_0,q_1,q_2)\), with (q_0) induced by \(\Omega_{111}\).

## Exact candidate calculation

Every one of the twenty-four rational functions was cancelled over
\(\mathbb Q(u,v)\).  Its (u)-adic order and leading coefficient were then
computed symbolically.  The order matrices are

\[
\operatorname{ord}_u B_u=
\begin{pmatrix}
-2&-1&-1\\
-1&-1&-1\\
-1&-1&-1\\
-1&-1&-1
\end{pmatrix},
\qquad
\operatorname{ord}_u B_v=
\begin{pmatrix}
-1&0&0\\
0&0&0\\
0&0&0\\
0&0&0
\end{pmatrix}.
\]

Thus the candidate has exactly one double pole:

\[
\operatorname{Lead}_{u=0}^{(-2)}(B_u)_{e_6,q_0}=-\frac18.
\]

All other entries are at most logarithmic in the total-energy normal.

## Comparison with the frozen source theorem

Entry 292 found in the raw primitive two-wall frame

\[
\operatorname{Lead}_{E=0}^{(-2)}
(\nabla_E\Omega_{111})=+\frac18e_6.
\]

The two calculations therefore agree on all structural data visible before
normalization:

- one and only one second-order normal term;
- source class \(\Omega_{111}\), hence (q_0);
- target line \(\langle e_6\rangle\subset\mathcal T_7\);
- no elliptic component;
- no new carrier divisor.

They do not agree on the recorded sign.

This is not repaired by the coordinate change.  At fixed (X_1=1),

\[
X_2=(u+v)/2-1,
\qquad
X_3=(u-v)/2.
\]

The difference between fixed-(v) and fixed-(X_2) differentiation is
tangent to (u=0), while the exact candidate (B_v) has no double pole in
the relevant coordinate.  A tangential correction therefore cannot reverse
the displayed second-order coefficient.

## Narrow conclusion

The candidate's pole order and labelled location are source-predicted, but
its boundary normalization is not yet source-authorized.  The mismatch has
three live explanations:

1. an undeclared sign change between the old raw (e_6) frame and the current
   serialized rank-twelve frame;
2. an opposite connection convention in one reduction;
3. failure of the generic-fiber rational interpolation at the boundary
   (u=0).

No one of these may be selected by convenience.  In particular, agreement
of absolute value does not license changing a normalization after seeing the
answer.

## Finite falsifier

Repeat the formal Laurent reduction of the complete current source
presentation directly at (u=0), using

\[
e_6=-\frac{K_1}{2K^{3/2}},
\qquad q_0=[\Omega_{111}],
\qquad \nabla=d+A.
\]

Export the fixed (u^{-2}) coordinate before interpolation.  The outcomes
are decisive:

- (-1/8): the old Entry 292 convention bridge must be corrected or made
  explicit;
- (+1/8): the reconstructed candidate fails at the total-energy boundary;
- non-fixed coordinate: the candidate's apparent second-order coefficient is
  presentation data rather than a source invariant.

Until this calculation is complete, the sole double pole is classified as a
candidate Rees term on existing algebraic coefficient support, not as a
certified rank-twelve source theorem.

## Durable artifacts

- checker: `research/benincasa/checkers/audit_marked_extension_total_energy_orders.py`;
- packet: `research/benincasa/results/marked_extension_total_energy_orders.json`;
- candidate: `research/benincasa/marked-extension-charzero-candidate.json`;
- allocator claim: `seqclaim-b4492c644b49fb0949323fa3`.
