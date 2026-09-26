# Normalization theorem dependencies and phase semantics

## Precisely scoped target

For every finite bit word w and nonnegative unary indices i,j, the Twin constructor normalizes under any sequence of enabled admitted reductions to two BOOL--OUT pairs with values member(w,i), member(w,j), uniquely up to port/kind isomorphism. This remains a target theorem, not an established result of the bounded searches.

## Dependency ledger

1. Constructor establishes the unified graph invariant and allocator high-water premise: explicit constructor inspected; a general inductive constructor proof is still to be assembled.
2. All fifteen rules preserve that invariant: written conditional boundary cases plus static interface audit and finite/adversarial tests; integrated universal closure argument remains a review gate.
3. Rank (number of original B/N, number of nonoriginal B/N/K) strictly decreases: conditional rule effects establish the arithmetic, provided item 2 preserves the role distinction. COPY removes one original and adds two copied heads; all other rules remove one nonoriginal data head.
4. Local diamonds: written interface/allocator argument, supported by 15,525 exact small diamonds. Its executable premises must remain satisfied via items 1–2.
5. Items 1–4 imply termination and a unique normal form by the terminating local-confluence argument, modulo fresh names.
6. Root/phase conditions imply that a normal form has exactly two BOOL--OUT pairs. This identifies shape, not their values.
7. A value interpretation invariant is needed to identify the two Booleans with indexed membership. This is the least-developed independent arrow and the next substantive leaf.

## Candidate value interpretation

Define M([],k)=false, M(b::s,0)=b and M(b::s,k+1)=M(s,k). Let k denote the number of remaining K nodes. For a query whose support word is s:

* Q_B with budget k denotes M(s,k).
* Q_S with remaining budget k denotes M(s,k+1): its preceding Q_B--K already consumed one budget unit but has not yet skipped the corresponding support bit.
* Q_R denotes M(s,0).
* BOOL denotes its Boolean value at its OUT; eraser components carry no query result.

This offset in Q_S is essential. Q_B--K maps budget k+1 to Q_S budget k without changing meaning. Q_S--B maps support b::s and budget k to Q_B(s,k), again preserving meaning; Q_S--N returns false. Q_B--N becomes Q_R. Q_R--B/N reads b/false.

For a copied support prefix ending at COPY.a/b, interpret its remaining word as that prefix concatenated with the original suffix at COPY.p. A bare wait denotes that original suffix directly. COPY--B preserves this virtual word by transferring its head into the copied prefix while shortening the original suffix; COPY--N replaces an empty virtual suffix with copied NIL. Thus a semantic proof need not assume the copier finishes before either query runs. This virtual expansion is a mathematical interpretation, not extra runtime copying or a claim of retained reusable support.

Next implement this interpretation on live wired graphs, checking each output value against its original (w,index) before and after every tiny rewrite, especially Q_S waits at COPY and query completion while garbage remains. Then prove its seven grouped rule equations under the structural invariant. No link to physical nine-point superforms is asserted.
