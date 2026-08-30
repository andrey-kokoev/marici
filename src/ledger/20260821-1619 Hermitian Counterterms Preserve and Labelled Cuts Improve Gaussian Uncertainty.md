# 1619 — Hermitian Counterterms Preserve and Labelled Cuts Improve Gaussian Uncertainty

## Hard-to-vary claim

For the finite-EFT covariance object of Entry 1618, freeze the admissible local counterterms before testing positivity.  If those counterterms arise from a Hermitian local quadratic Hamiltonian, their covariance action preserves the Gaussian uncertainty determinant, while the labelled Cut norm contributes positive-semidefinite noise and cannot lower it.

## Covariance convention

Let

\[
V=
\begin{pmatrix}
n+\frac12+x&y\\
y&n+\frac12-x
\end{pmatrix}.
\]

Then

\[
\det V-\frac14
=n+n^2-x^2-y^2,
\]

which is the uncertainty excess and Rees expansion of Entry 1607.

## Counterterm direction

A Hermitian local quadratic counterterm is represented by a symmetric matrix \(H\).  With the canonical symplectic matrix \(J\), its generator is

\[
A=JH,
\qquad
\operatorname{tr}A=0,
\]

and

\[
\dot V_{\rm ct}=AV+VA^T.
\]

Hence

\[
\frac{d}{dt}\det V
=2\operatorname{tr}(A)\det V
=0.
\]

This is a canonical/Hamiltonian transport statement, not a subtraction chosen after seeing the covariance.

## Cut direction

Entries 1617--1618 give the finite-EFT Cut contribution as an integral of outer products,

\[
N=\int_{\mathcal D_\Lambda}d\mu\,CC^\dagger\succeq0.
\]

For \(V\succeq0\),

\[
\left.
\frac{d}{d\epsilon}
\det(V+\epsilon N)
\right|_{\epsilon=0}
=
\operatorname{tr}(\operatorname{adj}(V)N)
\geq0.
\]

The checker verifies the Hamiltonian identity on 38,416 exact integer cases and the rank-one Cut inequality on 668,850 exact integer cases.

## Narrow result

\[
\boxed{
\text{frozen Hermitian local quadratic counterterms preserve Gaussian uncertainty, while labelled Cut noise improves or preserves it.}
}
\]

Thus no counterterm-versus-Cut obstruction appears at finite EFT cutoff in this admissible class.

This does **not** establish:

- that every cosmological renormalization prescription acts Hamiltonianly on the reduced covariance;
- positivity of an arbitrarily isolated finite subtraction;
- a cutoff-free renormalized positivity theorem;
- Gaussianity of the complete interacting state.

## Architectural update

The tested second-Rees mechanism now has a typed finite chain:

\[
\text{marked Gaussian first jet}
\longrightarrow
\text{second-grade labelled Cut norm}
\longrightarrow
\text{finite-EFT positive covariance},
\]

with local Hermitian counterterms acting tangentially to the uncertainty determinant.  This supports the shared-carrier/sector-specific-coefficient hypothesis H2 and supplies no evidence for a new cosmological carrier stratum.

## Durable artifacts

- `research/benincasa/checkers/gaussian_counterterm_cut_uncertainty.rs`
- `research/benincasa/results/gaussian-counterterm-cut-uncertainty.json`
- `research/benincasa/gaussian-counterterm-cut-uncertainty.md`

## Next falsifier

Derive the actual finite-time quadratic counterterm action from the source Schwinger--Keldysh kernel and test that its reduced covariance map lies in the Hamiltonian tangent class above.  If a source-required local term has a non-Hamiltonian symmetric component, compute its uncertainty derivative before adding the Cut term; do not repair it by a fitted finite subtraction.
