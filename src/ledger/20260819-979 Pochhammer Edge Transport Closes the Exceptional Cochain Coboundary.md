# 979 — Pochhammer Edge Transport Closes the Exceptional Cochain Coboundary

## Source-derived edge maps

Entry 978 identifies the missing datum as the six-edge action on the target
cochain. Entries 895–896 already provide its rank-one coefficient rule:
crossing an adjacent ordering wall transports the Koba–Nielsen fiber by the
corresponding half-monodromy. Reversing the crossing uses its inverse.

Orient the chamber cycle as

\[
123456\to124356\to142356\to143256
\to134256\to132456\to123456.
\]

The first three moves reverse an increasingly ordered pair; the final three
undo those reversals. Hence the exact transports are

\[
\boxed{
(U_0,\ldots,U_5)
=
(B_{34},B_{24},X,B_{34}^{-1},B_{24}^{-1},X^{-1}).
}
\]

Their cyclic holonomy is

\[
\prod_{k=0}^5U_k=1
\]

before imposing the mixed-corner specialization (X=1).

## Twisted coboundary

Let (c_k) denote the chamber index in the displayed cycle and let
\(\lambda_i\) be Entry 977's target cochain. Define

\[
d_k=\lambda_{c_{k+1}}-U_k\lambda_{c_k}.
\]

The individual (d_k) need not vanish: \(\lambda\) is a cochain evaluating
the exceptional comparison, not a horizontal section of the rank-one local
system.

Transporting every edge defect to the base vertex gives the oriented
two-cell boundary

\[
\boxed{
\sum_{j=0}^5
\left(\prod_{k=j+1}^5U_k\right)d_j=0.
}
\]

Exact Symbolica reduction verifies this identity with the complete rational
formulas for all six components of \(\lambda\).

## Narrow conclusion

The chamber-level comparison closes in the correctly twisted complex:

\[
\boxed{
\delta_{\rm KN}\lambda
\text{ is an exact edge cochain with zero oriented two-cell boundary.}
}
\]

Thus Entry 976's two circuit columns and Entry 978's missing transport do not
produce a global rank-one obstruction once the source Pochhammer local system
is retained. No new carrier wall or fitted coherence cell is required.

This remains rank-one coefficient closure. It does not prove a complete
six-dimensional chain equivalence or Gauss–Manin horizontality.

## Next falsifier

Compare this twisted chamber cochain with the six-point dense momentum-kernel
connection under differentiation in the unspecialized variables. Determine
whether the evaluation map is horizontal, or whether its covariant derivative
defines a nontrivial extension class supported on the existing resonance
divisors.

## Durable verification

- checker:
  research/benincasa/marici-gm/src/bin/string_six_point_pochhammer_cochain_closure.rs;
- packet:
  research/benincasa/string-six-point-pochhammer-cochain-closure.json;
- verified command:
  cargo run --quiet --bin string_six_point_pochhammer_cochain_closure;
- allocator claim:
  seqclaim-10bdda35277b6188dd6341e3.
- epistemic event:
  ev-000000000596-48529e91-dbdd-4a5f-9a90-17a4b6412b46.
