# Vacuum-port authority for partial sewing

## Question

What physical constructor authorizes attenuation of the outer sewing operation?

## Construction

Mix the visible sewing mode with a calibrated vacuum port through a lossless
two-mode coupler. Choose transmitted and complementary amplitudes `3/5` and
`4/5`. Their squared norm is exactly one.

The forward and reverse incidences each acquire amplitude `3/5`. The complete
visible round trip therefore acquires

\[
\tau=\frac35\frac35=\frac{9}{25}.
\]

At source coherence `gamma = 3/5`, the predicted relational visibility is

\[
V=\gamma\tau=\frac{27}{125}.
\]

## Authority gate

The scalar `tau` is not a free fitting parameter. Admission requires:

- the full two-port unitary transformation;
- calibration of both incidence directions;
- retention of the complementary vacuum-port outcome;
- explicit distinction between the full dilation and visible compression.

Vacuum identity additionally requires the companion coherent-leakage gate. A
small number expectation alone does not null the ancillary first moment.

The full dilation preserves norm and has no loss kernel. Its visible
compression forgets the complementary port and therefore has different kernel
data. They cannot be identified merely because their visible amplitudes agree.

## Falsification

The constructor fails if either incidence amplitude differs from `3/5`, the
column norm differs from one, complementary outcomes are discarded, or the
measured visibility differs from `27/125` after independently calibrated
source coherence and detector response are applied.

## Disposition

This repairs the abstract partial-sewing control. The attenuation now arises
from an executable optical dilation rather than selective scaling of one
formula block.

## Verification

Run:

```text
python research/aspect/checkers/check_vacuum_port_sewing_authority.py
```
