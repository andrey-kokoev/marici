# Triangular lift three-Green-equation ledger

For the reverse-triangular lift and polarized metric, the conservative identity separates into three block equations.

| Equation | Source block | Status |
|---|---|---|
| Auxiliary diagonal | zero-free causal/Tate feature `E` with positive relative-Haar metric `J_22` | Modulus/phase transport constructed; exact input-output metric placement requires the declared line frame |
| Mixed block | `F_Xi(w)^* J_12 E(z)+C_h(w)^*J_22E(z)` | First open equation; `J_12` candidate is the completed Wronskian/linking block |
| Xi diagonal | bare Xi Green defect plus mixed terms plus `C_h(w)^*J_22C_h(z)` | Positive kernel repair constructed; full equality depends on the mixed equation |

The mixed equation is logically first. If it fails, the positive feature is merely an observer and does not form one conservative system with the Xi pencil. If it holds, substitution into the upper-left block tests whether the repaired positive kernel is exactly the Green defect rather than only a dominating Gram.

Using the source-fixed choices

$$
J_{12}=G_{\rm link},
\qquad
J_{22}=G_{\rm Haar},
$$

the finite two-height test is

$$
F_\Xi(w)^*G_{\rm link}E(z)
+C_h(w)^*G_{\rm Haar}E(z)
=M_{\rm in}(w,z),
$$

where `M_in` is the independently declared mixed input metric row. It must be checked before setting `tau(z)=0`.

Thus the lowest remaining source-derived coherence is not positivity or divisor preservation; both are closed. It is the mixed Wronskian–Haar Green identity coupling the one-way feature to the Xi bordered pencil.

Status: three-equation conservative ledger fixed; mixed Wronskian–Haar identity remains open.
