# Convolution successors and character truncations act exactly on the gapless phase-energy spectral tower

## Fixed semilocal stage

Fix \(S\). The completed regular boundary is

\[
R_S
=|\mathcal A_S|
=M_{|a_S|}
\]

on \(\mathscr E_S\), with spectral stages

\[
E_{S,\eta}
=1_{[\eta,\infty)}(R_S)
=M_{1_{\{|a_S|\ge\eta\}}}.
\]

## Convolution successor

Let an admitted convolution successor be represented after Mellin transform by multiplication with \(m_b\):

\[
L_b=M_{m_b}.
\]

Assume \(m_b\) is a bounded multiplier on \(\mathscr E_S\). Since \(R_S\), its radical projection, and every threshold projection are multiplication operators,

\[
L_bR_S=R_SL_b,
\]

\[
L_b1_{\{0\}}(R_S)
=1_{\{0\}}(R_S)L_b,
\]

and

\[
L_bE_{S,\eta}
=E_{S,\eta}L_b.
\]

Thus every bounded convolution successor is an exact spectral morphism with threshold control

\[
\varphi_b(\eta)=\eta.
\]

For two successors,

\[
L_cL_b=M_{m_cm_b}=L_{c*b},
\]

so composition is strict on every spectral stage.

## Character and conductor truncation

Let \(P_F\) be the orthogonal projection onto a finite admitted family of angular characters or conductor sectors. The decomposition

\[
\mathscr E_S
=
\bigoplus_\chi
L^2
\left(
\mathbb R,e_S(\chi,t)dt/2\pi
\right)
\]

makes \(P_F\) diagonal in \(\chi\). Therefore

\[
P_FR_S=R_SP_F
\]

and

\[
P_FE_{S,\eta}=E_{S,\eta}P_F.
\]

Nested truncations satisfy

\[
P_FP_{F'}=P_F
\qquad(F\le F').
\]

Hence character/conductor restriction and inclusion act stagewise on the gapless spectral tower.

## Interchange

Both \(L_b\) and \(P_F\) are diagonal in the angular Mellin representation. When the successor preserves the declared character sector,

\[
P_FL_b=L_bP_F.
\]

Consequently the horizontal conductor and vertical convolution square commutes at every threshold:

\[
P_FE_{S,\eta}L_b
=
L_bE_{S,\eta}P_F.
\]

This instantiates the spectral interchange cell.

## Boundedness certificate

The exact spectral identities require a separate boundedness certificate:

\[
\|M_{m_b}\|_{\mathcal B(\mathscr E_S)}
=
\operatorname*{ess\,sup}_{\chi,t}|m_b(\chi,t)|
<\infty.
\]

For unbounded successor symbols, the same formulas hold on the common multiplication domain. Their completion requires graph-domain invariance and closedness certificates.

## Place enlargement

Place enlargement changes both

\[
e_S
\quad\text{and}\quad
a_S=rac{w_S}{e_S}.
\]

The contractive identity map

\[
\mathscr E_{S\cup\{v\}}
\longrightarrow
\mathscr E_S
\]

therefore need not intertwine \(R_{S\cup\{v\}}\) with \(R_S\). Its spectral transport requires a controlled threshold comparison between \(|a_{S\cup\{v\}}|\) and \(|a_S|\).

Thus exact spectral functoriality is established for fixed-\(S\) convolution successors and character truncations. Place enlargement defines the next comparison gate.
