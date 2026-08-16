---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Homogeneous Source Sector Inventory and the Missing Top-Sector Gluing Data

## Record

The first global-decomposition audit falsifies a naive rank inventory.
The number 34 does not describe the homogeneous three-site system. It is
the source count for the generic multi-external-leg lower family where
\(x_i\ne P_i\).

For homogeneous kinematics the primary source instead fixes:

\[
\boxed{\operatorname{rank}\mathcal P=15}
\]

for the displayed polylogarithmic four-denominator family,

\[
\boxed{\operatorname{rank}\mathcal Z=7}
\]

for its zero-denominator subsector, and

\[
\boxed{\operatorname{rank}\mathcal M_{G_{12}}^{q\text{-only}}=9}
\]

for the subsector containing only \(q_{\mathcal G_{12}}\), with source
block dimensions

\[
1+2+2+4=9.
\]

These are source-fixed modules, not pieces that may automatically be added
to obtain a global rank.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{the printed ranks }15,7,9\text{ canonically determine a complete
direct-sum decomposition of the homogeneous physical coefficient system.}
}
\]

The finite falsifier is the literal denominator support of equation
\(\mathrm{Triangle}\). Its six physical summands contain one of

\[
q_{\mathcal G_{12}},\quad
q_{\mathcal G_{23}},\quad
q_{\mathcal G_{31}}
\]

together with one of two lower poles. The source then says that evaluation
splits into:

1. a polylogarithmic family with lower denominators;
2. families containing \(q_{\mathcal G_{ij}}\) and a pair of lower
   denominators.

But the printed nine-master list is explicitly only the
\(q_{\mathcal G_{12}}\)-only subsector. The paper does not print the
master counts, bases, or complete differential modules of the
\(q_{\mathcal G_{ij}}\)+two-lower-pole top sectors.

Therefore

\[
15+3\cdot9
\]

is not a source-authorized global rank. It mixes one complete lower family
with proper subsectors of three larger cyclic families and omits the top
extensions that contain the physical summands.

## Exact source inventory

Primary source:
Benincasa--Brunello--Mandal--Mastrolia--Vazão,
arXiv:2408.16386v2, applications.tex.

- lines 204--243: six-term physical integrand;
- lines 273--276: partial-fraction split into the two family types;
- lines 309--327: fifteen-master polylogarithmic family;
- lines 329--365: seven-master homogeneous zero sector and its ten-letter
  linear alphabet;
- line 367: rank 34 only for generic multi-external-leg kinematics;
- lines 371--395: definition of the \(q_{\mathcal G_{12}}\)-containing
  families with lower-pole pairs;
- lines 397--421: nine-master \(q_{\mathcal G_{12}}\)-only subsector and
  block dimensions \(1,2,2,4\).

The exact executable certificate checks all rank markers, derives

\[
3^3-2^2(2+3)=7,
\]

checks the six cyclic denominator supports in the physical integrand, and
refuses the naive global rank.

## Classification

- fifteen-master lower family: source-defined polylogarithmic coefficient
  module;
- seven-master zero sector: Tate/Kummer/polylogarithmic subsector;
- nine-master \(q\)-only sector: source-defined residue coefficient
  module with rank-seven algebraic kernel and rank-two elliptic quotient;
- cyclic \(q\)+two-pole top sectors: source-defined denominator supports
  whose complete coefficient modules are not yet reconstructed;
- transition maps among partial-fraction families: not printed;
- number 34: nonhomogeneous lower-family datum, not the homogeneous rank;
- new carrier incidence: none derived;
- shared-carrier conjecture: not falsified by this gap.

The obstruction is coefficient-module and gluing data, not missing carrier
incidence.

## Consequence for the global conjecture

A canonical global decomposition cannot yet be claimed. The strongest
current architecture is a diagram of known subquotients:

\[
0\to\mathcal T_7\to
\mathcal M_{G_{ij}}^{q\text{-only}}
\to\mathbb V_{\rm ell}^{(ij)}(-1)\to0,
\]

together with the lower module \(\mathcal P\), the zero subsector
\(\mathcal Z\), and marked-relative endpoint objects. The source-defined
top-sector modules and their extension arrows remain missing vertices in
that diagram.

This is not evidence for a new cosmological carrier primitive. It is a
failure of the proposed decomposition to be fully defined.

## Exact evidence

- temp/arxiv-2408.16386-source/sections/applications.tex;
- temp/arxiv-2408.16386-source/sections/PartialFractioning.tex;
- research/benincasa/marici-gm/src/bin/homogeneous_sector_inventory.rs;
- research/benincasa/homogeneous-sector-inventory.json.

## Next hostile falsifier

For one canonical cyclic sector, freeze

\[
\{q_{\mathcal G_{12}},q_{\mathfrak g},q_{\mathfrak g'}\}
\]

exactly as printed. Compute its complete twisted-cohomology rank, a master
basis, and the support filtration by denominator deletion. Then derive the
maps to:

\[
\mathcal M_{G_{12}}^{q\text{-only}}
\quad\text{and}\quad
\mathcal P.
\]

Cyclic transport may be used only after the first sector closes.

The finite falsifier of shared carrier is a top-sector class whose
singular support or boundary map cannot be generated from the frozen
Cayley--Menger and denominator arrangement. Rank growth alone is
sector-specific coefficient complexity and does not falsify the carrier.

## Outcome contract

~~~json
{
  "claim": "The printed homogeneous ranks canonically determine a complete direct-sum coefficient decomposition.",
  "status": "falsified_by_missing_top_sector_modules_and_gluing",
  "homogeneous_polylog_family_rank": 15,
  "homogeneous_zero_subsector_rank": 7,
  "q_G12_only_subsector_rank": 9,
  "q_only_blocks": [1, 2, 2, 4],
  "generic_multi_external_lower_rank": 34,
  "rank_34_is_homogeneous": false,
  "naive_global_rank_authorized": false,
  "missing_modules": "q_Gij plus two-lower-pole top sectors",
  "missing_arrows": "support-filtration and cyclic partial-fraction transition maps",
  "new_carrier_incidence": false,
  "next_experiment": "Compute one complete q_G12 plus two-pole twisted-cohomology module and its deletion maps."
}
~~~
