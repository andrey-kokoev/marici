# Canonical coherence composites need depth-independent condition bounds

## Sharpened completion gate

Uniform bounds on generating coherence cells do not imply stable transport across arbitrary finite assemblies.

Suppose every associator and inverse satisfies
\[
\|\alpha\|\le M,\qquad
\|\alpha^{-1}\|\le M.
\]
A canonical comparison between two bracketings of \(n\) atoms may use \(O(n)\) generating cells. The naive estimate grows as
\[
M^{O(n)}.
\]
Pentagon coherence makes the resulting arrow path-independent. It does not make the arrow uniformly conditioned.

Therefore completion stability requires control of canonical composite intertwiners independent of atom count and cutoff.

## Two sufficient regimes

### Unitary coherence

If every admitted generator is isometric,
\[
\|\alpha\|=\|\lambda\|=\|\rho\|=1,
\]
and likewise for authorized braiding, duality, and dagger cells, then every coherence composite is isometric.

This regime is natural for determinant-line phases and genuinely unitary quantum coefficients, provided the varying-fiber identifications are themselves unitary in the frozen source topology.

### Uniformly bounded coherent geometry

For nonunitary cells, choose canonical normal bracketings and let
\[
U_{\tau\to\tau'}^{(n,X,s)}
\]
be the unique coherent comparison between bracketings \(\tau,\tau'\) of \(n\) atoms.

Require, on each compact off-seam set \(C\),
\[
\sup_{\substack{n,X,s\in C\\\tau,\tau'}}
\|U_{\tau\to\tau'}^{(n,X,s)}\|
\,
\|(U_{\tau\to\tau'}^{(n,X,s)})^{-1}\|
<\infty.
\]

In a projective locally convex topology, replace this by depth-independent two-sided seminorm estimates with a fixed seminorm transport schedule.

This is a bound on the coherent geometry, not merely on its local generators.

## Canonical transport formulation

Fix for each finite word \(w\) a canonical bracketing \(\nu(w)\). Let
\[
T_\tau:\tau(w)\to\nu(w)
\]
be the coherence transport.

It suffices to prove
\[
\sup_{w,\tau}\kappa(T_\tau)<\infty,
\qquad
\kappa(T)=\|T\|\,\|T^{-1}\|.
\]
Then
\[
U_{\tau\to\tau'}=T_{\tau'}^{-1}T_\tau
\]
has uniformly bounded condition number.

The choice of \(\nu\) and the transports \(T_\tau\) is part of the frozen completion constructor. It cannot be changed with cutoff to optimize estimates post hoc.

## Hostile: commuting diagrams with exponential amplification

Let each reassociation cell act on a typed two-dimensional coefficient fiber by
\[
S=
\begin{pmatrix}
M&0\\
0&M^{-1}
\end{pmatrix},
\qquad M>1,
\]
with inverse \(S^{-1}\). Define the coherence data so all pentagon diagrams commute by assigning the same canonical exponent to each bracketing and letting each associator be the difference of exponents.

Every generating cell and inverse has norm at most \(M\), and every finite coherence diagram commutes. Yet choose bracketings whose canonical exponents differ by \(d_n\to\infty\). Their comparison is
\[
S^{d_n}
=
\begin{pmatrix}
M^{d_n}&0\\
0&M^{-d_n}
\end{pmatrix},
\]
with condition number
\[
M^{2d_n}\to\infty.
\]

Finite monoidal coherence is perfect. Completion-stable coherent transport fails.

## Scalar phase control

If
\[
\alpha_{a,b,c}=\omega(a,b,c),
\qquad |\omega|=1,
\]
then phase composition is isometric regardless of depth. A nontrivial coherent \(H^3\) class therefore causes no norm amplification by itself.

However, if the phase is represented through nonunitary fiber trivializations,
\[
\alpha=T^{-1}\omega T,
\]
the trivializations can reintroduce condition growth. The relevant statement is unitarity in the actual frozen source/feature topology, not modulus one in an abstract scalar presentation.

## Mellin/Green normalization cells

Nonunitary normalization cells are the live case. Their cumulative growth can arise from:

- repeated half-density renormalization;
- changing Green feature metrics;
- seam fiber identifications;
- endpoint or archimedean rescaling;
- grade-dependent Adams coefficients;
- nonorthogonal coherent/disagreement splittings.

Each local map can be harmless while long assembly depth amplifies one direction and suppresses another.

## Relation to bounded-energy completion

A compatible finite assembly belongs to the completed source only when it satisfies the frozen bounded-energy condition. Coherent transport must preserve that class uniformly:
\[
\mathcal E(T_\tau x)
\asymp
\mathcal E(x)
\]
with constants independent of word length and cutoff.

Otherwise realizability depends on bracketing: one presentation has finite source energy while an equivalent coherent presentation leaves the restricted limit. That contradicts completion of the monoidal quotient.

## Relation to the five margins

Depth-dependent coherence conditioning can mimic collapse of any later analytic margin. Before computing the five margins, transport all presentations to the canonical bracketing and verify the depth-independent coherence bound.

Then the margins are presentation-invariant up to fixed constants. Without this gate, an apparent loss of \(\delta_P\), \(\delta_A\), or \(\delta_{\mathrm{mix}}\) may be an artifact of ill-conditioned reassociation rather than a source defect.

## Completion theorem refinement

The constructor completion theorem must establish:

1. the finite monoidal coherence basis;
2. cutoff-compatible canonical bracketings;
3. continuous canonical transports and inverses;
4. condition bounds independent of cutoff, atom count, and bracketing;
5. bounded-energy preservation;
6. optional isometric hexagon/dagger transport when admitted.

Unitary coherence proves items 3–5 immediately after topology compatibility. Nonunitary coherence requires a global geometry estimate.

## Next executable audit

For each finite word and bracketing:

1. compute the canonical transport digest;
2. compute forward and inverse seminorm/operator bounds;
3. group by atom count and cutoff;
4. estimate the maximal condition number;
5. test whether the envelope is bounded, polynomial, or exponential;
6. reject any unbounded envelope for completion authorization;
7. identify the local normalization cells contributing to growth.

The first substantive analytic target is to show that Mellin/Green normalization cells are either unitarizable by a source-authorized metric or possess a depth-independent coherent-geometry bound.
