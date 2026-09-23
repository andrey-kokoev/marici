# Analytical saturation commutes exactly on rectangles or lines

## Owning source test

Use the independently replayed three-bin Chebyshev moment carrier P and its
observables S=sum x_i and F=sum c_i x_i. The c_i are the owning rational
lower kernel coefficients, not exact within-bin kernel values. They satisfy

    c_3 < c_2 < c_1 < 0.

This is the declared analytical relaxation, not the prime-realizable source.
Define saturation relative to a fixed admitted source P by

    Sat_S(C)={x in P: S(x)=S(y) for some y in C},

and analogously for F. These are forgetting operators, not evidence merges.

## Explicit noncommuting diamond

With a=1000, take three admitted source witnesses

    start  = (0,a,0),
    middle = (a,0,0),
    end    = (0,0,a*c_1/c_3).

The start and middle agree in S; middle and end agree in F. Hence end belongs
to Sat_F(Sat_S({start})).

A reverse-order intermediate witness would need

    S=a*c_1/c_3,       F=a*c_2.

Every admitted nonnegative mass vector satisfies F-c_3*S>=0, because this
is sum (c_i-c_3)x_i with nonnegative coefficients. The proposed reverse
witness instead has

    F-c_3*S=a*(c_2-c_1)<0.

Its source fiber is empty. This is an exact rational obstruction certificate,
not a failure of a particular witness search. The same three witnesses remain
admitted after imposing S<=B_3/2, so that tightening does not repair the diamond.

## Exact convex-image criterion

Let P be any source with nonempty compact convex joint image

    Q={(S(x),F(x)):x in P} subset R^2.

No injectivity of (S,F) on source witnesses is required.

**The two saturation operators commute on every source subset iff Q is a
rectangle (a product of closed intervals) or has affine dimension at most one.**

First, commutation is exactly the rectangle-completion property: whenever
(s_0,f_0), (s_0,f_1), (s_1,f_1) belong to Q, so must (s_1,f_0). This is the
existence of the reverse-order middle witness; any source lift of the fourth
corner suffices. Singleton source subsets detect all failures.

If Q is a rectangle, completion holds immediately. If Q lies on an oblique
line, either coordinate determines the other and the observer kernels agree.
On a horizontal or vertical line one kernel is universal; it commutes with
the other. The point case is immediate.

Conversely suppose Q has nonempty interior and the kernels commute. Any two
interior points can be joined by a finite horizontal/vertical path inside
the interior: the connecting segment is compactly contained in the open
convex interior, so sufficiently short rectangular steps stay inside it.
Commuting equivalence relations have a composite equal to their equivalence
join. Thus all such interior paths reduce to a two-step path, and every mixed
corner of two interior points belongs to Q. The product of the interior
coordinate ranges is therefore contained in Q. Closedness then puts the
whole bounding rectangle inside Q; the reverse containment is automatic.
So Q is that rectangle.

Compactness, convexity and the two scalar observables are material hypotheses.
General nonconvex images can have several disconnected rectangular components
or other lower-dimensional structures. This is not their classification.

## Constructive restriction tests

The constructor independently projects four explicitly restricted carriers:

| Restricted source | Joint image | Saturations commute |
| --- | --- | --- |
| P | original six-facet polygon | no |
| P intersect {S<=B_3/2} | full-dimensional nonrectangle | no |
| P intersect {S=B_3/2} | nontrivial vertical segment | yes |
| P intersect a small interior (S,F) rectangle | that exact rectangle | yes |

For the last case, four explicit source lifts establish that every corner
of the rectangle is in Q. Convexity fills its interior; intersecting with the
observable rectangle gives precisely that image. The construction fixes
x_3=1000 for the corner lifts and solves the other two coordinates exactly.
It does not infer corner realizability from separate observable ranges.

All original and restricted images have exact source lifts and independently
verified vertex containment in both directions. The continuum classification
is a theorem, not an inference from the four tests.

These are admissible CONTROL SLICES of the analytical model. They are not
newly acquired evidence that actual prime masses satisfy those restrictions.
Whether an owning task supplies such a refinement is a separate admission
question. The result determines what its geometry would need to accomplish.

## Order independence is not safe forgetting

The positive rectangle case does NOT recover preservation of joint evidence.
On a nonempty rectangular image, starting with any one source witness and
saturating successively by S and F reaches the entire restricted source.
Both orders agree because both forget all observable restrictions.

Joint retention instead uses Sat_(S,F), whose kernel is the intersection of
the two observer kernels. Alternating separate forgetting closes under their
join. They remain different operations even in the commuting regime.

Likewise, restriction of the ambient P changes the relative saturation
operators. Intersecting C with new evidence while continuing to use the old
ambient P does not perform that change automatically.

The two repair regimes are also substantively different: a rectangle allows
all combinations of the visible coordinates, whereas a line can make one
determine the other. Commutation alone is not independence, witness uniqueness,
or an authorization to discard accepted evidence.

## Structural consequence

The question 'does stronger evidence make forgetting order-independent?' now
has a source-geometric answer for this convex analytical class. A stricter
numerical bound alone need not help; it must change the joint image into one
of the classified forms. Even then, a separate preservation contract is
needed to justify the resulting forgetting.

This complements, rather than repeats, finite saturation-diamond tests: it
gives a continuum criterion and an owning analytic obstruction, together
with constructive positive cases and an explicit limit on their meaning.

## Reproduction

    uv run --with python-flint python research/grothendieck/checkers/check_analytical_saturation_diamond.py
    python research/grothendieck/checkers/verify_analytical_saturation_diamond.py

Contract: `results/analytical-saturation-diamond-contract.json`.
Packet: `results/analytical-saturation-diamond.json`.

The producer freshly replays the owning query-relative interface verifier.
The independent verifier imports neither the producer nor its geometry code:
it uses rational determinant enumeration, source lifts and convex-combination
containment to verify restricted images. The empty reverse fiber is certified
by the explicit nonnegative source inequality above. No actual-source midpoint
status or prior calibration branch is changed.
