# The explicit cross-storage is contractive but cannot by itself make the doubled system passive

## Cross equation versus full KYP equation

The characteristic kernel solves the off-diagonal equation

\[
A_-^*K+KA_+=Q_{-+}.
\]

Numerically, the resulting operator is small and appears contractive. This closes only the cross block of the doubled KYP equation.

The diagonal blocks must be audited separately.

## Original diagonal Green supply

Put

\[
G_+
=
B^*B-C^*C.
\]

The oppositely oriented sheet has

\[
G_-=-G_+.
\]

Thus diagonal storage contributes

\[
\begin{pmatrix}
G_+&0\\
0&-G_+
\end{pmatrix}.
\]

## Clark diagonal supply

Let

\[
S
=
\frac12
\left(
\ell_0^*\ell_1+
\ell_1^*\ell_0
\right).
\]

The Clark supply has diagonal blocks

\[
Q_{++}=-S,
\qquad
Q_{--}=S.
\]

After the cross block is matched by \(K\), the unmatched diagonal residual is therefore

\[
\begin{pmatrix}
T&0\\
0&-T
\end{pmatrix},
\qquad
T=G_++S.
\]

## Sign obstruction

An operator of the form

\[
\operatorname{diag}(T,-T)
\]

cannot be positive or negative semidefinite unless

\[
T=0.
\]

Here \(T\ne0\). The distributed term \(C^*C\) is infinite-rank multiplication by

\[
-
\frac{\Phi'}{\Phi},
\]

whereas \(B^*B\) and \(S\) are boundary or finite-rank moment terms. They cannot cancel identically.

Consequently, no choice of the off-diagonal block \(K\) alone can convert the full doubled system with diagonal blocks \(I,I\) into a Hilbert-passive Clark realization.

## Meaning of the small norm

The numerical estimate

\[
\|K\|\approx0.00244914
\]

still has value. It indicates that the rank-two Clark gyrator admits a benign bounded storage correction. But that correction addresses only cross-sheet coupling; it does not remove the opposite distributed signatures.

## Required next construction

One must additionally perform one of the following:

1. compress to a source-defined matching subspace on which the two copies of \(T\) cancel;
2. replace the diagonal storages by nonidentical operators \(P_+,P_-\) satisfying their own Lyapunov equations;
3. quotient a maximal neutral boundary relation before asking for Hilbert passivity.

The first and third descriptions are equivalent to the previously identified positive boundary quotient.

## Control-theoretic conclusion

The doubled transport is fundamentally a lossless Krein colligation. A small contractive feedback block does not turn an indefinite colligation into a passive Hilbert colligation when equal and opposite distributed supply channels remain freely accessible.

The missing operation is therefore a physical-state admission or compression, not merely completion of the storage matrix.

## Disposition

The explicit characteristic kernel is a valid solution of the cross Sylvester problem, but it is not the universal positive filler. The full KYP audit proves that off-diagonal storage alone is structurally insufficient.
