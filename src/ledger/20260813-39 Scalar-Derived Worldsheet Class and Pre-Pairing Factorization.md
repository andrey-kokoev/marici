# Scalar-Derived Worldsheet Class and Pre-Pairing Factorization

## Record

Date: 2026-08-13

Status: the scalar-derived Pochhammer/Cousin comparison of entry 38 produces, after taking its
field-theory/nearby-cycle symbol and applying derived Verdier index raising, exactly the CHY class

\[
\boxed{
\mathsf J_n
=
[(\operatorname{Pf}'A_n)^2].
}
\]

The equality is representation independent and is separated by a complete Parke--Taylor basis.
The genuinely new result is not the period argument already recorded in entry 11. It is that the
scalar-derived covector now factorizes in the facewise Pochhammer/Cousin complex before index
raising and before pairing with a Parke--Taylor factor.

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

be the complete occurrence-resolved scalar associated-grade element. Apply the comparison of
entry 38:

\[
\Xi^{\rm PC}_{n,\alpha'}(\alpha)
=
\chi_{\alpha'}\Xi^{\rm sc}_{n,\alpha}.
\]

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

This equality is cell resolved: its summands are the scalar triangulations and marked regional
contacts of entries 26 and 27. It is not inferred from one already-summed NLSM formula.

The direct scalar descent theorem of entry 14 says that the family \(a_{R,n}(\alpha)\) annihilates
the Parke--Taylor kernel. Hence these periods define a representation-independent derived
covector

\[
A^{\rm PC}_{R,n}
\in
(H_n^-)^*.
\]

## Derived index raising

Define

\[
\boxed{
\mathsf J^{\rm PC}_n
=
(I_n^\flat)^{-1}A^{\rm PC}_{R,n}
\in
H_n^+.
}
\]

Equivalently, this is the middle-cohomology image of derived Verdier index raising applied to the
facewise Pochhammer/Cousin covector.

Choose any genuine BCJ-sized Parke--Taylor bases \(B_-\subset H_n^-\) and
\(B_+\subset H_n^+\). The coordinate expression is

\[
\mathsf J^{\rm PC}_n
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
\mathsf J^{\rm PC}_n
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
\mathsf J^{\rm PC}_n
=
[(\operatorname{Pf}'A_n)^2]
\in H_n^+.
}
\]

What has changed relative to entry 11 is the provenance. The covector on the left now arrives
through an intrinsic scalar cell-to-worldsheet normal-cone comparison, rather than being supplied
only as an order-indexed amplitude family.

## Factorization before pairing

Let \(e\) be an allowed physical channel. The scalar occurrence coaction is

\[
G_e(h)
=
-\frac{X_{d_e^0}}{X_e}h_e^0
-\frac{X_{d_e^1}}{X_e}h_e^1.
\]

Entry 38 lifts it before any pairing:

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

On the complete scalar element this gives

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

This is the required factorization naturality before pairing.

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

It is not. The construction now has the sequence

\[
\operatorname{gr}_R A_{\rm scalar}
\longrightarrow
\Xi^{\rm sc}
\xrightarrow{\chi_{\alpha'}}
\Xi^{\rm PC}
\xrightarrow{\operatorname{FT}}
A_R^{\rm PC}
\xrightarrow{(I^\flat)^{-1}}
\mathsf J,
\]

and the factorization square already commutes at the \(\Xi^{\rm PC}\) stage.

Thus the half-object exists as a derived normal symbol before pairing. Pairing identifies and
uses it; pairing does not create its factorization law.

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

The new result is that the \(\mathsf J\) entry is now supplied by a monoidal scalar
normal-cone construction. No additional half-integrand or factorization datum is required.

## Epistemic boundary

Established:

1. representation-independent scalar-derived worldsheet covector;
2. canonical derived index raising;
3. equality of the resulting CHY class with \([(\operatorname{Pf}'A)^2]\);
4. factorization in the Pochhammer/Cousin complex before pairing;
5. nested-cut monoidality;
6. correct nearby-cycle channel quotient at resonance;
7. agreement with reduced-Pfaffian degeneration;
8. closure of the \(\mathsf J\) row in the genus-zero three-generator table.

Not established:

1. equality of a preferred point-set chain or smooth form with the rational Pfaffian expression;
2. uniqueness of the finite-\(\alpha'\) regulator lift as a string completion;
3. a canonical dg inverse of the pairing outside the derived category;
4. modular/all-topology completion of this surface half-object;
5. the proposed adjunction between the scalar first jet and scalar-scaffold lowering operators.

## Decision

Promote:

> The rank-jump/Jordan primitive is an intrinsic, factorization-natural derived half-object of the
> scalar master. Its scalar cellular symbol has a monoidal finite-nonresonant
> Pochhammer/Cousin lift; its physical nearby-cycle symbol factorizes before pairing; and derived
> Verdier index raising identifies the resulting worldsheet class uniquely with
> \([(\operatorname{Pf}'A)^2]\).

The immediate Nima frontier is no longer existence or factorization of \(\mathsf J\). It is the
operator-algebra question suggested by the new scalar-scaffolding literature:

> Is the gauge first-jet raising operation adjoint, under the scalar-derived pairing, to the span
> of diagram-extracting differential lowering operators?
