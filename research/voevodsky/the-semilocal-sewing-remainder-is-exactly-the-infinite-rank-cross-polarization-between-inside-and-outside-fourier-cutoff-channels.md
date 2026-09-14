# The semilocal sewing remainder is exactly the infinite-rank cross polarization between inside and outside Fourier-cutoff channels

## Setup

Write

\[
P=P_\Lambda,
\qquad
Q=\widehat P_\Lambda=FP_\Lambda F^{-1},
\qquad
A=U_S(g).
\]

For the convolution square `h=g*g*`, one has

\[
U_S(h)=AA^*.
\]

Connes's semilocal trace uses

\[
\operatorname{Tr}(PQA A^*).
\]

The positive triple-compression comparison is

\[
\operatorname{Tr}(PQPAA^*)
=
\|QPA\|_{HS}^2.
\]

The sewing remainder is

\[
\mathcal E_{\Lambda,S}(g)
=
\operatorname{Tr}
\left(PQ(I-P)AA^*\right).
\]

## Exact Hilbert--Schmidt polarization

Assuming the cutoff products are Hilbert--Schmidt in the required order, cyclicity gives

\[
\begin{aligned}
\mathcal E_{\Lambda,S}(g)
&=
\operatorname{Tr}
\left(A^*PQ(I-P)A\right)\\
&=
\operatorname{Tr}
\left((QPA)^*Q(I-P)A\right).
\end{aligned}
\]

Define

\[
B_{\Lambda,S}(g)=QPA,
\qquad
C_{\Lambda,S}(g)=Q(I-P)A.
\]

Then

\[
\boxed{
\mathcal E_{\Lambda,S}(g)
=
\langle
B_{\Lambda,S}(g),
C_{\Lambda,S}(g)
\rangle_{HS}.
}
\]

Thus the remainder is exactly the cross polarization between the Fourier-cutoff images of the inside and outside physical channels.

## Product trace decomposition

Since

\[
A=PA+(I-P)A,
\]

one has

\[
\boxed{
\operatorname{Tr}(PQAA^*)
=
\|B_{\Lambda,S}(g)\|_{HS}^2
+
\langle B_{\Lambda,S}(g),
C_{\Lambda,S}(g)\rangle_{HS}.
}
\]

The first term is positive. The second has no fixed sign and need not be real without the source symmetry assumptions on `g`.

If the semilocal observer is inversion-symmetric so that the total trace is real, the relevant remainder is its real part.

## Full positive square

The larger positive operator `QAA*Q` has trace

\[
\|QA\|_{HS}^2
=
\|B+C\|_{HS}^2.
\]

Expanding gives

\[
\boxed{
\|QA\|_{HS}^2
=
\|B\|_{HS}^2
+
\|C\|_{HS}^2
+
2\operatorname{Re}
\mathcal E_{\Lambda,S}(g).
}
\]

Therefore

\[
\operatorname{Re}
\mathcal E_{\Lambda,S}(g)
=
\frac12
\left(
\|QA\|_{HS}^2
-
\|B\|_{HS}^2
-
\|C\|_{HS}^2
\right).
\]

The sewing term is a difference of three positive quantities, or equivalently one off-diagonal Gram entry. It is not itself a norm square.

## Sharp Cauchy bound

The Hilbert--Schmidt pairing gives

\[
\boxed{
|\mathcal E_{\Lambda,S}(g)|
\le
\|B_{\Lambda,S}(g)\|_{HS}
\|C_{\Lambda,S}(g)\|_{HS}.
}
\]

For every `eta>0`,

\[
2|\operatorname{Re}\mathcal E|
\le
\eta\|B\|_{HS}^2
+
\eta^{-1}
\|C\|_{HS}^2.
\]

This estimate is insufficient for exact Weil positivity unless the outside channel `C` is controlled by the same source bulk with the sharp contraction constant required by the endpoint correction.

## Commutator form

The off-diagonal cutoff block is

\[
PQ(I-P)
=
P[P,Q](I-P).
\]

Hence

\[
\boxed{
\mathcal E_{\Lambda,S}(g)
=
\operatorname{Tr}
\left(
P[P,Q](I-P)AA^*
\right).
}
\]

The remainder is therefore a cutoff commutator/sewing anomaly. It vanishes only if the physical and Fourier cutoffs commute or if the observer does not couple their off-diagonal sectors.

Neither condition holds in the prolate/Sonin problem.

## Rank audit

Both `P` and `Q` have infinite-dimensional range. Their off-diagonal block

\[
PQ(I-P)
\]

is generally compact after finite-window regularization but infinite-rank. In the archimedean prolate problem its singular values are governed by the transition region of the time--band limiting operator.

Once finite places are active, `A=U_S(g)` includes all semilocal scaling translations. Consequently `C=Q(I-P)A` contains infinitely many translated outside-to-inside channels. The remainder cannot be reduced to rank two before a nontrivial source cancellation.

## Singular-value decomposition

Let

\[
PQ(I-P)
=
\sum_{n\ge1}
\sigma_n
|u_n\rangle\langle v_n|
\]

be its singular-value expansion. Then

\[
\mathcal E_{\Lambda,S}(g)
=
\sum_n
\sigma_n
\langle
A^*u_n,
A^*v_n
\rangle.
\]

This displays the deterministic coupling across all prolate transition modes. Replacing the remainder by one endpoint scalar discards every singular channel except one.

The Connes--Consani archimedean theorem proves that, on its restricted support window, the hostile contribution can nevertheless be controlled by one Mellin evaluation. Such a collapse is a theorem about the observer subspace, not a rank statement about `PQ(I-P)` itself.

## Finite-part decomposition

Connes's theorem gives

\[
\operatorname{Tr}(PQAA^*)
=
2\|g\|^2\log\Lambda
+
W_S(g*g^*)
+
o(1).
\]

Using the exact polarization,

\[
W_S(g*g^*)
=
\operatorname*{FP}_{\Lambda\to\infty}
\left[
\|B_{\Lambda,S}(g)\|_{HS}^2
+
\langle B_{\Lambda,S}(g),
C_{\Lambda,S}(g)\rangle_{HS}

\right].
\]

The finite-part operation subtracts the common divergence `2||g||^2 log Lambda`. To compare with a positive bulk, one must know how this divergence is distributed between `||B||^2` and the cross term; subtracting it from the total does not determine either finite part separately.

## A correctly typed two-by-two Gram block

The pair `(B,C)` defines the positive Gram matrix

\[
\boxed{
\mathcal G_{\Lambda,S}(g)
=
\begin{pmatrix}
\|B\|_{HS}^2&
\langle B,C\rangle_{HS}\\
\langle C,B\rangle_{HS}&
\|C\|_{HS}^2
\end{pmatrix}
\succeq0.
}
\]

The semilocal trace observes the first diagonal entry plus one off-diagonal entry. The full positive square observes the sum of all four entries.

Therefore the precise rung-four sewing problem is to find a source-derived boundary condition or contraction identifying the missing conjugate and outside-square entries with the endpoint--gamma completion.

## Transition under adding a prime

When `S` is enlarged, the cutoffs `P,Q` retain their geometric definitions on the enlarged semilocal space, while `A=U_S(g)` changes through the common scaling representation. Both `B` and `C` therefore change coherently:

\[
B_{S\cup\{p\}}=Q_{S\cup\{p\}}
P_{S\cup\{p\}}A_{S\cup\{p\}},
\]

\[
C_{S\cup\{p\}}=Q_{S\cup\{p\}}
(I-P_{S\cup\{p\}})A_{S\cup\{p\}}.
\]

There is no independent prime remainder. Prime dependence occurs inside both legs of the same Hilbert--Schmidt Gram block.

## Disposition

The sewing remainder has now been identified exactly:

\[
\boxed{
\mathcal E_{\Lambda,S}(g)
=
\langle
Q_\Lambda P_\Lambda U_S(g),
Q_\Lambda(I-P_\Lambda)U_S(g)
\rangle_{HS}.
}
\]

It is infinite-rank, sign-indefinite, and is the off-diagonal entry of a positive `2x2` Gram matrix. The next required calculation is a correlated finite-part asymptotic for all four Gram entries, not merely the trace combination supplied by Theorem 4.
