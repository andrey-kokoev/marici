# The full Sobolev completion is too large for the transported ray connection

## Actual transported derivative

The half-density map satisfies

\[
\mathcal M_n\partial_x
=
n^{-1}e^{-u}
\left(\partial_u-\frac12\right)
\mathcal M_n.
\]

Thus the transported comoving derivative is not the constant translation
generator. Define

\[
T_n
=
n^{-1}e^{-u}
\left(\partial_u-\frac12\right).
\]

The bare theta energy is

\[
S=-\partial_u^2+\frac14.
\]

Although \(S\ge\frac14I\), the operator \(T_n\) is not relatively bounded
with respect to the ordinary \(S\)-form on the full line.

## Translation hostile

Choose a nonzero compactly supported smooth function \(\varphi\) for which

\[
e^{-u}
\left(\varphi'-\frac12\varphi\right)
\neq0.
\]

Translate it toward the negative end:

\[
\varphi_R(u)=\varphi(u+R).
\]

The \(S\)-form is translation invariant, so

\[
\langle\varphi_R,S\varphi_R\rangle
=
\langle\varphi,S\varphi\rangle.
\]

But after writing \(v=u+R\),

\[
\|T_n\varphi_R\|
=
n^{-1}e^R
\left\|
e^{-v}
\left(\varphi'(v)-\frac12\varphi(v)\right)
\right\|.
\]

Therefore

\[
\|T_n\varphi_R\|\to\infty
\qquad
(R\to\infty).
\]

No estimate of the form

\[
\|T_nf\|
\le
C\|S^{1/2}f\|
\]

can hold on the full Sobolev form domain.

## Correction to the spectral-carrier proposal

The quarter-gap remains correct for the bare energy. However, defining the odd
carrier only as a reducing spectral subspace of \(S\) can enlarge it beyond
the source asymptotic class on which the comoving derivative is meaningful.

The Adams comparison needs a joint graph domain for \(S\) and \(T_n\), not
merely the spectral domain of \(S\).

## Why the source Gaussian core survives

For

\[
f_j(x)=x^je^{-\pi x^2},
\]

the transported half-density behaves as \(u\to-\infty\) like

\[
\mathcal M_nf_j(u)
\sim
n^{j+1/2}e^{(j+1/2)u}.
\]

For odd \(j\ge1\), multiplication by \(e^{-u}\) still leaves decay at
least \(e^{u/2}\). Thus the source odd Gaussian-polynomial core lies in the
domain of \(T_n\).

The problem arises only when completion admits arbitrary left-translated
Sobolev packets that no longer retain this source vanishing order.

## Correct joint topology

A natural graph norm is

\[
\|f\|_{\mathrm{joint}}^2
=
\|S^{1/2}f\|^2
+
\|e^{-u}(\partial_u-\tfrac12)f\|^2.
\]

Equivalently, in the ray coordinate this retains control of
\(\partial_x f\) together with the dilation-completion energy.

The required completion is the closure of the source Gaussian cyclic core in
this joint norm, or a stronger source-authorized rigging. It must not be
replaced by the full \(H^1(\mathbb R)\) completion.

## Prime-label scaling

The explicit prefactor \(n^{-1}\) is favorable for large theta labels, but
it does not repair the left-end unboundedness for any fixed \(n\).
Uniformity over labels becomes available only after the joint domain is
frozen.

## Revised auxiliary gate

The causal-history contraction must be proved on the joint completed carrier:

\[
\mathcal K_{\mathrm{odd}}^{\mathrm{joint}}
=
\overline{
\operatorname{span}\{P^kg_{\mathrm{odd}}\}
}^{\|\cdot\|_{\mathrm{joint}}}.
\]

Then one must determine whether the represented odd history is bounded as a
form relative to \(S\) on that smaller carrier.

## Hostile

Prove the quarter-gap on \(H^1(\mathbb R)\), close the Gaussian core only in
that norm, and then apply \(T_n\). The translated packets above belong to
the completion and make the connection graph discontinuous.

## Frontier

The source now dictates a two-operator completion:

\[
\text{theta energy }S
+
\text{comoving derivative graph }T_n.
\]

The next theorem is closability and prime-uniform control of this joint graph,
followed by the causal-minus-anticausal relative contraction on its range.
