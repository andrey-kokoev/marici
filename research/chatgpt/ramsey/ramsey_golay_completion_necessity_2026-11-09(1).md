# Necessity audit: from the seven-rotation quotient to a Golay completion

9 November 2026

## Question

Does retained composition of the binary encoding of `RGRGR00` **force** the 23-position, 11-bit quadratic completion, rather than merely admit one?

**Result.** Two distinct claims must be separated.

1. Retention of the original seven-position quotient, full permutation symmetry on its seven marked directions, and injectivity of all syndromes of three or fewer marks **do not force** any sixteen-position extension. An 8-position, 7-bit extension satisfies those conditions.
2. If the next stage is additionally required to be a *strictly larger perfect binary three-error quotient*, elementary arithmetic forces 23 positions and 11 syndrome dimensions. Any extension containing the original six-dimensional quotient then forces the sixteen new columns to project to a full affine 4-space in the five new dimensions, yielding the canonical `1 parity + 4 phase` structure up to coordinates. The six old comparison coordinates are independently fixed by the full seven-direction exchange symmetry.

The quadratic **incidence function** itself has not been proved to be selected by these constraints, nor has perfect-packing preservation been derived from the original R/G/0 composition history. No Ramsey adjacency readout has been constructed.

## I. Exact root

Let `x` be the red-position indicator of `RGRGR00` in `F₂⁷`, and let `T` rotate the seven positions. Its seven translates are independent and their sum is the all-ones word. Modding out by that invariant line gives `U = F₂⁷/<1>`, dimension six, with seven distinguished directions `h_i` satisfying the unique relation `sum_i h_i=0`. The 64 subsets of at most three directions have distinct sums and exhaust `U`.

These are facts about the explicit binary encoding and its XOR operation. They are not consequences of color reflection without that encoding.

## II. Nonforcing counterexample

Take the same seven syndrome columns in `U ⊕ F₂` and adjoin one column `g=(0,1)`. All 93 subsets of at most three among eight positions have distinct syndromes: old-only subsets lie in the zero final coordinate; subsets containing `g` have final coordinate one and the remaining old subsets use at most two marks. The syndrome space has 128 points, so this extension has 35 unused states.

The full `S₇` action on the seven old distinguished directions extends to this state by fixing `g`. Thus symmetry, retention and collision-freedom alone permit an extension of length eight. They do not force the 16 new phase positions, or perfect saturation.

## III. Elementary packing-length theorem

Let `n≥7` be the number of columns in a binary syndrome system in which every `≤3`-mark subset maps bijectively onto an `r`-dimensional F₂-space. Then

`1+n+binom(n,2)+binom(n,3)=2^r`, equivalently

`(n+1)(n²-n+6)=6⋅2^r`.

Put `a=n+1`, `b=n²-n+6=a²-3a+8`. The product `ab=3⋅2^(r+1)`, so neither factor has a prime divisor other than 2 or 3, and the total exponent of 3 is one. If `16|a`, then `b ≡ 8 (mod 16)`, so `b` has exactly three factors of 2 and must equal 8 or 24, impossible for `a≥16` since `b≥216`. Therefore `16 ∤ a`. Thus `a∈{1,2,4,8,3,6,12,24}`. Direct substitution gives only `n∈{0,1,2,3,7,23}` satisfying the power-of-two identity. For `n≥7`, the possibilities are **7 and 23**.

Consequently **if** a strict successor is required to preserve perfect binary three-mark packing, the next possible length after seven is 23 and its dimension is eleven (`2^11=2048`). This is a theorem of the imposed packing condition, not an intrinsic selection theorem for the original Ramsey generator.

## IV. Forced structure of the sixteen new columns

Assume a perfect 23-column rank-11 syndrome representation that contains the old seven-column rank-six system. Let `W` be the five-dimensional quotient by the old syndrome span `U`, and let `p_1,...,p_16 ∈ W` be the projected new columns.

- No `p_i` can be zero: the corresponding new column would equal a sum of `≤3` old columns and create a collision.
- No two can agree: their difference would be a sum of `≤3` old columns, again yielding a collision.
- No three distinct projections can sum to zero: the sum of their full columns would lie in `U`, hence equal some sum of `≤3` old columns, giving a nonzero dependency of weight `≤6`. Such a dependency makes two distinct `≤3`-mark syndromes equal.

Thus `P={p_i}` is a *sum-free* subset of `W=F₂⁵` with 16 elements. Any sum-free subset of an elementary abelian 2-group containing half its elements is the nonzero coset of an index-two subgroup. Proof: `P∩(P+P)=∅`, while fixing `a∈P` gives `P+a ⊂ P+P` with 16 members, so `P+P=W\P=P+a`. Therefore `H=P+a` is closed under addition, contains zero and has 16 elements; it is a subspace. Hence `P=a+H` is an affine hyperplane.

After an invertible change of syndrome coordinates, **every** such completion has projected columns

`p_z=(1,z)` for all `z∈F₂⁴`.

This derives the `one parity + four phase` decomposition **conditionally**, without choosing a quadratic incidence decoder. There are exactly 31 nonzero affine-hyperplane cosets in `F₂⁵`, all equivalent under `GL(5,2)`.

## V. Old six-dimensional quadratic form and the constraint on any decoder

Full `S₇` symmetry on the seven independent directions modulo their collective relation forces the unique *nonzero, nondegenerate* invariant alternating form `B(h_i,h_j)=1` for distinct `i,j`. The invariant quadratic refinement satisfies `Q(h_i)=1`, because `Q(sum_i h_i)=7⋅1+binom(7,2)=0` in `F₂`. It is a plus-type form (36 isotropic vectors, including zero; 28 anisotropic vectors).

After the forced projection normalization, the 16 new full columns can be written

`g_z=(f(z), 1, z)`, `f:F₂⁴→U`.

For each affine parallelogram `{z,z+a,z+b,z+a+b}` with independent `a,b`, its four projections cancel. Let

`D_{a,b}f(z)=f(z)+f(z+a)+f(z+b)+f(z+a+b)`.

If this value were zero or anisotropic (`Q=1`), it would be represented by zero, one, or two old columns. Those four new columns together with `≤2` old columns would be a forbidden dependency of weight `≤6`. Therefore *every admissible perfect decoder necessarily satisfies*

`D_{a,b}f(z) ≠ 0`, `Q(D_{a,b}f(z))=0`.

There are 140 affine parallelograms in `F₂⁴`, and 35 possible nonzero isotropic directions in `U`. The existing choice `f(z)=ν₂(z)` (the six squarefree quadratic monomials), after a source-to-orthogonal-form isometry, attains this condition: `D_{a,b}ν₂=a∧b`, independent of `z`, ranging over all 35 nonzero decomposable bivectors.

The condition `D_{a,b}f(z)` is nonzero singular has **not** been shown to force `f` to have polynomial degree two. A stronger comparison law `D_{a,b}f(z)=a∧b` *would* force `f=ν₂+L(z)+c` for an affine-linear map `L(z)+c`, but that stronger law is not derived from the original history composition.

## VI. Finite audit

`python check_seven_frame_completion_necessity.py`

Checks performed with exact F₂ bit arithmetic:

- 8-position counterexample: 93 distinct `≤3` syndromes out of 128.
- Unique seven-frame invariant quadratic form; 36 zeros; explicit source-frame-to-exterior-square isometry.
- 31 affine hyperplanes of size 16 in `F₂⁵`.
- 140 phase parallelograms and 35 nonzero singular second differences of `ν₂`.
- All 24 single cubic-coordinate mutations of `ν₂` fail three-mark injectivity; all six single quartic-coordinate mutations fail. This is a **restricted perturbation test**, not an exhaustive classification of all nonlinear decoders.
- The companion `ramsey_heptad_quadratic_golay_constructor.py` constructs and checks the complete perfect Golay example, including the Steiner systems.

## VII. Next actual question

The remaining inference gap is at the first arrow:

`retained R/G/0 composition` -> **preservation of perfect three-mark packing**.

If a native promotion rule does not enforce perfect packing, the eight-position example already refutes necessity of the Golay leap. If it does enforce packing, the next length and the parity-plus-four-phase projection are mathematically forced; the nontrivial remaining selection is the six-coordinate decoder `f`, particularly whether its second derivatives are dictated by the retained comparison operations.

No conclusion about `R(3,k)` follows until an incidence-preserving map links this syndrome system to the triangle-free/independence constraints. In particular, 23 Golay coordinates and the forbidden threshold `R(3,7)=23` are not the same object.
