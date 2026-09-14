# The existing A2 wall specialization cannot be the pyramid return map

## Candidate clue

Ledger entry `20260816-285 Primitive Top Specialization into the Invariant A2 Line` supplies a genuine signed incidence:

\[
N_{\rm rel}(g_{111})=\pm(E_1-E_2).
\]

The four marked branches meet the two exceptional components with multiplicity one, so this difference is primitive. At first sight it appears capable of deciding the remaining sum-versus-difference route bit.

## Lattice obstruction

The exceptional target in entry 285 is the \(A_2\) root lattice, with Gram matrix

\[
G_{A_2}=\begin{pmatrix}-2&1\\1&-2\end{pmatrix},
\qquad |\det G_{A_2}|=3.
\]

The fixed-pencil complement of the \(e_6\) row is

\[
\mathbb Z\alpha_{13}\oplus\mathbb Z\alpha_{14}
\]

with Gram matrix

\[
G_{\rm pyr}=\begin{pmatrix}-2&0\\0&-2\end{pmatrix},
\qquad |\det G_{\rm pyr}|=4.
\]

An integral isometry would preserve the discriminant. Since \(3\ne4\), no integral isometry exists between these lattices.

The obstruction remains rationally: \(\det G_{A_2}/\det G_{\rm pyr}=3/4\) is not a square in \(\mathbb Q^\times\), so the two quadratic spaces are not rationally isometric either.

## Consequence

The primitive difference \(E_1-E_2\) verifies the orientation of the conductor degeneration, but it cannot be imported as \(\alpha_{13}-\alpha_{14}\) or \(\alpha_{13}+\alpha_{14}\). Doing so would conflate an \(A_2\) exceptional chain with the orthogonal \(A_1^2\) pyramid complement.

Therefore entry 285 does not decide the final return bit. A genuine comparison would require a non-isometric correspondence with explicitly computed index, scaling, or quotient data; none is presently supplied.

## Refined missing datum

The decisive signed incidence must land directly in the fixed-pencil \(A_1^2\) lattice, or come with an explicit integral correspondence

\[
A_2\longrightarrow A_1^2
\]

whose matrix and cokernel are computed. An unlabeled analogy between the two rank-two root systems is invalid.

Verification:

- `research/voevodsky/checkers/check_A2_pyramid_return_no_go.py`
- `research/voevodsky/results/A2_pyramid_return_no_go.json`
