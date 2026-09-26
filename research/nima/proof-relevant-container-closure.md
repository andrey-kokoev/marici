# Closure with retained comparisons and comparisons of comparisons

## Source record

For fixed complete routes a,b:Q~=N, a source/comparison package has the dependent form

R := Sigma(q:Q). (a(q)=b(q)),

with the complete intermediate a and b chains and their reconstruction maps retained as named fields or fixed indexed data. In the executable test these fields are stored explicitly in each record. The equality witness is data; it is not replaced by an inhabited/not-inhabited flag.

A next record can retain r:R, two comparisons p,q with the required common endpoints, and a field gamma:p=q. The last field can be empty. Forming its type does not choose an inhabitant. A recursive record grammar can contain these identity fields as atomic types for Sigma/Pi repackaging while preserving their endpoints and dependencies.

## General HoTT bridge

For an equivalence e:X~=Y and x,x':X, path application supplies an equivalence

ap_e : (x=x') ~= (e(x)=e(x')).

If g is an inverse of e and eta_x:g(e(x))=x is its inverse homotopy, the inverse path map has the form

r |-> inverse(eta_x) concatenated with ap_g(r) concatenated with eta_x'.

The equivalence laws provide the needed higher comparisons. Applying the same fact to these path-space equivalences transports identities between paths, and then their identities, at every specified finite level. This is a standard identity-transport argument written here as the bridge obligation; no proof-assistant certificate is claimed.

Likewise equivalence-based reindexing gives

Sigma(x:X). W(x) ~= Sigma(y:Y). W(g(y)),

with the appropriate inverse-homotopy transports. This accounts for the dependence of the witness fields on their source. An implementation must retain these transports or choose a strict semantic model in which they compute to identities.

Thus two tasks are distinguished operationally: the normalizer repackages dependent records, while identity transport moves their proof fields across established equivalences. Together they specify how a complete witness-bearing record remains usable at the next finite level.

## Nontrivial finite test

The previous finite dependent example had 18 discrete source values. For this experiment explicitly enrich each component to the classifying groupoid BC2. Every source has two self-comparison arrows, labeled 0 and 1, composing by XOR. The previously constructed source/normal-form bijection extends to a groupoid isomorphism by preserving each arrow label.

This is new declared comparison structure, not a deduction that the original set had nontrivial identity paths. It provides 36 retained source/chain/comparison records. Their two labels survive normalization and decoding separately. A next record retains its original first-level record, two parallel arrows, and their equality witness. All 36 reflexive higher records round-trip; the 36 attempted equalities between distinct C2 arrows are refused. A groupoid models a 1-type, so higher identities here are discrete. Richer higher types require a stronger backend.

The Python normalizer treats proof-bearing fields as opaque typed-by-contract payloads; it does not itself check arbitrary HoTT typing or construct new higher proofs. The test's Arrow and HigherEquality constructors enforce the declared finite groupoid boundaries.

## Consequence for the proposed tower

The tower can retain previous comparison data at every finite stage through dependent records and equivalence-induced identity transport. This supplies a precise closure specification. It does not imply every proposed coherence boundary has a filler. An empty comparison type remains empty through equivalent presentations.

The next meaningful implementation step is a checked HoTT definition of the record family and the lifted identity equivalences, rather than more finite set enumerations.

Checker: `research/nima/checkers/check_proof_relevant_container_closure.py`.
Result: `research/nima/results/proof-relevant-container-closure.json`.
