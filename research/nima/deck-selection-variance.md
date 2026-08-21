# Identity deck selections are pullback-natural only along monomorphisms

Let

\[
\phi:G\longrightarrow H
\]

be a homomorphism of finite deck groups.  Pullback of the identity idempotent
is

\[
(\phi^*\delta_{0,H})(g)
=\delta_{0,H}(\phi(g))
=1_{\ker\phi}(g).
\]

Therefore

\[
\boxed{
\phi^*\delta_{0,H}=\delta_{0,G}
\iff
\ker\phi=0.
}
\]

The physical identity selection is contravariantly natural only along
injective deck maps.

By contrast, every homomorphism commutes with the repetition maps:

\[
\phi\circ[n]=[n]\circ\phi.
\]

Thus the group-level arithmetic diagram can commute while the physical
selection square fails.

## Variance consequence

A quotient or forgetting map of deck groups has nontrivial kernel.  Under
naive pullback, its target identity selection becomes the indicator of the
whole kernel, enlarging the physically selected locus.  Such a constructor
cannot be represented by ordinary pullback alone.  It requires an
independently normalized covariant operation—pushforward, trace, transfer, or
Gysin—plus its selection-coherence square.

This is the same variance distinction repeatedly encountered elsewhere in
Marici:

\[
\text{restriction/pullback}
\ne
\text{supported pushforward/physical selection}.
\]

## Relation to prime-to-exponent operations

For a fixed \(G\), indices \(n\) prime to \(\exp G\) make \([n]\) an
automorphism and hence preserve \(\delta_0\).  Across changing deck groups,
however, selection naturality additionally restricts the allowed constructor
maps to monomorphisms unless transfer data is supplied.

## Verification

The checker enumerates every homomorphism \(C_m\to C_k\) for
\(2\le m,k\le20\), tests the kernel criterion pointwise, and verifies
commutation with \([n]\) for \(1\le n\le30\).

Evidence: `research/nima/check_deck_selection_variance.py` and the five-site
cosmological readout-composition packet.
