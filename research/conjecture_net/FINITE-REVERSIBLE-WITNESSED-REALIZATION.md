# Frozen first theorem: finite reversible witnessed realization

Contract: `contracts/finite-reversible-witnessed-realization.v1.json`.
Checker: `research/voevodsky/checkers/check_finite_reversible_witnessed_realization.py`.
Receipt: `research/voevodsky/results/finite-reversible-witnessed-realization-v1.json`.
Run: `python research/voevodsky/checkers/check_finite_reversible_witnessed_realization.py`.

## The exact proposition

For every k>=1, every bijection f:{0,1}^k->{0,1}^k and every a, there is a uniformly compiled finite word over NOT, CNOT and Toffoli which:

1. maps (x,0_work) to (f(x),0_work) for EVERY x;
2. reverses to implement f^-1 with clean work;
3. constructs the retained graph presentation C_f={(x,y):y=f(x)} and the common mark (a,f(a));
4. realizes both triangle returns through C_f;
5. preserves extensional composition and every specified continuation/readout on the logical data.

The compiler uses at most max(k-3,0) clean work bits. The source primitive set and target class are independently fixed. An arbitrary permutation table specifies the target; it cannot be executed as a primitive gate.

This freezes a bounded foundational instance in the familiar finite reversible-circuit model. It does not redefine the universal common-process conjecture. The construction uses standard reversible universality; the contribution here is the precise retained-realization interface and its explicit comparison tests, not a claim of a novel universality theorem.

## Uniform constructive proof

### Permutation decomposition

Start with the identity table. At input x, if the current output is u rather than f(x)=v, transpose output labels u and v. Neither is the already fixed output of a previous input, so earlier entries remain fixed. The last entry follows from bijectivity. At most 2^k-1 transpositions produce f. This is a terminating finite algorithm, not a search assumption.

### Transposition by a Gray path

Choose the path from u to v which flips differing bits in increasing bit-index order. Let its length be h<=k. Apply its first h-1 adjacent swaps, then its last swap, then undo the first h-1 in reverse order. This exchanges only u and v and restores every intermediate/spectator label. It uses 2h-1<=2k-1 adjacent swaps.

### Adjacent swap by frozen primitives

An adjacent pair differs in one target bit. Its remaining k-1 bits form a prescribed control pattern. Flip each negative control by NOT, perform a positive multi-controlled NOT, then undo those NOT gates.

For d=k-1 positive controls:

- d=0: NOT;
- d=1: CNOT;
- d=2: Toffoli;
- d>=3: compute successive conjunctions into d-2 clean work bits, flip the target using the final conjunction and last control, then uncompute the conjunction chain.

The chain uses 2d-3 Toffolis and restores every work bit to zero for arbitrary logical input. Thus max(k-3,0) clean work bits suffice for every adjacent swap and can be reused for the whole word. Each source gate is an involution; the reversed compiled word supplies the inverse on the clean logical subspace.

Let b(k)=2(k-1)+1 for k<=3, and b(k)=2(k-1)+(2k-5) for k>=4. A conservative uniform gate bound is

    L(f)<= (2^k-1)(2k-1)b(k).

This is an abstract gate-count budget, not physical time or energy.

## A substantive third presentation

The source and target each have the logical carrier B_k, but C_f is a constrained ordered pair of registers retaining BOTH coordinates:

    ac(x)=(x,f(x)),       ca(x,y)=x,
    bc(y)=(f^-1(y),y),    cb(x,y)=y.

Prepare ac by CNOT-copying the computational Boolean register x to a clean second register, then executing the compiled f on that second register. This is the reversible classical basis operation (x,0)->(x,x); it is not cloning arbitrary unknown quantum states.

Prepare bc by copying y into the first register and executing the inverse word there. Both graph preparations use 2k data bits and the same m work bits.

On the graph subspace, ca is implemented by reversing ac preparation, leaving (x,0); cb is implemented by reversing bc preparation, leaving (0,y). No nonzero coordinate is discarded. The bare projections on arbitrary ambient pairs are not the reversible source operations.

The equations follow for every input:

    cb o ac=f,       ca o bc=f^-1,
    f^-1 o cb o ac=id_A,
    f o ca o bc=id_B.

The common constructive center is exactly

    m=(a,f(a))=ac(a)=bc(f(a)) in C_f.

It is not an arbitrarily selected terminal object or an unspecified geometric barycenter. Its two coordinate roles and construction witnesses are retained. Abstract equivalence of C_f with B_k does not erase that presentation.

## Coherence and continuation scope

The target here is finite SET-level mathematics: equality of functions is extensional equality, and its proofs are propositional. Consequently compatible inverse/triangle certificate equalities have no independent higher choices at this scope. The actual identities above supply their parallel boundaries; proof irrelevance at the declared level supplies the coherence of those equality witnesses. This first theorem is not a model of nontrivial higher path families.

For any subsequent bijection h, the compiled f followed by compiled h evaluates to h(f(x)), with workspace clean between them. Compiling the table h o f separately gives the same full logical action. This is semantic composition preservation; the resulting gate WORDS need not be syntactically identical.

For every predicate/readout p:B_k->Bool, action equality gives p(eval(compiled f,x))=p(f(x)). Equality of successor states similarly preserves all finite future permutation words. This supplies every continuation in the frozen target class, not just the sampled regression continuations.

Input recovery requires retaining the bridge: f^-1(f(x))=x. Output alone does not reconstruct arbitrary circuit genealogy. Empty word and NOT;NOT are distinct source words with identical full extensional action. Therefore no decoder of that action recovers both words. This historical distinction is not automatically observable by the frozen EXTENSIONAL continuation family; demanding history inspection would enlarge the target interface.

## Verification and verdict proposal

The checker exhausts every permutation for k=1 and k=2, samples deterministic families for k=3,4,5, and checks every logical input for every case. It checks clean forward/inverse action, both graph preparations and recoveries, common marks, triangle returns and composition/continuation squares. Gate-deletion and unclean-work mutations are detected.

The written uniform construction gives an all-k proof candidate at ordinary finite constructive mathematics level; the exact checks are bounded regression, not its universal inference rule. No proof-assistant all-k certificate or shared outcome admission has been produced.

## What is now decided and what remains the next frontier

The source calculus, target class, graph presentation, center, continuation semantics and resource bound are now fixed. The claim has no unspecified P, C or notion of identity at this scope.

The next foundational strengthening is an explicitly higher target whose continuation uses a nontrivial path/filler witness. There the set-level proof-irrelevance shortcut no longer supplies the required coherence, and erased comparison structure can affect future capability. The retained tetrahedral and dependent-transport research supplies candidates for that next target, without changing this first theorem's definitions.
