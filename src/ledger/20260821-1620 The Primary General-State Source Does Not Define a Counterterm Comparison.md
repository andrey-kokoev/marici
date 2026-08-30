# 1620 — The Primary General-State Source Does Not Define a Counterterm Comparison

## Provenance question

Entry 1619 gives a conditional covariance theorem for frozen Hermitian local quadratic counterterms.  Does the primary general-initial-state source specify the counterterm map needed to instantiate that theorem?

Primary source:

N. Agarwal, R. Holman, A. J. Tolley, and J. Lin, *Effective field theory and non-Gaussianity from general inflationary states*, arXiv:1212.1172v2.

## What the source defines

Equations (8)--(15) define the closed-time-path generating functional and the initial density matrix.  Its quadratic boundary kernel is

\[
\mathcal S_2
=
\frac12\int_k
\left(
\Phi_k^+A_k\Phi_{-k}^+
-
\Phi_k^-A_k^*\Phi_{-k}^-
+i\Phi_k^+B_k\Phi_{-k}^-
+i\Phi_k^-B_k\Phi_{-k}^+
\right).
\]

Hermiticity requires \(B_k\) to be real.  Equations (103)--(116) incorporate these kernels into the doubled kinetic operator through initial-time delta functions.  The diagonal real part of \(A_k\) and the \((A_{kI},B_k)\) mixing block are therefore initial-state coefficient data.

Equations (18)--(29) separately define the bulk inflationary EFT action and its quadratic/cubic couplings.

## What the source does not define

The paper contains no loop counterterm prescription and no renormalization map for the finite-time covariance.  In particular, it does not supply:

- a declared bulk-plus-boundary counterterm basis for the loop problem;
- coefficients or normalization conditions for such counterterms;
- a map from those terms to \((x,y,n)\) covariance coordinates;
- a subtraction compatible with the finite excited-state cutoff.

The boundary kernels \(A_k,B_k\) cannot be silently retyped as counterterms.  They parameterize the initial density matrix; the mixed \(B_k\) kernel is statistical state data and is not generally a Hamiltonian tangent direction.

## Narrow result

\[
\boxed{
\text{The primary general-state source does not instantiate Entry 1619's counterterm class.}
}
\]

Therefore the proposed source-counterterm uncertainty test is currently **untyped**, not passed or failed.

This does not weaken the finite regulated Cut positivity of Entries 1617--1618.  It limits only the promotion from the conditional algebra of Entry 1619 to a renormalized source theorem.

## Correction of working language

Earlier research notes referred to “the declared bulk and boundary counterterms.”  Relative to arXiv:1212.1172v2, that phrase was too strong.  The source declares bulk EFT couplings and boundary initial-state kernels, but not the loop counterterm comparison needed here.

## Classification

\[
\text{missing datum}
=
\text{coefficient/renormalization comparison},
\]

not a missing Carrier cell.

## Next admissible moves

Either:

1. freeze a separate primary renormalization source that derives the finite-time bulk and boundary counterterms for this CTP problem; or
2. remain at the finite-regulated theorem and test the complete unrenormalized density-matrix evolution, where positivity follows from \(\rho\mapsto U\rho U^\dagger\), rather than assigning positivity to a subtracted perturbative component.

No counterterm coefficients may be inferred from the desired uncertainty inequality.
