# Research annotations

## Status and reading rule

These notes separate claims made explicitly in the talk from Marīci/Nima
inferences.  The transcript is a primary source for Nima's conceptual
architecture, not a proof of the stronger operation-algebra statements in the
ledger.

## What the talk says explicitly

### The carrier comes before the amplitude

At `transcript.md:115-209`, the primitive datum is a space whose boundary
splits as a product of two lower copies of itself.  Feynman graphs and marked
points on \(\mathbb P^1\) are two realizations.  A separate *dictionary* turns
that self-factorization into a factorizing amplitude.  Nima's stated research
program is to find such structures and then search for their amplitude
dictionaries.

This is stronger than the slogan that an amplitude has factorization poles:

\[
\partial_D\mathcal F_n\simeq
\mathcal F_L\times\mathcal F_R
\quad\hbox{precedes}\quad
A_n=V(\mathcal F_n).
\]

Here \(\mathcal F\) denotes the factorizing carrier and \(V\) its dictionary or
valuation.

### Compatibility is incidence geometry

At `transcript.md:540-569`, faces are labelled by compatible chord sets.  Face
refinement adds compatible chords, and an intersection is labelled by the
union of the labels of the intersecting faces.  Thus locality is encoded first
as a compatibility complex; residues are a later functional image of this
incidence data.

### The discovery method is deliberately pre-formulaic

At `transcript.md:850-900`, Nima warns that the structures are missed by
rushing toward a closed formula.  The method is to make kinematic space
"transparent and thoughtless," inspect its elementary coordinates and
relations, and let the relevant geometry become forced.  For Marīci this is a
methodological constraint: low-arity carrier and naturality tests should come
before naming a universal algebra.

### Kinematic space carries a sourced discrete wave equation

At `transcript.md:1320-1390`, the mesh variables obey

\[
(\Box_{\rm kin}X)_{ij}
=X_{ij}+X_{i+1,j+1}-X_{i,j+1}-X_{i+1,j}
=C_{ij}.
\]

Boundary data plus the sources determine the interior variables by a discrete
Gauss/Stokes law.  At `transcript.md:1390-1420`, both \(X_{ij}\) and \(C_{ij}\)
are required to be positive.

### Positivity generates locality and boundary self-factorization

At `transcript.md:1580-1764`, the causal diamonds of the mesh encode chord
crossing.  Positivity prevents causally related/crossing channels from
simultaneously vanishing.  On \(X_D=0\), the forbidden diamond disappears and
the two surviving regions obey wave equations of the same type, giving the
Cartesian product of lower carriers.

So the causal mesh is not decorative language.  It simultaneously organizes:

\[
\text{ordering}
\longrightarrow
\text{causal compatibility}
\longrightarrow
\text{locality and factorization}.
\]

### Green-function decomposition exposes zeros

At `transcript.md:1765-2025`, solving the sourced mesh one \(C_{ij}\) at a time
decomposes the associahedron into elementary pieces.  At
`transcript.md:2025-2125`, dimensional collapse of that geometry forces the
canonical top form to vanish.  Hidden zeros therefore appear as degeneration
or rank loss of the carrier, rather than as mysterious cancellation in a
common numerator.

### The NLSM relation preserves the sources

At `transcript.md:2070-2165`, the same zero locus appears in the NLSM and is
more primitive than the Adler-zero presentation.  The alternating kinematic
shift from the scalar amplitude to the NLSM leaves every \(C_{ij}\) unchanged.
In the wave-equation language it is therefore a homogeneous deformation:

\[
X\mapsto X+\delta X,
\qquad
\Box_{\rm kin}\delta X=0.
\]

The talk does not identify this with an associated grade or Rees limit; that
is Marīci's derived-normal interpretation.

### The same elementary pieces admit a string dictionary

At `transcript.md:2180-2250`, the Green-function pieces determine monomials in
an \(\alpha'\)-deformed integral, recognized as the open-string amplitude.
Thus one carrier can admit distinct dictionaries: canonical form for the
particle amplitude and a stringy integral completion.

### Multiplicity can become physical time

At `transcript.md:2290-2350`, Nima describes a third self-factorizing object:
the path integral of a particle moving on a line.  Its ordinary evolution time
is the scattering multiplicity, so the large-multiplicity limit is controlled
by ground-state/long-time physics.  This is the clearest bridge in the talk
from amplitude geometry to a native computational substrate.

## Marīci/Nima synthesis

The talk suggests replacing

\[
\text{one scalar amplitude with many theory faces}
\]

by

\[
\boxed{
\text{self-factorizing carrier}
\;\xrightarrow{\ E\ }\;
\text{derived or strictified carrier}
\;\xrightarrow{\ V\ }\;
\text{physical amplitude}.}
\]

The operation \(E\) may be a normal grade, jet/descent, Karoubi retract, or
presentation strictification.  The dictionary \(V\) must be monoidal with
respect to boundary products.  In this typing, pairing and modular completion
are also carrier-level composition laws before numerical evaluation.

This sharpens the master objective:

> Classify self-factorizing scalar carriers, their factorization-natural
> derived operations, and the monoidal valuations that turn them into physical
> theories.

The transcript supports the carrier-first architecture.  It does **not** by
itself prove that every operation currently listed in the Nima ledger exists
canonically on one universal scalar carrier.

## Consequence for the present frontier

Ledger entry 39 already establishes the genus-zero carrier-level
factorization of the scalar-derived \(\mathsf J\) class and its identification
with \([({\rm Pf}'A)^2]\).  The talk therefore redirects rather than reopens
that test.  The next structural question is whether the newer surface/curve
dictionaries are natural transformations of sewing carriers before final
scalar evaluation.

Entries 53-54 provide the first nontrivial example: physical polarization
closure of an ordinary cubic carrier becomes strict metric trace after passage
to the gauge-reduced curve representative, and the two-open-pair square
commutes even when individual nested longitudinal terms do not vanish.  This
is exactly the carrier/dictionary distinction emphasized here.

The next falsifier is an origin-resolved two-edge Ward--Brauer square: each of
the nine \((M,L^+,L^-)^2\) projector sectors must be assigned to resolved
endpoint extensions compatibly with either partial trace.  Final closed
polynomial equality alone is insufficient.

## Subsequent outcome

Entries 55--59 execute and refine that falsifier.

The diagonal assignment to raw cubic origins fails: every marked-theta
presentation needs all five vertex-sector coordinates.  Replacing origins by
connected marked regions produces a graph-multiplihedral carrier whose
component/innermost edge-deletion maps are strictly functorial in every
connected simple graph tested through five vertices.

The remaining non-strictness is not in the bare carrier.  The off-shell Ward
identity and propagator give a flag-incidence exact sequence with closed sector
\(H_1(G)\).  On the marked theta this Ward kernel is integrally and
equivariantly \(H_1(K_{2,3})\), but resolved noncrossing curves map onto that
homology without a canonical integral equivariant section.  The three
primitive circuit tags have one diagonal relation, an index-three symmetric
splitting obstruction, and pairwise intersection one.

Thus the talk's carrier/dictionary separation has become concrete:

\[
\begin{aligned}
\text{cellular carrier maps}&:\text{strict},\\
\text{Ward-to-homology map}&:\text{strict},\\
\text{homology-to-resolved-curve dictionary}&:\text{derived}.
\end{aligned}
\]

The next falsifier is an oriented Brauer--skein crossing/smoothing cell with
coefficients derived from the scalar first-jet Ward/contact complex and tested
against one separating and one nonseparating Cut.

## Road-polygon and flow-torsor refinement

Entries 60--63 sharpen the derived dictionary once more.  The all-arity
\(K_{2,m}\) circuit resolution is the cellular boundary sequence of the road
polygon \(C_m\).  Its symmetric rational section is the discrete Green
current \(\delta\Delta^{-1}\), and its denominator is the critical group
\(\operatorname{Jac}(C_m)\cong\mathbb Z/m\).

The invariant operation is not the Green formula.  For a source \(c\), it is
the integral torsor of currents satisfying \(\partial j=c\), modulo cellular
boundaries.  This torsor is strictly functorial.  A Green function merely
chooses a rational representative, and failure of that choice to commute with
a Cut is necessarily a harmonic cycle obeying a cocycle law.

This resonates directly with the talk's sourced discrete wave equation:
sources and boundary conditions determine a solution only after the harmonic
sector has been handled.  The new claim that the same derived divergence
resolution appears in both six-point QTDS polarity transport and marked-theta
Ward transport is a Marici inference, not a statement made in the talk.  Its
decisive test is a typed source-and-symmetry comparison, not another equality
of inverse-Laplacian matrices.

That carrier test now has a positive answer at six points. The two canonical
scalar polarity tripods are cones on the same three-channel set. Their union
is the suspension

\[
K_{2,3}=S^0*R_3,
\]

and Mayer--Vietoris identifies a sum-zero QTDS contact vector with an integral
Ward circuit. Equivalently, the two scalar contact primitives have the same
boundary and their difference is the suspended circuit. The construction is
equivariant under the full hexagon dihedral group.

This is unusually faithful to the talk's carrier-first method: the graph and
its homology are forced by gluing two elementary scalar pieces before an
amplitude formula is applied. The proposed interpretation of this circuit as
part of the physical first-jet Ward dictionary remains a Marici hypothesis;
the existing QTDS pole Cut and marked-theta topological Cut do not yet share a
typed target.

The suspension algebra itself is now exact for every number of roads:

\[
H_1(S^0*R_m;\mathbb Z)
\cong
\operatorname{sgn}_{S_2}\boxtimes
\widetilde H_0(R_m;\mathbb Z).
\]

This is a Marici theorem about the abstract carrier, not a claim made in the
talk. The scalar falsifier shows more structure than an arity sequence. At
eight points, connected rank-zero/rank-one fibers give two disjoint
eight-road stars; a global \(K_{2,8}\) appears only after collapsing
disconnected fibers and is not canonical. Every marked physical boundary
nevertheless recovers \(K_{2,3}\). More generally, cutting creates independent
regional polarity choices. The relevant object is the full core-incidence
diagram and its higher homotopy, not one \(K_{2,m}\) per multiplicity.
Conceptually, the source now has two distinct descendants. Solving its
divergence gives a flow torsor; gluing the two local solutions gives a
Mayer--Vietoris transgression class. This suggests that some physical sectors
may be Cech/descent obstructions between local amplitude dictionaries, rather
than values of strict global operators on an already-evaluated amplitude.
That inference extends the talk's carrier/dictionary distinction; it is not
contained in the transcript.

The coefficient comparison has also sharpened. The two complementary
scalar-scaffolded three-gluon residues agree on their common conductor, and
their polarity-odd relative normal symbol gives exactly the QTDS contact
matrix. Suspending that matrix gives the complete marked-theta Ward-kernel
map. This is the first exact relation between two distinct scalar normal
operations. It remains a Marici result: the talk motivates looking for the
carrier and dictionary, but does not state this normalization/conductor
construction or its pending BRST/Cut lift.

The next octagon audit reinforces the talk's warning not to infer geometry
from a compact final formula. The honest connected-fiber rank-two carrier is
homotopy equivalent to

\[
S^0*\operatorname{Quad}_8\simeq K_{2,12},
\]

with roads indexed by full quadrangulations. It is not the previously guessed
Möbius carrier. The Möbius complex instead resolves compatibility relations
among those roads. Thus the scalar carrier has at least two geometric axes:
polarity descent and quadrangulation coherence. Their coincidence in the
six-point triangle was exceptional. This is a Marici inference and exact
low-arity theorem, not a claim stated in the talk.
