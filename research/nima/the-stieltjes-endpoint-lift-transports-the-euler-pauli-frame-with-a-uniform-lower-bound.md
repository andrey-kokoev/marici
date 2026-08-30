# The Stieltjes endpoint lift transports the Euler Pauli frame with a uniform lower bound

## Result

On the strict primitive-square endpoint plane, the source Stieltjes window lift transports the normalized two-port Euler Pauli frame into the reduced cyclic Green space with a prime-uniform lower bound.

This closes arithmetic observability for the cyclic Stieltjes endpoint cell. It does not yet identify that cell with the complete enlarged Adams Green block.

## Source endpoint lift

Let

\[
E_{12}=\operatorname{span}\{e_1,e_2\}
\]

and, for \\(L=\log p\\), define

\[
J_p e_1=W_L,
\qquad
J_p e_2=W_{2L}
\]

in the source Stieltjes Hilbert space \\(L^2(\nu)\\), after its natural almost-everywhere quotient.

The exact window-history theorem gives:

- source-derived endpoint incidence;
- prime and cutoff naturality;
- the polarized Green/Stokes identity;
- reciprocal orientation;
- and uniform endpoint bounds

\[
m_\nu^2
\le \|W_L\|_\nu^2
\le \|W_{2L}\|_\nu^2
\le 1.
\]

In particular, neither endpoint lies in the cyclic Green radical.

## Two-port lift

Let

\[
X=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad
Y=
\begin{pmatrix}
0&i\\
-i&0
\end{pmatrix}
\]

be the normalized first-jet and central-current Euler ports on \\(E_{12}\\), up to the frozen orientation convention.

Define the typed lifted observer

\[
\mathcal O_pv
=
\begin{pmatrix}
J_pXv\\
J_pYv
\end{pmatrix}.
\]

Write

\[
A_p=J_p^*J_p
=
\begin{pmatrix}
a_p&z_p\\
\overline z_p&b_p
\end{pmatrix},
\]

where

\[
a_p=\|W_L\|_\nu^2,
\qquad
b_p=\|W_{2L}\|_\nu^2.
\]

The Pauli twirl identity gives

\[
\mathcal O_p^*\mathcal O_p
=
XA_pX+YA_pY
=
2
\begin{pmatrix}
b_p&0\\
0&a_p
\end{pmatrix}.
\]

Hence the endpoint cross-correlation \\(z_p\\) cancels exactly.

## Uniform coercivity

Using the source endpoint bounds,

\[
2m_\nu^2 I
\le
\mathcal O_p^*\mathcal O_p
\le
2I.
\]

Therefore, for every prime and every \\(v\in E_{12}\\),

\[
\sqrt2,m_\nu\|v\|
\le
\|\mathcal O_pv\|
\le
\sqrt2\|v\|.
\]

The direct sum over primes has the same bounds. Thus the cyclic Stieltjes endpoint realization preserves the essential two-port arithmetic frame uniformly over primes and cutoffs.

## What this closes

The theorem proves, on the strict cyclic endpoint cell:

1. source-derived primitive and square lifts;
2. radical descent;
3. exact Green/Stokes compatibility;
4. uniform endpoint norms;
5. preservation of the two typed Euler ports;
6. immunity of the arithmetic lower bound to endpoint cross-correlation;
7. a prime-uniform arithmetic margin \\(\sqrt2,m_\nu\\).

No endpoint-angle or triangular-shear estimate is needed for this particular lower bound.

## Remaining extension gate

The complete Adams auxiliary space also contains wall, causal-history, tail/PV, and reciprocal sectors. To promote this cyclic theorem to G1 and global \\(\delta_P\\), one must prove that the complete enlarged Green block:

- restricts to the Stieltjes form on the cyclic endpoint subspace;
- preserves its reduced embedding;
- does not kill either endpoint through a larger radical;
- keeps the two Pauli outputs typed until the global evaluator;
- and couples the additional sectors without changing the boundary identity.

Thus the first-edge frontier is no longer construction of endpoint lifts or their arithmetic lower estimate. It is the extension/intertwining theorem from the cyclic Stieltjes cell into the complete enlarged Adams Green system.

## Evidence combined

- `research/nima/the-front-stieltjes-window-history-obeys-an-exact-polarized-green-identity.md`
- `research/nima/the-two-port-pauli-frame-cancels-endpoint-cross-correlation-under-any-common-green-lift.md`
- `research/nima/the-strict-primitive-square-compression-of-the-two-euler-ports-is-an-exact-pauli-frame.md`
