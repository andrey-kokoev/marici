# A rank-one source channel repairs the tail only inside a sharp incidence cone

## Exact two-dimensional classifier

Work in the eigenbasis of the reciprocal tail Hamiltonian:

\[
H_{\mathrm{tail}}
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

Let a direct positive source channel contribute

\[
\alpha vv^{*},
\qquad
\alpha>0,
\qquad
v=
\binom{\cos\theta}{\sin\theta}.
\]

The loaded Hamiltonian is

\[
H_{\alpha,\theta}
=
\begin{pmatrix}
1+\alpha\cos^{2}\theta&
\alpha\sin\theta\cos\theta\\
\alpha\sin\theta\cos\theta&
-1+\alpha\sin^{2}\theta
\end{pmatrix}.
\]

Its trace and determinant are

\[
\operatorname{tr}H_{\alpha,\theta}=\alpha,
\]

\[
\det H_{\alpha,\theta}
=
-1+\alpha(\sin^{2}\theta-\cos^{2}\theta).
\]

Therefore positive semidefiniteness is possible exactly when

\[
\sin^{2}\theta>\cos^{2}\theta
\]

and

\[
\alpha
\ge
\frac{1}
{\sin^{2}\theta-\cos^{2}\theta}.
\]

Strict positivity requires strict inequality in the strength bound.

## Interpretation

A positive rank-one channel repairs the reciprocal tail only when its incidence vector has greater squared overlap with the negative tail eigenline than with the positive eigenline. Merely having a nonzero negative-mode component is insufficient.

The admissible incidence directions form an open cone around the negative eigenline. At the cone boundary,

\[
\sin^{2}\theta=\cos^{2}\theta,
\]

no finite loading strength can repair the determinant. As the incidence approaches this boundary from inside, the required strength diverges.

The perfectly aligned case gives the earlier threshold:

\[
v=v_-,
\qquad
\alpha\ge1.
\]

## Completion margin

Define the directional surplus

\[
\eta_v
=
|\langle v,v_-\rangle|^{2}
-
|\langle v,v_+\rangle|^{2}.
\]

Then the determinant condition is

\[
\alpha\eta_v\ge1.
\]

A completion-stable repair needs both a uniform angular margin and a uniform loading margin:

\[
\inf\eta_v>0,
\qquad
\inf(\alpha\eta_v-1)>0
\]

in the source-normalized frame.

These are not independent if the source fixes \(\alpha\) and \(v\) through one exact Gram identity, but they cannot be replaced by a scalar energy lower bound alone.

## Source consequence

The next source calculation should project each wall, square, and archimedean spectral-incidence vector onto the reciprocal tail eigenlines. This immediately classifies it as:

- repairing;
- critical;
- misaligned but potentially jointly repairing with another channel;
- incapable of rank-one repair.

Multiple individually insufficient channels may jointly repair the tail through their frame operator

\[
R=\sum_j\alpha_jv_jv_j^{*}.
\]

Then the correct test is positivity of \(H_{\mathrm{tail}}+R\), together with a uniform lower frame bound on the negative direction.

## Hostiles

- Arbitrarily large loading along the positive eigenline worsens no determinant obstruction.
- A vector with tiny negative dominance repairs only at diverging strength.
- Exact critical loading creates a radical and cannot prove strict phase velocity.
- Cutoff-dependent incidence rotates toward the cone boundary while scalar energy remains bounded below.

Thus the first high-information source datum is not the total wall energy. It is the oriented incidence angle of that energy relative to the reciprocal negative tail mode.
