# The naive graded Euler--Dirac supertrace produces a derivative or an unbounded anticommutator, not the Weil potential

## Target

The weighted Euler tower produces the real prime potential

\[
V(s)=
\sum_{p\in S}(\log p)
\sum_{k\ge1}p^{-k/2}\cos(ks\log p).
\]

We test whether a standard doubled Dirac operator turns this multiplication potential into a positive compressed supertrace representing the Weil functional.

Let

\[
D=-i\partial_s
\]

on a common smooth core.

## First doubling: separate signs

Take

\[
D_+=D+V,
\qquad
D_-=D-V.
\]

Then

\[
D_+^2=D^2+DV+VD+V^2,
\]

\[
D_-^2=D^2-DV-VD+V^2,
\]

so

\[
\boxed{
D_+^2-D_-^2=2(DV+VD).
}
\]

This does cancel `V^2`, but it produces the anticommutator, not multiplication by `V`.

Since

\[
DV=VD+[D,V],
\qquad
[D,V]=-iV',
\]

we have

\[
D_+^2-D_-^2=4VD-2iV'.
\]

The first term is unbounded and first-order. A trace against a spectral multiplier does not reduce formally to the zeroth-order Weil potential.

## Cyclic trace audit

Suppose `F` is a bounded smoothing/compression for which all relevant products are trace class and ordinary cyclicity is valid. Then

\[
\operatorname{Tr}(F[D,V])
=
\operatorname{Tr}([F D,V])
-
\operatorname{Tr}([F,V]D).
\]

If `F` commutes with `V`, the first term is the trace of a trace-class commutator and vanishes. What remains depends on the derivative or noncommutation of the observer, not on `V` itself.

Likewise, the anticommutator term contains

\[
\operatorname{Tr}(FVD),
\]

which is not automatically trace class and has no positivity sign. Therefore the proposed expression

\[
\operatorname{Str}(F(D_+^2-D_-^2))
\]

is neither automatically defined nor equal to the Weil current.

## Standard supersymmetric off-diagonal doubling

Consider instead

\[
\mathcal D_V=
\begin{pmatrix}
0&D-iV\\
D+iV&0
\end{pmatrix}.
\]

Its square is

\[
\mathcal D_V^2=
\begin{pmatrix}
(D-iV)(D+iV)&0\\
0&(D+iV)(D-iV)
\end{pmatrix}.
\]

Direct calculation gives

\[
(D-iV)(D+iV)=D^2+V^2+V',
\]

\[
(D+iV)(D-iV)=D^2+V^2-V'.
\]

Hence

\[
\boxed{
\operatorname{graded}(\mathcal D_V^2)=2V'.
}
\]

This is the usual supersymmetric mechanism: the common positive square cancels in the grading, leaving the derivative of the superpotential. It produces `V'`, not `V`.

For the prime tower,

\[
V'(s)
=-
\sum_{p,k}
k(\log p)^2p^{-k/2}\sin(ks\log p),
\]

which has the wrong parity and an extra factor `k log p` relative to the Weil prime current.

## Primitive workaround and its boundary cost

To obtain `V` from a supersymmetric derivative, one could choose a superpotential `A` satisfying

\[
A'=V.
\]

Termwise,

\[
A(s)=
\sum_{p,k}
\frac{p^{-k/2}}{k}
\sin(ks\log p)
\]

up to a constant. This is the imaginary part of a logarithm of the Euler product. It is bounded for every finite prime set, but its additive constant and branch are boundary data.

Using `A` in the supersymmetric Dirac gives

\[
\operatorname{graded}(\mathcal D_A^2)=2V.
\]

This algebraically produces the desired local current. However:

1. the two diagonal squares are positive separately, while their supertrace is signed;
2. an ordinary trace of their difference is an index/boundary quantity, not a positive trace;
3. branch constants reappear as endpoint terms;
4. under support or place exhaustion, uniform control of `A` is not automatic;
5. inserting the observer must make the heat/resolvent difference trace class.

Thus the primitive repairs the derivative order but moves the missing information into boundary normalization and trace regularization.

## Heat-supertrace test

For a genuine supersymmetric Fredholm pair, cyclicity makes

\[
\operatorname{Str}(e^{-t\mathcal D_A^2})
\]

time-independent and equal to an index. It cannot reproduce an arbitrary test-dependent Weil functional without inserting a noncommuting representation `vartheta(f)`. Once that insertion is made, the supertrace depends on commutators

\[
[\mathcal D_A,\vartheta(f)],
\]

and positivity is lost unless a separate trace identity reorganizes the result as `Tr(B_fB_f*)`.

This is precisely the nontrivial content of a relative trace formula; it is not supplied by supersymmetry alone.

## Corrected candidate

The only algebraically correctly typed local Dirac uses the Euler-logarithm primitive

\[
A_S(s)
=
\operatorname{Im}\log M_S(s)

\]

with

\[
A_S'=V_S.
\]

Then

\[
\mathcal D_{A_S}
=
\begin{pmatrix}
0&D-iA_S\\
D+iA_S&0
\end{pmatrix}
\]

has graded square difference `2V_S`. A completed construction must add the archimedean phase primitive and choose the endpoint branch so that the full phase is globally normalized.

The exact remaining identity is not positivity of `mathcal D_A^2`; it is a localized supertrace formula

\[
\operatorname{Str}
\left(\vartheta(f)e^{-t\mathcal D_A^2}
\right)
=
W_S(f)+
\text{controlled boundary remainder},
\]

followed by a separate argument that the relevant combination is a positive ordinary trace.

## Disposition

The first proposed graded square does not work:

\[
\boxed{
(D+V)^2-(D-V)^2=2\{D,V\},
}
\]

an unbounded anticommutator. Standard supersymmetric doubling gives `2V'`, also the wrong current.

Using the phase primitive `A=Im log M` corrects the derivative:

\[
\boxed{
\operatorname{graded}(\mathcal D_A^2)=2A'=2V.
}
\]

But its supertrace is signed and boundary-sensitive. The next required theorem is a localized heat-supertrace/relative-trace identity plus a conversion to an ordinary positive trace; supersymmetry by itself does not provide positivity.
