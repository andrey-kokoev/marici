# The theta Volterra history is a shift-semigroup functional, not a first-order resolvent

## Exact realization

The authorized causal history is

\[
(H^*g)(q)
=
\int_0^q\Phi(q-t)g(t)\,dt.
\]

Let \((R_u)_{u\ge0}\) be the right-shift semigroup on the half-line,

\[
(R_ug)(q)
=
\begin{cases}
g(q-u),&q\ge u,\\
0,&q<u.
\end{cases}
\]

Then, exactly,

\[
H^*
=
\int_0^\infty\Phi(u)R_u\,du.
\]

Its adjoint is the anti-causal history

\[
H
=
\int_0^\infty\Phi(u)R_u^*\,du,
\]

because

\[
(R_u^*c)(t)=c(t+u).
\]

Thus the theta history is a source-weighted semigroup functional of the minimal shift generator. It is not itself the resolvent of a first-order differential operator.

## Generator

The generator of \(R_u\) is

\[
A=-\partial_q
\]

on the half-line Sobolev domain with zero incoming trace,

\[
\operatorname{dom}A
=
\{g\in H^1(0,\infty):g(0)=0\}.
\]

Its adjoint is

\[
A^*=\partial_q
\]

on the maximal \(H^1\) domain. The Green identity is

\[
\langle Ag,c\rangle
-
\langle g,A^*c\rangle
=
g(0)\overline{c(0)}
\]

up to the fixed inner-product and sign convention. The minimal-domain value vanishes, while the maximal pair exposes the one incoming boundary coordinate.

The semigroup formula can therefore be written as a Hille--Phillips functional calculus:

\[
H^*=\widehat\Phi(-A)
\]

with notation adjusted to the chosen Laplace-transform convention.

## Correction to the reference-extension proposal

A generic theta kernel \(\Phi\) is not exponential. Hence the Volterra convolution cannot equal one resolvent

\[
(\lambda-A)^{-1}
\]

unless its kernel has the corresponding exponential form.

Therefore the required comparison theorem is not

\[
\text{one boundary extension}
\Longrightarrow
H.
\]

It is

\[
\text{minimal shift generator}
\Longrightarrow
\text{source theta semigroup functional}
\Longrightarrow
H,H^*
\Longrightarrow
\mathscr D_H.
\]

The first-order generator supplies causality, endpoint incidence, and the boundary port. The theta density supplies the distributed propagation law.

## Laplace multiplier

On the Hardy--Laplace representation, the causal history has multiplier

\[
m_\Phi(z)
=
\int_0^\infty\Phi(u)e^{-zu}\,du.
\]

Thus all theta memory is retained in one analytic transfer function. A scalar boundary channel can couple to an infinite-dimensional shift reservoir because repeated semigroup propagation exposes the whole kernel.

This is the correct realization-theoretic explanation for how fixed boundary rank can coexist with infinite prime or theta memory.

It does not imply minimality. The cyclicity of the boundary input must still be proved for the source-weighted functional.

## Reciprocal conservative double

The one-sided shift generator is maximal dissipative rather than selfadjoint. Its reciprocal completion pairs it with the adjoint orientation. The natural conservative block is built from

\[
A
\quad\text{and}\quad
A^*,
\]

while the bounded history Dirac is built from

\[
H=\widehat\Phi(-A)^*
\quad\text{and}\quad
H^*=\widehat\Phi(-A).
\]

These are two levels of one system:

1. generator level: boundary extension and Weyl theory;
2. theta-filtered level: bounded causal history and Green loading.

The already selfadjoint \(\mathscr D_H\) is the filtered conservative observable. The nontrivial boundary relation must be attached upstream to the reciprocal shift generator.

## Boundary-rank consequence

The scalar half-line shift has one incoming boundary port. Reciprocal doubling balances the two orientations, but the exact ordinary-boundary-triple rank depends on the doubled symmetric restriction and cannot be read off from the four coefficient characters.

The rank audit must therefore begin from the doubled derivative domains, then compute the map

\[
\mathcal W
\longrightarrow
\mathcal B_{\mathrm{shift}}
\]

from the four-character coefficient packet into the reachable generator boundary space.

Any coefficient direction in the kernel remains an exterior observer coordinate, not an extension parameter.

## Weyl return after theta filtering

The source return should be assembled in the order

\[
\mathcal B_{\mathrm{shift}}
\xrightarrow{\gamma_A(z)}
\text{shift defect state}
\xrightarrow{\widehat\Phi(-A)}
\text{theta-filtered history state}
\xrightarrow{\Gamma_1}
\mathcal B_{\mathrm{shift}}.
\]

Accordingly, the candidate return is a filtered Weyl or transfer function, not the bare Weyl function of \(A\).

This distinction matters: replacing the theta filter by an arbitrary analytic multiplier could fit any desired determinant. The multiplier must be the independently fixed Laplace transform of the source theta density.

## Minimality test

For the semigroup realization, the controllable cyclic space is

\[
\mathcal C
=
\overline{\operatorname{span}}
\{R_u b:u\ge0\},
\]

where \(b\) is the source-authorized boundary incidence, interpreted in the extrapolation space when it is distributional.

The observable dark space is

\[
\mathcal N
=
\bigcap_{u\ge0}
\ker\bigl(b^*R_u^*\widehat\Phi(-A)\bigr).
\]

The realization is minimal on the declared support only if

\[
\mathcal C=H_{\mathrm{shift}},
\qquad
\mathcal N=\{0\}.
\]

In Hardy form this becomes an outer-factor question for the source transfer multiplier and the boundary incidence.

## Exact next theorem

The next source-native theorem is:

> Prove that the theta Laplace multiplier and the reciprocal boundary incidence form a minimal conservative realization of the completed history packet.

Its finite and analytic gates are:

1. close the right-shift generator on the declared weighted rigging;
2. construct its reciprocal conservative double;
3. prove the semigroup integral equals the authorized \(H^*\) and \(H\);
4. compute the doubled deficiency or boundary-relation rank;
5. derive the coefficient-to-shift-boundary incidence;
6. prove cyclic controllability and observability, equivalently the needed outer-factor property;
7. form the filtered Weyl return;
8. only then compare its determinant section with \(\Xi\).

## Hostiles

A single exponential resolvent can reproduce one decay scale but not the full theta kernel.

An arbitrary analytic transfer multiplier can reproduce the scalar zeta section while lacking theta authority.

A theta multiplier with a nontrivial inner factor can preserve boundary norms yet leave an unobservable invariant subspace.

A reciprocal double may balance formal deficiency counts while its coefficient incidence reaches only one boundary polarization.

## Frontier

The operator architecture has now become source-specific:

\[
\text{reciprocal shift boundary system}
\to
\text{theta Laplace filter}
\to
\text{causal/anti-causal history pair}
\to
\text{selfadjoint history Dirac}
\to
\text{filtered boundary pencil}.
\]

The outer/minimality theorem for the theta transfer function is the next irreducible analytic gate.
