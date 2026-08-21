# Fiber-sum transfer repairs the noninjective deck-selection square

For a homomorphism of finite deck groups

\[
\phi:G\longrightarrow H,
\]

define the covariant fiber-sum transfer on function algebras by

\[
(\phi_!f)(h)=\sum_{g:\phi(g)=h}f(g).
\]

Unlike pullback, this preserves the physical identity selection for every
\(\phi\):

\[
\boxed{
\phi_!\delta_{0,G}=\delta_{0,H}.
}
\]

Indeed, only \(g=0\) contributes, and it lies over \(h=0\).

## Forced normalization

The transfer is the unnormalized fiber sum.  Dividing by \(|\ker\phi|\)
would give

\[
\frac1{|\ker\phi|}\delta_{0,H}
\]

and would fail the frozen physical normalization.  Thus the identity pairing
itself selects the counting/Gysin normalization.

## Composition and projection formula

Fiber sums compose strictly:

\[
(\psi\circ\phi)_!=\psi_!\phi_!.
\]

They also satisfy Frobenius reciprocity:

\[
\phi_!(f\cdot\phi^*g)=\phi_!(f)\cdot g.
\]

This supplies the finite-deck analogue of the supported pushforward required
by the variance audit.

## Constructor-principle reading

The earlier impossibility was relative to the wrong resource class:
ordinary pullback cannot preserve identity selection across a noninjective
deck map.  Adding the independently typed covariant transfer makes the task
possible and fixes its normalization.

This is exactly the predicted pattern

\[
\text{impossible under pullback alone}
+
\text{supported/covariant resource}
\longrightarrow
\text{canonical physical map}.
\]

## Physical-authority boundary

The finite-group construction is canonical algebraically, but it is not by
itself a physical cosmological map.  Physical admission requires the source
geometry to supply the corresponding deck trace, transfer, or Gysin map and
to verify its orientation, multiplicity, support, and chain normalization.

## Verification

The checker enumerates cyclic deck homomorphisms through order 12, verifies
identity-selection preservation and Frobenius reciprocity on indicator bases,
and checks strict composition for all cyclic orders through 9.

Evidence: `research/nima/check_finite_deck_transfer.py` and the preceding
deck-selection variance theorem.
