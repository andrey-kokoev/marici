# Two-axis quarter-turn braiding, higher coherence, and the Ramsey interface

Date: 2026-11-08  
Status: exact finite results plus unproved Ramsey interface.  
Companion checker: `check_two_axis_braid_coherence.py` (standard-library Python, integer quaternion arithmetic and mod-2 cellular elimination).  
Related note: `four_phase_rotation_cone_ramsey_comparison_2026-11-08.md`.

## 1. The mathematical objects must remain distinct

We have four different levels of information:

1. A **spatial rotation** in `SO(3)`: the resulting orientation of a three-dimensional frame.
2. A **spinor lift** in `SU(2)`: the sign of a full turn is retained; `+q` and `-q` induce the same spatial rotation.
3. A **word history** in specified elementary quarter-turns: two different words can induce the same spinor rotation.
4. A **witnessed comparison of word histories**, and possibly a further comparison between comparisons: equality of endpoints does not construct such a witness.

Our six proposed `2+1+2+1` *roles* comprise two primitive axes, one derived axis, two comparisons involving the derived axis, and one joint-coherence target. They are not six independent linear or spatial dimensions. The quaternion construction takes place in a supplied three-dimensional Euclidean frame; it generates the third oriented axis from the first two **within that frame**. It does not derive three-dimensional space from two-dimensional space.

## 2. Two quarter-turns generate the third oriented axis

Work in the unit quaternions, with `i²=j²=k²=ijk=-1`. Define

\[
X=\frac{1+i}{\sqrt2},\qquad
Y=\frac{1+j}{\sqrt2},\qquad
Z=XYX^{-1}=\frac{1+k}{\sqrt2}.
\]

Each generator is a positive 90-degree spatial rotation. The three pairs obey exact braid relations:

\[
XYX=YXY=\frac{i+j}{\sqrt2},
\]
\[
XZX=ZXZ=\frac{i+k}{\sqrt2},\qquad
YZY=ZYZ=\frac{j+k}{\sqrt2}.
\]

These latter two braid relations hold for the already constructed quaternion operators. They do not supply two additional independent spatial generators; `Z` is conjugate to `Y` by `X`.

The braid composite `Δ=XYX=YXY` obeys

\[
\Delta^2=-1,\qquad \Delta^4=1.
\]

Consequently two applications of `Δ` restore the **spatial orientation** while retaining spinor sign `-1`; four restore the **spinor state**. This is an algebraically exact example of apparent closure preceding full lifted closure.

A fixed four-operation block is

\[
ZXYX=j,\qquad (ZXYX)^2=-1,\qquad (ZXYX)^4=1.
\]

Repeating this block eight times traverses two four-block spinor periods, but it is only one itinerary through the group. It does **not** enumerate every allowed rotation.

## 3. Exhaustive positive-word coverage of the generated group

Start from identity and append either `X` or `Y`, without making inverse rotations additional primitive moves. Treat words of length at most `n` as reachable histories. Exact integer-quaternion enumeration gives:

| Maximum word length `n` | Spinor states reached | Spatial rotations reached |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 3 | 3 |
| 2 | 7 | 7 |
| 3 | 14 | 14 |
| 4 | **23** | 21 |
| 5 | 33 | **24** |
| 6 | 43 | 24 |
| 7 | **48** | 24 |

Therefore `⟨X,Y⟩` is the 48-element binary octahedral group; its spatial projection has 24 rotations. All spatial rotations are reachable by at most five positive moves; all spinor states by at most seven. The equality `23=R(3,7)` is numerical evidence only: the enumeration has no constructed map to triangle-free, bounded-independence graphs.

**Important:** there is no new group element to generate by increasing the Ramsey parameter once these 48 spinor states are reached. Any continuing Ramsey-related growth would have to involve source configurations, retained histories, higher comparison cells, or some larger representation that has not been constructed.

## 4. The first missing relation is present at word length four

The positive braid rewrite is

\[
XYX\ \longleftrightarrow\ YXY.
\]

It preserves word length and acts only when one of those three-letter substrings appears. Yet

\[
X^4=Y^4=-1.
\]

The words `XXXX` and `YYYY` contain neither rewrite pattern. They therefore have identical spinor endpoints but lie in **different braid-rewrite components**.

At word length three, distinct braid components and distinct spinor endpoints both number seven. At length four, there are twelve braid components but only eleven distinct spinor endpoints; `XXXX` and `YYYY` are the unique extra identification at that length.

This gives a shortest explicit witness for the distinction:

\[
\boxed{\text{spinor endpoint equality}\not\Rightarrow
\text{equivalence by the admitted braid rewrite}.}
\]

A new endpoint relation could be attached as an additional comparison, or a quotient could impose it. Neither is justified merely by the matrix equality if the target is a *retained-history* system: the corresponding comparison witness must be declared or constructed.

## 5. Exact growth of positive braid classes

Let `a_n` count connected components of all `2^n` length-`n` words under the single rewrite `XYX↔YXY`. This is the fixed-length equivalence relation of the positive three-strand braid monoid. The finite counts agree with

\[
a_n=F_{n+3}-1,
\]

where `F_0=0`, `F_1=1` and `F_{m+2}=F_{m+1}+F_m`. Equivalently, for `n≥3`,

\[
a_n=2a_{n-1}-a_{n-3},\quad
(a_0,a_1,a_2)=(1,2,4).
\]

The checker enumerates the components rather than assuming the recurrence.

| Exact word length | Braid-rewrite components | Distinct spinor endpoints | Additional component identifications needed to recover endpoint classes |
|---:|---:|---:|---:|
| 3 | 7 | 7 | 0 |
| 4 | 12 | 11 | 1 |
| 5 | 20 | 16 | 4 |
| 6 | 33 | 21 | 12 |
| 7 | 54 | 23 | 31 |
| 8 | 88 | 24 | 64 |
| 9 | 143 | 24 | 119 |
| 10 | 232 | 24 | 208 |
| 11 | 376 | 24 | 352 |
| 12 | 609 | 24 | 585 |

The last column is `braid components − endpoint classes` at fixed length, not a number of independent relation generators. It shows that endpoint saturation and braid-history growth are genuinely different phenomena.

## 6. Higher cubes generated by *independent* braid rewrites

Take a word of length `n` and mark `p` **disjoint** substrings of length three, each admitting `XYX↔YXY`. Rewriting each marked substring independently produces a `p`-cube with `2^p` vertices.

The total number of formal `p`-cells, over *all length-`n` binary words*, is

\[
\boxed{c_p(n)=\binom{n-2p}{p}\,2^{n-3p},\qquad 3p\leq n.}
\]

Here `c_0(n)=2^n`, and a `p`-cell includes all `2^p` rewrite choices, counted once. This model **attaches canonical cubical comparison cells** wherever the rewrites use disjoint positions; it does not infer that independently chosen, externally decorated witness transports necessarily commute.

| Word length `n` | Vertices `c₀` | Rewrite edges `c₁` | Squares `c₂` | 3-cubes `c₃` | 4-cubes `c₄` |
|---:|---:|---:|---:|---:|---:|
| 3 | 8 | 1 | 0 | 0 | 0 |
| 4 | 16 | 4 | 0 | 0 | 0 |
| 5 | 32 | 12 | 0 | 0 | 0 |
| 6 | 64 | 32 | 1 | 0 | 0 |
| 7 | 128 | 80 | 6 | 0 | 0 |
| 8 | 256 | 192 | 24 | 0 | 0 |
| 9 | 512 | 448 | 80 | 1 | 0 |
| 10 | 1024 | 1024 | 240 | 8 | 0 |
| 11 | 2048 | 2304 | 672 | 40 | 0 |
| 12 | 4096 | 5120 | 1792 | 160 | 1 |

At `n=15` there would also be one formal 5-cube by the counting formula; its full homology was **not** checked in this audit.

## 7. Cellular homology calculation

The companion checker constructs the mod-2 cellular boundary maps explicitly. Through word length 12, every positive-degree Betti number of this specific filled cubical complex is zero.

The first new top-dimensional boundaries give an informative removal test:

| Word length | Top cell newly possible | What happens if the unique top cell is withheld? |
|---:|---|---|
| 6 | One square | One `H₁(−;F₂)` class remains |
| 9 | One 3-cube | One `H₂(−;F₂)` class remains |
| 12 | One 4-cube | One `H₃(−;F₂)` class remains |

These are **relative ablation tests**: they demonstrate what the canonical cell fills. They do not show that an actual Ramsey instance lacks that filler. Nor does mod-2 acyclicity establish homotopical contractibility or coherence of arbitrarily decorated witnesses.

A compatible next layer for overlapping or witness-decorated braid moves can require noncubical comparison cells. The current cubical complex only handles nonoverlapping rewrites.

## 8. Existing Marici precedent for a noncubical higher comparison

The repository already contains exact constructions addressing the missing comparison type:

- [Pairwise filling equivalences can fail the three-direction braid](https://github.com/andrey-kokoev/marici/blob/7afcae687310b5db324ebfab4fbfe26444c73758/research/voevodsky/pairwise-filling-equivalences-can-fail-the-three-direction-braid.md). Boundary-preserving individual swaps can fail their combined three-direction braid comparison when internal witness tags are retained.
- [Theta parity squares and the permutohedral three-cell](https://github.com/andrey-kokoev/marici/blob/7afcae687310b5db324ebfab4fbfe26444c73758/research/voevodsky/theta-parity-squares-and-the-permutohedral-three-cell.md). An actual four-event comparison complex has 24 route vertices, 36 edges, six square faces, eight braid-hexagon faces, and a common three-cell. Its cellular boundaries satisfy `d₁d₂=0`, `d₂d₃=0`.
- [Prior arithmetic constructors for the theta permutohedral three-cell](https://github.com/andrey-kokoev/marici/blob/7afcae687310b5db324ebfab4fbfe26444c73758/research/voevodsky/prior-arithmetic-constructors-for-the-theta-permutohedral-three-cell.md). Ordered prime operations retain an explicit common refinement; quotient-before-transport can lose the necessary comparison information.
- [A source cycle selector makes the two-polarity four-chart seam faithful](https://github.com/andrey-kokoev/marici/blob/7afcae687310b5db324ebfab4fbfe26444c73758/research/nima/a-source-cycle-selector-makes-the-two-polarity-four-chart-seam-faithful.md). Four displayed Fourier phases can close while the source-defined successor advances the retained record.

These documents are independently constructed source examples. They are precedents for *comparison mechanisms*, not proofs of an identification with Ramsey colorings.

## 9. Moving frontier at k→k+1: precise hypothesis

The proposed sequence `[4] → [4,5] → [5,6]` could describe an active two-generator window. A legitimate recurrence must retain the **completed comparison evidence** between `4` and `5` even after `4` leaves the active frontier. Deleting `4` from a formal braid presentation by setting its generator to the identity collapses the adjacent relation and can force the `5` generator itself to become trivial; naïve deletion is not coherence-preserving.

The research hypothesis to test is:

> Extending a Ramsey-admissible colored configuration from parameter `k` to `k+1` induces an extension of its witnessed comparison complex; the new frontier may present a closed comparison boundary before an admissible filler is available, while previously completed comparisons remain recoverable.

This is a hypothesis, not yet a theorem. In particular there is no derived identification `n=k`, `n=3k`, or `n=k−c` between **word length** and **Ramsey parameter**, and no established map from an `R/G/0` row to a Ramsey graph or its color constraints.

## 10. Strongest next test

The next calculation should use the original incidence-bearing Ramsey source, not just the quaternion endpoint group:

1. Define exactly what a colored source configuration represents (graph edges, forbidden monochromatic triangles, independent sets, retained complement data).
2. Define the two primitive successor operations on that source and show that they preserve its admissibility conditions.
3. Derive the third axis and pairwise comparisons on the resulting retained history objects. Distinguish imposed comparison relations from source-generated witnesses.
4. Form the comparison complex of all admissible histories and calculate its relative homology or higher-coherence obstruction under `k→k+1`, without discarding inherited witnesses.
5. Only then compare the resulting threshold or obstruction sequence with the Ramsey values.

**Current result:** the quaternion/positive-braid system gives exact finite symmetry saturation, unbounded braid-history classes, a shortest endpoint-versus-history discrepancy, and a reproducible hierarchy of cubical fillers. **Not established:** that these structures cause, bound, or compute `R(3,k)`.

## 11. Reproduce this audit

Run:

```bash
python check_two_axis_braid_coherence.py
```

The script requires only Python's standard library and checks:

- exact quaternion multiplication in integer numerators divided by powers of `√2`;
- generation of the derived third quarter-turn and all three pairwise braid identities;
- `Δ²=-1`, `X⁴=Y⁴=-1`, and the selected four-turn block;
- full spatial and spinor reachable-state counts;
- all fixed-word-length braid-rewrite components through length 12;
- their distinct spinor endpoints, including the unique length-four collision;
- all disjoint-rewrite cellular counts, mod-2 boundary ranks, and positive-degree Betti numbers through length 12.

No repository commit or alteration to Marici is made by this note.
