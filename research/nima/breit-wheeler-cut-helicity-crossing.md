# Crossing the Breit--Wheeler cut into the Bell helicity basis

For a photon of direction \(n\), the chosen spherical-frame polarization obeys

\[
\epsilon_h(-n)=\epsilon_h(n)^*.
\]

This geometric identity does **not** identify the helicity label in the
unitarity bra with the label of the crossed all-incoming amplitude. The
physical outgoing states occur in the bra; crossing them into the source
convention reverses their helicity labels. The mixed channel also carries the
one-crossing polarization phase.

Consequently, for the physical cut matrix \(C\) ordered by outgoing helicity
pairs \((++,+-,-+,--)\), with the incoming column fixed to \(++\),

\[
\boxed{
\operatorname{Im}\Phi_1=C_{++,++},\qquad
\operatorname{Im}\Phi_2=C_{--,++},\qquad
\operatorname{Im}\Phi_5=-C_{+-,++}=-C_{-+,++}.
}
\]

The independent Euler--Heisenberg gate catches the distinction sharply:
\(C_{--,++}\) gives the known \(M_{++++}\) coefficient
\(-2\alpha^2/15\) at \(t=0\), whereas \(C_{++,++}\) belongs to
\(M_{--++}\). The map is fixed jointly by bra/crossing typing and the source
normalization, not by relabelling matrix rows after the fact.

The equality of the two mixed entries holds numerically to better than
\(3\times10^{-14}\) at three independent nonforward points. Increasing the
phase-space quadrature from order 20 to 32 changes the complete cut matrix by
less than \(2\times10^{-8}\).

Reproduce with
`research/nima/check_breit_wheeler_cut_helicity_crossing.py`.
