# Codimension-One Pairing as a Candidate Witness Generator

**Date:** 2026-10-27  
**Status:** Finite exact tests passed; conditional mathematical conclusions. No new Cubical Agda proof or native Marici construction claimed.

## Research question

Can the primitive be: *adjoin one codimension-one face at a time, preserving shared-boundary equality and reversible comparison*, such that higher coherent cells are derived rather than separately supplied? This tests whether a separate return witness `a′`, predetermined 4-simplex, or equal algebraic squares are necessary.

## 1. The exact local universal property

For two codimension-one faces with record spaces `F(A)` and `F(B)` and a shared codimension-two face `C`, with restriction maps `r_A : F(A) → F(C)` and `r_B : F(B) → F(C)`, define

\[
\operatorname{Match}(A,B)=\sum_{x:F(A)}\sum_{y:F(B)}\bigl(r_A(x)=r_B(y)\bigr).
\]

This *homotopy pullback* is a universal compatible-pair object. It has a canonical reversal by exchanging `(x,y)` and reversing the comparison path. **This does not mean the original generating arrows are invertible.**

For a simplicial candidate, the corresponding double-restriction equations are

\[
d_i d_j=d_{j-1}d_i\quad (i<j).
\]

These are commuting **face squares**, not the numerical equation `a²=b²`. Pair compatibility does not itself supply a higher cell `z` that restricts to the chosen pair.

The missing operation is a section of the restriction map

\[
\operatorname{res}_{i,j}: X_n\to X_{n-1}\times_{X_{n-2}}X_{n-1}.
\]

It may fail to exist, may not be unique, or may exist uniquely, depending on the source structure. A coherent filler selection must also respect authorized continuations and changes of presentation.

## 2. Exact finite models

### A. Reversible group: the nerve of `S₃`

An `n`-simplex is a word of `n` group elements; face maps drop a first/last arrow or compose two adjacent arrows. All `6^n` words were enumerated for `n=2,3,4,5`.

| Dimension | Simplices | Outcome for **every** pair of codimension-one faces |
|---:|---:|---|
| 2 | 36 | Every matching pair has exactly one filler |
| 3 | 216 | Every matching pair has exactly one filler |
| 4 | 1,296 | Every matching pair has exactly one filler |
| 5 | 7,776 | Pair restriction is injective; surjectivity not exhaustively enumerated |

For dimensions 2–4, both injectivity and surjectivity against **all** matching pairs were checked. In degree 5 only injectivity was enumerated; the unrestricted groupoid theorem supplies the general mathematics independently.

The category nerve of a groupoid has unique horn fillers in dimensions ≥2 and is a Kan complex. This yields a **positive, conditional** reconstruction rule. Its higher simplices encode composite arrows rather than independent higher witness degrees. Its homotopy type is a 1-type (`K(G,1)` for a one-object group).

### B. Noninvertible monoid: `{1,z}`, with `z²=z`

This is the nerve of the one-object category with an absorbing endomorphism `z`.

At degree 2, the pair of faces `(z,z)` has two fillers `(z,z)` and `(1,z)`; another matching pair `(z,1)` has no filler. These are two-sided boundary data, not forced composites.

For every degree 2–5, exact enumeration found both matching pairs without fillers and pairs with multiple fillers. **The universal matching object exists, but the filler restriction map is not an equivalence.**

### C. Reversible higher comparisons: `K(Z/2,2)`

Represent an `n`-simplex by `Z/2` labels on all its triangles, satisfying the tetrahedral cocycle condition

\[
\omega_{123}+\omega_{023}+\omega_{013}+\omega_{012}=0\pmod2
\]

on every tetrahedron (orientation signs coincide modulo two). The 2-cell labels form a group: each is reversible under addition. Every ordinary vertex/edge boundary matches.

| Dimension | Full coherent simplices | Compatible pairs of chosen codimension-one faces | Fillers per pair |
|---:|---:|---:|---:|
| 3 | 8 | 4 | 2 |
| 4 | 64 | 32 | 2 |

The counts hold for **each** choice of two faces. Every pair is extendible, but **not uniquely**. In each two-element fiber, adding a nonzero relative cocycle exchanges the two fillers while keeping both input faces exactly fixed. If this relative-cocycle symmetry is an admissible change of reference, no selection of a unique filler can be invariant under it.

A separate full-boundary obstruction occurs already in dimension 3: among 16 assignments of the four triangle labels to the boundary of a tetrahedron, eight have even sum and fill, while eight have odd sum and do **not** fill. For example `(1,0,0,0)` is obstructed. This is not a violation of the Kan *horn* property: prescribing **all** faces is stronger than prescribing a horn.

**Interpretation:** reversible higher witnesses plus commuting face squares do not make all complete boundaries fillable, nor select a unique extension from a pair.

## 3. Binding to actual Marici source

Existing source declarations:

- `research/nima/agda/ActualSeedEndpointTable.agda`: `AB, BC, CA, AD, DB, BA`.
- `research/nima/agda/SeedSeamPathComparisonBoundary.agda`: a free endpoint-typed path category, with no independent path equalities.
- `research/nima/agda/SeedFirstReturnActions.agda`: associative `append` for retained paths; source-defined parallel return words remain distinct.
- `research/nima/agda/FourSimplexHorn.agda`: one missing tetrahedron **together with** a top filler from a **four-face horn**, not from an arbitrary pair of tetrahedra.
- `research/strominger/source-incidence-selects-the-coherence-nerve.md`: source incidence determines whether a comparison is simplicial, cubical, or globular.

Exact re-enumeration of the six-arrow source yields counts of free paths of lengths 0–6:

`4, 6, 10, 16, 26, 42, 68`.

The source has both `AB : A→B` and `BA : B→A`, but `AB;BA` is a nonempty retained word, **not** the identity path at `A`. An opposite arrow is not necessarily an inverse. Ordinary nerve composition therefore provides canonical simplicial comparison bookkeeping, but no independent higher filler equating arbitrary parallel paths.

## 4. Precise conclusion

The candidate rule splits into three propositions:

1. **Pair matching:** derived from dependent sums and equality, with canonical reversible exchange of the two face presentations. **Yes**, in the declared type theory.
2. **Existence of a higher completion from every matching pair:** **No**, for general sources. The monoid test gives explicit failures. It holds in the strict groupoid nerve.
3. **Unique, universally coherent selection of the new witness:** **No** in general, even when every higher comparison is reversible; the `K(Z/2,2)` model gives two symmetrically related completions.

This does **not** disprove the existence of a richer one-witness-at-a-time generator. It isolates what such a generator must actually do: derive an **admissible filler or filler comparison**, not only the shared-face match. If uniqueness is not required, the generator may choose one witness, but its source authority and coherence under every admitted continuation must still be demonstrated.

A strict groupoid nerve generates coherent higher simplices with no new independent higher homotopy. To generate genuinely nontrivial higher witnesses, the source must specify or derive nontrivial higher filler data and their transport.

## 5. First useful Agda obligation

Instead of adding a new 4-simplex constructor, test the following source-typed interface at the first nontrivial degree:

```text
FacePair    : Type
Fill        : FacePair → Type
restricted  : (c : FullCell) → FacePair

exists      : (p : FacePair) → Fill p         -- or a precise obstruction
reversible : swapFace (swapFace p) ≡ p
naturality : witness/filler transport under every admitted continuation
retention   : recover both original face records and their full histories
```

1. First prove the exact pair-matching and reversal laws in the *existing* Marici source, without identifying an opposite-occurrence path with an inverse.
2. Try to derive a genuinely new comparison/filler from the native source rules. If impossible, give a typed negative model or a missing-premise theorem.
3. Check that full source history is retained and that all higher pastings work. The earlier four-face horn theorem must **not** be repackaged as a proof of two-face generation.
4. Do not demand filler uniqueness as an axiom. Classify the filler fiber and test whether source-authorized continuations can distinguish its elements.

## Verification and references

Exact Python executor: `marici_codim_one_pair_test.py`; machine result: `marici_codim_one_pair_results.json`. Both are in the same output folder as this note. All assertions passed. No Cubical Agda compilation, repository mutation, or new physical claim was made.

External background: [nerve characterization](https://ncatlab.org/nlab/show/nerve); [groupoid nerves and Kan horns](https://pure.mpg.de/rest/items/item_3698146_1/component/file_3698147/content).
