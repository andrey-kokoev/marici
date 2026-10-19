# Iteration5: executable native attachment and an action-section obstruction

## Fresh obligation and result

The freshly read36-node net recommended completing the relation binding by executing the retained source action rather than merely storing its matrix. This is now done for the fixed local source witness, with a fresh safe Cubical Agda closure.

`NativeRelationAttachmentAction.agda` reads the source-computed matrix directly from `Case.attachment ActualRelationPacketCase.actual`, interprets it on signed integer coordinate triples, and retains the original certified native answer alongside every input/output execution. It does not introduce a second independent fitted action matrix.

## Actual action and recovery

The fixed basis is (a,b,v), where v=ab is the previously checked four-event nonzero source product. The exported actual right-b action computes

    R(x,y,z) = (0,0,x).

The exported disconnected graded action computes zero. These formulas are proved by reduction from the serialized actual matrices, for every integer triple. Theorems additionally check R(a)=v and R squared=0.

`complete-action(c,v)` is an existing Complete package containing the original Answer(c), prior coordinate value, resulting value and action agreement. The native packet, original input and action are recoverable. In particular `retained-action` proves that reading and executing the action from the retained original case gives the same result after packaging. The two raw cuts, source factors and balanced certificates remain in that case.

The matrix decoder has default branches for malformed data; no correctness claim is made for an arbitrary malformed Case. The reduction theorems bind the evaluator specifically to the live-source-checked exported case. Python remains responsible for identifying that literal matrix with multiplication in the original path algebra.

## Formal no-section theorem

Let Q(x,y,z)=(x,y). The induced right-b action on the quotient is zero. Suppose a proposed section sigma:Z^2->Z^3 satisfies:

1. Q(sigma(q))=q;
2. sigma(0)=0;
3. R(sigma(q))=sigma(0), preserving that right action.

At q=(1,0), property1 forces the first coordinate of sigma(q) to be1. The actual R then has third coordinate1. Properties2 and3 force that coordinate to be0. `no-action-section` derives1=0 and contradiction.

This even excludes zero-preserving nonlinear sections with these equations, so in particular excludes an action-preserving linear section in this local integral model. It is not a fresh general Ext proof for the full source ideal. The owning nonsplitting theorem supplies that larger result at its stated scope.

`no-disconnected-substitute` independently rejects replacing the actual action with the disconnected one while claiming agreement on a. Thus the retained action is not decorative provenance: an admitted continuation detects its removal.

## Parent binding disposition

At the requested finite-witness scope, `relation-layer-wg-binding` is now constructed:

- actual four-event nonzero relation product and local attachment action;
- smallest five-event extension for genuinely distinct balanced cuts;
- exact source-generated coefficients and nonzero detector;
- native Layer1/Complete encoding retaining both histories;
- executable native local action and exact recovery;
- an action-preserving-section impossibility witness.

The verification split remains explicit: Python checks the original multiplication, recorder/seam algebra and exporter; Agda checks literal source data, typed endpoints/equalities, native package/operation recovery and the universal local coordinate obstruction. Neither verifies a new complete analytical receiver, the full source algebra inside Agda, an arbitrary WG phase law or a137-record identification.

The broader governing root stays open because the intended generative rung schedule and common continuation interface are not yet assembled. The next recommended root-relevant frontier is `generative-rung-leaf-schedule`, not another local attachment wrapper.

## Verification

Executed `python research/strominger/checkers/check_native_relation_attachment_action.py`.

The runner rechecks the live-source export and its finite controls, then runs Agda --safe --cubical --guardedness --ignore-interfaces. Exit0, passed=true, inputs_stable=true. The existing nonfatal owner import warning remains. Receipt: `research/strominger/results/native-relation-attachment-action-agda-v1.json`.

No owner source implementation, physical interpretation, source-policy selection or missing free-seed face was changed.
