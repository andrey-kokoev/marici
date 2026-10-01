# Witnessed reference return and pentagon coherence

## Source audit: which inverse is known?

The retained-total theorem in table-fibration.md establishes an equivalence
between original rows and their indexed dependent total. Its inverse reconstructs
records. The public theory describes T1 as relationships with witnessed round-trip
agreement. The inspected specifications supply no adapter turning the row
reconstruction equivalence into strict invertibility of the independently
retained matrix reference d:A->B.

Thus the preceding inverse-bridge construction remains a strict-reference sector.
Here we explicitly test the weaker DG round-trip contract:

    delta(u)=r*d-1_A, delta(v)=d*r-1_B,

where d:A->B and r:B->A are closed degree-zero maps, and u,v have degree1.
The differential, return and witnesses are supplied data; this is a construction
under that contract, not proof that every carrier reference admits it.

## Strict invertibility is stronger

An exact example has one surviving homology coordinate and two contractible
Q^2 pairs. The map d is identity on surviving homology, zero on one pair and
2I on the other; r is the identity matrix between the two copies of the complex.
It satisfies both round-trip equations with explicit u,v although its matrix is
singular. The example retains nonzero homology, unlike the earlier fully
contractible witness fixture.

This refutes deriving strict matrix invertibility from witnessed round trips
under the weak DG interpretation. In an ordinary degree-zero matrix model with
no higher witnesses, the same equations reduce to strict inverse identities.

## Reference drift must be retained

The operation Q star P=Q*r*P remains associative for any fixed closed r. Its
reference product d*r*d need not equal d. A reference-correction witness is

    e=d*u, delta(e)=d*r*d-d.

For fixed-reference comparisons C_i=d+rho_i, the exact residual law becomes

    rho_new = (d*r*d-d) + d*r*rho1 + rho2*r*d + rho2*r*rho1.

The two composite witness routes, both relative to the original d, are

    H_first=h2*r*C1+d*r*h1+e,
    H_second=C2*r*h1+h2*r*d+e.

Their difference is still delta(h2*r*h1). The same constructor is applied twice
in the checker. Even starting with C1=C2=d, the output can differ from d as a
matrix; the record retains e as the witnessed agreement. Erasing that drift
would change the contract.

## Associativity of values and coherence of histories

Write combine(P,Q) for the first-route construction. The actual maps agree
strictly across bracketings. The retained witnesses need an associator. For
leftmost input witness h1, define

    A(h1)=d*u*u+e*r*h1.

Then

    delta(A(h1))=H_((12)3)-H_(1(23)).

For four inputs, the three-edge and two-edge associator routes around the
pentagon have the same boundary. Their difference is filled by

    W(h1)=d*u*u*u+d*u*u*r*h1.

The checker verifies delta(W)=long_route-short_route, all five bracketings,
and delta^2(W)=0. Both A and W are nonzero in the explicit example. Thus weak
unit corrections produce executable degree-two and degree-three coherence
without assuming strict round-trip equality.

## Unit triangles expose a retained-history choice

The two reference-correction witnesses d*u and v*d have the same boundary.
Their difference t=d*u-v*d is closed but need not be a boundary for arbitrarily
fixed u,v.

An explicit adjustment of the B-side unit witness supplies a triangle:

    v_new=v+t*r,
    delta(v_new)=d*r-1_B,
    delta(t*u)=d*u-v_new*d.

The adjustment t*r is closed and must be retained as a history edit. It can
change the homotopy class of the unit witness: a zero-differential counterexample
has two valid unit witnesses with a nonzero triangle discrepancy and no filler.
Adjusting one makes them agree, but the edit is not exact in that example.
Therefore a fixed-history policy and a policy permitting adjusted coherent unit
witnesses have different admissibility conditions.

## Structural outcome

Recursive bridge composition extends to witnessed returns with an explicit
reference drift, unit witnesses, associator and pentagon filler. Strict inverse
closure is the special case u=v=0. The construction neither silently substitutes
a pseudoinverse nor discards witness histories.

The remaining carrier decision is which return and unit histories are retained
and whether coherent history adjustment is admissible. Its physical readout must
specify how it treats reference drift and history cost. A homology-level readout
and a raw matrix/cost readout can see different data. No numerical constant,
zero-cost strictification or physical gauge quotient is inferred here.

## Verification

    python research/nima/checkers/check_witnessed_reference_return.py

Sparse exact rational graded maps: singular witnessed reference with surviving
homology, both unit equations, nonzero reference drift, two constructor rounds,
two homotopy routes, all five bracketings, nonzero associator and pentagon filler,
triangle adjustment, and a fixed-unit-history triangle obstruction.
