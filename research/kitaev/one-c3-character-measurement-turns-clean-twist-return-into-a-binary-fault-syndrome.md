# One `C3` character measurement turns clean twist return into a binary fault syndrome

Owner: `marici.Kitaev`

## Bounded question

Can the two conjugate cube-root dark conditions be measured on one
three-branch return packet without a two-setting stationarity assumption?

Yes at the level of an exact instrument target. The full three-outcome `C3`
character PVM measures the accepted character line and both orthogonal dark
characters in one setting. Coarse-graining the two rejecting outcomes gives a
single fault bit. Its probability is exactly a sum of pairwise environment
mismatches.

The existing localized `D(S3)` charge packet supplies this character projector
algebraically inside the three-cycle centralizer. It does not yet supply the
physical incidence from a path register into that centralizer coordinate or a
clean controlled measurement.

## Twisted path-return state

Let the path register have basis

\[
|0\rangle,\qquad |1\rangle,\qquad |2\rangle.
\]

After zero, one, and two `G` twists, write the joint return state as

\[
|\Phi\rangle
=
{1\over\sqrt3}
\left(
|0\rangle|\eta_0\rangle
+\omega|1\rangle|\eta_1\rangle
+\omega^2|2\rangle|\eta_2\rangle
\right).
\]

Every unobserved controller, motion, ribbon, loss-flag, and environmental
degree belongs inside the vectors `eta_j`.

The ideal path character is

\[
|v\rangle
=
{1\over\sqrt3}
\left(
|0\rangle+\omega|1\rangle+\omega^2|2\rangle
\right).
\]

Define the accepted effect

\[
P_{\rm acc}=|v\rangle\langle v|\otimes I
\]

and its binary complement

\[
P_{\rm fault}=I-P_{\rm acc}.
\]

## Exact cleanliness theorem

Projection onto the accepted character gives

\[
(\langle v|\otimes I)|\Phi\rangle
=
{1\over3}
\left(
|\eta_0\rangle+|\eta_1\rangle+|\eta_2\rangle
\right).
\]

Therefore

\[
p_{\rm fault}
=
\langle\Phi|P_{\rm fault}|\Phi\rangle
=
{1\over3}\sum_{j=0}^2\|\eta_j\|^2
-{1\over9}
\left\|
\eta_0+\eta_1+\eta_2
\right\|^2.
\]

The polarization identity rewrites this as

\[
p_{\rm fault}
=
{1\over9}
\sum_{0\le j<k\le2}
\|\eta_j-\eta_k\|^2.
\]

Consequently,

\[
p_{\rm fault}=0
\]

holds exactly when

\[
\eta_0=\eta_1=\eta_2.
\]

This is stronger than the preceding two-setting formulation. Both nontrivial
dark characters are tested as the orthogonal complement of one accepted
character line in a single PVM.

## One bit detects; three outcomes diagnose

The full `C3` Fourier measurement has three character outcomes. One is the
declared twisted return character. The other two span its orthogonal
complement.

For the yes-or-no question of clean return, a binary record is sufficient:

- accepted character;
- any orthogonal character.

Retaining all three outcomes supplies additional diagnosis by identifying
which Fourier component caught the mismatch. It is not required for exact
fault detection.

Thus the minimal classical record dimension is two even though the coherent
effect is built from a three-character algebra.

This does not contradict the eight-outcome endpoint charge measurement. The
binary record is a coarse-graining for one declared `G`-twist calibration
task, not a complete charge label.

## Why this removes the setting-drift loophole

The earlier pair of equations could be estimated in two different analysis
settings and then incorrectly combined across two different branch maps.

Here one fixed PVM contains both rejecting character directions. A single
application acts on one joint state `Phi`. Repetition is needed only to
estimate a probability, as for any nondeterministic quantum measurement; no
switch between conjugate analyzer settings is required.

Time-varying drift between repetitions can still corrupt statistical
interpretation. It cannot be disguised as an exact algebraic consequence of
two separately chosen rows. The remaining assumption is ordinary instrument
stationarity or a declared adversarial confidence model, not equality between
two different settings.

## Relation to the localized `D(S3)` charge PVM

For three-cycle flux, the centralizer is `C3`. Its three irreducible character
projectors are the localized sectors `F,G,H`. The nonreal projectors require
the same coherent cube-root weights appearing in `P_acc`.

This supplies an exact algebraic template:

1. represent the three path labels as the regular `C3` module;
2. identify the declared twisted path character with `G` or `H`;
3. apply the centralizer character PVM;
4. coarse-grain the other two labels into the fault outcome;
5. erase every Fourier-index and conjugating-frame workspace.

Step one is an incidence map, not an automatic identity. The physical path
register and the localized three-cycle centralizer degree are different
systems until a source-derived coupling identifies their `C3` actions.

The existing charge-measurement packet explicitly leaves conditional
centralizer Fourier transforms and garbage uncomputation uncompiled. It
therefore authorizes the operator target but not this apparatus.

## Common-mode character-frame fault

Suppose a diagonal path transformation `D` rotates both the prepared character
line and the measurement projector:

\[
|v\rangle\longmapsto D|v\rangle,
\qquad
P_{\rm acc}\longmapsto
D P_{\rm acc}D^\dagger.
\]

The binary syndrome remains identically accepted. Thus the instrument can
certify internal path cleanliness while being wrong about the externally
declared character frame.

In particular, simultaneous `G/H` conjugation exchanges the two nonreal
characters but leaves the clean-return verdict unchanged. This is harmless
for Gram-rank certification and harmful for signed logical-phase
identification.

An independent ribbon-orientation or character-frame anchor is required only
for the latter claim.

## Trace-completeness boundary

The quantitative identity assumes the vectors `eta_j` inhabit the complete
output dilation. If loss is omitted and only successful returns are
postselected, the measured probability becomes conditional and can vanish
while branch-dependent loss remains.

The apparatus must either:

- include all loss flags inside the PVM domain;
- or record total success probability as an independent output.

An unobserved loss port is an additional dark kernel, not a harmless
normalization.

## Source-level two-cell interpretation

The character projector compares the three labelled routes before their
amplitudes are collapsed to one scalar total. The rejection space records the
failure of those routes to close on one common environment vector.

After scalar aggregation, the distinction can disappear through cube-root
cancellation. The character PVM is therefore a finite source-level comparison
cell rather than another terminal scalar evaluation.

This is structurally parallel to any programme in which two route orders
commute after scalarization but may differ before typed boundary currents are
aggregated. The parallel supplies a diagnostic form, not authority to identify
the underlying coefficient systems.

## Exact falsifiers

- Two conjugate analyzer settings claimed necessary after the full `C3` PVM is
  admitted.
- A one-bit record claimed too small for clean-return detection.
- The quantitative pairwise-mismatch identity failing.
- A path register identified with the local centralizer module without an
  incidence map.
- Algebraic existence of `Q_G,Q_H` promoted to a controlled Fourier
  measurement.
- Hidden Fourier or frame garbage called coherent erasure.
- Internal character consistency promoted to absolute `G/H` orientation.
- Postselected acceptance promoted to trace-complete clean return.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies the three-route return packet, accepted line
versus rejecting complement, binary syndrome, pairwise mismatch energy,
incidence boundary, and garbage ports.

The quantum coefficient lens supplies the `C3` regular module, cube-root
character line, `F/G/H` charge projectors, Fourier measurement, and ribbon
conjugation.

## Result

One `C3` character PVM turns the clean controlled-twist condition into a
single-setting binary fault syndrome. Its rejection probability is exactly
one ninth of the total pairwise return mismatch. This removes the conjugate
setting-typing problem while preserving the physical constructor boundary:
the path-to-centralizer incidence, coherent Fourier extraction, and garbage
erasure remain unproved.

No build or checker was run for this research-only packet.
