# The uniform seventh edgewise subdivision is well-typed for signed asymptotic realizations but not for positive feature realizations

## Two target categories must be distinguished

The phrase "uniform eight-node tetrahedral refinement" has two different meanings.

### Signed asymptotic realization category

Let

\[
\mathsf{Real}_S^{asym}
\]

contain observer-indexed Hermitian forms, distributional pairings, affiliated-operator pairings, and cutoff families modulo the rapid-decay ideal.

Morphisms are realization comparisons preserving the observer label, and 2-morphisms are equalities/modifications in the rapid-decay quotient.

In this category:

- the Hardy--Titchmarsh transform supplies `H_123`;
- Connes's cutoff theorem supplies `H_124`;
- Fourier/Mellin transport of `M_(-log|x|_S)` supplies `H_134`;
- faithful whiskering along the integrated representation uniquely recovers `H_234`;
- Connes's rapidly decreasing remainder makes that recovered face analytically admissible.

Thus there is a signed asymptotic homotopy-coherent simplex

\[
\boxed{
\Phi_S^{asym}:
\Delta^3
\longrightarrow
N_{hc}(\mathsf{Real}_S^{asym}).
}
\]

### Positive feature category

Let

\[
\mathsf{Real}_S^{+}
\]

require actual Hilbert feature maps, positive operators/compressions, bounded or controlled affiliated correspondences, and positive 2-cells before scalar trace.

In this category:

- `P_Lambda hat P_Lambda` is not positive or self-adjoint;
- `M_(-log|x|_S)` changes sign;
- the direct outside-from-inside layer contraction is not well-defined;
- the Sonin common-gap sector prevents a naive Fourier-doubled contraction;
- no completed positive tetrahedral filler is known.

Therefore no map

\[
\Delta^3
\to
N_{hc}(\mathsf{Real}_S^+)
\]

has yet been constructed.

## Why equal edge levels need not denote equal object types

The seventh edgewise subdivision is functorial. Once `Phi_S^asym` exists, define

\[
\boxed{
\operatorname{esd}_7(\Phi_S^{asym}):
\operatorname{esd}_7(\Delta^3)
\longrightarrow
\operatorname{esd}_7
N_{hc}(\mathsf{Real}_S^{asym}).
}
\]

This construction does not identify level `j` on one edge with level `j` on an opposite edge. It only subdivides each existing comparison and transports the face/tetrahedral coherence functorially.

Hence the following mismatch is harmless in `Real_S^asym`:

\[
C_{13,j}
\ne
C_{24,j}.
\]

The objects are different presentations connected through subdivided face and interior comparison data. They are not barycentric mixtures.

## Role of identity and degeneracy nodes

A seven-stage edge factorization may contain fewer than seven substantive analytic operations. To place it in the uniform subdivision, insert identity transformations at the unused levels.

Such a node is a simplicial degeneracy:

\[
X
\xrightarrow{\operatorname{id}}
X.
\]

It does not assert that unlike Hilbert, distribution, and trace objects are equal. It only pads one already typed factorization inside the same realization category.

Thus a uniform combinatorial subdivision does not require a uniform semantic operation at every level.

## Count in the signed category

The seventh edgewise subdivision of a 3-simplex has

\[
7^3=343
\]

top-dimensional elementary tetrahedra.

The rapid-decay propagation checker verifies that all translated cutoff faces remain negligible for positive cutoff exponents. Therefore

\[
\boxed{
343/343
\text{ elementary tetrahedra commute in }
\mathsf{Real}_S^{asym}.
}
\]

This is an equality/modification count, not a positivity count.

## Why the same conclusion does not lift to positive features

The forgetful/scalarization functor

\[
\mathsf{Real}_S^+
\longrightarrow
\mathsf{Real}_S^{asym}
\]

forgets precisely the data needed for positivity:

- kernels of feature maps;
- ordering of noncommuting cutoff projections;
- contraction norms;
- the Sonin harmonic summand;
- boundary sewing before trace.

Commutativity after this forgetful functor does not imply a positive lift.

Accordingly,

\[
\boxed{
0/343
\text{ elementary tetrahedra are certified in }
\mathsf{Real}_S^+.
}
\]

## Uniform versus nonuniform decision

### Signed asymptotic objective

For equality of realization functors modulo rapidly decreasing cutoff errors:

\[
\boxed{
\text{the uniform eight-node refinement is well-typed and sufficient}.}
\]

No nonuniform refinement is forced. Identity/degeneracy stages may pad shorter edges.

### Positive rung-four objective

For a positive Hilbert-feature realization before trace:

\[
\boxed{
\text{the current uniform eight-node refinement is not yet well-typed}.}
\]

The obstruction is not the number eight by itself. It is the absent Fourier-coupled Sonin/boundary feature and its contraction. Once that object is constructed, it may fit into the existing levels by degeneracies; if it requires separate projection, quotient, and boundary-sewing operations, a nonuniform common refinement will be necessary.

The decision is sharpened by the outside-leg trace-ideal audit: a second physical cutoff and a common Eisenstein/radical quotient are substantive positive stages. Hence the current eight-node route is insufficient. A ten-node common refinement is the first explicit sufficient candidate, although minimality is not claimed.

## Updated status of `C_34`

The former operator-typing gap on `C_34` has been partially closed:

\[
V_{loc,S}
\xleftrightarrow{\text{Mellin/Fourier}}
M_{-\log|x|_S}
\xrightarrow{\text{observer pairing}}
W_S.
\]

This is an affiliated/distributional operator lift, stronger than scalar endpoint equality.

What remains missing is not the existence of a common operator, but a **positive feature lift** connecting its two spectral-sign towers to the physical/Fourier cutoff pair while retaining the Sonin boundary sector.

## Final inventory

| Layer of structure | Certified cells | Meaning |
|---|---:|---|
| universal horn algebra | `343/343` | formal unique recovery under invertible whiskering |
| observer-generated face recovery | `343/343` | actual faithful semilocal whiskering |
| signed analytic asymptotic category | `343/343` | Connes remainder vanishes modulo rapid decay |
| positive Hilbert-feature category | `0/343` | contraction/boundary sewing not constructed |

## Disposition

The original uniform-refinement question now has a two-level answer:

\[
\boxed{
\text{yes for signed asymptotic coherence; no current proof for positive feature coherence}.}
\]

The next construction should target the regulated asymptotic feature decomposition and Eisenstein/radical quotient, followed by the Sonin-sector boundary sewing map. The resulting extra nodes are typed regulator/quotient stages, not arbitrary barycentric mixtures.
