# Dependency-aware partial-repair compiler

The compiler replaces the free finite-repair permutohedron by the legal path
space of a typed dependency poset. A repair constructor carries its local
defect transition, domain and graph-norm requirements, complete boundary and
support deltas, authority root, prerequisites, residual certificate type, and
capability consumption/production signatures.

For a finite repair poset `(R,<)`, the compiler enumerates precisely its linear
extensions. A listed order may still fail dynamically: every leg is checked
against the actual intermediate defect signature, graph domain, graph norm,
and residual capabilities. An unresolved prefix is retained only as an
`unsafe_repair_in_progress` state with its unresolved defects, next admissible
repairs, and residual capability packet.

## First three exact models

Three independent repairs produce all `3! = 6` paths. Authorized adjacent
swaps connect them into one component and all paths yield one typed endpoint.
This recovers the ordinary permutohedron exactly when the dependency poset is
discrete and all swap gates pass.

Adding `A < B` leaves the three linear extensions

```text
A B C
A C B
C A B
```

Adjacent swaps of incomparable repairs connect these paths. The missing
orders are absent because they are illegal, not because a coherence cell was
forgotten.

The third model has two legal orders and identical scalar endpoint bytes, but
the two composites produce inequivalent graph norms. Its swap gate reports
`repair_swap_domain_failure`; the legal path graph has two components and two
typed endpoints. Scalar equality therefore supplies neither a swap cell nor
endpoint coherence.

The higher comparison boundary is crossed only through a typed
comparison-current channel.

## Braid and anomaly gate

Every nonzero pairwise swap comparison value must carry its own source
authority root and `source_comparison_current` derivation. For a legal triple,
the compiler follows both braid words and subtracts their accumulated
comparison currents. It classifies the first residual as:

- `zero`: strict braid coherence;
- `exact_boundary`: a higher cell only when a source root and comparison cell
  are supplied;
- `central_phase`: a retained determinant/Pfaffian anomaly candidate;
- `domain_mismatch`: one comparison path is not defined;
- `untyped_residual`: rejection, with no fitted killing cell.

The failed-braid model has six legal paths and every pairwise swap cell, but its
two braid composites differ by one unit of comparison current. With no typed
higher witness it is classified `untyped_residual`. A second model has the same
scalar endpoint bytes and the same numerical residual, but a source-rooted
central-phase type; the compiler retains it as an anomaly candidate rather than
calling the paths coherent.

## Residual capability deletion

In the sixth model, both orders are linear extensions of the discrete
dependency poset. `Read;Delete` is dynamically legal. `Delete;Read` is not:
the first constructor consumes `residual_k`, so the second leg fails with
`repair_residual_capability_failure`. This is a domain-of-definition failure,
not a precedence relation inferred after the fact. The missing swap cell is
reported explicitly.

## Theta/Tate declaration barrier

The theta/Tate stages `{S,P,Q,A,L,C,D}` are present as a parameterized packet,
but the compiler assigns them no dependencies. Every stage currently lacks the
source-owned fields

```text
precedes
commutes_with
domain_after
boundary_delta
completion_scope
```

Accordingly the packet status is `source_declarations_required`; path
enumeration, component construction, braid comparison, and endpoint claims are
not performed. In particular, the compiler preserves the questions

```text
P <-> Q?
S <-> P?
L < C?
(P,Q,S,A) < D?
```

as questions. A hostile request to assume the discrete poset or enumerate the
incomplete packet is rejected.

A final refresh of Grothendieck's live notes found a source-native candidate
scale-flow graph norm and an explicit warning that the bulk tail--seam Gram
does not preserve the endpoint trace. This strengthens the need for the
`graph_norm_signature` and boundary-packet swap gates, but it still does not
declare the per-stage precedence, commutation, domain transition, boundary
delta, or completion scope. The seven-stage packet therefore remains correctly
blocked rather than being partially inferred from those analytic results.

## The compiler theorem

Legal staged repairs are dynamically admitted linear extensions of a typed
dependency poset. Adjacent swaps are available only for incomparable repairs
with source-declared commutation and equal complete local packets: boundary,
domain, graph norm, support/fault union, remaining defects, and reconstruction
capabilities. These swaps generate coherence only subject to the typed braid
and anomaly gate. Equal scalar bytes never suffice.

The compiler records two graphs separately. The abstract graph of all linear
extensions is connected under adjacent swaps of incomparable elements, as the
standard poset theorem requires. The dynamically legal, authority-bearing swap
graph is a subgraph: it can split when a domain is absent, a graph norm changes,
a residual capability is destroyed, or source commutation authority is
missing. Only connectivity of the latter establishes coherent construction.

## First theta/Tate repair triangle: `S`, `C`, `L`

The first source instantiation uses seam retention `S`, finite Clark bulk `C`,
and valuation pro-Gram construction `L`. Each carries the ten requested state,
domain, norm, boundary, completion, residual, and authority fields.

The exact cut decomposition authorizes `S` and proves that the seam cannot be
reconstructed from the retained tail:

\[
\|g_p\|\to0,
\qquad
\|h_p\|\to\|\Phi\|_2>0.
\]

The valuation constructor algebra authorizes the finite operational topology
behind `L`, while adjacent analytic atoms collapse and fixed-prime projectors
remain separated. Thus `L` requires both `seam_translation_norm` and
`raw_arithmetic_label`; completing before either is retained is irrecoverable.

The Clark identity authorizes `C` on finite packets:

\[
\|H_a+f\|^2+\|H_{-a}+f\|^2
=2\|G+f\|^2+2a^2\|\partial_zG\|^2.
\]

It does not authorize continuity through completion. Grothendieck's source
correction says the `z` derivative is not the scale-flow endpoint graph norm.
The endpoint is nevertheless controlled—separately—by the native first-order
operator (A_s=-\partial_q+(1-s)):

\[
|G(0)|^2\le {\|G+f\|_2^2\over 1-\Re s}.
\]

This closes ordinary one-sided tail completion escape, but it does not turn
the Clark `z` current into a completion-continuous valuation incidence map.
No fixed finite authorized family `F` uniformly dominating those current
matrices has been supplied, and the valuation/Fock-to-boundary incidence and
completion extension needed by `L` remain absent.

All six formal orders therefore have a typed first failure:

| Order | First rejection |
|---|---|
| `C L S` | `L` lacks the retained seam distinction |
| `C S L` | the common Clark/valuation incidence required by `L` is absent |
| `L C S` | `L` lacks the retained seam distinction |
| `L S C` | `L` lacks the retained seam distinction |
| `S C L` | the common Clark/valuation incidence required by `L` is absent |
| `S L C` | the completion extension required by `L` is not source-authorized |

There are currently zero completed typed paths, zero authorized adjacent swap
cells, and no braid comparison domain. The braid class is
`illegal_factorization`, not a fitted zero or central anomaly.

Backward requirement discharge now isolates the exact frontier. Seam retention
is already constructed and forces the logical precedence `S` before `L`. Two
source constructors remain necessary before even one completed path can be
claimed:

1. the joint rigged arithmetic completion extension on the four-lane boundary
   packet;
2. one fixed finite authorized family uniformly dominating the Clark current
   matrices on the common Clark/valuation module.

The first item no longer conflates finite incidence with completion. Finite
atomic incidence and universal Fourier chart sewing are already authorized.
Their boundary packet is the product of two regularity grades—primitive
exponential/Laplace and square tempered—with two chart parities—even overlap
and odd front. Equivalently, it retains both delta and principal-value boundary
distributions. The chart transform consists of two identical invertible
two-dimensional blocks and has total determinant (1/4). Reflection fixes the
delta/even-overlap channel and reverses the orientation of the
principal-value/odd-front channel.

What remains missing is arithmetic continuity of the joint four-lane packet
through the rigged completion. A delta-only scalarization or a single-grade
surrogate is rejected because either one destroys a source distinction before
the completion constructor can consume it.

The four lanes have unequal completion behavior. In the primitive odd
principal-value lane, translated localized tests carry a generic Hilbert tail

\[
\frac{m_0}{L}+\frac{m_1}{L^2}+\cdots .
\]

Primitive exponential weights make its leading terms fail even the term test.
This lane therefore requires a source-derived relative-moment cancellation
before prime aggregation, followed by exponential control of the remainder.
No finite list of algebraic subtractions is accepted as a replacement. By
contrast, the square-tempered odd lane admits the (1/L) tail.

Thus the missing joint extension contains two explicit primitive-odd
subconstructors: pre-aggregation relative-moment cancellation and exponential
remainder control. Merely authorizing the outer completion while either inner
constructor is absent is rejected.

There is also a no-go theorem for where the first subconstructor can live. A
nonzero compactly supported localized test cannot have every polynomial moment
zero: its Fourier transform is entire, and vanishing of the full moment jet
forces the test itself to vanish. Consequently the required exponential gain
cannot be produced by modifying one test, nor by a finite-rank counterterm.

The only admitted constructor type is therefore an exact relative identity on
the paired-sheet primitive odd current. It must be odd-equivariant under
reflection and must factor the pipeline as

\[
\text{paired source current}
\longrightarrow
\text{tail-cancelled odd current}
\longrightarrow
\text{prime aggregation}.
\]

Endpoint fitting after aggregation cannot create this arrow. The source has to
supply the paired-sheet tail identity itself; that identity remains missing.

The existing finite-shift cocycle is not that identity. For

\[
g_L=\tau_LK-K,
\]

its Fourier transform contains the factor

\[
\left(e^{2\pi iL\xi}-1\right)
\operatorname{pv}\!\left(\frac{i e^{-\pi\xi^2}}{2\pi\xi}\right).
\]

The phase zero cancels the principal-value singularity at the frequency
origin, placing every finite \(g_L\) in the Gaussian bulk. This is an exact
source cocycle and translation acts trivially on the boundary quotient.
Nevertheless the prime label remains in the bulk cocycle. Nothing in the
finite-\(L\) identity controls summation over the label \(L=\log p\).

The compiler therefore separates two axes:

- local Fourier-frequency regularization;
- arithmetic prime-label summability.

The first is proved; the second is not. Treating the phase zero as authority
for arithmetic completion is rejected.

There is a further source-order correction. Global Poisson sewing does not
factor through prime-power sampling. If \(S\) is the sampling map and \(P\)
the Poisson-sensitive source correspondence, there is a smooth variation
\(b\), supported between \(\log2\) and \(\log3\), with

\[
Sb=0,
\qquad
Pb\ne0.
\]

Hence no map reconstructed from the sampled register can equal \(P\). The
missing constructor begins on the full restricted adelic source, forms the
Poisson/Green boundary correspondence there, and only afterward projects to
archimedean, primitive, square, connected, and mixed diagnostics.

The diagnostic projections still form a pro-natural system. For finite prime
cutoffs \(X\subset Y\), their components \(I_X\) must satisfy

\[
\operatorname{res}_{X,Y}\circ I_Y
=
I_X\circ\operatorname{res}_{X,Y}.
\]

Finite labelled registers already exist, but the full-source Hardy comparison
and its compatible diagnostic projections do not. The target must retain three inequivalent
topological grades: projective Mellin-analytic primitive data, Hilbert-tempered
square data, and an absolute-summability connected tail. They cannot be merged
into one Hilbert coordinate or summed into one scalar energy.

Finite-packet joint faithfulness also does not settle the common kernel after
completion. The missing theorem is therefore a full-source Poisson/Green
correspondence, followed by pro-natural diagnostic descent and completion
separatedness—not convergence of a single all-prime series.

Global scalar continuation is not the missing operation either. The adelic
Tate integral, with reciprocal Poisson sewing and its endpoint polynomial,
already gives a source-derived meromorphic section and then an entire scalar
section. The missing constructor is a functorial lift

\[
\text{full adelic source}
\longrightarrow
\text{tail--seam boundary module}
\longrightarrow
\text{Tate scalar readout}.
\]

The composite must equal the known Tate readout, but the first arrow cannot be
reconstructed backward from that scalar function. Its boundary packet must
retain endpoint, archimedean gamma, connected prime-power, and mixed
Poisson--arithmetic components, sewn before continuation.

This lift still does not prove positivity of the completed Green kernel. That
positivity is the Weil/RH condition itself. A noncircular positivity route
would require a larger source-derived positive dilation whose relative Schur
boundary produces the completed current; that dilation remains open.

The lift itself is an extension problem. Write

\[
0\longrightarrow K_{\partial}
\longrightarrow B_{\mathrm{tail-seam}}
\longrightarrow R_{\mathrm{Tate}}
\longrightarrow0.
\]

In bare complex vector spaces this sequence always splits, so ordinary
algebraic \(\operatorname{Ext}^1\) is zero and carries no obstruction. The
operative category consists instead of locally convex modules with
Poisson/reflection action and declared graph domains. Pulling the extension
back along the Tate section gives a continuous, equivariant,
domain-preserving \(\operatorname{Ext}^1\) obstruction to a typed lift. When
that class vanishes,
the set of lifts is not canonically a point: it is a torsor over

\[
\operatorname{Hom}(S,K_{\partial}).
\]

The mixed Poisson--arithmetic channel lies in this scalarization kernel. In
the finite hostile model, the Tate scalar admits a three-parameter family of
boundary lifts; two Green constraints leave one mixed direction; only a full
rank source-derived Green packet selects a unique lift. Full rank fitted from
the desired endpoint still does not supply authority.

Thus existence, uniqueness, and source authority are three separate gates:
vanishing of the pulled-back extension class, elimination of the boundary
kernel torsor, and derivation of the eliminating constraints from the full
source.

The hostile ladder makes the category visible. An algebraic split may be
discontinuous; a continuous split may fail Poisson/reflection equivariance; an
equivariant split may leave the Green graph domain; and a split satisfying all
three conditions may still lack source authority. Only the continuous,
equivariant, domain-preserving, source-authorized case is admitted.

Finite Fourier/reflection equivariance is not an additional obstruction once
a continuous domain-preserving lift exists. If the graph domain is invariant
and scalarization and the Tate map are equivariant, Reynolds averaging gives

\[
\overline L
=
\frac1{|G|}\sum_{g\in G}
g_B\,L\,g_S^{-1}.
\]

Over \(\mathbb C\), the group order is invertible and positive-degree
cohomology of the finite symmetry module vanishes. The average remains a lift,
is continuous, and preserves the invariant graph domain.

Averaging does not select a unique lift. Equivariant lifts form a torsor over
\(\operatorname{Hom}_G(S,K_{\partial})\). Thus symmetry removes the
noninvariant part of the ambiguity, while source Green constraints must still
eliminate the invariant part. Noninvariant domains, nonequivariant
scalarization, or missing averaging authority remain hard failures.

The invariant ambiguity has a finite representation-theoretic classifier. If

\[
S\cong\bigoplus_\lambda m_S(\lambda)V_\lambda,
\qquad
K_{\partial}\cong\bigoplus_\lambda m_K(\lambda)V_\lambda,
\]

then

\[
\dim\operatorname{Hom}_G(S,K_{\partial})
=
\sum_\lambda m_S(\lambda)m_K(\lambda).
\]

Disjoint isotypic support gives uniqueness immediately. Otherwise the Green
packet needs only enough independent source constraints to kill the shared
isotypic multiplicities; constraints on nonshared types are irrelevant. A
claimed constraint rank larger than the invariant torsor dimension is
rejected as fitted overdetermination.

One boundary-side character calculation can already be completed exactly.
For the four-channel Tate--Poisson carrier, scalar aggregation has row
\((1,1,1,1)\), while reciprocal reflection exchanges channels \((0,1)\) and
\((2,3)\). Its three-dimensional scalar kernel therefore decomposes under
\(C_2\) as one even line and two odd lines. Both parities meet the blind
subspace, so reflection covariance alone cannot select a faithful scalar
readout.

This does not yet compute the refined theta source multiplicities. In
particular, the \(C_4\) characters of the five-cell Fourier carrier belong to
a different representation and cannot be transported into the source slot
without a source-derived comparison map. The remaining sharp gate is thus
the refined source character calculation; combined with the now-known
boundary multiplicities, it determines the invariant lift torsor and the
minimal Green constraint packet.

There is nevertheless a conditional finite source theorem. If a cutoff
arithmetic label module (C_X) has dimension (N), carries trivial Fourier
action, and the source authorizes the tensor identification (W\otimes C_X),
then each of the four (C_4) characters of (W) occurs with multiplicity
(N). For a Fourier observer (A_F) and arithmetic-cylinder observer (A_X),

\[
\operatorname{rank}(A_F\otimes A_X)
=\operatorname{rank}(A_F)\operatorname{rank}(A_X).
\]

Thus finite separation is equivalent to ranks (4) and (N) in the two
factors. This theorem is deliberately conditional: it does not determine the
live (C_2) source representation in the four-channel tail--seam extension.
Closing that torsor requires a source-derived equivariant comparison from the
refined tensor carrier to the four-channel lift. Equality of dimensions or
reuse of character names is not such a comparison.

Even granting a provisional common reflection action does not make the
comparison unique. Fourier square fixes the constant--delta plane of (W)
and negates its tail--principal-value plane. Therefore (W\otimes C_X) has
(2N) even and (2N) odd dimensions when (C_X) is Fourier-trivial. The
four-channel scalar kernel has one even and two odd dimensions, so

\[
\dim\operatorname{Hom}_{C_2}
  (W\otimes C_X,\ker\Sigma)
=(2N)(1)+(2N)(2)=6N.
\]

This is a conditional obstruction theorem, not the missing comparison map.
It says that symmetry averaging can make a supplied lift equivariant but
cannot select one: source Green constraints must eliminate a (6N)-parameter
equivariant torsor at cutoff (X). Moreover, identifying Fourier square with
the reciprocal channel involution itself still requires source authority.

The (6N) parameters split into two typed blocks. Maps from the
constant--delta source plane to the symmetric hidden channel contribute
(2N); maps from the tail--principal-value plane to the two odd hidden
channels contribute (4N). Existing labelwise tail equations cannot close
either block across labels: two nonzero endpoint states (a) and (-a) obey
their independent equations while their scalar sum vanishes. Arithmetic
cylinder ports detect that packet but are observers, not relations that
forbid it. Likewise, the existence of primitive and square currents does not
by itself prove that they couple labels.

Consequently the required repair is a source-authorized cross-label
arithmetic coherence locus. At cutoff (X), its independent constraint rank
must reach (6N) to select a unique equivariant comparison, and those
constraint cells must commute with cutoff restriction. This is the first
place where the input, control, and output towers must meet in one horizontal
Ward cell.

There is a further graph-theoretic boundary. Suppose the arithmetic
coherence law is generated by pairwise differences along a graph on (N)
labels with (c) connected components. For each of the six torsor species,
the incidence matrix has rank (N-c). Hence the combined difference law has

\[
\operatorname{rank}=6(N-c),
\qquad
\dim\ker=6c.
\]

Pairwise coherence can synchronize each component but cannot choose its six
componentwise-constant coordinates. A connected prime-scale graph therefore
still leaves six global modes. Unique comparison requires another (6c)
independent anchor conditions, typed as boundary or global source currents.
This separates transport coherence from boundary initialization: neither can
replace the other.

Boundary initialization itself has finite and completed gates. At finite
cutoff, anchor rows must have rank (6c) on the componentwise-constant
residual. At completion, the cutoff-natural anchor family must additionally
retain a uniform positive inf--sup reserve. The centered source operator
(L=\partial_u^2-1/4) does provide a genuine Green mate: it identifies the
completed odd port (R_2+R_3) as a source transform. It does not orient the
naive Hermitian bulk--polar pairing, whose sign is defeated by a positive
scale-atom hostile, and its contribution to the six anchor ranks remains
uncomputed.

Nor can a fixed finite packet of primitive, prime-square, seam, and
archimedean-jet rows close the completion gate. On normalized prime-orbit
Følner packets their combined energy is (O(N^{-1})) while state norm remains
one. The completed comparison therefore needs a nonlocal arithmetic current,
a boundary port transported with nondecaying strength, or an independently
authorized stronger source topology. Finite rank alone cannot establish
completed faithfulness.

The first surviving completion candidate is the full translated seam-history
Gram. Unlike every finite seam trace, it retains positive normalized Følner
blocks: for a prime orbit its norm has lower limit at least
(lVert\Phi\rVert_2^2>0). This tests only the unmodulated, zero-frequency
packet. Arbitrary phases are controlled by the Toeplitz frame symbol

\[
W_p(\theta)=\frac1{\log p}\sum_{m\in\mathbb Z}
\left|\widehat\Phi\!\left(
\frac{\theta+2\pi m}{\log p}\right)\right|^2.
\]

The single-prime completion gate is (inf_\theta W_p(\theta)>0); a modulated
long block near a zero or small value of (W_p) is the sharp hostile. Even
primewise lower bounds do not yet control the all-prime completion or its
cross-prime couplings.

The modular half-density does not bypass these gates. A diagonal reweighting
inside one carrier is a gauge change when coefficients transform
contragrediently, and otherwise changes the Mellin section. Its only live
source meaning is a relative comparison between independently typed additive
Haar and multiplicative Haar sectors. That comparison is not yet authorized.
Finally, a frame lower bound supplies state faithfulness, not the sign of its
attachment in the global Green identity; orientation remains an independent
control-tower gate.

These axes now assemble into a finite strict model of the fourth-tower
dependency nerve. Its indexing category is an authorized subcategory of

\[
\text{symmetry}\times\text{label incidence}\times\text{cutoff restriction}.
\]

The one-skeleton contains the three classes of admissible arrows. The
two-skeleton requires symmetry--label, symmetry--cutoff, and label--cutoff
squares. Pairwise faces do not imply the three-dimensional
symmetry--label--cutoff cube. Boundary anchoring is then a fiber condition
that must itself be natural over the complete cube; derived inverse-limit
completion and Green realization occur only afterward.

This gives an exact counterexample to determining the fourth tower from the
largest lower rung number. Three lower axes of height one can be locked to a
diagonal, have two independent directions, or vary independently. Their
dependency nerves then have depths one, two, and three respectively, despite
identical lower heights. The combinatorial invariant is the dimension of the
authorized dependency nerve. This strict cube is only the finite audit: weak
actions or nontrivial compositors require the already separate triangle and
pentagon anomaly gates.

### Spacetime coherence reversal: first hostile gate

The categorical reversal has two source-supported ingredients. In a
cobordism category, ((d-1))-manifolds are objects and (d)-dimensional
cobordisms are morphisms. In canonical gravity, hypersurface-deformation
brackets encode consistency among slicings on the constraint-and-equation
system. This makes a foliation parameter a presentation coordinate, not the
authority that supplies coherence.

Those facts do not derive (3+1) Lorentzian spacetime. The dimension shift is
the general (d-1\to d) cobordism pattern; a (2+1) example has it as well.
A four-dimensional Euclidean or purely topological cobordism has the same
object--morphism dimension shift without a Lorentzian causal cone. Moreover,
hypersurface deformations are not automatically identical to spacetime
diffeomorphisms off the constraint and equation domain.

The next admissible constructor is therefore a source-derived representation
of the hypersurface-deformation algebroid on the tower comparison carrier. It
must derive the normal--normal bracket's inverse-spatial-metric structure
function, fix the signature sign independently of basis gauge, state its
on-shell or off-shell domain, satisfy refoliation higher coherence, reconstruct
the causal cone from principal-symbol or equivalent metric data, and supply
an independent reason for three spatial dimensions. Until those gates pass,
the (3+1) match remains a conditional structural analogy.

The first exact algebra audit uses affine lapse--shift pairs ((N,M)) and a
constant structure coefficient (eta). Its bracket is

\[
[(N_1,M_1),(N_2,M_2)]
=
\left(
M_1N_2'-M_2N_1',
M_1M_2'-M_2M_1'
+\beta(N_1N_2'-N_2N_1')
\right).
\]

Exact rational replay gives a sharper correction. With the inverse metric
frozen as a scalar, the Jacobi identity fails for \(\beta=-1\) and
\(\beta=+1\); only the degenerate contraction \(\beta=0\) closes. The genuine
hypersurface-deformation object is therefore a Lie algebroid, not this frozen
Lie algebra: its metric structure function belongs to the base and must
transform through the anchor. The metric action is part of coherence itself,
while its source-fixed sign and principal symbol remain necessary to recover
signature and a causal cone. A representation of the full algebroid on the
actual tower comparison carrier remains unconstructed.

The Jacobi defect also fixes the minimum base type. A nondegenerate candidate
must retain the spatial metric (q), its conjugate momentum or extrinsic
curvature (pi), and embedding/domain data. Tangential generators act by
spatial Lie derivative, while normal generators change (q) through the
constraint dynamics and therefore depend on (pi). The bracket must satisfy
both the Lie-algebroid Leibniz law

\[
[e_1,fe_2]=f[e_1,e_2]+\rho(e_1)(f)e_2
\]

and the anchor-morphism law

\[
\rho([e_1,e_2])=[\rho(e_1),\rho(e_2)]
\]

on an explicitly declared domain. Metric-only, frozen-metric,
anchor-mismatched, degenerate-metric, and post-hoc-signature fixtures are all
rejected separately. This is still a structural acceptance contract rather
than a constructed representation on the theta comparison carrier.

The compiler tests these as independent conjuncts. Objectwise typed maps can
have zero common kernel and still fail because a restriction square does not
commute. Conversely, every restriction square can commute while a nonzero
completion-only ghost lies in the kernel of every Hardy port. A third fixture
shows that naturality and separatedness still do not authorize replacement of
the pro-register by a scalar, and a fourth keeps source authority independent
of all algebraic gates.

Hence an admitted global incidence first requires the full-source
Poisson/Green constructor and then all of:

1. typed finite-cutoff components;
2. cutoff naturality;
3. zero completed common kernel;
4. retention of the pro-valued target;
5. source authority for the comparison.

The completion defect also has two different homological grades. Write
\(K_X=\ker I_X\). The inverse-limit sequence begins

\[
0\longrightarrow \varprojlim K_X
\longrightarrow \varprojlim S_X
\longrightarrow \varprojlim H_X
\longrightarrow \varprojlim{}^{1}K_X.
\]

The ordinary limit (arprojlim K_X) contributes genuine invisible source
states. Separately, the comparison

\[
\eta:\widehat S\longrightarrow\varprojlim S_X
\]

may itself have a kernel, producing a completion-descent ghost before the
Hardy map is applied. These two kernels govern faithfulness. By contrast,
(arprojlim{}^{1}K_X) measures failure to lift compatible target data; it is
an effectivity obstruction and need not create a readout kernel.

The checker includes a case with nonzero derived obstruction that remains
faithful but is not effective. It rejects contracts that call every completion
defect a derived kernel or identify a (arprojlim{}^{1}) class with an
invisible source state.

This yields a concrete sufficient closure theorem. Choose the source-authorized
cofinal chain (X_n) consisting of the first (n) primes. Then require:

1. the cutoff seminorms are cofinal in the source topology and Hausdorff, so
   (eta) is injective;
2. the compatible kernel tower has zero inverse limit;
3. the kernel tower satisfies the Mittag--Leffler condition, so its derived
   first limit vanishes.

Together these imply faithful and effective pro-incidence. The conditions are
independent. Mittag--Leffler does not imply separation; separation does not
imply Mittag--Leffler; and Hausdorffness for a noncofinal observer family does
not control completion descent. Surjectivity of the target restriction maps
also does not imply the Mittag--Leffler property for the kernel tower.

The live theta task is now reduced to proving these three properties for the
source-derived incidence, once its finite Hardy comparison components have
been constructed.

One of the three gates is already closed for the canonical constructor
completion. Every defining seminorm is indexed by a finite constructor word
and a finite observation packet. Such a word uses only finitely many
prime-specific generators, while the full compatible Mellin family is present
at every stage. The first-(n)-prime chain is therefore cofinal in the defining
seminorm family. Since valuation projectors separate finite packets, the
constructor topology is Hausdorff, and its canonical Hausdorff completion
embeds in the inverse limit of the cutoff completions. Thus \(\ker\eta=0\) for
this completion type.

The other two gates remain open. Finite-packet separation does not prove that
the completed compatible kernel tower has zero inverse limit, and
surjectivity of target restrictions does not establish Mittag--Leffler for
the kernels. The live audit is consequently one gate closed and two open—not
a blanket completion obstruction.

The Mittag--Leffler gate does close on every bounded valuation/Fock grade. At
fixed grade \(r\), the cutoff kernels are finite-dimensional, so the descending
images in any fixed stage stabilize. The full completion, however, is a
product over unbounded \(r\). Gradewise stabilization does not provide one
stabilization index uniform in \(r\).

The exact hostile tower uses

\[
\operatorname{im}_{m,r}
=
\begin{cases}
\mathbb F,&m<r,\\
0,&m\ge r.
\end{cases}
\]

Every fixed grade stabilizes, while the product image loses a new coordinate
at every stage and never stabilizes. Thus the remaining derived obstruction is
not generic finite-dimensional algebra; it is a uniformity problem across the
unbounded grade. Likewise, bounded-grade separation remains conditional on
constructing the finite Hardy components, and global separation additionally
requires product descent.

The product tower is not yet the canonical source assembly. All connected
Fock grades are strata of the single log-Euler measure

\[
\mu_{\log}
=
\sum_p\sum_{k\ge1}\frac1k p^{-k/2}\delta_{k\log p}.
\]

The primitive, square, and connected-tail grades must be split for typing and
then reassembled before completion. At finite cutoff the reassembly is an
explicit nonzero transition in a determinant line. Globally it must remain
determinant-line-valued; replacing it by \(\log\zeta\) or
\(\zeta'/\zeta\) imports the divisor being investigated and is circular.

This creates two possible proof charts. One may prove uniform Mittag--Leffler
directly in the product presentation, or construct the missing
archimedean/modular determinant-line correspondence and transport the kernel
problem through it. The drifting-grade counterexample remains a valid hostile
for the product chart, but it is not promoted to a source-invariant
obstruction. Finite determinant transitions alone do not supply the missing
global correspondence.

This completed-path frontier is distinct from the all-path coherence frontier.
Even after those two constructors exist, the incomparable pairs `S`--`C` and
`C`--`L` need their own complete-packet comparison cells before all legal
factorizations can be identified. The pair `S`--`L` is not a missing swap:
the source contract forces `S` before `L`, so exchanging them is ill-typed.

The four-way ablation proves minimality. Supplying neither constructor, only
the valuation extension, or only the Clark family leaves zero completed paths.
Supplying both admits exactly the three orders respecting `S` before `L`:

```text
C S L
S C L
S L C
```

They yield one typed endpoint in the bounded source fixture. This is evidence
for conjunctive sufficiency of the two-constructor frontier within the stated
finite contract; it does not supply either missing constructor in the live
theta source.

The three paths nevertheless remain three coherence components when no swap
cell is authorized. Their endpoint packets are equal, but endpoint equality
does not identify construction histories. Authorizing only `S`--`C` or only
`C`--`L` leaves two components; authorizing both yields one. Hence these two
comparison cells are jointly minimal for coherence of the legal path graph,
while an attempted `S`--`L` swap is rejected as a precedence violation.

The compiler emits the principal hostile witness directly:

```json
{
  "code": "distinction_erased_before_required_repair",
  "path": ["complete_tail_quotient", "retain_seam"],
  "lost_capability": "seam_translation_norm",
  "recovery_possible": false
}
```

The resulting precedence law is logical rather than chronological: completion
may precede a repair only when it preserves every distinction required by that
repair's source contract.

Supplying `F` would remove the Clark/completion obstruction but would not by
itself authorize the `S`--`C` swap. A source comparison cell for their complete
domain, graph norm, boundary packet, and residual capability would still be
required before the triangle could be called coherent.

## Process provenance and the typed history quotient

Endpoint separation does not determine which process produced an endpoint.
The exact hostile pair

\[
F_1=I,
\qquad
F_2=\operatorname{diag}(1,-1)
\]

agrees on the observed line but differs on the recovery direction. A recovery
probe restores process provenance, while inverse authority additionally needs
an independently supported inverse constructor.

Process provenance is not automatically preserved by composition. The two
stagewise distinguishable histories `II` and `ZZ` have the same composite when
\(Z^2=I\). The correct invariant is therefore neither endpoint bytes nor raw
factorization words. It is the history space modulo source-authorized process
equations. Such equations must form a two-sided congruence, and every partial
constructor domain must be saturated by the equivalence. Where both
representatives are defined, their outputs must remain equivalent.

A terminating, locally confluent rewrite presentation proves unique history
normal forms. This proves canonical-form existence but does not itself supply
an executable normalizer. Quotient existence, unique normal forms, and
normalizer authority remain separate compiler coordinates.

## Typed descent, anomalies, and gauge strictification

Equal process normal forms do not identify attached domains, residual
capabilities, support, or authority kinds. These form a typed fiber over the
process quotient. Fiber data descends only when it agrees strictly or when a
source-authorized coherence cell transports it.

Pairwise fiber transports can carry nontrivial triangle holonomy. Trivial
holonomy gives strict descent. Nontrivial holonomy is retained only as a typed
central anomaly with a separately authorized higher cell. Triangle anomalies
must then satisfy tetrahedral cocycle closure.

Closure does not imply removability. Over the finite hostile models, exact
\(GF(2)\) elimination tests

\[
\operatorname{rank}(B)
=
\operatorname{rank}[B\mid\alpha]
\]

to decide whether an anomaly \(\alpha\) is a coboundary. A nontrivial
cohomology class cannot be strictified. Coboundary status still does not grant
authority to execute a gauge change.

When strictifications exist, they form an affine torsor over \(\ker B\). A
positive-dimensional torsor requires a source selector, and that selector must
be equivariant under authorized presentation changes. Some torsors have no
fixed point, so no canonical gauge representative exists.

## Canonical groupoid without a canonical representative

Failure of a natural gauge point does not destroy the invariant object. The
compiler retains the complete gauge action groupoid: gauges as objects and
authorized presentation changes as morphisms. Orbit-set projection is not
faithful because it discards stabilizers.

A scalar readout descends only when constant on presentation orbits. Descent
and faithfulness across distinct orbits are independent. Even a complete
family of orbit-level scalar readouts cannot reconstruct isotropy. Typed
stabilizer ports must retain:

- a valid finite multiplication table, modulo group relabelling;
- the stabilizer representation on each capability fiber;
- the linkage between the group element and its fiber action;
- invertible inter-object intertwiners.

Cardinality alone fails: \(Z_4\) and \(Z_2\times Z_2\) both have order four but
are not isomorphic. Abstract group structure alone also fails: the same
\(Z_2\) can act trivially or by swapping two fiber coordinates.

Inter-object transports form a strict groupoid fiber functor only when

\[
P_{ac}=P_{bc}P_{ab}.
\]

A weak functor is admitted when a source-authorized invertible natural
compositor \(C\) instead satisfies

\[
P_{bc}P_{ab}=CP_{ac}.
\]

Those compositors must themselves obey pentagon coherence. Equal endpoint
matrices, pairwise intertwiners, locally valid triangle cells, or equal
pentagon products never manufacture the corresponding authority.

## Fibered comparison carrier

The finite (6N) comparison count is a fiber rank, not a global carrier.
Once the hypersurface-deformation bracket has metric-dependent structure
functions, the comparison object must vary over the phase-space-and-domain
base of ((q,\pi)) and embeddings.  The acting object is therefore a Lie
algebroid over that base, and its representation is an algebroid connection
on the comparison-torsor bundle.

The compiler admits the representation only when the connection obeys its
section Leibniz law and has zero curvature, or a separately source-typed
central anomaly.  Scalar readouts must be bundle maps preserving the base,
anchor, and declared domains.  Cutoff restriction must form a Cartesian
base-change square; fiberwise agreement alone is insufficient.  Signature is
locally fixed on each connected nondegenerate base stratum, so a signature
change must meet a degenerate locus. A fixed \(6N\times6N\) matrix therefore
cannot stand in for this structure.

This sharpens the four-tower picture.  The fourth tower is not an extra scalar
coordinate and not an externally ordered succession.  Its next rung is the
coherent variation of comparison fibers over admissible changes of the lower
three towers.  Curvature is the first obstruction to composing those local
comparisons into a global one.

There is then another rung. Facewise curvature fillings are 2-cells; their
compatibility on a tetrahedral overlap is a 3-cell. For an ordinary strict
connection the Bianchi identity supplies this compatibility structurally.
For weak, independently source-authorized comparison cells it must be checked
or supplied by a separately authorized higher cell. Pairwise coherent faces
can therefore bound a nonzero untyped tetrahedral residual.

Nor is existence of fillings the same as a constructive choice. When the
filling space is a nontrivial torsor over closed central 2-cells, an executable
presentation requires a source-authorized selector. Consequently the fourth
tower does not close merely because each of its visible faces closes. Its
fillings generate a next coherence layer, and larger-net behavior is governed
by that layer rather than by the endpoint data of the faces.

The resulting ladder is not automatically infinite. Its source-derived upper
bound is the dimension of the authorized dependency nerve: an (n)-dimensional
nerve demands typed comparison cells through degree (n), while the absence
of higher simplices removes higher comparison obligations. This bound cannot
be inferred from the largest rung number in any lower tower.

Two notions of stopping remain distinct. Invariant closure retains the full
groupoid of top-degree fillings once every required cell has been typed.
Executable closure additionally requires the top filling space to be
contractible or to carry a source-authorized selector. Thus a finite coherence
ladder can define a complete invariant object without defining a canonical
operation on one chosen representative.

## The closure-capability category

Let (K) be a finite source-authorized dependency nerve and let
(F:K^{op}\to\mathbf{Gpd}) assign the typed presentation groupoid at every
simplex. Define \(\mathbf{CapCl}_K\) to have such diagrams as objects and
domain-, support-, variance-, and authority-preserving pseudonatural
transformations as morphisms.

The invariant closure is \(\operatorname{holim}_K F\). The executable closure
is a pointed homotopy limit whose point is supplied by an authorized global
section of the selector fibration. There is a forgetful arrow from executable
to invariant closure. The reverse arrow exists only when that authorized
section exists. Observation is a separate natural port family (R:F\to O),
and execution is a further authority-preserving actuator lift of the selected
section.

This construction generates five independent obstruction coordinates:

1. descent: local data do not form an effective invariant closure;
2. higher coherence: typed lower faces have an unclosed higher residual;
3. selector: the invariant filling groupoid has no authorized point;
4. observation: the port family is not conservative on invariant objects;
5. execution: a selected capability has no authorized actuator lift.

The finite fixtures isolate each coordinate. Strominger's unresolved inverse
limit kernel lies in descent; the tetrahedral residual lies in higher
coherence; a noncontractible filling torsor lies in selector; Green or port
faithfulness lies in observation; and Kitaev's conditional physical lift lies
in execution. Grothendieck's live completion can occupy several coordinates
simultaneously. The classification is predictive because changing any one
gate produces a different lifting problem and the hostile models forbid
substitution between them.

## Consolidated compiler theorem

An authority-bearing partial repair system admits a presentation-independent
completed object only after the following layers close in order:

1. dynamically legal partial constructors and dependency paths;
2. source-authorized process equations forming a domain-saturated congruence;
3. terminating and confluent normalization when executable canonical forms are
   requested;
4. descent of domain, capability, support, and authority fibers;
5. coherent anomaly cocycles, with coboundary and nontrivial classes separated;
6. natural gauge selection when a fixed point exists, otherwise retention of
   the gauge action groupoid;
7. invariant readouts, stabilizer structure, stabilizer actions, and
   inter-object intertwiners;
8. strict transport composition or source-typed weak compositors satisfying
   pentagon coherence.

The machine result records SHA-256 digests of the contract, compiler, and
checker. The current deterministic replay passes all six base models and all
134 hostile mutations.
