# Conditional spectral bridge to an existing independent-family successor

## Existing constructor, explicit adapter

Reuse `check_recursive_independent_comparison.py` unchanged. Its constructor groups supplied records by their targets and forms all ordered member pairs, preserving endpoint tuples and parent identities.

The selected input domain for this pilot consists of the nine LEFT-TRIANGLE x RIGHT-TRIANGLE occurrence pairs. Their endpoints are the corresponding ordered primitive endpoint tuples. No A->A endpoint assignment to modes is inserted. Complete spectral parents and both ordered history windows remain retained.

For those nine basis-labelled records, declare the FREE BILINEAR COEFFICIENT EXTENSION

    B(e_a,e_b)=e_(a,b), hence B(x,y)=x tensor y.

This follows uniquely once that basis action and bilinearity are stipulated. The structural constructor alone does not assign physical amplitudes or require this coefficient interpretation. Independent pairing, the selected input domain, complex coefficients and reader conventions are explicit pilot assumptions.

## Actual output type

Each input operand has nine complex coordinates. The output carrier has 81 labelled four-occurrence coordinates. B is bilinear in two independent inputs; self-comparison B(x,x) is quadratic, NOT a 9x9 linear evolution.

Input endpoint tuples have length two; output tuples have length four. The actual structural constructor supplies their parents and tuple concatenations. In this fixture the nine input target tuples are distinct, hence all incoming families are singletons. All 81 output target tuples are likewise distinct. No non-singleton higher family or physical growth law is claimed.

The 81-dimensional output carrier can support arbitrary linear combinations, but one pair (x,y) produces only a separable tensor. The coordinate count is not a claim that one input pair independently prepares 81 amplitudes.

## Commuting square

Let P_alpha be the nine previously verified mode-pair projectors. For both independently prepared coefficient inputs,

    x = sum_alpha P_alpha x,
    y = sum_beta  P_beta y.

Then

    B(x,y) = sum_(alpha,beta) (P_alpha x) tensor (P_beta y).

Thus reconstruct-then-compare agrees exactly with compare-in-spectral-components-then-reconstruct. The spectral output has 81 mode-pair-of-mode-pair channels on the 81-dimensional output carrier; they are not the old three channels or an unchanged 9x9 operation.

The checker verifies the square on every one of the 81 input basis pairs, plus a complex linear-combination fixture. Bilinearity extends the basis result to all inputs. Orthogonal spectral components preserve the tensor budget

    ||B(x,y)||^2 = ||x||^2 ||y||^2.

This is multiplicativity of the declared coefficient norm, not conservation of physical energy in a time evolution.

## Which retained residuals matter?

Write x=d+r and y=e+s, with d,e same-mode components and r,s their cross-mode residuals. The complete successor contains

    d tensor e + d tensor s + r tensor e + r tensor s.

Keeping only the first sector generally loses output coefficients. All four sectors and their separate budgets are checked.

Two observation conventions were fixed before choosing a hostile input:

1. **Unit-mass mean in each output target family.** Here all families are singletons, so this reader is the full coefficient array up to indexing. It does NOT factor through the two parents' same-mode projections.
2. **Unit-mass aggregate mean over all output records.** This reader DOES factor through those projections: mean(B(x,y))=mean(x)*mean(y). Every cross-mode component has zero coordinate sum because at least one local factor is orthogonal to the common mode. The input mean therefore already factors through D.

For a concrete hostile, compare inputs x=e_0 and x'=D e_0, holding y=e_0 fixed. They have identical current D-readings. The successor family readers differ, with squared norm difference 2/3; the aggregate means agree exactly.

This does not manufacture a dynamical mixing operation. It shows that a new constructor with a FINER OUTPUT READER can expose data omitted by the old reader. No contradiction arises with DTR=0 for the previous local slot controls.

## Follow-up: endpoint-compatible composition with the same coefficients and reader

Instead of admitting all 81 candidate pairs (a,b), retain only those satisfying

    target(a)=source(b)

as ordered endpoint TUPLES. Each input record comprises one occurrence from each original triangle; both component paths must compose. This gives exactly nine admitted candidates, one successor per input tuple, and 72 excluded candidates. The excluded records, their coefficients and reasons remain stored alongside the complete parent packet.

Independent comparison records had concatenated arity-four endpoints. A COMPOSED record instead has source(a) and target(b), both arity-two tuples, while retaining the four occurrence IDs and both parent IDs. The checker validates this change in type instead of merely filtering and calling the old concatenated endpoints a composition.

The endpoint incidence matrix M is derived from those tuples and equals C_left tensor C_right. It is not a new fitted coupling. On the 81 candidate coefficients the restriction simply selects the nine admitted coordinates. Selection is linear on that OUTPUT space, so it commutes with summing all spectral products. Exact checks verify the restricted reconstruction square on all 81 input basis pairs. Restricted spectral terms need not remain orthogonal: their amplitudes are summed before any squared norm is taken.

### Fixed reader control

Keep the original candidate measure 1/81. Define the joined aggregate as the SUM of admitted coefficients divided by 81, not by nine. This is a filtered response with a fixed measure; excluded candidates are not being asserted to have executed with zero physical response.

For bilinear coefficients this reader is

    J(x,y)=x^T M y / 81.

There is no complex conjugation in this formula: it is the same bilinear payload rule as the independent comparison, not a Hermitian inner product.

Use x=e_(AB,BA), x'=D x, and the SAME y=e_(BC,AD). Their current same-mode readings agree exactly. The results are:

| Operation/readout | x,y | x',y |
|---|---:|---:|
|Independent product, full aggregate mean|1/81|1/81|
|Endpoint-restricted sum, fixed denominator 81|1/81|1/243|
|Admitted-only mean, reported separately|1/9|1/27|

The fixed-reader difference is 2/243. Hence the difference is not produced by changing the denominator. An entirely hidden pair also yields joined aggregate 2/243 while its independent aggregate is zero.

### Which terms account for the difference?

In this fixture D is real symmetric and commutes with M. The aggregate mixed terms vanish:

    J(Dx,Ry)=J(Rx,Dy)=0,
    J(x,y)=J(Dx,Dy)+J(Rx,Ry).

The RR term is nonzero in general. Thus discarded residuals can influence a later aggregate through their paired contribution, although each remains invisible to its individual D-reader. This does not contradict the earlier DTR=0 result for linear local controls: this operation is bilinear and uses an output incidence restriction.

The incidence itself still factorizes as the two triangles' local successors. The test does not establish an irreducible seam coupling, a triangle-specific force, or the physical selection of endpoint composition. It establishes an exact observation distinction between two declared operations on the retained relationship.

### Recovery controls

Admitted records and the excluded-candidate ledger together recover the full original 81 candidate coefficients. Both complete input packets remain accessible. Dropping an admitted row, dropping an excluded row, or forging a composed endpoint is rejected. The candidate-coordinate squared norm splits between admitted and excluded coordinates; selecting only admitted coordinates is not a norm-preserving evolution.

## Follow-up: minimal coefficient state for a specified probe interface

Keep the SAME fixed-measure bilinear reader J(x,y)=x^T M y/81. Now hold x unknown and vary a known probe y. Probe availability is an explicit experimental assumption here, not native admission supplied by the seed.

Three probe families were checked:

| Declared probe family | Observation rank over the complex coefficient field | Undetectable coefficient subspace |
|---|---:|---|
|All nine occurrence-pair basis probes e_j|9|Zero|
|Same-mode probes D e_j|3|im(R), dimension six|
|Residual probes R e_j|6|im(D), dimension three|

The nine labelled D e_j reduce to three distinct probe vectors in this fixture; they span im(D). They are not renormalized between trials. Allowing all linear combinations in the stated probe subspace produces the same observation kernel.

### Exact reconstruction maps

Writing each profile as a column indexed by the known probe label,

    b_full(x) = M^T x / 81,
    b_D(x) = M^T D x / 81,
    b_R(x) = M^T R x / 81.

The identities for the restricted profiles use the checked rational symmetric projectors and their commutation with M. Since M is a permutation matrix,

    81 M b_full(x) = x,
    81 M b_D(x) = D x,
    81 M b_R(x) = R x.

Thus the three-channel coefficient state is sufficient and minimal AS A LINEAR SUFFICIENT REPRESENTATION for this same-mode probe interface. It is insufficient for the full occurrence-probe interface, whose observation map is injective. Any linear summary that preserves every full-profile response must have rank at least nine. This is not a claim about arbitrary encodings, physical memory units, detector precision or a state preparation mechanism.

Removing any one basis probe lowers the full-profile rank to eight. For each of the nine removals the checker supplies a nonzero coordinate state invisible to all remaining probes. Conversely, the complete ordered profile exactly reconstructs arbitrary complex coefficients. An incorrectly permuted profile fails the fixed decoder, showing why known probe labels and calibration cannot be discarded.

### What 'hidden' now means

Hiddenness is relative to the permitted comparison contexts. A nonzero residual is indistinguishable from zero for every same-mode probe but distinguishable with the complete occurrence-probe family. This strengthens the earlier single hostile into an all-input observation-kernel result.

These statements cover the declared one-step comparison interface and its linear span of probes. They do not assert closure under arbitrary future constructors that could generate new contexts. The already checked local slot controls preserve the same-mode sector; a different admitted operation must be audited separately.

Responses are complex amplitudes under the fixed known gain 1/81, not intensities or automatically available physical measurements. Coefficient tomography also does NOT reconstruct fresh identity labels, history windows or execution provenance: these remain separately retained inputs even when x is fully recovered.

## Retention remains necessary even with full output coefficients

B(2x,y/2)=B(x,y). Hence output coefficients alone do not recover the input pair. The successor retains both complete input packets, not just their product values or root IDs. Each packet retains all spectral components, the ordered occurrence manifest, and references to registered mode records/history windows.

The decoder validates structural output rows and parents, channel-pair products, and input history bindings. Missing channels, omitted rows and corrupted parent links are rejected. Equal projector matrices are never used to merge histories.

These are structural comparison records, not freshly executed primitive events. Deterministic tuple IDs in the existing constructor must not be confused with runtime execution receipts or a new physical clock.

## Result and open gate

There is now an executable conditional bridge from the full retained spectral packet to ONE actual successor constructor. It establishes the commuting representation square, exact output typing and observation-dependent need for residuals.

It does not select independent-family comparison as the intended horizontal generator, provide calibrated units or choose the physical reader. For independent pairing, a coarse aggregate observation and a fine target-family observation give different information requirements. For endpoint-compatible composition, even the fixed aggregate depends on a joint residual contribution. Neither the operation nor its physical reading is selected merely by making the square commute.

## Verification

    python research/nima/checkers/check_spectral_successor_bridge.py

Fresh exact checks pass. Importing the existing recursive comparison module also reruns its original full/omitted-arrow regression. The tests cover all 81 basis pairs, complex coefficients, tensor norm identities, full parent recovery, four-sector reconstruction, reader closure/nonclosure and five malformed-packet controls. The endpoint follow-up additionally checks nine admitted/72 retained excluded candidates, composed endpoint typing, the restricted spectral square, aggregate DD/RR decomposition, the fixed-denominator hostile and three selection-ledger rejection controls. The contextual-observation extension checks exact ranks 9/3/6, matrix decoder identities on the full carrier, all nine single-probe deletions with invisible-state witnesses, complex-state reconstruction and a probe-label corruption control.

Report: `results/spectral-successor-bridge.json`.
