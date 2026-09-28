# Weak mixing: matter-trace normalization audit

## Outcome

The existing matter-trace argument for 3/13 fails a multiplicity check. Source: research/nima/checkers/check_gauge_coupling_norm.py. It counts Q_L once in the SU(2) trace, but counts its three colours in the hypercharge trace.

Use Q=T3+Y and Tr_doublet(T_a T_b)=delta_ab/2. Per generation, the three quark colours contribute three weak doublets, giving SU(2) index 3/2. The lepton doublet contributes 1/2. Total: 2 per generation and 6 for three generations. Hypercharge squared sums to 10/3 per generation and 10 for three generations.

Under the source's additional common-normalization assumption g_i^2=k/C_i:

    sin^2(theta_W) = g'^2/(g'^2+g^2)
                  = C_SU2/(C_SU2+C_Y)
                  = 6/(6+10) = 3/8.

This is the familiar common-normalization boundary value, not a low-energy prediction without a scale and running prescription. The existing checker also labels g_2^2/g_1^2 with the trace ratio in the wrong direction in its printed output; inverse-trace normalization gives C_Y/C_SU2.

## Consequence for the carrier proposal

The arithmetic 3/(3+10)=3/13 is correct, but the cited trace computation does not justify those two inputs. A carrier-specific comparison measure could differ from the ordinary matter trace; it must explain explicitly why it changes colour weighting in one sector while retaining it in the other. The number three cannot simultaneously be treated as a generator count, a generation count, and a matter trace without maps relating those counts.

Likewise, the source's proposed 137 identity (C_Y+1)^2+(C_SU2+1)^2 changes to 170 when the matter trace is corrected to six. This invalidates that trace-based route to 137. The separate 121+16 comparison-slot hypothesis has different assumptions and was not tested by this audit.

## Consistent colour averaging

A second exact test weights every quark state by 1/3 in both traces, leaving leptons at unit weight. It gives C_SU2=3, C_Y=19/3, and sin^2(theta)=9/28 under common inverse-trace normalization. Thus uniformly removing colour multiplicity does not restore 3/13. Any alternative measure must specify its weights and apply them consistently to both operators.

## Common comparison space and positive-measure bound

Take the direct sum of the Standard Model matter multiplets as the common space, with Q=T3+Y. Let a positive operator W weight each quark state by q and each lepton state by ell. Both sector readouts use this same measure: C2=Tr(W T3^2), CY=Tr(W Y^2). Colour and weak-component multiplicities are retained. Per generation:

    C2 = (3/2)q + (1/2)ell,
    CY = (11/6)q + (3/2)ell,
    sin^2(theta) = (9q+3ell)/(20q+12ell).

For nonnegative q,ell, not both zero, the mixing fraction lies between 1/4 (leptons only) and 9/20 (quarks only). The proposed 3/13 lies below this whole interval. Directly, 10*C2-3*CY=(19q+ell)/2; achieving 3/13 requires ell=-19q. Thus no positive measure uniform within the quark and lepton classes can give 3/13 under common inverse-trace normalization.

This is a bound for the stated two-weight family, not for every gauge-invariant positive measure. Multiplet-specific weights enlarge the family. For example, leaving all multiplets at unit weight except e_R gives C2=2 and CY=7/3+w_e. Choosing w_e=13/3 yields 3/13. This value is solved from the target and has no independent carrier derivation. It demonstrates underdetermination rather than predicting the angle.

Outcome: the simplest common carrier measure is ruled out for 3/13. A viable construction must supply multiplet-specific weighting, additional physical content, or a scale-dependent coupling evolution beyond the static common-normalization model. Exact checker: research/nima/checkers/check_weak_mixing_common_measure.py.

## Next construction

Specify the common comparison space on which both gauge-sector operators act, the measure used for each trace, and the scale/normalization convention. Compute both weighted traces on that same space. Then form their normalized coupling ratio. This is the gauge-sector analogue of requiring a shared reference and readout for the electromagnetic comparison.

## Verification

research/nima/checkers/check_weak_mixing_matter_trace_audit.py recomputes every multiplet contribution using exact fractions. It passes and writes no artifacts. Historical checkers and their generated outputs were left unchanged.
