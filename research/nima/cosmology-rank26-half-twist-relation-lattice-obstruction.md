# Rank 26 survives the physical twist, but its relation lattice does not

## Replicated bounded census

The five-mark product-pole presentation was evaluated with identical cutoff
and pole-depth conventions at the generic counting weight

\[
\gamma=5
\]

and the physical three-dimensional Kummer weight

\[
\gamma=-\frac12.
\]

At both \(p=32003\) and \(p=32009\), the two quotients have dimension 26.
However, in the common 36-dimensional low-numerator space their relation
spaces satisfy

\[
\dim R_5=10,
\qquad
\dim R_{-1/2}=10,
\qquad
\dim(R_5+R_{-1/2})=15.
\]

Consequently

\[
\dim(R_5\cap R_{-1/2})=5.
\]

The equal rank therefore hides a nontrivial change of presentation. Neither
relation space contains the other, so the identity map on numerator
polynomials does not descend to a map between the two rank-26 quotients.

There is nevertheless a source-derived bridge candidate. At both primes, the
same unsplit physical numerator \(q_{g_{23}}+q_{g_{31}}\), under the two
implemented kinematic derivatives, horizontally saturates all 26 dimensions
at both weights:

\[
\dim\langle\nabla^I(q_{g_{23}}+q_{g_{31}})\rangle_{\gamma=5}
=
\dim\langle\nabla^I(q_{g_{23}}+q_{g_{31}})\rangle_{\gamma=-1/2}
=26.
\]

Thus physical specialization changes relations without requiring a new
bounded generator.

## Meaning

The generic \(\gamma=5\) computation correctly establishes the stable
critical-count rank and its labelled Gauss--Manin organization. It does not
by itself provide coordinates in which the physical Leray germ can be
integrated at \(\gamma=-1/2\).

The correct factorization is now

\[
H^2_{\gamma=5}
\xrightarrow{\ C_{5\to-1/2}\ }
H^2_{\gamma=-1/2}
\xrightarrow{\ \operatorname{Per}_{\Gamma_E^{\rm res}}\ }
\mathbb C,
\]

where the first arrow must be a source-derived contiguity, limiting-lattice,
or nearby-cycle comparison. It cannot be replaced by matching coordinate
indices merely because both spaces have dimension 26.

The replicated cyclicity result suggests how to construct it: choose a common
set of 26 source derivative words that is independent in both fibers and map
each generic word to the identical physical word. Canonicity then requires
proving that every relation among source words transports, rather than merely
choosing one convenient word basis.

## Scope

This is a bounded pole-depth-two calculation, not a complete resonant Betti
census. It proves a presentation obstruction, not that the physical twisted
cohomology has exactly rank 26. Higher-pole resonant classes remain possible.

## Next falsifier

Export derivative-word provenance for the common cyclic source and compute
the kernels of the word-evaluation maps in both fibers. A canonical word
transport exists exactly when the generic word relations are carried to the
physical ones (or an explicitly derived homotopy accounts for their
difference). Then test rank 26 and intertwining of all three kinematic
derivatives. Only afterward can the canonical Leray period covector be pulled
back to the generic rank-26 lattice.

Evidence is in
`checkers/check_rank26_half_twist_specialization_gate.py` and the two
prime-indexed result packets.
