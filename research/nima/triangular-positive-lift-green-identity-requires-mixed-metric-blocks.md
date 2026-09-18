# Triangular positive lift Green identity requires mixed metric blocks

Consider the divisor-preserving reverse-triangular lift

$$
L(z)=
\begin{pmatrix}
F_\Xi(z)&0\\
C_h(z)&E(z)
\end{pmatrix},
$$

where `E(z)` is zero-free and `C_h` is the source-derived causal/arithmetic observation. Its determinant is

$$
\det L(z)=\det E(z)\det F_\Xi(z).
$$

Let the output metric be

$$
J_{\rm out}=
\begin{pmatrix}J_{11}&J_{12}\\J_{12}^*&J_{22}\end{pmatrix}.
$$

Then the upper-left block of

$$
L(w)^*J_{\rm out}L(z)
$$

is

$$
F_\Xi(w)^*J_{11}F_\Xi(z)
+F_\Xi(w)^*J_{12}C_h(z)
+C_h(w)^*J_{12}^*F_\Xi(z)
+C_h(w)^*J_{22}C_h(z).
$$

The off-diagonal block is

$$
F_\Xi(w)^*J_{12}E(z)
+C_h(w)^*J_{22}E(z),
$$

and the auxiliary diagonal is

$$
E(w)^*J_{22}E(z).
$$

Therefore adding the positive feature Gram `C_h(w)^*J_22 C_h(z)` is not enough to produce a conservative realization. The mixed metric block `J_12` and auxiliary input metric must simultaneously satisfy the off-diagonal and auxiliary Green equations.

A block-diagonal metric forces

$$
C_h(w)^*J_{22}E(z)=0
$$

for all `w,z` whenever the input metric has no corresponding mixed block. With `E` invertible and a nonzero feature, this generally fails. Hence the positive one-way lift requires a genuinely polarized mixed metric, not an orthogonal direct-sum energy.

The source candidate for `J_12` is the already constructed ordered Wronskian/linking block, while `J_22` is the positive arithmetic/relative-Haar feature metric. The remaining theorem is that these source-fixed blocks satisfy all three displayed Green equations.

Status: divisor and positive feature kernel closed; conservative promotion reduced to explicit mixed-metric block identities.
