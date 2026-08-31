# Direct vertical boundary transport falsified

## Test

For the boundary inclusion from ambient degree \(A\) to \(A+2\), the candidate transition

\[
J_A(k,i,j)=(k,i,j+2)
\]

was tested by comparing normalized descriptor-coefficient signatures of independently reconstructed q-lifts.

## Result

No signature matches:

| inclusion | source boundary rows | matches |
|---|---:|---:|
| 12 to 14 | 48 | 0 |
| 14 to 16 | 60 | 0 |

Therefore multiplication by the second integration variable squared does not transport the chosen boundary representatives literally.

## Disposition

N3b5b1 is falsified. The failure does not yet falsify boundary compatibility modulo `T + S_K`: two q-lift representatives can differ while defining the same residual identity modulo the base relation space.

N3b5b remains active through N3b5b2. The next test must translate each source q combination into the larger ambient module, subtract the independently selected target q combination, and reduce that difference modulo the target `T + S_K`. Vanishing would supply an explicit correction cell; nonvanishing would exhaust this vertical-transition route.

## Reproducibility

- Signature extractor: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_ambient_signatures.py`
- Comparator: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_vertical_transport.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_boundary_vertical_transport.json`
