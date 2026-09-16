# Prior research reduces the Sonin--endpoint gate to a rank-one leverage bound in the two-space paired metric

## Active inequality

After endpoint parity reduction, the positive coupling condition is

\[
C_k\succeq b_kb_k^*.
\]

Prior research gives several equivalent formulations and sharply restricts the admissible proof route.

## Rank-one Schur form

The odd endpoint sector is one dimensional. Let its normalized source vector be \(v_k\), and write the odd endpoint coefficient as \(c_k>0\). Then

\[
b_kb_k^*=c_kv_kv_k^*.
\]

The Schur gate becomes

\[
C_k-c_kv_kv_k^*\succeq0.
\]

For a possibly singular positive operator \(C_k\), this holds exactly when

\[
v_k\in\operatorname{ran}C_k^{1/2}
\]

and

\[
c_k
\|C_k^{\dagger/2}v_k\|^2
\le1.
\]

Thus the gate has two independent parts:

1. a range condition;
2. a scalar leverage bound.

A norm estimate on \(b_k\) alone cannot replace the range condition.

## Douglas contraction

Equivalently, there must exist a vector \(d_k\) in the bulk feature carrier such that

\[
C_k^{1/2}d_k
=\sqrt{c_k}\,v_k
\]

and

\[
\|d_k\|\le1.
\]

This is the rank-one form of the required Douglas contraction.

Successor coherence requires that the vectors \(d_k\) be transported by the source successor maps rather than selected independently at each stage.

## Exact endpoint geometry

On the finite Paley--Wiener interval, the endpoint reproducing vectors are

\[
e_+(x)=e^{x/2},
\qquad
e_-(x)=e^{-x/2}.
\]

Their parity eigenvectors have squared norms

\[
\|e_{even}\|^2
=2(\sinh L+L),
\]

\[
\|e_{odd}\|^2
=2(\sinh L-L).
\]

The hostile channel is the odd harmonic mode. It is the cokernel vector of

\[
\partial_x^2-\frac14.
\]

The cross term is fixed by Green's identity as a Robin/Wronskian boundary trace. It is not a freely adjustable Schur parameter.

## Two-space semilocal metric

The semilocal Sonin transform does not make a reflected multiplier contractive by scalar similarity. Instead it supplies two different Hilbert spaces:

\[
H_S^+
=L^2(|E_S(s)|^2ds),
\]

\[
H_S^-
=L^2(dm_S),
\]

paired by the unweighted integral.

Inverse Euler factors in one space and conjugate Euler factors in the other preserve this pairing isometrically. Their moduli cancel, while differentiation retains the prime phase current.

Therefore the bulk operator \(C_k\) must be formed from the differentiated two-space pairing. It must not be formed from a one-space reflected multiplier norm.

## Falsified routes

Prior research excludes two tempting arguments.

### Finite-rank endpoint projection

Removing the two-dimensional endpoint space cannot repair essential multiplier expansion. Essential norm is invariant under finite-rank perturbation.

### Scalar Sonin weight

A scalar multiplication weight commutes with a scalar reflected multiplier. Similarity by that weight cannot reduce its essential norm.

Hence neither route can prove the Schur inequality.

## Source-derived candidate route

The remaining admissible route is the shifted-Laplacian energy complex. One seeks an intertwiner

\[
T_S
\]

from the differentiated canonical/dual connection into the bulk energy space such that

\[
P T_S
=T_S\mathscr D_{loc,S}
+
\text{controlled trace-class remainder},
\]

where

\[
P=
\partial_x^2-rac14.
\]

Green's identity would then express the endpoint vector as the boundary trace of a bulk energy vector. Contractivity of the intertwiner would yield the leverage bound.

No such intertwiner is currently constructed in the repository.

## Finite-dimensional evidence

The repository contains stable numerical Schur scouts and direct-spectrum checks at several cutoffs. They show no negative direction beyond numerical tolerance and produce positive low-rank Schur margins in selected discretizations.

These calculations are discovery evidence only. They do not provide:

1. certified continuum tail control;
2. range compatibility in the limiting operator;
3. a successor-natural Douglas vector;
4. uniform support exhaustion.

## Logical strength

The completed augmented Green operator is

\[
\mathbb G_S
=
\begin{pmatrix}
\mathcal A_S&B_S^*\\
B_S&J_{end}
\end{pmatrix}.
\]

Its bounded self-adjoint realization is closed. Positivity after odd-parity elimination is exactly the Schur gate above.

Because this completed form is the source realization of the Weil form, global positivity of the Schur complement is not a routine endpoint estimate. It carries the arithmetic positivity content.

Any proof must therefore contain genuinely new arithmetic input or an equivalent positive factorization. It cannot follow from lattice coherence alone.

## Most precise next target

The next analytical object should be the source-normalized odd endpoint vector \(v_k\) represented in the differentiated two-space bulk metric.

One must then establish

\[
v_k\in\operatorname{ran}C_k^{1/2}
\]

and compute or bound

\[
\ell_k
=
 c_k
\|C_k^{\dagger/2}v_k\|^2.
\]

The desired result is

\[
\ell_k\le1.
\]

Successor naturality requires compatible solutions of

\[
C_k^{1/2}d_k
=
\sqrt{c_k}\,v_k.
\]

## Disposition

Prior research supplies the exact endpoint vector, its parity and growth, the Green cross term, the correct two-space semilocal metric, and the Schur--Douglas equivalence.

The missing datum is one source-derived range factorization with leverage at most one. Constructing the shifted-Laplacian/paired-connection intertwiner is the only currently viable analytic route visible in the repository. The resulting inequality is arithmetic-strength, not bookkeeping.
