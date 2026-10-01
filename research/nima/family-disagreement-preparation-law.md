# A state-derived preparation: retained family-disagreement feedback

## Prior-source reuse update

The [exchange-to-feedback test](exchange-feedback-adapter-and-covariance.md)
now derives the averaged law of the older reversible carrier/record model.
That source already supplies endogenous increments, but its mismatch mean
operator does not preserve these family means. The natural linear adapter
fails. The relaxation below remains a distinct conditional model, not the
established reduction of the prior exchange dynamics.

## The added principle

Choose the following explicit source-model candidate: reduce disagreement
within each retained incoming family of primitive legs, while preserving its
member-weighted mean and keeping the old records. This is a relaxation or
calibration postulate. It is not implied by family promotion alone and is not
yet identified with a physical apparatus or dynamics.

Use the actual30 shared legs of the137-slot fixture. Arrow legs group by their
carrier target, separately for each leg role; state legs have singleton groups.
All member masses are the original unit masses. Let P replace each member value
by the mean of its own family. This induces precisely the32 target families of
the existing comparison-slot fixture, not the earlier leg-index partition.

## B is now calculated from the current records

For a common witness action T_h and a declared relaxation gain eta, set

    B_i(A,h) = eta * [(P T_h A)_i-(T_h A)_i],
    A'_i = (T_h A)_i+B_i(A,h).

The grouping projector commutes with the common witness action. Thus B is a
state-dependent feedback increment, not an independently fitted matrix at each
step. The remaining choices are the relaxation principle, grouping policy and
gain. This construction does not determine initial amplitudes.

For h=identity,

    A' = P A+(1-eta)(I-P)A.

Every family mean is preserved. At eta=1 the active fields become family means,
but retained kicks recover the old members exactly via A=A'-B. With a witness
step, apply its inverse after subtracting the retained kick. The old disagreement
is archived, not erased from the full state.

## Controlled disagreement decrease

Use the positive matrix inner product

    <X,Y> = tr(G^-1 X^T G Y),   G=[[2,1],[1,2]].

This is invariant under the declared S3 conjugation action. It is a mathematical
control metric, not an identified physical energy. The family projector is
orthogonal for the unit-member-weight sum of these inner products. For

    E_leg = sum_i ||A_i-(P A)_i||^2,

one update gives

    E_leg'=(1-eta)^2 E_leg.

Hence0<eta<2 contracts active disagreement. Restricting0<=eta<=1 additionally
makes each step a convex mixture of the member and its family mean. This is not
an assertion about thermodynamic dissipation or the cost of retained history.

For a fixed partition, two gains compose as

    eta_combined=eta1+eta2-eta1*eta2.

No physical clock is selected by this identity. It does not apply unchanged
when the grouping policy changes between steps.

## The actual comparison response remains factored

Write primitive legs in a target family as x=xbar+dx and y=ybar+dy. After a
relaxation step, q=1-eta gives

    y'x' = ybar*xbar
           +q*(ybar*dx+dy*xbar)
           +q^2*dy*dx.

Thus the product and its interaction term are calculated from updated shared
legs. All137 slot matrices remain factored; none is updated independently.
Every original target-family slot mean and the total mean remain unchanged.
The mean relative to the fixed d4 therefore remains unchanged as well. A common
witness transport acts covariantly on these statements.

Under the existing complete-product families, the linear and bilinear
fluctuations are orthogonal in the summed control metric. Consequently

    E_slot' = q^2 E_linear+q^4 E_bilinear.

At full relaxation every slot equals its original target-family mean. This
removes within-family disagreement, not necessarily differences between families
or all of the global mixed rectangle responses. The nonlinear slot terms are
forced by the shared-leg composition, not independently selected couplings.

## Scope and physical decision

This supplies an executable B-law using data already present in retained
comparisons. It preserves means, respects passive carrier relabelling, commutes
with a common witness action and supports exact historical reconstruction.
The checker verifies the original excluded-edge marking is transported with
relabelling rather than silently restored.

Family-constant fields receive no preparation at all. Thus this law relaxes an
existing preparation; it does not create amplitudes from zero, choose their
family means, or derive a physical constant. Nor does it force those means to
equal the physical reference. The control metric and gain require a physical
interpretation before this becomes a physical dynamics claim.

The next source-instantiation test is whether an actual comparison/calibration
operation implements this family feedback. If not, reject the relaxation
postulate rather than adjusting it to a desired readout. Nonuniform member
weights, changing partitions and independently varying witness actions would
need additional checks; they are not claimed by this fixture.

## Verification

    python research/nima/checkers/check_family_disagreement_preparation.py
    python research/aspect/scc/scc.py check nima-family-disagreement-preparation

Exact rational checks cover30 legs,137 slots and32 target families; computed
kicks and member recovery; all family/global means; leg and slot disagreement
scaling; composed gains; all six common witness actions; all24 carrier
relabellings; and zero-drive family-constant controls.
Machine result: `research/nima/results/family-disagreement-preparation.json`.
