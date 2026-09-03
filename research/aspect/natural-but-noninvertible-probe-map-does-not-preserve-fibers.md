# A natural but noninvertible probe map does not preserve fibers

## Question

Does restriction naturality alone preserve matching-map fibers, or is componentwise invertibility separately necessary?

## Claim boundary

This packet gives a finite countermodel on the full two-probe face system. It isolates invertibility in the local fiber-equivalence theorem. It does not assert that every natural transformation should preserve multiplicity or that natural isomorphism implies global rewrite confluence.

## Two lawful presheaves

Use the faces

\[
\varnothing,\quad \{p\},\quad \{q\},\quad \{p,q\}.
\]

For both presheaves, assign a singleton to the empty and singleton faces. At the joint face assign

\[
F(pq)=\{a,b\},
\qquad
G(pq)=\{c\}.
\]

Every proper restriction is the unique map to a singleton. Both presheaves satisfy identity and composition laws.

## Natural transformation

Define \(\alpha:F\Rightarrow G\) by the identity map on every proper singleton face and by

\[
\alpha_{pq}(a)=c,
\qquad
\alpha_{pq}(b)=c.
\]

Every naturality square commutes: both routes from either joint section to a proper face end at its unique element. The joint component is surjective but not injective, hence not an isomorphism.

## Matching fibers

For each presheaf, the matching object is the singleton compatible family \((*,*)\). The matching maps are the unique maps

\[
\mu_F:\{a,b\}\to\{(*,*)\},
\qquad
\mu_G:\{c\}\to\{(*,*)\}.
\]

Their fibers over the unique matching datum have cardinalities two and one. The natural transformation induces the collapse

\[
\{a,b\}\longrightarrow\{c\},
\]

which is not a fiber equivalence.

## Consequence

Naturality supplies compatibility with restriction; it does not supply reversibility. The local rewrite theorem therefore needs both:

1. naturality, to conjugate restriction structure;
2. invertibility, to turn the induced fiber map into an equivalence.

A natural noninvertible map may still represent a lawful abstraction, quotient, or information-losing compilation step. It must not be classified as a reversible probe rewrite.

## Disposition

The countermodel rejects the rival claim that naturality alone preserves extension multiplicity. Componentwise invertibility is independently necessary for the stated matching-fiber equivalence theorem.
