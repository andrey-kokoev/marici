# Threshold preregistration completeness audit (WP429)

## Attempted execution

WP428 freezes three rivals, a common preparation command, four frequency
settings, Gaussian detector resolution, and an acceptance rule. Before
constructing the response matrix, the rival-to-readout map must be evaluable
from frozen source data.

For each rival (R_j), a frequency-resolved prediction requires at least:

- pole locations (m_{ja});
- pole widths (Gamma_{ja});
- calibrated residues (r_{ja});
- continuum or contact spectral density (ho_j(\omega));
- the normalization map from the disjoint control channel to the
  selector-facing rate.

WP428 freezes none of these numerical or symbolic rival packets. It freezes the
detector map's sampling locations but not its source functions.

## Why WP130 cannot silently complete it

WP130 contains an exact three-bin response model with a predeclared overlap
parameter (\eta=1/4). It proves that one discrete resolved model has rank
three and that merging bins lowers the rank. It does not provide pole
locations, widths, residues, or spectral densities from which WP428's new
frequency offsets and Gaussian convolution can be derived.

Copying WP130's already-binned response columns into WP428 would replace the
new four-port experiment by the old three-port result. Choosing Lorentzian
poles now to reproduce a desired rank would fit the experiment after
preregistration. Neither operation is admitted.

## Exact disposition

The WP428 response matrix is undefined, not rank-deficient. No rank claim may
be made. The first missing arrow runs from the frozen rival constructor to its
frequency-resolved source spectrum.

The detector convolution and rank map occur only after that arrow.

This is a protocol defect, not evidence against threshold spectroscopy. It is
also a successful hostile test of the preregistration discipline: the missing
source packet was found before an outcome was manufactured.

## Repair contract

A successor preregistration must freeze, from independent source or calibration
data, the full spectral packet for every rival before importing the WP428
detector ports. It must name units and a common frame, define continuum support,
and state uncertainty sets. Only then may it evaluate Gaussian-convolved bin
integrals and rank.

The smallest exact falsifier of this incompleteness claim is a locator already
present in WP428 or its frozen dependencies that supplies every required
spectral field and a declared map to all four readouts. WP130's discrete ideal
matrix does not meet that contract.

Run `uv run --with sympy python
research/flavor/checkers/wp429_threshold_preregistration_completeness.py` to
regenerate the JSON result.
