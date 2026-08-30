# One cyclic Fourier covector generates the full exterior-observer packet

## Reduction

The five-cell boundary quotient relative to the Gaussian bulk is

\[
W=\operatorname{span}\{1,\delta_0,K,V\},
\]

with Fourier operator \(F\) satisfying

\[
F^4=I
\]

and character decomposition

\[
W=W_1\oplus W_{-1}\oplus W_i\oplus W_{-i}.
\]

It is unnecessary to construct four unrelated observer rows. One source-derived covector can generate the complete representation-valued observer, provided it is cyclic for the Fourier action.

## Orbit observer

Let \(\ell\in W'\) be a source-authorized boundary covector. Define

\[
\mathcal O_\ell:
W\longrightarrow\mathbb C^4,
\qquad
\mathcal O_\ell(w)
=
\bigl(
\ell(w),
\ell(Fw),
\ell(F^2w),
\ell(F^3w)
\bigr).
\]

This packet is automatically Fourier equivariant, with Fourier acting on the target by cyclic shift.

Write

\[
\ell_\chi=\ell|_{W_\chi},
\qquad
\chi\in\{1,-1,i,-i\}.
\]

In the character basis, the observer matrix factors as a discrete Fourier matrix times

\[
\operatorname{diag}
(\ell_1,\ell_{-1},\ell_i,\ell_{-i}).
\]

Therefore

\[
\mathcal O_\ell\ \text{is injective}
\quad\Longleftrightarrow\quad
\ell_\chi\ne0
\ \text{for every }\chi.
\]

Thus full boundary descent reduces to four nonvanishing character couplings of one covector.

## Quantitative frame

With unitary normalization of the four-point Fourier matrix,

\[
\sigma_{\min}(\mathcal O_\ell)
=
2\min_\chi |\ell_\chi|
\]

up to the fixed basis normalization. Completion-stable faithfulness is therefore equivalent to

\[
\inf_{X,s,\chi}
|\ell_{X,s,\chi}|>0
\]

on the declared cutoff family and compact off-seam parameter sets.

This is stronger and cleaner than checking only rank four at each finite cutoff. It exposes exactly which Fourier character becomes dark.

## Source authority

The construction is authorized only if:

1. \(\ell\) itself comes from one source boundary incidence, not from fitting four character coordinates;
2. all four iterates use the source Fourier–Tate arrow on one common domain;
3. Clark-before-tail precedence is preserved under every iterate;
4. the orbit closes with \(F^4=I\) or with the declared source comparison cell;
5. the resulting Green-current packet is transported by the same cyclic action.

The scalar Riemann readout is then a later matrix coefficient

\[
r_s\circ\mathcal O_\ell.
\]

It cannot replace \(\mathcal O_\ell\), because \(r_s\) may annihilate nonzero boundary packets.

## Minimal hostiles

A covector with \(\ell_i=0\) sees all even wall data but loses one reciprocal orientation sector. Its four orbit rows are dependent despite being distinct.

A family with every \(\ell_{X,\chi}\ne0\) but

\[
\min_\chi|\ell_{X,\chi}|\to0
\]

passes finite rank and fails completion.

A fitted cyclic covector having four nonzero components but no source boundary incidence passes linear algebra and fails constructor authority.

## Frontier

The exterior-observer problem has contracted to a cyclicity theorem:

> Find one source-derived five-cell boundary covector whose projections onto all four Fourier character lines are nonzero, and prove a uniform lower bound for those projections and their Green-current lifts.

If this succeeds, Fourier transport generates the complete representation-valued observer packet automatically. The remaining RH-bearing step is then the control theorem transporting nullity of the scalar matrix coefficient back to vanishing of the faithful four-port packet.
