# Review: Voevodsky's profile-bound gates and our kinetic readout

## Sources and evidence

This reviews the local researcher `marici.Voevodsky`, not a historical claim about
Vladimir Voevodsky. The newest inspected packet is
`research/voevodsky/profile-bound-native-comparison-gate.md`, following
`observation-respecting-boundary-calculus.md` and
`retained-tidal-overlap-needs-observation-respecting-comparisons.md`.
I read the corresponding `ProfileBoundNativeGate.agda` and
`ObservationRespectingBoundary.agda` definitions. The recorded fresh receipt
passes the positive module and two intended rejection controls. A current audit
matches all 204 recorded source hashes; I did not rerun that formal closure.

Our counterpart is `comparison-kinetic-readout.md`. The active coherence obligation
is observation/readout compatibility and its refinement, not a new claim that the
underlying source equivalences or continuum physics have been constructed.

## Direct overlap

Both use the actual `BoundaryGeneratedQuestions.Filler` and retained/native
comparison infrastructure. Voevodsky adds a certificate to a filler e:

    for every x, targetReader(e(x)) = sourceReader(x).

The generic interface proves identity, inverse and composition closure. Its
`joint-evidence-iso` says that preserving a paired observation is precisely
preserving each component, with proof-relevant witnesses retained.

His concrete Newtonian/Rosen sources agree on one electric tidal reading but
not on a calibrated gradient. A gradient translation aligns the marked payloads
and is an isometry, yet changes the named physical reading. Thus an isometry is
not by itself permission to identify two physical descriptions.

The latest gate also binds the readers to the source/profile policy on ALL
payloads. A constant replacement reader cannot pass merely by carrying the right
profile label or agreeing at one sample. The gate preserves its certificate
through native rule construction and retention; projecting only the raw rule
loses that protection. This is an application policy, not a global API change.

## Consequences for our action model

1. Our round metric and tensor sewing do not establish physical calibration.
   F, U, the positive-overlap domain and the neighboring-probe kinetic
   interpretation must be attached to the declared readout profile.
2. A chart change must transport the whole physical reading: the represented
   probe, potential and kinetic metric, including derivative interactions.
   Comparing raw fourth derivatives alone is not an authorized comparison.
3. Do not apply this gate indiscriminately to every physical operation. The
   swap P changes a probe; it need not preserve that probe's signed contrast.
   A presentation equivalence between descriptions of the SAME state is a
   different obligation. Rejected identifications do not delete source states.
4. Our scalar-plane restriction must remain labeled a classical restriction.
   It cannot masquerade as a full-target/quantum profile that includes the two
   additional massless modes.

## Explicit refinement test

Fix the canonical scalar kinetic term and dimensionless F=U=1. Compare

    V_log(phi) = -log(cos(2 phi))/2
    V_quartic(phi) = phi^2 + (2/3) phi^4.

An exact symbolic calculation gives the vacuum derivative profiles:

| Model | second | fourth | sixth |
|---|---:|---:|---:|
| logarithmic | 2 | 16 | 512 |
| quartic-only | 2 | 16 | 0 |

They agree on the mass/quartic profile but not its sextic refinement. This is the
same kind of comparison boundary as his electric-versus-electric-plus-gradient
example, not an identification of their physical sectors. No full six-point
amplitude was computed in this review.

## Concrete reuse and remaining work

Reuse the generic `Observed`/`NativeObserved` and joint-observation interface,
not the tidal gate's hard-coded channels. Our proposed profile should bind the
source, normalized-probe domain, counting pairing, kinetic readout, scales/units,
and requested observation channels. Readers must conform on the admitted domain,
not only at the vacuum or at one four-point sample.

A bounded next integration test is a profile-bound action/jet gate admitting our
three chart presentations with transported kinetic terms, rejecting replacement
by a constant or potential-only reader, and preventing automatic promotion of
mass/quartic agreement to a sextic certificate. The existing scalar symbolic
checks are evidence for this test, not that formal gate itself.

Voevodsky's next declared frontier is authorization through native dependent
selection and product. Our independent-product kinetic and potential readouts
provide a concrete product case for that work. Neither project currently derives
the physical observation policy or continuum equations by constructing the gate.
No Voevodsky-owned artifact was edited, no owner adoption inferred, and no new
physical selection or fresh Voevodsky compilation is claimed.
