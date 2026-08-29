# Crossing is a clutching wall between two spectral-coherence three-cubes

## Dimensional correction

Cutoff, parameter, reciprocal, and contour crossing cannot all be called the directions of an ordinary cube. Four independent edge directions generate a 4-cube. The cleaner typing is instead:

- cutoff \(c\), parameter \(a\), and reciprocal \(r\) are edge directions;
- crossing is a codimension-one wall carrying a clutching 2-morphism.

Let \(\mathcal C_-\) and \(\mathcal C_+\) be the contour-admissible 3-cubes on the two sides of a crossing stratum. Each cube has vertices indexed by \(\{0,1\}^3\), twelve edge transports, six square comparison cells, and one cube-coherence equation.

At every corresponding vertex \(v\), the wall supplies a finite crossing complex \(E_v\) and determinant clutch
\[
\kappa_v:
\operatorname{Det}(T^-_v)
\longrightarrow
\operatorname{Det}(T^+_v),
\]
factored through transfer of \(\det(E_v)\) between the defect and invertible-complement determinant factors.

## Audit hierarchy

The coherence audit has five typed levels.

### 1. Edge transport

Every \(c\), \(a\), and \(r\) edge carries source-authorized transport on the defect complex and relative determinant line.

### 2. Square curvature

For each pair \((c,a)\), \((c,r)\), and \((a,r)\), the two boundary composites of the square are compared. Nonidentity gives the first curvature residual.

### 3. Cube coherence

On each side, the six square comparisons must satisfy the boundary identity
\[
\prod_{f\subset\partial\mathcal C_\pm}\Omega_f^{\epsilon(f)}=I,
\]
with order and signs fixed by the oriented cubical boundary. This is coherence among the square coherences, not another edge holonomy.

### 4. Clutching naturality

For every edge and square \(F\) of the 3-cube, the clutching maps must intertwine the minus and plus transports:
\[
\kappa_{\partial_1F}\,T^-_F
=
T^+_F\,\kappa_{\partial_0F},
\]
with the determinant transfer factor included. These equations say that the wall is a natural transformation between the two cubical transport systems.

### 5. Final four-dimensional compatibility

The two 3-cubes and all clutching prisms form the boundary of a 4-dimensional coherence cell. Its ordered boundary product
\[
\mathfrak A_4
=
\prod_{G\subset\partial I^4}\Theta_G^{\epsilon(G)}
\]
must equal the identity.

The terms \(\Theta_G\) are cube comparisons or clutching-cube comparisons, not scalar edge transports. Therefore \(\mathfrak A_4\) is a higher obstruction.

## Classification of the final residual

- If \(\mathfrak A_4=I\), the crossing wall coherently couples charge, determinant phase, and reciprocal transport.
- If \(\mathfrak A_4\) is central but nontrivial, it defines a determinant-gerbe or anomaly class. It must not be demoted to holonomy of an ordinary determinant line.
- If \(\mathfrak A_4\) is noncentral, the completion is immediately incoherent: different orders of cutoff, continuation, reciprocity, and crossing act differently on the finite crossing data.

A scalar phase can therefore appear at two categorically distinct levels. Line holonomy is a one-dimensional transport invariant. A central four-cell residual is a coherence anomaly one level higher. Equality of their numerical values does not identify their types.

## Zero-charge region and wall

Away from the crossing wall, the RH component has \(\mathcal D=0\), so defect transport is trivial and the side cubes reduce to relative determinant transport on the invertible complement. At the wall, however, \(E_v\) can be nonzero. The clutching system must account for its algebraic multiplicity and, when authorized, its orientation. Thus zero charge on both open sides does not permit erasing the finite crossing complex at the wall.

For an RH exclusion proof, the desired admissible component must avoid such a wall entirely. The wall construction remains the hostile first-crossing witness: if exclusion fails, it records exactly where charge is created and how the determinant section acquires its zero.

## Reciprocal orientation gate

Reciprocal transport maps a crossing at \(s_0\) to one at \(1-s_0\). The \((r,\text{wall})\) clutching naturality cell must specify whether
\[
E_{s_0}\longmapsto E_{1-s_0},
\qquad
\det(E_{s_0})\longmapsto \det(E_{1-s_0})
\]
preserves or dualizes orientation. Without this typed map, reciprocal equality of scalar zero orders does not establish coherent pairing of crossings.

## Hostile checks

1. **Dimension collapse.** Four edge directions are mislabeled as a 3-cube.
2. **Wall-as-edge confusion.** A determinant clutching morphism is treated as ordinary transport.
3. **Face-only audit.** All square cells commute, but cube coherence is never checked.
4. **Cube-only audit.** Both side cubes cohere, but clutching is not natural across faces.
5. **Gerbe demotion.** A central four-cell residual is recorded as ordinary line phase.
6. **Noncentral concealment.** A basis-dependent residual is scalarized by taking its determinant.
7. **Wall erasure.** Zero defect rank off the wall is used to delete the finite crossing complex.
8. **Reciprocal orientation loss.** Paired multiplicities are asserted without determinant-factor transport.

## Next constructor

Encode the audit as a normalized cubical cocycle. Edge data are degree one, square residuals degree two, cube coherence degree three, and the wall compatibility residual degree four. The categorical RH gate should require:

1. vanishing degree-two defect curvature;
2. vanishing degree-three side-cube obstruction;
3. natural determinant clutching across the crossing wall;
4. trivial degree-four anomaly class on the admitted source-generated component.

This gives a dimensionally typed obstruction tower in which no higher anomaly can be silently renamed as another determinant phase.
