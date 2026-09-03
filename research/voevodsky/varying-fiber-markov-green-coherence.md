# Varying-fiber Markov Green coherence

## Question

Does the operator-valued coherence fragment survive when adjacent vertices carry different finite-dimensional fibers?

## Claim boundary

This packet treats finite chains of explicitly typed real fibers \(H_i=\mathbb R^{d_i}\) and rectangular contractions \(A_i:H_{i+1}\to H_i\). It does not infer identifications between unequal fibers and does not yet construct an infinite varying-fiber completion.

## Typed kernel

For \(i<j\), define

\[
K_{ij}=A_iA_{i+1}\cdots A_{j-1}:H_j\to H_i,
\qquad K_{ji}=K_{ij}^T,
\qquad K_{ii}=I_{H_i}.
\]

Every product is type-checked by its intermediate fiber. Assume

\[
I_{H_{i+1}}-A_i^TA_i\succeq0.
\]

Then the block kernel is the covariance of the typed recursion from \(H_i\) to \(H_{i+1}\), hence is positive semidefinite on \(\bigoplus_iH_i\).

## Coherence

Seam-compatible amalgamation concatenates rectangular transfers only when codomain and domain dimensions match. Associativity of typed matrix multiplication makes the associator identity and the pentagon strict. An intentionally dimension-mismatched seam is undefined rather than coerced by equal ranks elsewhere.

For orthogonal gauges \(U_i\in O(H_i)\), transformed edges

\[
A_i'=U_iA_iU_{i+1}^T
\]

have the same source and target types. Internal gauges telescope, proving compatible-gauge interchange. Companion and conjoint witnesses are respectively \(U_i\) and \(U_i^T\) on each typed fiber.

## Contiguous Beck–Chevalley

Restricting to a contiguous vertex interval preserves every intermediate fiber and transfer. Principal block compression therefore equals reconstruction from the restricted typed edge list, with identity comparison and strict nested pasting.

## Hostile boundary

Deleting an intermediate vertex would require a declared effective rectangular transfer equal to the ordered composite. Equal endpoint dimensions do not supply such a declaration. Permuting block coordinates without their fiber labels is likewise rejected.

## Disposition

Finite analytic partial-double-category coherence and the orthogonal gauge equipment fragment extend to varying finite fibers. Infinite completion and arbitrary fiber-changing vertical arrows remain open.

## Verification

- `research/voevodsky/checkers/check_varying_fiber_markov_green.py`
- `research/voevodsky/results/varying_fiber_markov_green.json`
