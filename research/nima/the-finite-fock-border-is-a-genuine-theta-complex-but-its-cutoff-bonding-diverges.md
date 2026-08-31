# The finite Fock border is a genuine theta complex but its cutoff bonding diverges

## Correction

The statement that no theta complex has been constructed requires one
qualification.  The symmetric-Fock multiplicative border gives a genuine
source-derived complex for every finite prime cutoff.  What is missing is its
completed cutoff-compatible limit.

## Finite complex

For finite \(X\), let

\[
u_X(s)=\Gamma_X(L_X(s))
\in\mathcal T_1(\mathcal F_X)
\]

and let

\[
y_X=\operatorname{Tr}_{\mathcal F_X}.
\]

On

\[
V_X=\mathcal T_1(\mathcal F_X)\oplus\mathbb C
\]

define the bounded Fredholm map

\[
D_X(s)=
\begin{pmatrix}
I&u_X(s)\\
y_X&0
\end{pmatrix}.
\]

Regarded as a differential from degree zero to degree one, this defines the
two-term complex

\[
T_{\theta,X}(s):
0\longrightarrow V_X
\xrightarrow{D_X(s)}V_X
\longrightarrow0.
\]

There is no square-zero issue: a two-term complex has no successive nonzero
differential to compose.

The Fredholm determinant is

\[
\det_{\rm Fr}D_X(s)
=-y_Xu_X(s)
=-\zeta_X(s).
\]

Tensoring with the finite archimedean and endpoint line gives the finite
completed determinant character.

## Cutoff factorization

For disjoint finite prime sets \(X\) and \(Y\),

\[
\mathcal F_{X\sqcup Y}
\cong
\mathcal F_X\widehat\otimes\mathcal F_Y,
\]

\[
u_{X\sqcup Y}=u_X\otimes u_Y,
\qquad
y_{X\sqcup Y}=y_X\otimes y_Y.
\]

Hence

\[
y_{X\sqcup Y}u_{X\sqcup Y}
=(y_Xu_X)(y_Yu_Y),
\]

which is exactly Euler-product cutoff multiplicativity.

The bonding map cannot be vacuum inclusion alone.  It must tensor the state
with \(u_Y(s)\), otherwise it discards the new prime loops.

## Norm of the bonding state

The trace norm of the added-prime factor is

\[
\|u_Y(s)\|_1
=
\prod_{p\in Y}(1-p^{-\operatorname{Re}s})^{-1}.
\]

For an exhausting sequence of prime cutoffs, the bonding norms remain bounded
only when

\[
\operatorname{Re}s>1.
\]

On the critical strip they diverge.  Thus the finite complexes do not form a
uniformly bounded inductive system in the ordinary trace-class/Fock topology.

## First failed completion arrow

The obstruction is now sharper than the absence of an abstract differential:

- each finite differential exists;
- each finite determinant has the correct Euler character;
- cutoff multiplicativity is exact;
- the required state bonding maps lose uniform norm at the Euler boundary.

The trace observer fails simultaneously in the infinite limit.  These are the
same prime-mass divergence seen from the column and row sides.

## Relation to the three-stratum line

The order-three determinant construction renormalizes the cutoff transition
as a determinant line by separating primitive and square anomaly data from
the connected tail.  It does not provide a bounded limit of the bordered Fock
differentials.

Therefore the completed theta complex, if it exists, must replace the
trace-class Fock bonding by a three-stratum relative complex whose transition
maps carry anomaly-line data.  Merely applying the scalar theta--Poisson
functional after the divergent limit would not construct its kernel.

## Revised earliest G4 constructor

The finite complex is available.  The earliest missing completed datum is a
relative cutoff bonding morphism

\[
\beta_{X,X'}:
T_{\theta,X}\longrightarrow T_{\theta,X'}
\]

whose primitive and square divergences land in their declared anomaly lines,
whose connected component is \(\mathcal S_3\)-controlled, and whose cone has a
uniformly bounded contraction after reciprocal boundary sewing.

This is more precise than asking for an unspecified theta differential.  No
such completed bonding morphism is currently constructed, and no RH
conclusion is authorized.
