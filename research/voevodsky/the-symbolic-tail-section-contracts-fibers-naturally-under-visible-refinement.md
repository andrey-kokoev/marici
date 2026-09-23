# The symbolic tail section contracts fibers naturally under visible refinement

## Source and section

Fix m>=2 and the owning analytical box B_m=product_j [0,100+2j], observed by L(t)=(sum t_j, sum 128^-j t_j). This is the declared analytical tail relaxation, not a prime-realizability statement. Nima's symbolic membership interface gives upper and lower greedy profiles h(U),l(U) and their weighted values Vmax(U),Vmin(U).

For 0<U<C(m), define

    theta=(V-Vmin(U))/(Vmax(U)-Vmin(U)),
    s(U,V)=(1-theta)l(U)+theta h(U).

At the two tips use the unique zero or full-cap source lift. This is precisely the runtime's generative source lift, interpreted in the ordinary topology of the source box.

## Continuity on the entire polygon

Both greedy profiles are continuous piecewise-affine functions of U. At a breakpoint, a full partial coordinate is identical to the next prefix with zero remainder; the discrete prefix index jump does not create a source-vector discontinuity.

The vertical gap is strictly positive for 0<U<C(m). Indeed x_j=U(100+2j)/C(m) is strictly interior to the box. A sufficiently small transfer between two coordinates keeps U fixed and changes V because the slopes differ. Thus no interior U-slice has zero vertical width.

The interpolation formula is therefore continuous away from the tips. At U->0 every coordinate of any feasible lift lies between zero and U. At U->C(m), every coordinate deficit lies between zero and C(m)-U. These bounds force continuity at both tips even if theta itself has no limit.

Consequently s is a global continuous section of L on Z_m. This is an all-m argument, not an extrapolation from finite samples. It asserts continuity for each fixed m, not uniform conditioning as m grows.

## A contraction natural under retained visible evidence

For any visible subset Q of Z_m, let C_Q=B_m intersect L^-1(Q). Define

    H(x,t)=(1-t)x+t s(Lx).

Convexity of the box and equality of the two endpoint observations imply that H stays in the same source fiber for all t. In particular it stays in C_Q even if Q is not convex. It starts at x, ends at s(Lx), and fixes every section point.

Thus C_Q strongly deformation retracts onto s(Q), which is homeomorphic to Q by L. For Q' subset Q, the contraction on C_Q' is literally the restriction of the same H. No recomputation of a run-specific contraction or additional coherence choice is required when evidence is refined.

For the engine's accepted observable halfspaces, Q is their accumulated intersection with Z_m. All previously retained frames are preserved simultaneously by the contraction. Empty Q gives the vacuous empty restriction, not a source witness.

## What this does not erase

The contraction does not encode which Q occurred. Its restriction is available uniformly, but the retained evidence identifying Q remains independently necessary. The theorem also does not apply to an unsaturated carrier with hidden source-coordinate restrictions: its chosen section point might be excluded.

Ordinary source paths are the declared identity notion here. The checker exhibits m=3 with coordinate zero changing from 0 to 17/86 along a same-observation contraction. Hence a source-coordinate audit does not automatically descend to this homotopy equivalence. The test's internal coordinate reads are mathematical diagnostics, not an extension of the runtime's admitted query language.

A compact generative section is not a constant-bit certificate. Exact arithmetic, query work, and retained run-specific evidence may still grow.

## Controls and reproduction

The checker imports the actual Generator, independently expands greedy profiles and source vectors for verification, and checks 408 exact section/contraction instances and 37 greedy join controls through m=1024. It includes both degenerate tips, near-tip values, source points other than the chosen lift, and retained halfspace histories. These are implementation controls; the continuum proof is above. This run does not independently replay the upstream all-m source-admission proof.

    python research/voevodsky/checkers/check_symbolic_tail_fiber_contraction.py

Artifact: `results/symbolic-tail-fiber-contraction.json`.

## Synthesis

The symbolic tail interface provides more than isolated feasible lifts: it supplies a global section and a fiber contraction that commutes strictly with restriction by visible evidence. This connects generator-based query answering to parameterized filling coherence while leaving visible-image identity, hidden restrictions, and representation costs distinct.
