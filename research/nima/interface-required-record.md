# Growth required by an actual unresolved interface: one exterior record

## Question

Instead of refining every face, identify information that an existing operation actually needs at a chosen boundary. Use the established two-block AB/BA interface adjacent to OAB, with the same twelve-triangle collective projector. No new interaction or spatial attachment is introduced.

This is an observation/response boundary, not a missing geometric face or an uninhabited type-theoretic horn. The complete global state already contains the missing information; it is missing only from the proposed local active view.

## Actual failure of local closure

On transported local-mode coefficients the existing operator is M, with M_ij=1/12. Let q retain only the two selected interface coefficients a,b.

Two full states can have the same q-value but different next q-values. Compare zero input with an input having coefficient one on a single exterior triangle. Both have interface value (0,0), while their next interface values are respectively

    (0,0),    (1/12,1/12).

Therefore qM does not factor through q. There is no autonomous update on the two coefficients reproducing this actual global operation for every admitted coefficient state.

This is the unresolved boundary: interface data alone is insufficient to calculate its next response.

## The source operation selects the missing record

The exterior-to-interface block is a 2-by-10 matrix with all entries 1/12 and rank one. Thus at least one additional scalar coordinate is needed in a linear sufficient interface representation. One is sufficient: retain the mean s of the ten exterior coefficients.

The exact extended active state and update are

    (a,b,s) -> (m,m,m),
    m=(a+b+10s)/12.

If T extracts (a,b,s) and U is this three-variable update, the source satisfies the exact commuting identity

    T M = U T.

Hence the update remains valid under repeated applications of this fixed operator, by induction; the checker uses the operator identity, not longer body executions. The extra one-dimensional information is selected up to a coordinate reparameterization, not a unique normalization-free variable name.

Unlike the subdivision rule, this extension is required by the demonstrated failure of the smaller observer. Unlike the earlier nonlinear covariance proposal, its coupling coefficients come directly from the existing source matrix.

## Retain everything outside the active view

The ten exterior values are recovered as s+r_i, with sum r_i=0. Their nine independent contrasts remain in retained records. Together with a,b,s, this is a lossless re-presentation of the twelve-coefficient state, not an assertion that three numbers recover everything.

The counting norm separates as

    ||x||^2=a^2+b^2+10s^2+sum_i r_i^2

for the real coefficient control. The same decomposition extends with absolute squares to complex coefficients. This is a norm identity, not norm conservation by the projector. The active three-variable operator is self-adjoint in metric diag(1,1,10) and remains a projection.

This applies the existing mean/fluctuation-retention principle to a source-specified interface. A native implementation would still require the actual package adapter and rule admission; this numerical commuting square is not itself an Agda construction of that adapter.

## Closing the exterior response does not generate the proposed electron

Block the existing M as [[A,B],[C,D]]. The exterior uniform eigenvalue is 10/12=5/6, and its contrasts have eigenvalue zero. Solving the stationary exterior equation gives

    x_ext=(I-D)^-1 C x_interface,
    M_eff=A+B(I-D)^-1 C = [[1/2,1/2],[1/2,1/2]].

The inverse and response are exact; no guessed stiffness or fitted gain is inserted. Stationary elimination is a diagnostic of this particular map, not a gravitational energy minimization or an assertion that the physical system equilibrates instantaneously.

The symmetric interface combination closes into the same collective background. The antisymmetric combination (1,-1) is still mapped to zero. Thus environmental closure supplies the needed relational record but does not turn the prior hidden contrast into a bound particle.

## Natural progression actually supported here

    local interface records
        -> detect failure to determine their next response
        -> retain the one missing exterior aggregate
        -> carry its response together with all residual history.

This is growth of an adequate local state description, not a new tetrahedron, new global degree of freedom, or an electron identification. Its minimality is relative to the chosen two-block observer, linear representations and the existing projector. Other observation profiles or operations can require other records.

## Verification

`python research/nima/checkers/check_interface_required_record.py` passes exact rational tests of the counterexample, rank-one exterior dependence, commuting update, full-state reconstruction, norm decomposition and stationary Schur response. Receipt: `results/interface-required-record.json`. No previous source operation, physical calibration, native rule or ledger entry was changed.
