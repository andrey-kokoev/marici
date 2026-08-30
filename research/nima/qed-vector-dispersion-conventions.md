# Vector-valued fixed-transfer dispersion conventions

Owner: `marici.Nima`

## Frozen source conventions

The physical Cut checker uses all momenta future/past directed as declared in
the Breit--Wheeler packet and helicity order

\[
(++,+-,-+,--).
\]

The source amplitude uses

\[
t_{\rm src}=(p_2+p_3)^2,
\qquad
u_{\rm src}=(p_1+p_3)^2.
\]

We freeze the physical momentum transfer as

\[
T=u_{\rm src}<0
\]

and introduce the crossing-centered coordinate

\[
\nu=s+\frac T2.
\]

Since \(s+t_{\rm src}+T=0\), the crossing
\(s\leftrightarrow t_{\rm src}\) acts by

\[
\nu\longmapsto-\nu.
\]

The physical pair threshold \(s=4m_e^2\), with \(m_e=1\), becomes

\[
\nu_0(T)=4+\frac T2.
\]

The outgoing bra is crossed into the all-incoming source convention by the
already certified rule

\[
(C_{++,++},C_{--,++},-C_{+-,++})
\longmapsto
(\operatorname{Im}\Phi_1,
 \operatorname{Im}\Phi_2,
 \operatorname{Im}\Phi_5).
\]

For the two-channel \(\Phi_1\) crossing packet define

\[
\rho_R=C_{++,++},
\qquad
\rho_L=C_{+-,+-}.
\]

The second entry is not an optional scalar parity assignment: it is the
source-labelled \(s\leftrightarrow t_{\rm src}\) partner.

## Coupled twice-subtracted relation

For \(|\nu|<\nu_0(T)\), the first component obeys

\[
\Phi_1(\nu,T)
=P_0(T)+\nu P_1(T)
+\frac{\nu^2}{\pi}
\int_{\nu_0(T)}^\infty
\frac{d\nu'}{\nu'^2}
\left[
\frac{\rho_R(\nu',T)}{\nu'-\nu}
+\frac{\rho_L(\nu',T)}{\nu'+\nu}
\right].
\]

Its Taylor coefficients are

\[
[\nu^n]\Phi_1
=\frac1\pi\int_{\nu_0}^\infty
\frac{\rho_R+(-1)^n\rho_L}{\nu'^{n+1}}d\nu',
\qquad n\ge2.
\]

Hence

\[
[\nu^2]\Phi_1=J_2^{++}+J_2^{+-},
\qquad
[\nu^3]\Phi_1=J_3^{++}-J_3^{+-},
\]

exactly reproducing the independently certified \(g_2,g_3\) assembly.

## Full helicity crossing is a tensor reshuffle

Write the all-incoming helicity amplitude as

\[
\mathcal A_{h_1h_2h_3h_4},
\qquad h_i\in\{+,-\}.
\]

The crossing \(s\leftrightarrow t_{\rm src}\) is the occurrence
transposition \(p_1\leftrightarrow p_3\). Its action is therefore

\[
(X\mathcal A)_{h_1h_2h_3h_4}
=\mathcal A_{h_3h_2h_1h_4}.
\]

This is a permutation of the 16-dimensional labelled helicity tensor.  It is
not left or right multiplication of the \(4\times4\) physical Cut matrix,
because the permutation changes which legs belong to the initial and final
pairs.

For example,

\[
\mathcal A_{--++}
\xmapsto{X}
\mathcal A_{+--+},
\]

which is exactly the pair

\[
C_{++,++}
\quad\leftrightarrow\quad
C_{+-,+-}
\]

used in the certified \(\Phi_1\) crossed-cut reconstruction.

The permutation has eight fixed labelled helicity words and four two-cycles.
Consequently its eigenspace dimensions before Bose/parity reduction are

\[
\dim V_+=12,
\qquad
\dim V_-=4.
\]

The constant subtraction tensor belongs to \(V_+\), while the linear
subtraction tensor belongs to \(V_-\). Sector symmetries must be applied
after this labelled construction; assigning scalar crossing signs first
would discard legitimate channels.

## Minimal subtraction space

Let

\[
F=(\Phi_1,\Phi_1^{\rm crossed})^T,
\qquad
X=
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
F(-\nu,T)=XF(\nu,T).
\]

The degree-at-most-one subtraction packet

\[
P(\nu,T)=P_0(T)+\nu P_1(T)
\]

must satisfy

\[
XP_0=P_0,
\qquad
XP_1=-P_1.
\]

Therefore

\[
P_0=a(T)(1,1)^T,
\qquad
P_1=b(T)(1,-1)^T.
\]

At \(T=0\), gauge invariance and four-photon softness force

\[
a(0)=b(0)=0,
\]

which is why the forward Cut moments reconstruct \(g_2\) and \(g_3\) without
extra data. At nonzero \(T\), crossing leaves two scalar subtraction
functions.  They are finite-rank boundary data at each fixed transfer, not an
arbitrary helicity phase and not yet a CDD factor.

## Branch and normalization contract

- Electron threshold: the right spectral integral begins at \(s=4\).
- The physical square root is \(\beta=\sqrt{1-4/s}>0\).
- Cut normalization:
  \[
  \operatorname{Im}M=\frac12\int d\Phi_2 A_LA_R^*.
  \]
- The final fourth-photon spherical frame carries the continuous transport
  sign already fixed by the forward optical theorem.
- Exact-amplitude hostile points must use the Region I--III \(w,z\) branches
  from the source implementation; no principal-branch replacement is
  admissible.

## Immediate numerical target

At each fixed \(T<0\), evaluate the dispersive integral and the independent
exact amplitude at three subthreshold real points and two complex conjugate
points. Fit only \(a(T),b(T)\) from two points, then demand prediction of all
remaining points.  A non-affine residual falsifies the claimed subtraction
classification and is the first candidate inner/CDD or missing-cut signal.
