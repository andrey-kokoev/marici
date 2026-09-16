# The complete polyphase row is unitary, so its Julia defects cannot supply gamma or endpoints

## Complete branch row

For fixed integer dilation \(r\), let

\[
S_{r,j}e_n=e_{rn+j},
\qquad 0\le j<r.
\]

The branch ranges are mutually orthogonal and partition the complete target
grade basis. Assemble the row synthesis operator

\[
U_r:igoplus_{j=0}^{r-1}\ell^2(\mathbb N)
\longrightarrow\ell^2(\mathbb N),
\qquad
U_r(x_0,\ldots,x_{r-1})
=
\sum_jS_{r,j}x_j.
\]

Orthogonality gives

\[
S_{r,i}^*S_{r,j}=\delta_{ij}I,
\]

and completeness gives

\[
\sum_jS_{r,j}S_{r,j}^*=I.
\]

Therefore

\[
\boxed{U_r^*U_r=I,
\qquad U_rU_r^*=I.}
\]

The complete unweighted polyphase row is unitary.

## Julia defects

The Julia defect operators are

\[
D_{U_r}=(I-U_r^*U_r)^{1/2},
\qquad
D_{U_r^*}=(I-U_rU_r^*)^{1/2}.
\]

Hence

\[
\boxed{D_{U_r}=0,
\qquad D_{U_r^*}=0.}
\]

Consequently the gamma and endpoint return channels cannot be identified with
Julia defects of the complete bare polyphase row. Completing the omitted
residue classes removes the Adams support defect entirely.

## Weighted heat branches

Heat reconstruction attaches diagonal branch multipliers

\[
m_{r,j,t}(n)
=
\sqrt{\frac{w_{rn+j}}{w_n}}
\exp\left[-\frac t2((rn+j)^2-n^2)(\log p)^2\right].
\]

The weighted row is

\[
T_{r,t}=U_r\operatorname{diag}(M_{m_{r,0,t}},\ldots,M_{m_{r,r-1,t}}).
\]

Its defects are diagonal weight deficits:

\[
I-T_{r,t}^*T_{r,t}
=
\bigoplus_j(I-M_{|m_{r,j,t}|^2}).
\]

These depend on the chosen heat weights and time. They encode attenuation
between grade coordinates; they do not contain the gamma logarithmic derivative
or endpoint residues. Identifying them with gamma/endpoints would add an
unsupported metric choice.

## Geometric-algebra interpretation

The polyphase branches form a complete orthonormal frame. Their assembled
versor is already a rotor, so it has no missing orthogonal leg. The required
counter-oriented gamma--endpoint channel must therefore couple to a different
geometric direction, not arise as the defect of grade partition.

## Revised path

The conservative colligation must start from the **signed interaction** between
prime polyphase magnitude and the archimedean/endpoint state, rather than from
the complete branch row alone. Algebraically, seek a coupling bivector \(K_S\)
so that

\[
\mathcal R_S=
\exp(K_S)
\]

acts on

\[
\mathcal H_{poly}
\oplus
\mathcal H_{\infty,end}
\]

and its cross term reproduces the polarized local Tate identity. The branch
partition supplies the prime coordinate frame; the logarithmic contour/Green
identity must supply the mixing bivector.

## Conclusion

The proposed “use the Julia defects of the complete polyphase row” route is
closed: those defects vanish in the natural branch metric. The useful output is
the exact prime frame on which a separately source-derived gamma--endpoint
rotor must act.
