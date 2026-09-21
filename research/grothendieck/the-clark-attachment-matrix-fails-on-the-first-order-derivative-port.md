# The Clark attachment matrix fails on the first-order derivative port

## Result of the requested calculation

The available first-order translation chart and the endpoint-moment transpose columns do not define the proposed matrix

(S_Cl O_01-W_Cl^times) P_loc^-1 W_Cl

on the declared common test space. A derivative source column produces a delta distribution after applying the resolvent. The output trace cannot act on that response. Gaussian regularization gives an explicit inverse-width divergence in the Clark-visible history/moment defect.

This evaluates the first concrete source constructor at which the naive assembly fails. It does not decide the matrix for a separately constructed higher-order paired arithmetic pencil; that pencil would have to supply its own inverse-domain theorem.

## 1. Distinct four-port records

The source packets distinguish

Gamma_mom=(g(0), integral g, g'(0), integral xg),

Gamma_hist=(g(0), integral g, integral_negative g, PV integral g/x).

Their common six-channel rigging is X_(r,m)=H^r intersect L2((1+x^2)^m), with r,m>3/2. The moment transpose has columns delta_0,1,-delta_0',x. They belong to X_(r,m)' and the trace row is bounded on X_(r,m).

These two continuity facts do not imply that a first-order resolvent sends those columns from the dual space back to the test space. That mapping property is what the proposed composition needs.

After the recorded Fourier-frame comparison, the surviving Clark-visible defect is the row (-i D1,-i D1), where

D1(g)=integral_negative g-(1/2)integral g-g'(0).

Its distributional primitive is K1=-|x|/2+delta_0. Exactness in the distributional complex does not define evaluation of D1 on another singular distribution.

## 2. Actual resolvent on the derivative constructor

Write D=partial_x and choose Re z>0. Its full-line inverse is

(R_z f)(x)=-integral_0^infinity exp(-zt)f(x+t)dt.

The inverse acts on the delta column by

R_z delta_0=-exp(zx)1_(x<0).

Since R_z commutes with differentiation,

R_z(-delta_0')=z exp(zx)1_(x<0)-delta_0.

This response is a distribution with a nonzero delta component. In particular it does not belong to H^r for r>3/2. The first-order translation operator therefore cannot instantiate the assumed bounded map P_loc^-1:X'->X on the declared four-port incidence.

The constant and linear source columns introduce additional global moment-domain issues. The derivative column already suffices to reject the full four-column lift into this test space.

## 3. Regularized defect calculation

Let rho_epsilon(x)=exp(-x^2/epsilon^2)/(sqrt(pi)epsilon), and replace -delta_0' by -rho_epsilon'. Then

g_epsilon=R_z(-rho_epsilon')=-z R_z rho_epsilon-rho_epsilon

is smooth and rapidly decreasing for real z>0. Put R0=(R_z rho_epsilon)(0). Direct integration gives

R0=-(1/2) exp(z^2 epsilon^2/4) erfc(z epsilon/2).

The source traces are

integral g_epsilon=0,

integral_negative g_epsilon=-R0,

g_epsilon'(0)=-z^2 R0-z/(sqrt(pi)epsilon).

Consequently

D1(g_epsilon)=(z^2-1)R0+z/(sqrt(pi)epsilon).

At z=1 this reduces exactly to

D1(g_epsilon)=1/(sqrt(pi)epsilon).

Thus the defect evaluated on this source column has no finite Gaussian-regularization limit. The recorded output projection (-i D1,-i D1) preserves this divergence.

This is a column-level output test. It is not a claim that every possible input-side Clark linear combination has the same leading divergence. A cancellation or renormalized composite would require its own specified domain and prescription; the declared four-column resolvent map itself has already failed.

## 4. What the prior proofs actually supply

The core identity W_Gamma^times=Gamma_mom is exact on Schwartz tests. The six-channel continuity theorem admits its columns as distributions. The primitive identity partial K1=D1 holds in that same distributional setting. None of these establishes the composition of the trace row with the first-order resolvent of its singular transpose column.

The independently sourced one-sided moment transfers use smooth forcing Phi and u Phi with an endpoint observation. Those cross-entry formulas are well-defined on their admitted charts. Replacing their forcing columns by the four moment-transpose distributions changes the source operation. Their common port count does not authorize that replacement.

## 5. Consequence for the main programme

The generic solution-cone contraction remains valid when P:X->Y is invertible on a domain carrying all source columns and output rows. This attempted arithmetic instantiation fails that hypothesis for the first-order moment-transpose assembly.

The surviving source-specific task is to construct the shared attachment using the actual smooth forcing/endpoint cross ports, or to prove that the intended independently defined paired pencil resolves the singular columns on its own graph domain. Either route must specify the action on -delta_0' and demonstrate that the resulting output traces exist. Scalar Clark identities and a formal distributional primitive leave that calculation open.

This finding narrows the problem to an explicit constructor-domain mismatch. It supplies no new closure axiom, physical calibration requirement, or confinement conclusion.

## Verification and provenance

`uv run --with mpmath python research/grothendieck/checkers/check_clark_resolvent_trace_obstruction.py` passes at 70 decimal digits. It checks the Gaussian resolvent formula and the exact predicted trace defect for z=1,2 and three widths. The distributional formulas and divergence are derived above.

Sources inspected:
- `research/nima/the-Schwartz-four-trace-port-canonically-supplies-the-core-Clark-colocation-map.md`
- `research/nima/correction-the-moment-four-port-and-history-four-port-require-a-six-channel-common-refinement-at-the-fixed-seam.md`
- `research/nima/the-surviving-Clark-defect-is-an-exact-distributional-boundary-with-a-canonical-even-primitive.md`
- `research/nima/the-six-channel-trace-and-Clark-port-columns-are-continuous-on-one-weighted-Sobolev-rigging.md`
- `research/voevodsky/the-completed-clark-pair-is-a-fixed-codiagonal-sewing-of-four-oriented-resolvent-cross-entries.md`
