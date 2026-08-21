# The five-site cosmological readout composition square closes

## Source objects

Entry 1225 supplies rank-32 coefficient and Betti modules labelled by

\[
G=(C_2)^5
\]

with simultaneous deck transport

\[
(g,h)\longmapsto(g\oplus k,h\oplus k).
\]

The physical pairing is

\[
\langle e_g,\Gamma_h\rangle=\delta_{g,h}.
\]

## Two constructors

The diagonal-deck quotient is the difference map

\[
F:G\times G\longrightarrow G,
\qquad F(g,h)=g\oplus h.
\]

Its fibers are exactly the 32-element diagonal deck orbits.  The physical
selection is the primitive identity idempotent

\[
E=\delta_0\in\operatorname{Fun}(G,\mathbb Q).
\]

Their composite is

\[
(E\circ F)(g,h)
=\delta_0(g\oplus h)
=\delta_{g,h}.
\]

Therefore

\[
\boxed{
(E\circ F)^*=F^*\circ E^*.
}
\]

## Result

This is the second closed readout-algebra composition square:

\[
\text{coefficient--Betti label pair}
\xrightarrow{\text{diagonal deck quotient}}
\operatorname{Fun}(G,\mathbb Q)
\xrightarrow{\text{identity idempotent}}
\mathbb Q.
\]

It realizes the same abstract pattern as the radiative-memory square:

\[
\text{quotient an unphysical/covariant redundancy}
\longrightarrow
\text{apply an invariant physical selection}.
\]

The coefficient objects and output algebras remain sector-specific.

## Verification and boundary

The checker verifies 1,024 compositions, 1,024 orbit fibers, and 32,768
simultaneous deck-transport identities.

This result uses Entry 1225's already established coefficient--Betti pairing.
It does not create a new physical chain, identify \(\mathbb Q^{32}\) with the
radiative-memory invariant ring, or supply a cross-sector algebra map.

Evidence: Ledger Entry 1225 and
`research/nima/check_cosmology_readout_composition.py`.
