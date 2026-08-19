# 977 — The Exceptional Row Lifts Uniquely as a Circuit-Compatible Cochain

## Retaining incidence

Entry 976 shows that the complete loaded comparison cannot be replaced by a
permutation-times-diagonal matrix. The two circuit columns must remain
two-term boundaries.

Let (C) be Entry 967's loaded (6\times6) matrix and let

\[
r_i=f_i u_i
\]

be Entry 975's six exceptional components in occurrence order. We seek a
target cochain

\[
\lambda=(\lambda_0,\ldots,\lambda_5)
\]

such that

\[
\lambda C=r.
\]

## Source-derived solution

The four singleton columns force

\[
\lambda_1=u_0,qquad
\lambda_4=u_2,qquad
\lambda_3=u_3,qquad
\lambda_5=u_5.
\]

The two oriented circuit boundaries then force

\[
\lambda_3-\lambda_2=u_1,
qquad
\lambda_1-\lambda_0=u_4.
\]

Therefore

\[
\boxed{
\lambda=
(u_0-u_4, u_0, u_3-u_1, u_3, u_2, u_5).
}
\]

Exact Symbolica substitution verifies all six identities

\[
\boxed{(\lambda C)_i=f_i u_i.}
\]

The signs are not fitted: they are exactly the signed endpoint orientations
of Entry 967's two circuit columns. Since (C) is generically invertible,
the cochain is unique over the common function field.

## Narrow conclusion

The monomial matrix of Entry 976 fails, but the exceptional comparison itself
does lift:

\[
\boxed{
\text{the rank-one exceptional row is the evaluation of a unique
circuit-compatible cochain on the frozen loaded complex.}
}
\]

Thus the apparent obstruction is resolved by preserving incidence, not by
adding support or choosing a post hoc row operation.

This proves a rank-one cochain comparison only. It does not establish a
six-dimensional chain equivalence or horizontality under kinematic
transport.

## Next falsifier

Transport \(\lambda\) around the chamber hexagon using the frozen pivot
transition maps. Test whether it is a cocycle globally:

\[
\delta\lambda=0.
\]

If a defect remains, determine whether the native two-cell coboundary kills
it. A nonzero class after that contraction is the first genuine global
assembly obstruction.

## Durable verification

- checker:
  research/benincasa/marici-gm/src/bin/string_six_point_circuit_exceptional_cochain.rs;
- packet:
  research/benincasa/string-six-point-circuit-exceptional-cochain.json;
- verified command:
  cargo run --quiet --bin string_six_point_circuit_exceptional_cochain;
- allocator claim:
  seqclaim-a848ecce09cc455fa0923ae4.
- epistemic event:
  ev-000000000594-675dc47f-1205-4d69-8a98-5df74da2d6cd.
