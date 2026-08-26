# Muon–tau selector disposition (WP259)

## Admitted domain and probe

The admitted state domain is the frozen 2015 CMS muon–tau pilot family at
labelled masses 130, 140, and 160 GeV, together with its partial simulated
background grammar. The 2016 actual-pole dimuon records remain a separate
source domain.

The largest currently source-authorized probe family on the tau branch is the
WP251 same-path trigger/offline-object operation followed by the WP253
visible-mass bins. It is executable on the declared files and separates the
three labelled signal templates and admitted background. Summing those bins
is a rank-one projection and erases this distinction.

## Contextual partition

The probe partitions the finite pilot domain by labelled visible-mass shape.
It does not induce the equality partition of `physical16`:

- fixed-bin interpolation fails exact leave-one-out closure;
- source-relative scaling improves the residual but still fails closure;
- the improved scaling requires a source-mass reference outside `physical16`;
- the existing actual-pole dimuon records lack four common-frame interface
  fields required by the tau response.

The first kernels therefore occur at distinct arrows: rate projection,
finite-grid transport, forgetting the source-mass port, and cross-topology
detector transfer.

## Selector classification

The tau branch is a finite-domain source-labelled discriminator and readout.
It is neither a proper-subspace selector nor a texture-presentation rigidifier,
and it is not a complete physical instrument on `physical16`. Its finite
template rank demonstrates distinction only inside the declared source-labelled
experiment; it supplies no numerical flavor selection law.

The smallest exact hostile witness remains WP257's pair: one `physical16`
point and one 65 GeV visible record acquire ratios \(1/2\) and \(13/32\) solely
from different external mass labels.

## Remaining gate

Progress requires same-frame actual-pole tau samples or an independently
derived reweighting that carries common topology, era, selection, physical
branching normalization, QCD control, weighted completion, and uncertainties.
Without that constructor, the branch closes negative for flavor selection.

Run `uv run --with sympy python
research/flavor/checkers/wp259_tau_branch_selector_disposition.py` for the
exact parent-chain and capability-matrix audit.
