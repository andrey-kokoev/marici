# Twenty-one magnetic harmonic ports minimally repair grade-three faithfulness

## Result

On the magnetic parity sector,

\[
 \ker\mathcal A_3=\bigoplus_{l=2}^{4}\mathcal H_{l,M},
 \qquad \dim_\mathbb R=21.
\]

No postprocessing of `A_3 C` can reconstruct coefficients already erased at
this arrow. Let `P_low` be the orthogonal projector onto magnetic `l=2,3,4`.
Then

\[
 \boxed{\mathcal J_3(C)=(\mathcal A_3C,P_{\rm low}C)}
\]

is injective on every Sobolev or distributional magnetic source space and is
stably invertible in the graph norm. Any finite-dimensional linear repair
needs at least 21 real scalar ports; harmonic coefficient pairings supply
exactly 21 and are minimal.

## Derivative-grade ladder

For `A_r^+=bareth eth^r` on spin-two fields:

| port | low modes killed |
|---|---|
| direct shear `C` | none |
| `bareth C` | none for `l>=2` |
| `bareth eth C` | `l=2` |
| `bareth eth^2 C` | `l=2,3` |
| `bareth eth^3 C` | `l=2,3,4` |

Grade-three blindness is cumulative endpoint failure of the raising ladder.
A grade-zero derivative port or the direct low coefficients restores all
modes. Combining grades one through three still misses `l=2`.

## Local, contour, and temporal ports

- Complete local shear test functions detect every nonzero smooth low mode.
- Puncture residue periods detect none: smooth harmonics have no pole residue.
- Contours downstream of the zero grade-three density remain zero.
- A lower-derivative Green/contour observable may detect them, but it is a
  different readout with its own kernel.
- Endpoint memory detects only `Delta C`.
- Returning pulses have zero endpoint memory but are detected by time-resolved
  news or energy ports.

The low projector commutes with parity and antipodal matching because it is a
sum of complete `l` blocks, and it is orthogonal to translation charges.

## First nonfaithful arrow

For smooth completed magnetic sources, the first additional nonfaithful arrow
is the spectral grade-three multiplier at `l=2,3,4`. It precedes any
Green/contour selection. Its typed witness is the 21-component low harmonic
packet.

## Evidence

`checkers/low_kernel_observability_checks.py` verifies the derivative-grade
zero pattern, minimal repair rank, augmented injectivity, parity commutation,
residue blindness, and endpoint/news distinction.
