# Finite-Alpha-Prime Normal-Torus Lift and Nearby-Cycle Unit Theorem

## Record

Date: 2026-08-13

Status: corrected in part by entries 70--72. The undecorated associahedral
face map and the all-arity **transverse** cellular coaction of entry 37 have a
canonical realization in the facewise generalized-Pochhammer/Cousin complex
at finite, nonresonant \(\alpha'\). The claim below that the
occurrence-decorated comparison is already a chain map on the complete scalar
envelope was too strong: eight-point dependent pentagons require a
scalar-facet coefficient specialization which has not yet been constructed.

The construction is canonical in the normal-cone/Cousin model and canonical up to filtered chain
homotopy after choosing actual tubular currents. It does not select a privileged smooth twisted
form. This is the correct strength: the earlier collar/Thom ambiguity disappears in the derived
facewise target, but not in a point-set de Rham representative.

The physical Pochhammer factor differs from \(1/X_e\) by an analytic unit. Consequently the
finite-\(\alpha'\) comparison has the exact scalar coaction as its \(V_e\)-associated grade. This
proves compatibility with physical specialization on the induced nearby-cycle channel sector,
without attempting to invert the resonant global pairing.

## The order of operations

The scalar extraction must precede the worldsheet regulator:

\[
\boxed{
\operatorname{Poch}_{\alpha'}\circ\operatorname{gr}_{R}
}
\]

is defined, while the opposite order is not a Laurent/Rees construction.

Indeed, the scalar normal family has

\[
\widetilde X_D(t)=X_D+\frac{\sigma_D}{t}.
\]

If it is exponentiated into Koba--Nielsen monodromy first, then

\[
\exp(2\pi i\alpha'\widetilde X_D(t))
=
\exp(2\pi i\alpha'X_D)
\exp\!\left(\frac{2\pi i\alpha'\sigma_D}{t}\right),
\]

which has an essential singularity at \(t=0\). There is no finite \(t\)-associated grade.

Therefore finite \(\alpha'\) is a regulator of the already extracted scalar cellular symbol. It
is not being asserted to be a string completion of the shifted scalar family.

This is another concrete noncommutation relation in the master operation algebra:

\[
\boxed{
\operatorname{Poch}_{\alpha'}\circ\operatorname{gr}_{R}
\neq
\operatorname{gr}_{R}\circ\operatorname{Poch}_{\alpha'}.
}
\]

## Worldsheet normal-crossing data

Let

\[
M_n=\mathcal M_{0,n},
\qquad
\overline M_n=\overline{\mathcal M}_{0,n},
\qquad
D=\overline M_n\setminus M_n.
\]

The Deligne--Mumford--Knudsen boundary is a simple normal-crossing divisor. Fix a cyclic ordering
\(\alpha\). The closure of its real chamber is the associahedron

\[
K_\alpha\subset\overline M_n(\mathbb R),
\]

whose faces are labelled by noncrossing polygon dissections. Thus every scalar presentation cell
in the marked associahedral envelope is already a face of the same worldsheet chamber.

Let

\[
\mathscr L_{\alpha'}
\]

be the rank-one Koba--Nielsen local system with monodromy

\[
q_E
=
\exp(2\pi i\alpha'X_E)
\]

around the boundary divisor \(D_E\). Work over the coefficient ring

\[
\mathbf k_{\rm nr}
=
\mathbf k
\bigl[(q_E-1)^{-1}:D_E\cap K_\alpha\neq\varnothing\bigr]
\]

and impose the finite nonresonance condition

\[
\boxed{
q_E\neq1
\quad
\text{for every boundary component meeting the chamber.}
}
\]

Equivalently, \(\alpha'X_E\notin\mathbb Z\) for every stable planar channel \(E\).

## The local normal Koszul complex

Near a codimension-\(r\) face

\[
F=D_{E_1}\cap\cdots\cap D_{E_r}\cap K_\alpha,
\]

choose positive oriented normal circles \(\ell_{E_i}\). The loading of one normal circle obeys

\[
\partial_{\mathscr L}\ell_E
=
(q_E-1)p_E,
\]

where \(p_E\) is the loaded radial basepoint, with the sign fixed by the normal orientation line.
Hence at nonresonance

\[
h_E
=
\frac{\ell_E}{q_E-1}
\]

is the canonical normal contraction.

For a nested face the normal model is the tensor product

\[
\mathsf K_F
=
\bigotimes_{i=1}^{r}
\left[
\mathbf k_{\rm nr}
\xrightarrow{\,q_{E_i}-1\,}
\mathbf k_{\rm nr}
\right].
\]

The factors commute as monodromy operators and carry the ordinary Koszul orientation signs.
Their contracting homotopy is the ordered product of the \(h_{E_i}\). Changing the order changes
only the orientation sign already recorded in

\[
\operatorname{or}(N_F)
=
\bigwedge_{i=1}^{r}\operatorname{or}(N_{E_i}).
\]

This local complex is the algebraic content of the higher-dimensional Pochhammer contour.

## The facewise Pochhammer/Cousin complex

Define

\[
\operatorname{PC}_{\alpha'}(K_\alpha)
\]

to be the total complex whose face-\(F\) summand consists of:

1. Borel--Moore chains on \(F^\circ\);
2. the induced loading of \(\mathscr L_{\alpha'}\);
3. the normal orientation line \(\operatorname{or}(N_F)\);
4. the localized normal Koszul factor \(\mathsf K_F\).

Its differential is

\[
d_{\rm PC}
=
d_{\rm tangential}
+
d_{\rm Cousin}
+
d_{\rm normal},
\]

where the Cousin term is the signed sum over codimension-one face inclusions. In a normal product
chart this is exactly the tensor-product differential of the one-dimensional Pochhammer
regularization.

For an oriented associahedral face \(F\), let

\[
\mathbb P_{\alpha'}(F)
\]

be its regularized face-tube symbol. Locally it is the product of \(F^\circ\) with the required
normal contractions \(h_E\), together with the lower-face terms forced by the total differential.
The one-dimensional identity above gives

\[
\boxed{
d_{\rm PC}\mathbb P_{\alpha'}(F)
=
\mathbb P_{\alpha'}(\partial_{\rm cell}F).
}
\]

Thus

\[
\mathbb P_{\alpha'}:
C_*^{\rm cell}(K_\alpha)
\longrightarrow
\operatorname{PC}_{\alpha'}(K_\alpha)
\]

is a chain map.

This statement is intrinsic in the normal-cone/Cousin complex. Realizing it by literal tubular
currents requires radii and collars, but any two choices are isotopic and give filtered
chain-homotopic maps. No such choice is needed for the derived class or its face residues.

## Monoidality

A physical boundary divisor has the canonical product form

\[
D_e
\cong
\overline M_L\times\overline M_R.
\]

On the real chamber,

\[
K_\alpha\cap D_e
\cong
K_{\alpha_L}\times K_{\alpha_R}.
\]

Both the Cousin differential and the normal Koszul complex tensor under this identification.
Therefore the facewise Pochhammer map is strongly monoidal:

\[
\boxed{
\operatorname{Res}^{\rm PC}_e
\mathbb P_{\alpha'}(F)
=
\mathbb P_{\alpha'}(F_L)
\boxtimes
\mathbb P_{\alpha'}(F_R)
}
\]

after retaining the oriented normal factor belonging to \(e\).

This is the chain-level form of the standard statement that associahedral facets and generalized
Pochhammer contours factor into lower-point products.

## The scalar-derived comparison

Let

\[
C^{\rm sc}_{n,\alpha}
=
C_*^{\rm cell}
\bigl(\operatorname{AssEnv}_\alpha;\mathcal L_J\bigr)
\]

be the occurrence-decorated scalar complex after taking the distinguished scalar associated
grade. A generator is written

\[
[F;\mu],
\]

where \(F\) is an actual associahedral face and \(\mu\) records the component marks and their
scalar Laurent weight.

Define

\[
\boxed{
\chi_{\alpha'}[F;\mu]
=
\mu\otimes\mathbb P_{\alpha'}(F).
}
\]

Entry 37 proves that the coefficient system is a chain cosheaf on every transverse mixed product
cell. The Pochhammer face map is a chain map on every associahedral factor. Consequently

\[
\boxed{
d_{\rm PC}\chi_{\alpha'}
=
\chi_{\alpha'}d_{\rm sc}
}
\]

on the transverse occurrence-decorated subcomplex and on every physical face
restriction for which the cellular coaction is defined. The undecorated
Pochhammer map remains a chain map on nontransverse cells, but tensoring it by
scalar occurrence weights requires an additional coefficient specialization.

Entries 70--71 exhibit the first missing case. On each of eight route
pentagons, the initial scalar edge exchanges one independent Laurent label;
after passage to the common full-core fiber, both
\(+\operatorname{Id}\) and \(-\operatorname{Id}\) satisfy every previously
established fixed-core, physical, orientation, and deck constraint. Thus the
statement that the Cousin differential handles nontransverse incidence is the
correct target, but was not proved here for the decorated scalar complex.

Entry 72 supplies the missing occurrence-level shape without yet loading it:
the scalar facet is a rank-four incidence span, and two saturated Čech
sequences glue its polarity images and companion-square image to the complete
rank-eight full-core fiber. A corrected complete comparison must tensor that
constructible diagram with the face-tube complex; it must not choose an
edgewise transport.

Entry 73 constructs the resulting formal cellular/coefficient totalization
and proves its differential squares to zero.  It also shows why this does not
yet extend the physical theorem: the four support charts are a cubical belt,
and support admits forty pentagon-to-square cellular lifts.  The physical
finite-alpha-prime Gysin natural transformation has not selected one of them.

Entry 74 sharpens the remaining statement.  The forty strict lifts give only
two maps in relative/Borel--Moore chains, distinguished by orientation; the
ordered normal line selects the positive class.  Thus the physical invariant
to construct is a derived bivariant kernel, not a preferred point-set map.
It also replaces entry 73's overlarge constant-coefficient cube by the tensor
of three weighted interval complexes and derives the unique localized
rank-one Cousin counit.  What remains open here is its assembly into a global
occurrence-decorated natural transformation.  Collar independence of the
underlying undecorated Pochhammer/Cousin class is already established above.

This is the filtered scalar-to-Pochhammer/Cousin comparison on the transverse
domain. Its extension across dependent associahedral faces is the remaining
coefficient-lift problem.

## Finite-\(\alpha'\) physical coaction

The normal Pochhammer propagator associated with \(e\) is

\[
\kappa_e(\alpha')
=
\frac{2\pi i\alpha'}{q_e-1}
=
\frac{2\pi i\alpha'}
{\exp(2\pi i\alpha'X_e)-1}.
\]

For a supported directed cut with common source slots \(d_e^0,d_e^1\), define

\[
\boxed{
G^{\alpha'}_e(h)
=
-
\kappa_e(\alpha')
\left(
X_{d_e^0}\,
\mathbb P_{\alpha'}(h_e^0)
+
X_{d_e^1}\,
\mathbb P_{\alpha'}(h_e^1)
\right).
}
\]

Equivalently, the factor \(\kappa_e\) is the normalized loaded normal circle and the two
\(X_d\)'s are the scalar-grade contact marks. They are not replaced by guessed stringy
numerators.

The rooted-spine theorem supplies the same two upper faces and slots at both endpoints. The
normal factor depends only on \(e\). Therefore

\[
\boxed{
d_{\rm PC}G_e^{\alpha'}(h)
=
G_e^{\alpha'}(\partial h).
}
\]

For several cuts, the normal Koszul factors tensor and the occurrence coactions commute. Hence
the finite-\(\alpha'\) lift is compatible with arbitrary nested transverse cuts, including all
product-associahedral propagations of the universal mixed prism.

## Nearby-cycle unit theorem

Put

\[
u_e(\alpha',X_e)
=
\frac{\exp(2\pi i\alpha'X_e)-1}
{2\pi i\alpha'X_e}.
\]

This is analytic at \(X_e=0\) and

\[
u_e(\alpha',0)=1.
\]

Therefore

\[
\boxed{
\kappa_e(\alpha')
=
\frac{1}{X_e}\,
u_e(\alpha',X_e)^{-1}.
}
\]

The finite-\(\alpha'\) Pochhammer pole and the field-theory propagator differ only by a unit in
the \(V_e\)-filtered local ring. It follows immediately that

\[
\boxed{
\operatorname{gr}_{V_e}^{-1}G_e^{\alpha'}
=
G_e
=
-\frac{X_{d_e^0}}{X_e}h_e^0
-\frac{X_{d_e^1}}{X_e}h_e^1.
}
\]

For a nested cut set \(E\),

\[
\prod_{e\in E}\kappa_e(\alpha')
=
\frac{1}{\prod_{e\in E}X_e}
\prod_{e\in E}u_e^{-1},
\]

and the product of units has constant term one. Thus the statement is simultaneously true on
every normal-crossing channel stratum and independent of cut order.

This proves the correctly typed specialization law:

\[
\boxed{
\operatorname{gr}_{V_E}
\operatorname{Res}^{\rm PC}_E
\chi_{\alpha'}
=
\left(
\boxtimes_{R\in\mathcal R(E)}
\chi_{\alpha',R}
\right)
G_E.
}
\]

It does not identify ordinary and compactly supported twisted homology at the resonant point
itself. It works on the Laurent/nearby-cycle associated grade, exactly as required by the pairing
audit of entry 13.

## Why this avoids the earlier ambiguity

Earlier entries correctly observed that a vertex tube or a scalar flip edge does not determine a
unique holomorphic form. That remains true.

The present construction avoids the false step. It lands in

\[
\operatorname{PC}_{\alpha'}(K_\alpha),
\]

not directly in \(\Omega^\bullet(M_n)\). Boundary strata, normal orientation lines, monodromies,
and all lower-face terms remain explicit. The normal-cone image is canonical; a current or de
Rham realization is only a representative of that derived object.

Thus the result is a canonical filtered comparison class, not a canonical gauge fixing.

## Source check

The ingredients used from the standard worldsheet construction are:

1. generic twisted cycles admit a regularization
   \[
   H_*^{\rm lf}(M_n,\mathscr L)
   \xrightarrow{\rm reg}
   H_*(M_n,\mathscr L);
   \]
2. the one-dimensional regularization has endpoint-circle coefficients
   \[
   (e^{2\pi i s}-1)^{-1};
   \]
3. after the minimal/Deligne--Mumford blowup the singular divisor is normal crossing;
4. each real chamber is an associahedron;
5. higher-dimensional Pochhammer contours are products in normal-crossing charts;
6. an associahedral facet is a product of lower associahedra.

These are the precise standard inputs needed for the construction. The scalar grading,
occurrence cosheaf, two-slot coaction, rooted-spine naturality, and order-of-operations statement
are Marici results.

## Epistemic boundary

Established here:

1. a finite nonresonant facewise Pochhammer/Cousin target;
2. a canonical normal-cone comparison from undecorated associahedral cells
   and from the transverse occurrence-decorated scalar subcomplex;
3. strict lifting of the all-arity mixed-cell coaction;
4. monoidality on physical boundary products;
5. exact recovery of the scalar \(1/X_e\) coaction as the \(V_e\)-associated grade;
6. simultaneous nested-cut compatibility;
7. deck covariance inherited from the scalar complex and cyclic chamber rotation;
8. independence from collar choices in the filtered derived category.

Not established here:

1. the scalar-facet coefficient specialization on dependent/nontransverse
   associahedral faces, hence a decorated chain map on the complete scalar
   envelope;
2. a privileged smooth twisted-form representative;
3. a canonical chain-level inverse of the global scalar intersection pairing;
4. an off-shell representative;
5. equality with \((\operatorname{Pf}'A)^2\) before passing to the derived/cohomological class;
6. a claim that the finite-\(\alpha'\) regulator is uniquely abelian Z-theory or any other string
   completion.

## Decision

Promote:

> After extracting the scalar normal grade, every undecorated associahedral
> face and every transverse occurrence-decorated cell has a canonical image
> in the finite, nonresonant generalized-Pochhammer/Cousin complex. The
> physical normal factor is
> \((2\pi i\alpha')/(e^{2\pi i\alpha'X_e}-1)\); it differs from \(1/X_e\)
> only by an analytic unit. Hence the all-arity two-slot scalar coaction is
> exactly the physical nearby-cycle associated grade of a monoidal
> loaded-worldsheet coaction on its proved transverse domain.

The first missing extension is now sharply typed by entry 71:

> construct the occurrence-decorated five-term Cousin identity on one
> eight-point route pentagon, including its scalar-facet specialization and
> lower-face terms, then rotate it through the single deck orbit.

After that, the original pairing test remains:

> apply derived Verdier index raising to this covector-valued comparison, prove that its complete
> Parke--Taylor period vector is the scalar grade, and use perfectness to identify the resulting
> worldsheet class with \([(\operatorname{Pf}'A)^2]\) while retaining the pre-pairing Cousin
> factorization law.
