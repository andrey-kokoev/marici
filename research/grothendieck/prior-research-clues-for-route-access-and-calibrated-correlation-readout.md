# Prior-research clues for route access and calibrated correlation readout

## Audit outcome

Prior work supplies a better candidate architecture than raw theta inversion: source-stage block-parity readout, calibrated jointly with the lower-order channel. It does not yet supply an arithmetic physical implementation. This audit reads the cited packets; their verification claims were not freshly rerun.

## 1. Strongest mathematical clue: missing information is Walsh parity

`research/voevodsky/prime-packet-signature-order-scaling-and-walsh-completion.md` proves that for d=2m labelled prime routes, the degree-(m-1) signature kernel is the direct sum of highest-parity modes on ordered blocks of m unordered pairs. Each block has 2^m routes. The missing dimension is (2m)!/2^m.

For four primes this identifies exactly six four-route alternating vectors. These are the lost correlations, not unspecified high-order complexity. The same packet implements six-prime parity readout and proves 2I<=G_joint<=438I for its declared route-counting and output metrics. That is genuine conditioning information, but it is not a raw theta or calibrated physical metric theorem.

New proposed application: implement six block-parity channels at the admitted route source rather than infer them by amplifying exponentially small theta tails. A signed parity accumulator only needs the ordered pair descriptor and orientation sign. It must act before the relevant route information is discarded.

Do not confuse edge-labelled signature degree two, which suffices for four primes, with the interval-projected degree-four construction. The projection changes the information content of each coordinate.

## 2. Physical architecture clue: accessible route markers and reference phases

`research/aspect/polarization-marker-quantum-eraser.md` explicitly distinguishes accessible route markers from inaccessible environmental leakage, and declares the route, marker, environment, and detector factors. Two referenced quadratures recover a complex coherence on the stated reduced-state class. Equal marginals do not imply equal accessible joint records.

Application: a proposed parity instrument must identify where the orientation information lives, whether that factor is accessible, and how its signed/complex output is read relative to a reference. A classical distribution of routes admits parity expectations directly; arbitrary complex route coefficients require coherent amplitude readout. Counting marker events alone is not a linear measurement of those complex coefficients.

This is an architecture template, not a map from the optical apparatus to the arithmetic theta carrier. Fitting a marker from a hidden route is not an authorized implementation.

## 3. Metric clue: calibration is a typed object

`research/voevodsky/sector_derived_product_metrics_are_noise_whitened_readout_metrics_not_arbitrary_direct_sums_20260911.md` supplies the required contract: record map R, positive covariance Sigma, units, quotient, and provenance. The metric is the pullback of the whitened output norm. Cross-covariance cannot be dropped just to obtain a product metric.

Application: for the lower-order channel plus six parity outputs, require the joint calibration, including their cross-noise. Test the whitened restricted-source minimum singular value against response-operator error. A source-pulled norm alone supplies neither detector precision nor physical energy.

## 4. Concrete apparatus precedent, not yet route correlation

`research/voevodsky/apparatus_conditioned_shell_probe_cutoff_study.md` studies source-programmed shell weights followed by boundary readout. In its declared Euclidean model, four settings at cutoff 960 have margin about 0.013965; the physical cutoff remains pending measured transfer/noise calibration.

Useful clue: change the authorized source operation before projection rather than postprocess a collapsed record. Limitation: those probes measure edge/cycle data. Any number of operations applied only to the same aggregate edge vector still annihilate the four-route correlation collision. The new programming must depend on event order or retained parity state, not just shell marginals.

## 5. Scope and authority warnings

- `research/grothendieck/theta-principal-angle-is-perfect-before-aggregation-and-tautological-after.md`: faithful/aligned upstream traces do not prevent a later arithmetic map from erasing their image.
- `research/aspect/repairable-complexity-optical-probe-libraries.md`: a hidden-route oracle is not an admissible probe; intervention authority must be frozen before evaluating success.
- `research/voevodsky/nonfaithful-probe-as-classical-factorization-witness.md`: a separating witness need not reconstruct the whole source. If the actual objective is to reject one rival rather than recover 24 coefficients, one authorized parity contrast may be enough. It also warns that recording routes can destroy coherent composition in quantum implementations.
- `research/aspect/optimal-route-gram-strict-return-certificate.md`: even knowing parity-controlled overlap does not supply absolute route norms or the physical route map.

## Recommended successor

Construct a finite calibrated parity-instrument contract, explicitly separating:

1. classical route-mixture parity expectation;
2. coherent complex-amplitude parity readout;
3. arithmetic source adapter;
4. noise covariance and units.

Use the four-route collision as the acceptance test, and reject any implementation using its hidden route labels unless the source actually exposes them. Then assess whether one parity witness suffices for the scientific objective before demanding full tomography.

This reopens a source-intervention branch, not the disproved post-aggregation inversion branch. None of the reviewed packets closes the physical arithmetic adapter by itself.
