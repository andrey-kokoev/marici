# The Euler--gamma scattering phase is the source-derived Clifford rotor whose connection is the Weil current

## Clifford plane

Let \(\gamma_1,\gamma_2\) be Hermitian Clifford generators with

\[
\gamma_1^2=\gamma_2^2=I,
\qquad
\gamma_1\gamma_2=-\gamma_2\gamma_1.
\]

Then

\[
B_{12}=\gamma_1\gamma_2
\]

is anti-Hermitian and satisfies \(B_{12}^2=-I\). It is the oriented bivector of
the derivative/local-phase plane.

## Source scattering phase

On the real spectral line, write the completed scattering ratio as

\[
J_{loc,S}(t)=e^{i\varphi_S(t)},
\qquad |J_{loc,S}(t)|=1,
\]

with a locally chosen phase on the common smooth core. Its metric connection is

\[
V_{loc,S}(t)
=\frac1{2i}\partial_t\log J_{loc,S}(t)
=\frac12\varphi_S'(t).
\]

Define the Clifford multiplication rotor

\[
\boxed{
\mathcal R_S(t)
=
\exp\left(\frac12B_{12}\varphi_S(t)\right).}
\]

Since \(B_{12}\) is anti-Hermitian and \(\varphi_S\) is real,

\[
\mathcal R_S^*\mathcal R_S=I.
\]

Thus this is a genuine source-derived unitary rotor, not a dilation reconstructed
from assumed positivity.

## Rotor connection

Let \(D=-i\partial_t\). Direct differentiation gives

\[
\mathcal R_S^{-1}D\mathcal R_S
=
D-i\mathcal R_S^{-1}\mathcal R_S'
=
D+\Gamma_{12}V_{loc,S},
\]

where

\[
\Gamma_{12}=-i\gamma_1\gamma_2.
\]

Therefore

\[
\boxed{
\mathcal R_S^{-1}[D,\mathcal R_S]
=
\Gamma_{12}V_{loc,S}.}
\]

The gamma and full prime-power Weil current are exactly the connection of one
Clifford rotor.

## Prime successor

Adjoining \(q\) multiplies the scattering ratio:

\[
J_{loc,S\cup\{q\}}=J_{loc,S}J_q.
\]

Because all increments rotate in the same bivector plane,

\[
\mathcal R_{S\cup\{q\}}
=
\mathcal R_S\mathcal R_q
=
\mathcal R_q\mathcal R_S.
\]

The associated connections add, and discrete curvature vanishes. Hence the
rotor is coherent over the complete finite-prime tower.

## Action on the polyphase prime frame

The complete polyphase row supplies a unitary grade-coordinate frame. The rotor
acts diagonally in the prime/grade labels but nontrivially in the Clifford
phase plane. Consequently the combined operator

\[
U_{poly,S}\otimes\mathcal R_S
\]

is unitary and retains every residue branch while installing the correct
Euler--gamma phase connection.

This solves the previously isolated task of constructing the source-derived
mixing bivector for the **local-current channel**.

## Endpoint direction

Introduce a third Clifford generator \(\gamma_3\) for the endpoint coordinate
\(X=M_t\). Then

\[
\Gamma_{13}=-i\gamma_1\gamma_3
\]

records the Heisenberg orientation because

\[
[D,X]=-iI.
\]

The four-component Clifford square contains both

\[
\Gamma_{12}V_{loc,S}
\quad\text{and}\quad
\Gamma_{13}.
\]

The first is now explicitly the Euler--gamma rotor connection. The second is
the endpoint orientation. Actual evaluation at \(t=\pm i/2\) remains a boundary
trace of the strip graph, not an interior rotor defect.

## Remaining crossing

The rotor constructs the signed local mixing without using Weil positivity. To
obtain the arity-two Weil CP crossing one must still prove that the strip
boundary trace of the rotor-covariant Clifford system equals the completed
endpoint residue pairing on the polarized two-copy source and that the resulting
boundary colligation is contractive.

Thus:

- complete prime polyphase frame: constructed;
- source gamma--prime mixing rotor: constructed;
- flat prime-successor law: exact;
- endpoint boundary attachment and positive colligation: still open.
