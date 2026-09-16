# The full analytical system is the joint-graph realization of the regular and endpoint channels

## Scope

This note constructs the full analytical realization without imposing an additional sign condition on the completed form.  It combines the already constructed regular phase-energy channel, the closed Sonin Green channel, and the intrinsic two-dimensional endpoint bundle on one source-reached graph domain.

## Common augmented carrier

Throughout, Hilbert pairings are linear in the first variable. Thus a coordinate expression for \(\langle u,Jv\rangle\) is \(\mathbf v^*J\mathbf u\).

Let

$$
\mathscr E_S
=
\bigoplus_\chi L^2\!\left(\mathbb R,e_S(\chi,t)\frac{dt}{2\pi}\right)
$$

be the phase-energy completion. The normalized regular multiplier

$$
\mathcal A_S=M_{w_S/e_S}
$$

is bounded and self-adjoint on \(\mathscr E_S\).

This normalization does not replace the original logarithmic multiplication form. Let \(A_S^0=M_{w_S}\) be the maximal self-adjoint multiplication operator on the unweighted Mellin carrier, with closed form domain \(D(\lvert A_S^0\rvert^{1/2})\). Since \(e_S\ge1\), the identity inclusion

$$
\jmath_S:\mathscr E_S\longrightarrow\mathscr H_S
$$

is continuous. The estimate \(\lvert w_S\rvert\le C_Se_S\) places \(\jmath_S\mathscr E_S\) continuously in the form domain of \(A_S^0\). If \(q_S^0\) denotes that closed signed form, then on the common Mellin--Schwartz core, and hence by continuity on \(\mathscr E_S\),

$$
q_S^0(\jmath_Sm,\jmath_Sn)
=
\langle m,\mathcal A_Sn\rangle_{\mathscr E_S}.
$$

Thus \(\mathcal A_S\) is the exact Riesz representative of the original Tate form in the phase-energy metric. The bounded realization changes the carrier norm, not the source form.

The explicit common core is

$$
\mathcal C_S
=
\left\{
(m_\chi):
 m_\chi\in C_c^\infty(\mathbb R),
\quad
m_\chi=0
\text{ for all but finitely many }\chi
\right\}.
$$

Angular truncation, radial cutoff, and weighted mollification give

$$
\overline{\mathcal C_S}^{\,\lVert\cdot\rVert_{\mathscr E_S}}
=
\mathscr E_S.
$$

Inverse Mellin transform sends this core to finite-character logarithmic Schwartz observers, so \(\mathcal C_S\) determines the regular multiplier and its functional calculus. Endpoint evaluation requires the distinct analytic subcore obtained from compactly supported physical observers, whose Mellin transforms are entire.

Write the two endpoint functionals as

$$
\ell_+(g)=\widehat g(i/2),
\qquad
\ell_-(g)=\widehat g(-i/2).
$$

They are linearly independent on the compact physical test space. Choose \(p_+,p_-\) there so that

$$
\ell_\sigma(p_\tau)=\delta_{\sigma\tau},
\qquad
\sigma,\tau\in\{+,-\}.
$$

Such packets are obtained by choosing any two tests with an invertible endpoint-evaluation matrix and multiplying the pair by its inverse. Let \(\chi_R\) be a compactly supported logarithmic cutoff and define

$$
g_R^{corr}
=
\chi_Rg
+
\sum_{\sigma\in\{+,-\}}
\bigl(\ell_\sigma(g)-\ell_\sigma(\chi_Rg)\bigr)p_\sigma.
$$

Then \(g_R^{corr}\) is compactly supported and satisfies the exact identities

$$
\ell_\sigma(g_R^{corr})=\ell_\sigma(g).
$$

For a vector in the analytic endpoint graph domain, cutoff convergence gives

$$
\lVert\mathcal M(\chi_Rg)-\mathcal Mg\rVert_{\mathscr E_S}
\longrightarrow0,
\qquad
\ell_\sigma(\chi_Rg)\longrightarrow\ell_\sigma(g).
$$

Because the two correcting packets are fixed elements of \(\mathscr E_S\), their coefficients tend to zero, and therefore

$$
\lVert\mathcal M(g_R^{corr}-g)\rVert_{\mathscr E_S}
\longrightarrow0.
$$

The endpoint difference is identically zero, so \((r_Sg_R^{corr},\beta_Sg_R^{corr})\) converges in the joint-graph norm. This proves density of the compact physical analytic core by an explicit rank-two correction. The regular and joint-graph extensions therefore use compatible dense cores, while the nonanalytic compact-spectral core is not used for off-real endpoint evaluation.

Let \(\mathscr H_{end,S}\) be the source-generated rank-two harmonic-cokernel fiber in its object-indexed evaluation metric. The weighted second-order relative graph is the domain on which endpoint, seam-value, and seam-flux traces are simultaneously continuous; it supplies provenance and boundedness for the endpoint quotient but is not itself the rank-two endpoint fiber.

More precisely, at seam \(a\) the common trace map is

$$
\Gamma_a:
\mathcal H_{rel,a}^2\longrightarrow\mathbb C^4,
\qquad
\Gamma_af
=
\bigl(f(-\infty),f(+\infty),f(a),f'(a)\bigr).
$$

The second graph derivative is essential for continuity of the flux coordinate. The causal Volterra map

$$
(H_ag)(u)=\int_{-\infty}^u g(v)\,dv
$$

is continuous from the derivative-regular source into \(\mathcal H_{rel,a}^2\), with traces

$$
\Gamma_aH_ag
=
\left(0,\int_{\mathbb R}g,
\int_{-\infty}^ag,g(a)\right).
$$

Thus all four traces are source reached. On each reciprocal deficiency channel, the value--flux pair carries the Green boundary form

$$
\omega\bigl((M,J),(\widetilde M,\widetilde J)\bigr)
=
J\widetilde M-M\widetilde J
$$

in the declared bilinear orientation convention. The two reciprocal channels carry the direct sum of this form. Integration by parts for the shifted Laplacian identifies it with the boundary Wronskian, so endpoint evaluation of a bulk exact vector is the corresponding boundary trace rather than an independent coefficient.

Moving-seam transport satisfies

$$
\Gamma_bT_{b\leftarrow a}
=
T_{b\leftarrow a}^{\partial}\Gamma_a
$$

and preserves the oriented total boundary form. The reciprocal-endpoint projection of this trace system, after the established Fourier--Mellin identification, gives the rank-two quotient below; seam value and flux remain in the graph domain that defines the mixed Green row.

Write

$$
\beta_Sg
=
\bigl(m_g(i/2),m_g(-i/2)\bigr)
\in\mathscr H_{end,S}.
$$

On the finite-character Mellin--Schwartz core, set

$$
F_{g,h}(z)=m_g(z)\overline{m_h(\bar z)}
$$

and use the single reflected differential

$$
\Omega_S(z)
=
\frac1{2i}\partial_z\log\frac{M_S(z)}{M_S^\#(z)}
+
\varepsilon_{end}\frac{2z}{z^2+1/4}.
$$

Indented-strip contour deformation gives

$$
\frac1{2\pi i}
\int_{\partial\mathfrak S}F_{g,h}(z)\Omega_S(z)\,dz
=
\langle m_g,V_{loc,S}m_h\rangle
+
E_{end,S}(g,h),
$$

where

$$
E_{end,S}(g,h)
=
(\beta_Sh)^*
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\beta_Sg.
$$

The same contour integral is the Fourier image of the physical Green boundary form. This equality fixes the common source pullback before completion.

The graph Green construction does **not** supply a bounded row from the independently completed bulk to the endpoint fiber. Indeed, there are source vectors \(g_n\) with

$$
r_Sg_n\longrightarrow0,
\qquad
\beta_Sg_n\longrightarrow e_{vert}\ne0.
$$

Choosing an endpoint test whose Green pairing with \(e_{vert}\) is nonzero contradicts every estimate of the form

$$
\lvert b_{src}(g,h)\rvert
\le C\lVert r_Sg\rVert_{\mathscr E_S}
       \lVert\beta_Sh\rVert_{end,S}.
$$

Thus no operator \(B_S:\mathscr E_S\to\mathscr H_{end,S}\) represents the mixed term. The contour identity determines the total form only on correlated source pairs; the vertical endpoint class forces the realization to remain on their closed joint graph.

## Closed Sonin restriction

Let \(V_S=V_{loc,S}\) be the self-adjoint logarithmic connection on the ambient Mellin carrier and set

$$
\mathcal Q_S^{Son}
=
\mathcal S_S\cap D(\lvert V_S\rvert^{1/2}),
$$

using the closure of the source Sonin Schwartz core in the absolute-form graph norm. This is a complete graph Hilbert space. Define

$$
\mathfrak g_S^{Son}(f,h)
=
\left\langle
\lvert V_S\rvert^{1/2}f,
\operatorname{sgn}(V_S)
\lvert V_S\rvert^{1/2}h
\right\rangle.
$$

With

$$
q_S(f,h)
=
\left\langle
\lvert V_S\rvert^{1/2}f,
\lvert V_S\rvert^{1/2}h
\right\rangle,
$$

one has

$$
\lvert\mathfrak g_S^{Son}(f,h)\rvert
\le
q_S(f,f)^{1/2}q_S(h,h)^{1/2}.
$$

so the Sonin form is continuous and closed on \(\mathcal Q_S^{Son}\). This restriction does not require the Sonin projection to reduce \(V_S\); it is a form restriction, not an asserted self-adjoint operator compression.

The differentiated dual--canonical pairing gives its Green identity on the boundary-vanishing core. Reflected contour deformation identifies the resulting boundary term with the endpoint trace system above.

For a prime successor let \(U_{S,q}:\mathcal S_S\to\mathcal S_{S\cup\{q\}}\) be the unitary Euler transition. On the common multiplication core write the affine connection law as

$$
U_{S,q}^*V_{S\cup\{q\}}U_{S,q}
=
V_S+K_{S,q},
$$

where \(K_{S,q}\) is the bounded real prime-current multiplier, with its sign fixed by the chosen connection orientation. Pointwise,

$$
1+\lvert V_S+K_{S,q}\rvert
\le
(1+\lVert K_{S,q}\rVert)(1+\lvert V_S\rvert),
$$

and the same inequality with \(V_S\) and \(V_S+K_{S,q}\) interchanged also holds. Hence

$$
(1+\lVert K_{S,q}\rVert)^{-1/2}
\lVert f\rVert_{Q_S}
\le
\lVert U_{S,q}f\rVert_{Q_{S\cup\{q\}}}
\le
(1+\lVert K_{S,q}\rVert)^{1/2}
\lVert f\rVert_{Q_S}.
$$

Thus \(U_{S,q}\) extends bicontinuously between the completed object-indexed Sonin graph domains. On the core, and then everywhere by form continuity,

$$
\mathfrak g_{S\cup\{q\}}^{Son}(U_{S,q}f,U_{S,q}h)
=
\mathfrak g_S^{Son}(f,h)
+
\langle f,K_{S,q}h\rangle.
$$

For two primes the scalar Euler multipliers and their real current increments commute, so the two iterated pullbacks coincide. This proves flatness of the Sonin form connection. The Sonin restriction, endpoint trace, and joint-graph form are therefore compatible pullbacks of the same logarithmic Green data.

Define the actual augmented carrier as the closed joint source graph

$$
\mathscr G_S
=
\overline{
\{(r_Sg,\beta_Sg):g\in\mathcal C_S^{an}\}
}^{\,\mathscr E_S\oplus\mathscr H_{end,S}},
$$

where \(\mathcal C_S^{an}\) is the compact-physical analytic source core. It is a Hilbert space with the inherited product metric, but need not split as the full Cartesian product.

The endpoint polarization is the bounded Hermitian form

$$
\mathfrak j_{end,S}(u,v)
=
\mathbf v^*
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\mathbf u,
$$

where \(\mathbf u\) and \(\mathbf v\) are the endpoint evaluation coordinate columns of \(u\) and \(v\). The Hadamard parity coordinates

$$
u_{even}=\frac{u_++u_-}{\sqrt2},
\qquad
u_{odd}=\frac{u_+-u_-}{\sqrt2}
$$

diagonalize the endpoint form:

$$
\mathfrak j_{end,S}(u,u)
=
\lvert u_{even}\rvert^2
-
\lvert u_{odd}\rvert^2.
$$

At support radius \(L\), the evaluation Gram is

$$
G_{end}(L)
=
\begin{pmatrix}
2\sinh L&2L\\
2L&2\sinh L
\end{pmatrix}.
$$

It commutes with the swap form. The corresponding metric-weighted signed endpoint matrix has parity eigenvalues

$$
2(\sinh L+L)
\quad\text{and}\quad
2(L-\sinh L).
$$

Thus both parity channels and their support-dependent scaling remain explicit in the object-indexed fiber.

Let \(\mathcal J_{end,S}\) be the Riesz operator of \(\mathfrak j_{end,S}\) with respect to the transported object-indexed endpoint Hilbert metric:

$$
\mathfrak j_{end,S}(u,v)
=
\langle u,\mathcal J_{end,S}v\rangle_{end,S}.
$$

The coordinate swap matrix describes the form; it need not be confused with the Riesz matrix after changing the endpoint Hilbert metric. This distinction avoids identifying the varying endpoint bundle with one fixed Euclidean \(\mathbb C^2\).

## Realizing operator

Let

$$
D_S=\mathcal A_S\oplus\mathcal J_{end,S}
$$

on the ambient product, and let \(\iota_S:\mathscr G_S\hookrightarrow\mathscr E_S\oplus\mathscr H_{end,S}\) be the closed inclusion. The reflected contour identity says exactly that, on the analytic source core,

$$
\mathfrak g_S^{src}(g,h)
=
\left\langle
(r_Sg,\beta_Sg),
D_S(r_Sh,\beta_Sh)
\right\rangle.
$$

Consequently

$$
\begin{aligned}
\lvert\mathfrak g_S^{src}(g,h)\rvert
&\le
\lVert D_S\rVert
\lVert(r_Sg,\beta_Sg)\rVert_{\mathscr G_S}
\lVert(r_Sh,\beta_Sh)\rVert_{\mathscr G_S}.
\end{aligned}
$$

This proves, rather than assumes, continuity in the joint-graph norm. The form descends through the joint response and extends uniquely to \(\mathscr G_S\). If \(P_{\mathscr G_S}\) is the ambient orthogonal projection onto the closed joint graph, its Riesz operator is the explicit compression

$$
\mathbf G_S^{an}
=
\iota_S^*D_S\iota_S
=
P_{\mathscr G_S}D_S\big|_{\mathscr G_S}.
$$

It is bounded and self-adjoint. This is compression of the total diagonal contour readout to correlated source vectors, not a block decomposition of the joint graph and not a mixed row between independently completed factors.

## Canonical feature realization of the complete operator

Because \(\mathbf G_S^{an}\) is bounded and self-adjoint, its Borel functional calculus gives

$$
\mathbf G_S^{an}
=
\operatorname{sgn}(\mathbf G_S^{an})
\lvert\mathbf G_S^{an}\rvert.
$$

Define the complete feature and its signature on the closed generated range by

$$
\Phi_S^{an}
=
\lvert\mathbf G_S^{an}\rvert^{1/2},
\qquad
\mathbf J_S^{an}
=
\operatorname{sgn}(\mathbf G_S^{an}).
$$

Then

$$
(\Phi_S^{an})^*\mathbf J_S^{an}\Phi_S^{an}
=
\mathbf G_S^{an},
$$

and

$$
(\Phi_S^{an})^*\Phi_S^{an}
=
\lvert\mathbf G_S^{an}\rvert.
$$

The kernel of \(\mathbf G_S^{an}\) is retained as the radical, while \(\mathbf J_S^{an}\) is a self-adjoint involution on the orthogonal complement of that kernel. Thus the complete bulk--endpoint operator has an ordinary Hilbert feature together with an exact signed readout; no diagonalization by unknown spectral points or choice of endpoint basis is required.

This feature is minimal in the generated-range sense. Suppose \((F,\mathcal H_F,J_F)\) is another realization satisfying

$$
F^*F=\lvert\mathbf G_S^{an}\rvert,
\qquad
F^*J_FF=\mathbf G_S^{an},
$$

and \(\mathcal H_F=\overline{\operatorname{ran}F}\). The assignment

$$
U\bigl(\Phi_S^{an}x\bigr)=Fx
$$

is well-defined and isometric because the two ordinary Grams agree. It therefore extends uniquely to a unitary from the canonical generated range onto \(\mathcal H_F\). Equality of the signed Grams gives

$$
U\mathbf J_S^{an}=J_FU
$$

on the generated range. Thus every minimal realization with ordinary Gram \(\lvert\mathbf G_S^{an}\rvert\) is uniquely unitarily equivalent to the functional-calculus realization. Additional orthogonal feature summands are nonminimal slack and are not part of the source-generated system.

## Source star and opposite-polarity dagger

The source involution is

$$
\iota(g)=g^*,
$$

which is antilinear, involutive, and reverses convolution order. In centered Mellin coordinates it exchanges the reciprocal endpoint evaluations. Hence the endpoint mate is

$$
J_\partial
\begin{pmatrix}u_+\\u_-\end{pmatrix}
=
\begin{pmatrix}\overline{u_-}\\\overline{u_+}\end{pmatrix},
\qquad
\beta_S\iota=J_\partial\beta_S.
$$

Prior reflected-kernel work constructs an opposite-polarity dagger on its own minimal source-generated kernel features. That theorem must not be transferred automatically to the present functional-calculus feature \(\Phi_S^{an}\).

The unconditional comparison for the present augmented carriers is the closed source-labelled relation

$$
\mathcal J_S^\star
=
\overline{
\{(\widetilde\Psi_{S,+}g,
\widetilde\Psi_{S,-}g^*):g\in X_S\}
}
\subset
\mathcal B_{S,+}^{an}\oplus\mathcal B_{S,-}^{an}.
$$

It is source faithful because each \(\widetilde\Psi_S\) retains the source coordinate. Involutivity of the source star implies

$$
(\mathcal J_S^\star)^{-1}
=
\mathcal J_S^\star
$$

after exchanging the two polarity labels. Its endpoint projection is exactly the graph of \(J_\partial\). Thus the opposite-polarity comparison exists as a closed analytical relation even when it is not the graph of an ambient antiunitary.

Promotion of this relation to an antiunitary operator requires an antiunitary

$$
I_S:\mathscr G_{S,+}\longrightarrow\mathscr G_{S,-}
$$

satisfying

$$
I_S\mathbf G_{S,+}^{an}
=
\mathbf G_{S,-}^{an}I_S
$$

and the source equation

$$
I_SZ_{S,+}g
=
Z_{S,-}g^*.
$$

If these identities are supplied, functional calculus gives the corresponding intertwining of absolute operators and signs, and the assignment on generated features is antiunitary. Without them, the source star is retained as an exact involution of the source and endpoint quotient, while the two complete coupled features are compared by their canonical source-labelled joint graph rather than by an asserted ambient dagger.

Even when a generated-range dagger is available, an extension to unused orthogonal complements of a larger carrier requires an independent antiunitary identification of those complements. No such extension is chosen in this realization.

The complete feature must not be identified with the direct sum of the regular Jordan feature and an endpoint feature. The joint graph has no canonical regular summand, so neither restriction of \(\lvert\mathbf G_S^{an}\rvert\) to \(\mathscr E_S\) nor compression to a regular block is defined. The established two-polarity phase-energy feature remains the canonical realization of the regular face, while \(\Phi_S^{an}\) realizes the correlated joint-graph form.

## Finite-regulator incidence into the regular face

At each finite regulator \(\alpha\), the transported eight-leg feature has a fixed signed readout

$$
D_\alpha=\Theta_\alpha^*K_8\Theta_\alpha.
$$

For every target-adapted finite packet \(E_n\), its compression converges to

$$
A_n=j_n^*\mathcal A_Sj_n.
$$

After the established packetwise common-edge removal, the residual ordinary Gram converges to \(\lvert A_n\rvert\). The inclusion

$$
j_n:E_n\longrightarrow\mathscr E_S
$$

is always an exact morphism for the signed compression, because \(A_n=j_n^*\mathcal A_Sj_n\). It is not generally an isometry for the ordinary absolute Grams:

$$
\lvert A_n\rvert
\ne
j_n^*\lvert\mathcal A_S\rvert j_n
$$

for an arbitrary packet. Therefore the pro-Hilbert packet system and the global regular feature must not be identified packet by packet.

For the established spectrally adapted filtration with packet projections \(P_n\), one has

$$
\bigl\lVert
\lvert P_n\mathcal A_SP_n\rvert
-
P_n\lvert\mathcal A_S\rvert P_n
\bigr\rVert
\le2\delta_n,
\qquad
\delta_n\longrightarrow0.
$$

This gives the precise asymptotic comparison between the packetwise absolute Grams and the global regular absolute operator.

The resulting signed incidence chain is

$$
\text{finite transported cell}
\longrightarrow
\text{cofinal packet system}
\longrightarrow
(\mathscr E_S,\mathcal A_S),
\qquad
\mathscr G_S
=
\overline{\operatorname{ran}(r_S,\beta_S)}.
$$

The first two arrows realize the regular signed face packetwise, with ordinary packet Grams related to the global regular Gram by the asymptotically reducing estimate above. There is no canonical arrow from the independently completed regular carrier into the joint graph: such an arrow would amount to choosing the unavailable splitting of its vertical endpoint sector.

## One source-reached analytical bulk

Let \(\mathsf{Obs}_S\) be the admitted observer source. The four charts are

$$
S_1g=g,
\qquad
S_2g=U_S(g),
$$

$$
S_3g=(\Omega_S^+g,\Omega_S^-g),
\qquad
S_4g=\mathscr R(g).
$$

The complete response is

$$
\mathscr R(g)=(B_g,Q_g,A_g,C_g),
$$

with

$$
B_g(a)=g(a),
\qquad
Q_g(a)=\widehat g(a),
$$

$$
A_g(a)=\int_{-\infty}^ag(x)\,dx,
\qquad
C_g(a)=\operatorname{pv}\int
\frac{e^{-2\pi iax}g(x)}x\,dx.
$$

Its target is

$$
\mathscr Y_S
=
\mathcal S\oplus\mathcal S
\oplus\mathcal H_{rel}^2
\oplus\mathcal H_{rel}^2
$$

with the declared product response topology.

Their inverses on the observer-generated essential images are

$$
R_1=I,
\qquad
R_2(T)=\mathcal F_{C_S}^{-1}(\sigma_T),
\qquad
\mathcal F_{C_S}T\mathcal F_{C_S}^{-1}=M_{\sigma_T}.
$$

$$
R_3(\xi^+,\xi^-)
=(\Omega_S^+)^{-1}\xi^+
=(\Omega_S^-)^{-1}\xi^-,
$$

and

$$
R_4(B,Q,A,C)=B.
$$

The fourth inverse is all-seam flux recovery: the complete response retains the function \(B_g=g\), rather than only one seam scalar. The map

$$
P_{resp}=\mathscr R R_4
$$

is a continuous idempotent on \(\mathscr Y_S\), and its range is the closed response image. Consequently

$$
R_iS_i=I,
\qquad
S_iR_i=I
$$

on every declared essential image.

Let

$$
\Psi_Sg=(S_1g,S_2g,S_3g,S_4g)
$$

be the resulting four-presentation joint graph, and let

$$
r_S:\mathsf{Obs}_S\longrightarrow\mathscr E_S
$$

be its regular phase-energy response. The endpoint response is the independently constructed harmonic-cokernel quotient \(\beta_Sg\) defined above. Define the augmented response by

$$
\widetilde\Psi_Sg=(\Psi_Sg,r_Sg,\beta_Sg).
$$

It is essential here that \(\beta_S\) is not factored through \(r_S\): the vertical endpoint class proves that no such bounded factorization exists.

The source coordinate \(S_1g=g\) is retained in \(\Psi_Sg\). Hence projection to that coordinate is a left inverse of \(\widetilde\Psi_S\), and

$$
\mathcal B_S^{an}=\operatorname{im}\widetilde\Psi_S
$$

is a faithful source-reached analytical bulk. Give it the transported source graph topology. Equivalently, on its ambient product use the continuous idempotent

$$
P_S^{an}=\widetilde\Psi_S\,\pi_1,
$$

where \(\pi_1\) extracts the retained source coordinate. Then

$$
(P_S^{an})^2=P_S^{an},
\qquad
\operatorname{ran}P_S^{an}=\mathcal B_S^{an},
$$

so the realized bulk is closed whenever the admitted source graph is complete.

This joint graph has the expected universal property. Let \(Y\) carry compatible maps \(f_i:Y\to V_i^{obs}\), \(r:Y\to\mathscr E_S\), and \(b:Y\to\mathscr H_{end,S}\) such that

$$
f_j=C_{ij}f_i,
\qquad
r=r_SR_if_i,
\qquad
b=\beta_SR_if_i.
$$

The source map \(g=R_if_i\) is independent of \(i\). There is then a unique continuous map

$$
F_Y:Y\longrightarrow\mathcal B_S^{an},
\qquad
F_Yy=\widetilde\Psi_S(g(y)),
$$

whose coordinate projections are \(f_1,\ldots,f_4,r,b\). Uniqueness follows from the retained source coordinate. Hence \(\mathcal B_S^{an}\) is the source-reached limit of the compatible presentation, regular-response, and endpoint-response diagram, not merely a convenient product embedding.

The analytical readout on this one bulk is the pullback

$$
\widehat{\mathfrak g}_S(g,h)
=
\mathfrak g_S\bigl((r_Sg,\beta_Sg),(r_Sh,\beta_Sh)\bigr).
$$

It is continuous because the joint response and \(\mathfrak g_S\) are continuous in the admitted source graph topology. Its mixed contribution is part of the joint-graph form and is not represented by a row on the Cartesian product. Thus the chart tetrahedron, regular phase-energy response, endpoint response, and mixed Green readout are coordinates and a form on one retained source graph rather than separately juxtaposed objects.

Let \(X_S\) be the completed admitted source graph and define the bounded augmented observation map

$$
Z_S:X_S\longrightarrow\mathscr G_S,
\qquad
Z_Sg=(r_Sg,\beta_Sg).
$$

The complete observer operator is

$$
\mathcal W_S
=
Z_S^*\mathbf G_S^{an}Z_S.
$$

It is bounded and self-adjoint on \(X_S\), and

$$
\widehat{\mathfrak g}_S(g,h)
=
\langle g,\mathcal W_Sh\rangle_{X_S}.
$$

The corresponding source feature is

$$
\widehat\Phi_S^{an}
=
\Phi_S^{an}Z_S.
$$

It satisfies

$$
(\widehat\Phi_S^{an})^*
\mathbf J_S^{an}
\widehat\Phi_S^{an}
=
\mathcal W_S
$$

and has ordinary Gram

$$
(\widehat\Phi_S^{an})^*
\widehat\Phi_S^{an}
=
Z_S^*\lvert\mathbf G_S^{an}\rvert Z_S.
$$

This is the source pullback of the minimal augmented feature, but it need not be the minimal feature of the compressed observer operator. In general,

$$
Z_S^*\lvert\mathbf G_S^{an}\rvert Z_S
\ne
\lvert Z_S^*\mathbf G_S^{an}Z_S\rvert.
$$

The canonical minimal observer feature and signature are instead

$$
\Phi_S^{obs}
=
\lvert\mathcal W_S\rvert^{1/2},
\qquad
J_S^{obs}
=
\operatorname{sgn}(\mathcal W_S).
$$

They satisfy

$$
(\Phi_S^{obs})^*J_S^{obs}\Phi_S^{obs}
=
\mathcal W_S,
\qquad
(\Phi_S^{obs})^*\Phi_S^{obs}
=
\lvert\mathcal W_S\rvert.
$$

Thus the observer source has two exact feature realizations: the inherited joint-graph feature \(\widehat\Phi_S^{an}\), which remembers the correlated regular--endpoint response, and the minimal observer feature \(\Phi_S^{obs}\), which removes compression slack.

Its source radical is

$$
\mathcal N_S^{obs}=\ker\mathcal W_S.
$$

The ambient quotient \(X_S/\mathcal N_S^{obs}\) is Hilbert because the kernel is closed. The minimal observer feature instead completes this quotient in the energy norm induced by \(\lvert\mathcal W_S\rvert\). These norms are equivalent exactly when the reduced minimum modulus of \(\lvert\mathcal W_S\rvert\) is positive.

Without that gap, retain the canonical spectral filtration

$$
X_{S,\eta}^{obs}
=
1_{[\eta,\infty)}(\lvert\mathcal W_S\rvert)X_S,
\qquad
\eta>0.
$$

Each filtered stage is coercive, and the complete minimal observer feature is recovered as \(\eta\downarrow0\). Thus the realization handles both closed-range quotients and gapless spectral-tower completions. Since \(Z_S(X_S)\) is dense in \(\mathscr G_S\) by construction,

$$
\ker\mathcal W_S
=
Z_S^{-1}(\ker\mathbf G_S^{an}).
$$

Indeed, \(\mathcal W_Sg=0\) makes \(\mathbf G_S^{an}Z_Sg\) orthogonal to the dense range of \(Z_S\), hence zero. The converse is immediate.

## Presentation maps

For the four complete-response presentations, retain the already established comparison maps

$$
C_{ij}=S_jR_i,
\qquad
C_{jk}C_{ij}=C_{ik}.
$$

For \(x\in V_i^{obs}\), recover its unique source as \(R_ix\) and define

$$
\mathfrak g_{S,i}(x,y)
=
\widehat{\mathfrak g}_S(R_ix,R_iy).
$$

Then, directly from \(R_jC_{ij}=R_i\),

$$
\mathfrak g_{S,j}(C_{ij}x,C_{ij}y)
=
\mathfrak g_{S,i}(x,y).
$$

Thus every \(C_{ij}\) preserves the realized Hermitian forms on the corresponding essential images. Together with \(C_{jk}C_{ij}=C_{ik}\), this proves strict analytical coherence without making an ill-typed conjugation between carriers in opposite map directions.

For an operator-level statement, equip each \(V_i^{obs}\) with the Hilbert topology transported from \(X_S\) by \(S_i\). Then \(S_i\) is unitary, \(R_i=S_i^*\), and the chart operator and chart feature are

$$
\mathcal W_{S,i}
=
S_i\mathcal W_SR_i,
\qquad
\widehat\Phi_{S,i}^{an}
=
\widehat\Phi_S^{an}R_i,
\qquad
\Phi_{S,i}^{obs}
=
\Phi_S^{obs}R_i.
$$

They satisfy the strict intertwining identities

$$
\mathcal W_{S,j}C_{ij}
=
C_{ij}\mathcal W_{S,i}
$$

and

$$
\widehat\Phi_{S,j}^{an}C_{ij}
=
\widehat\Phi_{S,i}^{an},
\qquad
\Phi_{S,j}^{obs}C_{ij}
=
\Phi_{S,i}^{obs}.
$$

Consequently the twelve chart edges preserve the operator realization, the inherited augmented feature, and the minimal observer feature, not only their scalar pairings. Their radicals obey

$$
C_{ij}(\ker\mathcal W_{S,i})
=
\ker\mathcal W_{S,j},
$$

so every chart transition descends to the nondegenerate source quotient.

Unitary functional calculus further gives, for every Borel set \(\Delta\subset[0,\infty)\),

$$
1_\Delta(\lvert\mathcal W_{S,j}\rvert)C_{ij}
=
C_{ij}1_\Delta(\lvert\mathcal W_{S,i}\rvert).
$$

Hence

$$
C_{ij}
\left(
1_{[\eta,\infty)}(\lvert\mathcal W_{S,i}\rvert)V_i^{obs}
\right)
=
1_{[\eta,\infty)}(\lvert\mathcal W_{S,j}\rvert)V_j^{obs}.
$$

The reduced minimum modulus and the closed-range/gapless alternative are therefore presentation invariant. The entire coercive spectral tower, not merely its limiting radical quotient, is transported strictly by all twelve chart edges.

## Chart rotation and Fourier sewing

The cyclic chart map is defined on the disjoint union of presentation images by

$$
\tau_S(S_ig)=S_{i+1}g,
$$

with indices modulo four. Source reconstruction gives

$$
\tau_S^4=I
$$

and, because every chart form is pulled back from the same source form,

$$
\mathfrak g_{S,i+1}(\tau_Sx,\tau_Sy)
=
\mathfrak g_{S,i}(x,y).
$$

This is the order-four rotation of the presentation charts.

It also has a single linear realization. Set

$$
\mathbb V_S
=
\bigoplus_{i=1}^4V_i^{obs},
\qquad
\mathbb W_S
=
\bigoplus_{i=1}^4\mathcal W_{S,i},
$$

and define \(\boldsymbol\tau_S\) on the \(i\)-th summand by

$$
\boldsymbol\tau_S\big|_{V_i^{obs}}
=
C_{i,i+1},
$$

with indices modulo four. The transported Hilbert norms make \(\boldsymbol\tau_S\) unitary, and strict chart composition gives

$$
\boldsymbol\tau_S^4=I,
\qquad
\boldsymbol\tau_S\mathbb W_S
=
\mathbb W_S\boldsymbol\tau_S.
$$

Let

$$
\mathbb\Phi_S^{an}
=
\bigoplus_{i=1}^4\widehat\Phi_{S,i}^{an}
$$

and let \(\sigma\) cyclically permute the four copies of the common inherited augmented feature carrier. The chart-feature identity gives

$$
\sigma\mathbb\Phi_S^{an}
=
\mathbb\Phi_S^{an}\boldsymbol\tau_S.
$$

The same construction with \(\Phi_{S,i}^{obs}\) gives the cyclic action on the minimal observer features. Thus chart rotation is realized simultaneously on chart carriers, observer operators, radicals, inherited augmented features, and minimal observer features.

## Oriented radial and semilocal Fourier realization

The source Fourier operator also has an independent explicit semilocal realization. Oriented logarithmic radialization retains both signs of the additive coordinate. Mellin transformation then gives, characterwise,

$$
(\mathbb F_Sh)_\chi(t)
=
\gamma_S(\chi,t)h_{\chi^{-1}}(-t).
$$

The Tate factor is unimodular on the real spectral axis, so \(\mathbb F_S\) is unitary. Its exact powers are

$$
\mathbb F_S^2=\mathcal R_{add},
\qquad
\mathbb F_S^4=I,
$$

where \(\mathcal R_{add}\) is additive reflection. The finite local seed pairs and ramified conductor phases are already incorporated in \(\gamma_S\), so no residual scalar phase is introduced.

Differentiation gives the logarithmic connection

$$
a_S=-i\gamma_S^{-1}\partial_t\gamma_S.
$$

The established source calculation shows that this connection is self-adjoint, additive under place enlargement, and commutes with \(\mathbb F_S\). Thus the same Fourier realization acts before and after passage from scattering data to the uncompressed logarithmic current.

On the external radial carrier the quarter turn is the metaplectic lift

$$
\widetilde W_u=C_u\mathcal FC_u^{-1},
\qquad
\widetilde W_u^2=W_u,
\qquad
\widetilde W_u^4=I.
$$

It is not replaced by the reciprocal half-turn \(W_u\). These oriented-radial, spectral, and external-radial operators are source-conjugate presentations of the additive Fourier action.

The shifted-comb orbit is realized on the meromorphic distribution/test-dual rung. For \(0<a<1\), oriented Mellin transformation gives the ordered pair

$$
P_a
\longmapsto
\bigl(\zeta(s,a),\zeta(s,1-a)\bigr).
$$

After Fourier transformation, the zero atom is retained as a separate endpoint port and the nonzero character comb gives

$$
C_{-a}
\longmapsto
\bigl(
\operatorname{Li}_s(e^{-2\pi ia}),
\operatorname{Li}_s(e^{2\pi ia})
\bigr).
$$

The same Tate gamma matrix transports these ordered pairs and closes their four-port orbit without fitted phases. This is a distributional realization: the unsmoothed comb is not inserted into the endpoint or Green Hilbert carriers, and no unregularized Hilbert Gram is assigned to it.

Separately, additive Fourier transformation induces the unitary order-four operator \(\mathbb T_S\) on the complete-response Hilbert essential image. Its Hilbert pairing is transported from the source by

$$
\langle\mathscr Rf,\mathscr Rg\rangle_{resp}
=
\langle f,g\rangle_{L^2}.
$$

On incoming/outgoing pairs use

$$
[(x_-,x_+),(y_-,y_+)]_\partial
=
\langle x_-,y_-\rangle_{resp}
-
\langle x_+,y_+\rangle_{resp}.
$$

The sewing relation is the graph

$$
\Lambda_{\mathbb T_S}
=
\{(x,\mathbb T_Sx):x\in\mathcal H_{resp,S}\}.
$$

Unitarity makes this graph isotropic. If \((u,v)\) is boundary-orthogonal to every \((x,\mathbb T_Sx)\), then

$$
\langle u-\mathbb T_S^*v,x\rangle_{resp}=0
$$

for every \(x\), so \(v=\mathbb T_Su\). Hence

$$
\Lambda_{\mathbb T_S}^{\perp_\partial}
=
\Lambda_{\mathbb T_S},
$$

proving maximal isotropy. The source response satisfies

$$
(\mathscr Rg,\mathscr R(\mathcal Fg))
\in
\Lambda_{\mathbb T_S}.
$$

These two order-four structures are both present in the full analytical system, but they are not identified. The chart rotation permutes source, geometric, spectral, and response presentations; the Fourier operator rotates the four Fourier ports inside the response boundary carrier. An identification would require additional orbit-to-presentation intertwiners and is not used here.

## Chamber and edgewise-subdivision realization

Let \(\mathcal C_7\) denote the seven-transition dependency complex with operation labels \(A,J,P,C,T,E,F\). A realized state consists of a presentation index and a completed-operation ideal. The chart rotation and a source successor act by

$$
\tau_S(i,I)=(i+1,I),
\qquad
U(i,I)=(i,I),
$$

on the combinatorial coordinates, while acting analytically on the corresponding source-reached carriers. Thus operation order and presentation index remain independent coordinates.

The signed asymptotic tetrahedron is a realization functor

$$
\Phi_S^{asym}:\Delta^3\longrightarrow
N_{hc}(\mathsf{Real}_S^{asym}).
$$

Applying the seventh edgewise-subdivision functor gives

$$
\operatorname{esd}_7(\Phi_S^{asym}):
\operatorname{esd}_7(\Delta^3)
\longrightarrow
\operatorname{esd}_7N_{hc}(\mathsf{Real}_S^{asym}).
$$

Every subdivided face is therefore obtained functorially from the already typed presentation comparisons. Degeneracy nodes insert identity maps and do not identify unlike intermediate object types. The complete source form \(\widehat{\mathfrak g}_S\) supplies one common scalar Hermitian readout at every source-reconstructed vertex, so all 343 top-dimensional subdivided tetrahedra commute in the signed analytical realization.

This subdivision statement concerns the signed analytical comparison maps. The stagewise Hilbert features are retained only where independently constructed; functorial subdivision of a signed form is not used to manufacture feature maps at untyped intermediate stages.

## Radical and terminal readout

The analytical radical of the augmented carrier is

$$
\mathcal N_S
=
\ker\mathbf G_S^{an}.
$$

For \(x\in\mathscr G_S\), the condition

$$
\mathfrak g_S(x,y)=0
\quad\text{for every }y\in\mathscr G_S
$$

is equivalent to \(\mathbf G_S^{an}x=0\). Hence \(\mathfrak g_S\) descends to an algebraically nondegenerate Hermitian form on

$$
\mathscr G_S/\mathcal N_S.
$$

Because \(\mathcal N_S\) is the kernel of a bounded operator, it is closed, so the quotient is a Hilbert space in the ambient quotient norm. This norm must be distinguished from the feature-energy seminorm

$$
\lVert[x]\rVert_{\lvert G\rvert}^2
=
\langle x,\lvert\mathbf G_S^{an}\rvert x\rangle.
$$

The map

$$
[x]
\longmapsto
\lvert\mathbf G_S^{an}\rvert^{1/2}x
$$

is an isometry for the feature-energy norm. Its completion is the closed generated feature range

$$
\overline{\operatorname{ran}\lvert\mathbf G_S^{an}\rvert^{1/2}}.
$$

It need not be an isomorphism for the ambient quotient norm unless the reduced minimum modulus is positive. Thus radical quotient, energy completion, and coercive quotient are not silently identified.

This quotient concerns the radical of the completed Hermitian readout. It is distinct from the retained complete-response graph, whose auxiliary graph norm contains the faithful source coordinate and therefore has trivial graph-norm radical.

The function-valued fourth presentation remains the reversible chart. Its completed scalar trace

$$
\rho_4:V_4^{resp}\longrightarrow\mathbb C
$$

is a terminal readout. It is source-defined on the response image, but it is generally noninjective. Therefore \(\rho_4\) has no reverse presentation edge and is not substituted for \(V_4^{resp}\) in the tetrahedron. The realized system consequently has a faithful four-chart analytical bulk followed by a nonfaithful scalar observation, with the two levels explicitly separated.

## Successor laws

Two kinds of successor must be distinguished.

For moving-seam transport at fixed arithmetic stage, let \(T_{b\leftarrow a}\) be bulk graph transport and let \(T^\partial_{b\leftarrow a}\) be its endpoint mate. Source naturality shows that the ambient product unitary maps correlated source pairs to correlated source pairs. Define its restriction

$$
\mathbf T_{b\leftarrow a}
=
\left(
T_{b\leftarrow a}\oplus T^\partial_{b\leftarrow a}
\right)\big|_{\mathscr G_{S,a}}:
\mathscr G_{S,a}\longrightarrow\mathscr G_{S,b}.
$$

Density extends this restriction to a unitary of the two closed joint graphs. Transport of the regular multiplier and endpoint Riesz form gives the exact fixed-stage law

$$
\mathbf T_{b\leftarrow a}^*
\mathbf G_{S,b}^{an}
\mathbf T_{b\leftarrow a}
=
\mathbf G_{S,a}^{an},
$$

and

$$
\mathbf T_{c\leftarrow b}\mathbf T_{b\leftarrow a}
=
\mathbf T_{c\leftarrow a}.
$$

Because \(\mathbf T_{b\leftarrow a}\) is unitary between the corresponding object-indexed Hilbert carriers, bounded Borel functional calculus gives

$$
\mathbf T_{b\leftarrow a}
\lvert\mathbf G_{S,a}^{an}\rvert^{1/2}
=
\lvert\mathbf G_{S,b}^{an}\rvert^{1/2}
\mathbf T_{b\leftarrow a}
$$

and

$$
\mathbf T_{b\leftarrow a}
\operatorname{sgn}(\mathbf G_{S,a}^{an})
=
\operatorname{sgn}(\mathbf G_{S,b}^{an})
\mathbf T_{b\leftarrow a}.
$$

Thus seam transport intertwines not only the signed form but also the complete canonical feature and its signature. It carries

$$
\ker\mathbf G_{S,a}^{an}
\quad\text{onto}\quad
\ker\mathbf G_{S,b}^{an},
$$

so it descends to the radical quotients and to the closed generated feature ranges.

Let \(U_{b\leftarrow a}:X_{S,a}\to X_{S,b}\) be source seam translation in the transported source graph metrics. Source naturality of the regular and endpoint responses gives

$$
Z_{S,b}U_{b\leftarrow a}
=
\mathbf T_{b\leftarrow a}Z_{S,a}.
$$

Consequently

$$
U_{b\leftarrow a}^*
\mathcal W_{S,b}
U_{b\leftarrow a}
=
\mathcal W_{S,a}.
$$

Functional calculus therefore transports the minimal observer features, observer radicals, and every spectral stage:

$$
U_{b\leftarrow a}
1_{[\eta,\infty)}(\lvert\mathcal W_{S,a}\rvert)
=
1_{[\eta,\infty)}(\lvert\mathcal W_{S,b}\rvert)
U_{b\leftarrow a}.
$$

Thus the complete observer spectral tower is seam-natural, not only the inherited joint-graph feature.

Prime enlargement is different. Adjoining a prime changes the logarithmic current by its connection increment. Therefore the current block, and hence the augmented operator, transforms affinely rather than by metric invariance. If \(U_{S,q}\) is the source successor and \(\widetilde U_{S,q}\) its transported action on the augmented source graph, the correct statement is

$$
\widehat{\mathfrak g}_{S\cup\{q\}}
( U_{S,q}g,U_{S,q}h )
=
\widehat{\mathfrak g}_S(g,h)
+
\delta_q(g,h),
$$

where \(\delta_q\) is the total source-derived prime connection increment evaluated on correlated regular--endpoint responses. It is not decomposed into an ambient mixed-row increment. Its continuity on \(X_S\) gives a unique bounded self-adjoint Riesz operator \(\Delta_{S,q}\) such that

$$
\delta_q(g,h)
=
\langle g,\Delta_{S,q}h\rangle_{X_S}.
$$

In operator form, the affine law is

$$
U_{S,q}^*\mathcal W_{S\cup\{q\}}U_{S,q}
=
\mathcal W_S+\Delta_{S,q}.
$$

For two distinct primes \(q\) and \(r\), order independence is the zero-curvature identity

$$
\Delta_{S,q}
+
U_{S,q}^*\Delta_{S\cup\{q\},r}U_{S,q}
=
\Delta_{S,r}
+
U_{S,r}^*\Delta_{S\cup\{r\},q}U_{S,r}.
$$

Equivalently, the covariant derivative, not the current alone, transforms by conjugation.

At feature level, retain the source-labelled successor relation

$$
\mathcal R_{S,q}^{obs}
=
\overline{
\{(
\Phi_S^{obs}g,
\Phi_{S\cup\{q\}}^{obs}U_{S,q}g
):g\in X_S\}
}.
$$

On generating pairs its two signed Grams differ exactly by the connection increment:

$$
\begin{aligned}
&\left\langle
\Phi_{S\cup\{q\}}^{obs}U_{S,q}g,
J_{S\cup\{q\}}^{obs}
\Phi_{S\cup\{q\}}^{obs}U_{S,q}h
\right\rangle\\
&\quad-
\left\langle
\Phi_S^{obs}g,
J_S^{obs}\Phi_S^{obs}h
\right\rangle
=
\delta_q(g,h).
\end{aligned}
$$

This relation is canonical even when the change of absolute Gram prevents a unitary or contractive feature operator. Its exact operator criteria are as follows.

It is the graph of a well-defined map on the algebraic generated range precisely when

$$
\ker\Phi_S^{obs}
\subset
\ker(\Phi_{S\cup\{q\}}^{obs}U_{S,q}).
$$

That map extends boundedly with norm at most \(\sqrt c\) precisely when the source Grams satisfy the Douglas domination

$$
U_{S,q}^*
\lvert\mathcal W_{S\cup\{q\}}\rvert
U_{S,q}
\preceq
c\lvert\mathcal W_S\rvert.
$$

It is contractive when \(c=1\), and isometric exactly when

$$
U_{S,q}^*
\lvert\mathcal W_{S\cup\{q\}}\rvert
U_{S,q}
=
\lvert\mathcal W_S\rvert.
$$

Thus no feature-level successor is asserted beyond the exact kernel and Douglas criteria supported by its two ordinary Grams.

On the four presentation charts, define transported successors by

$$
T_{i,S,q}
=S_{i,S\cup\{q\}}U_{S,q}R_{i,S}.
$$

They satisfy the exact naturality squares

$$
T_{j,S,q}C_{ij,S}
=
C_{ij,S\cup\{q\}}T_{i,S,q}.
$$

The chart representatives of the affine defect are

$$
\Delta_{i,S,q}
=
S_{i,S}\Delta_{S,q}R_{i,S},
$$

and obey

$$
\Delta_{j,S,q}C_{ij,S}
=
C_{ij,S}\Delta_{i,S,q}.
$$

Thus the connection increment is presentation-natural even though it is not an invariant metric.

The feature-successor criteria are presentation invariant as well. For every chart \(i\),

$$
T_{i,S,q}^*
\lvert\mathcal W_{S\cup\{q\},i}\rvert
T_{i,S,q}
\preceq
c\lvert\mathcal W_{S,i}\rvert
$$

holds if and only if the source Douglas domination holds. Likewise,

$$
\ker\Phi_{S,i}^{obs}
\subset
\ker\bigl(
\Phi_{S\cup\{q\},i}^{obs}T_{i,S,q}
\bigr)
$$

is equivalent to the source kernel condition. Hence the canonical successor relation is single-valued, bounded, contractive, or isometric simultaneously in all four presentations; none of these properties depends on the chosen chart.

Assemble the four chart successors into

$$
\mathbb T_{S,q}
=
\bigoplus_{i=1}^4T_{i,S,q}:
\mathbb V_S\longrightarrow\mathbb V_{S\cup\{q\}}.
$$

The adjacent-edge naturality squares are exactly the direct-sum equivariance law

$$
\mathbb T_{S,q}\boldsymbol\tau_S
=
\boldsymbol\tau_{S\cup\{q\}}\mathbb T_{S,q}.
$$

On the retained joint graph this map is simply source transport in every coordinate:

$$
(S_{1,S}g,\ldots,S_{4,S}g)
\longmapsto
(S_{1,S\cup\{q\}}U_{S,q}g,\ldots,
 S_{4,S\cup\{q\}}U_{S,q}g).
$$

Thus the successor cannot leave the source-reached joint bulk, and every chart projection intertwines it with the corresponding \(T_{i,S,q}\). Successors for two distinct primes commute because their scalar phase multipliers commute; consequently this equivariant tower is flat over the finite-place poset.

Thus seam motion is metric-natural, while prime enlargement is connection-natural and flat under changes of prime order. The former must not be used to claim an invariant metric under the latter.

## Placewise assembly of the semilocal tower

For an ordered finite place set \(S=\{v_1,\ldots,v_r\}\), the relative projection current has the exact telescoping decomposition

$$
Q_{\Gamma_S}-\Pi
=
\sum_{k=1}^r(Q_k-Q_{k-1}).
$$

The associated local difference rows form the orthogonal source-labelled feature

$$
D_S^{loc}m
=
\bigoplus_{k=1}^rD_{v_k}^{(k-1)}m,
$$

whose Gram density is the placewise sum

$$
e_S=1+\sum_{v\in S}\kappa_v.
$$

Consequently the regular carrier used above is the completion of one source graph retaining every local energy before the signed place sum. Adjoining a place appends one orthogonal local row, while the signed readout adds the corresponding local current and endpoint/index term.

The conjugated increment rows depend on the declared ordering of \(S\), but their source Gram does not: preceding local phases are commuting multiplication unitaries. Different orderings therefore give unitarily equivalent generated feature ranges, and the summed signed operator is exactly order independent. No canonical unitary on unused ambient feature directions is asserted.

The endpoint assembly follows the same place law. Local endpoint/index contributions add, weighted Adams maps compose exactly, and prime-label cutoffs commute with endpoint pushforward. Hence the finite-place realizations form a source-labelled flat connection tower with strict placewise feature inclusion and object-indexed endpoint transport. This supplies the semilocal tower underlying the stagewise augmented operators rather than treating each finite \(S\) as an unrelated realization.

## Polarized prime cell as a retained-source joint graph

For each prime \(p\), let

$$
E_{p,12}=\mathbb Ce_{p,1}\oplus\mathbb Ce_{p,2}
$$

be the labelled even/odd source plane. The independently constructed Stieltjes/window and theta cut--Wronskian realizations are maps

$$
A_{p,12}:E_{p,12}\longrightarrow\mathcal H_{St,p},
\qquad
C_{p,12}:E_{p,12}\longrightarrow\mathcal H_{\theta,p}.
$$

The source-faithful local cell is

$$
\Gamma_{p,12}
=
\{(x,A_{p,12}x,C_{p,12}x):x\in E_{p,12}\}.
$$

Projection to the first coordinate is its inverse source chart. Hence

$$
P_{p,12}(x,a,c)
=
(x,A_{p,12}x,C_{p,12}x)
$$

is a continuous idempotent, and \(\Gamma_{p,12}\) is closed and complemented. It carries both independently sourced Green forms without identifying them.

The prime cell occurs before history codiagonalization. Its source-authorized target is the resolved three-output boundary object

$$
f\longmapsto(f,Bf,M_\Phi f),
$$

with Green form

$$
\begin{aligned}
\mathfrak G_p^{\theta,res}(f,h)
={}&(1+M_\Phi^2)\langle f,h\rangle
+
\langle Bf,Bh\rangle\\
&+G_{jump,p}(f,h)
+G_{Wr,p}(f,h)
+G_{win,p}(f,h).
\end{aligned}
$$

The causal graph of \(H_\Phi=M_\Phi I+B\) is a downstream history observer. Its additional cross term \(M_\Phi(B+B^*)\) is not a second form on the prime-cell target and is not inserted before the codiagonal.

The coefficient-side Stieltjes plane is generated by \(W_L,W_{2L}\), where \(L=\log p\). Its even window entries are explicit:

$$
G_{p,ab}^{St,even}
=
\langle W_{aL},W_{bL}\rangle
=
2\bigl(R((a+b)L)-R(\lvert a-b\rvert L)\bigr),
\qquad a,b\in\{1,2\}.
$$

Its resolved tail attachment has

$$
\langle BW_L,BW_{2L}\rangle
=
2\bigl(C_{K_+*\rho}(L)-C_{K_+*\rho}(3L)\bigr)>0.
$$

The Wronskian polarization vanishes on this raw even window plane:

$$
\mathcal W(W_{aL},W_{bL})=0.
$$

Hence a nonzero oriented entry cannot be placed directly into the window Gram. It belongs to the independently retained tail--principal-value odd feature.

On the theta side let

$$
w_\theta=
\begin{pmatrix}1/2\\1/2\end{pmatrix},
\qquad
j_\theta=
\begin{pmatrix}1/4\\-1/4\end{pmatrix}.
$$

The endpoint metric is \(2I\), the odd window attachment is the already constructed graph map \(K_pj_\theta=d_p\), and the Wronskian readout is defined on the separate odd feature carrier. Thus the local theta target is the typed direct sum

$$
\mathcal H_{\theta,p}^{cell}
=
\mathcal H_{end,p}
\oplus
\mathcal H_{wall,p}
\oplus
\mathcal H_{tail,p}
\oplus
\mathcal H_{jump,p}
\oplus
\mathcal H_{odd,p},
$$

with its direct-sum Green form. The linear comparison has columns

$$
Q_p^{lin}e_1=w_\theta,
\qquad
Q_p^{lin}e_2=j_\theta.
$$

The even endpoint contribution is already fixed:

$$
\langle w_\theta,w_\theta\rangle_{2I}=1,
\qquad
\langle j_\theta,j_\theta\rangle_{2I}=1/4,
\qquad
\langle w_\theta,j_\theta\rangle_{2I}=0.
$$

Let

$$
F_{end,p},
F_{wall,p},
F_{tail,p},
F_{jump,p}
$$

denote the established source maps from \(E_{p,12}\) into the first four typed legs, with \(F_{end,p}=Q_p^{lin}\). Let \(P_{odd,p}\) be the \(2I\)-orthogonal projection onto \(\mathbb Cj_\theta\). The source record fixes the endpoint and derivative-tail values

$$
Q_p^{lin}e_2=j_\theta,
\qquad
Bj_\theta=-\frac12H_K.
$$

The half-density realization is explicit. Define closed twisted histories

$$
H_-=U_-^{-1}H_0U_-,
\qquad
H_+=U_+^{-1}H_0U_+,
$$

whose outgoing traces are

$$
M_-(g)=\int e^{-u/2}g(u)\,du,
\qquad
M_+(g)=\int e^{u/2}g(u)\,du.
$$

For \(L=\log p\), use the four-front packet

$$
b_p
=
U_{-2L}f_0-U_{2L}f_0-U_{-L}f_0+U_Lf_0,
\qquad
f_0(q)=e^{-\pi q^2}.
$$

It belongs to both twisted graph domains and satisfies

$$
M_-(b_p)=-m_p,
\qquad
M_+(b_p)=m_p,
$$

where

$$
m_p
=
2e^{1/(16\pi)}
\left(\sinh L-\sinh\frac L2\right)>0.
$$

Thus

$$
j_{1/2}(b_p)
=
\frac{M_+(b_p)-M_-(b_p)}{\sqrt2}
=
\sqrt2m_p
=:s_p^{(1/2)}.
$$

Let \(\xi_p=(H_-b_p,H_+b_p)/s_p^{(1/2)}\) in the closed two-history graph carrier and saturate its order-four response orbit. The analytic odd constructor is

$$
F_{odd,p}e_1=0,
\qquad
F_{odd,p}e_2=\frac12\xi_p.
$$

Its half-density odd trace is \(1/2\), matching the norm of the quarter-column \(j_\theta\), and reflection exchanges its two history components. Prime translation supplies labelled copies and finite cutoffs commute with the construction.

The derivative-tail identity \(Bj_\theta=-H_K/2\) gives the corresponding resolved tail shadow. The arithmetic mate is retained as a common-source joint graph. Let

$$
s_p^{src}=Pb_p,
\qquad
\mathbf Mb=(\mathcal M_nb)_{n\ge1}.
$$

The labelwise completion identity is

$$
\mathbf C^{-1}\mathbf M s_p^{src}
=
\mathbf M b_p.
$$

After the ordered primitive, the odd auxiliary column is

$$
d_p=-\frac12S_{ord}b_p,
\qquad
c_p=\mathbf M d_p.
$$

Thus the arithmetic source and analytic half-density histories meet in the closed local relation

$$
\Gamma_{p,12}
=
\{(A_{p,12}x,C_{p,12}x):x\in E_{p,12}\},
$$

and the typed odd constructor is

$$
F_{odd,p}
=
\pi_{odd}^{hist}C_{p,12}.
$$

The scalar

$$
\lambda_{p,\le2}^{(1/2)}
=
\frac{-\kappa_p^{(\le2)}}{2s_p^{(1/2)}}
$$

is a coordinate readout of this retained relation. The constructor itself is the labelled joint graph. With \(F_{odd,p}\) defined on the common primitive/square source, its Green mate \(L_p\) enters the complete theta matrix

$$
\begin{aligned}
H_p^\theta
={}&F_{end,p}^*(2I)F_{end,p}
+F_{wall,p}^*F_{wall,p}
+F_{tail,p}^*F_{tail,p}\\
&+F_{jump,p}^*F_{jump,p}
+F_{odd,p}^*J_{odd,p}F_{odd,p}\\
&+F_{end,p}^*L_p^*F_{odd,p}
+F_{odd,p}^*L_pF_{end,p}.
\end{aligned}
$$

This records the exact local completion. The finite-dimensional joint graph is closed, its positive direct-sum form has zero radical, and both Stokes and Wronskian traces are continuous.

The prime-cell comparison is the concrete identity

$$
G_p^{St}=H_p^{\theta}
$$

in the source basis \((e_1,e_2)\), after the declared radical quotients. The faithful retained-source joint graph exists independently of this stronger identity.

## Global retained-source completion

Let \(E\) be the labelled projective source completion and collect every continuous coordinate into

$$
T=(T_\alpha)_\alpha:E\longrightarrow
Y=\prod_\alpha Y_\alpha.
$$

The coordinates include prime and grade labels, theta labels, resolved histories, endpoint traces, primitive and square dual rungs, connected grades, and the archimedean response. Define

$$
J_Tx=(x,Tx),
\qquad
\mathcal G_T=J_T(E)\subset E\oplus Y.
$$

First-coordinate recovery gives

$$
\pi_EJ_T=I_E.
$$

Therefore

$$
P_T=J_T\pi_E
$$

is a continuous idempotent with range \(\mathcal G_T\). The global retained-source graph is complemented and closed. Its positive graph family retains the separating source seminorms, so its positive radical is zero.

Finite prime-and-grade cutoffs act diagonally and satisfy

$$
P_FJ_T=J_{T_F}P_F^E.
$$

Every local naturality square therefore extends to the projective cutoff system. The connected grades attach through the trace-norm holomorphic operator

$$
K_{\ge3}(z)
=
\sum_p\sum_{k\ge3}K_p^{(k)}(z),
\qquad
\operatorname{Re}z>-1/6,
$$

with locally uniform trace-norm convergence. Thus the connected nuclear leg, cutoff compatibility, global closedness, and radical descent are realized on the retained-source tetrahedron.

The four principal global vertices are obtained by grouping the coordinates into the labelled source, resolved window--Stokes, theta cut--Wronskian, and complete response families. For each group \(i\), let

$$
J_i:E\longrightarrow E\oplus Y_i,
\qquad
J_ix=(x,T_ix),
$$

and write \(\mathcal V_i=J_i(E)\). Each \(\mathcal V_i\) is complemented by \(J_i\pi_E\). Define every directed tetrahedral edge by

$$
C_{ij}=J_j\pi_E\big|_{\mathcal V_i}:
\mathcal V_i\longrightarrow\mathcal V_j.
$$

Then

$$
C_{ji}C_{ij}=I_{\mathcal V_i},
\qquad
C_{jk}C_{ij}=C_{ik}.
$$

Thus all triangular faces commute strictly, and the four vertices form one reversible analytical tetrahedron in their transported projective topologies. Cutoff compatibility follows from

$$
P_FJ_i=J_{i,F}P_F^E,
$$

so every finite tetrahedron maps into the next and converges coordinatewise to the global one. Transporting the source seminorm family along \(J_i\) makes every \(C_{ij}\) an isomorphism of the corresponding multi-rung graph spaces and carries zero radicals to zero radicals.

An output-only codiagonal has its own range topology. The present full realization keeps the labelled source coordinate, with scalar theta synthesis placed downstream as an observer.

## Higher simplicial realization and coherence defects

Let \(I\) be any finite presentation set and let

$$
T_i:E\longrightarrow Y_i,
\qquad i\in I,
$$

be continuous source realizations. Define

$$
J_i x=(x,T_ix),
\qquad
\mathcal V_i=J_i(E),
$$

and

$$
C_{ij}=J_j\pi_E\big|_{\mathcal V_i}.
$$

For every composable string \(i_0,\ldots,i_r\),

$$
C_{i_{r-1}i_r}\cdots C_{i_0i_1}
=
C_{i_0i_r}.
$$

Thus the retained-source presentations form the pair groupoid on \(I\), represented by complemented graph spaces. Its nerve is a strict simplicial analytical object: an \(r\)-simplex is a compatible string of \(r+1\) presentations, and every face or degeneracy map is induced by deleting or repeating a presentation index.

For source-forgetting comparison maps \(D_{ij}:W_i\to W_j\) on independently completed output carriers, define the triangular defect

$$
\Omega_{ijk}
=
D_{ik}-D_{jk}D_{ij}.
$$

Whenever all compositions are bounded on their declared graph domains, the four-index identity is

$$
\Omega_{ikl}-\Omega_{ijl}
+D_{kl}\Omega_{ijk}
-\Omega_{jkl}D_{ij}
=0.
$$

This is the tetrahedral Bianchi identity for presentation defects. The retained-source realization is its zero-defect sector. More general output-only realizations carry \(\Omega_{ijk}\) as bounded face data satisfying the displayed cell identity.

At the response boundary, the degree-one state defect is

$$
d_S(x,y)=y-\mathbb T_Sx.
$$

The pair \((d_S,\Omega)\) separates state-membership failure from presentation-coherence failure: \(d_S\) is transverse to the sewing graph, while \(\Omega\) measures triangular holonomy among output presentations. Prime and seam parameters turn these defect spaces into an object-indexed simplicial bundle. Commuting prime successors give a flat bundle; matrix-valued successors replace flatness by an operator curvature.

Finite cutoffs act levelwise on this nerve. Their projective limit produces a strict simplicial retained-source system together with any admitted bounded output defects. This extends the analytical tetrahedron to an arbitrary finite simplex of boundary-relation, Weyl-family, and colligation presentations.

## Exact remaining Evans membership frontier

The maximal-isotropic response graph admits every source-generated pair

$$
(\mathscr Rg,\mathbb T_S\mathscr Rg).
$$

It does not by itself admit the separately prescribed Evans boundary data \((e_-,e_+)\). Their membership requires the additional identity

$$
e_+=\mathbb T_Se_-.
$$

Recovering \(g_e=R_4e_-\) from the incoming all-seam flux does not prove this identity: the outgoing requirement remains

$$
e_+=\mathscr R(\mathcal Fg_e).
$$

On each prime shell and parameter jet, this is the vanishing of the declared adjoint residual. Equivalently, if \(T_{PB}\) is the constructed pair-to-bordered crossing and an authoritative forward map \(U_{G4}\) is supplied on the same paired carriers, then with

$$
\Delta=U_{G4}-T_{PB}
$$

the exact condition is

$$
\Delta^\top e=0
$$

for every generator \(e\) of the closed Evans cyclic jet subspace. The membership obstruction itself has a complete Hilbert realization. On the response phase space define

$$
d_S:\mathcal H_{resp,S}\oplus\mathcal H_{resp,S}
\longrightarrow\mathcal H_{resp,S},
\qquad
d_S(x,y)=y-\mathbb T_Sx.
$$

This map is bounded and surjective, and

$$
\ker d_S=\Lambda_{\mathbb T_S}.
$$

Hence there is a short exact sequence

$$
0\longrightarrow\Lambda_{\mathbb T_S}
\longrightarrow
\mathcal H_{resp,S}\oplus\mathcal H_{resp,S}
\mathrel{\mathop{\longrightarrow}^{d_S}}
\mathcal H_{resp,S}
\longrightarrow0.
$$

For \(d=d_S(x,y)\), completing the square gives

$$
\lVert x\rVert^2+\lVert y\rVert^2
=
2\left\lVert x+\frac12\mathbb T_S^*d\right\rVert^2
+
\frac12\lVert d\rVert^2.
$$

Therefore

$$
\operatorname{dist}
\bigl((x,y),\Lambda_{\mathbb T_S}\bigr)^2
=
\frac12\lVert y-\mathbb T_Sx\rVert^2.
$$

The orthogonal sewn projection is explicit:

$$
P_{sew}(x,y)
=
\frac12
\bigl(x+\mathbb T_S^*y,\mathbb T_Sx+y\bigr).
$$

Its complementary projection is

$$
P_{def}(x,y)
=
\frac12
\bigl(x-\mathbb T_S^*y,y-\mathbb T_Sx\bigr)
=
\frac12\bigl(-\mathbb T_S^*d_S(x,y),d_S(x,y)\bigr).
$$

Consequently

$$
\mathcal H_{resp,S}\oplus\mathcal H_{resp,S}
=
\Lambda_{\mathbb T_S}
\mathbin{\widehat\oplus}
\{(-\mathbb T_S^*k,k):k\in\mathcal H_{resp,S}\},
$$

where the sum is orthogonal for the positive response Hilbert metric. This complement is distinct from the orthogonal complement for the incoming-minus-outgoing boundary form, under which the sewing graph is maximal isotropic.

The Evans obstruction is thus the explicit defect vector \(d_S(e_-,e_+)\). The current materialized system supplies its carrier, quotient, and norm. Membership of the unchanged Evans state remains the arithmetic frontier.

## Boundary-relation, Weyl-family, and colligation realization

Let \(\nabla_S^{max}\) denote the maximal source-generated logarithmic connection relation on the completed Green graph, and let

$$
\Gamma_Sf=(\Gamma_{S,-}f,\Gamma_{S,+}f)
\in
\mathcal H_{resp,S}\oplus\mathcal H_{resp,S}
$$

be its complete incoming/outgoing response trace. The contour and Green identities take the boundary-relation form

$$
\langle \nabla_S^{max}f,g\rangle
-
\langle f,\nabla_S^{max}g\rangle
=
\langle\Gamma_{S,-}f,\Gamma_{S,-}g\rangle_{resp}
-
\langle\Gamma_{S,+}f,\Gamma_{S,+}g\rangle_{resp}
$$

on the common rapid core and hence on its graph closure. Define the source-generated boundary relation

$$
\mathcal B_S
=
\left\{
\bigl((f,\nabla_S^{max}f),
(\Gamma_{S,-}f,\Gamma_{S,+}f)\bigr)
\right\}.
$$

The Fourier sewing condition selects the extension relation

$$
\mathfrak A_{S,\mathbb T}
=
\ker\bigl(\Gamma_{S,+}-\mathbb T_S\Gamma_{S,-}\bigr).
$$

Its boundary values lie in the maximal-isotropic graph \(\Lambda_{\mathbb T_S}\). On the source-generated relation this is the sewn extension. Promotion to a self-adjoint extension of the full maximal connection is precisely the statement that \(\mathcal B_S\) is a unitary boundary relation for the full adjoint graph.

For a spectral parameter \(z\), let

$$
\mathcal N_S(z)
=
\ker(\nabla_S^{max}-z)
$$

inside the declared defect domain. The source-generated gamma relation and Weyl family are

$$
\gamma_S(z)
=
\left(
\Gamma_{S,-}\big|_{\mathcal N_S(z)}
\right)^{-1},
\qquad
M_S(z)
=
\Gamma_{S,+}\gamma_S(z),
$$

with inverse and product interpreted as linear relations on their natural ranges. The sewn spectral condition becomes

$$
M_S(z)x=\mathbb T_Sx.
$$

Equivalently, define the sewing-normalized Weyl relation

$$
\Theta_S^{W}(z)=\mathbb T_S^*M_S(z).
$$

Then a sewn defect vector satisfies

$$
(I-\Theta_S^{W}(z))x=0.
$$

For a prescribed Evans incoming state \(e_-(z)\), its exact obstruction is

$$
\delta_{Ev,S}(z)
=
\bigl(M_S(z)-\mathbb T_S\bigr)e_-(z).
$$

This places the arithmetic state in the boundary relation, its Weyl family, and the sewn response relation. A genuine unitary-colligation characteristic function has the transfer-function form

$$
\theta(\zeta)
=
H+\zeta G(I-\zeta T)^{-1}F.
$$

Identification of \(\Theta_S^{W}\) with such a characteristic function requires a conservative realization supplying the blocks \(T,F,G,H\). The retained-source tetrahedron supplies the compatible presentation groupoid for the presently constructed relations.

## Conclusion

The constructed analytical realization is layered rather than confined to one carrier.

Its central Hilbert layer is the bounded self-adjoint Riesz operator

$$
\mathbf G_S^{an}\in\mathcal B(\mathscr G_S),
\qquad
\mathscr G_S
=
\overline{\operatorname{ran}(r_S,\beta_S)}.
$$

The bounded observation map \(Z_S\) pulls this operator and its canonical feature to the completed observer source. Source reconstruction then transports the observer operator, inherited feature, and minimal observer feature through all four reversible presentations. The retained joint graph supplies strict chart coherence, chart rotation, radical descent, and terminal scalar observation.

The finite-regulator layer maps to the regular face through exact signed packet compressions and the asymptotically reducing absolute-Gram comparison. The oriented-radial, semilocal Fourier, metaplectic, and comb-orbit realizations occupy their declared Hilbert or distribution/test-dual carriers and are sewn through the common source rather than forced into the augmented Hilbert space.

Moving seams act by unitary metric transport; prime enlargement acts by the flat affine connection law; placewise local-energy rows and endpoint terms assemble the finite-place tower. The separate absolute-connection form domain \(D(\lvert V_S\rvert^{1/2})\cap\mathcal S_S\) supplies the closed Sonin restriction and is not substituted for the bounded augmented carrier.

Accordingly the realized system consists of one source-reached diagram of compatible carriers, operators, features, relations, and readouts. The joint-graph Riesz operator is its central completed Hermitian operator; no unsupported Cartesian-product block or placement of distributional objects in that Hilbert space is asserted.
