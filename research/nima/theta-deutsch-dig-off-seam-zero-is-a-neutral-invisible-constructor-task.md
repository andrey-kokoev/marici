# Deutsch dig: an off-seam zero is a neutral invisible constructor task

## Status

Exact finite energy identity, explicit hostile, and completion formulation. The
ordered-port repair and Krein symmetrizer criterion allow Deutsch's question to
be stated as a constructor task rather than as a zero-location assertion.

In the coordinate where the critical seam is the real spectral axis, an
off-seam transmission zero must construct a nonzero state that is:

- reachable from the endpoint actuator;
- invisible to the theta-source sensor;
- neutral in the modular state metric;
- and stable under arithmetic transport and completion.

The first three properties are forced by a two-line energy identity. The
fourth is the remaining source problem.

## Move one: zero becomes a zero-dynamics state

Fix the framed bordered pencil

\[
L(z)
=
\begin{pmatrix}
0&c^*\\
b&A-zI
\end{pmatrix},
\qquad
A=A^*.
\]

Suppose \(z\) is off the carrier spectrum and the transmission transfer

\[
F(z)=c^*(A-zI)^{-1}b
\]

vanishes. Then the nonzero kernel vector of the bordered pencil can be scaled
to

\[
\begin{pmatrix}
1\\x
\end{pmatrix},
\]

where

\[
(A-zI)x=-b,
\qquad
c^*x=0.
\]

Thus a transmission zero is an internally nonzero state produced by the
endpoint input while remaining invisible at the source output.

This is the exact constructor task. No zero inspection is needed once the
state equations are written.

## Move two: modular symmetrization forces neutrality

Assume the source supplies a Hermitian invertible state metric \(K\) and a real
nonzero scale \(\alpha\) satisfying

\[
AK=KA,
\qquad
Kb=\alpha c.
\]

Multiply the zero-dynamics equation by the \(K\)-pairing with \(x\):

\[
\langle x,K(A-zI)x\rangle
=
-\langle x,Kb\rangle.
\]

Because \(KA\) is Hermitian and \(Kb=\alpha c\), taking imaginary parts gives

\[
-\operatorname{Im}(z)
\langle x,Kx\rangle
=
0.
\]

For an off-seam point,

\[
\operatorname{Im}(z)\ne0,
\]

so every off-seam zero state must satisfy

\[
\langle x,Kx\rangle=0.
\]

The state is Krein-neutral.

## Move three: the impossible task is charge neutralization

If \(K\) is positive or negative definite on every nonzero endpoint-reachable
state, the task is impossible. No nonzero reachable state can have zero
\(K\)-charge, and therefore no off-seam transmission zero exists.

More generally, it is enough to prove a source-derived definite-type bound on
the admissible zero-dynamics class:

\[
\left|
\langle x,Kx\rangle
\right|
\geq
\kappa\lVert x\rVert^2,
\qquad
\kappa>0.
\]

This need not hold on the full state space. It must hold only on states that
can be constructed from the ordered endpoint input and survive every declared
source constraint.

Deutsch's question therefore becomes:

> Which prime-generated operation prevents an endpoint-reachable state from
> neutralizing its modular charge while remaining invisible to the theta
> source?

This is narrower than global coercivity and stronger than reciprocal symmetry.

## Exact three-state hostile

Indefinite modular symmetry alone permits the forbidden task. Take

\[
A
=
\operatorname{diag}(-1,0,1),
\qquad
K
=
\operatorname{diag}(1,-1,1),
\]

and

\[
b
=
\begin{pmatrix}
1\\1\\1
\end{pmatrix},
\qquad
c
=
Kb
=
\begin{pmatrix}
1\\-1\\1
\end{pmatrix}.
\]

Then \(AK=KA\) and the bordered pencil is \(J\)-selfadjoint with the induced
block metric. The transfer is

\[
F(z)
=
\frac{1}{-1-z}
-
\frac{1}{-z}
+
\frac{1}{1-z}.
\]

After combining denominators, its numerator is proportional to

\[
z^2+1.
\]

Therefore

\[
F(i)=F(-i)=0.
\]

The system is framed, the carrier is selfadjoint, the port metric is exact,
and the zeros still leave the seam. The associated zero-dynamics states are
\(K\)-neutral.

This is the minimal concrete hostile to the claim that the repaired modular
metric alone proves confinement.

## Move four: completion version

A completed transmission zero may appear without any finite cutoff having an
exact zero. The relevant hostile is a normalized family \(x_X\) satisfying

\[
\left\|
(A_X-zI)x_X+b_X
\right\|
\longrightarrow0,
\]

\[
c_X^*x_X
\longrightarrow0,
\]

and

\[
\lVert x_X\rVert=1.
\]

The same energy identity forces

\[
\langle x_X,K_Xx_X\rangle
\longrightarrow0
\]

for fixed off-seam \(z\), provided the residual pairings remain controlled.

Thus completion can create a zero only by producing an asymptotically neutral,
source-invisible reachable state. This reconnects the framed control problem
to the earlier no-escape and completion-at-infinity programme.

## Move five: source-local sufficient theorem

The smallest sufficient theorem is now explicit. For every compact off-seam
spectral region, prove a cutoff-independent constant \(\kappa>0\) such that

\[
\left|
\langle x,K_Xx\rangle
\right|
\geq
\kappa\lVert x\rVert^2
\]

for every normalized state satisfying the authorized endpoint-reachability,
boundary, residue, and transport constraints.

Then no exact or completion-generated off-seam zero state can exist.

The bound must be derived from:

- positive primitive and prime-power grammar;
- modular transport;
- the ordered endpoint/source incidence;
- retained seam and archimedean currents;
- and the completion topology.

It cannot be assumed as Herglotz positivity or fitted after examining zeros.

## Finite falsifier

At any finite cutoff, form the constrained reachable class and restrict the
metric \(K_X\) to it. A nonzero vector satisfying

\[
c_X^*x=0,
\qquad
\langle x,K_Xx\rangle=0
\]

and the zero-dynamics incidence is a complete falsifier.

Before solving the spectral equation, an even cheaper warning is a mixed-sign
restriction of \(K_X\) to the endpoint Krylov space. Mixed signature does not
prove an off-seam zero, but it proves that definiteness cannot be the source
mechanism without additional constraints.

## Decisive conclusion

The constructor-theoretic content is no longer vague. An off-seam zero is a
successful construction of neutral invisible memory from the endpoint port.
The modular metric turns displacement from the seam into a neutrality
requirement. RH would follow from a source theorem forbidding such neutral
states uniformly through completion.

The next calculation is not another generic rotation. It is the signature of
the modularly induced metric on the actual endpoint-reachable, source-invisible
theta state class.
