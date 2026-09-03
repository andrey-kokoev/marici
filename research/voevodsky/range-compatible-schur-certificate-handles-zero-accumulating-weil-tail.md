# A range-compatible Schur certificate handles a zero-accumulating Weil tail

## Question

What exact positivity certificate remains valid when the compact local Weil operator has eigenvalues accumulating at zero, so the tail has no uniform positive gap?

## Claim boundary

A strict tail lower bound is unnecessary. For a positive semidefinite tail block, full block positivity is equivalent to a range condition plus a generalized Schur-complement inequality. This identifies the exact finite/tail coherence data needed for local Weil positivity. It does not prove those conditions for the Weil operator.

## Block decomposition

For a finite trial projection \(P_M\), write

\[
A
=
\begin{pmatrix}
F&B\\
B^*&C
\end{pmatrix}.
\]

Here \(F=P_MAP_M\), \(C=(1-P_M)A(1-P_M)\), and \(B=P_MA(1-P_M)\).

Because \(A\) is compact, a positive tail need not obey \(C\geq\delta I\) for any \(\delta>0\). Ordinary inversion of \(C\) is therefore the wrong gate.

## Singular-tail Schur criterion

In finite dimensions, let \(C^\dagger\) denote the Moore--Penrose inverse. Then

\[
A\geq0
\]

if and only if

\[
C\geq0,
\]

\[
B(I-C^\dagger C)=0,
\]

and

\[
F-BC^\dagger B^*\geq0.
\]

The middle equation says that the off-diagonal coupling annihilates \(\ker C\), equivalently

\[
\operatorname{ran}(B^*)
\subseteq
\operatorname{ran}(C).
\]

Without it, coupling into a zero-energy tail direction creates a negative direction regardless of the finite compression.

## Infinite-dimensional form

The stable formulation avoids an unbounded pseudoinverse. Seek a bounded operator \(D\) satisfying

\[
B=DC^{1/2}.
\]

Then

\[
\begin{aligned}
\langle A(x,y),(x,y)\rangle
&=
\langle(F-DD^*)x,x\rangle\\
&\quad+
\lVert C^{1/2}y+D^*x\rVert^2.
\end{aligned}
\]

Consequently,

\[
C\geq0,
\qquad
B=DC^{1/2},

\qquad
F-DD^*\geq0
\]

is a sufficient positivity certificate and is the natural range-compatible Schur condition when zero is in the tail spectrum.

## Application to the local Weil tower

The prior log-elliptic proposal supplies the intended first condition: prove the high-mode tail form \(C_M\) nonnegative after adjoining endpoint representers to the finite trial space.

The remaining tasks are now exact:

1. factor the finite/tail coupling as
   \[
   B_M=D_MC_M^{1/2};
   \]
2. bound or compute \(D_MD_M^*\) on the finite trial space;
3. certify
   \[
   F_M-D_MD_M^*\geq0.
   \]

A norm-only estimate \(\lVert B_M\rVert\to0\) does not establish the range factorization and cannot replace it.

## Deliberate failure

For

\[
C=
\begin{pmatrix}4&0\\0&0\end{pmatrix},

\qquad
F=(1),
\]

the coupling \(B=(2,0)\) satisfies the range condition and gives a positive block with zero Schur complement. Replacing it by \(B=(2,1)\) couples to \(\ker C\); the full matrix is not positive despite unchanged \(F\) and positive \(C\).

## Disposition

The signed-tail gate is refined to two independent obligations: tail nonnegativity and range-compatible off-diagonal factorization. This is the next higher coherencer for each local Sobolev operator. RH remains unproved.

## Verification

- `research/voevodsky/checkers/check_range_compatible_schur_certificate.py`
- `research/voevodsky/results/range_compatible_schur_certificate.json`
