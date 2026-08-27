# Complete strict Hankel positivity does not confine the Evans character orbit

## A positive continuous hostile

Let `mu` have density `1` on `[0,1]` and density `2` on `[1,2]`. Its
bilateral Laplace transform is

\[
F(z)=\int_0^2 e^{zx}\,d\mu(x)
=\frac{e^z-1}{z}(1+2e^z),
\]

with the value at `z=0` supplied by removable continuation. Hence

\[
F(-\log 2+(2k+1)\pi i)=0
\]

for every integer `k`. These zeros have nonzero real part.

## The entire Stieltjes moment tower is strict

The moments are

\[
m_j=\int_0^2x^j\,d\mu(x)=\frac{2^{j+2}-1}{j+1}.
\]

For every nonzero real polynomial `p`,

\[
\sum_{i,j}c_i c_jm_{i+j}
=\int_0^2p(x)^2\,d\mu(x)>0.
\]

The shifted form is also strict:

\[
\sum_{i,j}c_i c_jm_{i+j+1}
=\int_0^2x p(x)^2\,d\mu(x)>0.
\]

Therefore every finite ordinary and shifted Hankel moment matrix is positive
definite. This is the complete strict Stieltjes moment condition, not merely
positivity of one finite carrier block.

## Consequence

Complete moment positivity controls the source measure and its resolvent
geometry. It does not orient the exponential character orbit. A positive
continuous source with the strongest finite Stieltjes tower can still have
off-seam zeros in its Evans/Laplace readout.

The missing RH law must therefore relate at least two pieces of structure:

```text
positive source carrier
+ distinguished exponential character orbit
+ theta/modular sewing
```

No theorem stated only in terms of ordinary and shifted Hankel positivity can
confine the endpoint zeros. In particular, replacing selfadjointness by
positive definiteness or total moment positivity does not repair the hostile
from the preceding source-Hankel theorem.

This does not concern the actual theta source and does not prove or disprove
RH. It rejects a proposed class of explanations.

## Durable verification

- Checker: `checkers/check_complete_strict_hankel_evans_hostile.py`
- The checker verifies the exact moment formula, exact off-seam character
  cancellation, and strict positivity of ordinary and shifted Hankel
  determinants through order eight. The all-orders statement follows from
  the displayed positive-density integrals.
