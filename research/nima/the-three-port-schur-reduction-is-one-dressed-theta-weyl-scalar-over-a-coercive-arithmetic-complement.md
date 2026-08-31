# The three-port Schur reduction is one dressed theta Weyl scalar over a coercive arithmetic complement

> **Crossing readback.** The seam-weighted summed incidence
> \(B_\Sigma:U\to H_\theta\) is Hilbert--Schmidt and supplies the common G4
> history crossing without an unweighted theta diagonal. Interpret every
> \(B\) below as \(B_\Sigma\). The formulas are completed off-seam Schur
> identities; seam use still requires limiting absorption.

## Minimal source characteristic

After the independent source-order audit, use

\[
D_\theta=0,
\qquad
R=0.
\]

Let

\[
R_H(z)=(A-z)^{-1}
\]

and define the history-eliminated two-port matrix

\[
M_{\theta U}(z)
=
\begin{pmatrix}
V^\dagger R_HV & V^\dagger R_HB\\
B^\dagger R_HV & Q_U(z)
\end{pmatrix},
\]

where

\[
Q_U(z)=D_U(z)+B^\dagger R_H(z)B.
\]

Frozen Green conventions may change both off-diagonal signs; the Schur product
must change coherently.

## Arithmetic complement

Assume \(Q_U(z)\) is invertible on the declared chart. The G3 margins are
eligible to control this block because it belongs to the retained
arithmetic/history complement rather than the theta divisor coordinate.

The needed estimate is compact-local and cutoff-uniform:

\[
\|Q_{U,X}(z)^{-1}\|
\le C_K
\]

for \(z\) in a compact parameter set \(K\).

## Dressed theta scalar

Eliminating the arithmetic source coordinate gives the scalar theta Schur
complement

\[
F_\theta(z)
=
V^\dagger R_HV
-
V^\dagger R_HB
Q_U(z)^{-1}
B^\dagger R_HV.
\]

Equivalently,

\[
F_\theta(z)
=
V^\dagger
\left(
R_H-R_HB Q_U^{-1}B^\dagger R_H
\right)V.
\]

Thus arithmetic feedback dresses the bare theta Weyl function by one exact
return through the coercive complement.

## Determinant factorization

At finite cutoff,

\[
\det M_{\theta U}(z)
=
\det Q_U(z)\,F_\theta(z).
\]

In the completed setting this becomes a determinant-line factorization with
\(\det_{\rm rel}Q_U\) interpreted in its declared ideal. If \(Q_U\) is
uniformly invertible, its determinant section is a unit after the separate
trace-mass completion test.

Therefore every divisor of the full three-port characteristic belongs to the
one-dimensional scalar \(F_\theta\).

## Exact Xi comparison target

The remaining divisor theorem is now

\[
F_\theta(z)=E_\theta(z)\tau(z),
\qquad
E_\theta(z)\ne0.
\]

Here \(\tau\) is the two-sided Evans mismatch equal to the Xi section in the
source frame. This identity is stronger than equality of zero sets and fixes
multiplicity.

It must be proved from the source history, arithmetic law, incidence, and
boundary matching. Defining \(D_U\) or \(E_\theta\) from the quotient
\(F_\theta/\tau\) is forbidden.

## Kernel map and seam qualification

Inside a history-resolvent chart, a zero of \(F_\theta\) gives

\[
x_z
=
-Q_U(z)^{-1}B^\dagger R_H(z)V c,
\]

\[
u_z
=R_H(z)(Vc+Bx_z).
\]

These formulas produce the paired kernel state without requiring
\(Bx=\Phi\).

On the critical seam, \(A-z\) may meet continuous spectrum, so \(R_H(z)\)
need not exist as a bounded Hilbert-space resolvent. Applying the formulas to
an Xi zero requires a source limiting-absorption or rigged-history theorem
showing that the dressed Schur expression and reconstructed state have
boundary values in the declared maximal-isotropic domain. Scalar analytic
continuation of \(F_\theta\) is insufficient.

## Multiplicity

Holomorphic invertibility of \(Q_U\) makes Schur elimination a holomorphic
triangular equivalence. Hence the local cokernel length of the full source
matrix equals the vanishing order of \(F_\theta\). The comparison
\(F_\theta=E_\theta\tau\) then preserves Xi multiplicity.

## G4 consequence

The three-port G4 problem has reached one scalar, source-typed residual:

\[
\mathcal R_{\theta,\rm dress}(z)
=
F_\theta(z)-E_\theta(z)\tau(z).
\]

All other states belong to the arithmetic/history complement \(Q_U\), where
G3 may supply inverse control. No RH conclusion is authorized until the
source identity and unit property are proved.
