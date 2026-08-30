# Trace preservation derives the Weyl contact but not all quantum counterterms

Consider the ordering family

\[
H_a=q^2p+a\,i\hbar q.
\]

Using

\[
(q^2p)^\dagger=pq^2=q^2p-2i\hbar q,
\]

one finds

\[
H_a^\dagger=q^2p-(2+a)i\hbar q.
\]

Hermiticity requires

\[
a=-(2+a),
\qquad
\boxed{a=-1.}
\]

Thus the required ordering contact is

\[
\boxed{
H_W=q^2p-i\hbar q=qpq.
}
\]

For a non-Hermitian choice, the first-order evolution has trace defect proportional to

\[
-i\langle H_a-H_a^\dagger\rangle
=
2(a+1)\hbar\langle q\rangle.
\]

Hence trace preservation/positivity rejects every \(a\ne-1\).

This criterion does not fix the residual family

\[
H_W+\lambda\hbar q,
\qquad \lambda\in\mathbb R,
\]

because those additions remain Hermitian. Positivity derives the contact required to repair a chosen monomial ordering, but independent source or renormalization data is still needed to select finite Hermitian quantum counterterms.
