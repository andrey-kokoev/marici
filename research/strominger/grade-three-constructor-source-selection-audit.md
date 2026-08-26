# Grade-three constructor source-selection theorem

## Curvature commutator

Write \(E_t:{}_t\mathcal H\to{}_{t+1}\mathcal H\) and
\(B_t:{}_t\mathcal H\to{}_{t-1}\mathcal H\) for the spin ladder maps. Their
harmonic multipliers give

\[
B_{t+1}E_t-E_{t-1}B_t=2tI.
\]

For the four spin-two to spin-four words, listed in acting order,

\[
F_0=EEEB,\quad F_1=EEBE,\quad F_2=EBEE,\quad F_3=BEEE,
\]

successive commutation gives

\[
F_0=F_1+8E^2,\qquad
F_1=F_2+6E^2,\qquad
F_2=F_3+4E^2,
\]

and therefore

\[
F_0=F_3+18E^2.
\]

All four words agree on the \(l=2,3\) kernel of \(E^2\). On \(l=4\),

\[
F_3=-18E^2,
\]

so \(F_0\) vanishes. The extra nine-dimensional kernel is an exact spherical
curvature cancellation invisible to the common flat principal symbol.

## Source derivation from the Bondi constraint

The upstream identity is the \(G_{uz}=8\pi G T_{uz}\) Bondi constraint. In the
conventions of Pasterski, Strominger, and Zhiboedov, its shear term is

\[
\frac14\partial_z
\left[D_z^2C^{zz}-D_{\bar z}^2C^{\bar z\bar z}\right].
\]

Taking \(\partial_{\bar z}\) of this equation, taking \(\partial_z\) of its
conjugate, and selecting the imaginary curl gives

\[
\operatorname{Im}\!\left[\partial_{\bar z}D_z^3C^{zz}\right]
=
2\operatorname{Im}\!\left[
\partial_u\partial_{\bar z}N_z+\partial_{\bar z}T_{uz}
\right].
\]

This is equation (5.2) of *New Gravitational Memories*, JHEP 12 (2016) 053,
derived from equation (2.3) and its conjugate:
<https://doi.org/10.1007/JHEP12(2016)053>.

The derivative order is fixed before any spectral kernel is computed:

    Bondi shear C
      -> two covariant z derivatives inside the angular-momentum constraint
      -> the constraint's outer z derivative
      -> the curl's final zbar derivative
      -> EEEB

The mass-aspect gradient disappears under the imaginary curl. Flux and the
angular-momentum aspect survive on the right-hand side. Replacing \(F_0\) by
\(F_1\) changes the readout by \(-8E^2C\); replacing it by \(F_3\) changes it
by \(-18E^2C\). These are new curvature counterterms, not reorderings
authorized by the same Einstein constraint.

## Authority classification

    ordered readout:
      derived from the Bondi G_uz constraint plus curl
    spectral kernel:
      exact consequence of the derived readout
    21-port completion repair:
      exact conditional capability
    uniqueness among words for that constraint-derived port:
      established
    uniqueness among all conceivable physical observables:
      not asserted

Thus 21 has an explanation inside the declared asymptotically flat
Einstein-gravity sector:

\[
\text{Einstein constraint}
\longrightarrow
\text{curl removing the mass gradient}
\longrightarrow
F_0
\longrightarrow
\text{curvature cancellation on }l=4
\longrightarrow
\dim\ker F_0=21.
\]

This does not make \(F_1,F_2,F_3\) meaningless. They are simply different
observables. Authorizing one requires a modified constraint or another
source-derived readout.

## Coordinate-to-bundle coherence

The independent local checker closes the remaining comparison. Its
`chain` constructor applies the covariant \(z\)-derivative successively at
weights 2, 3, and 4, then `M` applies the final \(\bar z\)-derivative. It
derives the invariant puncture response without using the harmonic
multiplier. The global checker independently composes the three spin-raising
multipliers and the final lowering multiplier.

These two presentations agree on:

1. source spin two and target spin four;
2. acting order `EEEB`;
3. fourth differential order;
4. parity-conjugate helicity pairing;
5. a nonzero invariant puncture witness.

This rules out a hidden reordering or fitted curvature correction in the
coordinate-to-bundle transport. Overall normalization and phase remain
convention-sensitive, but neither affects the kernel or word selection.
