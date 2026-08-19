# 1033 — The Localized Loaded Complex Has a Unique Internal Contraction

## Frozen complex

Entry 1028 types the loaded matrix as the differential

\[
C_1^{\rm load}\xrightarrow{C}C_0^{\rm chamber}.
\]

Entries 969 and 1032 give

\[
C=S\operatorname{diag}(q_i),
\qquad
q_i=M_i-1,
\qquad
S\in GL_6(\mathbb Z).
\]

Let

\[
R_{\rm reg}=R[q_1^{-1},\ldots,q_6^{-1}].
\]

## Exact contraction

Over (R_{\rm reg}), define

\[
\boxed{
h=\operatorname{diag}(q_i^{-1})S^{-1}.
}
\]

Direct exact multiplication gives

\[
\boxed{
Ch=1_{C_0},
\qquad
hC=1_{C_1}.
}
\]

Because (C) is invertible, any two-sided contracting homotopy is necessarily
(C^{-1}).  The contraction is therefore unique inside the frozen two-term
complex.

Its only poles are the six labelled occurrence factors (q_i).  No additional
irreducible denominator or integer index occurs.

## Narrow result

\[
\boxed{
\text{the localized loaded complex has no internal Čech or extension
obstruction.}
}
\]

Any remaining global Betti obstruction cannot be obtained by choosing a
different inverse, endpoint gauge, or circuit representative inside this
complex.  It must arise from additional geometric data: a higher-cell lift,
an intersection pairing, or a source normalization not encoded by the
two-term loaded packet.

This cleanly separates two statements:

\[
\text{algebraic loaded complex: canonically contractible after localization},
\]

\[
\text{global regularized twisted cycles: not yet constructed}.
\]

## Consequence for the next test

The next calculation should not search for another (6\times6) inverse.
Instead, it must construct the comparison from the geometric
loaded-associahedron cellular complex to this two-term model.  Its restriction
to degree one is forced to be (h).  The sole possible new class is the
failure of that comparison to extend through the native two-cell.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_loaded_complex_contraction.rs`;
- packet:
  `research/benincasa/string-six-point-loaded-complex-contraction.json`;
- allocator claim:
  `seqclaim-fb8ddb1d9e494d6d1fffc9eb`.
- epistemic event:
  `ev-000000000652-27f96777-c562-476d-9498-0f33dc6da763`.
