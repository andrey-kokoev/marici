# Erratum: boundary residue does not compute the absolute Picard period

## Typing correction

The proposed use of equation (A.1) from `Cosmology meets cohomology` was incorrectly typed.

That equation pairs a **relative boundary class** \(\delta_I(\check\varphi_I)\) with a primal logarithmic form and begins by taking \(\operatorname{Res}_I\). The pyramid vertices

\[
d_i=[C_i^+]-[C_i^-]
\]

are instead absolute Picard classes in \(H_2\) of the compactified double-cover surface. They are not automatically the paper's relative \(\delta_I\) classes. Therefore

\[
\operatorname{Res}_{L_i}\varphi=0
\]

does not imply

\[
\langle d_i,\varphi\rangle=0.
\]

A Gysin/Betti--de Rham comparison is required to turn the divisor class into the appropriate de Rham functional.

## Generic v_alg representative recovered

The exact nine-master reducer (`derive_nine_master_residue_connection.py`) specifies

\[
e_7=\frac{1}{\sqrt{K_E}},
\qquad
e_8=\frac{a^2}{\sqrt{K_E}},
\qquad
e_9=\frac{b^2}{\sqrt{K_E}},
\]

up to the common \(da\wedge db\). Ledger entry 169 gives the generic algebraic-kernel vector

\[
\begin{aligned}
v_{\rm alg}(E)={}&
(x^2-y^2)(x^2y^2-E^4)e_7\\
&+2x^2(E^2+y^2)e_8
-2y^2(E^2+x^2)e_9.
\end{aligned}
\]

Hence

\[
\boxed{
\varphi_{v_{\rm alg}}(E)
=
\frac{N_E(a,b)}{\sqrt{K_E(a,b)}}\,da\wedge db
}
\]

with

\[
N_E=(x^2-y^2)(x^2y^2-E^4)
+2x^2(E^2+y^2)a^2
-2y^2(E^2+x^2)b^2.
\]

This supplies the first-order family that was previously thought absent. Notice that \(N_E\) is even in \(E\), while the four fiber locations separate linearly in \(E\). Any antisymmetric first normal response must therefore come from transport of the cycles/marking or from the \(E\)-dependence of \(K_E\), not from a linear term in the numerator.

## Correct next computation

The needed object is one of the following equivalent marked comparisons:

1. the divisor Gysin pairing
   \[
   H_2(\overline S_E,\mathbb Z)\times H^2_{\rm dR}(\overline S_E)
   \to\mathbb C;
   \]
2. a Čech representative of \(c_1(\mathcal O(C_i^+-C_i^-))\) paired with \(\varphi_{v_{\rm alg}}\);
3. an integral Betti transport matrix followed by the known de Rham coordinate projection.

The ordinary wall-residue shortcut is not one of these without an additional theorem identifying \(d_i\) with a relative boundary class.

## Disposition

The central pair-collision and generic \(v_{\rm alg}(E)\) formulas survive. All conclusions deriving route nullity solely from \(\operatorname{Res}_{b=\pm x}=0\) are withdrawn.