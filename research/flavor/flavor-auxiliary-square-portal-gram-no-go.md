# Auxiliary-square portal Gram no-go: WP718

## Question

Can a real-triplet tensor or F-term constraint force the asymmetric portal on
the admitted domain without merely moving the tunable coefficients into an
auxiliary-field coupling matrix?

## Complete linear auxiliary grammar

Let each real triplet auxiliary channel be

\[
F_{\alpha i}=\chi
\left(C_{\alpha n}n_i+C_{\alpha m}m_i\right).
\]

With a common positive normalization, eliminating the auxiliaries gives

\[
V_F=\kappa\sum_{\alpha,i}F_{\alpha i}^2
=\chi^2
\begin{pmatrix}n&m\end{pmatrix}
K
\begin{pmatrix}n\\m\end{pmatrix},
\qquad
K=\kappa C^TC.
\]

Thus

\[
g_n=\kappa\lVert C_n\rVert^2,
\qquad
g_m=\kappa\lVert C_m\rVert^2,
\qquad
h_{nm}=2\kappa C_n\mathbin\cdot C_m.
\]

The auxiliary construction is a positive Gram carrier. Independent triplet
flips require \(C_n\mathbin\cdot C_m=0\); otherwise the same square generates
the forbidden mixed term \(\chi^2 n\mathbin\cdot m\).

## Symmetry and asymmetry

If the two columns are related by source exchange symmetry, their norms agree
and

\[
g_n-g_m=0.
\]

An unequal fixed Clebsch packet can force a ratio. For example,
\(C=\operatorname{diag}(2,1)\) gives \(g_n:g_m=4:1\). But this is explanatory
only if a declared representation theorem fixes that matrix independently of
the desired portal.

Even then, the common rescaling \(C\mapsto sC\) preserves the incidence,
orthogonality, and representation pattern while sending

\[
K\longmapsto s^2K.
\]

Equivalently, the common auxiliary normalization \(\kappa\) remains a free
continuous source parameter. The portal magnitude is not selected.

## Angular and completion gates

This auxiliary square contains no \((n\mathbin\cdot m)^2\) term. A separate
scalar auxiliary constraint can generate that angular stiffness, but using an
independent coefficient would again split selector from rigidifier. A complete
source must tie the portal Gram and angular constraint to the same normalized
algebra.

The strongest surviving possibility is therefore not a generic F-term. It is
a representation-fixed gauge–Yukawa construction in which:

1. inequivalent representations force unequal Clebsch norms and their sign;
2. a gauge or extended-symmetry identity fixes the common coupling;
3. the same multiplet algebra generates the angular constraint;
4. the completed beta system has an attractive physical ray;
5. a specified nondecoupling threshold transports the relation; and
6. representation-labelled mediator channels provide the calibrated readout.

## Claim boundary and disposition

WP718 proves that generic real auxiliary squares do not answer the source
question. They encode the portal in the Gram matrix \(C^TC\). They become a
genuine rigidifier only after an independent representation theorem fixes
\(C\), and they remain nonselective until a source identity fixes the overall
normalization. The smallest falsifier is the harmless-looking rescaling
\(C\mapsto sC\).

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp718_auxiliary_square_portal_gram_no_go.py`

Generated result: `results/wp718_auxiliary_square_portal_gram_no_go.json`.
