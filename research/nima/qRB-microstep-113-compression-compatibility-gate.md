# qRB microstep 113: compression compatibility gate

The canonical approximants `J_n=P_nJ_linkP_n` match physical finite readouts only if

$$
\langle J_nu,v\rangle
-
T_{\alpha_n}(u,v)
\longrightarrow0
$$

on the source core.

A sufficient decomposition is

$$
\langle J_nu,v\rangle-T_{\alpha_n}(u,v)
=
\langle (P_n-I)J_{\rm link}u,v\rangle
+
\langle P_nJ_{\rm link}(P_n-I)u,v\rangle
+\mathcal E_n(u,v),
$$

where `E_n` is the physical regulator/compression residual. Strong convergence of `P_n` controls the first two terms; the source theorem must control `E_n`.

Status: compatibility criterion isolated; physical residual estimate remains open.
