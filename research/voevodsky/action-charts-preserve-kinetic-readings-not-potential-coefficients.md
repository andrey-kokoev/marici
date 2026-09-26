# Action charts preserve kinetic readings, not potential coefficients

## Selection and result

The operator redirected the next synthesis test from general constructor
propagation to Nima's three chart presentations of one conditional scalar action.
Fresh graph resume still selected `construction-observation-compatibility:v2`;
the general constructor task is deferred, not declared solved by this example.
Nima's message at sequence 15615 independently proposed this integration and
identified its physical-scope limitations.

**Positive result:** there are nonidentity, invertible coefficient-jet comparisons
between the angle, ratio and sine charts that preserve the calibrated mass and
on-shell quartic reading. Their potential quartic coefficients do NOT agree.
The kinetic terms must transform too. This is a concrete use of our generic
observed/native boundary interface, rather than another identity-on-payload gate.

A further symbolic calculation gives a sixth-order canonical reader. It agrees
in all three charts for the logarithmic model and distinguishes that model from
its quartic truncation, despite identical mass/quartic readings.

## Same state, different charts

We retain Nima's actual pointed source swap, not an invented substitute source.
Its normalized scalar-plane probe has counting overlap cos(2 theta). With the
supplied neighboring-probe kinetic prescription,

    L = F^2/2 (d theta)^2 - U [-log(cos(2 theta))/2], F,U>0.

Compare theta, u=tan(theta), z=sin(theta), on the positive-overlap branch:

    |theta|<pi/4, |u|<1, |z|<1/sqrt(2).

For the physical chart variable v=F times the chosen coordinate, the maps to the
canonical angle field are v, F atan(v/F), and F asin(v/F). They are increasing
local diffeomorphisms on these domains. Independent probe formulas agree after
these maps. The pulled-back kinetic metrics are respectively

    1, (1+(v/F)^2)^(-2), (1-(v/F)^2)^(-1).

The symbolic checker constructs norm, overlap and metric from the probe vectors
and the owner's recorded actual swap images. It checks state agreement and the
kinetic pullback identity, not just equality of three selected output numbers.

This is a presentation change of the SAME state. It does not require the source
operation P, which can change a probe, to preserve every signed state reading.

## Actual boundary comparison and authorization

`agda/ActionChartComparison.agda` uses fourth-order coefficient jets

    j=(m2, lambda_pot, A), A=2a,
    L4=a v^2(dv)^2-lambda_pot v^4/24.

At F=U=1, put b=6 beta for a cubic chart change v=w+beta w^3. Clearing the
rational chart denominators gives an integer carrier map

    T_b(m2,l,A)=(m2, l+4 m2 b, A+b).

Agda proves its inverse T_-b, additive composition law and preservation of

    observe(j)=(m2, l-4 A m2).

An explicit equality connects this convention with Nima's `effective` reader.
The angle-to-ratio and angle-to-sine parameters are b=-2 and b=1. Actual marked
jets are

    angle=(2,16,0), ratio=(2,0,-2), sine=(2,24,1).

The packages retain the actual source filler, declared policy and chart tag.
These maps inhabit the owner's actual `BoundaryGeneratedQuestions.Filler`, our
`Observed` interface and the native observed interface. Inverse/composition also
supply comparisons between every pair of these three packages.

The application gate fixes the chart transition and requires readers to agree
with `observe` on all declared jets. It therefore cannot replace the prescribed
reader by a constant or a potential-only projection. Native retention preserves
the gate evidence as well as the comparison output, with a recovery equality.

This formal layer is a FOURTH-ORDER INTEGER JET comparison at unit scales.
It is not a formal equivalence of real intervals or a formal continuum action.
All raw integer jets are algebraic test inputs, not claimed physically admitted
sources. The real domains, general scales, exact metric functions and source
interpretation are separate supplied analytic/symbolic evidence.

## Sixth-order canonical refinement

Write, in any quadratically normalized parity-even chart,

    G(v)=1+2a v^2+2b v^4+O(v^6),
    V(v)=m2 v^2/2 + l v^4/24 + g v^6/720 + O(v^8).

Here b is the fourth-order metric coefficient, NOT the cleared cubic chart
parameter used above. Integrating sqrt(G) and inverting gives

    phi=v+(a/3)v^3+(b/5-a^2/10)v^5+O(v^7),
    v=phi-(a/3)phi^3+(13a^2/30-b/5)phi^5+O(phi^7).

Thus the canonical coefficients are

    lambda_can = l-8a m2,
    g6_can = g-40a l+352a^2 m2-144b m2.

The checker derives these formulas from a general symbolic jet, independently
of the three example coefficients. It checks their application at arbitrary
positive F,U, obtaining lambda_can=16U/F^4 and g6_can=512U/F^6.

At F=U=1:

| Chart | l | a | b | g | lambda_can | g6_can |
|---|---:|---:|---:|---:|---:|---:|
| angle | 16 | 0 | 0 | 512 | 16 | 512 |
| ratio | 0 | -1 | 3/2 | 240 | 16 | 512 |
| sine | 24 | 1/2 | 1/2 | 960 | 16 | 512 |

Dropping the fourth-order metric term breaks the sixth-order comparison.
For the angle model truncated to its quartic potential, the checker transports
THAT SAME truncated action to the other charts; it does not truncate afresh in
each chart. Its canonical profiles are (2,16,0), whereas the logarithmic model's
are (2,16,512). Agda proves that no function of the common mass/quartic profile
alone can recover these different sixth derivatives. The derivation of the sixth
derivatives themselves is symbolic, not an Agda real-analysis proof.

**A canonical sixth potential derivative is not a full six-point amplitude.**
Exchange diagrams and their chart-dependent derivative vertices have not been
computed here. No quantum decoupling of Nima's two additional massless modes,
physical scale selection, or source-derived spacetime is inferred.

## Verification and next test

    python research/voevodsky/check_native_radar_formal.py --action-charts --fresh
    uv run --with sympy python research/voevodsky/check_action_chart_comparison.py

Fresh safe/cubical closure passes. Two intended negative controls reject the
potential-only equality and the false sixth-profile identification. All 55
symbolic/provenance checks pass, including the current owner dependencies and
fresh proof-source hashes. No owner file was modified or adoption inferred.

Artifacts: `action-chart-comparison-formal.json`, `action-chart-comparison.json`,
`agda/ActionChartComparison.agda`, and `check_action_chart_comparison.py`.

Next bounded physical-readout test: compute the complete single-field tree
six-point amplitude across these charts, including contact and exchange terms,
and test the logarithmic-versus-quartic refinement at that level. General native
constructor propagation and the Rosen operational/completion comparison remain
separate, deferred directions. Owner review of this integration is requested;
that request is not an adoption or a verification result.
