# Nima Research Objective

This document fixes the current mathematical objective for the Nima branch.
It is a research target, not a statement of established fact. Scoped results
and corrections continue to live in `src/ledger`. Research execution and
admission follow `docs/research-lifecycle.md`; in particular, a proved local
theorem must be recorded separately from any still-open global lift.

## Current position

At generic, nonresonant tree kinematics, scalar index raising already
identifies the NLSM half-class

\[
\mathsf J_n=(I_n^\flat)^{-1}a_n
\simeq [({\rm Pf}'A_n)^2].
\]

The unresolved problem is not generic amplitude reconstruction. It is to make
this class intrinsic on scalar boundary geometry and natural under physical
factorization.

At the first nontrivial boundary, \(D=03\), entries 93--102 establish ten
pieces of that construction:

1. a normalization--conductor cdh square whose first polarity-odd normal
   symbol is \(K_{\rm alt}\otimes L_{\rm pol}\);
2. the integral, Verdier-self-dual augmented triangle resolution

   \[
   0\longrightarrow\mathbf 1_{\rm or}
   \xrightarrow{\Delta}P_{\rm tag}
   \xrightarrow{\partial_\triangle}P_{\rm road}
   \xrightarrow{\epsilon}\mathbf 1
   \longrightarrow0.
   \]
3. the canonical first conductor normal-link carrier differential and its
   exact integral fold onto that augmented triangle.
4. the actual factorization-marked transverse span

   \[
   Z_0\longleftarrow W_{03}\longrightarrow Z_3
   \]

   with minimal coefficient \(K(u_0,u_3)\), unique marked lower-Cousin
   primitive, and its road-costalk PC realization.
5. the endpoint-normalized reciprocal-twist bivariant trace on the exact
   road-face costalk,

   \[
   \Theta_{1,\partial}^{\rm PC}:
   \mathcal S_{1,\rm reg}^{\rm mark,\vee}
   \boxtimes
   \mathcal Q_{03,\partial,\rm lf}^{\rm PC}
   \longrightarrow\mathbf1_{\chi_N}.
   \]
6. the geometric three-road relation target in the weighted hexagon
   associahedron,

   \[
   d\mathcal K_{\rm rel}^{\rm PC}
   =\mathcal T_0^{\rm PC}
   +\mathcal T_1^{\rm PC}
   +\mathcal T_2^{\rm PC},
   \]

   obtained relative to the six short-diagonal pentagonal facets rather than
   by adjoining a formal cone.
7. two polarity-related integral global carrier maps from the suspended
   central vertex figures to that relative target, together with the
   canonical plus/\(D03\) excess sequence

   \[
   0\longrightarrow K(Q)[1]
   \xrightarrow{(h_3^+-h_3^{03})\wedge-}
   K(I_+)\otimes K(I_{03})
   \longrightarrow K(Q)\longrightarrow0.
   \]
8. the support-directed one-normal can--var packet, its Koszul--Cech
   realization, and the three labelled local excess traces. A strict
   finite-free stalk map is now ruled out.
9. the exact weighted three-road star at coefficient level, together with
   the falsification of a pairwise \(q_2\) road transition as the next
   intrinsic objective. The remaining datum is one filtered
   conductor-to-dual-block comparison.
10. the identification of the augmented triangle as the
    orientation-twisted integral \(C_3\)-Tate periodicity window representing
    the generator of
    \(\operatorname{Ext}^2_{\mathbb Z[D_3]}(\mathbb Z,\mathbb Z_{\rm or})
    \cong\mathbb Z/3\), together with the proof that the weighted normal
    packet is not this window over the unlocalized base.

Its incidence branch gives the QTDS/contact sector, while its dual
augmentation gives the primitive boundary symbol. Their Smith index three is
intrinsic integral gluing; it is not a reason to introduce a rational
projector.

The source carrier differential, its two global carrier maps, the first
marked coefficient span, and its local trace are therefore no longer missing.
Entry 95 rules out replacing the span
by a strict fold of two independent normal characters into one supported
rank-one target. Entry 96 shows that the span first produces the road-costalk
class \(d_1^\vee\otimes\chi_N\); entry 97 constructs the arrow to its Verdier
dual without identifying \(d_1\) with \(d_1^\vee\). Entry 98 rotates this
trace and constructs the target relation geometrically. Entry 99 proves that
the six carrier attachments are restrictions of two global maps and that the
local excess orientation and shift are canonical. Entry 100 constructs the
paired can--var/Koszul--Cech coefficient packet and all three labelled local
derived traces. It also proves that no strict finite-free map of branch and
road stalks can carry the unit coefficient. Entry 101 proves that the
pairwise lower-vertex comparison proposed there was not canonically typed:
the roads are disjoint correspondence targets, not overlapping charts. It
replaces that objective by a single weighted star and isolates one filtered
comparison \(\alpha_+\) as the first unproved arrow.

Entry 102 explains the index-three gluing without adding a new geometric
map: the augmented triangle is the norm/\((1-r)\)/augmentation window of the
\(C_3\)-Tate resolution, with the reflection orientation twist making its
order-three class \(D_3\)-invariant. This is the integral carrier shadow of
the construction. It is not a replacement for the weighted normal/Rees
packet: the latter has supported homology and cannot be identified with the
exact Tate window without globally inverting the very normals whose support
must be retained.

Entry 96 also corrects the order of the relation test. A single pair has image
in \(\mathbb Z d_1\) and therefore cannot realize
\(\Delta=d_0+d_1+d_2\). The \(\Delta\) coherence belongs only after all three
marked pairs have been assembled.

## North-star construction

Construct the scalar total-specialization complex associated to the conductor
square

\[
\begin{matrix}
\widetilde Z&\longrightarrow&\widetilde F\\
\downarrow&&\downarrow\\
Z&\longrightarrow&F,
\end{matrix}
\]

starting from the actual scalar normalization--Cech, normal/Rees, and
Pochhammer--Cousin maps. A schematic target is

\[
\boxed{
\mathcal S_F^{\rm sp}
:=
\operatorname{Tot}\!\left[
\operatorname{Sp}^{\rm fact}(F)
\longrightarrow
\operatorname{Sp}^{\rm fact}(\widetilde F)
\oplus\operatorname{Sp}^{\rm fact}(Z)
\longrightarrow
\operatorname{Sp}^{\rm fact}(\widetilde Z)
\right].
}
\]

The arrows, cohomological shifts, twists, and totalization signs must be
derived from those geometric operations. They may not be fitted to the known
matrix \(K_{\rm alt}\).

The immediate formula objective is a filtered chain map

\[
\boxed{
G_{03}^{\rm Cousin}:
(\mathcal S_F^{\rm sp},d_{\rm sp,sc})
\longrightarrow
(\mathcal R_{03}^{\rm circ,PC},d_{\rm circ}^{\rm PC})
}
\]

and its primitive composite

\[
\boxed{
\pi_{03}^{\rm PC}
=
\mathbb D(\Delta_{03}^{\rm circ})
\circ G_{03}^{\rm Cousin}.
}
\]

Its first local component is now established after making support and twist
directions explicit. Let \(\mathcal S_{1,\rm reg}^{\rm mark,\vee}\) denote
the reciprocal-twist regularized image of the entry-96 supported diagram on
\(Z_0\leftarrow W_{03}\to Z_3\), and let
\(\mathcal Q_{03,\partial,\rm lf}^{\rm PC}\) denote exactly the
locally-finite/Borel--Moore road-face costalk of entry 38. Entry 97 proves

\[
\boxed{
\Theta_{1,\partial}^{\rm PC}:
\mathcal S_{1,\rm reg}^{\rm mark,\vee}
\boxtimes\mathcal Q_{03,\partial,\rm lf}^{\rm PC}
\longrightarrow\mathbf1_{\chi_N}.
}
\]

Its currying gives

\[
\boxed{
\operatorname{Tr}_{1,\partial}^{\rm PC}:
\mathcal S_{1,\rm reg}^{\rm mark,\vee}
\longrightarrow
\mathbb D(\mathcal Q_{03,\partial,\rm lf}^{\rm PC})\otimes\chi_N
=:\mathcal T_1^{\rm PC}.
}
\]

The target is typed by Verdier duality from the established road costalk; it
is not a newly postulated common local system. Its associated grade is entry
89's unit Laurent pairing and its endpoint is entry 86's occurrence counit.
The same notation must not be extended silently to the full
\(\operatorname{PC}(\mathsf J_4\boxtimes\mathsf J_6)\), which retains a
contact kernel.

Entry 98 proves that rotating this construction to the two other existing
pairs produces the boundary of an actual relative scalar face-tube object:

\[
\boxed{
d\mathcal K_{\rm rel}^{\rm PC}
=\mathcal T_0^{\rm PC}+\mathcal T_1^{\rm PC}+\mathcal T_2^{\rm PC}.
}
\]

Entry 99 then proves the global source carrier maps

\[
A_\pm^{\rm car}:D_\pm^{\rm car}
\longrightarrow C_*(K_6,B_{\rm short}),
\]

with \(f_+\mapsto K_{\rm rel}\), \(f_-\mapsto-K_{\rm rel}\), and the six
link edges mapped with unit coefficients to their three matched road facets.
Entry 100 identifies the local coefficient object required to lift those
maps. For one normal it is the packet

\[
K_1(u)=[R\xrightarrow{u}R]
\xrightarrow{(1,u^{-1})}
C_u=[R\longrightarrow R[u^{-1}]],
\]

with paired support conventions

\[
Rj_*:\ (\operatorname{can},\operatorname{var})=(u,1),
\qquad
j_!\mathbb D:\ (\operatorname{can},\operatorname{var})=(1,u^\vee).
\]

The finite Koszul stage carries the perfect Verdier pairing; the Cech stage
realizes the supported simple pole without globally inverting \(u\). For

\[
I_+^\vee=(u_1^\vee,u_3^\vee,u_5^\vee),
\qquad
I_{03}=(u_0,u_3),
\]

the labelled \(D03\) correspondence, after the forced Laurent-unit twist
normalization, now satisfies

\[
\boxed{
\eta_{03,\rm mix}
\longmapsto
\left[\frac{1}{u_0u_1u_3u_5}\right]
\in H^4_{(u_0,u_1,u_3,u_5)}(R_0)
}
\]

and the two rotated roads satisfy the analogous identities. A strict
finite-free map \(K(I_+^\vee)\to K(I_i)\) with unit carrier coefficient is now
falsified.

Entry 101 corrects the next operation. The long-road facets are disjoint, so
there is no intrinsic pairwise transition at their shared dual-link label
\(q_2\). The unlocalized residual normal packet is instead

\[
K_E=K(u_4,u_0,u_2),
\]

and its exact formal star is

\[
\boxed{
f\mapsto\tau_AK_{\rm rel},\quad
e_1\mapsto\frac{\tau_A}{u_4}T_2,\quad
e_3\mapsto\frac{\tau_A}{u_0}T_1,\quad
e_5\mapsto\frac{\tau_A}{u_2}T_0,\quad
q_i,a\mapsto0,
}
\]

where \(\tau_A=[1/(u_1u_3u_5)]\). This is a proved coefficient identity but
not yet an intrinsic PC morphism. The canonical formulation starts with the
absolute loaded associahedron, applies the filtered central dual-block
counit, and only then passes to the relative object:

\[
\boxed{
A_+^{\rm Cous,PC}
=q_{\rm cell}\epsilon_{\rm cell}\alpha_+,
\qquad
\alpha_+:
\mathcal S_+^{\rm cond}
\xrightarrow{\sim}C_{\rm abs}^{v_+}.
}
\]

The counit and cellular relative map are canonical. The comparison
\(\alpha_+\), in an integral \(D_3\)-equivariant filtered/Rees category, is
the single missing construction. Its associated grade must be the displayed
weighted star and its three Cousin edge terms must be the established local
traces. Every branch/pair intersection still has nonzero rank-one
\(\operatorname{Tor}_1\), so treating an edge attachment as transverse
remains false.

Its carrier-forgetting shadow must also reproduce the exact two-extension

\[
\beta_\triangle=
\left[
0\to\mathbb Z_{\rm or}\xrightarrow{N}P_{\rm tag}
\xrightarrow{1-r}P_{\rm road}\xrightarrow{\epsilon}\mathbb Z\to0
\right]
\in\operatorname{Ext}^2_{\mathbb Z[D_3]}
(\mathbb Z,\mathbb Z_{\rm or})\cong\mathbb Z/3.
\]

This is a compatibility test, not an instruction to construct \(\alpha_+\)
in a Tate-localized category. The weighted and Tate shadows are deliberately
not identified over the unlocalized coefficient ring.

Here \(d_{\rm sp,sc}\) denotes the canonical total scalar specialization
differential to be constructed. It is **not** a scalar BRST differential.
Gauge BRST belongs downstream in Yang--Mills descent.

## Decisive identities

The construction must satisfy, without inserting the desired answer into its
definition,

\[
d_{\rm sp,sc}^2=0,
\qquad
d_{\rm circ}^{\rm PC}G_{03}^{\rm Cousin}
=G_{03}^{\rm Cousin}d_{\rm sp,sc},
\]

and

\[
\operatorname{gr}_{\mathfrak c}^{1}
(G_{03}^{\rm Cousin})
=K_{\rm alt}\otimes L_{\rm pol}.
\]

Entry 97 recovers entry 86's occurrence-resolved endpoint counit and
entry 89's four unit road occurrences at the \(D=03\) physical cut. The
entry-98 target relation preserves all three rotated local identities, entry
99 supplies the two global carrier maps and the unique local excess symbol,
and entry 100 supplies the paired one-normal packet and all three local Cech
residues. Realizing the relation generator \(\Delta\), its carrier source,
and the three local source/road derived correspondences is therefore
established. Entry 101 shows that no lower-vertex transition should be added.
The source chain identity now depends on the single filtered comparison
\(\alpha_+\); its associated grade is already forced by the weighted star.

The first global test is Beck--Chevalley/factorization naturality:

\[
\operatorname{Cut}_E\,\pi_D^{\rm PC}
\simeq
(\pi_{D_L}^{\rm PC}\boxtimes\pi_{D_R}^{\rm PC})
\operatorname{Cut}_E,
\]

with occurrence coefficients, twist reversal, ordered normal lines, and
internal-state coevaluation retained.

## Success ladder

1. **Local bivariant trace -- established in entry 97:**
   \(\Theta_{1,\partial}^{\rm PC}\) and
   \(\operatorname{Tr}_{1,\partial}^{\rm PC}\) obey the endpoint,
   associated-grade, support, twist, and independent-character identities.
2. **Three-road target relation -- established in entry 98:** the weighted
   relative hexagon supplies \(\mathcal K_{\rm rel}^{\rm PC}\), its unique
   normalized reciprocal cocycle, and the three rotated boundary traces.
3. **Global source carrier -- established in entry 99:** the two central
   vertex figures map integrally and equivariantly to the relative target;
   the six carrier attachments are their road restrictions. The plus/\(D03\)
   excess symbol and every already-typed boundary invariant are fixed.
4. **Local unlocalized packet -- established in entry 100:** the paired
   support-directed can--var objects, Koszul--Cech comparison, mixed excess
   line, and three labelled road residues are explicit. A strict finite-free
   stalk map is falsified.
5. **Filtered global assembly -- immediate frontier:** construct the
   normalization--conductor comparison
   \(\alpha_+:\mathcal S_+^{\rm cond}\simeq C_{\rm abs}^{v_+}\) in the
   integral \(D_3\)-equivariant Rees category. Its associated grade must be
   entry 101's weighted star and its three Cousin residues must be the local
   traces of entry 100. Its carrier shadow must be entry 102's integral Tate
   two-extension, without replacing the weighted complex by that exact
   window. Polarity then supplies the minus lift.
6. **Boundary naturality:** prove the physical-Cut square for one \(4+6\)
   channel, then obtain its orbit by \(D_8\)-equivariance.
7. **Intrinsic half-object:** assemble the local perfect complexes and
   noninvertible Gysin correspondences into a cdh-local, factorization-natural
   object \(\mathsf J^{\rm PC}\).
8. **CHY comparison:** construct a specialization-compatible comparison
   \(\Phi_{\rm CHY}(\mathsf J_n^{\rm PC})\simeq[({\rm Pf}'A_n)^2]\), rather than
   only matching paired amplitudes.
9. **Higher coherence:** evaluate the residual twisted top class on a quartic
   grammar and test whether it is exactly the universal Jordan defect

   \[
   Q_{Q_xy}-Q_xQ_yQ_x.
   \]

Stage 5 is the immediate frontier. Later stages should not be used to hide a
failure of the filtered absolute-to-relative assembly.

## Prohibited shortcuts

The objective is not met by:

- declaring an arbitrary square-zero source differential;
- calling the missing source structure “scalar BRST”;
- splitting the three-road resolution with \(1/3\);
- replacing Gysin correspondences by invertible chart transitions;
- treating physical Cuts alone as a conservative descent topology;
- forgetting occurrence labels, polarity, normal orientations, or contact
  terms;
- proving only equality after pairing or only at generic cohomology;
- adding generators solely to force a desired commutative square.
- folding two independent universal monodromy characters strictly into one
  supported rank-one target over the identity base.
- requiring one tag pair to realize the three-tag relation \(\Delta\).
- treating a branch/pair intersection as transverse despite its nonzero
  excess \(\operatorname{Tor}_1\) line.
- defining a source top map by the target relation it is meant to prove.
- replacing a derived branch/road correspondence by a strict finite-free
  stalk map; entry 100 proves that such a unit lift cannot exist.
- calling \(R\to R[u^{-1}]\) itself a two-way can--var quiver, or globally
  inverting \(u\) and thereby erasing its supported class.
- comparing disjoint road facets through an invented common \(q\)-vertex
  transition; entry 101 shows that the canonical union target gives a
  nonzero difference while the deeper conductor requires the missing Gysin
  map by definition.
- taking the ordinary costalk directly in the relative object. The central
  vertex is removed there and the desired morphism is ordinary-null; its
  information survives only in the filtered absolute-to-relative composite.
- replacing the supported weighted/Rees packet by the exact constant Tate
  window, or globally inverting \(u_4,u_0,u_2\) to make their incidence
  matrices conjugate. Entry 102 proves that their unlocalized homology
  differs.
- treating the order-three Tate class as the missing \(\alpha_+\). It
  explains the carrier's integral nonsplitting but supplies none of the
  geometric support, occurrence, excess, or Cousin data.

The three-tag triangle belongs to factorization-marked scalar geometry, not
to the bare one-parameter amplitude family. That enrichment is allowed, but
it must remain explicit.

## Bounded long-run objective

A long or overnight investigation should attempt exactly the first canonical
unproved comparison in the construction. The marked road spans,
reciprocal-twist bivariant traces, three-road target, two global carrier maps,
local top-\(\operatorname{Tor}_1\) symbols, paired one-normal can--var packet,
all three labelled Cech residues, and the exact weighted star are now
established. The current bounded target is

\[
\boxed{
A_+^{\rm Cous,PC}
=q_{\rm cell}\epsilon_{\rm cell}\alpha_+,
\qquad
\alpha_+:
\mathcal S_+^{\rm cond}
\xrightarrow{\sim}C_{\rm abs}^{v_+}
}
\]

in a bounded, exhaustive, separated, integral, \(D_3\)-stable filtered/Rees
category. Construct \(\alpha_+\) from the actual normalization--conductor and
absolute loaded dual-block geometry, not from the target equation. The Rees
parameter \(t\), the normal variables \(u_j\), and \(3\) must remain
uninverted. Occurrence pullbacks, reciprocal/Borel--Moore support directions,
all localization summands, repeated-normal excess lines, lower-Cousin maps,
physical normal lines, and \(\chi_N\) must remain visible.

The decisive specialization tests are

\[
\operatorname{Rees}(A_+)/(t-1)\simeq0
\]

in the ordinary relative derived object, and

\[
\operatorname{Rees}(A_+)/(t)
=\operatorname{gr}(A_+)
=A_+^{\rm car}
\]

with the entry-101 weighted coefficients. Its three edge residues must be
exactly \(\Theta_{14}^{\rm loc},\Theta_{03}^{\rm loc},\Theta_{25}^{\rm loc}\),
while their total road restriction contracts because the source is supported
at the removed central vertex.

After forgetting supported coefficients, the same filtered construction must
recover entry 102's class \(\beta_\triangle\). This is a second acceptance
test on one \(\alpha_+\), not a proposed chain isomorphism between the
weighted packet and the Tate window.

Its useful terminal outcomes are either:

- one proved filtered comparison and absolute-to-relative chain identity,
  with a reproducible certificate; or
- one sharp falsifier showing that the normalization--conductor source cannot
  be the filtered central dual-block costalk, or that one established local
  trace is incompatible with its Cousin boundary.

Do not recompute the target relation, construct the six road maps
independently, resurrect a pairwise \(q\)-vertex transition, test \(\Delta\)
on one pair alone, or expand to a new multiplicity, a fourth primitive, or
another sign census while \(\alpha_+\) remains unconstructed.
