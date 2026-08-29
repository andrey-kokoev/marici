# Polarized boundary incidence factors through scale, cyclicity, and half-density

## Question

Does the inclusion of the positive valuation cone into its bilateral group completion determine the primitive and square boundary currents?

It determines their support and orientation, but not their weights.

At one prime, a boundary map compatible with valuation reversal may send the grade-\(k\) cyclic state to

\[
a_{p,k}\,\delta_{k\log p}
\]

for many possible coefficients \(a_{p,k}\). Reversal only transports this atom to the opposite scale orientation. It does not select \(a_{p,k}\).

## Three source laws

The theta/Tate incidence coefficient is fixed only after composing three independently derived operations.

First, the labelled Fock word supplies the scale map

\[
(p,k)\longmapsto k\log p.
\]

Second, cyclic trace formation supplies the orbit normalization

\[
k\longmapsto\frac1k.
\]

Third, unitary sewing on the critical seam supplies the half-density amplitude

\[
u_p=p^{-1/2}.
\]

The grade-\(k\) word carries \(u_p^k\). Therefore the incidence is

\[
I_k(p,k)
=
\frac{u_p^k}{k}\delta_{k\log p}
=
\frac1k p^{-k/2}\delta_{k\log p}.
\]

The primitive and square maps are the first two grades:

\[
I_1(p,1)=p^{-1/2}\delta_{\log p},
\]

\[
I_2(p,2)=\frac12p^{-1}\delta_{2\log p}.
\]

The factor \(1/2\) is cyclic normalization. The factor \(p^{-1}\) is the square of the seam half-density. Neither is supplied by cone polarization alone.

## Uniqueness recurrence

Write \(a_k=u^k/k\) at one fixed prime. These coefficients satisfy

\[
a_1=u,
\qquad
(k+1)a_{k+1}=ku\,a_k.
\]

Conversely, the initial value and this recurrence uniquely determine every cyclic grade. This is the coefficient-level form of logarithmic determinant reconstruction:

\[
-\log(1-uz)=\sum_{k\ge1}\frac{u^k}{k}z^k.
\]

Thus no grade may be normalized independently once the primitive amplitude and cyclic constructor are fixed.

## Fourier typing

Fourier exchanges the two valuation polarizations:

\[
I_{k,-}\mathcal F_k
=
R_{\mathrm{scale}}I_{k,+},
\]

where \(R_{\mathrm{scale}}\) reverses the oriented scale coordinate. This square preserves the coefficient and changes the carrier orientation. It does not derive the coefficient.

The boundary-incidence constructor therefore factors as

\[
\text{cyclic source}
\longrightarrow
\text{weighted labelled scale atoms}
\longrightarrow
\text{relative determinant line}.
\]

The first arrow is now source-derived. The second remains the completed boundary augmentation and must still retain the primitive exponential rigging, square tempered/Hilbert grade, connected trace-class tail, and archimedean channel.

## Finite hostile

Choose arbitrary nonzero coefficients \(b_1,b_2\) and place them at the correct scales. Their atoms have the correct support, arity, and reversal covariance. Unless

\[
2b_2=b_1^2,
\]

they cannot be the first two grades of one cyclic determinant source.

For example, \(b_1=b_2=1\) passes the bare cone and reversal tests but fails cyclic reconstruction. This proves that polarization alone is insufficient.

A second hostile changes the square coefficient while preserving the primitive one. It silently treats the square current as an independent port and breaks the recurrence.

## DPC

A proposed prime/Fock-to-boundary incidence passes only if:

1. the atom is supported at the source scale \(k\log p\);
2. its orientation reverses under intertower Fourier transport;
3. its primitive amplitude is the source half-density \(p^{-1/2}\);
4. cyclic grade \(k\) carries the normalization \(1/k\);
5. all grades satisfy the recurrence from one primitive amplitude;
6. primitive and square coefficients cannot be varied independently;
7. scalar augmentation occurs only after the typed current spaces are retained.

## Outcome

The cone boundary is necessary but not sufficient. The atomic incidence map is uniquely determined by the composite of labelled scale, cyclic trace normalization, and seam half-density. The remaining unknown is no longer the arithmetic incidence coefficient. It is the completed augmentation that couples these already fixed atomic currents to the archimedean boundary and produces a relative determinant-line unit.
