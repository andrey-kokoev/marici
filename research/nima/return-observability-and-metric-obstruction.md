# Return observability and the history-metric obstruction

## Instantiate the readout from existing data

The assembly already supplies actual leg maps, the independent reference,
137 slot responses and109 factored mixed responses. The weak-return construction
adds actual round-trip defects r*d-1 and d*r-1, plus reference drift d*r*d-d.
All are functions of the retained degree-zero maps.

Changing unit witnesses by closed terms leaves their boundaries fixed. At fixed
actual maps and return, it therefore leaves these response observables fixed.
The current slot and rectangle readouts add no sensitivity to an independent
closed unit-history edit. This statement concerns the specified response maps;
a direct observation of history coefficients would be a different observable.

## Exact pullback test

In the singular-reference DG fixture, degree-one A-side and B-side witness
spaces each have dimension14. The degree-two triangle space has dimension10.
Thus the policy's coefficient space has dimension38.

The tangent equations for a coherent history change are

    delta(du)=0, delta(dv)=0,
    delta(dW)=d*du-dv*d.

Their exact rank is24, leaving14 admissible history directions. Every one lies
in the kernel of the round-trip residual readout

    L(du,dv,dW)=(delta(du),delta(dv)).

A triangle's boundary observed through a further boundary readout also vanishes,
since delta^2=0. L has rank20 on the unconstrained coefficient space, but is zero
on the entire14-dimensional coherent-history tangent. Even locking both unit
histories leaves six independent closed triangle directions.

Consequently, for any positive metric G on these response channels,

    ||L(change)||_G^2=0

for all those admissible changes. Pulling back the existing residual readout
cannot yield the strictly positive history metric used by the earlier policy.
Its coefficient norm assigns positive cost to each nonzero tested direction.
These are different metrics measuring different data.

## What the test does and does not identify

The original137-slot matrix assembly and the singular-reference DG fixture are
separate constructions. The checker makes no identification of their chain
spaces. The linkage used here is a dependency statement: the specified slot and
mixed-response formulas depend on actual maps, not on an independent choice of
unit-history coefficient. Additional coupling of that history to actual maps
would be a new dynamical law and could change this conclusion.

In particular, two previously accepted coherent versions with different unit
histories and different coefficient costs have identical unit-boundary responses.
The protected-weighted-mean policy was a consistent declared selector, rather
than a physical metric derived from those residual observations.

## Symmetry leaves another normalization choice

Carrier relabelling preserves arrow/state comparison kind. A metric with a
constant positive weight a on arrow slots and b on state slots is invariant
under kind-preserving permutations for any such a,b. Hence this symmetry alone
does not select their ratio. Equal slot weights remain a stated normalization
choice until a metric or physical measurement principle supplies them.

The test checks representative block permutations for two different positive
weight choices; invariance under every such permutation follows directly from
constancy within each block. No enlarged label symmetry is asserted as physical.

## Synthesis consequence

There are three concrete routes beyond the obstruction:

1. Introduce a history-sensitive observable or dynamics coupling history into
   the existing response, with an independently specified measurement law.
2. Transport a separately supplied retained-record metric, identifying its
   physical meaning and units rather than extracting it from residuals alone.
3. Treat the hidden histories as observationally equivalent for this readout,
   while retaining them for reconstruction. Constants extracted solely from
   that readout must then be independent of the history selector.

The new result is a precise limit on the proposed metric derivation. Algebraic
coherence and retention do not determine a positive physical cost for changes
that the current observables cannot see. No additional constant prediction is
obtained by selecting arbitrary weights on these directions.

## Verification

    python research/nima/checkers/check_return_observability_metric_gate.py

Exact ranks20 and24, a basis of14 admissible invisible directions, six residual
triangle freedoms with locked units, positive coefficient-cost versus zero
response-cost comparison, distinct coherent versions with equal observed unit
boundaries, all137 matrix slot and109 mixed-response formulas, and block-weight
symmetry controls. Prerequisite policy and shared-leg checks also run.
