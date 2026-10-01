# Joint context incidence from promoted-value composition

## Source obligation and scope

The active obligation is source-operation realization followed by
route/coherencer compatibility. Use the actual endpoint keys, retained leaves,
and two horizontal candidates in `check_rung_transport_diagram.py`, not a new
row/column partition of the137 matrix slots.

Both candidates first form32 incoming families. In the second promotion,
retaining distinct inherited target keys leaves32 families; assigning a common
target merges them into one. Both retain all137 leaves and give the same weighted
first-moment response relative to the fixed rung4 reference.

We now apply a declared **promoted-value self-composition probe**: compose each
promoted matrix value C_F with itself through r=d4^-1 and average by family mass.
This operation is well-typed. It is a diagnostic of the candidate generators,
not an assertion that self-composition is the selected physical successor.

## Product coefficients follow from the source operation

Let leaf i have mass m_i, total mass M, and family F have mass M_F. The promoted
matrix value in the existing fixture is

    C_F = sum_(i in F) (m_i/M_F) C_i.

Therefore the promoted-value composition readout expands exactly as

    sum_F (M_F/M) C_F r C_F
      = sum_(j,i) pi_ji C_j r C_i,

    pi_ji = m_j*m_i/(M*M_F) if i,j belong to the same final family F,
            0 otherwise.

This supplies a concrete leaf-pair incidence: the fiber product of retained
membership over the final families. Both marginals are the original leaf masses
m_i/M. Coefficients telescope through nested retained families, so direct leaf
expansion and staged conditional expansion agree. Passive source/target indexing
does not change the leaf-labelled incidence.

**No physical statistical-independence assumption was used in this expansion.**
The product coefficients follow algebraically from composing weighted family
means. Choosing to compose those means, rather than the full member packets,
is the explicit source-operation choice. The expansion introduces operand
occurrences of existing leaves, not independently variable physical copies.

## A new discriminator for the two horizontal candidates

With unit leaf masses, the32 first families have sizes

    sixteen singletons, one family of4, six families of6, nine families of9.

The two policies therefore induce different pair supports:

| Horizontal policy | Final families | Supported ordered leaf pairs |
|---|---:|---:|
| Inherited target keys |32|977|
| Common target |1|18769 =137 squared|

The exact matrix readouts differ even though their original means agree.
Writing mu for the common mean and F for the first families, the difference is

    sum_F (M_F/M) (C_F-mu) r (C_F-mu).

This is the ordered between-family covariance. It is nonzero in the actual
shared-leg fixture, under both unit and positive nonuniform leaf masses.
Subtracting the same fixed reference d4 does not remove it.

Thus the previously first-moment-indistinguishable endpoint policies can be
separated by a subsequent valid comparison operation. This does not select
which policy is physical, but gives a concrete test any proposed selection must
answer. Pair counts are support sizes for this probe, not field counts or costs.

## Three distinct operations, not two interchangeable normalizations

1. **Compose each retained member before averaging:** diagonal leaf incidence.
2. **Compose each promoted family mean:** conditional pair incidence within that
   final family, derived above.
3. **Compose the total mean:** global product incidence over all leaves.

The difference between1 and2 is within-family covariance. The difference between
2 and3 is between-family covariance. Their sum is the full correction from the
mean/fluctuation packet law. Both identities are checked in the actual fixture.

In particular, the earlier packet checker grouped by leg-slot indices to test
its general identity. The present checker instead uses the actual carrier
source/target endpoint keys of the rung fixture and recovers its32 families.
These are different partitions; their group counts must not be conflated.

## What is now derived, and what is still an input

Given the promoted-value operation and a specified endpoint policy, its joint
leaf incidence and weights are determined. They are no longer a free measure
chosen to repair the readout square. The previously missing choice has been
localized to the source constructor:

- which family ports does it compose?
- does it compose promoted matrix values or retained member responses?
- which next-level endpoints determine those families?

The architecture's retention requirement alone does not answer those questions.
No gauge identification, physical sampling law, normalization or1,2,4 successor
identification follows from this conditional expansion.

## Verification

    python research/nima/checkers/check_promoted_context_incidence.py
    python research/aspect/scc/scc.py check nima-promoted-context-incidence

Exact rational tests of direct/staged leaf coefficients, family masses and both
marginals, passive retained-index covariance, matrix expansion, first-moment
agreement and second-order separation, and within/between covariance accounting.
The machine-readable result is `research/nima/results/promoted-context-incidence.json`.
