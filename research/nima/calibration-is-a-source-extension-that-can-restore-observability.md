# Calibration is a source extension that can restore observability

## Claim boundary

A calibration record is not merely another passive observation of the same closed system. When its preparation is independently controlled, calibration enlarges the source and interaction alphabet. That enlargement can make a coordinate observable that every passive probe necessarily loses.

This packet establishes the finite categorical and robust-control statement. It does not claim that a particular laboratory or flavor instrument supplies the required calibrated channel.

## Passive quotient

Let the latent state space be

\[
M=X\times \mathbb Z_5
\]

with coordinates \((f,\delta)\). Let \(\mathbb Z_5\) act by

\[
k\cdot(f,\delta)=(f+4k\bmod 20,\delta+k\bmod 5).
\]

The passive record

\[
R(f,\delta)=(f\bmod 4,f+\delta\bmod 5)
\]

is invariant under this action. Its fibers are precisely the five-point orbits. Therefore every probe of the form

\[
q\circ R
\]

is constant on those orbits and cannot recover \(\delta\).

Adding more passive post-processing does not help. The information loss occurred at the quotient map \(R\), before the probes were chosen.

## Controlled source extension

Adjoin an independently prepared calibration input \(u\) with a certified source law. The minimal useful preparation fixes \(f=0\). Its record is

\[
R(0,\delta)=(0,\delta).
\]

This separates the torsor coordinate. The augmented experiment is not a more ingenious readout of the old passive packet. It is a new source-bearing constructor

\[
C:\mathbb Z_5\longrightarrow M,
\qquad
C(\delta)=(0,\delta),
\]

followed by the existing record map.

The distinction is categorical:

- passive probing factors through the quotient \(R:M\to R(M)\);
- active calibration adds a section-like source map into \(M\);
- observability is restored only for the enlarged experiment containing that map.

Calling the calibrated coordinate a hidden primitive of the original closed system would erase the source extension that made it identifiable.

## Connection to context transport

When calibration changes between contexts \(c\) and \(c'\), the prepared reference also constructs a transport between their state and readout fibers. A valid comparison requires

\[
P^Y_{c\to c'}F_c=F_{c'}P^X_{c\to c'}.
\]

Thus calibration performs two logically distinct jobs:

1. it may add an input direction that repairs observability;
2. it may certify the connection used to compare observations across contexts.

Neither job is supplied by endpoint equality.

## Robust observability margin

Let \(d\) be the nominal separated detector-score direction, let \(W\) be an independently frozen positive metric, and let calibration and nuisance uncertainty be an admitted ball of radius \(\rho\). The worst-case completed Gram is

\[
\inf_{\delta^T W\delta\leq \rho^2}
(d+\delta)^T W(d+\delta)
=
\max\!\left(\sqrt{d^T Wd}-\rho,0\right)^2.
\]

Therefore the calibrated separator remains observable exactly when

\[
\rho<\sqrt{d^T Wd}.
\]

This is an uncertainty-stable separator gate. It is not a selector or a rigidifier: it certifies that one declared difference survives every admitted calibration completion.

## Exact falsifier

Take

\[
d=(1/4,-1/4),
\qquad
W=2I.
\]

Then \(d^T Wd=1/4\). If \(\rho=1/2\), the uncertainty ball contains \(-d\), so the completed Gram vanishes. If \(\rho=1/4\), its lower bound is \(1/16\).

The first case disproves any claim that nominal separation alone supplies robust response authority.

## Cross-sector consequence

The same architecture appears in three sectors:

- optics: a known reference phase enlarges the experiment and authorizes epoch transport;
- control: a known input changes an unobservable passive realization into an observable augmented realization;
- flavor: a source-derived score is operative only after an independently calibrated detector transport preserves a positive worst-case margin.

The durable rule is:

> A lost coordinate is not recovered by richer inspection of the quotient. It becomes observable only through an independently authorized source or interaction extension whose response survives the admitted uncertainty class.

