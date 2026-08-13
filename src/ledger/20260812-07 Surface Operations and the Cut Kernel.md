# Surface Operations and the Cut Kernel

## Record

Date: 2026-08-12

Status: proposed intrinsic framework, with established bare Cut-Equation input and explicitly marked extensions.

## Question

Does scalar surface theory itself carry normal-grade, jet, pairing, primitive-symmetric, and sewing operations from which NLSM, Yang–Mills, and gravity follow functorially?

## Verdict

Not in the bare surface-function algebra. There is a coherent minimal candidate after adjoining logarithmic deformation data, state duality, an intersection module, and primitive cut-kernel boundary data.

The decisive obstruction is

\[
\boxed{\text{Cut is not conservative: it annihilates local/contact data.}}
\]

Consequently, cut compatibility is necessary but cannot establish equality or naturality of two surface theories without separate control of their cut-free primitives.

## Bare surface object

For an oriented marked surface \(\Sigma\), let \(\mathcal A_\Sigma\) denote its surface-function algebra. Propagator variables \(x_C\) and numerator variables \(Y_C\) are kept independent until kinematic specialization.

For every admissible curve \(C\),

\[
\Delta_C
=
\iota_C^*\frac{\partial}{\partial x_C}:
\mathcal A_\Sigma\longrightarrow\mathcal A_{\Sigma\setminus C}.
\]

If \(C\) separates the surface, disjoint union gives

\[
\mathcal A_{\Sigma\setminus C}
\simeq
\mathcal A_{\Sigma_L}\otimes\mathcal A_{\Sigma_R}.
\]

The established bare layer consists of mapping-class covariance, disjoint union, cuts, and boundary/contact functions. It does not itself contain a rank-deformation base, fusion divisors, gauge-state fibers, or a perfect all-surface intersection form.

## The cut kernel and the correct sewing relation

Define the simultaneous cut kernel

\[
\mathcal K_\Sigma=\bigcap_C\ker\Delta_C.
\]

For polynomial surface functions this contains the propagator-free contact sector. On punctured surfaces it can also contain topology-local terms.

For a chosen cut, an antiderivative or sewing primitive \(S_C\) obeys

\[
\Delta_CS_C=\mathrm{id},
\qquad
S_C\Delta_C=\mathrm{id}-e_C,
\]

where \(e_C(F)=F|_{x_C=0}\). The kernel relevant to one chosen cut is larger than \(\mathcal K_\Sigma\); the latter is the ambiguity left after imposing all cuts.

Cut-invisible and scaleless are different notions. A scaleless term may have nonzero cuts, while a contact constant can be both scaleless and cut-invisible. Any quotient by integration-null functions must therefore use a hereditary ideal stable under cuts and sewings.

## Associated grade at a rank jump

Let \(Z_\Sigma\subset B_\Sigma\) be a rank-jump boundary with ideal \(I_\Sigma\). Its associated grade is

\[
\operatorname{gr}_{Z_\Sigma}\mathcal A_\Sigma
=
\bigoplus_r
I_\Sigma^r\mathcal A_\Sigma/
I_\Sigma^{r+1}\mathcal A_\Sigma.
\]

For degenerations at infinity or functions with poles, this is replaced by a Laurent/Rees lattice. A leading coefficient is intrinsic as a normal-cone-valued object; a scalar coefficient requires a trivialization of the normal line.

If a cut is filtered of degree \(-w_C\), then for a separating cut

\[
\Delta_C(\operatorname{gr}^{r}F_\Sigma)
=
\sum_{a+b+c=r-w_C}
\operatorname{gr}^{a}F_L
\otimes
\operatorname{gr}^{c}\eta_C
\otimes
\operatorname{gr}^{b}F_R ,
\]

where \(\eta_C\) is the internal sewing kernel and is \(1\) in the un-enriched scalar theory.

Thus the literal same-degree relation

\[
\operatorname{Cut}\circ\operatorname{gr}^{r}
=
(\operatorname{gr}^{r}\otimes\operatorname{gr}^{r})
\circ\operatorname{Cut}
\]

is false. The correct relation is graded convolution. Lowest nonzero initial forms multiply when valuations add and the leading internal contraction does not cancel.

If the cut boundary and rank degeneration are not Tor-independent, ordinary associated grade does not commute with base change. The corrected functor belongs in a derived Rees category.

## First jets and their algebra

For a fusion divisor \(D\) with ideal \(J_D\), the intrinsic first neighborhood is

\[
J_D^1\mathcal A_\Sigma
=
\mathcal A_\Sigma\otimes_{\mathcal O_B}\mathcal O_B/J_D^2.
\]

The exact sequence

\[
0\longrightarrow J_D/J_D^2
\longrightarrow\mathcal O_{D^{(1)}}
\longrightarrow\mathcal O_D
\longrightarrow0
\]

has no canonical splitting in general. Therefore the full first jet is intrinsic, while a separate normal derivative of an arbitrary function is not. A reduced coefficient becomes intrinsic after prescribing a vanishing order, choosing a normal retraction, retaining its conormal-line value, or realizing it as the residue of a canonical double-pole form.

For divided Hasse–Schmidt jets,

\[
\mathsf J_t(FG)=\mathsf J_t(F)\mathsf J_t(G).
\]

At first order, including a sewing kernel,

\[
\Delta_Cj^{[1]}F_\Sigma
=
j^{[1]}F_L\,\eta_0F_R
+
F_L\,j^{[1]}\eta_C\,F_R
+
F_L\eta_0\,j^{[1]}F_R.
\]

Accordingly,

\[
\operatorname{Cut}\circ J^1
\neq
(J^1\otimes J^1)\circ\operatorname{Cut}
\]

unless the right side is pulled back to the diagonal and truncated to total order one. Without truncation it contains a second-order cross term.

## Pairing layer

Two independent pairings are needed:

\[
I_\Sigma:
\mathcal H_\Sigma\otimes\mathcal H_{\bar\Sigma}\to\mathbf1
\]

on ordering chambers or twisted cycles, and

\[
g:E\otimes E\to\mathbf1
\]

on the local physical jet-state fiber.

The global scalar pairing supplies KLT data. The local metric supplies state evaluation, trace removal, and internal state sums. Conflating them obscures which loop-level structure is missing.

Cyclicity requires

\[
I_\Sigma(S_Cu,v)
=
I_{\Sigma\setminus C}(u,\Delta_Cv).
\]

The pairing descends through associated grade only when it respects the filtration. Its inverse descends only if the leading graded pairing remains perfect:

\[
\operatorname{gr}(I^{-1})
=
(\operatorname{gr}I)^{-1}
\]

is not automatic at a rank jump.

For a deforming pairing,

\[
j^1I(u,v)
=
I_0(j^1u,v_0)
+
I_0(u_0,j^1v)
+
I_1(u_0,v_0).
\]

The last term vanishes only when the pairing is flat along the fusion divisor.

## Proposed theory-operation algebra

The minimal structure is a colored logarithmic cyclic modular PROP:

\[
\mathsf{ThOp}_{\mathrm{surf}}
=
\operatorname{Kar}\!\left(
\mathsf{Surf}^{\log}_{\mathrm{cut/sew}}
\ltimes\mathsf{Rees}_Z
\ltimes\mathsf{HSJet}_D
\ltimes(\mathsf{GaugeState},g)
\ltimes(\mathsf{TwCycle},I)
\right)
/\mathcal N^{\mathrm{her}}.
\]

It contains:

1. mapping-class actions and disjoint union;
2. compatible cuts and sewings;
3. Rees grades with convolution;
4. Hasse–Schmidt multi-jets with Leibniz relations;
5. evaluation and coevaluation for local and global pairings;
6. Karoubi images of self-adjoint state projectors;
7. curved primitives \(\omega_\Sigma\in\mathcal K_\Sigma\);
8. a hereditary null ideal \(\mathcal N^{\mathrm{her}}\), when integrated equivalence is desired.

## Epistemic perimeter

Established:

- surface functions and the Cut Equation on arbitrary marked surfaces;
- independent propagator and numerator variables;
- the tree-level twisted-cycle interpretation of the scalar matrix;
- scalar scaffolding residues and their tree-level cut behavior.

Strong structural inference:

- Rees grade and multi-normal residue extend to a common logarithmic modular PROP;
- derived Rees and derived jet functors repair nontransverse base-change failures.

Open:

- construction of the deformation bases and normal bundles on every surface;
- proof that all required pairings are strict and perfect under degeneration;
- a complete loop-level off-diagonal intersection matrix and coevaluation;
- classification of primitive cut-kernel data.

Do not claim:

- that cuts uniquely reconstruct a surface theory;
- that all scaleless functions lie in the cut kernel;
- that a normal derivative of an arbitrary surface function is coordinate-free;
- that the loop inverse-KLT scalar function is already a complete pairing matrix.

## Sources

- [The Cut Equation](https://arxiv.org/html/2412.21027v2)
- [Scalar-Scaffolded Gluons and the Combinatorial Origins of Yang-Mills Theory](https://arxiv.org/html/2401.00041v3)
- [Combinatorics and Topology of Kawai-Lewellen-Tye Relations](https://arxiv.org/abs/1706.08527)
- [A Surface Integrand for the Inverse KLT Kernel](https://arxiv.org/pdf/2602.15102)
