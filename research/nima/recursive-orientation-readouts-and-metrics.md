# Recursive orientation systems, readouts and metrics

## Transport through the comparison tree

The rank1,2,4 spaces are the degree2 homology coordinates of the full primitive
relation and its successive independent comparison products. Each primitive
context relabelling acts by its tetrahedron orientation sign. Under products,
these give independent sign actions on the coordinate classes.

Two symmetry contracts are tested:

1. Retain the ordered operand roles: independent signs only.
2. Also allow interchange of the two operands at any node of the binary
   comparison tree: signs together with binary-tree automorphisms.

The second contract exchanges whole subtrees while preserving the comparison
hierarchy. It does not require arbitrary permutations of all leaves. Its signed
action groups have orders2,8,128 at ranks1,2,4. Primitive orientation signs and
all pairs of these signed tree actions satisfy composition exactly.

Operand exchange is an explicit architectural symmetry choice. The earlier
ordered record constructor retains enough provenance to distinguish the roles.

## Linear readouts and quadratic metrics

Independent sign reversals force every invariant linear scalar readout to zero.
For a quadratic form x^T M x, they force all off-diagonal entries of M to vanish.
Thus labelled operands permit n independent diagonal weights at rank n.

Tree automorphisms act transitively on the n leaves. Requiring those exchanges
as symmetries forces all diagonal weights equal:

    Q_n(x)=lambda_n * sum_i x_i^2.

Positive-definite metrics require lambda_n>0. Exact invariant-space ranks give
one metric parameter at each of ranks1,2,4 under the exchange contract. Symmetry
alone does not identify the scale between ranks.

If comparison additionally obeys the additive budget law

    Q_(2n)(x,y)=Q_n(x)+Q_n(y),

then lambda_(2n)=lambda_n. This transports one initial scale through the tower.
Additivity is a stated composition contract; it is not a consequence of sign
or permutation symmetry.

## Covariant returns

A linear request on these oriented coordinates must carry its covector a along
with the context. Under a signed permutation G, the covector coordinates become
G*a. For metric lambda*I the least-change increment realizing a^T delta_x=d is

    delta_x = d*a/(a^T a).

The scale cancels from this update and remains in its cost. The checker verifies
return covariance for every admitted signed tree action at all three ranks.
The covector is required request data; there is no nonzero invariant linear
covector available from the orientation symmetry alone.

At the zero state, an equivariant operation cannot return a uniquely selected
positive-norm vector without directional data. Zero is fixed by every sign
change, so an equivariant output there must belong to their common fixed space,
which is zero. An invariant scalar target by itself does not select an edit.

## Quartic readouts detect the retained hierarchy

At rank4 the independent-sign and tree-exchange invariant quartic polynomials
have dimension3. A basis is

    A = x0^4+x1^4+x2^4+x3^4,
    B = x0^2*x1^2+x2^2*x3^2,
    C = (x0^2+x1^2)*(x2^2+x3^2).

B couples siblings within the two first-level comparisons; C couples their
blocks. Tree swaps preserve both. A permutation exchanging a sibling with a
member of the other block need not preserve them separately.

If all leaf permutations are admitted instead, only two independent quartic
invariants remain: A and B+C. Thus the quadratic norm forgets the pairing
hierarchy while quartic readouts can retain it. Their coefficients and any
positivity conditions require additional readout choices.

## Structural result

The product-derived1,2,4 spaces now have compositional orientation transport,
a classification of invariant linear/quadratic readouts, a covariant return
contract, and a first hierarchy-sensitive invariant interface at degree4.
The mathematical next distinction is whether the comparison tree is retained
operational data or whether rebracketing is an equivalence. That distinction
controls which quartic readouts are admissible.

## Verification

    python research/nima/checkers/check_recursive_orientation_transport.py

Exact group composition, invariant linear and symmetric-metric ranks,
least-change return covariance, quartic monomial orbits, a non-tree-permutation
negative control, and an additive-budget check. The computed metrics are on
oriented homology-coordinate spaces; their relation to the leaf-edit metric
and physical observables remains to be constructed.
