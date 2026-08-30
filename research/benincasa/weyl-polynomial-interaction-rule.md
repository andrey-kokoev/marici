# Polynomial Weyl interactions obey one arity-uniform quantum rule

For

\[
H_{\rm int}=\frac{q^d}{d},
\]

the primitive relation is

\[
Dp=-q^{d-1}.
\]

Normal ordering gives the uniform formula

\[
D(p^m)
=
\sum_{k=1}^{\min(m,d)}
(-i)^{k+1}\hbar^{k-1}
\frac{k!}{d}
\binom mk\binom dk
q^{d-k}p^{m-k}.
\]

The \(k=1\) term is the classical force contribution \(-m q^{d-1}p^{m-1}\). The first term containing neither \(q\) nor \(p\) occurs at \(m=d,k=d\), with coefficient magnitude

\[
\boxed{(d-1)!\,\hbar^{d-1}.}
\]

All interaction degrees use the same binomial/normal-order rule.

In the homogenized Weyl coalgebra, define

\[
\Theta_D=\Delta D-(D\otimes1+1\otimes D)\Delta.
\]

This is the co-Hochschild coboundary of \(D\). Since \(\Delta\) is coassociative and well typed before fixed-\(\hbar\) specialization, the next coboundary vanishes identically. Normal ordering changes the coefficients of \(\Theta_D\), but cannot create an independent ternary obstruction.

Thus Entry 1660 is not an accidental cubic cancellation: it is the first explicit instance of an arity-uniform quantum coherence theorem.
