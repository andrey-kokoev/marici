# The unilateral theta shift has an exact Stein defect, so two-prime reality requires the bilateral port lift

## Existing source identity

For the translated theta synthesis `J_p`, source Gram

\[
G_p=J_p^*J_p,
\]

valuation shift

\[
A_p=p^{1/2}S,
\]

and moving seam-window observer `B_p`, the exact Stein identity is

\[
G_p-A_p^*G_pA_p=B_p^*B_p.
\]

Thus the unilateral arithmetic/theta shift is contractive in the source Gram,
with a nonzero boundary defect measured by the seam window. It is not unitary
in that carrier.

## Consequence for reciprocal star compatibility

The desired operator identity

\[
A_p^{-1}=A_p^\sharp
\]

cannot hold on the unilateral history space unless the seam observation
vanishes on the state under consideration. Iterating the Stein law yields

\[
\|J_pc\|^2
=\sum_{j\ge0}\|B_pA_p^jc\|^2
\]

for finite labelled packets. Hence vanishing of every transported seam window
would force the analytic state itself to vanish. A nonzero retained base cannot
be made unitary by simply discarding the defect channel.

## Bilateral resolution

The half-line shift has a canonical minimal unitary dilation

\[
V_L=P_+U_Li,
\qquad
U_L^*=U_{-L}
\]

on `L^2(R)`. This is the correct carrier in which inverse translation and
Hilbert adjunction agree before spectral specialization.

To use it for the zero-state packet, the source forcing and observation ports
must lift to vectors or boundary distributions `b_dil,c_dil` satisfying

\[
P_+b_{\rm dil}=b_0,
\qquad
c_{\rm dil}i=c_0,
\]

with the source colocation/metric relation. That lift must retain the seam
energy which appears as `B_p^*B_p` in the compression.

## Minimal seam argument

If the corrected nonzero base `b_z` belongs to the lifted bilateral carrier
and is a generalized prime-translation eigenstate

\[
U_{\log p}b_z=p^{-z}b_z,
\]

then unitarity gives

\[
\|b_z\|=\|U_{\log p}b_z\|
=p^{-\operatorname{Re}z}\|b_z\|.
\]

Since `b_z` is nonzero, this forces `Re z=0`. In practice the statement must be
made in the declared rigging because translation has no nonzero ordinary
`L^2(R)` eigenvectors.

## Disposition

The unilateral theta carrier cannot supply the required star law; its exact
Stein defect proves why. The remaining noncircular route is the already open
bilateral forcing/observation port lift, together with rigged eigenstate
membership of the corrected base. The two-prime trace-square test is a finite
shadow of this stronger dilation statement.