# Acyclic Stabilization RG-Descent No-Go

## Question

Can a single quiver or chain complex make the WP820 charge selector and the
WP821 matter-spectrum RG data one unavoidable source object?

## WP820 as an integer complex

The WP820 boundary map is

\[
B=
\begin{pmatrix}
2&-1&0\\
3&0&-1
\end{pmatrix}
:\mathbb Z^3\longrightarrow\mathbb Z^2.
\]

It has primitive kernel \(\mathbb Z(1,2,3)^T\) and trivial cokernel. This
correctly carries the relative charge ray selected by oriented inflow.

It is not an ordinary directed-graph incidence matrix: its columns do not sum
to zero and it contains entries of magnitude greater than one. Realizing it as
a quiver therefore already requires weighted arrows, auxiliary nodes, a
higher-cell complex, or a factorization. Those choices are not unique.

## Acyclic stabilization

Add the unit contractible complex

\[
K:\mathbb Z\xrightarrow{1}\mathbb Z
\]

and form

\[
B'=B\oplus(1).
\]

The stabilized complex has the same primitive kernel and trivial cokernel:

\[
\ker B'=\mathbb Z(1,2,3,0)^T.
\]

Thus \(B\) and \(B'\) have identical charge homology and support the same
oriented inflow record.

At the physical matter level, the acyclic sector can carry a massive
vectorlike pair of charges \((r,-r)\). It contributes

\[
r+(-r)=0,
\qquad
r^3+(-r)^3=0
\]

to the linear and cubic anomalies, but contributes

\[
r^2+(-r)^2=2r^2
\]

to quadratic loop indices. Topological anomaly data is blind to precisely the
matter that changes RG flow.

## Failure of RG descent

Use the WP821 conditional coefficient packet with
\(a=b=d=f=1\). Its gauge fixed coordinate is

\[
x_*=\frac1{c-1}.
\]

For the unstabilized packet \(c=3\), \(x_*=1/2\). If the vectorlike pair
shifts \(c\) by \(2r^2\), then

\[
x_*'(r)=\frac1{2+2r^2}.
\]

The unit pair gives \(x_*'=1/4\), and different integer \(r\) give an infinite
family of anomaly- and homology-equivalent fixed-point magnitudes.

Therefore the RG assignment is not a function of charge homology. The first
nonfaithful arrow is

\[
\text{full chain-level matter complex}
\longrightarrow
\text{charge homology and inflow}.
\]

The portal sign and primitive charge survive this projection; its magnitude
and basin do not.

## Minimality is not a harmless quotient

One might demand a minimal complex and delete every contractible summand. But
a physically populated acyclic sector has a gauge-invariant mass and produces
threshold corrections. Quotienting it away preserves homology while erasing
real scattering and decoupling data. Chain minimality is therefore not
physical equivalence unless an independent source law forbids or removes the
sector.

The relevant mass is a free deformation. Above the unit-pair threshold the
conditional fixed coordinate is \(1/4\); below it the reduced packet returns
to \(1/2\). Anomaly matching remains exact on both sides.

## Contextual probes and instrument

A low-energy topological probe sees the same primitive charge and inflow for
\(B\) and \(B'\). A threshold-sensitive probe can distinguish them in
principle, but it must resolve the heavy pair and calibrate its response. A
record of the threshold jump still has a source–gain ambiguity without such
calibration. No physical16 descent is present.

## Aspect germ audit

The native germ must retain the full complex, acyclic sector, oriented inflow,
mediator, three flavor operators, and threshold detector. Passing to homology
before forming the RG and threshold response fails the fiber gate. The
chain-level matter constructor, exclusion or selection of acyclic sectors,
threshold mass, physical16 map, and detector calibration are all missing.

## Classification and falsifiers

Homology plus inflow is a genuine selector of primitive oriented charge, but
not of the full matter spectrum or portal magnitude.

The smallest exact hostile pair is

\[
B
\quad\text{and}\quad
B\oplus(1),
\]

which have the same charge homology while giving conditional fixed coordinates
\(1/2\) and \(1/4\). The vectorlike charge pair \((1,-1)\) is the smallest
anomaly-neutral loop-index changer.

## Deutschian appraisal

The desired source cannot be merely a homology class, anomaly polynomial, or
minimal presentation. It must explain the complete chain-level matter object,
including why no physically active acyclic sectors are present—or predict
their masses and threshold records.

The sharper successor is a source principle of spectral completeness:
the oriented complex must be the full finite spectral object, with a
source-derived action assigning masses and kinetic normalizations to every
contractible sector. Only then can RG and threshold response be functorial.
That full spectrum must subsequently be connected to a calibrated physical16
instrument.

## Disposition

Negative descent theorem. Acyclic stabilization preserves WP820's topological
selector while changing WP821's RG magnitude and thresholds. The unified
source must live before the homology quotient.
