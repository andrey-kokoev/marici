# Compact Correlation Reduces Completion Escape to a Fredholm Eigenstate

Let the phase-sensitive normalized correlation operator be

\[
H=R^*R=D+K,
\]

where \(D\) is a bounded background satisfying \(0\le D\le dI\) for some
\(d<1\), and \(K\) is compact self-adjoint. Because \(H\) comes from a Gram
block, assume \(0\le H\le I\).

Weyl stability places the essential spectrum of \(H\) below or at \(d\).
Every spectral point above \(d\) is therefore an isolated eigenvalue of
finite multiplicity. It follows that

\[
I-H\text{ is coercive}
\quad\Longleftrightarrow\quad
\ker(I-H)=0.
\]

Under this compact-remainder hypothesis, injectivity is enough: eigenvalues
below one cannot accumulate at one because one lies strictly above the
essential spectral ceiling. Equivalently, completion invisibility can occur
only through an actual finite-dimensional eigenstate

\[
Hv=v.
\]

This is a Fredholm reduction, not an exclusion theorem.

## Finite-stage hostile

Let \(u_i=\sqrt3/2^i\) on \(\ell^2(\mathbb N)\), so \(\|u\|=1\), and set

\[
H=\frac12I+\frac12uu^*.
\]

The remainder is rank one, hence compact, while \(Hu=u\). The first \(N\)
coordinates satisfy

\[
\|P_Nu\|^2=1-4^{-N}
\]

and the largest eigenvalue of the finite compression is

\[
1-\frac1{2\,4^N}<1.
\]

Thus every finite stage is strictly coercive, yet the completed operator has
the exact invisible eigenstate \(u\). Compactness explains the failure as one
rank-one obstruction; it does not let finite nonvanishing rule it out.

## Noncompact contrast

For the diagonal operator

\[
He_n=(1-n^{-1})e_n,
\]

there is no eigenvector at one, but \(I-H\) is not coercive. The normalized
states \(e_n\) become asymptotically invisible. This diffuse escape is possible
because the correlation remainder is not compact relative to any background
whose spectral ceiling is uniformly below one.

## Theta/Tate consequence

Grothendieck now has a theorem-changing fork:

1. Prove that the completed phase-sensitive correlation is a compact
   perturbation of a uniformly subcritical background. The RH-bearing gate
   becomes exclusion of the finite-dimensional equation \(Hv=v\).
2. If compactness fails, one must control essential-spectrum escape directly;
   absence of an exact invisible state is no longer enough.

Analytic dependence on \(s\) could further turn the finite-dimensional
obstruction into an analytic Fredholm determinant, but that requires a
source-derived analytic compact family and is not supplied here.

## Falsifiers

- Compactness is inferred from finite rank at every cutoff.
- The background ceiling \(d<1\) is not uniform.
- Absence of a finite-cutoff eigenvalue one is used to exclude a completed
  eigenstate.
- Injectivity is promoted to coercivity without the compact-remainder theorem.
- Analytic Fredholm theory is invoked before analytic dependence and domain
  constancy are proved.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The goal was to decide what compactness would genuinely buy.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Compactness is shown to eliminate diffuse escape but leave a finite
eigenstate obstruction, with exact compact and noncompact hostiles separating
the two regimes.
