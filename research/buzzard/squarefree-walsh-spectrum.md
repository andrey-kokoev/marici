# Squarefree Walsh spectrum: Lean packet

Source: `research/grothendieck/squarefree-prime-cube-walsh-positivity-theorem.md`.

`RealAddCharacter` is the minimal real exponent-two character interface on a
finite additive commutative group: it preserves zero and addition and is
invariant under negation. `finiteConvolution_apply_character` proves that such
a character is an eigenvector of `finiteConvolution`, with eigenvalue

\[
\sum_y f(y)\chi(y).
\]

This is the exact diagonal-action layer. The converse statement that
nonnegative character eigenvalues imply positive semidefiniteness additionally
needs a complete character basis and a Hermitian quadratic-form transport.
`FiniteCharacterCompleteness.lean` supplies the former using Mathlib's finite
Pontryagin duality: complex additive characters form a basis of `G → ℂ`, their
number equals `|G|`, and the complete basis diagonalizes the complex finite
convolution convention used here.

`SpectralCongruencePSD.lean` supplies the Hermitian transport theorem. For an
invertible complex synthesis matrix `U` and real spectrum `λ`,

\[
U^*\operatorname{diag}(\lambda)U\succeq0
\quad\Longleftrightarrow\quad
\lambda_i\ge0\ \text{for every }i.
\]

Its hostile zero-synthesis example proves why invertibility cannot be omitted:
a noninvertible congruence can erase a negative spectral channel.

`FiniteCharacterSynthesis.lean` constructs a square synthesis matrix rather
than assuming one. It reindexes the point-mass basis by a cardinality
equivalence with the character type, takes the character change-of-basis
matrix, proves it is a unit, and identifies its inverse as the reverse
change-of-basis matrix. The chosen reindexing is deliberately noncanonical;
positivity cannot depend on that enumeration.

`FiniteCharacterOrthogonality.lean` fixes the normalization convention: the
character Gram matrix for the uniform finite-group average is exactly the
identity, and distinct characters have zero normalized overlap. This is the
orthogonality statement corresponding to the raw relation
`Uᴴ U = |G| I`, without introducing a square root of the cardinality into the
coefficient field.

`FiniteConvolutionReconstruction.lean` closes the finite spectral identity at
the invariant level. It bundles convolution as a complex linear operator and
proves that it equals the unique operator constructed from the complete
character basis by multiplying each character by its Fourier coefficient.
This statement is independent of the noncanonical enumeration used to display
a square matrix; the coordinate congruence is its basis representation.

For a finite prime-label type `ι`, `tensorWalshCoefficient` sums the exact
tensor correlation over all squarefree subsets. The theorem
`tensorWalshCoefficient_factorization` proves

\[
\sum_{S\subseteq\iota}\prod_{i\in S}\varepsilon_i r_i
=\prod_i(1+\varepsilon_i r_i).
\]

`tensorWalshCoefficient_nonnegative` then proves every coefficient is
nonnegative under the pointwise assumptions `|r_i| ≤ 1`. Thus the exact tensor
branch is separated from the additive-edge branch, where the shared `l1`
budget in `AdditivePrimeEdgeBudget.lean` is necessary.

Typing boundary: convolution uses a finite additive commutative group and real
coefficients; the concrete tensor theorem uses an arbitrary finite label type
and Boolean polarities. The finite Fourier diagonalization, completeness,
normalization, reconstruction, and PSD transport are covered. The remaining
source interface is a route-independent completed Weil correlation on each
squarefree cube, together with its identification as the translation kernel
fed to this finite theorem. Route holonomy is not averaged away.

Verification boundary: Nima's active no-build instruction remains in force.
Only bounded static scans were run; the module remains outside
`MariciFormal.lean`.
