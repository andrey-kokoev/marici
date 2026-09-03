# The `q_G12` sewn-residue factorization square

## Question

Does physical residue commute with source sewing at the first three-site factorization divisor?

## Claim boundary

For the `q_G12` sector, the source-unsplit rational form is explicitly

\[
\frac{da\wedge db}{\sqrt{K_E}\,q_{g1}q_{g2}q_{g3}}
\left(\frac1{q_{g23}}+\frac1{q_{g31}}\right).
\]

The two occurrence terms therefore enter before the next residue with the source coefficients `(+1,+1)` and a common orientation. Direct substitution computes sewn form-level residues on `q_g1`, `q_g2`, and `q_g3`; all three have generically nonzero numerators. Execution `structured_command_execution:e_4616_1788296044880618900_62` reproduces the exact rows.

The occurrence-resolved certificate independently proves

\[
\eta_{31}+\eta_{23}=\eta_{\rm unsplit},
\qquad
\Phi_{31}+\Phi_{23}=\Phi_{\rm unsplit}
\]

coefficientwise at both endpoints. Hence sewing commutes with taking the meromorphic representative and its endpoint-jet boundary data. Regulator hierarchy and endpoint subtraction remain ambiguous for either summand, but cancel in the source-unsplit combination.

## Result strength

The square commutes at the rational-form and endpoint-jet levels:

\[
\operatorname{Res}_{q_{gi}}\circ S
=
S_{\partial}\circ
\left(
\operatorname{Res}_{q_{gi}}^{(23)}
\oplus
\operatorname{Res}_{q_{gi}}^{(31)}
\right),
\qquad i=1,2,3,
\]

where equality means direct algebraic substitution with the frozen common orientation. This is not yet a physical factorization theorem.

## First missing arrow

The existing checker explicitly leaves open normalization/conductor reduction of each wall one-form and their Čech sum. No admitted arrow identifies the resulting sewn residue class with an independently normalized lower-graph amplitude or cosmological-wavefunction coefficient.

Thus the first missing map is

\[
N_{\partial}:H^1_{\rm sewn}(q_{G12}\cap q_{gi})
\longrightarrow
\mathcal A_{\rm lower},
\]

including the `sqrt(K_E)` branch, orientation, conductor reduction, and source normalization. Generic numerator nonvanishing does not prove cohomological nonvanishing or the lower-graph identification.

## Deliberate failure

Keeping only `1/q_g23` or `1/q_g31` fails physical canonicity: allowed regulator hierarchies change its boundary current, and endpoint exact terms retain nonzero polar jets. The single-occurrence route therefore cannot define `N_partial`.

## Acceptance test

1. reduce each sewn wall one-form in the declared conductor/relative complex;
2. compute their Čech sum with orientation;
3. prove independence from two regulator hierarchies and two endpoint trivializations;
4. specify the lower-graph source object and normalization;
5. verify equality, not only proportionality, in all three shared-wall channels;
6. retain one occurrence-resolved term as the required failure.

## Disposition

Source sewing repairs occurrence-level noncanonicity and the residue square passes through endpoint jets. Physical amplitude factorization remains blocked at normalization/conductor reduction and the lower-graph comparison map.

## Evidence

- `research/benincasa/physical_g12_shared_wall_residues.py`
- `research/benincasa/occurrence-resolved-physical-period-no-go.md`
- `research/benincasa/complete-unsplit-weight-zero.json`
