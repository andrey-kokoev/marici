# Many-many relative Evans sewing cone

Let `E_Ev` be the independent transverse Evans/Xi carrier and let `G_joint` be the faithful joint Green response graph carrying Fourier–Poisson, linking, and connected/archimedean coordinates.

A source comparison is a holomorphic map

$$
F_{\rm Ev}:E_{\rm Ev}\to G_{\rm joint}.
$$

The relative sewing cone is

$$
\operatorname{Cone}(F_{\rm Ev})
=G_{\rm joint}\oplus E_{\rm Ev}[1]
$$

with differential

$$
d_{\rm cone}
=\begin{pmatrix}d_G&F_{\rm Ev}\\0&-d_{\rm Ev}\end{pmatrix}.
$$

Its boundary coordinate is the response-graph defect

$$
d_T(e)=e_+-\mathbb T e_-
$$

in the quotient of doubled boundary phase space by `Graph(T)`. The prior v17 audit identifies the candidate boundary as the absolute response residual paired against a Wronskian connecting class. The absolute residual has its canonical Hilbert coefficient one. The radial source equation fixes the linking block itself as

$$
K_{\rm link}=-\frac12J_{\rm link}.
$$

Accordingly, the normalized cone-form candidate is

$$
Q_{\rm cone}(e)
=\|d_T(e)\|_{\rm resp}^2
+\langle e,G_{\rm link}e\rangle
+Q_{\rm arch/conn}(e),
$$

where

$$
G_{\rm link}=\begin{pmatrix}0&K_{\rm link}\\-K_{\rm link}&0\end{pmatrix}.
$$

The linking sign is encoded by the oriented block and reverses under slot exchange. The remaining normalization gate is the archimedean/connected term and its cross coupling to the cone.

The required source conditions are: `tau` enters essentially through `d_Ev`; the cone defect is `tau`-divisible rather than identically zero; and `Q_cone` is nonzero on at least one source test away from the Xi divisor.

Status: relative Evans sewing cone assembled; residual and linking coefficients are source-fixed, while archimedean/connected coupling and sign/transversality remain open.
