# A computable classical forcing bound for the lattice pilot

## Result and attribution

The **mathematical finite-pattern vertex-coloring pilot** has a uniformly computable sufficient bound. This is a classical Hales–Jewett/Gallai-type consequence, not a new Ramsey theorem or a native Marici derivation of the forcing principle. The reduction uses additive lattice structure and applies more broadly than the tetrahedral–octahedral presentation; no special combinatorial advantage of that presentation is proved.

For a finite nonempty labelled S in the even-sum lattice L and r>=1, put

$$
M=\max_{s\in S}\|s\|_\infty,
\qquad B(r,S)=M\,H(|S|,r),
$$

where H(k,r) is the least positive word length forcing a combinatorial line for every r-coloring of a k-letter word cube. Below, H is specified by an explicit exhaustive algorithm, not left as an unspecified existence oracle. Hales–Jewett supplies the proof of termination of that unbounded mathematical search.

Verification level: written classical-theorem-based proof, exact finite enumeration controls and independent lattice-certificate verification. The classical theorem is an **external mathematical dependency**, not independently proved or proof-assistant checked here. No cross-net proof outcome is imported. The governing native-solvability conjecture remains open.

## Classical input, stated separately

**Finite Hales–Jewett theorem:** for every positive k,r there is a positive n such that every r-coloring of all length-n words over k letters contains a combinatorial line. Such a line fixes some coordinates and fills a nonempty common set of variable coordinates with the same alphabet letter, ranging over every letter.

Classical attribution: A. W. Hales and R. I. Jewett, *Regularity and positional games*, Transactions of the American Mathematical Society 106 (1963), 222–229. This packet uses that established theorem; it does not claim a fresh inspection or reproduction of the original proof.

## Explicit bound algorithm and its termination

For n=1,2,...:

1. Enumerate the k^n words.
2. Enumerate every variable-word template: each coordinate is a fixed letter or a star, with at least one star. There are (k+1)^n-k^n such templates.
3. Enumerate every one of the r^(k^n) colorings of the words.
4. Test whether each coloring has a constant-color line among those templates.
5. Return the first n for which every coloring passes.

Each length test is finite and decisive. A failing test supplies an actual avoiding word coloring at that length. Hales–Jewett guarantees some length passes; hence the idealized unbounded algorithm terminates for every k,r. Thus H and B are computable functions. This is not an efficient algorithm or a claim that its astronomical cases fit available memory.

The reference implementation has explicit word/template/coloring budgets. Exceeding a budget raises `ForcingResourceError`; it does not return an avoiding coloring, an infinite Ramsey obstruction or a numerical radius. Removing resource budgets specifies the mathematical exhaustive search, subject to the usual idealization of unbounded computation rather than an all-input hardware guarantee.

## Word-line to lattice-certificate proof

Use the labels of S as the alphabet, in supplied record order. Map a word w to

$$
\Phi(w)=\sum_{i=1}^n s_{w_i}.
$$

L is closed under addition, so every image lies in L. Each coordinate has absolute value at most nM, so the entire word cube maps into L_(nM). Pull any complete lattice coloring back along Phi.

Let V be the nonempty variable-position set of a monochromatic word line. Define

$$
m=|V|\ge1,
\qquad a=\sum_{i\notin V}s_{w_i}.
$$

The line images are exactly a+mS, in one common color. Their labels are those of S. Distinct S points remain distinct because m>0. Consequently the independent finite-certificate predicate is satisfied. Taking n=H(|S|,r) proves the stated forcing bound for **all** finite patterns and finite color counts, not only the tetrahedral and octahedral fixtures.

Phi need not be injective on the whole word cube: exchanging two fixed letters can give the same sum. This causes no problem for color pullback or for the injective image of an individual line. It does mean this reduction is **not** a faithful native encoding of every word history. The implementation retains the variable-word template and alphabet labels beside the returned lattice certificate; it does not claim native replay of the Hales–Jewett proof or of the exhaustive forcing search.

## Completely explicit small families

- Singleton S, or r=1: n=1 suffices, so B=M. This includes S={0}, M=B=0.
- Two-point S: H(2,r)=r, so B=rM suffices. A maximal chain of the Boolean word cube of length r has r+1 words; pigeonhole gives a same-colored comparable pair, which is a binary combinatorial line. Conversely, at length r-1 color by Hamming weight; all r ranks have different colors, so no line is monochromatic. The r=1 case uses the positive-length convention directly.

These are sufficient lattice radii, not claims of smallest possible geometric radii. B depends on the chosen origin and template coordinates; no canonical or translation-invariant minimal bound is asserted.

## Executable tests and limits of the conclusion

Implementation: `research/voevodsky/ramsey_forcing.py`.

The source-bound checker tests finite Hales–Jewett lengths directly, validates avoiding-coloring witnesses independently, checks the binary formula, exercises exact labelled word-line projection and runs the existing independent certificate verifier on resulting lattice witnesses. An existing marked scale-two tetrahedral fixture is linked to the length-two all-variable template: this is a line for that particular pulled-back coloring, **not** a claim that word length two forces every two-color tetrahedral pattern.

Practical budgets do not compute a numerical two-color forcing radius for the tetrahedron or octahedron in this work. The classical computable construction is established at written-proof scope; a native Marici forcing argument, efficient bounds, exact Ramsey numbers and graph/hypergraph extensions remain separate.

- Prospective scope: `research/voevodsky/contracts/ramsey-uniform-bound-attempt.v1.json`.
- Checker: `research/voevodsky/checkers/check_ramsey_uniform_bound.py`.
- Receipt: `research/voevodsky/results/ramsey-uniform-bound-v1.json`.
- SCC model: `research/voevodsky/scc-models/ramsey-uniform-bound-v1.json`.
