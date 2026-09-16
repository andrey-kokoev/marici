# The universal logarithmic divergence has an exact Følner-module feature and orthogonal residual

## Scope

This note constructs a positive feature carrying the universal volume term on the **finite-window regular reference carrier**. It does **not** yet realize Connes's actual one-sided physical/Fourier product cutoff, identify the residual with the completed Weil form, or identify the volume module with the Eisenstein radical.

Let

\[
\mathcal M_S=VN(C_S)
\]

be the von Neumann algebra of the semilocal scaling group, with its canonical semifinite Plancherel trace \(\tau_S\). Put

\[
H_{\mathrm{obs},S}=L^2(\mathcal M_S,\tau_S).
\]

For an observer \(g\), write \(\Xi_S(g)\in H_{\mathrm{obs},S}\) for its left-regular convolution vector. Then

\[
\langle \Xi_S(g_1),\Xi_S(g_2)\rangle
=\tau_S(U_S(g_2)^*U_S(g_1)),
\]

and, for \(h=g*g^*\),

\[
\|\Xi_S(g)\|^2=h(1).
\]

Thus \(\Xi_S\) is the bulk GNS feature; it is an isometric copy of the whole observer space, not one vector.

## Følner feature space

Use logarithmic coordinates on the noncompact scaling direction. Let \(I_\alpha\) be a finite cutoff packet of Haar volume

\[
V_\alpha=\mu(I_\alpha).
\]

For the symmetric finite-window reference cutoff \(I_\Lambda=[-\log\Lambda,\log\Lambda]\),

\[
V_\Lambda=2\log\Lambda.
\]

This interval is an auxiliary regular model. Connes's transformed physical cutoff is the one-sided half-line \(( -\infty,\log\Lambda]\), whose Haar volume is infinite. The numerical equality of scales does not identify the two feature spaces.

Define

\[
e_\alpha=1_{I_\alpha}\in L^2(C_S),
\qquad
\|e_\alpha\|^2=V_\alpha,
\]

and the cutoff feature space

\[
\mathcal K_{\alpha,S}
=L^2(C_S)\widehat\otimes H_{\mathrm{obs},S}.
\]

Define

\[
\boxed{
J_{\alpha,S}\xi
=V_\alpha^{-1/2}e_\alpha\otimes\xi.
}
\]

Then

\[
\begin{aligned}
\langle J_{\alpha,S}\xi,J_{\alpha,S}\eta\rangle
&=V_\alpha^{-1}
\langle e_\alpha,e_\alpha\rangle
\langle\xi,\eta\rangle\\
&=\langle\xi,\eta\rangle.
\end{aligned}
\]

Hence

\[
\boxed{J_{\alpha,S}^*J_{\alpha,S}=I.}
\]

This gives the required cutoff-dependent isometric embedding without asserting a strong limit as \(\alpha\to\infty\).

## Exact bulk vector

Define

\[
\boxed{
T^{\mathrm{bulk}}_{\alpha,S}(g)
=e_\alpha\otimes\Xi_S(g)
=\sqrt{V_\alpha}\,J_{\alpha,S}\Xi_S(g).
}
\]

Its polarized Gram form is exactly

\[
\boxed{
\langle T^{\mathrm{bulk}}_{\alpha,S}(g_1),
T^{\mathrm{bulk}}_{\alpha,S}(g_2)\rangle
=V_\alpha\,
\tau_S(U_S(g_2)^*U_S(g_1)).
}
\]

In particular,

\[
\|T^{\mathrm{bulk}}_{\Lambda,S}(g)\|^2
=2\log\Lambda\,h(1).
\]

This has the same universal scalar coefficient as the counterterm in Connes's trace formula. It is its exact positive realization on the finite-window regular reference carrier, not yet a feature-level factorization of the actual product cutoff.

## Orthogonal bulk projection

The projection onto the bulk copy is

\[
\boxed{
\Pi_{\alpha,S}
=J_{\alpha,S}J_{\alpha,S}^*
=P_{\mathbb C e_\alpha}\otimes I.
}
\]

Explicitly, for a simple tensor \(f\otimes\xi\),

\[
\Pi_{\alpha,S}(f\otimes\xi)
=
\frac{\langle e_\alpha,f\rangle}{V_\alpha}
 e_\alpha\otimes\xi.
\]

For any regulated feature

\[
T_{\alpha,S}:E_S\to\mathcal K_{\alpha,S},
\]

define its orthogonal residual

\[
\boxed{
\mathfrak b_{\alpha,S}(g)
=(I-\Pi_{\alpha,S})T_{\alpha,S}(g).
}
\]

Then

\[
\|T_{\alpha,S}(g)\|^2
=
\|\Pi_{\alpha,S}T_{\alpha,S}(g)\|^2
+
\|\mathfrak b_{\alpha,S}(g)\|^2,
\]

so the residual Gram kernel is positive at every cutoff.

## Exact coefficient map

The bulk coefficient extracted from an arbitrary regulated feature is

\[
\boxed{
\beta_{\alpha,S}(g)
=V_\alpha^{-1/2}J_{\alpha,S}^*T_{\alpha,S}(g).
}
\]

The desired feature-level trace-density theorem is therefore the concrete estimate

\[
\boxed{
\beta_{\alpha,S}(g)
\longrightarrow
\Xi_S(g)
}
\]

uniformly on bounded observer packets. Equivalently,

\[
\Pi_{\alpha,S}T_{\alpha,S}(g)
=
\sqrt{V_\alpha}J_{\alpha,S}\Xi_S(g)
+o(1).
\]

This isolates the remaining analytic assertion: it is a vector-valued Følner mean estimate, not the construction of a guessed divergent line.

## Translation-kernel realization

In the model \(C_S=\mathbb R\), identify a convolution feature with the kernel

\[
K_M(x,y)=1_{[-M,M]}(y)k(x-y).
\]

Under the unitary coordinate change

\[
(u,v)=(x-y,y),
\]

one has

\[
K_M(u,v)=k(u)1_{[-M,M]}(v).
\]

Thus the feature is exactly

\[
K_M=e_M\otimes k
=\sqrt{2M}\,J_Mk.
\]

The familiar identity

\[
\|K_M\|_{HS}^2=2M\|k\|^2
\]

is therefore the norm of the free Følner module. The failure of the normalized kernels to converge strongly is expected because the embeddings \(J_M\) vary with \(M\); it does not obstruct this exact module realization.

## Separation from arithmetic conditioning

The construction uses only:

1. the scaling group;
2. its Haar/Følner packets;
3. the Plancherel trace;
4. the observer GNS space.

It contains no zeta factor and imposes no endpoint-vanishing condition. Therefore

\[
\boxed{
\text{universal volume module}
\ne
\text{Eisenstein radical}
}
\]

unless a separate source-derived intertwiner is proved.

The two operations must remain distinct:

\[
\text{Følner bulk removal}
\quad\text{then}\quad
\text{Eisenstein/Sonin arithmetic conditioning}.
\]

## What is now constructed

The following data are explicit:

\[
(H_{\mathrm{obs},S},\Xi_S),
\qquad
(\mathcal K_{\alpha,S},J_{\alpha,S}),
\qquad
T^{\mathrm{bulk}}_{\alpha,S},
\qquad
\Pi_{\alpha,S},
\qquad
\mathfrak b_{\alpha,S}.
\]

They provide an exact finite-window reference feature for

\[
2\log\Lambda\,h(1)
\]

and a positivity-preserving orthogonal residual operation on that reference carrier.

## Remaining gates

For the actual semilocal two-cutoff feature

\[
T_{\Lambda,R,S}(g)
=
\begin{pmatrix}
Q_\Lambda P_\Lambda U_S(g)\\
Q_\Lambda(P_R-P_\Lambda)U_S(g)
\end{pmatrix},
\]

one still must prove:

1. a common correspondence model in which the displayed \(J_{\Lambda,R,S}\) acts;
2. the coefficient convergence \(\beta_{\Lambda,R,S}(g)\to\Xi_S(g)\) for a specified relation \(R=R(\Lambda)\);
3. convergence of the residual features;
4. arithmetic conditioning by the Eisenstein range;
5. the Sonin boundary identity equating the final residual norm with the completed Weil form.

## Disposition

The universal divergent term has the following canonical positive realization in the finite-window regular reference model:

\[
\boxed{
2\log\Lambda\,h(1)
=
\|1_{[-\log\Lambda,\log\Lambda]}
\otimes\Xi_S(g)\|^2.
}
\]

In that reference model, bulk subtraction can therefore be replaced by the orthogonal operation

\[
\boxed{
T_{\alpha,S}
\longmapsto
(I-J_{\alpha,S}J_{\alpha,S}^*)T_{\alpha,S}.
}
\]

Transport to the actual cutoff cannot use the physical half-line compression alone. It must be built from the finite phase-space operator \(P_\Lambda Q_\Lambda P_\Lambda\), then compared with this reference feature by centered regulator comparison. The Eisenstein and Sonin gates occur only after that physical-alignment step.
