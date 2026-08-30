# Unit-equivariant character twists do not constrain the trivial Riemann block

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact twisted-sector descent no-go

## Character decomposition

The compact norm-one idele-class symmetry decomposes a source module into
character sectors. At finite conductor this is the ordinary Fourier
decomposition of a finite abelian unit group:

\[
\mathcal H=\bigoplus_\chi\mathcal H_\chi.
\]

The standard Riemann vacuum lies in the trivial sector. Nontrivial sectors
produce twisted Dirichlet or Hecke data.

## Equivariance theorem

Let \(T\) be a source-authorized comparison commuting with the unit action.
For \(v_\chi\in\mathcal H_\chi\) and
\(v_\psi\in\mathcal H_\psi\), equivariance gives

\[
\langle v_\chi,Tv_\psi\rangle=0
\qquad(\chi\ne\psi).
\]

Equivalently, \(T\) is block diagonal in character coordinates:

\[
T=\bigoplus_\chi T_\chi.
\]

Thus positivity, unitarity, or resonance information in a nontrivial twist
does not constrain the trivial block unless an additional source operation
couples distinct characters.

## Minimal exact model

For the cyclic group of order four, every equivariant operator is a
circulant polynomial in the regular shift. The character Fourier transform
diagonalizes it exactly. The matrix element between the trivial character and
each nontrivial character vanishes.

This finite model is not an analogy but the local representation-theoretic
mechanism used at every finite abelian unit quotient.

## Consequence for the proposed twisted attack

Collecting all completed \(L(s,\chi)\) functions gives a larger block system,
but no descent theorem to \(\zeta(s)\). Products such as a cyclotomic Dedekind
zeta aggregate the blocks at determinant level; they do not make one block's
resonance confinement follow from the others.

To obtain a genuine comparison, one must derive an operation that is not
diagonal in the unit characters. Such an operation must be independently
authorized by arithmetic incidence—induction, restriction, conductor change,
or rational-boundary transport. It cannot be added merely to couple the
desired zeros.

## Return to the primary RH target

The rational diagonal boundary is the most plausible non-character-diagonal
object because it is an incidence relation in the full additive adelic phase
space, not a vector inside one compact unit representation.

Therefore the next attack returns to the existing Lagrangian-incidence
programme: construct the closed boundary trace relation directly and test
maximal self-adjointness. Character enlargement alone cannot substitute for
that construction.

## Scope

This theorem applies to unit-equivariant operators. A genuinely
source-derived operation changing conductor or unit type may mix blocks, but
its authority and descent law must be proved separately.

## Verification

The checker diagonalizes the full commutant of the regular cyclic order-four
unit action and verifies vanishing cross-character matrix elements.
