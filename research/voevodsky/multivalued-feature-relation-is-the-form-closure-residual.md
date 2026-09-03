# Multivalued feature relation is the form-closure residual

## Question

What object contains every nonclosability witness of the endpoint-corrected source kernel at once, rather than testing null sequences individually?

## Claim boundary

After a uniform lower shift makes the kernel positive, its feature relation has a canonical multivalued subspace. The form is closable exactly when this subspace is zero. Projecting it out gives the maximal regular part, but that projection changes the source form and is admissible only when source data authorize the removed singular component.

## Positive feature relation

Assume a constant \(C\) has been proved such that

\[
K_C(a,b)
=
K_{R,h}(a,b)+CG(a,b)
\]

is positive definite on every finite Gaussian packet. Let \(\mathcal E_C\) be its reproducing-kernel Hilbert space, with feature vectors \(k_a\) satisfying

\[
\langle k_a,k_b\rangle_{\mathcal E_C}
=
K_C(a,b).
\]

Define the algebraic feature operator

\[
T_0:
\operatorname{span}\{g_a\}
\longrightarrow
\mathcal E_C,
\qquad
T_0\left(\sum_j c_jg_{a_j}\right)
=
\sum_jc_jk_{a_j}.
\]

Then

\[
q_{R,h}(f)+C\lVert f\rVert_{\rm ord}^2
=
\lVert T_0f\rVert_{\mathcal E_C}^2.
\]

## Residual subspace

Take the closure of the graph of \(T_0\) as a linear relation. Its multivalued part is

\[
\mathcal M
=
\{y\in\mathcal E_C:
(0,y)\in\overline{\operatorname{graph}(T_0)}\}.
\]

Equivalently, \(y\in\mathcal M\) when there is a sequence \(f_n\) with

\[
f_n\longrightarrow0
\]

in the order norm and

\[
T_0f_n\longrightarrow y
\]

in feature norm.

Therefore

\[
q_{R,h}+C\lVert\cdot\rVert^2
\]

is closable exactly when

\[
\mathcal M=0.
\]

The entire family of base-null/form-Cauchy residuals is represented by this one closed subspace.

## Canonical regular part

Let \(P_{\mathcal M}\) be the orthogonal projection onto \(\mathcal M\). Then

\[
T_{\rm reg}
=
(1-P_{\mathcal M})T_0
\]

has zero multivalued part and determines the regular closable portion of the form. The complementary feature

\[
P_{\mathcal M}T_0
\]

is the singular form residue.

For the endpoint rank-one defect, \(\mathcal M\) is exactly the endpoint feature line, and source endpoint subtraction removes that line with the uniquely forced coefficient.

## Authority boundary

For the corrected remainder, projecting away \(\mathcal M\) merely to obtain closability would alter the completed source quadratic form. It is not authorized unless the singular feature is independently identified with a source term that must be subtracted. Otherwise a nonzero \(\mathcal M\) is an obstruction, not a repair instruction.

## Next executable test

Once a uniform lower shift \(C\) is available, construct finite feature maps from \(K_C\) and search for sequences with vanishing \(G\)-norm but convergent feature vectors. Their limiting span approximates \(\mathcal M\). A proved nonzero limit reports nonclosability; proof that every such limit is zero establishes closability.

## Disposition

The remaining closure residual now has a canonical typed object: the multivalued feature subspace \(\mathcal M\). Its value for the endpoint-corrected remainder kernel is unknown because uniform semiboundedness has not yet been established. No source modification or RH implication is asserted.
