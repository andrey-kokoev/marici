# The actual P_y gain audit identifies the source but not the four-tower faces

## Audit result

One actual labelled source/observer step now has a checked identification, rather than a substitution of the five-dimensional structural fixture.

The audit reconstructs the original six-event source v_y from the finite structural certificate, translates its Boolean corner labels to arithmetic endpoints, checks its expanded path cost and normalized private coefficient, and verifies gain-two transport of its numerical task.

The structural obstruction is freshly reverified on the original packet. The full-source coordinate-gain theorem applies to the declared operation under its owning hypotheses. However, the bundle does NOT yet supply actual four-tower face witnesses or a tetrahedral filler.

This isolates the remaining identification gate rather than covering it with another abstract fixture.

## 1. The source identification is now checked, not just referenced

The source is

`v_y=mixed(2,3) forgotten(5,7) mixed(11,13)`.

Starting from the structural certificate's selected prefix and suffix, the audit reconstructs this product. Its expansion has 32 path terms with total absolute coefficient 32. The private coefficient is exactly one.

Boolean-corner labels are converted using

`endpoint(mask)=2 * product(event_primes selected by mask)`.

The resulting marked seams are

- `[2,4]`, retained;
- `[12,60]`, forgotten;
- `[420,4620]`, retained;

inside the outer corner `[2,60060]`.

These are compared directly with the numerical bridge manifest. Thus the normalized scalar is the coefficient of the SAME source line `x=a v_y`, with declared path cost `32|a|`; agreement is not inferred merely from shared names.

The audit reruns both existing verifiers and checks the manifest's referenced evidence hashes against the actual files. This is content binding, not authentication or a proof of external assumptions.

## 2. A genuine coordinate operation, not an invented calibration family

The tested operation is defined on the entire saturated family of the private raw seed:

`lambda_new(x)=2 lambda_old(x)`

for every source and admitted context. All other seed families and the lower observer remain unchanged. The source comparison is the identity.

This is a re-expression of fixed readouts. It is NOT a claim that varying a physical theta parameter doubles the detector, nor is it inferred from agreement on one witness or the 270 cubic columns.

With `z_y=E_y P_y`, the new coordinates obey

`z'_y=2 z_y`, `E'_y=2 E_y`, `P'_y=P_y`.

The saved enclosure `[1e-240665,1e-240664]` and synthetic raw-data interval therefore both become `[2e-240665,2e-240664]`. The source budget remains 32 and the target remains `P_y>1/20`.

The old feasible witness and dual bound verify against the new problem after rebinding its digest. Both certificates establish the universal lower bound `P_y>=1/10` and nonempty feasibility.

## 3. Error transport is explicit

The raw interval's center and absolute radius double. Dividing the radius by the calibration lower bound gives the same conservative bound before and after the gain, namely `9/2`.

This broad quantity is ONLY the raw-radius contribution normalized by a calibration lower bound. It is not the total posterior coefficient uncertainty or a claim of achievable experimental precision. The positivity result uses the full data/calibration intervals and source prior, not a small-error approximation.

No measurement was performed and no Arb integral was rerun. The saved calibration enclosure and the synthetic acquisition retain their explicitly declared external meanings.

## 4. Structural links: what is checked and what is theorem-backed

Fresh independent verification checks the original source certificate's:

- 240 local two-event kernels;
- 360 prefix generators;
- 720 right actions;
- 359 N-prefix generators;
- 270-dimensional private coefficient matrix;
- `P_y(N I)=0` and `P_y(f(v_y))=1`.

This is the actual labelled packet, not the dual-number gain fixture.

The owning theorem `../voevodsky/whole-row-calibration-gains-transport-the-filtered-attachment-but-internal-reweighting-need-not.md` gives the additional conditional transport statement: a positive gain on the COMPLETE saturated family preserves its full source kernel and induces the unique source-compatible comparison. It transports the inherited filtration and the filtered pushout, and its comparisons compose exactly.

For the operation defined here, the whole-source gain identity holds by definition. Nevertheless the present audit does not export a machine-readable matrix or symbolic presentation of the full actual observer, its inherited ideal action and its chosen source lift. The finite obstruction verification must not be advertised as having checked those additional structures.

## 5. Precise remaining artifact

The next missing artifact is a source-compatible presentation of the ACTUAL saturated evaluations together with the retained source lift. It must bind:

1. source actions and evaluation maps;
2. the inherited source ideal and its filtration images;
3. the chosen lower-filtration nullhomotopy/source lift, not just a nonzero/zero status;
4. the six comparisons and four face witnesses of the proposed four-tower diagram.

The numerical source line is a restriction of the source domain, not an identification of the full observer module. The five-dimensional dual-number fixture is not that full module either. Their labels cannot supply the absent maps.

A suitable export may be symbolic rather than a dense matrix over rational numbers: the fixed actual analytical coefficients must not be replaced by arbitrary enclosure endpoints to manufacture exact identities.

Only after this artifact is supplied can the existing higher-coherence checker be connected to actual face and filler data. The present audit therefore records `full_four_tower_identification_verified: false`.

## Verification

`python research/nima/checkers/audit_actual_py_gain_identification.py`

The run succeeds and rejects three altered identifications: a wrong seam endpoint, a wrong outer endpoint, and a raw reading gain without the corresponding calibration-coordinate gain.

Artifacts:

- `research/nima/results/actual-py-gain-identification-audit.json`
- `research/nima/results/actual-py-gain-problem.json`
- `research/nima/results/actual-py-gain-certificate.json`
- `research/nima/results/actual-py-gain-transition.json`

The gained numerical certificate can also be checked directly:

`python research/nima/certificates/verify_diagonal_task.py research/nima/results/actual-py-gain-problem.json research/nima/results/actual-py-gain-certificate.json`
