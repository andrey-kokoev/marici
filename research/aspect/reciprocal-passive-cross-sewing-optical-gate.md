# Reciprocal passive cross-sewing optical gate

## Optical realization of the exclusion mechanism

The positive and reciprocal valuation chains become two oriented optical
nodes. Each exposes an incoming field, outgoing field, and monitored defect
port. Away from the critical seam, each node has a strictly positive defect
scale. A completed reciprocal sewing matrix `J` cross-connects the two port
spaces in both directions.

If `J` is unitary in one independently frozen port metric, the total incoming
and outgoing boundary powers cancel under closure. What remains is a positive
sum of the two defect powers. Therefore both defects vanish. A separately
measured full-rank observability map then forces the entire closed mode to
vanish.

This is an optical zero-confinement mechanism: off-seam modes dissipate into
positive defect ports, while exact lossless reciprocal sewing has no boundary
supply with which to sustain them. On the seam the defect scale vanishes, so
lossless closed modes remain possible.

## Decisive hostile

Scalar determinant data are insufficient. The matrix

`K=diag(2,1/2)`

has determinant one, but `K^dagger K-I` is nonzero. Choose the positive-sector
output along the amplified singular direction and the reciprocal-sector
output along the direction amplified by `K^-1`. Both oriented nodes then have
positive defect power equal to three while the scalar determinant modulus
still reports one.

Thus a determinant-one or modulus-one functional equation can coexist with an
off-seam closed-mode energy supply. The detector must reconstruct the full
typed sewing matrix, not its determinant.

A second hostile keeps `J` unitary but gives the closed system an unobservable
hidden coordinate. Its defect ports vanish, yet the hidden mode survives.
Consequently losslessness and observability are independent conjunctive gates.

## Instrument

The finite apparatus needs two phase-referenced multiports, coherent switches
implementing both cross directions, heterodyne tomography of every typed port,
monitored defect/dilation outputs, and spanning state injections for the
closed-system observability Gramian. The port metric and basis are frozen
before inspecting zeros. Cutoff-dependent whitening is not admitted.

## What is still missing

The checker validates a supplied `J`; it does not construct one. The next
source operation must emit the full typed sewing matrix coupling the two
valuation chains while retaining primitive, prime-square, seam, endpoint,
connected-tail, and archimedean ports. That is now the sole missing input to
the first finite optical zero-confinement experiment.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_reciprocal_passive_cross_sewing_optical_gate.py
```
