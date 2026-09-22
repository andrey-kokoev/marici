# Sharper bulk norms reduce the fixed projection remainder

## Result

The squared-norm upper bounds used by the FIXED 136-dimensional auxiliary projection are now sharper:

| Damped bulk component | Previous upper bound | New upper bound |
| --- | --- | --- |
| H_+ | 0.25380988 | 0.24893556 |
| H_- | 0.41993619 | 0.41520763 |

These displayed upper bounds are rounded upward. The actual response has not changed: this removes slack from its norm certificate, not energy from the detector.

With the same projection and deployed hats, the new outward C_bin enclosure is

    [1.97202360, 1.97234062].

Its width improves by a further factor of about 1.352; the positive-gain width improves by a further factor of about 1.165. The frozen middle task remains UNRESOLVED in both modes. Its normalized necessary cost is about 39.98909179, while its calibration-uniform witness cost is about 40.01112928, against budget 40.

The raw observations, order-16 prior, actual detector, 76-bin/horizon-64 filters, 136-dimensional projection, source-functional bounds and theta quadrature are unchanged. Earlier conclusive cases remain conclusive. Ten longer portable identity-refinement chains are exported and independently verified.

## 1. Audit the old allowance before changing the proof

The owning Plancherel norm calculation integrates whole frequency cells, then bounds the entire remaining frequency tail. Its old cutoff is 2048 and its common tail upper bound is approximately 0.00662147039527 per squared norm.

The new checker records the old finite-band enclosures, not just their sum. It then separates the decrease in each squared-norm upper bound into three exact rational differences:

| Contribution to upper-bound decrease | H_+ | H_- |
| --- | --- | --- |
| Finer finite cells and cancellation-preserving evaluation | 0.00171046122 | 0.00317239296 |
| Resolve frequencies 2048 through 8192, retaining the old tail formula at 8192 | 0.00217791658 | 0.00104300526 |
| Sharper tail algebra at 8192 | 0.00098594172 | 0.00051316194 |

These table entries are approximate; exact rational differences are saved and telescope exactly to the total decrease. They are not estimates of the unknown true norm error. Each positive decrease proves that at least that much of the earlier upper allowance was removable.

The new finite bands use cells per frequency unit:

    [0,16]: 4096,
    [16,128]: 1024,
    [128,2048]: 64,
    [2048,8192]: 8.

All 352256 cells are enclosed in their entirety at the same 80-bit arithmetic precision. A nonfinite enclosure would be bisected or rejected, never accepted as a sampled value. No bisections were needed in this run.

The larger cutoff is a proof-only frequency cutoff. It is not a change of physical acquisition horizon or a truncation of the actual response.

## 2. Preserve exact cancellations in the bulk profiles

Keep s=7/2, beta=3/2, q=beta+it and the actual logarithmic derivative L(s). Define

    c=1/s+1/(s-1)-L(s),
    D(q)=psi(q/2)/2-log(pi)/2+zeta'(q)/zeta(q).

The owning response formulas simplify EXACTLY to

    H_+(q)=(c-D(q))/(q+s-1),
    H_-(q)=(c+D(q))/(q-s).

The rational terms 1/q and 1/(q-1) cancel before interval evaluation. These are the same profiles, not new kernels. The checker verifies the rational coefficient identities after clearing denominators and cross-checks their numerical implementation against the owning formulas. The algebraic identities, not a finite comparison scan, justify their use throughout each cell.

This rewrite also sharpens the infinite-tail estimate by retaining the real and imaginary parts of the logarithmic main term rather than bounding all terms separately by a triangle inequality.

## 3. A side-specific infinite-tail majorant

On Re(q)=beta>1,

    |zeta'(q)/zeta(q)| <= P_beta=-zeta'(beta)/zeta(beta).

The owning digamma estimate gives

    D(q)=log(q/(2pi))/2 + zeta'(q)/zeta(q) + error,
    |error|<=1/t.

For T=8192 put

    delta_T=log(1+(beta/T)^2)/4,
    a_+=-log(2pi)/2-c,
    a_-=-log(2pi)/2+c,
    u_±=log(T)/2+a_±+delta_T.

The required positive-real-main-term inequalities are certified. For t>=T, the imaginary logarithmic main term has magnitude at most pi/4, and its real part is bounded above by log(t)/2+a_±+delta_T. Using

    sqrt(v^2+b^2) <= v+b^2/(2v),  v>0,

and v>=u_± gives

    |H_±(beta+it)| <= [log(t)/2+K_±]/t,
    K_±=a_±+delta_T+pi^2/(32u_±)+P_beta+1/T.

Here both denominator moduli are at least t. Writing Q_±=log(T)/2+K_±, integration yields

    (1/pi) integral_T^infinity |H_±(beta+it)|^2 dt
      <= [Q_±^2+Q_±+1/2]/(pi T).

The new tail upper bounds are approximately 0.00103803349544 and 0.00151081326419. Both improve on the old common formula evaluated at the SAME new cutoff, approximately 0.00202397520408.

All constants and inequalities are enclosed with Arb/Acb. The Euler-line bound covers all primes and prime powers and does not use a prime-number-theorem approximation. These are norms of the declared damped bulk responses, not ordinary L2 norms assigned to an undamped limiting field.

## 4. Propagate only the improved norm information

For each component the fixed-hat pairing proof remains

    <g,b> = <Pg,Pb> + <g-Pg,b-Pb>,
    |remainder| <= sqrt[(B_g-||Pg||^2)(||b||^2-||Pb||^2)].

Only B_g changes. The checker retains:

- the 136 auxiliary rates and 3072-bit projection arithmetic;
- the exact deployed hat coefficients and their normalizers;
- the projected pairing center and fixed-hat projection residual;
- the endpoint and weak contributions.

The new certified pairing-error upper radii are approximately 0.0000815718 and 0.0000769306, down from approximately 0.0001142083 and 0.0001000582.

Positive-window calibration is replayed with the same 262144 complete cells, 192-bit arithmetic and cutoff 32. Exact endpoint comparisons prove that the new positive-gain intervals are strictly nested in their parents. The crossed and vacuum gain enclosures remain unchanged.

The middle case still straddles the source-budget boundary. Its conditional positive task bounds are NOT relabelled as a nonvacuous task conclusion. Neither the auxiliary approximation nor its norm certificate changes which physical detector is being studied.

## 5. Reproduction and independent transition checks

Fresh norm audit, fixed-projection pairing, and frozen-task replay:

    uv run --with sympy --with python-flint python research/grothendieck/checkers/certify_bulk_norm_task_refinement.py

The norm audit alone:

    uv run --with python-flint python research/grothendieck/checkers/refine_bulk_response_norm.py

Exact-rational replay, telescoping audit checks, and portable chain export:

    uv run python research/grothendieck/checkers/check_fixed_bin_response_refinement.py --bulk-norm

The preceding `*-fixed-hat.json` chains must exist; if absent, run the same checker without `--bulk-norm` after producing the earlier portable chains.

Independent verification:

    python research/grothendieck/certificates/verify_source_task_transition.py research/grothendieck/results/portable-source-task-transitions/private-middle_threshold-bulk-norm.json

Artifacts:

- `results/bulk-response-norm-refinement.json`;
- `results/three-channel-source-task-calibration-bulk-norm.json`;
- `results/bulk-norm-task-refinement.json`;
- `results/bulk-norm-task-refinement-tests.json`;
- `results/portable-source-task-transitions/*-bulk-norm.json`.

The portable verifier rechecks source-budget and task statements and identity refinement, including isolated execution outside the repository. The analytical norm and calibration claims remain the responsibility of their fresh owning computation; a digest or a nested interval alone does not prove them. No source-action, filtration or derived-class transport is inferred.
