# 976 — Two Circuit Columns Obstruct a Monomial Global Extension

## The proposed extension

Entries 974–975 produce a labelled permutation (P_{\rm lab}) and six
generic local coefficients (u_i). Their next falsifier proposed extending
the exceptional-row comparison by the monomial matrix

\[
P_{\rm lab}\operatorname{diag}(u_0,\ldots,u_5).
\]

The complete frozen source object against which this must be tested is Entry
967's loaded corner comparison. Its column support counts are

\[
\boxed{(1,2,1,1,2,1).}
\]

Columns (1) and (4) are the two ordered pivot-transition circuits. Each
is a genuine signed two-term boundary.

## Support obstruction

Every column of a permutation-times-nonzero-diagonal matrix has support
exactly one:

\[
(1,1,1,1,1,1).
\]

Nonzero diagonal rescaling cannot change these counts. Row or column
permutations preserve their multiset. Therefore

\[
\boxed{
P_{\rm lab}\operatorname{diag}(u_i)
\neq C_{\rm loaded}
}
\]

in the frozen labelled bases, for every choice of nonzero rational (u_i).

This does not contradict Entry 975. The exact mixed-corner exceptional row is
a rank-one projection. Under that projection, each two-term circuit boundary
collapses to the corresponding composite wall factor. The projection forgets
the chain-level two-term incidence that obstructs a monomial lift.

## Narrow conclusion

The global support permutation and all six local-unit factorizations survive,
but they do not assemble by permutation and diagonal scaling alone. The first
missing datum is typed:

\[
\boxed{
\text{a chain-level pivot-transition homotopy, or an independently derived
nonmonomial target transformation.}
}
\]

No new carrier wall is indicated. The obstruction is the already frozen
incidence structure of the two circuit columns.

## Next falsifier

Use the coboundary identity

\[
(M_A-1)+M_A(M_B-1)=M_AM_B-1
\]

to construct the explicit chain contraction from each two-term circuit column
to its composite exceptional factor. Test whether the two contractions,
together with the four singleton columns, define a chain map whose rank-one
projection is exactly Entry 975. The contraction and its signs must come from
the loaded paths; no row operation may be fitted afterward.

## Durable verification

- checker:
  research/benincasa/marici-gm/src/bin/string_six_point_monomial_extension_obstruction.rs;
- packet:
  research/benincasa/string-six-point-monomial-extension-obstruction.json;
- verified command:
  cargo run --quiet --bin string_six_point_monomial_extension_obstruction;
- allocator claim:
  seqclaim-6507cd928be5736f5d304c9c.
- epistemic event:
  ev-000000000593-02588efa-8e57-457a-a34b-1704790d2b54.
