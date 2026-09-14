# Multiplicity-valued reciprocal and Real bulk multipliers admit a full block classification

## Question

What replaces the scalar diagonal classification when each radial channel carries an auxiliary Hilbert multiplicity space and the bulk observer may mix the two reciprocal channels?

## Claim boundary

The classification concerns essentially bounded operator-valued multiplication fields on a doubled radial Hilbert space. Equalities hold almost everywhere. A fixed conjugation on the multiplicity space is part of the Real datum. The result classifies reciprocal-even, reciprocal-odd, and fixed-fiber Real covariance; it does not classify arbitrary nonlocal operators in the full commutant.

## Multiplicity-valued radial carrier

Let \(K\) be a complex Hilbert space equipped with a conjugation

\[
\kappa:K\to K,
\qquad
\kappa^2=I.
\]

Set

\[
\mathcal H_K
=
L^2(\mathbb R_+,K)\oplus L^2(\mathbb R_+,K).
\]

For \(u\in U(1)\), define

\[
W_u=
\begin{pmatrix}
0&u^{-1}I_K\\
u I_K&0
\end{pmatrix}.
\]

Let \(\mathsf K\) act fiberwise by \(\kappa\), and define the twisted Real structure

\[
J_u=
\begin{pmatrix}
I_K&0\\
0&u^2I_K
\end{pmatrix}\mathsf K.
\]

Then \(W_u^2=I\), \(J_u^2=I\), and \(J_uW_u=W_uJ_u\).

## General block multiplication observer

Let

\[
\mathcal M(r)=
\begin{pmatrix}
A(r)&C(r)\\
D(r)&B(r)
\end{pmatrix}
\]

be a weakly measurable, essentially bounded field in \(B(K\oplus K)\). It defines the bounded multiplication observer \(M_{\mathcal M}\) on \(\mathcal H_K\).

Write

\[
\overline T=\kappa T\kappa
\]

for the conjugate of an operator on \(K\).

## Reciprocal-even classification

Direct block multiplication gives

\[
M_{\mathcal M}W_u=W_uM_{\mathcal M}
\]

if and only if

\[
B=A,
\qquad
D=u^2C.
\]

Thus every reciprocal-even block multiplier has the form

\[
\mathcal M_+(A,C)=
\begin{pmatrix}
A&C\\
u^2C&A
\end{pmatrix}.
\]

The earlier diagonal family is the subfamily \(C=0\).

## Reciprocal-odd classification

Similarly,

\[
M_{\mathcal M}W_u=-W_uM_{\mathcal M}
\]

if and only if

\[
B=-A,
\qquad
D=-u^2C.
\]

Hence every reciprocal-odd block multiplier has the form

\[
\mathcal M_-(A,C)=
\begin{pmatrix}
A&C\\
-u^2C&-A
\end{pmatrix}.
\]

The earlier diagonal odd family is recovered at \(C=0\).

## Fixed-fiber Real covariance

The condition

\[
M_{\mathcal M}J_u=J_uM_{\mathcal M}
\]

is equivalent to

\[
A=\overline A,
\qquad
B=\overline B,
\qquad
\overline C=u^2C,
\qquad
D=u^2\overline D.
\]

Intersecting with either reciprocal parity gives the same two independent Real conditions:

\[
A=\overline A,
\qquad
\overline C=u^2C.
\]

Therefore the Real reciprocal-even and reciprocal-odd fields are exactly

\[
\mathcal M_+(A,C)=
\begin{pmatrix}
A&C\\
u^2C&A
\end{pmatrix},
\qquad
\mathcal M_-(A,C)=
\begin{pmatrix}
A&C\\
-u^2C&-A
\end{pmatrix},
\]

with \(A\) real relative to \(\kappa\) and \(C\) carrying twisted Real weight \(u^2\).

No self-adjointness is implied. If self-adjoint observer fields are additionally required, then the off-diagonal blocks must satisfy

\[
D=C^*.
\]

For the even family this becomes \(C^*=u^2C\); for the odd family it becomes \(C^*=-u^2C\). Those are additional metric conditions, not consequences of reciprocal or Real covariance.

## Variance versus observation strength

Let

\[
S=\begin{pmatrix}I_K&0\\0&-I_K\end{pmatrix}.
\]

Then

\[
\mathcal M_-(A,C)=S\mathcal M_+(A,C).
\]

Since \(S\) is unitary,

\[
\mathcal M_-^*\mathcal M_-
=
\mathcal M_+^*\mathcal M_+.
\]

Thus even and odd fields built from the same \((A,C)\) have identical pointwise singular values and identical ungraded observation Gramians. Their distinction is entirely reciprocal variance: the even observer preserves the \(W_u\)-eigenspaces, while the odd observer exchanges them.

This extends the scalar conclusion without requiring \(A\) and \(C\) to commute.

## Pointwise coercivity

If there is \(m>0\) such that

\[
\mathcal M(r)^*\mathcal M(r)\ge m^2I_{K\oplus K}
\]

for almost every \(r\), then

\[
\|M_{\mathcal M}f\|\ge m\|f\|.
\]

This supplies a bulk lower bound independently of reciprocal parity. Conversely, if the essential infimum of the smallest fiber singular value is zero, pointwise multiplication is not bounded below on the ambient \(L^2\) rung.

For graph-domain observation by derivative plus multiplier, pointwise coercivity is sufficient but not necessary. A uniformly thick operator-valued field can still control broad packets.

## Uniform operator-valued thickness

A natural sufficient multiplicity-valued analogue is: there exist \(\ell,\beta>0\) such that every interval \(I\subset\mathbb R_+\) of length \(\ell\) satisfies the weak-operator inequality

\[
\int_I\mathcal M(r)^*\mathcal M(r)\,dr
\ge
\beta I_{K\oplus K}.
\]

For constant multiplicity vectors this is the exact uniform local-mass condition. Extending the scalar graph-observability proof to arbitrary \(K\)-valued \(H^1\) functions requires controlling variation of vector direction inside each interval. The Bochner fundamental theorem and the estimate

\[
\|f(r)-f(s)\|
\le
|r-s|^{1/2}\|f'\|_{L^2(I;K)}
\]

provide the same reduction as in the scalar proof, uniformly in the dimension of \(K\). A complete quantified theorem is deferred to the sharper-coercivity objective rather than inferred here.

## Full commutant boundary

The block calculation classifies decomposable multiplication operators. The full operator commutant of \(W_u\) on \(\mathcal H_K\) is larger: after diagonalizing the involution, it consists of arbitrary bounded operators preserving the two eigenspaces. Such operators may be nonlocal in the radial coordinate and need not arise from measurable multiplier fields.

Therefore “full block classification” means full classification inside the \(2\times2\) operator-valued multiplication algebra, not the full commutant in \(B(\mathcal H_K)\).

## Green--Real role assignment

- \(W_u\): reciprocal Green comparison cell;
- \(J_u\): fixed-fiber Real comparison;
- \(M_{\mathcal M_+}\): reciprocal-even bulk observer;
- \(M_{\mathcal M_-}\): reciprocal-odd bulk observer;
- pointwise or thick Gramian test: independent essential-observer gate.

Covariance does not imply coercivity, and coercivity does not imply covariance.

## Deliberate failures

1. Setting only \(A=B\) does not give reciprocal-even covariance when \(D\ne u^2C\).
2. Setting only \(A=-B\) does not give reciprocal-odd covariance when \(D\ne-u^2C\).
3. Real-valued diagonal blocks do not establish Real covariance of an arbitrary off-diagonal block.
4. Equal even/odd Gramians do not identify their reciprocal variance.
5. The multiplier classification does not promote to the full nonlocal commutant.

## Disposition

Multiplicity does not alter the reciprocal parity pattern but introduces a twisted off-diagonal Real sector. Even and odd block multipliers have identical ungraded observation strength while carrying opposite reciprocal variance. The classification is exact for essentially bounded operator-valued multiplication fields. Quantified graph coercivity under operator-valued thickness remains the next analytic gate.
