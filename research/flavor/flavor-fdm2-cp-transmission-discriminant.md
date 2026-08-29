# Exact CP-transmission discriminant for the FDM-2 portal: WP1019

## Question

What exact condition distinguishes a complex singlet phase that reaches
physical quark CP from one erased by the mediator portal?

## Admitted domain and quotient

Use the real-coefficient rank-one FDM-2 grammar

\[
Y_d=Y_0+(x+i y)ab
\]

at a CP-broken singlet vacuum. Work in a representative with nondegenerate
diagonal (H_u=\operatorname{diag}(u_1,u_2,u_3)); the final commutator
determinant is a full weak-basis invariant on physical16.

Put (c=Y_0b^T). Each off-diagonal down-Gram entry has the form

\[
(H_d)_{ij}=p_{ij}+i y q_{ij},\qquad
q_{ij}=a_i c_j-c_i a_j.
\]

Thus the imaginary portal response is the bivector (a\wedge c).

## Exact transmission polynomial

Define

\[
T=\operatorname{Im}((H_d)_{12}(H_d)_{23}(H_d)_{31}).
\]

The checker derives

\[
T=y(q_{12}p_{23}p_{31}+p_{12}q_{23}p_{31}
 +p_{12}p_{23}q_{31})-y^3q_{12}q_{23}q_{31}.
\]

Writing

\[
\Delta_u=(u_1-u_2)(u_2-u_3)(u_3-u_1),
\]

one has exactly

\[
\det[H_u,H_d]=2i\Delta_u T.
\]

For nondegenerate spectra, (T=0) is precisely the physical CP-blind portal
hypersurface. The WP90 witness has (T=24/5) and determinant (1152i).

## Contextual partition

The signed Jarlskog readout partitions the portal family into (T<0),
(T=0), and (T>0). It separates these physical classes but selects none.
The condition (T\ne0) is open and generic; treating genericity as source
authority would simply delete the hostile class by assumption.

The smallest exact blind locus is

\[
a\wedge(Y_0b^T)=0.
\]

There every (q_{ij}) vanishes even though (y\ne0). More generally,
nonzero bivector components can still cancel in the cubic expression for
(T).

## Instrument and source gate

The signed Jarlskog/CKM measurement is a physical instrument for (T). It
does not prepare portal coefficients or enforce a nonzero transmission
margin. A genuine selector requires a weak-basis-covariant source law whose
admissible image obeys (|T|\ge\tau>0), with (	au) derived before fitting.

## Smallest exact falsifier

Choose (a\parallel Y_0b^T). Then the singlet remains complex but
(a\wedge(Y_0b^T)=0), hence (T=0). The deliberate contrasting obstruction
is the exact WP90 value (T=24/5\ne0).

## Claim boundary

The equivalence between (T\ne0) and physical CP violation assumes
nondegenerate up and down spectra. This packet derives a discriminator, not a
portal coefficient law, normalization, preparation apparatus, or numerical
prediction. It assigns no implicit time or causal interpretation.

## Disposition

Use (T) as the exact hostile gate for every future FDM-2 coefficient
constructor. Do not call CP transmission selected until an independent source
operation excludes the entire (T=0) hypersurface with a positive calibrated
margin.

Verification: uv run --with sympy python
research/flavor/checkers/wp1019_fdm2_cp_transmission_discriminant.py.
