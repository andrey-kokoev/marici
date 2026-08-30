# Valuation-shell shift embeds isometrically into continuous scale translation

## Prime scale mesh

Fix a prime \(p\) and set

\[
L_p=\log p.
\]

Let \(\ell^2(\mathbb N_0)\) carry the valuation-shell sequence \(c=(c_k)\). Define the step-history embedding

\[
(J_pc)(t)
=
L_p^{-1/2}c_k,
\qquad
kL_p\le t<(k+1)L_p.
\]

Its range is the closed subspace of \(L^2(\mathbb R_+)\) consisting of functions constant on the prime-scale mesh intervals.

## Isometry

Direct integration gives

\[
\|J_pc\|_{L^2}^2
=
\sum_{k\ge0}
\int_{kL_p}^{(k+1)L_p}
L_p^{-1}|c_k|^2\,dt
=
\sum_{k\ge0}|c_k|^2.
\]

Therefore

\[
J_p:\ell^2(\mathbb N_0)\to L^2(\mathbb R_+)
\]

is an isometry.

No prime-dependent norm loss is introduced by the mesh length.

## Shift intertwining

Let \(B\) be the shell backward shift

\[
(Bc)_k=c_{k+1}.
\]

Let \(T_{L_p}\) be continuous left translation on the half-line:

\[
(T_{L_p}f)(t)=f(t+L_p).
\]

Then

\[
T_{L_p}J_p=J_pB.
\]

Indeed, translating one mesh interval forward reads the next shell coefficient.

Thus the discrete valuation ray is an invariant step-history subspace of continuous scale translation.

## Boundary observer

Point evaluation at \(t=0\) is not bounded on \(L^2\). The correctly typed observer on the step-history subspace is the normalized first-cell average

\[
A_{0,p}f
=
L_p^{-1/2}
\int_0^{L_p}f(t)\,dt.
\]

For embedded sequences,

\[
A_{0,p}J_pc=c_0.
\]

Hence

\[
A_{0,p}J_p=E_0.
\]

The discrete endpoint evaluation becomes a bounded cell-average boundary port in the continuous history carrier.

## Resolvent comparison

For \(|q|<1\),

\[
(I-qT_{L_p})^{-1}J_p
=
J_p(I-qB)^{-1}.
\]

Applying the boundary observer gives

\[
A_{0,p}
(I-qT_{L_p})^{-1}
J_p
=
E_0(I-qB)^{-1}.
\]

With \(q=p^{-s}\),

\[
Z_p(f,s)
=
A_{0,p}
\left(
I-p^{-s}T_{L_p}
\right)^{-1}
J_p\mathcal R_pf.
\]

This is an exact continuous-history realization of the local Tate observer.

## Relation to theta scale histories

The theta cut atoms already use displacements

\[
k\log p=kL_p.
\]

Therefore the mesh of \(J_p\) is not invented. It is exactly the prime-power scale lattice already present in the theta history construction.

The discrete shell shift and continuous moving-seam translation now share the same source clock.

## What is closed

The following comparison is exact:

\[
\text{valuation shell sequence}
\xrightarrow{J_p}
\text{prime-mesh continuous history},
\]

with intertwining of:

- one-step shell transport;
- translation by \(\log p\);
- resolvents;
- boundary evaluation versus first-cell average.

This closes the carrier-level discrete-to-continuous Green comparison.

## Remaining theta-profile gate

The range of \(J_p\) consists of step histories. The actual theta histories are smooth profiles such as

\[
t\mapsto\Phi(t+kL_p)
\]

and oriented seam restrictions.

A source smoothing map must compare the step-history subspace with these theta-generated histories while preserving:

\[
T_{L_p},
\qquad
A_{0,p},
\qquad
\text{tail–seam orientation}.
\]

Convolution by \(\Phi\) is a natural candidate, but it changes the boundary observer and requires an exact Green/Stokes comparison.

Thus the remaining arrow is no longer discrete versus continuous time. It is step history versus theta-smoothed history.

## All-prime assembly

The mesh length depends on \(p\), so no single common step partition exists across primes. The correctly typed global carrier is the direct sum

\[
\bigoplus_p
L^2(\mathbb R_+)_{(p)}
\]

with one prime-labelled translation \(T_{\log p}\) per fiber.

Erasing prime labels before embedding would mix incompatible meshes.

Each \(J_p\) is isometric, so the direct-sum embedding has norm one. The prime dependence enters only through the boundary average and subsequent Euler weights.

## Rigged qualification

The spherical constant shell state is not in \(\ell^2\), and its constant step history is not in \(L^2(\mathbb R_+)\). Both belong to corresponding rigged dual or weighted spaces.

The intertwining formula first holds on finite shell packets and then extends in the locally convergent resolvent topology for \(\operatorname{Re}s>0\).

## Hostiles

1. use point evaluation as a bounded \(L^2\) wall observer;
2. omit the factor \(L_p^{-1/2}\);
3. combine different prime meshes before retaining labels;
4. infer equality with smooth theta histories from translation intertwining alone;
5. place the constant spherical state in ordinary Hilbert space.

## Verdict

The valuation backward shift has an exact isometric realization as translation by \(\log p\) on prime-mesh step histories, and its boundary Weyl function is preserved.

The final Tate-to-theta comparison is now narrowed to a smoothing/intertwining theorem from step histories to theta histories with the correct boundary Green port.
