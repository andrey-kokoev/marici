# Prior research: canonical response split and remaining crossing

Date: 2026-09-08

## Architectural split is available

Prior finite synthesis research gives a non-fitted split of the fixed combined diagonal response.  On the finite labelled shell-pair carrier,

\[
U_X^{\rm rad}:V_X^{\rm shell}\to H_X^{\rm rad}
\]

is the forward radial synthesis.  Its canonical reciprocal return is

\[
N_X^{\rm rad}=(U_X^{\rm rad})^*
\]

in the Hermitian lane, or `(U_X^rad)^top` in the analytic-transpose Evans lane.  The Wronskian term is not an arbitrary share of that return; it is the fixed skew incidence `-1/2 w` inside the radial first-order equation

\[
D_t\rho=e-\frac12w.
\]

The endpoint border retains `rho(0)` and the additional `2E` term.  This produces the minimal bordered block

\[
\mathbb T_X(z)=
\begin{pmatrix}
D_t-z&U_X^{\rm rad}\\
N_X^{\rm rad}&B_X(z)
\end{pmatrix}.
\]

Thus the mechanism-level division is source-canonical:

- reciprocal port: adjoint/transpose radial return;
- linking port: Wronskian skew incidence;
- border: initial value and moving endpoints.

## Pure reflection is insufficient

The reflected Evans overlap satisfies

\[
I_{a,b}^{(\rm refl)}(z)=-I_{a,b}^{(0)}(-z)
\]

and has late-shell order `Phi(a)^2/Lambda(a)^2`, whereas the required diagonal response has order `Phi(a)^2/Lambda(a)`.  Unit reflection is therefore one inverse decay rate too small.  A constitutive endpoint component is necessary.

## Euler target and missing crossing

The completed-theta diagonal expansion has algebraic orders

\[
p^{-2},p^{-4},p^{-6},\ldots,
\]

so reciprocal-balanced total grades must be divisible by four.  Adams grade two supplies the first Euler cyclic-square target with weight `p^-2/4`, but equal asymptotic order does not identify the completed-theta pair shell with that Euler current.

The remaining typed chain is

\[
\mathcal C_\theta\otimes\overline{\mathcal C_\theta}
\xrightarrow{\operatorname{Loc}_p}
\mathcal G_{\theta,\rm pair}^{[p,p^+]}
\xrightarrow{T_{\theta\to\rm cyc2,p}}
\operatorname{ran}(S_2\otimes S_2)
\xrightarrow{T_{\rm end}}
\mathcal G_{\rm recip/link,p}.
\]

`Loc_p` is explicit.  The additive-to-multiplicative comparison `T_{theta to cyc2,p}` and its endpoint normalization remain unconstructed.  Matching the leading `p^-2` coefficient cannot define them because distinct finite-shell kernels share that order.

## Disposition

Prior research supplies the canonical finite reciprocal/linking split, so arbitrary allocation of `R+2E` is unnecessary.  The live obstruction is the comparison from the completed-theta ordered-pair shell to the Euler cyclic-square carrier and then to the bordered radial block.  It must preserve the full shell kernel, ratio orientation, parameter jets, and the divisible-by-four grade rule.

## Evidence

- `research/nima/transfer-audit-the-finite-synthesis-adjoint-pair-canonically-splits-radial-propagation-from-wronskian-linking.md`
- `research/nima/pure-reciprocal-reflection-of-the-evans-history-has-ordinary-overlap-scale-and-cannot-carry-the-dominant-diagonal-shell-response.md`
- `research/nima/the-completed-theta-diagonal-shell-expansion-selects-reciprocal-balanced-total-grades-divisible-by-four.md`
- `research/nima/correction-adams-two-is-only-an-order-matched-euler-target-until-the-completed-theta-pair-shell-maps-to-the-cyclic-square-carrier.md`
