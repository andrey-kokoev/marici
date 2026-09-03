# A uniform diagonal-dominance certificate for Green positivity

## Question

After fixed-size local tests fail, is there a source-checkable condition that certifies joint Green positivity at every finite size?

## Claim boundary

This packet supplies a sufficient finite-dimensional criterion for symmetric real Green matrices. It is not necessary, and it does not establish that the Stieltjes construction satisfies the criterion.

## Certificate

Let \(G=(g_{ij})\) be a symmetric real matrix. Require

\[
g_{ii}>\sum_{j\ne i}|g_{ij}|
\]

for every row. Gershgorin's theorem then places every eigenvalue in the positive half-line, because each interval

\[
\left[g_{ii}-\sum_{j\ne i}|g_{ij}|,
      g_{ii}+\sum_{j\ne i}|g_{ij}|\right]
\]

has positive lower endpoint. Hence \(G\) is positive definite at every finite size.

Unlike a fixed principal-minor cutoff, this test scales with the actual joint matrix and controls the collective mode directly.

## Exact test

The checker constructs a symmetric five-sector matrix with unit diagonal and off-diagonal entries of magnitude \(1/10\). Every row radius is \(2/5\), so every eigenvalue is at least \(3/5\). Exact leading principal determinants are positive.

## Named rivals and falsification scope

Diagonal dominance is not necessary. The four-sector equicorrelation matrix with \(r=1/2\) has row radius \(3/2>1\), so the certificate fails, while its eigenvalues are \(1/2\) and \(5/2\), hence it is positive definite.

The earlier hostile matrix with \(r=-2/5\) also fails diagonal dominance, but is genuinely indefinite. Therefore certificate failure leaves positivity unresolved; it is not a negative verdict.

## Disposition

A uniform all-size Green certificate exists, falsifying any inference that full spectral computation is always necessary. The surviving gate is disjunctive:

- verify full joint positivity directly; or
- provide a source-derived sufficient certificate such as strict diagonal dominance, Cholesky factorization, or another proved positive-kernel construction.

Promotion to Stieltjes remains blocked until its actual Green blocks satisfy one such criterion.

## Verification

- `research/voevodsky/checkers/check_diagonal_dominance_green_certificate.py`
- `research/voevodsky/results/diagonal_dominance_green_certificate.json`
- `research/voevodsky/no-fixed-green-positivity-cutoff.md`
