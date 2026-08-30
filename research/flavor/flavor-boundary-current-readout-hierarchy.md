# Boundary-Current Readout Hierarchy

## Question

If WP854 selects an oriented antisymmetric boundary current, which existing or
minimal flavor probes can read its magnitude and sign?

## Source packet

Represent the two matched charged-cycle paths by

\[
p=(P_A,P_B)^T.
\]

The normalized boundary orientations are

\[
p_+=\frac1{\sqrt2}(1,-1)^T,
\qquad
p_-=-p_+,
\]

and the absent source is (p_0=0). The sign labels orientation relative to
the marked boundary port.

## Ordinary sum-port kernel

The WP638--WP641 charged contact factors through the sum row

\[
S=(1,1).
\]

Both oriented boundary states and the absent source satisfy

\[
Sp_+=Sp_-=Sp_0=0.
\]

Consequently the current contact, partonic cross section, and its downstream
Standard Model interference are all blind to the WP854 boundary mode. Once
the source is projected through (S), no downstream probe can restore it.
The first nonfaithful arrow is the two-path current-to-sum projection, before
charged-scalar elimination or detector response.

## Loop parity readout

The WP644 neutral loop depends on a product such as (P_AP_B^*). It separates
the symmetric and antisymmetric relative-sign classes, but

\[
(p_+)_A(p_+)_B^*=(p_-)_A(p_-)_B^*=-\frac12.
\]

Thus it retains relative parity while erasing the boundary orientation. Its
`physical16` response also carries the previously established normalization
and rank-two limitations.

## Complementary difference port

The source-derived complementary row

\[
D=(1,-1)
\]

gives

\[
Dp_+=\sqrt2,
\qquad
Dp_-=-\sqrt2,
\qquad
Dp_0=0.
\]

Amplitude access would separate all three contexts. Intensity alone retains
presence and magnitude but identifies (p_+) with (p_-).

To recover orientation, the experiment needs a coherent calibrated reference
amplitude (R\ne0) in the same external channel. The pair of responses

\[
|R+Dp|^2,
\qquad
|R-Dp|^2
\]

is odd-sensitive through their difference. This reference changes the
physical groupoid to the stabilizer of its declared phase. It measures a
relative sign and does not reveal an absolute phase of the unreferenced
experiment.

## Instrument status

No current charged-cycle instrument supplies the difference port before the
sum projection. WP641's Standard Model amplitude is downstream of the map to

\[
G=|SP|^2/m_\chi^2,
\]

so it cannot serve as the missing reference for (Dp). A valid realization
requires a second source-derived charged amplitude with the same external
quantum numbers and controlled relative phase, finite widths, production
support, and detector calibration.

## Classification

- Existing sum/contact family: neither separator nor instrument for the
  boundary current.
- Existing loop family: relative-parity probe, not orientation-faithful and
  not a selector.
- Difference intensity: source-relative magnitude probe requiring a new port.
- Referenced difference pair: jointly faithful on the declared three-state
  boundary packet, conditional on a calibrated coherent instrument.

This does not yet close the full portal objective. It specifies the smallest
physical readout architecture capable of retaining the sign selected by
WP854 and proves why the existing contact channel cannot do so.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp855_boundary_current_readout_hierarchy.py
```
