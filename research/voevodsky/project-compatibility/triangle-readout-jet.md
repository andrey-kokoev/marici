# Decision point: a finite normalized boundary value is not a finite-part readout

## Fresh starting result

The independent Cartesian calculation confirms a nonzero local Euclidean regulator pole. Freeze that benchmark rather than continue extending the old finite-value interpretation. The question now is which physical observation the completed interface must retain.

At a fixed E>0, consider the candidate finite-part domain of simple-pole Laurent germs

    G=A/epsilon+B+O(epsilon),
    R=r1*epsilon+r2*epsilon^2+O(epsilon^3), r1!=0,
    P=R*G=P0+epsilon*P1+O(epsilon^2).

This is a data-sufficiency test. It does not claim that we have computed B for the triangle, or that two arbitrary germs represent the same fully specified physical source.

## Exact loss and recovery

Multiplication gives

    P0=r1*A,
    P1=r1*B+r2*A.

Thus P0 determines the pole coefficient A, but not B. For example, r1=2,r2=3,A=5 and finite parts7 or11 both give P0=10. Their P1 values are29 and37.

Retaining the first regulator jet recovers both:

    A=P0/r1,
    B=P1/r1-r2*P0/r1^2.

For the actual old-to-Euclidean comparison,

    R=H/(3sqrt(pi))*Gamma(1/2+epsilon)/Gamma(epsilon)
     =(H/3)*epsilon*[1-2log(2)*epsilon+O(epsilon^2)],

so, if the finite-part germ is supplied,

    B=(3/H)*[P1+2log(2)*P0].

The Gamma expansion is written analysis; the generic jet identities are checked exactly. P1 is genuinely additional retained data: it is not recoverable from the already computed P0 alone.

## A severe test of prescription independence

Multiplying a regulated germ by a factor1+sigma*epsilon+O(epsilon^2) leaves A unchanged and sends B to B+sigma*A. A dimensionless scale convention lambda^(2epsilon) has sigma=2log(lambda). The old boundary value P0 is unchanged while a finite-part readout changes whenever A is nonzero.

This does NOT say all such multipliers are authorized by the physical source. It proves that pole data or a coarse normalized boundary value alone cannot select among them. A fully fixed regulated family has a definite Laurent finite part when it exists; interpreting that coefficient physically requires the intended normalization and subtraction/readout prescription, not an arbitrary choice of multiplier.

## Concrete programme decision

The mathematical pole is now independently confirmed. The next selected work is the physical readout contract, not further endpoint asymptotics. Distinguish explicitly:

1. the regulated Euclidean period G(E,epsilon);
2. its regulator-pole coefficient A(E);
3. a specified Laurent finite part B(E) or another subtraction scheme;
4. the old normalized boundary value P0(E)=r1(E)A(E);
5. a source-prescribed finite combination of contributions, if the observable is not an individual diagram.

None may be substituted for another solely because it is finite or has the desired boundary behavior. The source must also specify the actual continued chain and comparison with the diagram-level family.

If a finite-part comparison is selected, retain at least the regulator jet through P1 and the normalization through r2. This is the minimum algebraic information for that task, not a claim that all global analytic or physical gates are thereby solved. Other strata and infinity remain unproved.

Next executable source task: inspect the primary paper's explicit finite-observable/subtraction constructions and determine which of the five objects, if any, they authorize for this triangle. Ask the source owner for exact equations and conditions in parallel; do not treat acknowledgment as mathematical evidence.

## Verification

`check_triangle_readout_jet.py` passes108 exact Laurent-jet and normalization-shift controls, including the explicit same-P0/different-finite-part counterexample. Receipt: `triangle-readout-jet.json`. This verifies a data-loss theorem for the stated germ domain, not physical scheme equivalence or a computed triangle finite part.
