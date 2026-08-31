# Exact replay requires base-row provenance

The canonical-seed extractor inherited the chart default `GAMMA=5` without
serializing its twist. It now explicitly sets the physical value `-1/2` and
records it. Independent reruns at primes 32003 and 32057 reproduce the prior
coefficient hashes exactly, so those two seed signatures are empirically
independent of this correction; the correction prevents generic-twist evidence
from being mislabeled physical.

An exact rational source generator is available in principle: the fiber
polynomials have integer coefficients, differentiation is formal, gamma is
rational, and interpolation has rational Lagrange weights. The present reducer,
however, retains only q-row provenance. It discards the tangent and K base-row
coefficients that witness

`target + q combination in T + S_K`.

The smallest exact subsystem cannot therefore be recovered from current
receipts. The next implementation gate is base-row provenance tracking through
pivot construction and target reduction, followed by reconstruction and exact
replay on that bounded closure.
