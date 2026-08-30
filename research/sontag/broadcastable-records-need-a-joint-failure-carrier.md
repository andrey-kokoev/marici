# Broadcastable Records Need a Joint Failure Carrier

## Question

Kitaev's no-broadcasting boundary identifies when a classical record label can
be copied. What additional structure is needed before several copies constitute
reliable redundancy for feedback or decision?

## Three equal-marginal noise models

Broadcast one correct bit to three consumers. In every model, each physical
copy has error probability

\[
p=1/10.
\]

Compare three joint disturbance laws.

**Independent flips.** Each copy flips independently. Majority vote fails with
probability

\[
3p^2(1-p)+p^3=7/250.
\]

**Common-mode flips.** With probability \(p\), all three copies flip together;
otherwise none flips. Every marginal error remains \(p\), but majority vote
fails with probability

\[
1/10.
\]

**Exclusive single flips.** With probability \(1/10\), exactly copy one flips;
similarly for copies two and three; with probability \(7/10\), none flips.
Again every marginal error is \(p\), but majority vote never fails.

Thus identical copy count and identical per-copy calibration support majority
error probabilities zero, \(7/250\), and \(1/10\).

## Agreement is not a common-mode monitor

The common-mode model makes all three records agree on every trial. It therefore
maximizes inter-copy agreement while retaining the largest majority error of
the three fixtures. Comparing copies with one another cannot detect a failure
that acts identically on all of them.

A common-mode claim requires a source-referenced audit channel or a physically
diverse realization whose disturbance coupling is independently constrained.
More copies on the same disturbance channel do not add observability in the
common-mode direction.

## Broadcastability versus redundancy

Exact broadcastability supplies a fanout constructor for a commutative label.
Reliable redundancy additionally needs:

- a joint failure process for all record carriers;
- transport and storage dynamics for each copy;
- common-cause and correlated-error coordinates;
- a decoder or voting Task;
- and a source-referenced calibration that identifies the relevant joint law.

The record algebra can be perfectly classical while its physical copies remain
perfectly correlated in failure.

## Control interpretation

Redundancy improves reliability only in disturbance directions transverse to
the voting kernel. A common-mode error lies in the diagonal subspace and passes
unchanged through majority vote. Exclusive single-copy errors lie in directions
that voting removes.

The marginal error vector is a projection of the joint disturbance Carrier.
It does not determine the probability mass assigned to decoder-failure regions.
Reliability must be evaluated over the full reachable joint error set or law.

## Cheapest discriminating records

Under a source-known calibration bit, pairwise error coincidences distinguish
the three exact fixtures:

- independent errors have pair probability \(1/100\);
- common-mode errors have pair probability \(1/10\);
- exclusive errors have pair probability zero.

Without source truth, pairwise copy disagreements still cannot expose an
all-copy flip. A calibrated reference, temporal checksum, or diverse physical
channel is required to identify that direction.

## Marici consequence

A broadcast record is not complete for multi-consumer control until the fanout
constructor is joined to a disturbance correspondence. The copied labels and
their error process form one capability witness. Treating three marginal
channels as a Cartesian product silently assumes independent reachability.

This is the same structural correction found in detector gain: covariance is
operative Carrier structure. Here it determines whether redundancy suppresses,
preserves, or completely avoids decision error.

## Verification boundary

The dependency-free checker enumerates all eight three-bit error patterns. It
verifies equal marginals, the three different majority-error probabilities,
pairwise coincidence rates, and the failure of agreement as a common-mode
diagnostic.

This is a finite classical record theorem. It does not quantify approximate
quantum broadcasting, storage lifetime, adversarial faults, or nonstationary
failure processes.

