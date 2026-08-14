# Nima Research Objective

This document fixes the current mathematical objective for the Nima branch.
It is a research target, not a statement of established fact. Scoped results
and corrections continue to live in `src/ledger`.

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

At the first nontrivial boundary, \(D=03\), entries 93--94 establish two
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

Its incidence branch gives the QTDS/contact sector, while its dual
augmentation gives the primitive boundary symbol. Their Smith index three is
intrinsic integral gluing; it is not a reason to introduce a rational
projector.

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

It must also recover entry 86's occurrence-resolved endpoint counit, realize
the relation generator \(\Delta\), and reproduce the four unit road
occurrences at the \(D=03\) physical cut.

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

1. **Local chain lift:** derive \(d_{\rm sp,sc}\) and prove the three displayed
   \(D=03\) chain and grade identities.
2. **Boundary naturality:** prove the physical-Cut square for one \(4+6\)
   channel, then obtain its orbit by \(D_8\)-equivariance.
3. **Intrinsic half-object:** assemble the local perfect complexes and
   noninvertible Gysin correspondences into a cdh-local, factorization-natural
   object \(\mathsf J^{\rm PC}\).
4. **CHY comparison:** construct a specialization-compatible comparison
   \(\Phi_{\rm CHY}(\mathsf J_n^{\rm PC})\simeq[({\rm Pf}'A_n)^2]\), rather than
   only matching paired amplitudes.
5. **Higher coherence:** evaluate the residual twisted top class on a quartic
   grammar and test whether it is exactly the universal Jordan defect

   \[
   Q_{Q_xy}-Q_xQ_yQ_x.
   \]

Only stages 1--2 are the immediate frontier. Later stages should not be used
to hide a failure of the local chain lift.

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

The three-tag triangle belongs to factorization-marked scalar geometry, not
to the bare one-parameter amplitude family. That enrichment is allowed, but
it must remain explicit.

## Bounded long-run objective

A long or overnight investigation should attempt exactly the first canonical
unproved arrow in the construction. Its useful terminal outcomes are either:

- one proved local chain identity, with a reproducible certificate; or
- one sharp falsifier identifying the first geometric map, filtration, or
  Beck--Chevalley identity that cannot exist.

Do not expand to a new multiplicity, a fourth primitive, or another sign
census while the \(D=03\) total-specialization lift remains untyped.
