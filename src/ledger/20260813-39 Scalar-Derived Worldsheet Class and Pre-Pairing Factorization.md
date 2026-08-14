# Scalar-Derived Worldsheet Class and Pre-Pairing Factorization

## Record

Date: 2026-08-13

Status: corrected in part by entries 70--75. The complete Parke--Taylor
period vector and derived Verdier perfectness still identify the
representation-independent cohomology class

\[
\boxed{
\mathsf J_n
=
[(\operatorname{Pf}'A_n)^2].
}
\]

The equality is representation independent and is separated by a complete
Parke--Taylor basis. However, the stronger claim that a complete
occurrence-decorated scalar covector already factorizes in the facewise
Pochhammer/Cousin complex before index raising is conditional. Entry 38
supplies that comparison on transverse cells. For the eight nontransverse
pentagons, entries 74--75 now supply a formal scalar-edge Cousin counit, the
correct weighted target cube, and one normalized torsion-free local derived
class. Its occurrence-decorated extension across the source caps and cube is
still missing.

Thus this entry contains two logically distinct results:

1. the cohomological half-class and its Pfaffian-square identification remain
   established;
2. its claimed intrinsic scalar chain provenance and pre-pairing coherent
   factorization are proved only on the transverse subcomplex.

The finite-\(\alpha'\) object is a regulator lift. Its full \(\alpha'\)-dependent class is not
claimed to equal the undeformed Pfaffian square; the equality is for the normalized
field-theory/nearby-cycle class that defines the CHY half-object.

## Correct derived typing

Let

\[
H_n^-
=
H^{n-3}(M_n,\nabla_{-\omega_n}),
\qquad
H_n^+
=
H^{n-3}(M_n,\nabla_{\omega_n}),
\]

and let

\[
I_n:
H_n^-\otimes H_n^+
\longrightarrow K_n
\]

be the generic twisted-intersection pairing. Its flat map is

\[
I_n^\flat:
H_n^+
\xrightarrow{\sim}
(H_n^-)^*.
\]

At chain level the canonical object is the Verdier pairing

\[
\mathbb I_n:
R\Gamma_c
\bigl(M_n,\operatorname{DR}\mathscr L_{-\omega_n}\bigr)
\overset L\otimes
R\Gamma
\bigl(M_n,\operatorname{DR}\mathscr L_{\omega_n}\bigr)
\longrightarrow
K_n[-2(n-3)].
\]

Entry 38 gives a finite, facewise model for the compact/normal-cone side. It does not choose an
inverse between arbitrary point-set dg models. The index raising used here is therefore

\[
(\mathbb I_n^\flat)^{-1}
\]

in the derived category, whose middle-cohomology map is the familiar inverse BAS/KLT pairing.

This distinction removes the apparent conflict between a canonical class and a noncanonical
smooth representative.

## The scalar Pochhammer covector

For each cyclic order \(\alpha\), let

\[
\Xi^{\rm sc}_{n,\alpha}
\in
C_*^{\rm cell}
\bigl(\operatorname{AssEnv}_\alpha;\mathcal L_J\bigr)
\]

be the complete occurrence-resolved scalar associated-grade element. On the
transverse occurrence-decorated subcomplex, apply the comparison of entry 38:

\[
\Xi^{\rm PC}_{n,\alpha'}(\alpha)
=
\chi_{\alpha'}\Xi^{\rm sc}_{n,\alpha}.
\]

As a formula on the **complete** decorated complex, this line is now a target
rather than a theorem. The missing components are the eight-point route
pentagons and their higher-arity analogues. The undecorated Pochhammer face
map exists there, but its scalar occurrence coefficient has not been lifted.

Let

\[
\operatorname{FT}
\]

denote the normalized field-theory symbol: take the leading normal-torus/Pochhammer grade and
replace

\[
\frac{2\pi i\alpha'}
{e^{2\pi i\alpha'X_E}-1}
\]

by its \(V_E\)-leading term \(1/X_E\). The generalized Pochhammer field-theory localization is
vertexwise. A maximal-codimension face labelled by a triangulation \(T\) contributes the scalar
cubic denominator

\[
\frac{\epsilon_T}{\prod_{E\in T}X_E}.
\]

The scalar associated grade acts on these vertex coefficients before the Pochhammer
regularization. Consequently

\[
\boxed{
\left\langle
\operatorname{PT}^-_\alpha,
\operatorname{FT}\Xi^{\rm PC}_{n,\alpha'}
\right\rangle
=
a_{R,n}(\alpha).
}
\]

The period equality is exact. Its interpretation as the period of one
globally assembled cell-resolved Pochhammer chain is conditional on completing
the nontransverse coefficient lift. Independently, entries 14 and 27 provide
the order-indexed scalar grade and its marked regional summands, so the period
vector itself does not depend on that unfinished assembly.

The direct scalar descent theorem of entry 14 says that the family \(a_{R,n}(\alpha)\) annihilates
the Parke--Taylor kernel. Hence these periods define a representation-independent derived
covector

\[
A_{R,n}
\in
(H_n^-)^*.
\]

## Derived index raising

Define

\[
\boxed{
\mathsf J_n
=
(I_n^\flat)^{-1}A_{R,n}
\in
H_n^+.
}
\]

Equivalently, this is the middle-cohomology index raising of the scalar period
covector. Once the nontransverse lift is completed, it should also be the
image of one globally assembled facewise Pochhammer/Cousin covector.

Choose any genuine BCJ-sized Parke--Taylor bases \(B_-\subset H_n^-\) and
\(B_+\subset H_n^+\). The coordinate expression is

\[
\mathsf J_n
=
\sum_{\beta\in B_+}
\operatorname{PT}^+_\beta
(m^{-1})^{\beta\alpha}
a_{R,n}(\alpha).
\]

Because this is the coordinate expression of a derived duality morphism, changes of either basis
give the same class. No pseudoinverse of the full ordering matrix is used.

## Identification with the Pfaffian square

The CHY NLSM formula states

\[
I_n\!\left(
\operatorname{PT}^-_\alpha,
[(\operatorname{Pf}'A_n)^2]
\right)
=
A_n^{\rm NLSM}(\alpha).
\]

The scalar normal-grade theorem gives

\[
a_{R,n}(\alpha)
=
A_n^{\rm NLSM}(\alpha)
\]

for every even cyclic order, while both sides vanish at odd multiplicity. Therefore, for every
\(\alpha\in B_-\),

\[
I_n\!\left(
\operatorname{PT}^-_\alpha,
\mathsf J_n
\right)
=
I_n\!\left(
\operatorname{PT}^-_\alpha,
[(\operatorname{Pf}'A_n)^2]
\right).
\]

Perfectness separates the two classes:

\[
\boxed{
\mathsf J_n
=
[(\operatorname{Pf}'A_n)^2]
\in H_n^+.
}
\]

This cohomological conclusion is the sound part of the claimed provenance.
Until the nontransverse coefficient lift is completed, the covector on the
left is canonically specified by its scalar-derived Parke--Taylor periods,
not yet by one complete occurrence-decorated worldsheet chain.

## Factorization before pairing

Let \(e\) be an allowed physical channel. The scalar occurrence coaction is

\[
G_e(h)
=
-\frac{X_{d_e^0}}{X_e}h_e^0
-\frac{X_{d_e^1}}{X_e}h_e^1.
\]

Entry 38 lifts it before any pairing on its proved transverse domain:

\[
d_{\rm PC}G_e^{\alpha'}
=
G_e^{\alpha'}d_{\rm PC},
\]

and proves the normalized specialization law

\[
\boxed{
\operatorname{gr}_{V_e}^{-1}
\operatorname{Res}^{\rm PC}_e
\chi_{\alpha'}
=
(\chi_{\alpha',L}\boxtimes\chi_{\alpha',R})
G_e.
}
\]

The right-hand side already contains:

1. the physical channel;
2. the oriented normal line;
3. the two source slots;
4. one scalar contact mark in every resulting component;
5. the lower-point product cell;
6. the \(1/X_e\) propagator.

No Parke--Taylor factor and no inverse KLT kernel has entered.

On the transverse occurrence-decorated subcomplex this gives the local
factorization law. The desired extension to the complete scalar element is

\[
\boxed{
\operatorname{gr}_{V_e}^{-1}
\operatorname{Res}^{\rm PC}_e
A^{\rm PC}_{R,n}
=
A^{\rm PC}_{R,L}
\boxtimes
A^{\rm PC}_{R,R}.
}
\]

Forbidden parity channels have no supported leading normal symbol, so both sides vanish.

For a nested cut set \(E\), normal-crossing monoidality and strict cut commutativity give

\[
\operatorname{gr}_{V_E}
\operatorname{Res}^{\rm PC}_E
A^{\rm PC}_{R,n}
=
\boxtimes_{R\in\mathcal R(E)}
A^{\rm PC}_{R}.
\]

These are the required factorization formulas, but their assertion on one
globally assembled occurrence-decorated chain is conditional on the
nontransverse Cousin lift. At cohomology level the same factorization follows
independently from the identified Pfaffian-square class and its standard
boundary degeneration.

## Index raising on the channel quotient

At \(X_e=0\), the full generic pairing is resonant and its full residue matrix is rank deficient.
Do not invert it.

The boundary Verdier pairing instead restricts to the induced channel quotient:

\[
\operatorname{gr}_{V_e}\mathbb I_n
=
\epsilon_e\,
(\mathbb I_L\boxtimes\mathbb I_R),
\]

with \(\epsilon_e\) the plumbing-normal orientation sign. Applying derived duality only on this
quotient gives

\[
\boxed{
\Delta_e^+\mathsf J_n
=
\mathsf J_L\boxtimes\mathsf J_R.
}
\]

This conclusion follows from the pre-pairing covector factorization and perfectness of the two
lower-point pairings. It is not obtained by inverting
\(\operatorname{Res}_e m_n\) on the full \(n\)-point space.

The reduced-Pfaffian degeneration supplies an independent representative-level check:

\[
(\operatorname{Pf}'A_n)^2
\longrightarrow
(\operatorname{Pf}'A_L)^2
(\operatorname{Pf}'A_R)^2
\]

with the appropriate plumbing power in allowed channels and zero leading term in forbidden
channels.

## Natural factorization verdict

The original falsification question was whether

\[
I_{\rm scalar}^{-1}
\operatorname{gr}_R A_{\rm scalar}
\]

was merely an amplitude reconstruction device.

At cohomology level it is not: the complete scalar-derived period covector
determines a unique half-class. At chain level the stronger answer remains
conditional. The intended sequence is

\[
\operatorname{gr}_R A_{\rm scalar}
\longrightarrow
\Xi^{\rm sc}
\overset{\chi_{\alpha'}}{\dashrightarrow}
\Xi^{\rm PC}
\xrightarrow{\operatorname{FT}}
A_R^{\rm PC}
\xrightarrow{(I^\flat)^{-1}}
\mathsf J,
\]

where the dashed arrow is proved on transverse cells and still requires the
nontransverse scalar-facet lift. The factorization square commutes at the
\(\Xi^{\rm PC}\) stage on that proved domain and after passing to the
identified cohomology class. It has not yet been assembled as a globally
coherent pre-pairing chain map.

Thus the half-object exists canonically in cohomology. The stronger statement
that its complete factorization law is already intrinsic before pairing is
the live pentagon/Cousin frontier.

## Consequences for the three-generator web

With twist reversal understood,

\[
\mathsf J^+
=
[(\operatorname{Pf}'A)^2],
\qquad
\mathsf J^-\in H^-.
\]

Therefore the standard scalar-derived pairings remain

\[
\langle\mathsf C,\mathsf J\rangle
=
\mathrm{NLSM},
\]

\[
\langle\mathsf G,\mathsf J\rangle
=
\mathrm{Born\!-\!Infeld},
\]

\[
\langle\mathsf J^-,\mathsf J^+\rangle
=
\mathrm{special\ Galileon}.
\]

These pairings close the \(\mathsf J\) row at cohomology level. A complete
monoidal scalar normal-cone representative still requires the dependent-face
coefficient lift; no additional **cohomology class** is required, but
additional chain-level specialization data is.

## Epistemic boundary

Established:

1. representation-independent scalar-derived period covector;
2. canonical derived index raising;
3. equality of the resulting CHY class with \([(\operatorname{Pf}'A)^2]\);
4. factorization in the Pochhammer/Cousin complex on the transverse
   occurrence-decorated subcomplex;
5. nested-cut monoidality on normal-crossing/transverse channel strata;
6. correct nearby-cycle channel quotient at resonance;
7. agreement with reduced-Pfaffian degeneration;
8. cohomology-level closure of the \(\mathsf J\) row in the genus-zero
   three-generator table.

Not established:

1. a complete occurrence-decorated scalar-to-Pochhammer chain map across
   dependent/nontransverse faces;
2. factorization naturality of one global scalar-derived half-chain before
   pairing;
3. equality of a preferred point-set chain or smooth form with the rational Pfaffian expression;
4. uniqueness of the finite-\(\alpha'\) regulator lift as a string completion;
5. a canonical dg inverse of the pairing outside the derived category;
6. modular/all-topology completion of this surface half-object;
7. the proposed adjunction between the scalar first jet and scalar-scaffold lowering operators.

## Decision

Promote:

> The rank-jump/Jordan primitive is an intrinsic cohomological half-object of
> the scalar master: its complete scalar-derived period vector and derived
> Verdier index raising identify it uniquely with
> \([(\operatorname{Pf}'A)^2]\). Its finite-nonresonant
> Pochhammer/Cousin lift and pre-pairing factorization are established on the
> transverse subcomplex; the complete chain-level statement awaits the
> nontransverse coefficient lift.

The immediate Nima frontier is again the strongest original one:

> construct the loaded five-term Cousin identity on one route pentagon and
> its companion square, using the two saturated incidence/Čech resolutions
> of entry 72, and thereby complete—or falsify—the factorization-natural
> scalar half-chain before pairing.

Only after that closure should the lowering-operator adjunction return to the
front of this branch.
