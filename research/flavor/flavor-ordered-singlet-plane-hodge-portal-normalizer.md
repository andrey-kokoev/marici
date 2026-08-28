# Ordered Singlet-Plane Hodge Portal Normalizer

## Question

Does Strominger's source-derived Hodge bridge transfer to WP877's ordered
simple-parent singlet plane, and if so, which part of the asymmetric portal
does it fix?

## Typed transfer

WP877 supplies two ordered, orthogonal source directions. Normalize them as
\(e_u=u/|u|\) and \(e_v=v/|v|\), and write

\[
P_u=e_ue_u^T,
\qquad
P_v=e_ve_v^T,
\qquad
P_2=P_u+P_v.
\]

The order and orientation define a real complex structure on their plane:

\[
J=e_ve_u^T-e_ue_v^T.
\]

It obeys

\[
J^T=-J,
\qquad
J^2=-P_2,
\qquad
JP_uJ^{-1}=P_v.
\]

This is the exact flavor analogue of Strominger's celestial Hodge operation,
but no scalar extension is required: \(J\) is already a real source operator
on the two-dimensional singlet fiber.

## Unique primitive odd contrast

Let \(S\) be a real symmetric operation supported on the singlet plane and
diagonal in the two source projectors. Then

\[
S=aP_u+bP_v.
\]

Require it to be odd under the source complex structure,

\[
JSJ^{-1}=-S.
\]

This forces \(b=-a\). Requiring primitive unit normalization
\(S^2=P_2\) leaves \(a=\pm1\). Finally, declaring the later-stage line
\(L_v\) positive fixes

\[
H=P_v-P_u.
\]

Thus the ordered two-stage source uniquely fixes the dimensionless portal
contrast, including its relative sign and unit magnitude. The result is not
an arbitrary choice of \(g_n-g_m\): every alternative diagonal primitive
operator either equals \(H\) or reverses the declared source order.

The pair satisfies the real Clifford relations

\[
H^2=P_2,
\qquad
JH=-HJ.
\]

## Transport requirement

If the ordered breaking frame changes along an RG or threshold parameter,
the correct objects are co-moving:

\[
P_i(s)=U(s)P_i(0)U(s)^T,
\quad
J(s)=U(s)J(0)U(s)^T,
\quad
H(s)=U(s)H(0)U(s)^T.
\]

This imports Grothendieck's moving-incidence lesson into flavor: freezing the
contrast while moving its source frame creates an untyped connection
residual. It also matches WP869's Kato-projector transport. The connection or
constructor history is part of the threshold packet; an inclusive scalar
normalization cannot erase it while claiming to retain the labelled portal.

## Instrument transfer

Sontag's disturbance-excitation theorem sharpens the readout gate. Two
detector records do not establish access to the two singlet directions. A
calibrated flavor experiment must independently excite source perturbations
along \(P_u\) and \(P_v\), subtract its baseline, and recover a rank-two
response Jacobian. An inclusive sum row has rank one and erases \(H\).

Aspect's path audit supplies a separate execution gate. The real rotation
\(\exp(\theta J)\) exists algebraically, but for generic \(\theta\) it rotates
the ordered projectors and therefore leaves their stabilizer groupoid. It is
not executable control of the original prepared source unless the breaking
apparatus itself supplies that co-control.

Buzzard's Rosenbrock audit adds a dynamic readout warning. A zero in one
selected detector port can be a transmission zero while a complementary port
remains bright. Hence a vanishing inclusive flavor channel cannot establish
absence of the Hodge-odd source; the complete labelled output family and its
source-to-detector realization must be retained.

Benincasa's endpoint type-separation result is a rejected transfer with useful
force. Flavor's source and sink projectors are not celestial extremal weights
or cosmological marked-fiber points merely because all are called endpoints.
No endpoint algebra transfers without a source-defined comparison map.

Nima's braid-cube result supplies the final coherence gate. Pairwise
compatibility of source selection, RG transport, threshold matching, and
detector realization does not prove that their alternative composites agree.
The eventual end-to-end constructor must retain and test the corresponding
higher residual on the faithful flavor packet.

## Remaining magnitude fiber

The physical portal has the form

\[
G=gH.
\]

The Hodge--Clifford construction fixes \(H\), not the common coupling \(g\).
Both \(g=1\) and \(g=2\) satisfy all dimensionless source relations while
giving different physical intensities. The transfer therefore repairs the
relative sign and normalized representation magnitude, but it does not fix
the gauge--Yukawa fixed point, global RG basin, radial breaking scales, mass
gaps, or calibrated detector units.

## Disposition

Progressive cross-sector transfer. WP877's two compulsory breaking directions
carry a real source Hodge structure that uniquely selects the primitive
ordered contrast \(H=P_v-P_u\). This strengthens the simple-parent branch
from a labelled-projector rigidifier to a dimensionless sign-and-normalization
selector.

It is not yet the complete source principle sought by the programme. The next
calculation remains the full anomaly-free simple-parent gauge--Yukawa system.
It must fix the common coefficient \(g\) and an attractive basin while its
threshold connection transports \((P_u,P_v,J,H)\), and its physical
instrument must expose two independently excited calibrated response
directions.

## Smallest exact falsifiers

- Reversing the ordered frame sends \(J\mapsto-J\) and \(H\mapsto-H\).
- Replacing \(H\) by \(cH\) with \(c^2\ne1\) violates primitive unit
  normalization.
- A threshold mixing term proportional to
  \(e_ue_v^T+e_ve_u^T\) fails to preserve the labelled projectors.
- An inclusive detector row collapses the two source excitations to rank one.
- A selected detector port may have a transmission zero while a complementary
  labelled port remains nonzero.
- Changing \(g\) preserves the dimensionless Clifford packet and changes the
  physical portal magnitude.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp878_ordered_singlet_plane_hodge_portal_normalizer.py
~~~
