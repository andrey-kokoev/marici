# The archimedean line extension preserves the split endpoint retract, but global Poisson sewing remains separate

## Setup

Let \(E_\theta\) be the retained theta endpoint plane, with coercive metric
\(G_\theta\), and let

\[
P_\theta:E_\theta\oplus E_{\mathrm{win}}\longrightarrow E_\theta
\]

be the split endpoint projection. Let \(\mathcal L_\infty(s)\) be the
one-dimensional archimedean determinant line supplied by the Gaussian Mellin
source.

Archimedean completion acts by tensor extension:

\[
\mathcal E^{\mathrm{comp}}(s)
=
\mathcal L_\infty(s)\otimes
\bigl(E_\theta\oplus E_{\mathrm{win}}\bigr).
\]

It is not an additive perturbation of the endpoint Green block.

## Tensoring a split retract

The endpoint projection extends canonically as

\[
P_\theta^\infty
=
I_{\mathcal L_\infty}\otimes P_\theta.
\]

If \(J_\theta:E_\theta\to E_\theta\oplus E_{\mathrm{win}}\) is the graph
inclusion, then

\[
P_\theta J_\theta=I_{E_\theta}
\]

implies

\[
P_\theta^\infty
\bigl(I_{\mathcal L_\infty}\otimes J_\theta\bigr)
=
I_{\mathcal L_\infty\otimes E_\theta}.
\]

Thus the split endpoint port survives archimedean line attachment exactly.
No scalar Euler--Maclaurin synthesis is needed for this conclusion.

## Metric transport

Choose the source Hermitian metric \(g_\infty(s)>0\) on the archimedean line.
The completed endpoint metric is

\[
G_\theta^\infty(s)
=
g_\infty(s)\otimes G_\theta.
\]

On a compact off-seam parameter set \(C\), if

\[
0<m_C\le g_\infty(s)\le M_C<\infty,
\qquad s\in C,
\]

then

\[
G_\theta^\infty(s)
\ge
m_Cc_\theta I.
\]

Hence the archimedean tensor extension preserves zero radical, closed range,
and a compact-uniform endpoint lower bound. The nonvanishing gamma line is
sufficient for pointwise preservation; compact-uniform metric bounds are
needed for completion-stable coercivity.

## Reciprocal line sewing

The local Tate operator has the form

\[
\widehat{K_\pm g}(t)
=
m_\pm(t)\widehat g(-t),
\]

with

\[
m_+(t)m_+(-t)=1,
\qquad
m_-(t)m_-(-t)=-1.
\]

On the real Mellin axis, \(|m_\pm(t)|=1\). Therefore local reciprocal sewing
acts unitarily on \(\mathcal L_\infty\), up to the declared parity cocycle.
Tensoring this unitary line action with the retained endpoint graph cannot
erase the wall or jump coordinate.

The even and odd Tate lines must remain separately typed. Replacing both by a
single scalar gamma magnitude loses the reciprocal sign.

## What this does not prove

This theorem does not construct global Poisson sewing at finite Euler cutoff.
A finite Euler truncation is not a finite modification of the adelic theta
source: omitting infinitely many Euler factors changes infinitely many
unramified vectors.

Consequently there is no source-authorized finite-cutoff Poisson operator whose
limit may be used to prove the global attachment theorem.

The valid order is:

1. retain the full restricted adelic source;
2. apply global Fourier--Poisson sewing;
3. attach the archimedean determinant line;
4. take Mellin or determinant readout;
5. use finite Euler truncations only as diagnostic projections.

## Global attachment factorization

The reciprocal--archimedean attachment now separates into two arrows:

\[
\text{coercive theta endpoint graph}
\longrightarrow
\mathcal L_\infty\otimes\text{endpoint graph}
\longrightarrow
\text{globally Poisson-sewn adelic carrier}.
\]

The first arrow is closed by the tensor-retract argument above. The second is
not a local endpoint estimate. It is a constructor-coherence theorem on the
full restricted product.

To preserve the local result, global sewing \(\mathscr P\) must satisfy an
intertwining law

\[
\mathscr P
\bigl(I_{\mathcal L_\infty}\otimes P_\theta\bigr)
=
\bigl(I_{\mathcal L_\infty}\otimes P_\theta\bigr)
\mathscr P
\]

or a source-authorized unitary comparison between the two sides. Equality only
after scalar Tate readout is insufficient.

## Hostiles

1. Multiply the archimedean line metric by a positive scalar tending to zero
   along the cutoff or parameter family. Pointwise nonvanishing survives, but
   the endpoint lower margin collapses.
2. Replace tensor extension by additive attachment. This can invent mixed
   arithmetic--archimedean traces and need not preserve the retract.
3. Collapse even and odd Tate lines to their common absolute value. Endpoint
   energy survives while reciprocal orientation is lost.
4. Demand finite-Euler Poisson naturality. This uses a source object outside
   the restricted adelic product.
5. Let global sewing commute only with scalar endpoint synthesis. The retained
   theta coordinate may then disappear before completion.

## Verdict

The archimedean determinant line preserves the split theta endpoint coordinate
by an exact tensor retract. With compact-uniform line-metric bounds, it also
preserves endpoint coercivity and zero radical.

The remaining attachment gate is purely global:

\[
\text{prove that full adelic Fourier--Poisson sewing preserves, or unitarily
transports, the retained split endpoint retract.}
\]

This gate cannot be replaced by finite Euler truncation or scalar functional
equation agreement.
