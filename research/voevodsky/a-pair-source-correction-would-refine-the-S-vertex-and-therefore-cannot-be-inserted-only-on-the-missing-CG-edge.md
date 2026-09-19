# A pair-source correction would refine the S vertex and cannot be inserted only on the missing CG edge

The only located source shape capable of supplying a new divisor-surviving
history correction is the ordered-pair response.  It requires a linearized
source coproduct and pair incidence

\[
U_{\rm ar}\xrightarrow{\Delta_{\rm pair}}U_{\rm pair}
\xrightarrow{B_{\rm rad}}\mathcal G_{\rm pair,rad}.
\]

This cannot be simulated by reweighting an existing scalar port.  The radial,
Wronskian, and endpoint responses are bilinear in the theta inputs and become
linear only on a tensor/density/Fock-square carrier.  The present arithmetic
incidence is linear on `U_ar`; the two constructors have different arity.

In the 4-simplex architecture this has a further consequence.  Adding
`Delta_pair` is not merely a new map on the missing `CG` edge.  It refines the
source filtration stage itself:

\[
S\rightsquigarrow S_{\rm pair}.
\]

Hence every interval incident to `S` changes:

\[
X_{SA},\quad X_{SC},\quad X_{SG}.
\]

The three faces `SAC`, `SAG`, and `SCG` must then be reconstructed and compared
with their old versions.  Inserting the pair response only into `X_CG` would
violate the shared-face rule: the proposed tetrahedra would no longer restrict
to identical source triangles.

A valid pair-source repair therefore needs a refinement morphism of
filtrations, not a patch to one residual equation.  It must provide:

1. a source-authorized linear coproduct `Delta_pair`;
2. compatibility with prime/grade labels and the Xi-adic filtration;
3. refined intervals `X_(S_pair A)`, `X_(S_pair C)`, and `X_(S_pair G)`;
4. comparison maps from the original three source intervals;
5. reciprocal duality and cofiber compatibility on all affected faces;
6. only then, a corrected `CG` mate.

No such coproduct is currently present.  The pair route remains a genuine new
constructor candidate, but adopting it restarts the boundary data of the
middle facet rather than filling the existing horn in place.
