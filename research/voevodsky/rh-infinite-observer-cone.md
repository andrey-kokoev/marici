# RH as an infinite observer cone

## Question

Does final RH closure require infinitely many observers for infinitely many source-derived identities?

## Claim boundary

The answer concerns the shape of a faithful criterion. It does not establish the required positivity transformation.

## Two equivalent observer families

For an even completed spectral distribution \(\rho\), define heat-jet observers

\[
J_{k,t}(\rho)=
\langle\rho,u^{2k}e^{-tu^2}\rangle,
\qquad k\geq0,
\quad t>0.
\]

The positivity requirement is

\[
J_{k,t}(\rho)\geq0
\]

for every pair \((k,t)\).

Alternatively, fix one \(\sigma>0\). For every finite real translate packet \(A=(a_1,\ldots,a_n)\), define

\[
G_{\sigma,A}(\rho)_{ij}
=
\langle\rho,
e^{-2\sigma u^2}e^{-i(a_i-a_j)u}
\rangle.
\]

The requirement is positive semidefiniteness for every packet size and every packet.

The Bernstein and Bochner reductions prove that these two infinite families are jointly faithful and equivalent.

## Observer index category

Let an object be a finite set of requested heat jets and Gram packets. A morphism is inclusion of observer sets. Each object defines a finite positivity cone \(C_F\), and refinement gives

\[
F\subseteq F'
\quad\Longrightarrow\quad
C_{F'}\subseteq C_F.
\]

The faithful positive cone is the inverse intersection

\[
C_+=\bigcap_F C_F.
\]

Prior hostile fixtures prove that no bounded stage equals \(C_+\): finite derivative order, finite parameter sampling, and bounded matrix rank are each nonfaithful.

## Coherence among observers

The observers are not independent. They satisfy source-derived identities such as

\[
J_{k+1,t}=-\partial_tJ_{k,t},
\]

restriction and permutation naturality of Gram matrices, and equality between coincident even character jets and heat derivatives at \(t=2\sigma\).

Final closure therefore requires a coherent cone over infinitely many observers, not infinitely many unrelated numerical verifications.

## Relation to the pyramids

This observer cone is the base of the positivity pyramid. It is not a fourth pyramid because it introduces no new apex object. The analytic and arithmetic pyramids both map to the same \(\rho\); the positivity pyramid asks whether \(\rho\) factors through this observer-limit cone.

## Proof compression

A valid proof should not enumerate observers. It should construct one source-derived positive measure or Gram transformation whose naturality generates every observer identity uniformly. That single transformation would fill the cross-pyramid positivity cell and discharge infinitely many consequences at once.

## Disposition

The operator's hypothesis is correct after this qualification: infinitely many observers are necessary at the criterion level, but the proof should be one uniform coherent constructor. The missing datum remains that constructor for the coupled endpoint–gamma–prime arithmetic apex.
