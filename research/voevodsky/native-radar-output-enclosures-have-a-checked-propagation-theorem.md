# Native radar output enclosures have a checked propagation theorem

## Result and fresh leaf

Fresh resume selected `formal-radar-output-enclosure:v1`.
A safe/cubical Agda theorem now propagates input delay intervals through the
nonlinear squares, native temporal/polarization expression and signed output
scaling. It is a universal conditional enclosure theorem, not a finite-corner
inference. A concrete integer coefficient model is checked and its expression
is definitionally equal to the existing native numerator reading.

The two retained physical-example packets also have compiled delay-shift
certificates and exact rational output endpoint evaluations. Their diagonal
output intervals still exclude zero. The premise that ideal arrivals belong
to the supplied input intervals remains external analytic evidence.

## What is formally proved

`agda/RadarOutputEnclosure.agda` defines a minimal ordered-arithmetic interface:
order reflexivity/transitivity, addition monotonicity, order reversal under
negation, multiplication monotonicity by nonnegative factors, and nonnegative
interpretations of natural coefficients. It does NOT assume the desired
readout-bound theorem as a field.

For an interval i=[l,u], membership means l<=x and x<=u. The compiler checks
soundness of:

    [l,u]+[a,b] = [l+a,u+b],
    -[l,u] = [-u,-l],
    c[l,u] = [cl,cu] for c>=0,
    square([l,u]) = [l^2,u^2] provided l>=0.

The last rule is derived using multiplication monotonicity twice on each side.
It is not used on a zero-crossing interval.

A small expression syntax independently represents the existing native
numerator reading: a cell squares one delay, followed by addition, negation
and nonnegative integer scaling. Structural induction proves

    sound : input-membership + nonnegative-input-lowers
         -> output-membership.

The expression has the original coefficients 16,6,9 and temporal weights
1,-2,1. There is no legacy decoder or call to an assumed interval oracle.
`output-sound` additionally handles a nonnegative scale alpha and the outer
minus sign, exchanging endpoints correctly.

An actual instance for Cubical integers is provided. Its multiplication and
addition order laws come from the library; negation reversal is derived using
its order laws and checked ring identities. For every integer clock record r,

    eval(native-expr component, clock-delay r)
      = NativeRadarReadout.native-read r component

is checked componentwise by refl. Thus this expression is linked to the prior
native package reading rather than being an unrelated interval example.

## Connection to the admitted clock intervals

The previous clock certificate stores absolute reception bounds in units
1/(D*B), with D=suc k and B=suc refinement. This turn adds a `DelayCertificate`
that retains natural lower and upper delay counts and proves

    absolute_lower = B*emission_ticks + low_delay,
    absolute_upper = B*emission_ticks + high_delay.

This is an additional positivity gate. Future RECORDED reception alone does
not imply that the entire supplied interval lies after emission.

`agda/RadarOutputPhysicalCertificates.agda` contains generated instances for
both existing packets. The compiler checks their exact shift equations against
the already compiled clock certificates. `CertifiedBounds` then specializes the
integer enclosure theorem to those nonnegative delay boxes, still requiring
membership of whichever input values are to be bounded.

The generator is not trusted as proof acceptance. A separate audit parses its
numeric declarations and checks their agreement with the physical receipt.
Compilation supplies the arithmetic proof; hashes only identify the evidence.

## Normalization and its precise formal boundary

For delays measured in units 1/(D*B), write N for the integer-polynomial native
numerator. The physical reading is

    Y=-alpha*N, alpha=2048/[144*(D*B)^2] > 0.

The generic ordered-arithmetic theorem proves interval propagation for any
nonnegative alpha in its coefficient model, including the necessary reversal
under the outer minus sign. The concrete integer specialization proves the
signed numerator enclosure; integers themselves do not supply arbitrary
positive reciprocals.

For the current physical cases B=1, Python Fraction evaluation applies the
EXACT positive rational alpha and checks the result against the earlier
protocol implementation. This is not a freshly compiled rational/real-number
instance of `OrderedArithmetic`. Interpreting the generic theorem over ordinary
real arithmetic is mathematically justified by those standard order laws, but
the concrete real model and reciprocal normalization have NOT been instantiated
inside this Agda development.

Likewise, the general fine-grid theorem bounds the expression in its declared
fine-grid units. All compiled physical fixtures here have B=1. A formal claim
of invariance between different refinements B requires an explicit homogeneity
and normalization comparison, not just changing a denominator annotation.

These boundaries prevent a conditional coefficient-model theorem from being
reported as a complete formal real-analysis pipeline.

## Exact physical-example endpoint evaluation

`check_radar_output_enclosure.py` evaluates the certified delay boxes with exact
Fraction arithmetic, the same expression and the same normalization. It then
independently evaluates the original time-first protocol on all 512 endpoint
choices for each packet. Every corner is contained; each component's box extrema
are attained. This checks the endpoint implementation and its signs, not the
universal theorem (which is proved by induction).

Rounded displays of the resulting intervals are:

| Source | Y_11 | Y_22 |
|---|---|---|
| Initially-resting vacuum wave | [-0.0339685665926341, -0.0339685665923584] | [0.0284243270561017, 0.0284243270563336] |
| Moving flat control | approximately -0.0323053641577086 | approximately -0.0326659977837677 |

The receipt stores exact rational endpoints, including the much narrower flat
control intervals and the off-diagonal components. All component widths are
below 1e-10. Rounded native readings are inside their intervals. The intervals
also overlap the previous independent analytic-response enclosures.

Zero remains excluded from both diagonals in both cases, with opposite Y_22
signs between the wave and flat moving control. Conditional output uncertainty
therefore does not erase the earlier physical distinction. It still does not
make Y a pointwise curvature tensor: the moving control has zero curvature.

The 1,024 endpoint records are synthetic interval controls, not 1,024 newly
realized vacuum experiments or a stochastic noise model.

## Verification

Run:

    python research/voevodsky/generate_radar_output_certificates.py
    python research/voevodsky/check_native_radar_formal.py --output --fresh
    python research/voevodsky/check_radar_output_enclosure.py

The fresh positive root `RadarOutputPhysicalCertificates` checks the generic
ordered-arithmetic proof, integer instance, actual native-expression equality,
clock certificates and physical-packet delay shifts in isolated snapshots.
Owner/library originals remain unchanged.

Ten intended rejection controls pass: the seven previous clock/provenance
controls, plus rejection of a zero-crossing square shortcut, failure to reverse
endpoints under negation, and substitution of a false zero lower delay for an
actual source bound. The endpoint/source audit passes 26 checks, covering all
1,024 synthetic corners.

Receipts:

- `radar-output-certificate-generation.json`;
- `radar-output-enclosure-formal.json`;
- `radar-output-enclosure-audit.json`.

## Disposition and next gate

The output-propagation leaf is resolved in the scope above: a checked universal
ordered-arithmetic theorem, checked integer/native specialization, certified
input shifts and exact rational endpoint controls for both physical examples.

Next: provide a concrete ordered rational coefficient interpretation and prove
reciprocal normalization/refinement invariance in the formal development.
Keep that finite coefficient task separate from soundness of the ideal null-ray
input enclosures and from a full real-number completion theorem.
