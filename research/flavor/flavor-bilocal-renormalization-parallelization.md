# Bilocal renormalization parallelization

Work package: WP552  
Owner: marici.Figueiredo

## Question

After WP551 separates Omega scale setting from dimensionless residues, where
does current and operator renormalization actually act in the WP535 pipeline?

## Typed factorization

For each pole, collect the four bare bilocal estimators into

\[
h_i^{\mathrm{bare}}=(H_{i,V},H_{i,RR},H_{i,LL},H_{i,RL})^T.
\]

A common declared operator map gives

\[
h_i^{\mathcal S}=Z_{\mathcal S}h_i^{\mathrm{bare}}.
\]

The Ward-complete amplitude is

\[
A_i=w_i^{\mathcal S}h_i^{\mathcal S},
\qquad
w_i^{\mathcal S}=
\left(1,-{m_b^2\over\mu_i^2},-{m_s^2\over\mu_i^2},
{2m_bm_s\over\mu_i^2}\right).
\]

The signed source residue enters only after this operation:

\[
M_{12}^{\mathrm{new}}=\sum_i r_i A_i.
\]

Thus \(Z_{\mathcal S}\) acts on bilocal operator coordinates, not on the
source resolvent residue \(r_i\).

## Scheme covariance

For any invertible change of renormalized operator basis \(S\),

\[
h_i^{\mathcal S'}=S h_i^{\mathcal S},
\qquad
w_i^{\mathcal S'}=w_i^{\mathcal S}S^{-1}.
\]

Then \(A_i\) is unchanged exactly. The checker verifies this for six poles and
a nontrivial exact diagonal basis change. The residue-weighted scalar is also
unchanged without transforming the residues.

This is a parallelization contract: the estimator vector and Ward coefficient
row must be transported through the same named scheme interface. Compatible
coordinates alone do not authorize their composition.

## Rank and covariance

With one invertible four-channel map shared across all poles, the 24-channel
renormalization map has rank 24 and the six Ward rows retain rank six. The
covariance must transform as

\[
C_{\mathcal S}=(I_6\mathbin\otimes Z_{\mathcal S})
C_{\mathrm{bare}}
(I_6\mathbin\otimes Z_{\mathcal S})^T.
\]

Cross-pole covariance is retained because all six kernels are evaluated on
the same ensemble stream.

## Deletion replay

Deleting \(Z_{\mathcal S}\), its subtraction prescription, or its covariance
does not alter the source residues and does not undo the Omega unit map. It
does invalidate every renormalized \(A_i\) and hence the experimental scalar.

The smallest exact falsifier is to change the operator basis by \(S\) while
holding the Ward coefficient row fixed. The amplitude then changes even
though a legal scheme change must leave it invariant.

## Status

WP552 is an exact typing and covariance theorem. It is neither a selector nor
an executed renormalization calculation. Physical authority requires a
nonperturbatively determined mixing and subtraction matrix in a declared
continuum scheme, with uncertainties and common-ensemble covariance.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp552_bilocal_renormalization_parallelization.py

The generated result is
research/flavor/results/wp552_bilocal_renormalization_parallelization.json.
