# First critical-pair test: reflected paths and generated coherence

Date: 2026-11-09. Status: exact finite constructions, counterexamples, and a conditional general theorem. **Not a proof of the spatial R/B/G conjecture or a Ramsey theorem.**

## Question

Can two separately admitted extensions `a,b` generate (rather than receive) their Green comparison `G`, and does this enforce point-reflected paths and higher triangulated closure?

## 1. A conditional positive construction

Input a set `E={e1,...,en}` of independent extension events. **Additional assumptions:**

- every subset `S⊆E` is an admissible observable state;
- the result of adding different events depends only on `S`, not the order;
- the intended higher simplices are the chains of strict inclusions of states (the order complex/nerve of the Boolean poset).

Let `B_n=(P(E),⊆)`; a vertex `S` has a geometric realization `v_S∈{0,1}^n`. A `k`-simplex is a chain `S_0⊊...⊊S_k`. Each of the `n!` maximal chains gives one `n`-simplex; these triangulate the `n`-cube. No diagonal is chosen by hand *after the poset/nerve construction is stipulated*.

Complementation `c(S)=E\S` is order-reversing, so on chains define `c(S0,...,Sk)=(c(Sk),...,c(S0))`. The embedding realizes this operation as point reflection about `(1/2,...,1/2)`. In the two-extension square, the path `∅→{a}→{a,b}` maps to the reversed complementary path `∅→{b}→{a,b}`. The two triangles are `(∅,{a},E)` and `(∅,{b},E)`. This is a triangulated disk, **not a closed manifold**.

Exact output:

| n | f-vector, increasing dimension | Euler characteristic | top simplices |
|---|---|---:|---:|
| 2 | (4,5,2) | 1 | 2 |
| 3 | (8,19,18,6) | 1 | 6 |
| 4 | (16,65,110,84,24) | 1 | 24 |

**Scope:** this is a result in *history/configuration space*. No map from the simplices of `B_n` to the proposed physical/spatial R, B, G simplex-tree assembly has been constructed. The term "coherence simplex" here refers to the nerve, not an independently generated source-level 2-morphism or a physical green spatial simplex.

## 2. Minimal higher-closure obstruction

For three events `a,b,c`, retain the seven subset states of size ≤2 but **exclude `{a,b,c}`**. Every initial pair has its complete commutative diamond, so every pairwise two-branch completion exists. Nevertheless, there is no three-way state or 3-simplex. The order complex has `f=(7,12,6,0)`. Hence *pairwise diamonds at the source are insufficient to generate a three-way completion*.

Full-subset admissibility across **all contexts**, not merely at the initial state, is the extra condition used by the cube construction. The conjecture has not yet derived that condition.

## 3. Retained comparison is not forced by observable agreement

`ab` and `ba` are different histories although they reach the same subset state. A proof or operator interpreting their comparison is additional to that endpoint equality. There is, however, a computable **comparison residue** if the admitted structure contains invertible implementing operations:

`κ(a,b)=(ab)(ba)^{-1}=aba^{-1}b^{-1}`.

When observable actions commute as inner automorphisms `Ad_a` and `Ad_b`, their commutator is central in the implementing algebra. This gives an intrinsic candidate value for a green *residue*, but does not by itself supply a 2-cell identifying histories.

### Exact two-by-two test

Let

```
X = [[1,0],[0,-1]]
Y = [[0,1],[1,0]]
```

Then `X²=Y²=I`, `Ad_X Ad_Y=Ad_Y Ad_X`, `XY=-YX`, and `κ=-I`.

Thus the two *implemented* orders `XY` and `YX` are algebraic point-opposites about zero. This is a **linear operator-space** antipodality, not proof of geometric point-reflection for simplex trees.

An alternative (trivial central extension) realizes the *same commuting observable swap actions* with commuting lifts, `κ=+I`. Both retain their distinct event histories and satisfy ordinary multiplication associativity and reversal. Therefore observable independence, reversal and coherence do **not** select the central sign or force algebraic antipodality.

### Three-branch control

For `(Z/2)^3`, the explicit cocycles

`σ(g,h)=(-1)^{Σ_(i<j) c_ij g_j h_i}`, `c_ij∈{0,1}`

produce 8 different assignments to the three pairwise commutator signs, all associative, normalized, and with elementary generators squaring to `+1`. More generally this construction realizes `2^(n choose 2)` sign patterns for `n` independent branches. The computation exhaustively checks the displayed family for `n=2,3`; it does not classify every conceivable coherent lift.

This is consistent with, but does not supersede, the prior Marici finite two-swap cocycle classification in `research/nima/phase-selection-from-coherence.md`.

## 4. What has been established

- **Conditional theorem:** full independent-subset composition plus the poset nerve gives a canonical point-reflection-invariant triangulation of an `n`-cube. Proof: order maximal chains by coordinate order; coordinate complementation reverses chains.
- **Counterexample:** all initial pairwise diamonds do not imply triple closure.
- **Nonuniqueness:** the central comparison sign is `+1` or `-1` in two explicit coherent lifts with the same projected source action.
- **Positive exact example:** choosing the real `M₂(R)` Clifford inner implementation forces an algebraic `XY=-YX` pair and residue `-I`, but *choosing this representation is extra structure*.
- **Not established:** unique Green filler, source-admitted spatial realization, manifold closure, topological 3-sphere/Poincaré sphere, or Ramsey translation.

## 5. Next narrow theorem target

Determine whether **source-defined admissibility under arbitrary allowed continuation** (rather than global full-subset admissibility) forces comparators of two extension orders. If yes, determine whether the resulting comparator has a specified central phase and can be realized as a spatial simplex. In parallel, identify a source-level condition selecting nontrivial inner implementation over the trivial coherent extension. Do not import `M₂(R)` or a sign by fiat.

## Sources

- [Typed generator layer 2 — distinct retained histories and optional composition](https://github.com/andrey-kokoev/marici/blob/main/research/nima/typed-generator-layer-2.md)
- [Phase selection from coherence — nonunique cocycle classes](https://github.com/andrey-kokoev/marici/blob/main/research/nima/phase-selection-from-coherence.md)
- [Clifford retained-order recursion](https://github.com/andrey-kokoev/marici/blob/main/research/nima/clifford-retained-order-recursion.md)
- [Reversible local generation note](https://github.com/andrey-kokoev/marici/blob/main/research/chatgpt/marici_reversible_local_generation_note.md)
- [A rewriting coherence theorem with applications in homotopy type theory (2023)](https://www.cambridge.org/core/journals/mathematical-structures-in-computer-science/article/rewriting-coherence-theorem-with-applications-in-homotopy-type-theory/8AFEEEFAC1B7EEE61A187CFB0249AA1D)

## Reproduction

`python first_critical_pair.py` (standard library, exhaustive finite `n=2,3` central phase checks, Boolean order complexes for `n=2,3,4`, reflection, and the absent triple-state counterexample).
