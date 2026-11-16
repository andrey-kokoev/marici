# Closed path codes and witness syndromes: first exact tests

**Date:** 2026-11-09  
**Status:** Exhaustive finite calculation for lengths 3 and 4; conditional proposal for higher coherence. No Ramsey threshold derived.

## 1. Frozen source and the error model

Let `r,s` be two distinct path letters. For `k=3,4` retain every length-`k` word containing exactly two `r`s:

\[
C_k=\{w\in\{r,s\}^k:\#_r(w)=2\}.
\]

The source of a word is its first letter; its target is its last. A **complete circle** is a cyclic ordering of all members of `C_k`, each once, such that the target of each word equals the source of the next. Individual word and gluing histories are never identified.

There are two distinct error models:

1. A **letter substitution** flips exactly one `r`/`s` occurrence inside one word.
2. A **single splice error** exchanges the continuation assignments of two existing words with the same target letter. The result still pairs matching endpoints and retains every word once, but splits one complete circle into two. A repair is another such exchange that restores a single circle. The corrupted state includes its complete (possibly two-cycle) successor map.

The model assumes that word boundaries are available; inserting or deleting letters, or losing word alignment, is a different synchronization-error problem.

## 2. Exact finite results

| Quantity | `k=3` | `k=4` |
|---|---:|---:|
| Path words | 3 | 6 |
| Endpoint-compatible one-circle orders, modulo rotation | 1 | 8 |
| Distinct single-splice corrupted states | 1 | 16 |
| Repairs per corrupted state | 1 | 2 or 4 |
| Isolated-word one-letter error uniquely recoverable? | No | No |
| One-letter error in a complete inventory uniquely recoverable? | Yes | Yes |

The last result assumes a known **complete inventory**, meaning that all members of `C_k` are included once and other words are intact. Changing one letter changes the word's weight, so the received word is not in `C_k`. Exactly one inventory word is missing and can be restored at its original position. Exhaustive checks cover all 9 (`k=3`) and all 192 (`k=4`) tour/word/letter choices. This is global redundancy; it is not a decoder of an isolated word.

For isolated words, every corrupted length-four word has three possible source words. For length three, three corrupted strings have two possible source words and the remaining one has three.

## 3. Three independent gluing choices at length four

The six words have the following typed roles:

| Word | Source → target | Role |
|---|---|---|
| `rrss` | `r→s` | first crossing, chosen as cyclic anchor |
| `rsrs` | `r→s` | second crossing |
| `srsr`, `ssrr` | `s→r` | two returns |
| `rssr` | `r→r` | closed `r`-loop |
| `srrs` | `s→s` | closed `s`-loop |

After anchoring the circle at `rrss`, every legal complete circle is determined by three independent binary decisions:

- `a`: which `s→r` return appears first;
- `b`: whether the `s→s` loop appears at the first or second `s` visit;
- `c`: whether the `r→r` loop appears after the first or second return to `r`.

Therefore the eight complete-circle **histories** are canonically parametrized relative to these role choices by `{0,1}³`. They are eight distinct histories, not eight endpoints of a cyclic action.

Flipping any one of the three decisions produces another legal complete circle using the same six words. These give three distinct involutive **gluing transformations**. They commute on the three-bit outcomes, but their retained construction histories remain different.

The resulting incidence pattern is a 3-cube:

- 8 circle histories (vertices);
- 12 elementary gluing changes (candidate N comparisons);
- 6 square comparison boundaries (candidate NN obligations);
- 1 three-dimensional boundary comparing square-composition histories.

The cells above are **comparison requirements** unless a source-admitted witness constructor is supplied. In particular, the three gluing transformations are not automatically the original `r,s,rs` group operations.

## 4. An optimal two-bit single-splice syndrome

Define a *retained* checksum of the gluing choices by

\[
\sigma(a,b,c)=(a,b\oplus c)\in\mathbb F_2^2.
\]

Exact enumeration shows that for **every** one-splice corrupted state, all compatible one-circle repairs have different values of `σ`.

The 16 corrupted states split into:

- eight states with two possible repairs;
- eight states with four possible repairs.

A state with four repairs requires at least four distinct checksum values for unambiguous recovery. Hence at least two checksum bits are necessary, and `σ` attains the minimum.

The confusability graph on the eight full circles has 24 edges: it is `K₈` minus a matching of four non-confusable history pairs. Each non-confusable pair differs by simultaneously flipping `b` and `c`, so `σ` gives its exact optimal four-coloring. The four two-history color classes are **forced, up to relabeling**, because each history has precisely one other history with which it does not share a one-splice corrupted state. Thus the optimal syndrome *partition* is derived from the gluing confusability relation. Its interpretation as `F₂²` still uses a choice of labels. The kernel `{(0,0,0),(0,1,1)}` is a non-confusability subgroup, not an identification of the two histories.

**Contract:** The original construction computes and retains `σ` independently of the successor assignments that may become corrupted. Given a corrupted two-cycle successor map plus this intact `σ`, a decoder determines exactly one original complete-circle history.

The checksum is a deterministic function of the full construction history, not a new random parameter. Nevertheless, requiring it to be available intact after corruption is additional data preservation. Existing path composition and endpoint closure alone do not provide it.

## 5. Local two-bit codeword checks

For `k=3,4`, assign positions distinct vectors from `F₂²`: `00,01,10` and, when `k=4`, `11`.

For a word whose `r` positions are `i,j`, add the two check bits

\[
\tau(w)=v_i\oplus v_j.
\]

The systematic binary code `(w, τ(w))` has minimum Hamming distance at least three in both cases and therefore uniquely corrects one corrupted bit (including a flipped check bit).

For `k=4` the three nonzero tag values are exactly the three complementary path pairs:

| Pair displacement in `F₂²` | Codeword pair (exchange `r` and `s`) |
|---|---|
| `01` | `rrss`, `ssrr` |
| `10` | `rsrs`, `srsr` |
| `11` | `rssr`, `srrs` |

The four codeword **positions** form the affine plane `F₂²`. Each nonzero displacement pairs the four positions in two disjoint edges. These are the three matchings of `K₄`, and the three displacement operations satisfy the Klein-four multiplication law: for distinct nonzero `u,v`, the third direction is `u+v`. This is a genuine `r,s,rs`-shaped three-direction algebra at the *position/tag layer*. It is not the earlier cyclic position group `C₈` with inversion `s=r⁴`, nor does it automatically produce a physical or native coherence witness.

The two extra bits are **minimal among systematic binary extensions**: with one added bit, the three pairwise distance-two words of `C₃` cannot all obtain different tags; nor can the three `C₄` words sharing one fixed `r` position. The length-four dictionary has six words, requiring length at least six even without the systematic condition, by the sphere-packing bound.

This is one-error **correction**, not a perfect binary Hamming code. With respectively 3 and 6 codewords, the radius-one Hamming balls cannot partition a binary cube of any length: both codebook cardinalities have an odd factor of 3.

## 6. Consequences and precise open problem

A shift from `k=3` to `k=4` creates a new form of **global gluing ambiguity**, even though every individual path remains endpoint-typed and the complete word inventory is fixed. The ambiguity has a three-bit set of distinct complete-circle histories, while two appropriately chosen retained bits suffice to correct one splice error.

The potentially relevant coherence construction is:

\[
\text{complete circle} \to
\text{three gluing choices} \to
\text{commuting-square obligations} \to
\text{retained two-bit syndrome}.
\]

The unresolved question is whether the **native** `r,s` composition system generates and preserves these syndrome bits as admitted N/NN witnesses, rather than merely allowing us to calculate them after constructing the whole circle.

Neither the existence of eight complete circles nor the two-bit syndrome proves `R(3,4)=9`. The word dictionary contains six paths, whereas the extremal Ramsey graph contains eight vertices. A source-derived bridge between path histories, graph vertices, and admissibility is still needed.

**Reproduce:** `python cyclic_error_coherence_test.py`. JSON: `cyclic_error_coherence_results.json`. Uses only the Python standard library, enumerates all legal tours and splice errors, and verifies each proposed decoder exhaustively.
