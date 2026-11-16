# Native continuation algebra and the nonsplitting obstruction to green coherence

**Research note — 2026-11-09**  
**Program:** Reflected simplex trees, source-generated coherence, Ramsey obstruction.  
**Status:** Exact source audit and group-theoretic/topological deductions; reproducible finite checks. Not a new Marici constructor, proof-assistant verification, or a Ramsey theorem.

## 1. The question resolved and the question not resolved

The Stage 8 group model produced a continuation-invariant discrepancy precisely when a relative commutator lay in the centralizer of the admissible prefix group. But its admissible group and effect interpretation were supplied independently. Here we determine the **maximal directed continuation grammar of the frozen six-arrow Marici seed** without supplying an effect group:

```
A --AB--> B --BC--> C --CA--> A
A --AD--> D --DB--> B --BA--> A
```

An edge occurrence is distinct from its reverse presentation and from its hypothetical inverse. In particular, `AB` and `BA` are independent occurrences. The source supplies endpoint matches and path concatenation; it does **not** supply triangle 2-cells or path equalities. This is stated and verified in the existing Cubical Agda modules:

- [ActualSeedEndpointTable.agda](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/ActualSeedEndpointTable.agda)
- [SeedSeamPathComparisonBoundary.agda](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/SeedSeamPathComparisonBoundary.agda)
- [SeedFirstReturnActions.agda](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/SeedFirstReturnActions.agda)
- [SourceGraphFreeRealization](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/source-graph-free-realization-v1.md)
- [SeedNativePromotionBindingGate](https://github.com/andrey-kokoev/marici/blob/main/research/nima/seed-native-promotion-binding-gate.md)

**Scope:** “Source-admitted” below means all finite composable histories in this explicitly specified *free seed*. An implementation selecting a deterministic generator, additional response semantics, or richer native WG admissibility may admit a different subset; it must be declared and verified separately. This result does not claim to classify the complete repository's possible extensions.

## 2. Theorem: all directed returns are generated freely by four blocks

A **first return** at `A` is a nonempty directed path from `A` to `A` with no intermediate visit to `A`. There are exactly four:

```
r00 = AB BA           (length 2)
r01 = AB BC CA        (length 3)
r10 = AD DB BA        (length 3)
r11 = AD DB BC CA     (length 4)
```

**Proof.** From `A`, take either `AB` or `AD·DB`; both reach `B` without revisiting `A`. From `B`, take either `BA` or `BC·CA`; both return to `A`. There are no other branches before the return. Every directed path `A→A` is uniquely cut at the successive occurrences of `A`. Conversely, concatenating any sequence of the four first-return paths produces an admitted `A→A` history. Thus

\[
\operatorname{End}_{\mathcal C}(A)\cong\{r_{00},r_{01},r_{10},r_{11}\}^{*},
\]

where \(\mathcal C\) is the free directed-path category and the right side is a **free monoid** (not a free group).

The length-generating series is

\[
\sum_{n\ge0}a_n t^n=\frac{1}{1-t^2-2t^3-t^4}.
\]

The checker enumerates paths through length nine, verifies this first-return decomposition for every enumerated `A→A` path, and reproduces the full seed's path counts `4,6,10,16,26,42,68` for lengths zero to six. This numerical verification supplements the general decomposition proof, not replaces it.

**Important distinction:** The abstract group completion of the rank-four return monoid is not the free *graph* fundamental group below. Inverting all six individual **graph edges** introduces additional homotopic word reductions.

## 3. The free geometric realization and its continuation centralizer

In the free graph realization, choose the spanning tree `AB, AD, BC`. The three remaining oriented chords provide a free basis of

\[
\pi_1(X,A)\cong F(x,y,z),
\]

where

\[
\begin{aligned}
x&=AB\,BC\,CA=r_{01},\\
y&=AD\,DB\,(AB)^{-1},\\
z&=AB\,BA=r_{00}.
\end{aligned}
\]

The four first returns have images

\[
r_{00}=z,\quad r_{01}=x,\quad r_{10}=yz,\quad r_{11}=yx.
\]

Here the inverse of `AB` belongs to the *geometric fundamental groupoid*, not to the original directed occurrence alphabet. The directed return monoid maps into `F(x,y,z)`; its images group-generate the full free group.

**Continuation-centralizer theorem.** A fixed group-valued discrepancy \(d\in\pi_1(X,A)\) whose value is invariant under conjugation by **every admitted directed return** must be trivial:

\[
\bigcap_{r\in\operatorname{End}_{\mathcal C}(A)} C_{F_3}(r)=\{1\}.
\]

**Proof.** Both `x=r01` and `z=r00` are source-admitted returns and are independent free generators. In a nonabelian free group, the centralizer of a free generator is its infinite cyclic subgroup. Hence \(C(x)\cap C(z)=\langle x\rangle\cap\langle z\rangle=\{1\}\).

This theorem applies to a *single, context-independent label in the free graph fundamental group*. It does **not** rule out context-transported comparisons, non-group-valued witnesses, or nontrivial central elements in an independently supplied effect representation.

## 4. What changes when the red and blue triangles are admitted

**Additional assumption:** Attach 2-cells with the actual red and blue cyclic boundaries

\[
R=AB\,BC\,CA=x,\qquad B=AD\,DB\,BA=yz.
\]

The resulting group is

\[
\pi_1(X_{RB},A)=\langle x,y,z\mid x=1,\ yz=1\rangle
\cong\langle z\rangle\cong\mathbb Z.
\]

All source-admitted return images now lie in this cyclic group (`r00=z`, `r01=1`, `r10=1`, `r11=z^{-1}`). Every possible discrepancy in the group is central. In particular, `z` is continuation-invariant and nontrivial.

**Consequence:** A rule that accepts every continuation-invariant residue cannot fill `z`; it simply accepts it. A rule that rejects all nonzero residues would forbid the already well-defined R/B complex. Centrality is therefore not a source-derived selector for G.

For comparison, adding `G1=AB (DB)^{-1} (AD)^{-1}` sets `y=1` and thereby `z=1`. Adding the reflected `G2=BA (CA)^{-1} (BC)^{-1}` creates a 2-cycle rather than a further fundamental-group relation. The resulting homology is:

| Cells attached | \(\pi_1\) | \(H_1(\mathbb Z)\) | \(H_2(\mathbb Z)\) |
|---|---|---|---|
| none | \(F_3\) | \(\mathbb Z^3\) | 0 |
| R, B | \(\mathbb Z\) | \(\mathbb Z\) | 0 |
| R, B, G1 | trivial | 0 | 0 |
| R, B, G1, G2 | trivial | 0 | \(\mathbb Z\) |

Smith normal forms were computed for the integral cellular boundary maps. An explicit integral 2-cycle for the last row is

\[
Z=R-B-G_1+G_2,\qquad \rho(Z)=-Z.
\]

These are conclusions of the specified **conditional CW/Δ-complex** construction, not statements about filled faces already admitted by the free source.

## 5. The deeper obstruction: reflection of the quotient need not split at a basepoint

The free source graph has one nontrivial involutive automorphism

\[
\rho:\quad A\leftrightarrow B,\ C\leftrightarrow D,
\quad AB\leftrightarrow BA,\ BC\leftrightarrow AD,\ CA\leftrightarrow DB.
\]

This is a genuine order-two automorphism of the unbased graph. However, `A` is exchanged with `B`. To turn it into a map of loops based at `A`, choose a connecting path `s=AB` from `A` to `B`. Its reflected path is \(\rho(s)=BA\), **not** the formal inverse of `AB`. The resulting transported automorphism \(\Phi\) of `F(x,y,z)` satisfies

\[
\Phi(x)=zy,\qquad \Phi(y)=xz^{-1},\qquad\Phi(z)=z,
\]

and hence

\[
\boxed{\Phi^2(w)=zwz^{-1}.}
\]

The nontrivial square is the return `z=s·ρ(s)`; it is not an arbitrary sign fitted to an effect model.

The quotient by the free involution has two vertices and three edge orbits. Give them names

```
a = AB / BA        (loop on the A/B vertex orbit)
b = BC / AD        (edge from A/B to C/D)
c = CA / DB        (edge from C/D to A/B)
```

The two R/B faces descend to one face with boundary `a b c=1`. Choosing `b` as a spanning-tree edge gives

\[
\pi_1(X_{RB}/\rho)\cong\langle a\rangle\cong\mathbb Z,
\]

while the double cover corresponds to the index-two subgroup \(2\mathbb Z\). The resulting exact sequence is

\[
1\longrightarrow 2\mathbb Z\longrightarrow\mathbb Z
\longrightarrow C_2\longrightarrow1.
\]

**It does not split:** no element of \(\mathbb Z\) mapping to the nonidentity class in \(C_2\) has order two. This is a statement about *based fundamental-group lifts of the reflection*, not a denial that the covering space has an order-two deck transformation.

The green face descends to `a c^{-1} b^{-1}=1`. Since `bc=a^{-1}` from R/B, its boundary reduces to `a²`. Adding the green orbit therefore gives

\[
\pi_1(X_{RBG}/\rho)\cong\langle a\mid a^2=1\rangle=C_2;
\qquad \pi_1(X_{RBG})=1.
\]

At the level of this quotient group presentation, green closure is **equivalent to imposing the missing order-two based monodromy relation**. This equivalence explains the geometry of G, but still does not justify imposing the relation from the source alone.

In the free *graph* before R/B, the covering extension likewise does not split: \(1\to F_3\to F_2\to C_2\to1\), since \(F_2\) has no torsion. Attaching R/B simplifies the obstruction without eliminating it.

## 6. Universal countermodels: green closure is not a theorem of the audited rules

The source's own retained-history action already distinguishes the parallel paths `AB` and `AD·DB`: take the representable covariant functor \(v\mapsto \operatorname{Hom}_{\mathcal C}(A,v)\), with each edge acting by right concatenation. Applied to the empty history, the two effects produce different words. This is the checked `SeedFirstReturnActions` construction. Hence no equality of the two effects can hold *naturally for every interpretation* of the free source.

Even if one independently strengthens the source by supplying both R/B face relations **and** reflection-equivariant reversible effects, strict G is still not selected. Take additive effects in \(\mathbb Z\), with

\[
AB=BA=a,\quad AD=BC=0,\quad DB=CA=-a.
\]

Both red and blue boundaries evaluate to zero for every integer `a`, whereas

\[
G_1=G_2=2a.
\]

`a=0` supplies a model with strict green closure; `a=1` supplies a model with a nontrivial green defect. Both obey all declared R/B and reflection constraints. The checker verifies the formula for every integer `a` between `-9` and `9`; the algebraic calculation proves it for all `a`.

**No-go theorem (specified language).** Graph incidence, free path composition, unbased point reflection, reversal of paths in the geometric realization, the R/B face relations, and invariance of a fixed group-valued defect under all admitted return continuations do **not** logically entail the G relation. The additive `a=1` model is a counterexample, while the identical constraints permit `a=0`.

This does not rule out a richer source operator, a dynamically admitted subcategory, a higher comparison with a nonzero label, or a physically chosen interpretation. It identifies the additional information such a rule must carry.

## 7. Research decision: what additional principle would actually add information?

Within this six-arrow source, the obstruction is now classified rather than merely named:

1. **Directed histories:** the free monoid on four first-return blocks.
2. **Geometric reversible continuations:** a rank-three free fundamental group; the full-return centralizer is trivial.
3. **After R/B admission:** an infinite cyclic return class; continuation centrality no longer constrains it.
4. **Reflection quotient:** a non-split `C2` fundamental-group extension, whose nonsplitting is measured by the squared endpoint-switching loop.
5. **G attachment:** a new order-two relation in the quotient, followed by a reflected face producing the sphere class.

The most useful next candidate must be **a separate rule that is independently justified**, not merely `z=1` under another name. It should specify what local source observation licenses attaching a 2-cell to a selected return, be stable under admitted continuations and reflection, and predict a different answer on an asymmetric or branching source without being refitted.

If no such rule exists in the source, the correct result is the no-go: free composition alone does not select a green filler. We should not use additional geometric regularity, order-two based monodromy, or a Clifford effect representation as if any had been derived.

The Ramsey translation is still open. The exact `R(3,7)=23` threshold cannot be inferred from any of these group presentations without a uniform, predictive map from Ramsey colorings to the source's admitted compositions.

## 8. Verification and provenance

`check_native_continuation_algebra.py` (Python 3 + SymPy) independently checks:

- all graph automorphisms (exactly 2), the reflected edge action, and path counts;
- all 72 `A→A` histories through length nine and their unique first-return decompositions;
- first-return images in `F(x,y,z)` and the formulas for the transported reflection on every enumerated return;
- the integral cellular boundary relation `∂₁∂₂=0`, Smith normal forms, and the antisymmetric 2-cycle;
- the quotient boundary matrix Smith form `(1,2)` after adding G, which gives `H1=Z/2`;
- the integer-effect countermodels for R/B closure with and without G.

The universal statements about free monoids, free-group centralizers, and covering extensions are justified mathematically in the preceding sections; finite checks alone do not establish those theorems. No new Cubical Agda module was compiled; none of the Marici repository files was edited.

Files: `native_continuation_results.json`, `test_output.log`.
