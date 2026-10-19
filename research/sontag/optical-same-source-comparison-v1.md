# Same-source statistical optical history comparison v1

## Source and licensed scope

Use the SAME successor event source from `optical-statistical-feedback-v1.md`: fixed coherent preparation parameters a0,b0 and retained phases; independent Gamma preparation priors with supplied shapes/rates; calibrated ideal gain/tap parameters; counts as externally observed outcomes. Fresh vacuum inputs are preconditions at every passive mixing operation. This is a conditional mathematical/physical-theory comparison, not an experiment or physical calibration certificate.

The exact predecessor's passive `read-total` event is NOT in this source. Positive comparison here cannot resolve a node interpreted as exact nondisturbing physical feedback without a versioned scope review.

## Two maps

Mathematical realization M retains current occupations A=f1*a0, B=f2*b0, cumulative lost mean occupation, event/outcome record and posterior parameters. Gain multiplies f1 by q² and f2 by q⁴. Tap multiplies both by 1−τ, adding τ(A+B) to recorded loss; count likelihood is Poisson with means ητ(A,B).

Ideal physical realization P retains coherent signal amplitudes α,β, every fresh ancillary output, fixed-frequency convention and detector outcome record. Gain acts by the two passive rotations R(q), R(q²). Tap splits each amplitude into surviving sqrt(1−τ), observed sqrt(ητ) and unobserved sqrt((1−η)τ) branches. Projection π sends coherent amplitudes to squared modulus and environmental outputs to summed occupation. The physical energy map is ħω times occupation under the declared equal-frequency convention.

For each admitted event e, `π(P(e)(z))=M(e)(π(z))`, including signal AND loss ledger. Physical count likelihoods equal the mathematical likelihoods. Under coherent product preparations, counting the tapped output has no extra signal change beyond that splitter, conditional on fixed amplitudes. This special instrument property is part of the source assumptions.

## Sequential posterior state

Keep priors on INITIAL a0,b0. At each tap the exposure coefficient for mode i is `ci=ητfi`, where fi is the current pre-tap gain/tap factor. Given the complete recorded history, posterior shape is `ki+sum counts_i` and rate is `ρi+sum ci`. Current means and variances are `fi*shape_i/rate_i` and `fi²*shape_i/rate_i²`.

An adaptive gain is a function of preceding public observations. Conditioning on that observed history fixes the gain; it is not an additional independent noisy observation of the hidden preparation. Therefore the same exposure rule holds for observation-based policies. This general statement is analytic; the executable prefix fixture below uses predeclared rational gains, while the earlier successor checker separately verifies target-policy moment calculations.

## Composition theorem

Initial projection, prior and resource records agree. The one-event state/resource/likelihood squares imply by induction that every finite admitted history has matching projected intermediate states, accumulated resource effects and conditional likelihoods. The Gamma kernel update gives matching posterior information at every prefix. Concatenation agrees provided both routes use the same terminal information state, physical environments and admission conditions. This is a same-source statement, not independent endpoint fitting.

Retention is essential: factors and outcome records affect later detector exposure. Replacing a post-gain exposure by its initial value changes the likelihood/posterior. Reusing environment inputs invalidates the one-event square. Equal H does not justify collapsing sectors: `(8,0)` and `(0,8)` produce 2 and 1/2 after q=1/2 in both realizations.

## Fresh execution

`uv run --with sympy python research/sontag/checkers/optical_same_source_history_v1.py`

18 checks pass on four shared event prefixes: tap/count, gain, tap/count, gain. Independent summary and coherent-amplitude implementations compare signal state, cumulative loss, count likelihood, posterior shapes/rates and current factors. Initial phases differ by π/2 and remain in the physical record. Count transcripts are mathematical fixtures, not measured data. The posterior hostile checks that intervening attenuation is included in subsequent exposures.

Result: `results/optical-same-source-history-v1.json`.

## Disposition

Constructed: conditional same-source finite-history comparison for the versioned statistical optical candidate. Unestablished: device controls/calibration, preparation/prior evidence, time/routing, apparatus reset and total resource costs, accuracy under model deviations and coverage across other physical processes. Source-module attachment comparison remains separate under the operator-permitted mathematical scope. Shared net outcome remains unchanged; this evidence requires explicit versioned candidate review rather than retroactively resolving the exact-observation predecessor.
