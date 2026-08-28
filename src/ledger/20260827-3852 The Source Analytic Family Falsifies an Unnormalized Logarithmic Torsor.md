# 3852 — The Source Analytic Family Falsifies an Unnormalized Logarithmic Torsor

## Conjecture tested

Entry 3848 left open the conjecture that the primary three-site source canonically determines only conductor residues, while every finite logarithmic coefficient remains a torsor requiring an external scale choice.

This is too strong.

## Frozen primary-source audit

The source archive for arXiv:2408.16386 defines the loop measure as

\[
\mu_d
=
c_{d,n_e^{(L)},L}
\left(\frac{\operatorname{Vol}^2\Sigma_{n_e^{(L)}}}
{\operatorname{Vol}^2\Sigma_{n_e^{(L)}-L}}
\right)^{(d-n_s-L)/2},
\]

with an explicit dimension-dependent normalization (c_{d,n_e^{(L)},L}).

For the one-loop three-site family,

\[
n_s=3,
\qquad L=1.
\]

The source then declares

\[
d=3+2\epsilon
\]

with (epsilon) serving as an analytic regulator. Therefore the Cayley–Menger factor is not merely (K^{-1/2}), but the normalized analytic family

\[
K^{-1/2+\epsilon}.
\]

The differential-equation solution requires boundary values supplied independently by the original integral, direct integration, or regularity conditions. This is a limitation of solving the differential equation, not freedom to rescale the frozen source family.

## Falsification

The primary source does define a preferred analytic regularization section. Once the original integral and its boundary data are retained, meromorphic continuation in (epsilon) has unique Laurent coefficients.

Hence the broad claim

\[
\text{source readout}=\text{unnormalized logarithmic torsor only}
\]

is false.

An arbitrary replacement

\[
K^{-1/2+\epsilon}
\longmapsto
u^{\epsilon}K^{-1/2+\epsilon}
\]

would shift the finite coefficient by the residue times (log u), but (u) is additional data. It is not an equivalence internal to the frozen primary source.

## Surviving distinction

The source Laurent finite coefficient and a renormalized physical observable are different types.

- The normalized analytic integral has a canonical Laurent jet.
- Admitting finite local counterterms may create a later scheme orbit.
- A physical renormalization condition must select a point in that orbit.

Thus the corrected architecture is

\[
\text{source-normalized Laurent jet}
\longrightarrow
\text{counterterm quotient or orbit}
\longrightarrow
\text{renormalized physical readout}.
\]

Only the latter arrows remain underdetermined.

## Durable artifacts

- `research/benincasa/checkers/check_rank26_source_analytic_regularization_section.py`
- `research/benincasa/results/rank26-source-analytic-regularization-section.json`
- primary source: `temp/arxiv-2408.16386-source.tar`

The checker passes eight source and symbolic gates.

## Next falsifier

Compute the Laurent action of the normalized (K^{-1/2+\epsilon}) family on the two active conductor costalks. Then derive the finite local counterterms admitted by this specific three-site model and determine the rank of their action on the resulting two finite coefficients. Do not import the counterterm space of a different cosmological toy model.
