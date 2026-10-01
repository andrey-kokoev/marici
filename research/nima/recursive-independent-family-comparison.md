# Recursive independent comparison of promoted families

## Constructor

Let q:E->V be the incoming-family assignment, with F_v=q^-1(v). Promote each
family to a fresh labelled record retaining all of its members. Then select an
ordered pair of family records independently. Its retained comparison members
are the Cartesian product F_v x F_w, with their ordered parent IDs.

This separates the two operations:

    promotion: E -> labelled retained families,
    comparison: (F_v,F_w) -> all ordered member pairs.

Their compatibility law is

    (q x q)^-1(v,w) = F_v x F_w.

Thus grouping first and independently comparing the families gives exactly the
same next relation as comparing every record pair and then grouping by the pair
of target endpoints. It also supplies the promoted record's next endpoints:
ordered pairs of the prior source/target endpoints, with original members retained.

Both routes preserve multiplicity and identities. Cardinalities obey
|F_v x F_w|=|F_v|*|F_w|. This law justifies product member counts where means are
formed over the comparison members. The checker tests membership and counts;
no new scalar response function or transaction scheduling is introduced here.

## Same rule applied twice

The implementation starts with the primitive arrow relation and applies this
constructor twice. A comparison record has an ordered tuple of primitive origins;
its immediate parent pair is retained. Fixed-length tuples distinguish repeated
origins occupying different operand positions.

| Primitive relation | Stage0 arrows | Stage1 arrows | Stage2 arrows |
|---|---:|---:|---:|
| Full off-diagonal | 12 | 144 | 20736 |
| Arrow(0,1) omitted | 11 | 121 | 14641 |

The operand arities are1,2,4. Incoming-family counts are4,16,256 for either
input. Every possible ordered primitive-arrow tuple of the given arity appears
exactly once. Both grouping/comparison squares commute by exact record equality.
The auxiliary16 state-pair slots of the earlier137-slot fixture are outside this
arrow-relation constructor; their recursive role remains to be specified.

## Independence witnesses

For the full relation, fix all source coordinates except one at label0, and
vary the remaining coordinate over the four tetrahedron vertices. The oriented
tetrahedron boundary is a2-cycle in the product Dowker complex. Repeating this
for each operand coordinate gives1,2,4 explicit sphere cycles.

Their evaluations under the corresponding coordinate projection cocycles form
a diagonal matrix with nonzero entries. This proves the displayed classes are
independent, including at the four-operand stage. The previously proved product
identification gives the matching upper bound. Its Poincare polynomials are

    1+t^2,
    1+2t^2+t^4,
    1+4t^2+6t^4+4t^6+t^8.

The four-operand homology statement follows from the product theorem and these
witnesses; the exponentially large simplicial chain matrices are not enumerated.

For the omitted-arrow input, all independent tuple choices still exist. Each
coordinate sphere is missing one triangular face. Its Dowker factors are disks,
so positive-degree absolute homology remains zero. Independent operand selection
and survival of sphere classes are separate requirements.

## Architectural result

There is now an explicit recursive operation compatible with retained-family
promotion that produces the product recurrence. The new independently selected
comparison operand supplies the factor growth. Fresh labelling supplies its
addressability, and the fibre law makes the order of grouping and comparison
irrelevant at the record level.

Independent all-pairs comparison is a declared addition to the architecture.
The earlier grouping-only rule does not select it. Gauge assignments and the
reference policy still require their own identification.

The subsequent [reference-semantics audit](reference-semantics-carrier-versus-counted-domain.md)
locates the exclusion in the counted comparison view while the direct reference
is retained. The full marked carrier already keeps its sphere. The next adapter
must connect that direct reference to the local marks and comparison legs;
no boundary restoration is required merely to retain the full-carrier classes.

## Verification

    python research/nima/checkers/check_recursive_independent_comparison.py

Checks both input relations through two successive comparisons, exact equality
of the grouping/comparison routes, complete tuple coverage, parent provenance,
product family counts, closed coordinate sphere chains, independent projection
evaluations, and missing-facet controls. Exact integer/Fraction arithmetic.
