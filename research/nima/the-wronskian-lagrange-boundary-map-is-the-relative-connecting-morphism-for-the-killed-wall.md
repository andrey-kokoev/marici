# The Wronskian–Lagrange boundary map is the relative connecting morphism for the killed wall

The wall killed by theta completion is not disconnected from the completed
image. Its source-derived connecting morphism is the boundary concomitant of
the completion differential.

## Completion operator and wall kernel

Let

\[
\mathcal C
=
\partial_u^2-\frac14.
\]

The two half-density wall solutions are

\[
\omega_-(u)=e^{-u/2},
\qquad
\omega_+(u)=e^{u/2},
\]

and

\[
\mathcal C\omega_\pm=0.
\]

They span the bilateral wall kernel in the maximal relative domain.

## Lagrange identity

For a precursor \(h\) in the relative Green domain,

\[
\omega\,\mathcal Ch-(\mathcal C\omega)h
=
\partial_u\left(\omega h'-\omega'h\right).
\]

Since \(\mathcal C\omega_\pm=0\), integration gives

\[
\int_{\mathbb R}\omega_-(u)\mathcal Ch(u)\,du
=
\Delta
\left[
e^{-u/2}\left(h'(u)+\frac12h(u)\right)
\right],
\]

and

\[
\int_{\mathbb R}\omega_+(u)\mathcal Ch(u)\,du
=
\Delta
\left[
e^{u/2}\left(h'(u)-\frac12h(u)\right)
\right].
\]

These are exactly the two source Wronskian traces.

## Relative connecting morphism

Define

\[
\partial_{\mathcal C}:
\operatorname{Ran}\mathcal C
\longrightarrow
(\ker\mathcal C)^*
\]

by

\[
\left\langle
\partial_{\mathcal C}(\mathcal Ch),\omega
\right\rangle
=
\left[
\omega h'-\omega'h
\right]_{-\infty}^{+\infty}.
\]

In the wall basis \((\omega_-,\omega_+)\),

\[
\partial_{\mathcal C}(\mathcal Ch)
=
\begin{pmatrix}
M_-(\mathcal Ch)\\
M_+(\mathcal Ch)
\end{pmatrix}.
\]

Thus the completed source pairs canonically with the killed wall through a
boundary map. No splitting of the exact sequence and no post-completion
identity insertion is required.

## Independence of precursor representative

If \(h\) is replaced by \(h+k\) with \(k\in\ker\mathcal C\), the completed
image is unchanged. The boundary concomitant changes by the wall–wall
symplectic pairing

\[
[\omega k'-\omega'k]_{-\infty}^{+\infty}.
\]

Therefore the connecting morphism is single-valued precisely on the relative
domain whose authorized endpoint frame fixes this kernel ambiguity, or after
recording the kernel coordinate as part of the mapping-cone object. This is
why quotienting by the wall before boundary typing is invalid.

The correct object is not merely \(\operatorname{Ran}\mathcal C\), but

\[
\operatorname{Cone}(\mathcal C)
=
\ker\mathcal C
\oplus
\operatorname{Dom}\mathcal C
\oplus
\operatorname{Ran}\mathcal C
\]

with the Lagrange boundary relation.

## Theta normalization

For

\[
h(u)=\frac12e^{u/2}\vartheta(e^{2u}),
\qquad
\Phi=\mathcal Ch,
\]

the source endpoint asymptotics give

\[
\partial_{\mathcal C}(\Phi)
=
\begin{pmatrix}
\frac12\\
\frac12
\end{pmatrix}.
\]

Hence the killed wall has a nonzero, exactly normalized return from the
completed theta image. In parity coordinates,

\[
w(\Phi)=\frac1{\sqrt2},
\qquad
j(\Phi)=0.
\]

For the source derivative,

\[
\partial_{\mathcal C}(\Phi')
=
\begin{pmatrix}
\frac14\\
-\frac14
\end{pmatrix},
\]

so

\[
w(\Phi')=0,
\qquad
j(\Phi')=-\frac1{2\sqrt2}.
\]

The even wall and odd reciprocal jump are therefore the two components of one
relative Lagrange boundary map.

## Reflection covariance

Reflection exchanges \(\omega_-\) and \(\omega_+\). It fixes \(\Phi\) and
reverses \(\Phi'\). Consequently the connecting morphism decomposes into the
correct reciprocal-even and reciprocal-odd characters without an imported
phase convention.

## Constructor consequence

The missing relative face is now explicit:

\[
\operatorname{Ran}\mathcal C
\xrightarrow{\partial_{\mathcal C}}
(\ker\mathcal C)^*.
\]

This closes the source-level wall-to-completed-history incidence in the
relative completion complex. It also explains why the wall column of
\(\mathcal C\) is zero while its boundary observation is nonzero.

What remains is to attach the Gaussian adjacent-window cell to
\(\operatorname{Dom}\mathcal C\) and prove that its two fronts and path
derivative produce this same Lagrange boundary relation. Only then may the
Green form be transported by block congruence and Schur elimination.

No Adams type edge, completed boundary pencil, or coercivity theorem follows
yet.

## Source locators

- research/nima/twisted-theta-histories-give-exact-normalized-completion-trace-columns.md
- research/nima/the-completion-differential-annihilates-the-wall-so-the-common-carrier-must-be-relative.md
- research/nima/the-first-theta-label-completion-packet-has-three-explicit-jordan-grades-and-zero-wall-image.md
- research/nima/the-bilateral-theta-derivative-supplies-the-missing-reciprocal-trace-direction.md
