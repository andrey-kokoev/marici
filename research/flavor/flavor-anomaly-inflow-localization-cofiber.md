# Anomaly-inflow localization cofiber: WP755

## Question

Does five-dimensional anomaly inflow select the bulk-versus-boundary
localization needed to remove WP754's spectral-index ambiguity?

## Local balance equations

For one anomaly channel, let \(B\) be the total anomaly coefficient of bulk
chiral zero modes and let \(b_0,b_\pi\) be boundary-localized coefficients.
The bulk anomaly is split equally between the fixed points. A five-dimensional
Chern–Simons level \(k\) contributes with opposite signs:

\[
A_0=b_0+\frac{B}{2}+k,
\qquad
A_\pi=b_\pi+\frac{B}{2}-k.
\]

The global condition is

\[
A_0+A_\pi=b_0+b_\pi+B=0.
\]

It contains no \(k\). Whenever the global condition holds and the needed
level belongs to the admitted quantization lattice,

\[
k=-b_0-\frac{B}{2}
\]

cancels both local anomalies. Thus inflow pairs the boundary imbalance with a
Chern–Simons class rather than selecting the localization.

Localized anomalies of bulk orbifold fermions and their relation to
long-distance four-dimensional cancellation were derived by
[Arkani-Hamed, Cohen, and Georgi](https://arxiv.org/abs/hep-th/0103135).
The role and normalization of Chern–Simons terms in localized cancellation
are discussed by
[Groot Nibbelink, Nilles, and Olechowski](https://arxiv.org/abs/hep-th/0205012).

## Smallest exact witness

Take a four-dimensional chiral packet with anomaly coefficients \(+1\) and
\(-1\).

If both modes arise from bulk fermions, their half anomalies cancel at each
boundary and \(k=0\).

If the \(+1\) mode is localized at \(y=0\) and the \(-1\) mode at \(y=\pi R\),
the raw boundary anomalies are \((1,-1)\), and \(k=-1\) cancels both.

The four-dimensional spectrum and global anomaly are identical, while the
bulk hypermultiplet count differs by two. Therefore the two lifts contribute
differently to the WP753 spectral index.

## Disposition

Anomaly inflow is not by itself a localization selector. With an adjustable
inflow level it defines a cofiber of paired localization and Chern–Simons
classes. Fixing local consistency does not fix the Scherk–Schwarz spectral
sign.

The next source datum cannot be another freely chosen inflow counterterm. A
higher-dimensional anomaly polynomial, topological compactification, or UV
completion must derive the complete Chern–Simons level vector independently.
Only after freezing that vector can the local anomaly equations be used to
test whether one localization class survives.

This theorem covers a channel cancellable by one Chern–Simons term. Some
non-Abelian, mixed, or parity-anomaly channels can impose stronger constraints
or have no such cancellation. Those complete anomaly lattices remain to be
computed for the product-group flavor packet.

The portal spectral sign, gauge normalization, radion, boundary masses,
threshold accessibility, physical16 descent, and calibrated instrument remain
open.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp755_anomaly_inflow_localization_cofiber.py

Generated result:
research/flavor/results/wp755_anomaly_inflow_localization_cofiber.json
