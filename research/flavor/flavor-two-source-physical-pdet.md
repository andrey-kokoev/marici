# Two-source physical detector map (WP242)

## Result

There is an executable, experimentally calibrated source-identifying
`P_det` on the finite labelled source domain

\[
\{\mathrm{MSSM}\ M_A=130,\ \mathrm{MSSM}\ M_A=150,
  \ \text{smooth dimuon background}\}.
\]

This is the first flavor-sector detector map here that distinguishes two
source-labelled signal constructors rather than one signal from a nuisance.
It is not yet a selector on `physical16` and does not identify the WP237
trace-adjoint constructor.

## Source and instrument typing

The signal columns come from independently generated CMS Open Data samples:

- record 43611: `MA-130`, `Tanb-20`, 4,600 events;
- record 43651: `MA-150`, `Tanb-20`, 4,600 events.

Both use the same POWHEG V2 plus Pythia8 MSSM bottom-associated production
grammar and forced dimuon decay. Every local ROOT file passes its published
Adler-32 checksum. The frozen WP239 truth-matched reconstruction, quality,
isolation, kinematic, charge, and trigger selection accepts 1,371 and 1,367
events respectively.

The readout is the certified 2016 CMS DoubleMuon collision shard already typed
in WP240. Applying the same reconstructed-muon selection yields 82 events in
the common 110--175 GeV support. A smooth exponential nuisance is fixed from
sidebands that exclude both signal neighborhoods; it is not fitted from either
desired signal template.

## Contextual faithfulness

Let `s130`, `s150`, and `b` be the normalized 1-GeV-bin response columns. The
detector map is

\[
 P_{\rm det}(n_{130},n_{150},n_b)
 =n_{130}s_{130}+n_{150}s_{150}+n_b b.
\]

The measured matrix has rank three and

\[
 \det(P_{\rm det}^{T}P_{\rm det})
 =3.0726019784875036\times10^{-4}>0.
\]

Consequently the three nonnegative component yields are identifiable on this
declared finite response domain. The collision-shard maximum-likelihood yields
are approximately `(0.099, 5.856, 76.045)`. These fitted values demonstrate
execution; they are not a discovery claim and no significance is assigned.

A deterministic 500-replicate multinomial bootstrap resamples both simulated
source columns. The checker requires the five-percent lower quantile of the
Gram determinant to remain positive. This covers finite Monte Carlo counting
uncertainty only; detector systematics, luminosity, and theory normalization
are outside the present identification claim.

The contextual partition consists of distinct `MA130`, `MA150`, and smooth
background response classes. Because invariant mass and source labels do not
depend on weak-basis presentation, this operation descends under the full
weak-basis groupoid on its admitted domain.

## Exact falsifier and authority boundary

Replacing `s150` with `s130` makes the two source columns identical and lowers
the full response rank from three to two. This is the smallest exact falsifier
of source identification.

The source labels authorize identification of these two MSSM mass hypotheses.
They do not authorize identification of trace-adjoint coefficients. The forced
decays also do not provide physical branching fractions. WP241 therefore still
forbids transport to WP237 until a validated topology map or a trace-adjoint
event sample supplies physical production, branching, mass, width, and common
detector response. No reference port is involved.

## Reproduction

Run:

`uv run --with numpy --with awkward --with uproot --with scipy python research/flavor/checkers/wp242_two_source_physical_pdet.py`

The checker regenerates
`research/flavor/results/wp242_two_source_physical_pdet.json` and fails on a
checksum error, source/event mismatch, non-full response rank, nonpositive Gram
determinant, failed collision fit, or failed hostile-pair test.
