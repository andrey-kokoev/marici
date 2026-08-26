# Counterfactual centralizer rigidity

## Bounded question

When does naturality across source variations actually make an explanation
hard to vary? The proposed finite criterion is that the centralizer of the
admitted counterfactual action, restricted by the actual record, contains no
unexplained rival mechanism.

## Four-source attack

Enumerate all 256 mechanisms from the source set `{0,1,2,3}` to itself. Require
the actual record `f(0)=0` and naturality--commutation--with admitted source
transformations.

The actual record alone leaves 64 mechanisms. Admit swaps inside two
disconnected source components, `0 <-> 1` and `2 <-> 3`. The actual record
fixes the first component, but a nonidentity rival can still swap the second
component. Naturality is therefore still too cheap.

Add the bridge swap of sources `1` and `2`. The three swaps generate a connected
counterfactual action over all four source values. Among actual-fit
mechanisms, their common centralizer is now exactly the identity.

## Explanatory reading

This sharpens the previous source-family result. A list of counterfactuals is
not enough. What matters is the residual mechanism space that commutes with
them:

```text
explanatory rivals = actual-fit mechanisms intersect counterfactual centralizer
```

The explanation is rigid in this finite model exactly when this set is a
singleton. A nontrivial centralizer is the control-theoretic analogue of an
unobservable mechanism symmetry: the admitted criticism operations cannot see
how the explanation was varied.

For Marici, the source-variation structure therefore needs a discrimination
claim, not merely an existence claim. Its transformations should be jointly
faithful on the declared rival class. This does not authorize adding arbitrary
interventions until uniqueness appears. Each generator must be independently
source-admissible; otherwise the construction only encodes the desired
answer.

## Claim boundary

Connectivity is sufficient in this particular four-point permutation model,
not a universal criterion. In other actions, a connected or transitive source
orbit can retain a nontrivial centralizer. The general candidate is
centralizer rigidity relative to a frozen rival class and admitted criticism
algebra.

An initial three-source version of this packet predicted that a disconnected
orbit would retain a rival. Exact enumeration refuted it: fixing source `0`
and commuting with `0 <-> 1` already forced the isolated third point to remain
fixed. That failed formulation is superseded here, not counted as support.
The next falsifier should seek a transitive admissible action with multiple
actual-fit natural mechanisms, or prove why exact base fixation forbids one.

## Verification

```text
python research/sontag/checkers/counterfactual_centralizer_rigidity.py
```
