# RH identity/continuation transport: exact predictive quotient and hostile

Dictionary: `research/conjecture_net/contracts/rh-stage-dictionary.v1.json`.
Checker: `research/voevodsky/checkers/check_rh_identity_continuation_audit.py`.
Receipt: `research/voevodsky/results/rh-identity-continuation-audit-v1.json`.

Fresh construction: `uv run research/voevodsky/checkers/check_rh_identity_continuation_audit.py --replay`.
Default execution validates the retained result and source hashes without repeating symbolic construction or source suites.

## Result

The three required identity/continuation cells now have explicit equivalences, permitted operations, reconstruction/retention witnesses and failure controls. A scalar Riemann readout is future-safe under the twelve-arrow Fourier/generator task but not under native history extension. The native endpoint task needs two linear coordinates, not four, to predict all future scalar readouts.

This is a task-relative predictive quotient of existing endpoint/history operations, not an identification of the full source, a new physical detector or a discarded archive. Analytic domain/completion and stagewise assembly remain open.

## Contexts and equivalences

| Cell/task | Equivalence | Permitted continuations | What remains retained |
|---|---|---|---|
| `hidden-reconstruction`, generic carrier analytic task | P x=P y | Existing C12 and D12 flow | Nx, original coefficients and provenance |
| Carrier unshifted task | r12 x=r12 y | Same C12 and D12 flow | All lost labelled coefficients/history; kernel dimension 11 |
| `history-retention`, full endpoint/generic analytic task | O_n x=O_n y | Actual step_n and existing lifted L_n flow | Endpoint-invisible history Nfull_n and complete history package |
| `riemann-quotient`, scalar-only native-history proposal | ell x=ell y | Native M | **Rejected** as a continuation-safe identity |
| Repaired scalar predictive task | Z x=Z y, Z=[ell;ell M] | Native M and declared endpoint drift | Active endpoint coordinates, invisible histories and complete provenance remain archived |

These contexts do not license arbitrary writes, restoration, additional physical controls or source substitutions. Added Fourier is a separately declared endpoint operation, not native extension and not automatically a supplied history actuator. If an observation context includes archived coordinates, the coarser equivalence must be refined accordingly. No actual resource budget or detector is inferred from these mathematical readers.

## Carrier reconstruction and future transport

The source-derived projection P and embedding E satisfy

    x=E P x+N x, N=I-EP,
    P C12=C4 P, P D12=D4 P,
    N C12=C12 N, N D12=D12 N.

Thus equal P-readouts remain equal through the allowed operation algebra and generator flow. Since the generic comb attachment is injective on four coefficients, this is also equality of its complete generic analytic readout, under the recorded seed/domain choices. It is not equality of the twelve-arrow source: the checker constructs a nonzero h in ker P and reconstructs h from its retained hidden record.

For r12=ones^T J P, r12 C12=r12 and r12 D12=0. The rank-one unshifted quotient therefore predicts the same future scalar value under this specific carrier task. This fact does not transfer to native history M by similarity of readout dimensions.

## History reconstruction and coherent continuation

At actual audited dimensions n=10,16,26,42, retain full endpoint sections and hidden projectors:

    Pfull_n=Q^-1 O_n,
    x=Efull_n Pfull_n x+Nfull_n x,
    O_next step_n=M O_n,
    Nfull_next step_n=step_n Nfull_n,
    O_n L_n=A_endpoint O_n.

The checker reconstructs these objects from the actual retained successor ledger, not an invented free endpoint fixture. It also verifies L_next step=step L_n on the three audited extensions. Equal endpoints stay equal under native extension; endpoint-invisible differences stay invisible but remain reconstructible.

Original history, sections and kernel data are retained. This is reconstruction in the fixed coefficient/history model. It does not identify arbitrary source-algebra relation attachments with unrelated hidden coordinates. The separate I^2/half-phase applicability flags remain unbound to this RH source.

## Exact equal-present/different-future witness

In endpoint order A,B,C,D, the existing analytic chart J gives

    ell=ones^T J=[2,2,0,0],
    ell M=[2,2,2,2].

Choose x=e_A and y=e_A+e_C. Then

    ell x=ell y=2,
    ell Mx=2, ell My=4.

The checker realizes both endpoints inside each actual history space using unit coefficients on actual paths ending at A and C. The states are nonnegative coefficient preparations in the declared mathematical domain; no physical preparation or equal physical resource budget is claimed. Three actual native extensions reproduce the next scalar readings 2 and 4. Their complete source reconstruction remains exact.

Therefore the current scalar observation cannot license substitution through native extension. This is a concrete counterexample, not just the weaker observation that ell M is a different row.

## Smallest future-safe linear reader for the scalar task

Retain

    Z=[ell;ell M]=[[2,2,0,0],[2,2,2,2]].

Direct computation gives

    Z M=T Z, T=[[0,1],[1,1]],
    Z A_endpoint=0.

For z=Z x, native extension sends z to (z1,z0+z1). Continuous drift leaves z fixed. The first coordinate remains the current Riemann scalar readout. The future readout sequence obeys the exact recurrence

    y_(k+2)=y_(k+1)+y_k.

Sufficiency follows by induction from ZM=TZ. Necessity follows because current and next observations are exactly the two rows of Z: equal observations for all native futures imply equal Z. Thus Z equality is precisely behavioral equality for this scalar observation and the declared native/drift protocol.

The observability rows ell, ell M, ell M^2, ell M^3 have rank two. Any linear reader that factors every future scalar observation must have at least two rows; Z attains that bound. This is minimality for linear predictive readers on the declared coefficient spaces, not for arbitrary nonlinear encodings, physical instruments or complete states. On the history spaces the reader is Z O_n and also has rank two.

The recurrence theorem concerns all powers of the declared endpoint operation M. The concrete retained-history realization is freshly checked at four stages and three extension squares; no additional physical continuation or arbitrary infinite-history completion is admitted. No Fourier periodicity is substituted for this native recurrence.

## Cells closed and boundaries preserved

- `hidden-reconstruction`: reconstructed full source and proved future-safe quotient for the fixed carrier operations.
- `history-retention`: exact section/kernel reconstruction and generator/native-extension transport on actual retained stages.
- `riemann-quotient`: rejected scalar-only native identity, explicit realized hostile, and minimal two-coordinate predictive replacement for the selected task.

`one-dimensional-binding` remains a boundary cell, not a selected multichannel source rule. `channel-carrier-source-map`, `one-dimensional-source-selection` and form/Weil obligations remain open independently. No claim about complete Mellin-domain extension, a positive Weil form or RH follows.

## Verification

Fresh replay executes the full endpoint and Riemann specialization suites, requiring their pinned receipts to remain unchanged. The new exact constructor checks source/history reconstruction, stable kernels, the endpoint hostile, three actual future readouts, the predictive update and rank-two minimality. Subsequent runs validate hashes and the retained witness packet. Four structural controls reject missing coverage, scalar/full-state conflation, unbound interventions and promotion of channel selection.
