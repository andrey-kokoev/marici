# Correction: external linking is closed; the final local Green gate is ordered bulk polarization

Fresh state supersedes the claim that the anti-diagonal external boundary block remains to be constructed. The completed zero-trace theorem already proves

$$
\mathfrak b_\partial^+-\mathfrak b_\partial^-+\mathfrak F_B=0.
$$

Thus the wall/jump/external-port flux, including the weighted linking transport, is closed. The scalar `omega_p` belongs to that already completed endpoint theorem; recomputing it from the bulk would duplicate the closed boundary construction.

What survives is the ordered zero-trace bulk cross-face polarization. For source states `K_z` and `K_w`, define the sesquilinear two-height form

$$
\mathcal C(w,z)
=\langle D K_w,\,zK_z\rangle
+\langle w K_w,\,D K_z\rangle,
$$

with the corresponding analytic-transpose formula in the analytic lane. On the diagonal,

$$
\mathcal C(z,z)
=2\operatorname{Re}\langle DK_z,zK_z\rangle,
$$

and the oriented face difference is

$$
\Delta_{\rm face}(z)
=4\operatorname{Re}\langle DK_z,zK_z\rangle
=2\mathcal C(z,z).
$$

The positive face sum and resolved Gram do not determine `C`; phase rotation of `DK` preserves all diagonal norms while changing this cross term.

Let `e_1,e_2` be the two resolved face columns. The exact finite residual is the ordered matrix-unit defect

$$
\mathcal R^{\rm bulk}_{ij}(w,z)
=
\mathcal C_{\rm source}(w,z;e_i,e_j)
-
\mathcal C_{\rm arith}(w,z;e_i,e_j),
\qquad i,j\in\{1,2\}.
$$

All four entries must vanish. Checking only the face-energy sum, determinant, or odd endpoint line cannot detect reversal of `E_12` and `E_21`.

For descent through the resolved completion, one must additionally prove

$$
\mathcal C(r,v)=\mathcal C(v,r)=0
$$

for every radical vector `r` of the even zero-trace bulk form. Diagonal radical vanishing alone is insufficient.

Once this ordered bulk identity is combined with the already closed external-flux cancellation, the positive doubled Green balance has no remaining local boundary term. Global closed range and prime-uniform coercivity remain separate completion gates.

Status: endpoint/linking frontier corrected to closed; ordered two-height bulk matrix-unit identity is the earliest remaining local Green coherence.
