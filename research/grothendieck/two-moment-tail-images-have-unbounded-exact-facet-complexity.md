# Two-moment tail images have unbounded exact facet complexity

## DPC disposition: corroborated for every m>=2

The owning bounded-atom tail relaxation has finite-support faces whose
observable images have dimension two and exactly 2m exposed edges. Exactly
2m halfspaces are necessary and sufficient to represent each image in the
original two observable coordinates.

This is a sharp representation-growth law, not merely a bad elimination
order. An exact residual representation cannot remove the growth while
remaining in the declared halfspace format.

## Owning analytical source and an all-m admission proof

Use the N=1e6 relaxation with nonnegative masses at integer log positions,
atom caps log n and cumulative envelope

    A(log x)<=M(x)=2log(2)x+log x+log(2)-psi(N).

For m>=2 retain only the positions

    n_j=4^(50+j)=2^(100+2j),  j=0,...,m-1,

setting every other atom to zero. These coordinate-zero restrictions define
a face of the nonnegative carrier. The claim is that its remaining atom caps
are completely independent: the entire box is admitted.

Write x_j=log(2)t_j. Then 0<=t_j<=100+2j. The maximum cumulative mass through
j is log(2)(j+1)(100+j), which is less than P_j=(j+1)(100+j).
The owning finite evidence gives psi(N)<2^24. The following exact induction
holds for every nonnegative integer j:

    P_0=100,
    4P_j-P_(j+1)=3j^2+301j+198>=0,
    P_j<=100*4^j < (2^100-2^24)*4^j <= n_j-psi(N) < M(n_j).

The last inequality uses 2log(2)>1. M is increasing, so checking the atom
positions controls every intervening cut and the infinite interval after
the last atom. Before the first atom cumulative mass is zero and the owning
envelope is nonnegative. Therefore these really are admitted boxes, not
independently plausible coordinates assembled without a joint check.

They are faces of the RELAXATION, not a description of uncertainty in actual
prime powers. In particular, the actual Mangoldt mass at these powers of two
is known more precisely than the declared log n cap. That stronger arithmetic
information is not part of this carrier. No actual prime realization is
asserted or needed for this representation lower bound.

## Exact kernel, not rationally substituted slopes

Every selected position satisfies log n_j>=100log(2)>64. Beyond the terminal
hat knot the owning combined kernel is exactly

    K(log n)=C*n^(-7/2),    C=B0-J64<0.

The verifier independently recomputes C from the linear hat primitives.
Retain total mass S and exact combined-kernel pairing F on the face. With
r_0=2^-350, make the fixed invertible normalization

    U=S/log(2),       V=F/(C*log(2)*r_0).

The image is exactly

    Z_m = { sum_j t_j (1,r_j) : 0<=t_j<=100+2j },
    r_j=2^(-7j).

All geometry in these coordinates is rational. Invertible normalization
preserves dimension, edges and minimal halfspace count; no approximate
kernel samples are used. S is finite on each finite-support face; this is
not a claim that the untruncated mass of the full infinite prime tail is a
finite observable.

## Exactly 2m facets: constructive proof and lower bound

For generator j choose either normal

    a_j=(-r_j,1) or -a_j.

Its support value is

    h(a)=sum_i (100+2i) max(0,a dot (1,r_i)).

The slopes r_i are distinct. Thus a_j is perpendicular to generator j alone.
Every other atom is forced to one of its two endpoints when maximizing this
normal, while t_j remains free. The exposed face is a nondegenerate segment
with explicit source lifts at both endpoints. Opposite normals expose the
opposite segment, yielding 2m distinct edges.

Conversely, a nonzero normal not perpendicular to any generator forces every
atom to an endpoint and exposes a single vertex. Hence there are no additional
edges. These 2m supporting halfspaces describe the complete zonotope. Each
edge's relative interior requires its own supporting line in any exact
finite halfspace representation of this full-dimensional polygon. Therefore
2m is both necessary and sufficient.

Adding one new atom with a distinct slope obeys the constructive recurrence

    Z_(m+1)=Z_m + [0,100+2m]*(1,2^(-7m)),

and adds exactly two exposed edges. The accumulated witness still has just
two observable coordinates. The growth belongs to its compatible possibility
set, not to the dimension of an individual boundary value.

## Separating queries and source lifts

For every facet, the packet constructs a rational point just outside the
relative interior of that edge, satisfying all other facet inequalities.
A singleton query at this point is a finite conjunction of rational closed
halfspaces. It is admitted after forgetting that facet, but rejected by the
complete image. These are explicit continuation witnesses for the proposed
undersized interface.

The packet also supplies atom-box lifts for every polygon vertex. All source
box points satisfy the support inequalities, and every vertex of their bounded
halfspace intersection has such a lift. Convexity proves equality of the
whole image, not merely agreement on finitely sampled objective directions.

## Checks and scope of the all-m claim

Exact packets are generated for m=2,3,4,8,16, with 4,6,8,16,32 facets. The
independent verifier imports neither the producer nor a geometry library.
It checks:

- owning artifact bindings and the independently recomputed suffix constant;
- logarithmic normalization and the uniform admission induction;
- exact slope ratios and positive caps;
- all support identities and exposed-edge endpoint lifts;
- bounded halfspace intersections and their complete vertex lists;
- every facet-omission witness and rejection of a corrupted support bound.

The theorem for all m follows from the symbolic induction and exposed-face
argument. It is not extrapolated from the five finite replays.

## What this settles for structural synthesis

The preceding analytical elimination result established correctness when all
shared factors survive. This result proves that some output growth can be
unavoidable even for perfectly correct elimination and a fixed two-coordinate
cut presentation.

It separates three notions:

1. finite-dimensional boundary values: two coordinates here;
2. exact materialized possibility geometry: 2m necessary halfspaces;
3. succinct generative descriptions: this regular family is described by a
   short formula and its parameter m.

The third is an important limitation: this is NOT an information-theoretic
lower bound against every encoding. It excludes auxiliary-variable extended
formulations, support-function programs and other symbolic representations.
A compact source rule can generate a large exact residual polygon. That is
precisely why representation contracts must be explicit.

There is no new prime-distribution fact or full-tail midpoint separation.

## Reproduction

    uv run --with python-flint python research/grothendieck/checkers/construct_two_moment_tail_complexity.py
    uv run --with python-flint python research/grothendieck/checkers/verify_two_moment_tail_complexity.py

Contract: `results/two-moment-tail-complexity-contract.json`.
Packet: `results/two-moment-tail-complexity.json`.
