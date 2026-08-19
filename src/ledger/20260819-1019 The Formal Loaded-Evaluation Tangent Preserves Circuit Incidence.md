# 1019 — The Formal Loaded-Evaluation Tangent Preserves Circuit Incidence

## Algebraic control problem

Entry 1017 constructs the universal first logarithmic jet but does not reduce
the physically inserted forms.  Before attempting that reduction, differentiate
the already proved rational identity from Entry 977,

\[
\lambda C=r,
\]

where (C) is the complete occurrence-labelled loaded comparison and
(lambda) is its unique circuit-compatible exceptional cochain.

Choose the (B_{34}) channel.  Exact Symbolica differentiation gives

\[
\boxed{
\lambda' C+\lambda C'=r'.
}
\]

All 6 components are verified as rational identities; no sampling or fitted
primitive is used.

## Incidence support

The original column supports of (C) are

\[
(\{1\},\{2,3\},\{4\},\{3\},\{0,1\},\{5\}).
\]

Only columns (4,5) depend on (B_{34}).  Their derivative supports are

\[
(\varnothing,\varnothing,\varnothing,\varnothing,\{0,1\},\{5\}),
\]

which are exactly the existing (B_{34}) circuit and singleton incidences.
Thus

\[
\boxed{
\operatorname{Supp}(C')\subseteq\operatorname{Supp}(C).
}
\]

No new edge, wall, or circuit cell appears in the formal tangent lift.

## Interpretation

The rational loaded comparison has a canonical first tangent, and its two-term
boundary structure survives differentiation.  Therefore a connection-level
obstruction cannot be blamed on failure of the frozen circuit incidence under
ordinary algebraic differentiation.

This is deliberately not identified with the physical Gauss–Manin derivative.
The latter differentiates the Koba–Nielsen factor and inserts
(log(f_{34})), as emphasized by Entry 929.  The missing comparison is now the
difference between:

\[
\text{physical logarithmic insertion reduction}
\quad\text{and}\quad
\text{formal tangent of the rational loaded evaluation}.
\]

## Narrow conclusion

\[
\boxed{
\text{formal first tangent closes on existing incidence;
physical first tangent remains uncomputed.}
}
\]

Any residual physical extension will be coefficient-theoretic rather than a
new carrier incidence.

## Next falsifier

Construct the (B_{34}) logarithmically inserted six-form packet from the
source disk integrals.  Map it to the formal tangent packet through twisted
de Rham reduction.  The comparison cone is the intrinsic first-jet extension:
zero cone closes the rank-one comparison, while a nonzero cone must be
classified within the logarithmic coefficient object.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_loaded_evaluation_tangent.rs`;
- packet:
  `research/benincasa/string-six-point-loaded-evaluation-tangent.json`;
- allocator claim:
  `seqclaim-24192245af21df9ba620c7d0`.
- epistemic event:
  `ev-000000000638-05bf8fe1-6a3c-477f-bca1-9383bed1e27f`.
