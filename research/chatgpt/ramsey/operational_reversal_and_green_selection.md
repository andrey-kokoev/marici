# Operational reversal, green generation, and the nonsplit reflection obstruction

**Research note — 2026-11-09**  
**Scope:** The actual Marici six-occurrence source, categorical effect interpretations, the conditional reflected R/B face construction, and finite exact control models.  
**Status:** Category-theoretic arguments and group-extension classification are mathematical deductions under explicitly declared assumptions. Exact finite computations pass. No source-derived inverse, no native green 2-cell, and no new Cubical Agda proof are claimed.

## 1. The actual source and what it does not assert

The source has vertices A,B,C,D and six *directed occurrences* `AB`, `BC`, `CA`, `AD`, `DB`, `BA` in [`ActualSeedEndpointTable.agda`](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/ActualSeedEndpointTable.agda). Its reflection swaps A↔B, C↔D and pairs AB↔BA, BC↔AD, CA↔DB. Table transposition reverses the *presentation* of AB while retaining its occurrence label; it is not an equation AB^-1=BA.

The paths `p=AB` and `q=AD·DB` are distinct retained words A→B; `s=BA` and `t=BC·CA` are distinct retained words B→A. [`SeedSeamPathComparisonBoundary.agda`](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/SeedSeamPathComparisonBoundary.agda) formally separates these paths. [`SeedFirstReturnActions.agda`](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/SeedFirstReturnActions.agda) has effect comparisons *conditional on* supplied pointwise witnesses, and preserves the distinct history channel.

An inverse in the *free groupoid completion* is the formal path `(AB)^-1`; it is not automatically the separately declared `BA`. Any identification between them is new operational information.

## 2. A minimal green-generation theorem

Let C be any category of interpreted effects. Take arrows

- p,q:A→B, representing the direct and indirect forward histories;
- s,t:B→A, representing the direct and indirect return histories.

Assume the red and blue face compositions close:

\[t\circ p=1_A,\qquad s\circ q=1_A.\]

**Proposition.** If s is a two-sided inverse of p, i.e.

\[s\circ p=1_A,\qquad p\circ s=1_B,\]

then `p=q` and `s=t` in C.

**Proof.** Since `p∘s=1_B` and `s∘q=1_A`,

\[q=(p\circ s)\circ q=p\circ(s\circ q)=p.\]

Since `t∘p=1_A` and `p∘s=1_B`,

\[t=t\circ(p\circ s)=(t\circ p)\circ s=s.\]

This is a *generation of green effect equalities*, not an identification of native histories and not a unique choice of a higher 2-cell. In a groupoid-valued interpretation it also applies with the ordinary groupoid inverse.

**One-sided negative control.** Set A=R, B=R², `p(x)=(x,0)`, `q(x)=(x,x)`, `s(x,y)=x`, `t(x,y)=x+y`. Then `t∘p=s∘q=s∘p=1_A` but `p≠q` and `s≠t`. Thus the one-sided return `s∘p=1_A` is insufficient without the other inverse law or another cancellation hypothesis. This control is not asserted to be reflection-equivariant.

## 3. Why the natural dagger alternative is not sufficient

A dagger is a contravariant involution on morphisms. It does not mean `f†=f^-1`. Unitary morphisms do satisfy that stronger condition. See [definition of dagger and unitary](https://pmc.ncbi.nlm.nih.gov/articles/PMC8892366/).

**Exact adversarial model:** interpret all four vertex effects in the one-dimensional real Hilbert space. Give the reflection-paired arrows `AB=BA=2`, `AD=BC=1`, `DB=CA=1/2`, acting by scalar multiplication. Each arrow is invertible; its reflected partner equals its adjoint. Both original triangles close (`2·1·1/2=1` and `1·1/2·2=1`), yet the return `AB·BA` is multiplication by 4, and the green comparison `AB=AD·DB` fails (`2≠1/2`).

A *source-independent* norm/metric requirement that proves the AB operation is unitary and that BA is its adjoint would suffice for the above categorical theorem. Neither that metric nor those identities are contained in the six-arrow table; imposing them merely because green closure is wanted would be circular.

## 4. Reflection-equivariant group effects: complete local classification

Let H be a group with involutive automorphism θ. Assign `AB=a`, `BA=θ(a)`, `AD=b`, `BC=θ(b)`, `DB=c`, `CA=θ(c)`. The red and blue loops close precisely when

\[bc=\theta(a)^{-1}.\]

One can freely choose a,b and then set c=b^-1 θ(a)^-1. The forward and reflected green discrepancies are respectively

\[g_1=a\theta(a),\qquad g_2=\theta(a)a.\]

Thus they vanish together, exactly if `θ(a)=a^-1`. The choice of b does not affect this condition. It is the nonabelian C2-cocycle condition for a. **This calculation classifies these interpretations; it does not construct θ from source incidence.**

Exact enumerations:

| Model | R/B-closed assignments | Both G close | Central nontrivial G | Noncentral G |
|---|---:|---:|---:|---:|
| Q8, θ=id | 64 | 16 | 48 | 0 |
| Q8, θ=conjugation by k | 64 | 48 | 16 | 0 |
| S3, θ=conjugation by a transposition | 36 | 24 | 0 | 12 |

In Q8, a=i and b=j give green closure under θ=conjugation by k, but give residue -1 under θ=id; the latter vanishes only after projection Q8→Q8/{±1}. In S3, a transposition not fixed by conjugation produces a noncentral 3-cycle discrepancy. These are explicit strict, projective, and context-dependent models satisfying the same face-closure pattern.

## 5. A stronger result: deriving the reflection action from an extension

Suppose **independently** that the relevant observable return system fits into a group extension

\[1\longrightarrow A\longrightarrow E\longrightarrow C_2\longrightarrow 1,\]

where A is abelian. Let u∈E be a lift of the nontrivial reflection class. Conjugation by u induces an involutive action θ on A, independent of changing u within its coset. In this setting θ **is derived from the extension**, not arbitrarily selected. Put c=u²∈A. Then θ(c)=c, and for any a∈A replacing u by a·u changes the square by

\[(au)^2=a\theta(a)c.\]

Therefore the class of c in

\[A^{\theta}/N_\theta(A),\qquad N_\theta(a)=a\theta(a),\]

is independent of the chosen lift. This is the cyclic-group cohomology class `H²(C2,A)` for the prescribed action. The extension splits (equivalently, there is a lift of order two) **if and only if that class vanishes**. This standard classification is discussed in [Conrad, *Extensions and H²(G,A)*](https://math.stanford.edu/~conrad/210BPage/handouts/Cohomology%26Extensions.pdf) and [cyclic-group cohomology](https://mathoverflow.net/questions/236954/group-cohomology-of-the-cyclic-group).

**Application to the conditional Marici R/B quotient.** The reflected two-face complex X_RB has an unbranched double-cover quotient Y=X_RB/ρ with

\[1\to 2\mathbb Z\to \mathbb Z\xrightarrow{\bmod 2} C_2\to1.\]

The derived θ on 2Z is trivial. A reflection lift is an odd integer u=2k+1, whose doubled value is 4k+2. Thus

\[H^2(C_2,2\mathbb Z)=2\mathbb Z/4\mathbb Z\cong C_2,\qquad[c]=[2]\ne0.\]

**No choice of reflection lift, basepoint transport, or equivalent presentation within this extension produces an involutive return.** Green closure requires *changing the presented 2-dimensional relations* (or changing the carrier), not choosing a better representative of the same source symmetry. This is an obstruction theorem under the R/B face assumption, not a source-native filler.

The complementary finite controls are C4→C2 (nonsplit), C2×C2→C2 (split), and the restriction of Q8→Q8/{±1} to the order-two subgroup represented by i (nonsplit).

## 6. Higher branching is still unresolved

Even if every primitive effect is unitary and hence has an operational inverse, **independent branch swaps need not commute**. Exact real matrices

\[X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\]

are both involutive orthogonal operators but satisfy XZ=-ZX. Their two orders differ by the central phase -I. Therefore a reversal law can generate the initial triangular green comparisons without generating arbitrary adjacent interchanges or their higher coherence.

The already completed Marici phase-selection work [*Does retained coherence select the central phase?*](https://github.com/andrey-kokoev/marici/blob/main/research/nima/phase-selection-from-coherence.md) independently establishes that two coherent central-phase lifts can survive the same source action unless an additional inner-implementation condition is adopted. The present note does not claim to supersede it.

## 7. Exact open obligation

The next valid input is not a generic 'G-filler'. It is an explicit, source-authorized **reversal contract** for a typed primitive occurrence:

1. An effect action (or a specified effect category), with evidence for why that interpretation is admitted.
2. An operation reversing AB whose relation to the independent occurrence BA is stated and justified.
3. A criterion distinguishing dagger/adjoint reversal, a two-sided inverse, and inversion only after a specified quotient.
4. A continuation law retaining histories and transporting any residual comparison; no automatic erasure of projective phases.
5. A branch-order comparison law separate from operational inversion.

**Selection experiment:** Given the native source and a proposed operational contract, show without reference to G that it accepts the unitary interpretation and rejects or records the scalar-2 countermodel, classifies the quaternion -1 residue, and remains valid on two noncommuting unitary branches. This is the weakest route found so far to genuine predictive green generation.

## Verification

Run `python operational_reversal_audit.py` in this directory. It writes `operational_reversal_results.json` and checks the exact source reflection permutation, all 164 finite group assignments, the scalar dagger counterexample, the one-sided section counterexample, noncommuting unitary matrices, and the finite extension-class controls. The categorical proofs and infinite-extension statement are provided mathematically above; they were not typechecked in Agda in this session. No repository files were modified.
