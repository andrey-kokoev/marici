# Fixed-support Weil gate disposition

## Question

Which original gates are closed, reduced, or blocked after the prior-research audit?

## Claim boundary

This packet records demonstrated proof status. It does not assert positivity of the fixed-support Weil form.

## Gate matrix

### Interval localization: analytically closed

A proper-support \(C^3\) partition exists. For quadratic IMS, the angular windows

\[
\rho_1=\sin(\pi s/2),
\qquad
\rho_2=\cos(\pi s/2)
\]

satisfy \(\rho_1^2+\rho_2^2=1\). Directed interval integration certifies the normalized localization upper bound by the exact outward-rounded dyadic

`0x1.43b3d9e9bf596p+3`.

The half-line Carleman identity, digamma-minus-log bound, and localization commutator estimates establish that the archimedean interval remainder is bounded. Changing an admissible partition changes the declared localization formula by a bounded order-zero form; positivity margins must still be updated.

### Infinite tail: reduced to compact weighted tails

Writing

\[
A=\log(1+\sqrt{-\Delta_D}),
\qquad
K=A^{-1/2}BA^{-1/2},
\]

makes \(K\) compact when \(B\) is the bounded signed remainder. This avoids the invalid scalar-frequency diagonalization and the artificial cutoff produced by subtracting the full localization norm from \(A\).

For a split \(E_M\oplus Q_M\), directed data

\[
\lambda_{\min}(F_M)\ge\mu_M,
\quad
\lVert C_M\rVert\le c_M,
\quad
\lVert Q_MKQ_M\rVert\le r_M<1
\]

certify positivity if

\[
\mu_M-\frac{c_M^2}{1-r_M}\ge0.
\]

Thus the low block, coupling, and tail gates have one finite acceptance test.

### Finite low block: source-blocked, not computed

No signed source matrix has been assembled. Existing Gaussian explicit-formula packets belong to shifted-spectral or modulated-Gaussian test families and do not supply the comparison map to compact zero-extended interval tests.

The first missing authoritative object is a normalized compact-support explicit-formula identity declaring Fourier convention, quadratic normalization, archimedean factor, prime signs/prefactors/directions/adjoints, polar rank terms, zero extension, and the Dirichlet comparison map. The machine-readable acceptance contract is

`research/voevodsky/compact-weil-source-identity-contract.json`.

Until an authoritative instance satisfies that contract, neither the finite ground eigenvalue nor the coupling matrix is defined with source-correct signs. Matrix enlargement is therefore prohibited by the source-identity gate.

## Disposition

The interval-localization gate is closed at boundedness level. The infinite-tail problem is reduced to compact weighted finite-section certification. The finite low-block and coupling values remain unverified because the normalized signed source identity is absent. There is no nonredundant executable matrix computation before that object is materialized.

## Evidence

- `research/voevodsky/angular-ims-directed-interval-integration.md`
- `research/voevodsky/results/angular_ims_interval_integration.json`
- `research/voevodsky/archimedean-boundedness-versus-normalized-assembly.md`
- `research/voevodsky/weighted-birman-schwinger-finite-certificate.md`
- `research/voevodsky/normalized-source-formula-family-mismatch-audit.md`
- `research/voevodsky/compact-weil-source-identity-contract.json`
