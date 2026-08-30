# Entry 1617 — The Statistical Dyson Jet Factors Through the Labelled Production Cut

## Claim

At the occurrence-resolved integrand level, the Keldysh-noise contribution to
the statistical Dyson covariance equals the Cut norm of the source production
response.

## Exact factorization

Let \(C\) retain the bulk/surface location cells and the two ordered internal
occurrences.  Let \(R\) be the retarded map from those source cells to one
component of the marked phase-space jet.  The noise kernel is

\[
N=C C^\dagger.
\]

Associativity gives the exact identity

\[
\boxed{
R N R^\dagger
=R C C^\dagger R^\dagger
=(RC)(RC)^\dagger.
}
\]

The right side is the production-amplitude Cut norm seen by the covariance
projector.

## Source normalization checks

Two independent finite checks remove possible multiplicity defects:

1. the labelled cubic Wick census has 36 connected fish contractions in each
   of the \(BB,BS,SS\) sectors;
2. the ordered internal occurrences \((q,k)\) and \((k,q)\) are exchanged by
   the measure-preserving involution, so their factor two cancels the
   identical-pair \(1/2!\).

Thus no fitted sector normalization is needed.

## Consequence

Together with Entries 1607, 1613, 1615, and 1616, this closes the algebraic
part of the conjecture:

\[
\text{Gaussian second-Rees statistical completion}
=
\text{labelled Keldysh Cut norm}
\]

before continuum integration.

## Remaining qualifications

- the physical continuum phase-space measure must be positive in the chosen
  convention;
- the bra operation must be the physical Hermitian conjugation, not a formal
  transpose;
- regulator removal and the finite EFT cutoff must preserve the identity;
- the result concerns the two-point covariance layer, not global Gaussianity
  of the interacting state.

## Artifacts

- `research/benincasa/marici-gm/src/bin/gaussian_dyson_cut_factorization.rs`
- `research/benincasa/results/gaussian-dyson-cut-factorization.json`
- `research/benincasa/gaussian-dyson-cut-factorization.md`

Allocator claim: `seqclaim-d9a5ae1080419476d235e31d`.
