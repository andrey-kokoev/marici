# Diagonal product-group Clebsch selector: WP736

## Question

Can a single parent gauge representation make the singlet-triplet portal
asymmetry unavoidable, instead of choosing two low-energy Yukawa couplings
independently?

## Parent source grammar

Take

\[
G_P=SU(2)_A\times SU(2)_B\times U(1)_Y
\]

and break the two non-Abelian factors to their diagonal subgroup with a
bifundamental link field. Assign

\[
L\sim(2,1)_{-1/2},\qquad
H\sim(1,2)_{1/2},\qquad
\Psi_R\sim(2,2)_{-1}.
\]

The unique parent contraction is

\[
\kappa_U\bar L_iH_j\epsilon_{jk}\Psi_{R,ik}.
\]

After diagonal breaking, define

\[
X_{ij}=\epsilon_{jk}\Psi_{R,ik}
=\frac{1}{\sqrt2}\psi_A\delta_{ij}
 +\frac{1}{\sqrt2}\psi_B^a\sigma^a_{ij}.
\]

The trace and traceless components are the diagonal-group singlet and triplet.
Using the Hiller-model normalization (t^a=\sigma^a/2), matching gives

\[
\kappa_A=\frac{\kappa_U}{\sqrt2},
\qquad
\kappa_B=\sqrt2\kappa_U,
\qquad
\frac{\alpha_{\kappa_B}}{\alpha_{\kappa_A}}=4.
\]

This ratio is a Clebsch theorem of one parent invariant. It is not an adjustable
relation between two low-energy operators. If the parent flavor Yukawa is also
one coupling, then (y_A=y_B=y_U) at matching. The additive portal contrast is

\[
-4\alpha_{\kappa_A}\alpha_{y_A}
+3\alpha_{\kappa_B}\alpha_{y_B}
=8\alpha_{\kappa_A}\alpha_{y_U}>0.
\]

Thus the parent representation fixes a nonzero ordered sign and a ratio. It
evades WP735 because above the breaking scale there is one beta equation for
(\kappa_U), not two independent low-energy nullcline equations.

## Executable parent check

An official PyR@TE 3 calculation at revision
`04b219c2016f3fc4f2371d72607edc26a7e06364` gives

\[
\frac{\beta_{\kappa_U}}{\kappa_U}
=-\frac{15}{4}g_1^2-\frac92g_A^2-\frac94g_B^2
+2\operatorname{tr}(\kappa_U^\dagger\kappa_U)
+\frac32\kappa_U\kappa_U^\dagger.
\]

For three flavor-diagonal copies, the parent self coefficient is (15/2) in
the amplitude beta function and (15) for the squared coupling. This verifies
that the parent operator is executable as a gauge-invariant renormalizable
Yukawa interaction. It does not establish an interacting fixed point.

## Exact low-energy transport defect

Write the squared low-energy couplings as

\[
a=\alpha_{\kappa_A},\quad b=\alpha_{\kappa_B},\quad
u=\alpha_{y_A},\quad v=\alpha_{y_B}.
\]

On the matching ray (b=4a) and (v=u), the simultaneous one-loop beta
functions of WP735 give

\[
\frac{d}{dt}\log\frac ba=-12g_2,
\qquad
\frac{d}{dt}\log\frac vu=4u-24g_2.
\]

Therefore the parent Clebsch ray is not invariant below diagonal breaking.
The Yukawa cross terms preserve (b/a=4); the unequal diagonal (SU(2)_L)
Casimirs split it. Define the ratio controlling the portal sign,

\[
R=\frac{bv}{au}.
\]

At matching (R=4), while

\[
\left.\frac{d\log R}{dt}\right|_{b=4a,\,v=u}
=4u-36g_2.
\]

The low-energy portal source retains its sign exactly when (R>4/3). Its
initial margin is finite, but survival to a detector scale depends on the
source-fixed breaking scale and the complete RG trajectory. The product-group
Clebsch theorem supplies sign and ratio at matching, not an automatic
threshold theorem.

## Completion gates

The construction is a progressive source principle but not yet the requested
complete explanation.

1. The parent gauge-Yukawa system needs an anomaly-free complete matter packet
   and an isolated interacting fixed point fixing (alpha_{\kappa_U}).
2. Placing (L) and (H) on different gauge sites makes ordinary
   renormalizable Standard Model Yukawas non-invariant above diagonal breaking.
   A link insertion or mediator completion is required; its coefficients may
   reopen a source fiber.
3. The link potential must fix the breaking scale relative to the one admitted
   physical clock.
4. Finite matching and the full low-energy flow must prove (R>4/3) over the
   uncertainty-completed trajectory.
5. Singlet- and triplet-labelled production and decay channels must remain
   distinguishable with an independently authorized calibration locus. A
   shared source-detector drift can defeat even a rank-two formal response.

## Disposition and falsifiers

WP736 identifies the first concrete representation theorem in this branch
that fixes the required portal sign without choosing (kappa_A-kappa_B) by
hand. It is a matching-scale selector and rigidifier, but not yet a numerical
low-energy selector.

The smallest exact RG falsifier is any point with (g_2>0) on the matching
ray: then (d\log(b/a)/dt=-12g_2\ne0). The smallest source-completion
falsifier is the absence of a renormalizable parent Standard Model Yukawa with
(L\sim(2,1)), (H\sim(1,2)), and a site-singlet right-handed fermion.

Reproduce with:
`uv run --with sympy python research/flavor/checkers/wp736_diagonal_product_group_clebsch_selector.py`.

Generated result:
`results/wp736_diagonal_product_group_clebsch_selector.json`.
