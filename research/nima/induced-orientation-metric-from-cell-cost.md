# Inducing orientation metrics from retained comparison-cell costs

## Which record layer supplies the cost?

In a comparison chain complex, a degree2 class is represented by a closed
2-chain z: d2*z=0. Pulling an edge-edit cost Q1 back along that boundary gives

    Q1(d2*z)=0.

Thus the boundary action on lower member/edge records cannot assign a positive
cost to these classes. A cost on retained comparison-cell data, or another
specified coupling to member data, is required. This applies equally to the
biclique and Dowker chain descriptions; their edge bases are different.

The calculation below assigns unit Euclidean cost to the oriented triangle
records of the Dowker complex. It then derives, rather than independently
chooses, the minimum representative cost of each homology coordinate.

## Explicit harmonic representatives

For n independently compared full primitive carriers, source vertices are
n-tuples of four labels. Every set of three distinct product vertices is a
Dowker triangle. For a triangle sigma and coordinate i, define epsilon_i(sigma)
as its projected oriented tetrahedron-boundary coefficient when the three
projected labels are distinct, and zero otherwise.

Let N=64^(n-1). The normalized chain

    z_i(sigma) = -epsilon_i(sigma)/N

has period1 on the selected primitive triangle(0,1,2) in factor i and period0
on the other factors. The sign reflects the fixed tetrahedron orientation.

It is a cycle: at any edge whose two projected labels differ, the two possible
remaining projected labels contribute opposite boundary signs with identical
other-coordinate multiplicities. If those labels agree, the contribution is
zero. It is orthogonal to all3-boundaries because epsilon_i is the pullback of
a closed primitive2-cochain. Hence z_i is the minimum-unit-cell-cost representative
of its homology class. The product theorem gives all n independent classes.

For each of four primitive faces, the other n-1 coordinate triples can be
chosen in(4^3)^(n-1)=N ways. The support size is4*N, so

    ||z_i||^2 = 4/N.

Different coordinate representatives are orthogonal: a primitive odd permutation
flips one and preserves the other, while preserving the triangle metric.
Therefore the induced homology-coordinate metric is

    M_n = (4/64^(n-1))*I_n.

| Number of factors | Induced unit-triangle cost scale |
|---:|---:|
| 1 | 4 |
| 2 | 1/16 |
| 4 | 1/65536 |

Ranks1 and2 are computed using full exact chain matrices. Rank4 uses the support
count and product proof, with local cycle/cocycle checks; its entire matrix is
not materialized.

## Return contract and scale propagation

At a fixed rank M_n is a scalar multiple of identity. A linear differential
request a^T delta_h=d therefore has the same class-coordinate least-change
return as in the earlier Euclidean test:

    delta_h=d*a/(a^T a).

Its cell implementation is sum_i delta_h_i*z_i. The checker verifies the period
constraint and the induced cost. Adding a3-boundary preserves the class but
increases cost by its squared norm, since the harmonic lift is orthogonal to it.

The scale changes sharply with factor count under fresh unit triangle costs.
More redundant triangle representatives permit a lower-cost distributed lift.
Forcing the additive cross-rank class budget with constant scale4 requires
transporting triangle weights as64^(n-1). This follows from the derived scale
once that budget law is imposed; it is an additional cost policy.

## Presentation control

The same primitive sphere has six rectangle2-cells in its bipartite incidence
presentation and four triangle2-cells in its Dowker presentation. Its primitive
integral cycle has unit coefficients in either presentation. Fresh unit costs
give squared class norms6 and4 respectively. Homology equivalence therefore
does not automatically transport the edit metric.

This is the higher-cell analogue of the earlier family-mean result: retaining
content and reindexing it is compatible with a metric, but assigning fresh equal
weights to a different presentation changes the return geometry.

## Structural result

The proposed orientation-return metric can be induced from explicit higher-cell
costs. The original boundary-mediated leaf cost supplies zero on these closed
classes. A full architecture must therefore retain comparison cells as costed
records or declare another observable action on lower records.

The next metric-coherence test is an explicit weighted chain comparison between
the rectangle and triangle presentations. It should preserve the normalized
class cost while recording any discarded or orthogonal cell-level components.

## Verification

    python research/nima/checkers/check_induced_orientation_metric.py

Exact period normalization, zero boundary, orthogonality to3-boundaries, Gram
matrices, least-change differential lifts, boundary-perturbation cost, primitive
rectangle/triangle discrepancy, rank4 support counts and local identities,
and the weighting required for an additive cross-rank class budget.
