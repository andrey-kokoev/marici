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

At the first nontrivial boundary, \(D=03\), entries 93--99 establish seven
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
local excess orientation and shift are canonical. It isolates the first
unproved arrow more sharply: an unlocalized, support-filtered augmented
dual-block/Cousin can--var kernel lifting either global carrier map.

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
The unresolved operation is the filtered lift of either global map. With

\[
I_+=(u_1,u_3,u_5),
\qquad
I_{03}=(u_0,u_3),
\]

the first local restriction of that lift must satisfy

\[
\boxed{
\rho_{03}A_+^{\rm Cous,PC}
=
\operatorname{Tr}_{03,\partial}^{\rm PC}\partial_{+,03}.
}
\]

The candidate shift and excess orientation have now been derived rather than
fitted: \(\eta=h_3^+-h_3^{03}\), and wedge by \(\eta\) is the canonical
integral top-\(\operatorname{Tor}_1\) inclusion. What remains is the actual
unlocalized can--var/Cousin kernel and all of its lower terms. It may not be
defined by the displayed identity. Every branch/pair intersection has
nonzero rank-one \(\operatorname{Tor}_1\), so treating the square as
transverse is false.

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
entry-98 target relation preserves all three rotated local identities, and
entry 99 supplies the two global carrier maps and the unique local excess
symbol. Realizing the relation generator \(\Delta\), its carrier source, and
the source/road associated-grade square is therefore established. The source
chain identity now depends on one global unlocalized augmented-dual-block
lift; its six local excess squares must follow by restriction rather than be
normalized independently.

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
4. **Unlocalized source lift -- immediate frontier:** construct one global
   augmented-dual-block/Cousin can--var kernel whose associated grade is
   \(A_+^{\rm car}\). Its three road restrictions must be the established
   excess symbols and entry-97 traces. Polarity then supplies the minus lift.
5. **Boundary naturality:** prove the physical-Cut square for one \(4+6\)
   channel, then obtain its orbit by \(D_8\)-equivariance.
6. **Intrinsic half-object:** assemble the local perfect complexes and
   noninvertible Gysin correspondences into a cdh-local, factorization-natural
   object \(\mathsf J^{\rm PC}\).
7. **CHY comparison:** construct a specialization-compatible comparison
   \(\Phi_{\rm CHY}(\mathsf J_n^{\rm PC})\simeq[({\rm Pf}'A_n)^2]\), rather than
   only matching paired amplitudes.
8. **Higher coherence:** evaluate the residual twisted top class on a quartic
   grammar and test whether it is exactly the universal Jordan defect

   \[
   Q_{Q_xy}-Q_xQ_yQ_x.
   \]

Stage 4 is the immediate frontier. Later stages should not be used to hide a
failure of the unlocalized source lift.

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

The three-tag triangle belongs to factorization-marked scalar geometry, not
to the bare one-parameter amplitude family. That enrichment is allowed, but
it must remain explicit.

## Bounded long-run objective

A long or overnight investigation should attempt exactly the first canonical
unproved arrow in the construction. The marked road spans, reciprocal-twist
bivariant traces, three-road target, two global carrier maps, and the local
top-\(\operatorname{Tor}_1\) symbols are now established. The current bounded
target is one global plus-sheet lift

\[
A_+^{\rm Cous,PC}:
\mathcal D_+^{\rm Cous,reg,\vee}
\longrightarrow
\mathbb D\operatorname{PC}(K_6,B_{\rm short})\otimes\chi_N
\]

over the unlocalized universal monodromy ring, satisfying

\[
\operatorname{gr}A_+^{\rm Cous,PC}=A_+^{\rm car}
\]

and, by restriction to all three roads,

\[
\rho_iA_+^{\rm Cous,PC}
\simeq
\operatorname{Tr}_{i,\partial}^{\rm PC}\partial_{+,i}^{\rm ex}.
\]

It must retain the rank-one excess orientations, occurrence pullbacks,
reciprocal/Borel--Moore support pairings, lower Cousin terms, physical normal
lines, and the integral dihedral action. In particular it must be constructed
before inverting the \(u_j\). The target identity

\[
d\mathcal K_{\rm rel}^{\rm PC}
=\mathcal T_0^{\rm PC}+\mathcal T_1^{\rm PC}+\mathcal T_2^{\rm PC},
\]

and its global carrier preimage are already proved. The remaining lift must
prove

\[
\operatorname{gr}A_+^{\rm Cous,PC}=A_+^{\rm car}.
\]

Its useful terminal outcomes are either:

- one proved local chain identity, with a reproducible certificate; or
- one sharp falsifier identifying the first geometric map, filtration, or
  Beck--Chevalley identity that cannot exist.

Do not recompute the target relation, construct the six road maps
independently, test \(\Delta\) on one pair alone, or expand to a new
multiplicity, a fourth primitive, or another sign census while the global
unlocalized source lift remains untyped.
