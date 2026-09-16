# Canonical full-wall observations do not have theta-cut columns as native graph adjoints

## Question

Does the reciprocal wall graph constructed for Gate 2.B carry a canonical full prime-labelled observation \(\Gamma\) whose native graph adjoint has columns \(p^{-1/2}c_{\log p}\)?

## Claim boundary

Two canonical meanings of full wall observation are available: the jump observation and the one-sided endpoint observation. The jump observation is bounded into the unweighted jump space, while the unweighted endpoint observation fails to map the whole graph into \(\ell^2\). Their native graph adjoints are Green-Riesz columns determined by the graph metric. The theta-cut columns satisfy a different source equation, so neither canonical observation has the required adjoint under the native reciprocal wall norm.

Let \(H_{\mathrm{wall,rec}}\) carry the graph inner product induced by \(\|f\|_{\mathrm{wall,rec}}^2=\|f\|_2^2+\|f'_{\mathrm{reg}}\|_2^2+\sum_a|[f]_a|^2\).

Define the jump observation by \(\Gamma_Jf=([f]_{\log p},[f]_{-\log p})_p\). This map is contractive into \(\ell^2\oplus\ell^2\) because its squared target norm is a sub-sum of the graph norm.

Let \(k_{p,+}=\Gamma_J^{*G}e_{p,+}\). Its defining identity is \(\langle f,k_{p,+}\rangle_G=[f]_{\log p}\) for every \(f\in H_{\mathrm{wall,rec}}\). Testing against \(f\in C_c^\infty(I)\) on any wall-free interval \(I\) gives \(\int_I f\overline{k_{p,+}}+f'\overline{k'_{p,+}}=0\). Hence \(k_{p,+}-k''_{p,+}=0\) weakly on every wall-free interval. The jump-adjoint columns are therefore piecewise homogeneous Green kernels whose interface conditions are fixed by the graph metric.

The required arithmetic column is \(b_{p,+}=p^{-1/2}c_{\log p}\), where \(c_{\log p}\) is the translated completed-theta cut profile with a retained wall atom. Its regular bulk is source-forced by the theta profile rather than by the homogeneous equation \(k-k''=0\). Consequently \(\Gamma_J^{*G}e_{p,+}\neq b_{p,+}\) under the native graph metric.

Define the unweighted endpoint observation formally by \(\Gamma_Ef=(f(\log p+))_p\). Choose a smooth \(H^1\) function agreeing with \(e^{-t/4}\) for \(t\ge1\). Its endpoint samples satisfy \(|f(\log p)|^2=p^{-1/2}\), and \(\sum_pp^{-1/2}=\infty\). Thus \(\Gamma_E\) does not map the whole zero-jump \(H^1\) subspace into \(\ell^2\).

A source-weighted endpoint observation may restore boundedness, but its native adjoint columns remain shifted Green-Riesz kernels for endpoint evaluation. Equality with the theta-cut columns would require a separately chosen source-pulled metric or a complete observation whose functionals are \(f\mapsto\langle f,b_{p,+}\rangle_G\).

The latter choice is exactly \(B^\dagger\) and makes the desired adjoint equality definitional. It is a legitimate joint-graph observation, while it supplies no independent geometric wall-trace derivation.

## Disposition

Step 2 rejects the native full-wall-adjoint route. The bounded jump observation has piecewise homogeneous Green-Riesz adjoints rather than theta-cut columns, and the unweighted endpoint sequence is not \(\ell^2\)-valued on the graph domain. The surviving GSAC route must use a source-pulled joint-graph metric or retain geometric wall observation and arithmetic incidence as distinct legs connected by a nontrivial comparison operator.
