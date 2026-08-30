# The selfadjoint history-incidence Dirac has no boundary defect space

## Decisive distinction

The canonical incidence Dirac

\[
\mathscr D_H=
\begin{pmatrix}
0&H^*\\
H&0
\end{pmatrix},
\qquad
\operatorname{dom}\mathscr D_H
=
\operatorname{dom}H\oplus\operatorname{dom}H^*,
\]

is selfadjoint whenever \(H\) is closed and densely defined.

Therefore

\[
n_+(\mathscr D_H)=n_-(\mathscr D_H)=0.
\]

It has no nontrivial ordinary boundary triple and no family of selfadjoint extensions parameterized by a finite boundary carrier.

This blocks a silent identification made in the current architecture: the selfadjoint graph-conormal Dirac cannot simultaneously be the minimal symmetric history operator whose deficiency space carries the Weyl pencil.

## Two operators are required

The source construction currently supplies an adjoint-complete incidence operator:

\[
H
\longmapsto
\mathscr D_H.
\]

A boundary-triple construction instead requires a proper symmetric restriction

\[
S_{\min}\subsetneq S_{\max}=S_{\min}^*
\]

with nonzero equal deficiency indices. Its extension data live in

\[
N_s=\ker(S_{\max}-s).
\]

These are categorically different roles:

- \(\mathscr D_H\): completed conservative propagation, already selfadjoint;
- \(S_{\min}\): unresolved differential or history generator with boundary degrees of freedom;
- \(S_\Theta\): a source-selected selfadjoint extension of \(S_{\min}\).

The first may realize one particular extension of the second, but that relation must be constructed.

## Consequence for the Weyl proposal

One cannot define a nontrivial Poisson operator for \(\mathscr D_H\) by

\[
\gamma(s):\mathcal B\to
\ker(\mathscr D_H^*-s)
\]

off the real axis. Since \(\mathscr D_H^*=\mathscr D_H\), this kernel is zero for every \(s\notin\mathbb R\).

Hence the proposed finite Weyl function must come from a separate maximal operator \(S_{\max}\), not from the already selfadjoint graph Dirac.

A formal endpoint trace attached to \(\mathscr D_H\) does not change this. Unless its domain is first enlarged and a genuine minimal restriction is frozen, it is an observer of a selfadjoint operator rather than an extension coordinate.

## Candidate source restriction

The adjacent-window path suggests the correct local differential carrier. On each oriented scale interval \([L,2L]\), begin with the first-order generator on compactly supported histories and then close it with zero endpoint trace:

\[
S_{\min,p}
=
-i\partial_t
\quad
\text{on the minimal endpoint domain}.
\]

Its maximal adjoint has unrestricted \(H^1\) traces, and the endpoint Green form is

\[
\langle S_{\max,p}u,v\rangle
-
\langle u,S_{\max,p}v\rangle
=
-i\langle u(2L),v(2L)\rangle
+i\langle u(L),v(L)\rangle.
\]

For a scalar channel, the deficiency indices are \((1,1)\). Reciprocal doubling gives \((2,2)\), provided the two orientations are genuinely independent and the source domain does not identify them earlier.

This is the plausible rank-two history boundary space. It is not yet the full theta history incidence \(H\), and it is not established merely by writing the derivative model.

## Required comparison theorem

To connect the exact Adams constructor to boundary Weyl theory, prove a commuting realization:

\[
\text{minimal scale derivative}
\longrightarrow
\text{source-selected extension}
\longrightarrow
\text{Volterra history propagator }H
\longrightarrow
\mathscr D_H.
\]

Concretely, one needs:

1. a source-derived minimal differential operator \(S_{\min}\);
2. its maximal adjoint and complete endpoint Green identity;
3. exact deficiency indices;
4. a boundary relation \(\Theta_0\) whose extension produces the declared causal/anti-causal history;
5. identification of the corresponding Poisson or resolvent block with the constructed history map;
6. proof that graph-conormal completion of that extension equals the canonical \(\mathscr D_H\).

Without item 4, the boundary condition may be fitted. Without item 5, the Weyl return and the Adams constructor remain parallel models rather than one system.

## Placement of arithmetic sewing

The arithmetic relation \(\Theta(s)\) should act on the deficiency boundary of \(S_{\min}\), while the reference extension \(\Theta_0\) realizes the zero-free history propagation.

The finite spectral defect is then a relative extension comparison:

\[
\Theta(s)-M(s),
\]

or equivalently a Krein resolvent correction relative to \(S_{\Theta_0}\).

This explains why the bulk history may remain invertible while zeros arise from finite sewing. It also prevents adding a boundary pencil to an operator that was already selfadjoint with no declared restriction.

## Relation to the growing reservoir

The first-order reciprocal double has fixed deficiency rank two only if every additional prime-labelled memory mode belongs to the interior realization of the reference extension. If any growing reservoir direction enters

\[
\ker(S_{\max}-s),
\]

the rank-two claim fails.

Thus the next finite audit must compute the defect equation for the actual source differential carrier, not for the abstract graph Dirac and not for the scalar characteristic polynomial.

## Hostile

Take any closed injective \(H\) and form \(\mathscr D_H\). Attach an arbitrary two-dimensional space \(\mathcal B\) and a fitted analytic matrix \(M(s)\). Because \(\mathscr D_H\) has zero deficiency indices, this matrix cannot be its Weyl function. Any determinant agreement obtained from it is external fitting.

A second hostile starts from \(-i\partial_t\) but chooses boundary conditions after matching zeta. Its deficiency rank is correct while its arithmetic authority is circular.

## Frontier contraction

The earliest unresolved operator theorem is now:

> Construct the minimal reciprocal scale-history generator whose source-selected reference extension reproduces the already authorized causal history map.

Only after this theorem can the finite rank-two boundary carrier, its Weyl function, and its arithmetic sewing determinant be regarded as properties of the same constructor system.
