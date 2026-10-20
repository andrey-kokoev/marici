# Nonidentity source comparison is internalized, with a retained interchange witness

## Result

The seed's nonidentity source comparison is now an ACTUAL native comparison
operation inside a recursively retained package type, not only an external
transport on descriptions. Native attachment can follow it. Moreover, the two
routes 'attach then compare' and 'compare then attach' have a derived,
source-port-preserving equivalence that is itself compiled through the native
comparison rule.

The two route packages remain provably unequal as retained Complete objects.
The new comparison stores both route derivations; it does not erase their
construction order.

The positive result is relative to the declared source modes (identity and the
seed symmetry) and an explicit TARGET-SIDE continuation convention. Existence
of an equivalence alone does not select which side of a comparison should supply
its next boundary.

## A retained internal interface, not a fresh seed adapter

`InternalSourceComparisons.agda` defines an inductive-recursive Body indexed by
its active source vertex. A prepared input stores:

- its actual Complete package q;
- its actual Resolve Seeds q derivation;
- a port reader on the ENTIRE interpreted value carrier;
- evidence that the selected value reads as the indexed boundary.

An attachment retains its entire previous Body and an actual outgoing source
edge. A comparison retains both complete prior Bodies, the chosen source mode,
an equivalence e, its selected-value witness, and a whole-carrier port law:

    act(mode,read_left(x)) = read_right(e(x)).

Neither operands nor their readers and native derivations are discarded. The
native compiler applies the existing E/reflexivity and compare rules recursively,
using the actual prior derivations. No new source seed is looked up after input
preparation.

The initial nonidentity instance uses sigma=(A B)(C D), its actual equivalence,
and the previously declared graph-retaining vertex packages. It is compiled as
compare-rule, not mistaken for a primitive edge CD or DC or a physical traversal.

## Continuation and source compatibility

A comparison carrier contains (x,y,witness:e(x)=y). Its active reader is explicitly
read_right(y). The source-side reading remains available through the retained
left operand and x. The module proves on EVERY comparison value:

    act(mode,read_left(x)) = read_right(y).

Thus the comparison does not merely match its selected endpoint while violating
source readings elsewhere. The existing unrestricted native comparison rule
alone does not impose this requirement; the source-aware Body interface does.

For the A->B comparison, target-side continuation permits BA or BC. Using AD
from the old A boundary is rejected. A source-side continuation interface could
be defined differently, but changing between them would require an explicit
policy/witness rather than an unnoticed decoder change.

This preserves the previous exact-attachment contract: the outgoing family is
Out at the DECLARED active boundary. It does not prove that target-side rather
than source-side continuation is uniquely forced by the bare source.

## Derived interchange, with no guessed higher filler

Start with any admitted source-compatible pointed comparison a->b in this
interface, and a source edge o at a's boundary. Two native routes are available:

1. Attach o to a and its transported edge to b, then compare the attachments.
2. Internally compare a to b, then attach the transported edge to that result.

The module derives the comparison between these routes from:

- equivalence of the source outgoing-edge fibers;
- the original pointed equivalence and its port witness;
- the existing equivalence-induced path lift;
- equivalence between a comparison graph and its source carrier.

The graph contraction keeps its equality witness explicitly during the proof.
Pointed loop transport uses the actual supplied point path. It does NOT assume
arbitrary loop spaces are contractible or truncate proof-relevant paths.

The resulting interchange equivalence has a proved selected-value law and a
proved port-preservation law. It therefore supplies all fields of another
internal comparison, whose ACTUAL native derivation is built from the two
route derivations. No independent arbitrary interchange filler is assumed.

## Both routes survive the witness

A reader of the actual compare-rule premises recovers precisely the two native
endpoint-and-derivation pairs for the routes. Reification retains the Body and
its complete native closure as well.

Separately, Agda proves that the route packages are not literally equal: the
first has an outer comparison code, the second an outer E code. Consequently
this result is a specified comparison between retained histories, not permission
to identify or quotient away those histories.

Internalizing a reversible comparison is itself a retained construction. Repeating
it can add more comparison provenance even when the underlying source vertex map
returns to its starting point. No involution law for complete construction
histories is inferred from sigma squared being identity on vertices.

## Concrete continued instance

The supplied instance starts with the A->B seed comparison and edge AD. Its
transported edge is BC. Both routes reach the active C boundary, and their
interchange comparison is an actual Body at C. A further native attachment CA
is then derived, yielding a Body at A.

Every intermediate operand, comparison, edge witness and native derivation
remains retained. Positions in this construction express typed dependence,
not physical time or event issuance.

## Scope of the conjecture test

The local internalization test now succeeds:

    source-compatible nonidentity comparison
      -> native retained comparison operation
      -> admissible continuation
      -> derived comparison between construction orders
      -> further native continuation.

The source policy is not hidden: permitted source modes, full port compatibility,
and target-side continuation are explicit. Exact attachment representation
continues to apply at the selected boundary, but the preference for that boundary
convention is not derived here.

Remaining claims include coherence among multiple interchange witnesses,
compatibility with arbitrary source isomorphisms, and derivation/selection of
more general task policies. No universal internalization theorem or arbitrary
higher filling is asserted.

## Verification

    python research/strominger/checkers/check_internal_comparison_interchange.py

Fresh headless Agda closure with `--ignore-interfaces` passes under Agda 2.8.0.1 /
Cubical 0.9. New modules use safe Cubical/guardedness with no postulates or holes
and introduce no unsupported indexed-match warning.

Two intended negative controls are rejected (exit 42 each):

- attaching unmoved AD after the internal A->B comparison;
- using tau=(A B), fixing C,D, while claiming the whole-carrier port law of sigma.
  Tau matches the selected A->B points but fails the declared source comparison.

Finite controls exhaust 12 source/mode/selected-edge interchange instances and
20 route-carrier values, checking both inverse laws, pointedness and port
preservation. These are set-specialized controls; the Agda loop construction is
not restricted to sets.

Artifacts:

- `agda/InternalSourceComparisons.agda`
- `agda/InternalComparisonInterchange.agda`
- `agda/negative/InternalBadContinuation.agda`
- `agda/negative/InternalBadPortComparison.agda`
- `checkers/check_internal_comparison_interchange.py`
- `results/internal-comparison-interchange.json`
- `results/internal-comparison-interchange-positive.log`
- `results/InternalBadContinuation-negative.log`
- `results/InternalBadPortComparison-negative.log`

Source hashes are stable across verification. Only Strominger-owned files were
edited; dependency interfaces may be refreshed by Agda. No physical claim,
graph publication, commit or push.
