# Actual opposite observer transports source actions and relations

## Construction

Reverse each source word and its retained-mark sequence, and send corner (a,b) to (63 xor b,63 xor a). Attach each original coefficient functional to the reversed path with its original fixed analytical coefficient. This constructs the formal opposite observer Oop with Oop(Rx)=O(x).

Reverse a source action by exchanging left/right and sending its edge start a and event i to start 63 xor (a union {i}), with event i and retained mark unchanged. Matrix entries retain their values and row indices.

## Fresh exact checks

The checker uses the actual base and three aggregate frame exports:

- 3,591 coefficient rows;
- 6,001 action entries checked separately in each orientation;
- 26,083 word/mark cut identities;
- all 51,550 exported source-ideal generators reconstructed after reversal in the opposite corner's rational ideal basis;
- exact double reversal of every row and action.

Action verification independently strips the first or last event from the raw functionals and compares the result against the exported sparse matrices. It exhausts both expected and supplied action groups. Analytical window recipes are treated as opaque fixed scalars, with rho and sigma tracked as formal monomials. The resulting identities hold without choosing calibration values.

The opposite rows and actions are exported in `results/formal-actual-opposite-observer.json.gz`. Input digests and the deterministic packet digest appear in `results/actual-opposite-observer-transport.json`.

## Meaning

The previous same-observer reversal obstruction is compatible with this construction: the opposite observer carries the reversed kernel. The checks establish actual finite algebraic transport rather than a freely chosen coordinate permutation fixture.

Reversal of concatenation exchanges the order of factors. Together with preservation of the source ideal this gives algebraic preservation of its powers on the admitted square-free source domain. Explicit transport matrices for the exported J1/J2 presentations remain to be constructed. The run verifies membership against the existing exported basis; it does not rebuild that basis or its completeness certificate.

## Remaining conjecture gates

The formal opposite keeps each original coefficient value attached to its reversed path. An admitted reversed measurement recipe must justify that assignment from its own constructors, window semantics and calibration. The construction supplies no such acquisition certificate yet.

The causal certificate-availability result introduces an additional structured object: evidence incidence at observer events. Logical reversal of a causal diagram produces its opposite diagram. Admission of that opposite as a reliable-message protocol requires its own constructors. In particular, changing the orientation of a send/receive edge does not establish that a certificate is available at the new sending event. This causal admission gate remains open.

Thus source-ideal membership, raw observer functionals, generator actions and double reversal have fresh positive certificates. Full protocol-level opposite-observer admission remains unresolved.

## Reproduction

    python research/voevodsky/checkers/check_actual_opposite_observer_transport.py
