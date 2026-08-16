# dP6 Boundary-Only Q-Lift No-Go and the Interior Kernel Gate

## Outcome

The oriented dP6 construction of entry 249 canonically closes the six local
boundary corridors, but its literal target is the road subobject

\[
P=F_B/F_V\longrightarrow E=F_K/F_V.
\]

Consequently every boundary column has zero image under the quotient
\(E\to Q=F_K/F_B\).  Entry 143 independently retains the nonzero generic norm
\(q_\Sigma=(1,1,1)\in Q\), with augmentation three.  Therefore no integral
linear combination of the twelve dP6 boundary columns can realize the required
generic comparison.  This is the first exact failure of a boundary-only
six-functor lift; it is not a no-go for an enlarged log/nearby-cycle kernel.

The executable checker verifies rank zero for the boundary image in \(Q\), the
nonvanishing and augmentation of \(q_\Sigma\), and the empty boundary-only
solution.  Adjoining one based interior column with value \(q_\Sigma\) repairs
the coefficient presentation primitively (Smith factor one), but does not
construct its geometry.

## Minimal additional datum

One needs an interior-supported mixed-variance transformation

\[
\Phi_{\mathrm{int}}:\mathcal S_{\rm sh}^{\rm norm,reg}
  \longrightarrow E_{\partial,Q}^{\rm BM,\check C}
\]

whose associated \(Q\)-grade sends the normalized dP6 disk/top to the based
class \(q_\Sigma\), while its boundary is the already constructed twelve-edge
map in \(P\).  Equivalently, this is the missing boundary-crossing
Beck--Chevalley cell in the square

\[
\begin{array}{ccc}
N_{\rm road}&\longrightarrow&P\\
\downarrow&&\downarrow\\
\langle q_\Sigma\rangle&\longrightarrow&Q.
\end{array}
\]

It must also carry the reciprocal-regular normalization provenance and the two
endpoint comparison cells required by entry 158.  Until that map exists, the
endpoint/Q mapping fiber is uninstantiated and the physical
\(p_{\partial,Q}\), its Bockstein, and downstream \(D_8\)/Jordan coherence are
undefined.

## Evidence

- `research/voevodsky/check_dp6_boundary_only_q_lift_no_go.rs`
- entry 143, especially the filtration \(0\to F_B/F_V\to E\to Q\) and the
  zero \(Q\)-image of literal half-corridors;
- entry 158, definition and missing-data boundary for the endpoint/Q mapping
  fiber;
- entry 249, normalization-provenanced oriented dP6 boundary construction.

```json
{
  "status": "falsified_scoped_boundary_only_q_lift",
  "boundary_edges": 12,
  "boundary_Q_rank": 0,
  "qSigma": [1, 1, 1],
  "qSigma_augmentation": 3,
  "boundary_only_solution": "EMPTY",
  "minimal_coefficient_extension_columns": 1,
  "augmented_smith": [1],
  "interior_mixed_variance_kernel_constructed": false,
  "mapping_fiber_instantiated": false,
  "physical_p_defined": false,
  "physical_bockstein_defined": false,
  "D8_Jordan_tested": false,
  "graph_admission_claimed": false
}
```
