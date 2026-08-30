# Sheet parity and face orientation are independent local gradings

## Source-extracted four-chart cell

The local comoving carrier has two binary coordinates:

\[
(\varepsilon,f)
\in
\{+,-\}_{\mathrm{sheet}}
\times
\{\mathrm{in},\mathrm{out}\}_{\mathrm{face}}.
\]

The source actions are independent:

- reciprocal Fourier transport exchanges the sheet and reverses \(u\);
- Čech boundary incidence exchanges the valuation faces.

On the discrete chart labels, write

\[
R=\sigma_x\otimes I,
\qquad
J=I\otimes\sigma_x.
\]

Hence

\[
RJ=JR.
\]

Any proposed Adams edge that identifies these involutions is mistyped even if its scalar shadow is correct.

## Face diagonalization

Use the symmetric and oriented face vectors

\[
s=e_{\mathrm{in}}+e_{\mathrm{out}},
\qquad
a=e_{\mathrm{out}}-e_{\mathrm{in}}.
\]

Then

\[
Js=s,
\qquad
Ja=-a.
\]

The source records identify their analytic meanings:

\[
s\longmapsto -1
\]

is the constant fifth-wall overlap, while

\[
a\longmapsto C(u)=1-2H(u)
\]

is the oriented relative current, with

\[
C'(u)=2e^{-\pi u^2}>0.
\]

Thus the local face representation already splits into a boundary channel and a positive bulk channel.

## The first radical is a relative-versus-bulk distinction

If one retains only the Gaussian bulk energy, the symmetric face vector is invisible. In the \((s,a)\) basis its schematic Gram block is

\[
G_{\mathrm{bulk}}
=
\begin{pmatrix}
0&0\\
0&g
\end{pmatrix},
\qquad g>0.
\]

Therefore

\[
\ker G_{\mathrm{bulk}}=\operatorname{span}\{s\}.
\]

This is not permission to quotient away \(s\). The source identifies \(s\) with the constant–delta boundary orbit. The complete relative form must retain a separate wall block:

\[
G_{\mathrm{rel}}
=
G_{\mathrm{bulk}}\oplus G_{\mathrm{wall}}.
\]

Consequently there are two different notions of radical:

1. the radical of bulk energy alone;
2. the radical of the complete relative Green form.

The radical-leakage hostile must use the second. Treating the bulk radical as gauge would erase the fifth wall and manufacture false descent.

## Sheet diagonalization and seam character

Use sheet parity vectors

\[
r_+=e_++e_-,
\qquad
r_-=e_+-e_-.
\]

Then

\[
Rr_+=r_+,
\qquad
Rr_-=-r_-.
\]

The oriented zero-section current is reciprocal-odd, so the arithmetic flux lives in the \(r_-\) sector. The constant overlap and oriented face current are face types, not sheet parities.

Therefore the seam character of the first Adams edge is determined by its sheet-parity block. Taking an adjoint may conjugate the coefficient phase, but it must not exchange \(s\) with \(a\) or \(r_+\) with \(r_-\).

The correct covariance test is blockwise:

\[
R_1 K R_2^{-1}=\chi K^*,
\]

with \(K\) already resolved by sheet parity and face type.

## Positive valuation-excess block

The arithmetic identity supplies

\[
Q_p(r)=\max(r-1,0).
\]

Coupled to the oriented Gaussian density, it gives

\[
\mathcal E_{p,r}(u)
=
2(\log p)Q_p(r)e^{-\pi u^2}\ge0.
\]

This block is strict exactly for \(r\ge2\). Its arithmetic kernel is the squarefree sector. That kernel is distinct from the symmetric face direction and from any gauge radical.

The local null taxonomy is therefore:

- **bulk face-null:** the symmetric overlap direction, rescued by the wall block;
- **arithmetic coefficient-null:** squarefree occupation, requiring a complementary primitive channel;
- **gauge radical:** only vectors null for the complete relative form;
- **observer kernel:** vectors erased by final scalar evaluation.

Conflating any two of these creates a false quotient.

## Minimal local matrix audit

Order the four chart labels as

\[
(+,\mathrm{in}),
(+,\mathrm{out}),
(-,\mathrm{in}),
(-,\mathrm{out}).
\]

The source-derived checker must verify:

1. \(R^2=J^2=I\);
2. \(RJ=JR\);
3. the face change of basis splits \(s\) and \(a\);
4. the sheet change of basis splits \(r_+\) and \(r_-\);
5. the bulk form is supported on the oriented face block;
6. the wall form observes the symmetric face block;
7. valuation excess multiplies only the positive oriented bulk;
8. reciprocal transport preserves face type and assigns the declared sheet character.

Only then should one form the mixed primitive-to-square block.

## New frontier

The local representation and its principal null spaces are now source-extracted. The remaining finite datum is the wall Green block on the constant–delta orbit and its cross pairing with the oriented Gaussian block.

That cross block decides whether the complete relative radical is smaller than the bulk radical and whether primitive squarefree states are observed without corrupting the positive valuation-excess energy.
