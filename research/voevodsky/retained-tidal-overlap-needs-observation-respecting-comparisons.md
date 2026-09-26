# Retained tidal overlap needs observation-respecting comparisons

## Result

Fresh resume selected `retained-local-tidal-overlap-comparison:v1`.
The local Newtonian/Rosen overlap is now an actual retained boundary comparison
using the owner's complete-package, native-rule and native-history interfaces.
Both source records, their calibration contexts and analytic evidence references
remain attached. A common electric reading does not identify those source records.

A sharper hostile is also checked: an unrestricted **isometric equivalence** can
align the refined marked values while violating the calibrated gradient reading.
Thus neither bare carrier equivalence nor metric control selects the physically
admissible comparison. Named observations and calibration must commute with it.

## 1. Actual retained comparison

`agda/RetainedLocalTidalOverlap.agda` declares two distinct source signatures:

- the preceding NEW Newtonian pair, masses 36 and 18 at radius 12 along x and z;
- the exact cosh/cos Rosen wave with a=1/4.

It retains the preceding affine/free-fall calibration and Newtonian local Taylor
bound; on the wave side it retains the proper-clock factor, controlled source
interval, and epsilon=h^4, sigma=h^8 radar-limit interpretation. The common
profile fixes nonrotating xyz axes, the corner electric reading and denominator
13824=8*1728. The limit route is not relabelled as equality of the frozen finite Y.

The electric payload is diag(-432,432,0) over that denominator. The source-side
Newtonian Hessian and actual independent native jet-row reading are compared.
On the Rosen side the analytic corner reading is supplied from the prior source
derivation; this turn does not introduce a formal native Einstein PDE solver.

Using `BoundaryGeneratedQuestions.Filler` and `WholePackageResolution.compare-rule`,
the module constructs the marked identity comparison over this electric payload.
It then constructs the corresponding native rule directly from the actual native
packages, using `NativeTableRules.compare-kind`. Only admission evidence is
transported; the native operation and Newtonian readout are not computed by
calling a legacy decoder.

`NativeTableResolution.ForOldSeeds` supplies the actual retained histories.
Both the encoded source closure and the directly constructed native closure have
checked recovery laws. Header equalities expose the retained source packet and
observation profile in the actual native nodes.

This is a boundary witness OVER a common reading. It is not an equivalence of
the physical source spaces. The two source records are provably unequal in their
fixed, tagged source signature. We do not infer that every possible unmarked
universe-level relabelling of carrier encodings is impossible.

## 2. Evidence boundary is explicit

The main construction is parameterized by an admission-evidence family indexed
by sector and source declaration. It never manufactures an inhabitant of that
family. Stronger independently verified source evidence can instantiate the same
construction later.

The concrete instance retains selected-declaration equality and an analytic
reference containing path, SHA-256 digest and claim scope. The referenced file is
`source-anchored-tidal-overlap-is-local-and-stops-at-the-next-jet.md`, digest
`9e7fb956af22885ab81855b752c2f786af67dcd92ac6584908b14fee856cca80`.

**A citation is not a compiler proof of continuum physics.** The potential,
vacuum metric, covariant gradient and controlled limit arguments remain written
mathematics. The formal result is the finite comparison, source/reference
retention, rule/history integration and obstruction conditional on the supplied
interpretation. The exact audit checks that the retained reference is current.
The new literal seed policy is our explicit integration policy, not adoption by
the owner's original fixed-source policy. No owner artifact is modified.

## 3. A genuine refinement obstruction

Extend the reading from E to

    (E, g), where g=partial_x E_xx

in the declared parallel/nonrotating frame. The preceding physical derivation
supplies g_Newtonian=-1/96 and g_wave=0. Over denominator 13824 these are -144
and 0. Hence

    fine_Newtonian=(E,-144), fine_wave=(E,0).

Agda proves that no function of the shared E alone recovers g on both selected
sources. It also proves that no equivalence preserving the calibrated gradient
channel can send fine_Newtonian to fine_wave. In particular there is no lift of
the coarse identity comparison that preserves both named channels.

This does not require throwing away either source or its retained history.
Refining the observation profile filters admissible comparisons, not the
underlying source declarations.

## 4. Why “no refined filler exists” would be false

The owner's unrestricted filler type permits any pointed type equivalence.
Consider the concrete map on Tensor x Integer:

    e(T,g)=(T,g+144), inverse(T,g)=(T,g-144).

The module proves its inverse laws and constructs an actual unrestricted
`BoundaryGeneratedQuestions.Filler` between the refined packages. It preserves
the entire electric projection and sends (E,-144) to (E,0).

Moreover,

    (g+144)-(h+144)=g-h.

This identity is proved for arbitrary integer variables. Since the tensor
components are unchanged, e is an isometry for the independently specified
fixed-coordinate maximum norm, as well as for other translation-invariant
product norms. Metric completion or uniformity does not exclude it.

But it does NOT preserve the calibrated gradient reading: its value at the
Newtonian marked input changes from -144 to 0. The profile fixes the physical
zero and units of this observable; no such offset was supplied as a legitimate
change of calibration. Thus this filler is inadmissible for that profile.

This is not an intra-carrier collapse: e remains injective and maps two distinct
inputs to two distinct outputs. The failure is false physical alignment between
marked source and target observations when calibration compatibility is omitted.

## 5. What has been proved

Compiler-checked:

- retained source-record distinction in the fixed signature;
- actual Newtonian native-package comparison and metadata headers;
- source and directly constructed native comparison histories, with recovery;
- no factorization of g through the common electric reading;
- no gradient-preserving marked refinement;
- the unrestricted refined filler and its inverse/difference-preservation laws.

The generic observation-preserving boundary calculus is the next leaf; this turn
proves the concrete example and hostile rather than claiming a new universal
physical foundation or a completed metric theory.

Verification:

    python research/voevodsky/check_native_radar_formal.py --retained-overlap --fresh
    python research/voevodsky/check_retained_local_tidal_overlap.py

Fresh safe/cubical closure passes. Two controls reject source-record erasure and
false gradient preservation for the intended type mismatches. The exact audit
passes 56 checks, including the retained reference digest, source/normalization
metadata and finite isometry controls. Universal algebraic and obstruction
claims rely on the formal proofs, not those finite probes.

Receipts: `retained-local-tidal-overlap-formal.json` and
`retained-local-tidal-overlap.json`.

## Successor

Extract an observation-respecting predicate on the ACTUAL boundary fillers and
native comparison rules. Prove closure under identity, inverse and composition,
and show that adding observations restricts the allowable comparison space.
Retain the unrestricted isometric hostile as a rejection control. Keep supplied
source admission and uniform completion bounds as separate obligations; neither
is derived merely by adding this compatibility predicate.
