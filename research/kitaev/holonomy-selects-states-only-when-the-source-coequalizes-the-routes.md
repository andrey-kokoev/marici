# Holonomy selects states only when the source coequalizes the routes

## Correction

Nontrivial loop holonomy reduces an admissible equalizer only when the source declares the competing routes to represent the same constructor-level result. Scalar agreement of the routes is insufficient.

This is the authority gate missing from the common-fixed-subspace proposal.

## Two parallel routes

Let

\[
T_1,T_2:V\longrightarrow W
\]

be two source-authorized routes and let \(L:W\to\mathbb C\) be the scalar readout.

There are three distinct possible laws.

### Distinct-process law

Both routes are allowed operations and may produce different outputs. No equality constraint is imposed.

### Scalar coequalizer law

The source proves only

\[
LT_1=LT_2.
\]

Then

\[
(T_1-T_2)V\subseteq\ker L.
\]

The constructor residual may be nonzero and completely scalar-invisible.

### Constructor coequalizer law

The source proves

\[
T_1x=T_2x
\]

for every admissible \(x\), or explicitly defines admissibility by this equation.

Only this law cuts the state space to

\[
C=ker(T_1-T_2).
\]

## Loop form

When \(T_1\) is invertible, define

\[
H=T_1^{-1}T_2.
\]

Constructor coequalization becomes

\[
(H-I)x=0.
\]

Scalar coequalization gives only

\[
LT_1(H-I)x=0.
\]

It does not authorize restriction to \(\operatorname{Fix}(H)\).

## Toric-code hostile case

Within the toric-code ground space, local syndrome is unchanged by a noncontractible logical loop. Let \(H\) be such a logical operator and \(L\) the local syndrome readout. Then

\[
LH=L.
\]

But physical code states are not required to satisfy

\[
Hx=x.
\]

Imposing the fixed-point condition would select one logical eigensector and erase the remaining authorized logical states. The loop is a constructor resource, not a compatibility equation.

Thus scalar route agreement cannot be promoted to constructor equalization without changing the theory.

## Rank consequence

Suppose a proposed network gains scalar faithfulness by replacing \(V\) with

\[
C=\bigcap_j\ker(H_j-I).
\]

For every \(H_j\), it must identify the exact source law authorizing state-level invariance. If the available theorem is only

\[
L(H_j-I)=0,
\]

then the claimed domain reduction is unsupported.

The first failed typing is the promotion from a scalar coequalizer to a constructor coequalizer.

## Functional-equation application

A scalar functional equation may identify two completed scalar routes. It does not automatically identify the underlying Fock, Tate, tail, seam, or operator-valued states.

To use Fourier--Tate round trips as fixed-point selectors, the programme needs a lifted natural transformation or operator identity on the declared source domain. Equality after Tate integration does not supply that identity.

Two operator lifts can have the same scalar section and different seam or logical action. They define the same scalar coequalizer and different constructor equalizers.

## Legitimate alternatives

Nontrivial holonomy can still contribute in three ways without an unauthorized fixed-point restriction.

### Measurement

Add a constructor-complete loop probe that reads the holonomy sector rather than forcing it to be trivial.

### Controlled selection

Use a source-authorized projector or boundary condition that deliberately selects an eigensector of \(H\).

### Energy penalty

Derive a positive source term involving \(H-I\), and prove that admissible minimizers or zero-energy states lie in its kernel. The positivity and zero-energy premise must be independent.

## Minimal audit

For every proposed route equality, report:

1. the two typed source routes;
2. their common domain and codomain;
3. whether equality is constructor-level or scalar-only;
4. the residual image \((T_1-T_2)V\);
5. whether that image lies merely in \(\ker L\);
6. the exact authority for any fixed-point restriction;
7. the dimension removed by the authorized restriction.

## RH consequence

The multi-object network can shrink the off-seam admissible state space only through independently source-authorized constructor coequalizers, noninvertible incidence, boundary conditions, or energy-minimizing laws. Scalar functional-equation agreement cannot do this work by itself.

The missing operator lift is therefore not a technical embellishment. It decides whether the sheet loop is:

- an equality constraint;
- a measurable sector action;
- or an invisible scalar-kernel ambiguity.

## Verdict

Holonomy is a selector only under a declared constructor-level invariance law. Otherwise it is an operation or observable. Replacing scalar path agreement by a state fixed-point equation manufactures domain reduction and can erase legitimate sectors.
