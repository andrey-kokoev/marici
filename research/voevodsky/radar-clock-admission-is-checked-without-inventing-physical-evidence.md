# Finite radar clock admission is checked without inventing physical evidence

## Result and fresh leaf

Fresh resume selected `formal-radar-clock-admission:v1`.
The finite part of admission is now a concrete Agda certificate, not an opaque
predicate or source-name string. The certificate is inhabited for the static
reference and for the retained rounded wave and moving-flat packets, with their
actual receipt enclosures. A fresh safe/cubical closure check passes.

This is deliberately NOT a proof that an arbitrary enclosed clock record arises
from null rays. Finite admissibility and physical realization are separate types.
The stronger physical admission policy is their dependent pair; it is not replaced
by the weaker finite policy.

## Concrete certificate

`agda/RadarClockAdmission.agda` defines `ClockCertificate k r`, where r contains
all nine integer clock pairs and the proper-time tick denominator is D=suc k.
Its retained data and equality witnesses assert:

1. Calibration equals the declared fixed protocol: the actual probe vectors,
   epsilon=1/32, proper-time step 1/4, center 1, proper-clock/c=1 convention,
   and instantaneous return.
2. D=4*q for a retained quarter-tick count q. Emission ticks are respectively
   3q,4q,5q at the three sample times.
3. Each reception tick a equals its emission tick plus suc lag. This establishes
   strictly future reception, not merely nonnegative or unsigned time difference.
4. For positive refinement B=suc refinement, each enclosure has integer bounds
   l,u in units 1/(D*B). Natural witnesses satisfy

       l+below=B*a,
       B*a+above=u,
       u=l+width,
       width+slack=W.

   Thus the recorded arrival lies inside the supplied interval and its width is
   at most the declared common budget W. Nonnegative natural differences encode
   the required order relations without accepting a Boolean assertion as proof.

Every equation is checked by Agda. The total function type Time -> Direction ->
ClockPair supplies the complete nine-slot domain; the existing native interface
retains its selected rows, identifiers and witness values.

A claimed budget need not be experimentally useful merely because it is valid.
This certificate checks the claim against the retained interval data; it does
not invent an accuracy specification or derive an instrument noise floor.

## Realized finite instances and source alignment

The static reference has D=32, emission ticks 24,32,40, and round-trip tick
increments 6,8,10 along x3,y4,xy5. It has exact singleton enclosures and W=0.
Its physical interpretation is the earlier independently supplied Minkowski
solution, not a consequence of this finite arithmetic proof.

`generate_radar_clock_certificates.py` extracts exact rational data from the
previous physical receipt and emits `agda/RadarClockPhysicalCertificates.agda`.
Generation is not acceptance: the compiler then checks every generated equality.
An independent audit parses its numeric declarations and compares all 18 clock
pairs and enclosure endpoints with the source receipt.

Both nontrivial certificates use D=2^80 and B=1:

| Packet | Width budget W in these ticks |
|---|---:|
| Initially-resting cosh/cos vacuum wave | 1,719,544,332 |
| Moving isotropic flat control | 12 |

These are the actual interval widths inherited from the rational enclosure
calculation. They are not experimentally estimated timing errors.

If an ideal reception time lies in its supplied interval, its discrepancy from
the recorded reception is at most W/(D*B), hence the radar-distance discrepancy
is at most W/(2*D*B). This conservative bound uses the full interval width; it
does not assume a midpoint property not present in the certificate.

The italicized logical condition matters: the finite certificate proves that
the RECORD lies in the interval. Membership of the IDEAL NULL-RAY ARRIVAL is
still supplied by the prior analytic/rational enclosure argument, not by a
hash, a source label, or this Agda datatype. The real-valued error consequence
is stated mathematically here; it is not newly formalized as a real-analysis
result in this module.

## Instantiation of native retained resolution

`FiniteChecked k r certificate` instantiates the existing formal
`NativeRadarReadout.Admitted` module with the concrete `ClockCertificate` policy.
It re-exposes the actual retained-readout comparison, marked radar reading and
history-recovery theorem. The static reference supplies a closed nonempty
instance; the universal module applies to the compiled wave and moving-control
certificate values as well.

For physical authorization, `WithPhysical` instead takes a separately supplied
predicate

    Physical : (k : Nat) (r : Rows) -> ClockCertificate k r -> Type

and defines admission as

    Sigma (ClockCertificate k r) (Physical k r).

Its native integration requires BOTH witnesses and retains their pair. There
is no function manufacturing the second witness from finite certificate data.
No stronger original source policy is silently transported into a weaker one.

The analytic vacuum and ray witnesses remain external mathematical evidence.
Their earlier source hashes identify what was read and checked; hashes are not
inhabitants of the stronger physical proposition. Owner adoption of these new
integration files is not inferred, and no owner artifact was changed.

## Verification

Run:

    python research/voevodsky/generate_radar_clock_certificates.py
    python research/voevodsky/check_native_radar_formal.py --admission --fresh
    python research/voevodsky/check_radar_clock_admission.py

The positive root `RadarClockPhysicalCertificates` passes a fresh
`--safe --cubical --guardedness --ignore-interfaces` check in private snapshots,
including the actual native package/resolution dependencies.

Seven negative roots reject with the expected `UnequalTerms` diagnostics:

- two prior controls: erased readout port and erased retained evidence;
- wrong quarter-clock grid: 32 != 28;
- genuinely past reception (23 after an emission of 24): positive-delay claim
  would require 23=25;
- false lower-enclosure inclusion arithmetic: 31 != 30;
- changed baseline calibration: 16 != 32;
- falsely zero wave width budget: 1,719,544,332 != 0.

The source-alignment audit passes 83 checks, including current compiled source
hashes, generated-file linkage, exact clocks/enclosures, causal gaps and budgets.
These controls supplement the formal type checking; they do not derive physical
realizability by sampling.

Receipts:

- `radar-clock-certificate-generation.json`;
- `radar-clock-admission-formal.json`;
- `radar-clock-admission-audit.json`.

## Disposition and next gate

The selected finite clock-admission leaf is resolved. The abstract interface now
has a useful, mechanically inhabited finite component and an explicit separate
physical-evidence boundary.

The next nonredundant task is output uncertainty: propagate admitted input
intervals through the nonlinear square and linear native reading to a checked
output enclosure or error bound, retaining normalization and calibration.
The premise that ideal arrivals lie in the input intervals must remain explicit;
finite propagation must not be advertised as a new proof of null-ray enclosure
soundness or of physical-law selection.
