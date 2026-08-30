# Paired mate sewing interferometer

## Question

What optical instrument realizes `2(3+2+1)+1` and detects relational coherence
that is absent from both completed local descriptions?

## Construction

A heralded path-correlated photon pair feeds two independently controlled
path-marker mate interferometers, wings A and B. Each wing contains its own
input, output, and control; forward record construction and backward
conditioning; and calibrated mate totalization over its complete record.

Only after both local mates close, a delayed coherent analyzer sews the wings.
It resolves the even and odd joint sectors. This outer operation is the final
`+1`. Classical comparison of already measured local bits is not its substitute.

## Exact signature

For coherence `gamma` and joint-phase cosine `c`, freeze

\[
p_{00}=p_{11}=\frac{1+\gamma c}{4},
\qquad
p_{01}=p_{10}=\frac{1-\gamma c}{4}.
\]

Both local marginals are exactly one half at every phase. Nevertheless,

\[
p_{\rm even}=\frac{1+\gamma c}{2},
\qquad
p_{\rm odd}=\frac{1-\gamma c}{2}.
\]

The discovery channel is therefore not a local fringe. It is a joint parity
fringe carried entirely by the relation between locally completed wings.

## Frozen finite gate

The instrument uses three coherence settings and four joint phases. Six
proportions are retained per cell: four joint outcomes and two local marginals,
for seventy-two primary proportions. With 750,000 effective trials per
proportion and tolerance one twentieth, Chebyshev plus the union bound gives
the exact familywise ceiling

\[
\frac{72}{4(750000)(1/20)^2}=\frac{6}{625}<\frac{1}{100}.
\]

All single-click and no-click records remain attached to the pair herald. Both
local calibrations and the joint analyzer calibration must share one epoch.

## Falsifiers

The executable contract rejects:

- two factorized local mate instruments with no joint coherence;
- a coincidence-only parity fringe missing the full wing outcomes;
- calibration assembled across different epochs;
- phase dependence leaking into either local marginal;
- classical comparison presented as coherent sewing.

## Disposition

This is a finite source-typed optical instrument for relational coherence. Its
positive signature is flat local marginals together with a calibrated joint
even-odd fringe after both local mates have closed.

## Claim boundary

The checker establishes the finite probability and acquisition contract. A
source implementation still requires a declared entangled-pair preparation,
physical coherent parity analyzer, loss model, and spacetime timing layout.

## Verification

Run:

```text
python research/aspect/checkers/check_paired_mate_sewing_interferometer.py
```
