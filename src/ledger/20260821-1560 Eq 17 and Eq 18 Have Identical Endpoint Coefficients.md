# 1560 — Eq. (17) and Eq. (18) Have Identical Endpoint Coefficients

## Hard-to-vary claim

Once the integrated boundary Hamiltonian is typed as

\[
\int H_0=-S_0,
\]

the direct exponent in Eq. (17) and the Hamiltonian representation in
Eq. (18) have identical quadratic coefficients:

\[
\boxed{
-\frac12H^2+HS_0-\frac12S_0^2.
}
\]

Therefore the factor-two mismatch isolated in Entry 1558 is not introduced
by replacing \(+iS_0\) with an endpoint Hamiltonian insertion.

## Exact comparison

Equation (17) gives

\[
\frac12(-iH+iS_0)^2
=
-\frac12H^2+HS_0-\frac12S_0^2.
\]

Equation (18) gives

\[
-\frac12(H+H_0)^2,
\]

and substituting \(H_0=-S_0\) produces the same expression. Entry 1559's
separated regulator verifies that the local notation
\(H_0=-\tfrac12\delta S_0\) realizes this integrated identity without a
diagonal excess.

## Artifacts

- `research/benincasa/checkers/eq17_eq18_endpoint_expansion.rs`
- `research/benincasa/results/eq17-eq18-endpoint-expansion.json`

## Narrow conclusion

The source discrepancy is downstream of Eq. (18). Given the independently
checked sector reductions

\[
J_1,qquad-2J_2,qquad-J_0,
\]

the first unresolved step is the unpublished contraction/reduction that
produced Eq. (19)'s doubled boundary-containing coefficients.

This does not yet prove that Eq. (19) is wrong: an omitted contraction family
could still supply a second copy of both boundary-containing sectors. But it
cannot come from exponent combinatorics, endpoint delta mass, or a simple
diagonal contact.

## Next falsifier

Perform a labelled Wick census directly from the unsymmetrized
\(\zeta(\partial\zeta)^2\) slots for all connected two-point fish
contractions. Partition it by bulk--bulk, mixed, and boundary--boundary
location. Test whether any contraction family is absent from the compact
sector formulas while leaving the bulk coefficient unchanged.
