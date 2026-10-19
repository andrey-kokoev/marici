# KrakenSDR successor: held-out physical composition and complementary readout

Owner: `marici.Kitaev`. Status: design draft; no acquisition performed or authorized by this packet.

## Question, claim boundary and disposition

Can independently calibrated physical interventions predict new compositions on held-out inputs, and does a joint complex readout distinguish specified physical preparations that a declared coarse readout cannot?

This replaces the primary scientific target of the [old shell protocol](../voevodsky/krakensdr_conducted_rf_route_residue_experiment.md), without editing that historical packet. Programmed shell attenuation remains an electronics/pipeline control, not evidence of naturally occurring arithmetic coupling. Current disposition: executable synthetic analysis controls and a draft acquisition specification; apparatus acceptance, numeric preregistration and physical records remain absent.

Applicable SCC obligations: forward realization of named hardware operations; attachment transport through the same independently calibrated port map; route/composition compatibility; and readout descent. A successful classical RF realization is not evidence against conventional RF theory, nor evidence for a unique physical realization of the native mathematical framework.

## Governing conjecture and rivals

Conjecture: one frozen calibration model with shared physical parameters predicts held-out composed IQ records within separately specified uncertainty and engineering tolerances. For a declared coarse-collision pair, a calibrated complementary quadrature adds predictive discrimination without reading source labels as signal.

Rivals: per-setting response fitting; source waveform synthesis of the desired answers; unmodeled mismatch/reflections; shared-reference drift mistaken for a second signal; endpoint-only identification of continuous transport; and mixed contrast mistaken for noncommutativity. Strong falsifiers are a wrong held-out gain that training interpolates, conjugate complex responses with identical intensity/real part, and nonzero mixed contrast between commuting scalar attenuators. No result is obtained by changing these rivals after test labels are opened.

## Research inputs that change the old design

- [Native joint parity](../nima/seed-joint-parity-response.md): a joint record can retain a mixed contrast erased by either marginal; commuting updates can already produce it. The Boolean diagnostic is not a calibrated amplitude or energy.
- [Unitary image nonuniqueness](../nima/tick-unitary-image-nonuniqueness.md): identical corner operations can have inequivalent intermediate realizations. Endpoint agreement does not select a generator, rate or physical clock.
- [Finite character collisions](../voevodsky/finite_character_probes_have_constructive_route_collisions.md): do not claim a fixed finite observer family separates every larger packet.
- [Complementary quadratures](../voevodsky/two_real_quadratures_form_a_stable_complementary_observer_for_relative_phase_holonomy_20260910.md): real trace/intensity can erase orientation; joint quadratures recover the specified phase in its stated domain.
- [Premise correction](../voevodsky/route_residue_metaphysical_premise_correction.md): the open physical issue is construction and source authority, not whether an already compatible faithful observer distinguishes.

The recent SU2 lattice results supply no RF realization map or new RF prediction. They are not hypotheses tested by this bench.

## 1. Source, ports and physical configurations

Keep conducted operation, protection pads, DC verification, 50-ohm loading, raw coherent IQ and the old manual-based port-safety gate. Intended instruments remain SDG2042X, KrakenSDR, DHO924 and NanoVNA V2 Plus4; delivery, working condition and limits must be checked rather than inferred from the historical procurement list.

Minimal first implementation: one physical signal path containing two replaceable, independently calibrated blocks A and B, each with two declared configurations A0,A1 and B0,B1. A may be an attenuation insert/bypass pair; B may be two cable/delay inserts. Each bypass includes its actual connectors and switch/patch fixture. Select actual parts only after inventory and characterization. The generator supplies fixed prepared inputs, not separately fabricated answers for the four compositions.

Use an upstream reference pickoff and the existing receiver's in-run reference. Assign channels by measured capability: reference, test output, and available diagnostic/replicate branches. A splitter alone does not implement controllable two-mode mixing. A native four-state/Boolean reader is NOT automatically realized by four RF channels.

For each configuration record an explicit directed port list and full terminated topology. All unused splitter ports stay terminated. Do not connect active generator outputs together. No antenna or radiated transmission is part of this protocol. Reconfigure only with the safe shutdown procedure from verified manuals.

The admitted configuration family must be enumerated. Run a four-corner factorial only if all four compositions are independently available on this hardware. Record unavailable compositions as unavailable, not as zero-valued measurements. For AB versus BA record the actual source-to-load direction and reconnect procedure; mathematical inverse certificates do not imply executable inverse hardware. Lossy pads are not unitary gates.

## 2. Calibration and composition model

Measure A0,A1,B0,B1,fixtures,receiver paths,source/load mismatch and repeatability independently of the held-out composed-response records. Freeze calibration estimates, allowed uncertainty, physical units and reference frames.

The matched scalar baseline at frequency f is

    y_ij(f)=C(f) H_Bj(f) H_Ai(f) x(f).

Use that product ONLY when the measured matching/isolation bound justifies it. Otherwise compose calibrated two-port scattering or chain matrices with the actual source/load reflection coefficients and intervening fixtures. In the matched-load approximation even two scalar two-ports have

    S21_(B after A)=S21_B S21_A / (1-S22_A S11_B),

so multiplying S21 alone can predict the wrong answer. Reverse order can change loading without implying any exotic or quantum effect. A two-port NanoVNA does not measure an unrestricted multiport apparatus matrix; scope any loaded-network model to its measured terminations.

Calibrate the receiver map C and phase convention on separate basis/reference runs. Verify simultaneous reference stability; do not assume the AWG and SDR oscillators are locked merely because each instrument has coherent channels. Reference normalization is a declared inference step with propagated correlated uncertainty; preserve the raw amplitudes and delivered/lost-power records. Never renormalize each setting to equal surviving power.

Calibrating the complete AB response on the same data and then calling its reconstruction a composition prediction is prohibited. An independent AB VNA measurement may be retained as a held-out cross-instrument check, not used to refit the component model scored on it.

## 3. Freeze three partitions, not one fitted response table

1. Non-discriminating pilot: establish safe linear levels, phase stability, settling, repetition count and attainable tolerances. No target-contrast label inspection.
2. Calibration partition: estimate component maps, common nuisance parameters, noise/drift covariance and detector from designated inputs/settings. Declare the model's interpolation domain.
3. Sealed evaluation partition: new prepared amplitudes/phases, composed configurations, and intermediate settings or waveforms on which named rivals disagree. Evaluation records must not also be component-calibration records.

Freeze all partitions, waveform/configuration identifiers, randomization seed or ordering rule, reset/settling rule, model/version digests, and analysis code before evaluation. Use repeated reference blocks and A/B order randomization to estimate—not erase—reconnection and drift effects. Log physical acquisition timestamps and controller state. No mathematical grade, attenuation depth or native history index is assigned physical time.

If calibration drift or a port-limit violation invalidates the frozen uncertainty,stop; a revised calibration requires a new run/version and fresh sealed evaluation. Preserve excluded records with reasons. No per-setting or per-held-out-mode nuisance refit is allowed. One shared parameter vector must apply to the whole scored packet.

## 4. Primary prediction test and uncertainty

Stack all scored complex outputs as a real vector y=(Re y_1,Im y_1,...). Compute the prediction y_hat from calibration only. The primary residual is r=y-y_hat. Propagate a JOINT covariance for measurement and calibration uncertainty,including shared reference,source,configuration blocks and their cross-covariances; do not automatically add independent covariances for correlated quantities.

Freeze a physically meaningful residual norm/units,tolerance epsilon_phys,confidence procedure and error probability before evaluation. Declare a separate noise-weighted residual score on the supported covariance range. A singular covariance retains unresolved modes; it is not a reason to delete them. Any regularization/subspace rule and resulting claim scope must already be frozen.

Acceptance requires a simultaneous upper confidence bound on the physical prediction error below epsilon_phys AND the preregistered predictive coverage check. Failure to reject a zero-residual null is not equivalence. A noisy apparatus must not pass merely because its covariance was inflated; calibration/drift limits and the absolute engineering tolerance remain separate gates. Report overcoverage and undercoverage as well as failures. Multiplicity across settings/readers/model comparisons is included in the frozen confidence procedure.

Compare named rivals using held-out prediction loss with a declared uncertainty interval. If ordinary calibrated RF and the proposed realization have identical predictions,report observational equivalence on this domain. No fundamental-theory discrimination is admitted.

## 5. Mixed response and order response are different tests

Retain the full complex output vector. For available four configurations compute

    Delta=y_11-y_10-y_01+y_00.

For a fixed linear component model this is C(B1-B0)(A1-A0)x. It can be nonzero for COMMUTING scalar attenuators. Its target is a held-out factorization prediction,not evidence of noncommutativity,nonlinearity or quantum behavior.

For an admitted order experiment separately compute

    K=y_(B after A)-y_(A after B).

Its conventional RF prediction must include matching,loading,controller state and reference/reconnection uncertainty. A nonzero K only establishes order sensitivity within the tested physical configuration when those rivals are excluded. The initial matched scalar null should predict K=0. A genuine independently controlled two-mode mixing test is a separate apparatus extension,not a capability attributed to the present splitter.

For either contrast L y,propagate N_contrast=L N_joint L^T in the real representation. Independent-channel error bars are not a substitute. Contrast magnitudes alone are not the primary acceptance test in section4.

## 6. Complementary-observer test

Choose the coarse map in advance: intensity |z|^2 or one fixed real quadrature Re(z),where z is a declared relative transfer in a common calibrated frame. Joint observation retains (Re z,Im z). Do not equate these coordinates with the native parity bits without an additional source-to-hardware map.

From calibration,select two PHYSICAL configurations with matched amplitude within a preregistered equivalence tolerance and separated relative phases. A single common phase-frame rotation may be frozen from calibration; no setting-dependent correction may be fitted to force a collision. Raw power is still retained.

Conjugate responses z_+=r exp(i theta),z_-=r exp(-i theta) illustrate the target: equal intensity and real quadrature,opposite imaginary quadrature. The measured pair must actually satisfy its coarse equivalence gate. Swapping arbitrary unequal-loss paths gives z->1/z,not generally conjugate(z); it is not automatically an intensity-blind pair. If coarse amplitudes remain distinguishable,that pair does not demonstrate coarse blindness.

Freeze a calibration-trained joint classifier and a coarse classifier with equal label access; score both on sealed trial labels. The complementary-observer claim requires (a) coarse equivalence within tolerance and (b) joint discrimination exceeding the frozen noise/confidence margin on held-out trials. Source/controller labels are for scoring only and cannot enter signal features. Shared-reference drift is an explicit null. Read both quadratures from the same preparation where possible; sequential readings require a stationarity/repeatability justification,not an independence assumption.

## 7. Intermediate transport test

Do not infer a unique continuous generator from matching endpoint operations. A concrete RF rival uses two delays differing by one carrier period: they agree at that carrier but differ at other frequencies or in pulse arrival. Freeze the delay/model alternatives from independent physical characterization; use held-out frequencies or transients to discriminate them. Sampling,phase unwrap and bandwidth must resolve the declared alias alternative.

If a native unitary/Hamiltonian realization is later claimed,it needs a separately typed physical carrier,preparation,operation map,parameter-to-clock map,detector and loss model. RF phase variation is not automatically quantum Hamiltonian evolution. This stage presently tests the calibrated RF transfer interpolation and controller record,not an abstract preferred logarithm.

## 8. Evidence ladder and stop conditions

- Synthetic controls only: analysis semantics/pipeline validation.
- Physical prediction gate passes: calibrated held-out composition prediction on the declared ports,levels,frequencies and configurations.
- Prediction plus coarse-equivalence/joint-separation gates pass: observer complementarity on that specific tested pair.
- A source-natural arithmetic claim or uniquely selected native dynamics: BLOCKED until an independent physical source/realization map and distinct falsifiable prediction are supplied. The first three stages do not remove that blocker.

A valid held-out prediction failure criticizes the declared model. Saturation,synchronization loss,wrong topology or invalid records are execution defects requiring repair and a new sealed run,not scientific support for either model. An unresolved residual is retained with its raw record and the cheapest discriminating test. No graph admission,checker pass or software freeze certifies apparatus performance.

## 9. Acquisition prerequisites and files

Fill the companion template with actual inventory/manual limits,safe link budget and margin,measured calibration/noise references,typed admissible configuration set,physical tolerances,confidence/coverage rules,settling/reset/timing,repeat count and held-out identifiers. All are intentionally absent at draft creation. A programmatic readiness pass checks completeness/consistency only; it does not validate the cited measurements or authorize energizing equipment.

Raw IQ stays in an actually ignored or external acquisition directory,with immutable manifests and file digests; no raw samples enter Git. Each evaluation record binds source waveform,physical topology,calibration/model version,settings,reference/raw files and quality flags. Store failed records as well as accepted ones.

Companions:
- `contracts/krakensdr-physical-composition.v1.json`: analysis contract and claim gates.
- `contracts/krakensdr-physical-composition-run.template.json`: unready run template.
- `checkers/check_krakensdr_physical_composition.py`: exact synthetic falsifiers and fail-closed preflight tests.
- `results/krakensdr-physical-composition-v1.json`: software-only receipt.

A software SCC freeze fixes this draft and its tests; it is NOT a completed acquisition preregistration. No instrument settings have been chosen or executed here. The user requested this successor after identifying the old target as obsolete; that instruction allocates design work,not evidence or hardware authority.
