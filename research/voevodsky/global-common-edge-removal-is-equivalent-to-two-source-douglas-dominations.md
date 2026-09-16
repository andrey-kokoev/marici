# Global common-edge removal is equivalent to two source Douglas dominations

## Objective

Turn the open packet-independent common-subfeature problem into an exact pair of source-form inequalities, without taking packetwise Jordan decompositions.

Let

\[
X_\alpha^T:\mathcal C\to\mathcal H_\alpha^T,
\qquad
X_\alpha^0:\mathcal C\to\mathcal H_\alpha^0
\]

be the globally aligned positive regulator features on a common dense source core. Write

\[
G_\alpha^T=(X_\alpha^T)^*X_\alpha^T,
\qquad
G_\alpha^0=(X_\alpha^0)^*X_\alpha^0,
\]

and assume the exact alignment

\[
D_\alpha=G_\alpha^T-G_\alpha^0.
\]

Assume first that \(D_\alpha\) is a bounded self-adjoint operator on the chosen phase-energy completion. Define its global spectral parts

\[
D_{\alpha,+}=\frac{|D_\alpha|+D_\alpha}{2},
\qquad
D_{\alpha,-}=\frac{|D_\alpha|-D_\alpha}{2}.
\]

These are taken before every observer-packet compression.

## Canonical candidate

Any exact common edge leaving the canonical Jordan residuals is forced at source-Gram level. Indeed, if

\[
G_\alpha^T=C_\alpha+D_{\alpha,+},
\qquad
G_\alpha^0=C_\alpha+D_{\alpha,-},
\]

then necessarily

\[
\boxed{
C_\alpha
=G_\alpha^T-D_{\alpha,+}
=G_\alpha^0-D_{\alpha,-}.
}
\]

The equality of the two expressions follows from

\[
D_{\alpha,+}-D_{\alpha,-}=D_\alpha
=G_\alpha^T-G_\alpha^0.
\]

Thus there is no choice of a source Gram once the aligned regulators and global Jordan target have been fixed.

## Exact existence criterion

The canonical common edge exists as a positive source form if and only if

\[
\boxed{
D_{\alpha,+}\preceq G_\alpha^T,
\qquad
D_{\alpha,-}\preceq G_\alpha^0.
}
\]

Either inequality implies positivity of the same \(C_\alpha\); because the two differences coincide, the pair is redundant algebraically but both orientations are useful analytically.

Equivalently,

\[
\boxed{C_\alpha\succeq0.}
\]

This criterion is global and packet-natural. It does not assert the generally false identity

\[
|P_ED_\alpha P_E|=P_E|D_\alpha|P_E.
\]

## Physical common subfeature by Douglas factorization

Suppose the two dominations hold. Douglas factorization gives contractions

\[
A_{\alpha,+}:
\overline{\operatorname{ran}X_\alpha^T}
\to
\overline{\operatorname{ran}D_{\alpha,+}^{1/2}},
\]

\[
A_{\alpha,-}:
\overline{\operatorname{ran}X_\alpha^0}
\to
\overline{\operatorname{ran}D_{\alpha,-}^{1/2}}
\]

such that

\[
D_{\alpha,+}^{1/2}=A_{\alpha,+}X_\alpha^T,
\qquad
D_{\alpha,-}^{1/2}=A_{\alpha,-}X_\alpha^0.
\]

Define the defect features

\[
Y_\alpha^T
=(I-A_{\alpha,+}^*A_{\alpha,+})^{1/2}X_\alpha^T,
\]

\[
Y_\alpha^0
=(I-A_{\alpha,-}^*A_{\alpha,-})^{1/2}X_\alpha^0.
\]

Their source Grams are

\[
(Y_\alpha^T)^*Y_\alpha^T
=G_\alpha^T-D_{\alpha,+}=C_\alpha,
\]

\[
(Y_\alpha^0)^*Y_\alpha^0
=G_\alpha^0-D_{\alpha,-}=C_\alpha.
\]

Hence the two defect features have identical Gram kernels. The source-labelled rule

\[
U_\alpha Y_\alpha^T u=Y_\alpha^0u
\]

is therefore well-defined and isometric on their generated ranges. After this canonical isometric identification, they are one physical common subfeature.

This constructs the common edge from the original aligned physical legs; it is not merely a matrix square root on each finite packet.

## Residual feature

Removing the common defect feature leaves

\[
F_\alpha u
=
\left(
D_{\alpha,+}^{1/2}u,
D_{\alpha,-}^{1/2}u
\right).
\]

Its ordinary and signed Grams are exactly

\[
\boxed{F_\alpha^*F_\alpha=|D_\alpha|,}
\]

\[
\boxed{F_\alpha^*JF_\alpha=D_\alpha,}
\qquad
J=\operatorname{diag}(I,-I).
\]

Therefore, once the two Douglas dominations are established globally, packet-independent common-edge removal and the absolute residual are exact at every finite regulator.

## Form-domain version

If the regulator Grams or \(D_\alpha\) are unbounded, replace operator inequalities by closed-form domination on the common core:

\[
q_{D_{\alpha,+}}[u]
\le q_{G_\alpha^T}[u],
\qquad
q_{D_{\alpha,-}}[u]
\le q_{G_\alpha^0}[u].
\]

The form version of Douglas factorization then produces contractions between the corresponding energy completions. Closability and equality of the two defect forms must be checked before completion.

## Packet consequences

For every finite packet projection \(P_E\), global domination implies

\[
P_ED_{\alpha,+}P_E
\preceq
P_EG_\alpha^TP_E,
\]

\[
P_ED_{\alpha,-}P_E
\preceq
P_EG_\alpha^0P_E.
\]

The resulting compressed residual is

\[
P_E|D_\alpha|P_E,
\]

not \(|P_ED_\alpha P_E|\). Along the spectrally adapted packet filtration, their difference tends to zero by asymptotic reduction. This reconciles the global construction with the previous finite-packet theorem.

## Sufficient quantitative form

A useful regulator-tail target is the existence of \(\varepsilon_\alpha\downarrow0\) and a positive common edge scale \(B_\alpha\) such that

\[
G_\alpha^T
=B_\alpha+E_\alpha^T,
\qquad
G_\alpha^0
=B_\alpha+E_\alpha^0,
\]

with

\[
\|E_\alpha^T-D_{\alpha,+}\|_{B_\alpha}
+
\|E_\alpha^0-D_{\alpha,-}\|_{B_\alpha}
\le\varepsilon_\alpha,
\]

and a lower margin on the relevant energy core. Here the relative norm means the norm after conjugation by \((I+B_\alpha)^{-1/2}\). Such a bound implies the Douglas inequalities after an arbitrarily small common-edge adjustment and controls leakage uniformly in the graph norm.

## What remains analytic

Exact positive alignment already supplies \(G_\alpha^T-G_\alpha^0=D_\alpha\). It does not imply either Douglas domination. The first genuinely global estimate is now precisely

\[
\boxed{
(D_\alpha)_+
\preceq G_\alpha^T
\quad\text{or equivalently}\quad
(D_\alpha)_-
\preceq G_\alpha^0.
}
\]

At finite packet rank, large Widom-edge coercivity proves this eventually. Globally, near-null prolate modes prevent that argument from being uniform. The required source input is therefore a relative edge domination on the phase-energy graph norm, not a uniform positive scalar lower bound.

After domination, Mosco convergence reduces to:

1. \(D_\alpha\to\mathcal A_S\) in strong resolvent/form sense;
2. \(|D_\alpha|\to|\mathcal A_S|\) on the adapted graph core;
3. uniform tail control for the spectrally adapted observer filtration;
4. separate stability of the signed-null Sonin summand.

## Disposition

The open global common-subfeature problem is equivalent to a concrete pair of Douglas inequalities:

\[
\boxed{
D_{\alpha,+}\preceq G_\alpha^T,
\qquad
D_{\alpha,-}\preceq G_\alpha^0.
}
\]

When they hold, the physical common edge, its canonical isometric identification, and the residual absolute Gram \(|D_\alpha|\) are all constructed globally before observer compression. The next analytic task is to prove this domination in the phase-energy graph norm for the transported eight-leg regulators.
