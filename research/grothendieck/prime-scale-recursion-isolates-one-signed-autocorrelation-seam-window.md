# Prime-scale recursion isolates one signed autocorrelation seam window

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact source-recursion theorem

## Labelled prime decomposition

Fix a prime (p), put

\[
c=p^{-1/2},
\qquad
L=\log p,
\]

and write the exact theta label recursion on the positive chart as

\[
\Phi(q)=A_p(q)+c\Phi(q+L),
\]

where (A_p=\Phi_{p\nmid}) is the positive primitive-label remainder.

Define the full separation autocorrelation

\[
\rho(d)=2\int_0^\infty\Phi(q)\Phi(q+d)\,dq.
\]

Expanding both factors gives four labelled cells. Introduce

\[
\begin{aligned}
\rho_{AA}(d)&=2\int_0^\infty A_p(q)A_p(q+d)\,dq,\\
\rho_{A,L}(d)&=2\int_0^\infty A_p(q)\Phi(q+d+L)\,dq,\\
\rho_{L,A}(d)&=2\int_0^\infty \Phi(q+L)A_p(q+d)\,dq,
\end{aligned}
\]

and the finite moving-seam window

\[
W_L(d)=2\int_0^L\Phi(q)\Phi(q+d)\,dq.
\]

The shifted self-correlation satisfies

\[
2\int_0^\infty\Phi(q+L)\Phi(q+d+L)\,dq
=\rho(d)-W_L(d).
\]

Therefore

\[
(1-c^2)\rho(d)
=\rho_{AA}(d)
+c\rho_{A,L}(d)
+c\rho_{L,A}(d)
-c^2W_L(d).
\]

## Meaning

The prime recursion has converted a globally positive autocorrelation into
three positive labelled correlations and one negative finite-window term. The
only signed contribution is not fitted: it is the exact boundary lost when
the translated integration interval is returned to the original half-line.

For theta coefficients,

\[
1-c^2=1-p^{-1}>0.
\]

Thus the source-specific distinction from the positive two-cell hostile model
is now explicit. Theta arithmetic repeatedly decomposes the forcing while
carrying a finite moving seam that the unlabelled source does not possess.

## Odd forcing transform

Applying the odd Laplace transform in the separation variable gives the same
identity for the doubled forcing:

\[
(1-p^{-1})\mathcal K
=\mathcal K_{AA}
+p^{-1/2}(\mathcal K_{A,L}+\mathcal K_{L,A})
-p^{-1}\mathcal K_{W_L}.
\]

The window term is the first exact candidate for the modular boundary current
required by the Green identity. The theorem does not yet show that its odd
transform is a derivative in the flow coordinate or that iteration over all
primes cancels the positive correlation terms.

## Sharp next gate

Differentiate the moving-window transform with respect to (L). Its endpoint
variation is source-local. The decisive question is whether prime-labelled
iteration telescopes these variations into the primitive, square, and
archimedean boundary packet.

The route fails if a non-window signed residual survives the expansion, or if
the window transform cannot be typed continuously through restricted-product
completion.

## Verification

The exact checker performs the identity on a finite symbolic labelled source,
including all endpoint truncations. It verifies that the sole negative term is
the moving-seam window and checks the theta coefficient at (p=2).
