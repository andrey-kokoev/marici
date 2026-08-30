# Half-density transport gives the completion operator a canonical quarter-gap Green inverse

## Conjugated completion

On one positive ray, the half-density transform satisfies

\[
\mathcal C\mathcal M_n
=
\mathcal M_nP,
\]

where

\[
P=A(A+1)
\]

and

\[
\mathcal C
=
D_u^2-\frac14.
\]

Because \(\mathcal M_n\) is isometric, the analytic inversion problem for
\(P\) is transported to the constant-coefficient operator \(\mathcal C\) on
the logarithmic line.

## Spectral gap

Under the Fourier transform in \(u\),

\[
\widehat{\mathcal C h}(\xi)
=
-\left(
\xi^2+\frac14
\right)\widehat h(\xi).
\]

Hence

\[
-\mathcal C
\ge
\frac14 I.
\]

There is no \(L^2(\mathbb R,du)\) radical, and

\[
\|\mathcal C^{-1}\|_{L^2\to L^2}
=
4.
\]

Thus the reduced inverse needed for the first Adams cell is not an arbitrary
pseudoinverse on the Hilbert ray. It is the canonical bounded Green
resolvent of the quarter-gap operator.

## Explicit Green kernel

The inverse is convolution with

\[
G_{\mathcal C}(u,v)
=
-e^{-|u-v|/2}.
\]

Indeed,

\[
\mathcal C^{-1}h(u)
=
-\int_{\mathbb R}
e^{-|u-v|/2}h(v)\,dv.
\]

The sign is fixed because \(\mathcal C\) is strictly negative.

## Transported inverse

On the half-density image of the positive ray,

\[
P^{-1}
=
\mathcal M_n^{-1}
\mathcal C^{-1}
\mathcal M_n.
\]

This formula is label-independent up to the canonical coordinate isometry.
It supplies the Green propagation required in

\[
b_p
=
P^{-1}
\left(
T_LPf_0+[P,T_L]f_0
\right).
\]

For the two-ray packet, use the direct sum of the two quarter-gap resolvents,
followed by the already proved moving-cut sewing.

## What remains typed

The Hilbert inverse is now solved, but three constructor checks remain:

1. the complete source
   \[
   T_LPf_0+[P,T_L]f_0
   \]
   must be transported into the correct two-ray half-density fibers;
2. coefficient-wall routing must be separated before entering the Hilbert
   resolvent;
3. theta-label assembly must commute with the resolvent on the declared
   graph core.

These are intertwining questions, not questions of existence or norm control
for the Green inverse.

## Uniform control

The inverse bound

\[
\|\mathcal C^{-1}\|=4
\]

is independent of prime, theta label, cutoff, and reciprocal ray. Therefore
the Green-propagation stage contributes no prime-dependent loss to the first
Adams edge.

Any remaining completion instability must arise in the incidence, wall,
label-synthesis, or sewing maps.

## Source-coordinate caution

The formal kernel of \(A(A+1)\) contains the algebraic modes \(1\) and
\(x^{-1}\). They do not become \(L^2(du)\) half-density vectors on the full
logarithmic line. Treating them as a Hilbert radical would incorrectly erase
the quarter-gap.

They may still occur as exterior wall distributions, but those are typed
outside the Hilbert resolvent and routed separately.

## Consequence

The first Adams-edge assembly now has an explicit analytic normal form:

\[
\text{base plus curvature source}
\longrightarrow
\mathcal M_{\pm}
\longrightarrow
\mathcal C^{-1}
\longrightarrow
\text{two-ray sewing}
\longrightarrow
S_{\mathrm{ord}}.
\]

The earliest unresolved arrow is the source-authorized compatibility of this
normal form with theta-label assembly and coefficient-wall routing.

## Hostile

Insert a Moore--Penrose inverse for \(P\) in the raw algebraic coordinate and
declare the modes \(1,x^{-1}\) to be gauge. This changes the source topology
and misses the canonical fact that the half-density Hilbert completion has a
strict gap \(1/4\) and an ordinary bounded inverse.
