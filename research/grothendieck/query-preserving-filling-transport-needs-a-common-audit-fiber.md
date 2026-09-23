# Query-preserving filling transport needs a common audit fiber

## Frozen question and result

Use the owning three-bin Chebyshev moment carrier P, with S=sum x_i and
F=sum c_i*x_i. Freeze witness audits to all rational predicates x_1<=r,
with exact truth values. No bin-two or bin-three audit is silently added.

On the earlier rectangular observable restriction, the S and F saturations
commute, but the two middle filling fibers of an explicit diamond have
different x_1 ranges. **No equivalence preserving the declared audits exists.**
This rules out every audit-preserving bijection, not just one poorly chosen
transport.

On a separately constructed product slice, every base fiber has the same
nondegenerate raw-x_1 interval. There is a unique audit-preserving transport,
given by keeping x_1 and replacing (S,F). Exact affine identities make this
transport coherent for arbitrary finite paths.

The positive carrier is a new controlled restriction. It is not a coordinate
change of the negative carrier, a new acquisition from the actual primes, or
a repair of a fixed defective transport by reparameterization.

## Exact fiber coordinates

Because c_2!=c_3, the map x -> (S,F,h=x_1) is invertible:

    x_1=h,
    x_2=(F-c_3*S-(c_1-c_3)*h)/(c_2-c_3),
    x_3=S-h-x_2.

For each fixed (S,F), substituting these formulas into the owning source
inequalities gives a closed interval of possible h values. The checker
retains the source rows attaining its exact lower and upper endpoints and
source lifts of both endpoints. Every bound is rational.

All rational threshold audits together distinguish distinct real h values.
Thus an audit-preserving map must leave h unchanged. Since (S,F,h) identifies
a unique source point, a bijection between these two filling fibers exists
with the declared audits iff their h intervals agree. If it exists, it is
uniquely determined.

## Original commuting rectangle: a stronger obstruction than existence

Use the same source-lifted rectangle from the analytical saturation test.
Choose its lower-left and upper-right corners as outer endpoints. The two
middle bases are upper-left and lower-right. Their exact source fibers have
approximate h ranges

    [886.1622084125702, 887.1312701588176],
    [1112.9200624383077, 1113.7860380700542].

Both are nonempty nondegenerate intervals. Their endpoint relations commute
because the full observable image is a rectangle. Nonetheless, a rational
threshold between the two lower endpoints is feasible in the first middle
fiber and impossible in the second. The exported source witness and active
lower-bound row certify this distinction exactly.

There can be no map from the first fiber to the second preserving that
threshold truth value for every witness, and hence no audit-preserving
equivalence. Contractibility as ordinary topological intervals does not
remove the obstruction: it does not authorize erasing a declared observation.

Without these raw-h audits the intervals can be related by normalized
position tau=(h-lo)/(hi-lo). Such affine reparameterizations can be made
coherent by retaining tau across fibers, but they change raw h and fail the
declared audits. This is an explicit scope distinction, not a claim that
all witness transports on the underlying intervals are impossible.

## Positive construction from source inequalities

Start at the strictly admitted source point (1000,1000,1000). Transform every
owning inequality into (S,F,h) coordinates using the exact inverse matrix.
Choose strictly positive proposed widths and scale them by a rational rho
so that, for each row,

    sum |transformed_coefficient_i| * width_i <= source_slack/2.

This proves the entire three-dimensional coordinate box lies in P; checking
only representative lifts would not suffice. The packet also exports all
eight corner lifts. In this run the common h interval is approximately

    [999.9979976208923, 1000.0020023791077].

Let P* be P restricted by this (S,F,h) box. The row guards prove that P* is
EXACTLY the inverse image of the full product of the base rectangle and this
common h interval. No unrepresented source restriction remains inside that
product.

For base values u,v define

    T_(u,v)(x)=inverse(v,x_1).

It is admitted everywhere on the corresponding fiber, preserves every frozen
h audit, has inverse T_(v,u), and satisfies

    T_(v,w) T_(u,v)(x) = inverse(w,x_1) = T_(u,w)(x).

These coefficient identities prove all path-composition comparisons, not
just sampled triangles. Every endomorphism T_(u,u) is identity. The complete
audit coordinate makes the allowable transport unique; coherence follows
from that uniqueness and the explicit formula, not from existential kernel
permutability alone.

The positive restrictions are admissible model control slices. They are not
evidence that the actual prime masses obey the narrow box. No actual-source
selection, causal reversal or publication authority follows.

## Structural synthesis

The test separates three levels on an owning analytical source:

1. A rectangular observable image guarantees reverse-order middle existence.
2. A common audit fiber is additionally required for audit-preserving witness
   comparison; commuting endpoints do not supply it.
3. A certified product trivialization with a complete retained audit
   coordinate supplies unique, coherent transport.

This also separates three kinds of attempted repair:

- changing coordinates while retaining the same observation semantics;
- changing the audits (for example, replacing raw h with normalized position);
- changing the admitted carrier to one with uniform audit fibers.

Only the last is the positive construction tested here. No hidden quotient
identifies previously distinguishable witnesses, and no claim is made that
an arbitrary chosen family of diamond bijections must satisfy higher coherence.

## Verification

    uv run --with python-flint python research/grothendieck/checkers/check_query_preserving_filling_transport.py
    python research/grothendieck/checkers/verify_query_preserving_filling_transport.py

Contract: `results/query-preserving-filling-transport-contract.json`.
Packet: `results/query-preserving-filling-transport.json`.

The producer freshly replays the owning saturation verifier. The separate
verifier imports neither the producer nor a geometry/optimization package.
It reconstructs exact fiber bounds, both affine inverse identities, the audit
obstruction, all whole-box source guards and eight corner lifts. It checks
375 base/tag triangle controls; the continuum coherence claim rests on the
exact affine identities. Existing task calibration artifacts are unchanged.
