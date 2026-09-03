# Audit of the claimed compact-window Weil certificate

## Question

Can the unconditional margin claimed in arXiv:2608.24827v2 be admitted as executable evidence for the Gaussian truncation route?

## Source inspection

The arXiv source archive was downloaded directly on September 4, 2026. Its SHA-256 is

`1afc4e867bc69cabf5128db8b70187af61804e55bd773a16cdf16d17c4284c73`.

The archive contains only:

- `00README.json`;
- `main.tex`;
- four PNG figures.

The TeX source has SHA-256

`14ec17c2b2e1d3d8069c1d424dae4f5aa6c92b75c73b89d10915ed868495f2c5`.

No matrix, Cholesky factor, interval enclosure, error-budget file, run log, source script, zero dataset, hash manifest, or independent verifier occurs in the archive. The only external URL in the TeX file is the general mpmath website.

## Printed claim

Theorem `thm:L08` states that for every real even `f` supported in `[-0.8,0.8]`,

\[
Q(f)\ge 8.9\times10^{-18}\|f\|_2^2.
\]

The prose at source lines 267--275 attributes this to a 200-mode Legendre computation with 50-digit arithmetic and tail/coupling errors below `10^-100`. The reproducibility section at lines 2440--2462 says that supplementary material provides code, matrices, factors, logs, budgets, hashes, and `verify_certificate.py`. Those files are absent from the downloaded arXiv source package.

The same paper records that an earlier support-2.38 certificate was retracted because a prime-envelope inequality ran in the wrong direction. This correction increases, rather than decreases, the need to inspect the actual support-1.6 certificate.

## Disposition

The printed theorem is a potentially useful unrefereed claim, but its computational proof is not independently reproducible from the arXiv package. The numerical margin must not be used as an admitted bound in the RH argument until the claimed supplementary package is obtained and the independent verifier is run.

Classification: `authority-blocked computational claim`.

This does not refute the theorem. It blocks the proposed immediate comparison

\[
|W(h-h^{(0.8)})|<8.9\times10^{-18}\|f_{0.8}\|_2^2
\]

because the right-hand margin is not presently verified.

## Reopening condition

Obtain the exact supplementary archive named in the reproducibility section, including `verify_certificate.py`, the archived `M_200`, Cholesky factor, quadrature budgets, tail constants, logs, software versions, and SHA-256 manifest. Verify that the hashes match the paper and run the independent verifier under the declared environment.

## Surviving route

The analytic one-stroke reduction in Theorem `thm:reduction` can still be audited from the TeX proof. A new independent implementation could reconstruct the `L=0.8` matrix and budgets, but that is a substantial certification project rather than verification of the claimed archived certificate. The finite-double-contact problem remains open.
