# Positive-Gram support packet (marici.Figueiredo continuation)

Date: 2026-08-20. This packet consolidates the exact support-level result
after the sparse-chart phase was shown not to descend to the physical flavor
quotient.

## Established finite result — corrected orientation scope

The 18 originally chosen nine-link representatives separate into fourteen
with numerical physical witnesses and four structurally excluded
representatives, numbered 1, 3, 8, and 12. This is **not** a complete
physical support census: the original enumeration quotiented by
\(Y_u\leftrightarrow Y_d\), whereas physical feasibility is sector-labelled.
Removing that exchange gives 36 \(S_3^3\)-orbits, with no exchange-fixed
orbit. The exchanged 18 orientations have now all been audited: fourteen
have physical witnesses and four—again 1, 3, 8, and 12—have independent
exact central-point exclusions. The first swapped-orientation pilot was
already decisive against extending the
18-representative separator by fiat: exchanged orbit 4 has an explicit
\(\chi^2=3.363\) physical witness even though the down-specific combinatorial
rule changes truth value after the swap. Thus the rule is a summary of the
tested orientations, not an orientation-free support law.

A second correction is equally instructive. The swapped orbit-2 numerical
pilot found no minimum, but exact Gram elimination reconstructs a unique
\(\alpha=|a|^2\) for the support
\[
Y=\begin{pmatrix}a&0&b\\c&d&0\\e&f&0\end{pmatrix}
\]
and all six squared magnitudes are positive for every row labeling. An
explicit factor satisfies \(YY^\dagger=H_u\) to \(2.6\times10^{-79}\).
Hence swapped orbit 2 is physically realizable and the no-fit result was an
optimizer miss. Positive-Gram construction is strictly stronger evidence
than absence of numerical minima.

The remaining swapped pilot misses also admit exact certificates. Swapped
orbit 1 requires an off-diagonal entry of
\(V^\dagger\operatorname{diag}(y_u^2,y_c^2,y_t^2)V\) to vanish; conservative
rational triangle bounds exclude all three column pairs. Swapped orbit 3
fails the same intrinsic zero-diagonal Gram inequality, now evaluated on
that up-sector Gram, for all six basis labelings. Swapped orbits 8 and 12
still force an exact CKM zero. Thus the complete oriented central-point
census is fourteen viable and four excluded in each orientation, but the
individual proofs are sector-typed and cannot be identified by exchange.

- Orbit 1 is excluded exactly by a forced off-diagonal zero in the down Gram
  matrix together with exact rational triangle bounds on CKM row pairs.
- Orbit 3 is excluded by the exact positive-Gram cone. For
  \(Y_d=\begin{psmallmatrix}0&a&b\\c&0&d\\e&f&0\end{psmallmatrix}\), let
  \(A,B,C\) be the diagonal Gram entries and \(p,q,r\) the squared
  off-diagonal magnitudes. Realizability is equivalent to the existence of
  \(p/B<y<A\) satisfying
  \[
  C=\frac{r}{B-p/y}+\frac{q}{A-y}.
  \]
  Strict convexity gives the exact necessary and sufficient inequality
  \[
  C(AB-p)\ge rA+qB+2\sqrt{pqr}.
  \]
  Every row labeling fails at the central CKM point, and all 64 CKM-compatible
  corners of the quoted three-sigma box remain outside the cone.
- Orbits 8 and 12 force exact CKM zeros because their support graphs isolate
  orthogonal sector eigenvectors.

On the 18 originally chosen orientations, the resulting exact discriminator is
\[
\boxed{\text{excluded}\iff
\min_j\deg_{Y_d}(j)\ge2\quad\text{or}\quad
z(H_d)\ge2,}
\]
where \(z(H_d)\) counts structurally forced off-diagonal zeros of
\(H_d=Y_dY_d^\dagger\). It classifies those 18 orbit representatives, but
is not an orientation-free law: the swapped certificates use the up Gram or
forced CKM-zero incidence instead. It is also not asserted for support
families outside this census. A
depth-two leave-one-out refit predicts 17 of 18, missing the unique held-out
feature combination at orbit 1.

## Interpretation

The invariant structure exposed by the failure is semialgebraic, not the
chart holonomy \(\phi\). Sparse support maps positive edge magnitudes into
the positive Hermitian Gram cone; physical masses and CKM data select a
point in that cone. Excluded textures fail because the point lies outside
the support image or on a forced-zero incidence stratum. The observed
\(\pi/8\)-type phase clusters remain properties of the viable sparse
presentation ensemble unless a weak-basis invariant is shown to detect
them.

The first boundary elimination is now exact for the six-link zero-diagonal
support. With squared edge variables \((x,y,z,w,v,t)\), its Gram map is
\[
(A,B,C,p,q,r)=(x+y,z+w,v+t,yw,xt,zv).
\]
Writing
\[
L=ABC-Ar-Bq-Cp,
\]
the interior critical-value wall is
\[
\boxed{\Delta_{\rm Gram}=L^2-4pqr=0},\qquad L\ge0,
\]
and the realizable side is \(L\ge2\sqrt{pqr}\). This is independently
certified in two ways: it is the discriminant of the eliminated fiber
quadratic, and its pullback is exactly
\[
\Delta_{\rm Gram}\circ F=(tyz-vwx)^2
                  =\det(dF)^2.
\]
Thus the wall is not fitted from the viable/excluded labels. It is the
intrinsic critical-value locus of the positive Gram map. Its source equation
balances the two alternating products of edge moduli; the loop phase remains
a separate chart coordinate. Coordinate faces supply additional incidence
boundaries and must not be folded into this interior discriminant.

An exploratory ensemble audit then compared the folded loop phase with the
source-defined alternating modulus imbalance
\[
\rho=\left|\log\frac{\prod_{e\ {\rm even}}|Y_e|}
                         {\prod_{e\ {\rm odd}}|Y_e|}\right|.
\]
After removing symmetry/search duplicates, 227 viable minima remain. The
phase–imbalance correlation is strong both globally
(Pearson \(r=0.695\), Spearman \(r_s=0.628\)) and after subtracting each
oriented-orbit mean (Pearson \(r=0.446\), orbit-preserving permutation
\(p<10^{-4}\)). The highest \(\rho\) quartile assigns all 57 minima nearest
to the \(3\pi/8\) nominal cluster, with phase standard deviation \(0.020\)
radians.

This is evidence that the phase histogram is coupled to sparse-chart modulus
geometry, not evidence for a physical invariant or UV quantization. A
subsequent exact Jacobian census makes the distinction sharp. Of the 20
oriented supports having square phase-free monomial Gram maps, the
alternating-balance binomial divides the Jacobian in exactly two cases:
original and swapped orbit 3, the already excluded zero-diagonal texture.
For all 18 viable square charts the Jacobian determinant is only a coordinate
monomial and is therefore nonzero throughout the positive interior.

Thus the observed phase–\(\rho\) correlation is regular chart/readout
coupling, not distance to a universal singular carrier wall. The
zero-diagonal discriminant is support-specific. The six overdetermined
phase-free maps are also now closed: every one has a coordinate-monomial
maximal minor, hence full rank throughout the positive interior. Altogether
24 of the 28 viable oriented classes are certified regular in phase-free
Gram coordinates.

The four remaining viable classes are original and swapped orbits 0 and 2.
They lie among the ten phase-sensitive supports, where a Gram
off-diagonal contains a coherent sum of two edge products. Their correct
map retains the loop coefficient through the rephasing-invariant coordinate
\(\operatorname{Im}(H_{01}H_{12}H_{20})\), together with the three Gram
diagonals and three off-diagonal norms.

The exact \(10\times10\) Jacobians are generically full rank in all four
cases. In the folded chamber \(0\le\phi\le\pi/2\), orbit 0 is strictly
regular throughout the positive interior. Orbit 2 can lose rank only at
\(\phi=0\) together with an exact equality of two edge-product moduli.
Consequently none of the nominal \(\pi/8,\pi/4,3\pi/8,\pi/2\) clusters is
a critical-value wall. All 28 viable oriented classes are regular near the
observed clusters. The phase structure must therefore live in the regular
coefficient/readout map or in the induced sampling measure, not in a
singular carrier stratum. The other six phase-sensitive classes are the
already excluded orientations 1, 8, and 12.

A local profile-Jacobian audit separates readout sensitivity from a flat
optimizer direction. At 219 deduplicated viable minima, the standardized
17-observable Jacobian has rank ten everywhere. After projecting the phase
column off the span of all nine log-magnitude columns, the median retained
information fraction is \(0.906\). Hence magnitude retuning cannot generally
mimic the phase response. The result is numerically stable under halving the
finite-difference step: 218 of 219 records agree within \(10^{-3}\), with a
single 2.8-percent outlier.

The profiled phase information decreases very strongly with folded phase:
global Pearson \(r=-0.904\), Spearman \(r_s=-0.969\), and
within-oriented-orbit Pearson \(r=-0.948\). Thus the readout genuinely
selects and weights the phase coordinate inside each sparse lens; the
clusters are not merely unconstrained optimizer drift. This still does not
make \(\phi\) a function on the weak-basis quotient: different sparse lenses
can represent the same physical point. The typed conclusion is therefore
\[
\boxed{\text{sparse lens + physical readout selects phase,
but phase does not descend globally}.}
\]

The global fiber is now typed more precisely. Four previously identified
same-chart doublets have physical-observable separation below
\(5.1\times10^{-7}\) standard deviations while reaching phase separation
\(0.469\) radians and large magnitude-coordinate separation. Both endpoints
of every doublet have rank-ten local observable Jacobians (transported across
the declared \(S_3^3\) chart symmetry where deduplication removed a repeated
representative). Therefore the multiplicity is neither a flat direction nor
a singular fold:
\[
\boxed{\text{the lens/readout map is locally immersive but globally
noninjective}.}
\]
The observed phases label distinct regular sheets over essentially the same
physical point. Their ten-dimensional observable tangent spaces coincide:
the largest principal angle among all four doublets is below
\(3.0\times10^{-8}\) radians. Since each sheet is full rank onto the same
local physical manifold, the inverse-function theorem supplies a local
transition map between the sheets. The induced first-order arrows have now
been computed explicitly. They intertwine the endpoint observable Jacobians
with relative residual at most \(1.95\times10^{-9}\), and the forward/reverse
derivatives compose to the identity with residual at most
\(1.55\times10^{-14}\). Their determinants are nonzero (between \(1.003\) and
\(1.904\) on the four certified doublets). Thus these are genuine local
differential groupoid arrows, not merely coincident tangent subspaces. This
does not yet give a global deck group: the transitions must still be continued
around loops and checked for path independence and monodromy.

As a first continuation test, each of the four arrows was transported around
contractible two-parameter loops at radii \(10^{-4},2\times10^{-4}\), and
\(4\times10^{-4}\). All twelve continuations returned to their initial
sheet: the worst parameter return residual was
\(1.98\times10^{-10}\), while the worst standardized observable residual
was \(3.29\times10^{-8}\). Thus no local holonomy is detected at these
scales. This is a radius-replicated local null result, not a proof of global
trivial monodromy; a noncontractible loop must be tied to a derived
discriminant component.

The first candidate linked component has also been typed exactly. For
phase-sensitive orbit 2, at the balanced positive point
\[
\phi=0,\qquad m_5m_8=m_6m_7,
\]
the ten-coordinate invariant map has rank nine, not rank eight. Its intrinsic
kernel and cokernel are both one-dimensional. Along the exact straight null
line, the cokernel-projected Taylor series vanishes at orders two and three
and begins with
\[
16t^4+\frac{32}{3}t^6+\cdots.
\]
Thus the tempting complex-square/corank-two interpretation is falsified. An
exact Lyapunov--Schmidt reduction then removes the apparent quartic germ: the
reduced cokernel series vanishes through order six. In fact this vanishing is
exactly geometric. At \(\phi=0\), all ten invariants are constant on the
positive family
\[
\begin{aligned}
(m_3,m_4,m_5,m_6,m_7,m_8)
=\bigl(&r,\sqrt{2-r^2},r^{-1},\sqrt{2-r^{-2}},\\
       &r^{-1},\sqrt{2-r^{-2}}\bigr),
\qquad 2^{-1/2}<r<2^{1/2}.
\end{aligned}
\]
The provisional \(A_3\) interpretation is therefore superseded. This locus
is a one-dimensional positive fiber collapsed by the invariant readout, not
a finite branched cover and hence not a source for ordinary deck monodromy.

A complete join against all four observed same-chart doublets then closes the
finite-branch possibility in their positive interiors. The two orbit-0
doublets lie in a chart whose exact phase-aware Jacobian is strictly positive
there. Orbit 11 has a coordinate-monomial Gram Jacobian and can lose rank only
on an edge-zero face. Orbit 2 is the collapsed continuous fiber above.
Therefore
\[
\boxed{N_{\rm finite\ interior\ branch}=0}
\]
for the observed doublets. Their certified local differential arrows are not
currently restrictions of an ordinary branched deck cover.

The equal-readout fiber product supplies the correct replacement. At every
doublet,
\[
\operatorname{rank}[J_0,-J_1]=10,
\qquad
\dim T(X\times_{\mathcal O}X)=20-10=10.
\]
The tangent kernel is the graph of the previously computed transition
derivative, with relative residual below \(1.95\times10^{-9}\). The smallest
gap between the tenth and eleventh singular values is
\(3.69\times10^7\), so the dimension statement is numerically well
separated. Hence all four doublets lie on positive-dimensional local
correspondence components; none is an isolated transverse self-intersection.

A first global slice was then continued in both phase directions from every
doublet. After normalizing the stored unfolded phase charts and using an
adaptive corrector, all eight scans reached their declared displacement
limits of \(0.75\) radians. The worst standardized observable residual was
\(1.52\times10^{-7}\), while the smallest source--partner parameter distance
remained \(9.78\). Thus these branches remain decisively off the diagonal
over a substantial phase interval; they are not tiny local coincidences. The
scan limit is artificial, so this does not yet identify a natural endpoint.

Continuation toward a source-defined coordinate face does identify the first
natural boundary. In each chart the smallest source edge was suppressed by
ten logarithmic units. All four partners remained solvable and bounded. Their
smallest magnitudes vanished with fitted log slope in
\[
[-1.000000000004,-0.997719],
\]
and the limiting partner/source vanishing ratio lay in
\([1.0000,1.0229]\). Hence the off-diagonal correspondence compactifies onto
the same lower-support coordinate face on both factors. It does not blow up,
hit the diagonal in the positive interior, or terminate at an unexplained
rank defect.

The induced boundary arrows are not declared chart symmetries. A complete
enumeration of the \(216\) elements of \(S_3^3\) gives:

- two arrows delete the same labelled edge on both factors, but their only
  support automorphism is the identity and their surviving log magnitudes
  differ by \(5.604\);
- two arrows delete different edges and the resulting labelled lower
  supports are not isomorphic under \(S_3^3\).

Hence zero of the four limiting arrows is a permutation-plus-rephasing
candidate. That conclusion concerns only the declared sparse chart groupoid;
it does not exclude the full weak-basis group.

The full \(U(3)^3\) test supplies the required correction. Singular-value
gauges and diagonal CKM phase alignment construct explicit common-left and
sector-right unitary intertwiners for all four limiting arrows. Their worst
relative Yukawa residual is \(7.61\times10^{-12}\), and their worst unitarity
residual is \(1.91\times10^{-15}\). Thus the boundary correspondences are
non-monomial weak-basis transitions between sparse presentations. They are
not new coefficient laws. What is new is only their realization inside the
sparse lens, where the restricted \(S_3^3\)-plus-rephasing groupoid cannot
see them.

The infinitesimal stabilizer calculation makes this geometry precise. At all
eight limiting boundary textures (source and partner for four arrows), the
full weak-basis stabilizer has dimension two: the generic common phase plus
the additional null-state phase created by the rank-two boundary Yukawa. The
weak-basis orbit therefore has dimension \(27-2=25\). Its intersection with
the ambient complex sparse-support tangent has dimension seven. However,
after imposing the actual real-positive one-phase gauge used by the texture
chart, the tangent intersection dimension is exactly zero in every case.

Thus each sparse chart is transverse to the weak-basis orbit. The paired
presentations are discrete, separated intersections of the same orbit,
connected by a weak-basis path that leaves the sparse gauge slice and later
re-enters it. This is analogous to a Gribov-copy phenomenon for the sparse
lens: local gauge fixing is valid, but not globally unique.

The finite stabilizer double-coset audit separates the four arrows further.
Using the product chordal metric on \(U(3)^3\) and minimizing over the
two-dimensional stabilizers at both endpoints gives
\[
3.0655863,\qquad 3.4698496,\qquad 3.5611197,\qquad 3.9925039.
\]
Three independent global-search seeds agree within
\(5.42\times10^{-13}\), whereas the smallest separation between distinct
values is about \(9.13\times10^{-2}\). Since this minimized distance is a
double-coset invariant, the four arrows lie in four distinct weak-basis
transition classes. The sparse multiplicity is therefore not one universal
hidden rotation repeated in different charts.

A genuine three-object composition audit now upgrades the pairwise picture
to a weak-basis groupoid. Three distinct sparse representatives, drawn from
orbits 2, 11, and 13, agree pairwise in the physical observables to at most
\(1.44\times10^{-8}\) standard deviations. Explicit \(U(3)^3\) arrows for
all three ordered edges have relative Yukawa residual at most
\(1.29\times10^{-11}\). The composed action has residual
\(9.49\times10^{-12}\), and the direct and composed arrows agree modulo the
generic common-phase stabilizer with product-chordal residual
\[
\boxed{1.46\times10^{-15}}.
\]
Thus the sparse Gribov copies carry an honest weak-basis groupoid
composition law; they are not merely unrelated pairwise coincidences. This
does not make the complete graph of all weak-basis-equivalent presentations
the source-defined sparse incidence graph. Identifying its canonical
generators still requires boundary/incidence data rather than arbitrary
pairwise equivalence.

The first finite incidence census makes that gap quantitative. On the
61-point fiber, maximally closing every same-orbit/same-phase class under the
declared \(S_3^3\) action and adjoining all four certified same-chart
multisheet arrows gives only 27 spanning generators and leaves
\[
\boxed{34\text{ connected components}.}
\]
The component sizes are \(6,4,4\), sixteen copies of size two, and fifteen
singletons. The census is unchanged when the phase-group tolerance varies
from \(10^{-5}\) to \(10^{-7}\). Because the \(S_3^3\) closure was granted
optimistically without demanding an individual parameter-transport witness,
this is a conservative disconnection result: at least 33 additional
source-defined incidence edges are required to connect the fiber. Full
\(U(3)^3\) equivalence cannot fill this role without making the graph
complete by definition.

The complete codimension-one support atlas then separates carrier eligibility
from actual incidence. Deleting each of the nine nonzero entries at all 61
vertices gives 549 face occurrences and 67 sector-preserving
\(S_3^3\)-canonical face types. Sixty face types occur in more than one of
the 34 components. The resulting carrier-eligibility graph has 442 component
pairs and is connected. Therefore
\[
\boxed{\text{common boundary support is abundant but nonselective}.}
\]
A deterministic maximum-support spanning tree reduces the next readout audit
to exactly 33 face witnesses. Each still requires normalized boundary
readout and continuation compatibility; no edge in that tree is yet an
admitted sparse incidence arrow.

A depth-ten normalized-readout pilot on those 33 witnesses produces a second
separation. Thirty continuations preserve the complete 17-observable readout
to final \(\ell^2\) residual at most \(3.11\times10^{-5}\), but only four
also drive the nominated target edge to the common face. Their derived log
normal slopes are
\[
-0.9710,\qquad -1.0061,\qquad -0.8221,\qquad -1.0000.
\]
Twenty-six solvable continuations escape through another target direction,
and three fail before depth ten. Thus even
\[
\text{common support face}+\text{continued equal readout}
\]
is insufficient: the normal valuation must also agree. The four survivors
remain candidates rather than admitted arrows because the deterministic tree
selects one occurrence of each face and does not exhaust alternative
vertex/deletion witnesses.

The exhaustive infinitesimal census covers 3,019 concrete shared-face
occurrence pairs. All tangent readout equations solve with worst relative
residual \(4.48\times10^{-8}\). Even at the strict reciprocal unit-normal
window \(|s+1|\le0.05\), 567 occurrence pairs survive, representing 177
component edges, and their graph connects all 34 components. Thus first-order
normal compatibility is also abundant rather than selective.

Nonlinear continuation of the best-conditioned 33-edge strict spanning tree
then restores discrimination. At log depth ten, 24 edges remain solvable, but
only 20 track their nominated face with near-unit finite normal valuation;
four exit through another face and nine fail. Since a spanning tree has no
cycles, the 20 surviving edges leave a 14-component forest. This is not yet a
global disconnection theorem: the unused strict tangent graph contains 144
alternative component edges that may reroute the failed cuts.

That rerouting census is now complete for the best-conditioned witness on all
177 strict component edges. Ninety-four reach depth ten, 53 track the
intended face nonlinearly, and 41 preserve readout while exiting through a
different face; 83 fail. The 53 surviving edges form four components of
sizes
\[
\boxed{30,\ 2,\ 1,\ 1}
\]
in the prior 34-component quotient, corresponding to \(57,2,1,1\) of the
original 61 presentations. The exceptional charts are:

- orbit 7, member \((417,334)\), \(\phi=0.8192714391\), paired only with
  orbit 5, member \((401,421)\), \(\phi=1.5567685591\);
- isolated orbit 9, member \((116,481)\), \(\phi=1.1870327109\);
- isolated orbit 4, member \((226,468)\), \(\phi=1.5661289519\).

This is still a bounded numerical classification, not a proof of four exact
physical sectors: it used depth ten, a five-percent infinitesimal prefilter,
and the best occurrence per component edge.

The island-only occurrence audit removes most of that apparent splitting.
Exhausting every strict occurrence incident to the three islands leaves the
same four components, but widening the reciprocal tangent window to twenty
percent and testing both arrow orientations joins the doublet and the orbit-4
singleton to the dominant component. The final bounded decomposition is
therefore
\[
\boxed{60+1}.
\]
The only remaining presentation is orbit 9, member \((116,481)\), with phase
edge \((d,0,0)\) and \(\phi=1.1870327109\). Its best bidirectional candidate
to component 9 follows the nominated face through depth ten, but the fitted
normal order is only about \(-0.73\), rather than \(-1\). Extending this one
audit to depth twenty makes the order drift farther away (about \(-0.39\)
forward and \(-0.54\) backward) before the numerical solve terminates. Thus
the remaining singleton is not a hidden unit-normal bridge at the tested
depths. Directionality was essential to the other mergers, so this remains
a bounded nonlinear isolation statement, not an exact sector theorem.

The exact local chart calculation closes that final numerical gap. Write the
orbit-9 down texture near its nominated face as
\[
Y_s=\begin{pmatrix}a&0&0\\0&0&b\\e&c&d\end{pmatrix},
\qquad r^2=c^2+e^2.
\]
The neighboring \((116,405)\) chart has the representative
\[
Y_t=\begin{pmatrix}ac/r&0&ae/r\\0&b&0\\0&d&r\end{pmatrix}.
\]
Direct symbolic reduction gives
\[
Y_sY_s^\dagger=Y_tY_t^\dagger,
\qquad
\frac{(Y_t)_{02}}{(Y_s)_{20}}=\frac{a}{r}.
\]
Thus the two down textures differ only by a right-handed unitary change of
frame, the phase on \(a\) transports to the target phase edge \((d,0,2)\),
and the boundary valuation is exactly one whenever \(a,c\ne0\). The apparent
orbit-9 singleton is therefore an optimizer-path artifact. This exact arrow
closes the only gap left by the bounded continuation graph, so that graph now
contains all 61 presentations. It does not retroactively exactify the other
numerically continued arrows. No extra coefficient/readout sector is licensed
by the present census.

There is now an independent exact global certificate. Of the 67 canonical
eight-link faces, 28 are connected on the full nine-vertex
\(Q\!\sqcup u\!\sqcup d\) graph. Each therefore has eight edges on nine
vertices and is a tree. Such a face has no loop holonomy: after transporting
its support by an explicit \(S_3^3\) permutation, every edge phase is removed
or relocated by vertex rephasing. The connected-face incidence graph contains
391 component pairs, and a deterministic 33-edge spanning tree connects all
34 original sparse-fiber components. Thus exact support permutations and
rephasings—not the optimizer continuations—prove that all 61 presentations
belong to one codimension-one carrier groupoid. The numerical calculations
remain diagnostics of particular fitted sections through that groupoid.

The first coefficient-line descent test does not inherit this connectivity.
For every pair of occurrences over a common boundary tree, transport the
deleted edge to canonical support and ask whether the two normal edges lie in
the same orbit of the tree's \(S_3^3\) automorphism group. This is the exact
gate for identifying the two one-parameter smoothings without adding an
incidence kernel. Only 28 of the 391 carrier component pairs pass. Their graph
has 14 components of sizes
\[
3,3,3,3,3,3,3,3,2,2,2,2,1,1.
\]
Thus carrier connectivity does not canonically trivialize the normal/phase
coefficient line. This is not yet a theorem that the coefficient object has
14 physical sectors: a source-derived map between inequivalent smoothing
normals could still join them. It is an exact falsification of the naive
identity-gluing coefficient lens.

The predeclared labelled incidence pairing supplies the missing nontrivial
kernel. For a boundary tree \(T\) and smoothing normal \(e\), let \(c_e\) be
the signed fundamental cycle in \(T\cup\{e\}\). Pair two smoothing lines by
the ordinary signed edge-occurrence contraction
\[
K_T(e,f)=\langle c_e,c_f\rangle.
\]
Allowing the exact automorphisms of \(T\), this kernel is nonzero on 370
carrier component pairs and contains a 33-edge spanning tree across all 34
components. Hence the labelled coefficient occurrence module is connected,
but by a genuine incidence kernel rather than identity gluing. This remains
upstream of physics: the contraction has not yet been shown to descend to a
weak-basis-invariant selection/readout map.

The existing exact rational weak-basis rotation supplies that final descent
test negatively. It preserves every audited weak-basis invariant while taking
the nine-link support to a twelve-link support. The labelled edge module—and
hence the contraction \(K_T\)—is then not defined invariantly on the same
physical orbit. Therefore the fundamental-cycle kernel is a canonical
coefficient map inside the sparse presentation groupoid, but it does not
descend by itself to physical flavor space. A physical selection map must
factor it through independently weak-basis-invariant data; the sparse cycle
pairing cannot serve as the readout.

This is the concrete mathematical sense in which a lens–readout combination
can produce a multiplicity of presentations without that multiplicity
becoming a quotient-level physical observable.

## Sharp next calculation

The complete oriented carrier census, local sheet derivatives,
contractible-loop continuation, branch-source join, and tangent
correspondence calculation are now available. The ordinary deck-cover and
isolated-crossing hypotheses are both falsified for the observed doublets.
The off-diagonal correspondence also persists through all eight bounded phase
scans and has now been followed asymptotically to a common coordinate face.
Its induced boundary arrows fail the complete \(S_3^3\)/rephasing candidate
test but pass the full weak-basis equivalence test. The stabilizer and tangent
intersection show that the gauge-fixed sparse slice is transverse but
globally nonunique; the finite double-coset audit separates four arrow
classes; and a three-representative test now verifies groupoid composition
modulo the common stabilizer. The next calculation is to derive the minimal
source-defined incidence graph and generators among the known fiber
representatives. Arbitrary pairwise weak-basis equivalence would produce a
complete graph and therefore cannot supply that missing sparse geometry.
The codimension-one carrier atlas is complete and connected, so support
matching alone cannot discriminate. Occurrence exhaustion, a wider tangent
window, both arrow orientations, and a depth-twenty audit reduce the nonlinear
classification to one dominant 60-presentation component and an apparent
orbit-9 singleton. The row-Gram transition removes that local artifact, while
the connected-tree-face certificate exactifies the global carrier statement
without relying on any fitted continuation. The sharp next calculation is
now coefficient-level: transport the one-loop phase line through the exact
33-edge tree and test the fundamental cycles created by the remaining exact
tree-face arrows. Any nontrivial cocycle belongs to the lens/readout data, not
to disconnected carrier geometry.

Evidence:

- `checkers/wp10_orbit1_exact_obstruction.py`
- `checkers/wp10_orbit3_gram_criterion.py`
- `checkers/wp10_orbit3_gram_3sigma_box.py`
- `checkers/wp10_support_cone_census.py`
- `checkers/wp10_support_combinatorial_discriminator.py`
- `checkers/wp10_swapped_exact_obstructions.py`
- `checkers/wp10_swapped_orbit3_gram_criterion.py`
- `checkers/wp10_oriented_pilot_census.py`
- `checkers/wp10_zero_diagonal_gram_discriminant.py`
- `checkers/wp10_phase_cycle_balance_audit.py`
- `checkers/wp10_oriented_gram_map_inventory.py`
- `checkers/wp10_square_monomial_gram_jacobians.py`
- `checkers/wp10_phase_aware_invariant_jacobians.py`
- `checkers/wp10_local_phase_identifiability.py`
- `checkers/wp10_regular_multisheet_fiber.py`
- `checkers/wp10_orbit2_branch_jet.py`
- `checkers/wp10_doublet_branch_source_census.py`
- `checkers/wp10_boundary_correspondence_symmetry.py`
- `checkers/wp10_boundary_weak_basis_equivalence.py`
- `checkers/wp10_boundary_weak_basis_stabilizer.py`
- `checkers/wp10_weak_basis_groupoid_composition.py`
- `checkers/wp10_sparse_fiber_incidence_graph.py`
- `checkers/wp10_sparse_fiber_face_atlas.py`
- `checkers/wp10_sparse_fiber_boundary_readout_pilot.py`
- `checkers/wp10_sparse_fiber_normal_response_census.py`
- `checkers/wp10_sparse_fiber_strict_normal_continuation.py`
- `checkers/wp10_sparse_fiber_nonlinear_component_classification.py`
- `checkers/wp10_orbit9_exact_boundary_transition.py`
- `checkers/wp10_exact_tree_face_spanning_groupoid.py`
- `checkers/wp10_tree_face_normal_line_compatibility.py`
- `checkers/wp10_tree_face_fundamental_cycle_kernel.py`
- corresponding JSON packets under `research/flavor/results/`
