# 2136 — Component-Resolved Deletion Poles Reproduce the Labelled Normal Module

## Hard-to-vary claim

Every grade-two or grade-three component pole involving two loop distances has the universal relative-Landau factor

\[
\boxed{
p_f-L^2,
}

where `L` is the component site-energy sum and `P_f^2=p_f` is the squared separation of the two distance foci.

For isolated contact components this is exactly the labelled normal direction

\[
\nu_i=P_i^2-X_i^2.
\]

## Universal two-distance calculation

Consider a component pole

\[
q=L+y_a+y_b.
\]

On `q=0`, write

\[
y_b=-L-y_a.
\]

Restrict the three-site Cayley--Menger determinant to this hyperplane and impose the two remaining critical equations. The exact elimination gives, up to a nonzero rational unit,

\[
\boxed{
p_f^2(p_f-L^2)^3\Lambda(p_1,p_2,p_3)^3.
}

Thus the generic component threshold is

\[
L=\pm P_f,
\]

with soft and external-triangle factors separated.

## Grade-two packet

For deletion `S={12,23}`, the components are `G_{13}` and `G_2`:

\[
q_{13}=X_1+X_3+y_{12}+y_{23},
\qquad
q_2=X_2+y_{12}+y_{23}.
\]

The two foci are separated by `P_2`. Their thresholds are

\[
(X_1+X_3)^2=P_2^2,
\qquad
X_2^2=P_2^2.
\]

The first is an existing signed-energy/component-energy divisor. The second is

\[
\nu_2=P_2^2-X_2^2=0.
\]

## Grade-three packet

The three isolated contact poles give cyclically

\[
X_i^2=P_i^2,
\qquad i=1,2,3.
\]

Hence their Landau support is exactly

\[
\boxed{
(\nu_1\nu_2\nu_3)=0,
\qquad
\nu_i=P_i^2-X_i^2.
}

These are the same labelled normal directions whose square-free second-normal products appeared in Entry 698's generic lower algebraic-letter sector.

## Homogeneous specialization

On the homogeneous physical locus

\[
P_i=X_i,
\]

all three isolated-contact thresholds collapse identically. Therefore their information belongs to the labelled normal/Rees geometry and cannot be recovered from the homogeneous scalar restriction alone.

## Classification

\[
\boxed{
\text{correlator deletion ports}
\longrightarrow
\text{the existing labelled }(\nu_1,\nu_2,\nu_3)\text{ normal module}.
}

This is a cross-check of H2 and of the port-adapter architecture. The wavefunction-to-correlator map does not generate a new quartic home; it exposes the same normal directions through a different physical readout.

## Verification

The exact factor appears as `two_distance_component_landau` in

`research/benincasa/marici-gm/src/bin/three_site_deletion_landau.rs`.

## Next falsifier

Compute the first nonzero associated grade of the component-resolved correlator sum at `\nu_i=0`. Determine whether the three isolated-contact contributions generate only the diagonal normal lines `\nu_i`, or whether their additive readout produces a canonical square-free second grade

\[
\langle\nu_1\nu_2,\nu_1\nu_3,\nu_2\nu_3\rangle
\]

matching the generic lower-sector module—without inserting cross-sector coherence by hand.

