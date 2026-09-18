# Many-many archimedean / connected line carrier

Let `L_infinity` be the Tate line with transition

$$
\gamma_\infty(s)
=\pi^{s-1/2}
\frac{\Gamma((1-s)/2)}{\Gamma(s/2)},
\qquad
\gamma_\infty(1-s)=\gamma_\infty(s)^{-1}.
$$

Let `L_det` be the normalized determinant line of the common relative operator `K`, with finite character

$$
\Delta_3(K)
=e^{-r(K)}\det_3(I+K)
=\det(I+K),
$$

where

$$
r(K)=-\operatorname{Tr}K+\frac12\operatorname{Tr}(K^2).
$$

Define the common line carrier

$$
\mathcal L_{\rm ac}
=\mathcal L_\infty\otimes\mathcal L_{\det}.
$$

Its transition is line-valued and combines the Tate cocycle with the anomaly-normalized connected character. Primitive and square rows are the first and second cumulants of the same `K`; the connected row is its `det_3` tail. Reciprocal `det_2` gluing is retained as a separate relative return and is not multiplied into `Delta_3` twice.

The modular reciprocal action on the endpoint pair is

$$
R_\infty(s)=
\begin{pmatrix}0&\gamma_\infty(s)^{-1}\\
\gamma_\infty(s)&0\end{pmatrix}.
$$

The remaining source identity is that G4 uses this tensor-product line transition and the same relative operator `K` on primitive, square, and connected strata.

Status: common archimedean/connected line carrier defined; common-operator and G4 transition identification remain open.
