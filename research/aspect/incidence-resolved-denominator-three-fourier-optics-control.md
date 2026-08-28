# Incidence-resolved denominator-three Fourier optics control

## Matched scalar sources

Compare the canonical integer comb with Grothendieck's denominator-three
Fourier orbit at strength `0<epsilon<1`.  Before normalization, the hostile
integer residue weights are

`(1+2epsilon,1-epsilon,1-epsilon)`

and the shifted endpoint classes `+1/3` and `-1/3` each carry weight
`epsilon`.  Division by `1+2epsilon` makes both mean density and origin weight
equal to one, exactly matching the canonical scalar metadata.

The four noncanonical ports

`(P_+,P_-,C_+,C_-)`

form a Fourier orbit.  Their equal sum is fixed by the orbit permutation.
Positivity, Fourier invariance, origin normalization, and mean density
therefore all survive.

## Incidence port

Retain the endpoint-class distribution per Haar cell:

`canonical=(1,0,0)`

for offsets `(0,+1/3,-1/3)`, while

`hostile=(1,epsilon,epsilon)/(1+2epsilon)`.

Both vectors have scalar sum one.  They are nevertheless different packets.
The fractional-incidence monitor has response

`2epsilon/(1+2epsilon)`

on the hostile and zero on the canonical source.

This is the required cross-prime/source discriminator: scalar normalization
forgets which endpoint inside each Haar cell carried the mass.

## Active rank identification

Use two declared probes:

1. common-density excitation;
2. fractional-endpoint excitation.

The canonical response has rank one.  The hostile response has rank two.  The
common probe alone gives the same aggregate response and aliases the models;
the second probe exposes the extra incidence direction.

This imports Sontag's disturbance-excitation theorem directly into the theta
apparatus.  Multiple detector records are not enough; the endpoint-class
direction must be actively excited.

## Optical packet

Use three time bins or spatial modes for endpoint offsets `0,+1/3,-1/3` and
four coherent internal ports for the rational Fourier orbit.  Record:

- the normalized scalar sum;
- the origin amplitude;
- both fractional endpoint amplitudes;
- the four-port Fourier permutation residual;
- the baseline, common-probe, and fractional-probe response columns.

The expected hostile signature is a scalar match and a strictly positive
incidence mismatch.  If the incidence-resolved packet also matches, this
denominator-three model has been implemented incorrectly or an unrecorded
projection has erased the fractional ports.

## Transfer to the RH kernel-avoidance problem

The two-prime codiagonal hostile proved that a scalar sewing kernel can create
off-seam zeros from locally confined cells.  This control now tests the first
source-specific candidate for avoiding that kernel: one distinguished
endpoint per unit Haar cell.  It does not establish confinement.  It makes the
incidence law an independently measured input rather than a scalar attribute
fitted after the zero scan.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_incidence_resolved_denominator_three_control.py
```
