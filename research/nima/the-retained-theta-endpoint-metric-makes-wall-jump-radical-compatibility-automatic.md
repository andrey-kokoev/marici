# The retained theta endpoint metric makes wall--jump radical compatibility automatic

## Radical of a positive graph sum

Let \(G_0\ge0\) and \(G_1\ge0\) be closed positive forms, and let \(K\) be a
form-bounded map. Define

\[
G_\Gamma(x)
=
G_0(x)+G_1(Kx).
\]

Then

\[
\operatorname{rad}G_\Gamma
=
\operatorname{rad}G_0
\cap
K^{-1}(\operatorname{rad}G_1).
\]

Indeed, a sum of two nonnegative numbers vanishes exactly when both terms
vanish.

This identity is stronger than merely showing that \(K\) maps one radical
into another.

## Application to the theta--window graph

For the local wall--jump graph,

\[
G_{\Gamma,p}(y)
=
G_{\theta,p}(y)
+
G_{\mathrm{win},p}(K_py).
\]

The source endpoint metric is \(2I\) on the two reciprocal coordinates. Hence

\[
G_{\theta,p}(y)\ge 2\|y\|^2
\]

in that coordinate normalization, and

\[
\operatorname{rad}G_{\theta,p}=\{0\}.
\]

Therefore

\[
\operatorname{rad}G_{\Gamma,p}
=
\{0\}.
\]

No property of the soft window radical is needed. Retaining the theta endpoint
coordinate removes every wall--jump radical before completion.

## Uniform coercivity

The same estimate gives

\[
G_{\Gamma,p}(y)
\ge
G_{\theta,p}(y)
\ge
2\|y\|^2.
\]

If a different normalized endpoint convention rescales \(2I\) to \(I\), the
lower bound becomes one. In either convention it is independent of \(p\).

The trace-class window term can only increase the graph energy. It cannot
create a new radical or reduce the lower margin.

## Prime completion

On the prime-labelled direct sum,

\[
G_\Gamma
=
\bigoplus_pG_{\Gamma,p}.
\]

Uniform endpoint coercivity yields

\[
G_\Gamma(y)\ge c_\theta\|y\|^2,
\qquad
c_\theta>0.
\]

Thus the completed wall--jump graph has zero radical and closed range. The
trace-class family \(K=\bigoplus_pK_p\) supplies a compact positive
perturbation without affecting this conclusion.

## Extension to full histories

Let \(T:\mathcal H_{\mathrm{hist}}\to E_\theta\) be the endpoint trace. The
first-order Green identity shows that the odd coupling factors through \(T\)
and annihilates

\[
N=\ker T.
\]

Decompose the history problem into:

- the endpoint plane \(E_\theta\), where the retained metric is coercive;
- the zero-trace history space \(N\), where the odd coupling vanishes.

Any remaining radical of the full history form is therefore confined to the
even zero-trace bulk form. It cannot leak into the wall--jump interaction.

If \(N_0\) is that bulk radical, quotienting by \(N_0\) commutes with the odd
boundary graph because

\[
T N_0=0,
\qquad
J N_0=0.
\]

## Correct quotient order

The safe sequence is

\[
\mathcal H_{\mathrm{hist}}
\longrightarrow
\mathcal H_{\mathrm{hist}}/N_0
\longrightarrow
E_\theta\oplus E_{\mathrm{win}}.
\]

Equivalently, one may first split endpoint and zero-trace coordinates using a
bounded trace right inverse, quotient only the zero-trace radical, and then
form the graph.

What is forbidden is quotienting the endpoint plane by the kernel of scalar
theta synthesis. That kernel is unrelated to the Green radical and can erase
the unit or jump coordinate.

## Reciprocal compatibility

Reflection preserves \(G_{\theta,p}\), \(G_{\mathrm{win},p}\), and the graph
of \(K_p\). It diagonalizes the endpoint plane into wall and jump lines.
Because both lines have positive theta energy, neither can enter the radical.

Thus radical reduction cannot identify opposite reciprocal characters in the
retained graph model.

## What remains open

This closes radical compatibility for:

- the local wall--jump plane;
- its prime-labelled completion;
- and its attachment to a history form whose odd part factors through the
  endpoint trace.

It does not prove coercivity of the even zero-trace bulk form. Nor does it
prove that archimedean and reciprocal global attachments preserve the same
split endpoint coordinate.

The next gate is therefore no longer local radical descent. It is the global
attachment theorem:

\[
\text{coercive theta wall--jump graph}
\longrightarrow
\text{reciprocal plus archimedean boundary carrier}
\]

with the endpoint projection retained or transported unitarily.

## Hostiles

Remove \(G_{\theta,p}\) and keep only the compact window covariance. The
completed odd sector can then lose its lower bound.

Quotient by scalar synthesis kernel before forming the graph. This can kill a
nonzero endpoint vector despite positive Green energy.

Allow the odd coupling to act on a zero-trace bulk direction. Then endpoint
radical control no longer determines the full operator; this contradicts the
first-order Green boundary factorization.

## Verdict

The graph radical formula and the positive theta endpoint metric close the
local wall--jump radical gate:

\[
\operatorname{rad}G_{\Gamma,p}=\{0\}.
\]

All residual radical questions lie in the even zero-trace bulk, where the odd
Adams coupling is absent. The next constructor obligation is global
reciprocal--archimedean attachment with preservation of the split endpoint
port.
