# Spin(5) tau actual-pole transfer audit (WP894)

## Question

Does WP893's source-derived radial Higgs portal authorize transport of the
existing 2015 muon--tau grid to the two actual Spin(5) radial poles?

## Exact obstruction

No. The strongest preregistered candidate remains WP256's source-relative
coordinate \(x=m_{\rm vis}/M_{\rm source}\). Its leave-one-out prediction at
140 GeV has exact total-variation residual

\[
\frac{12641608}{354073635}>0.
\]

The first-bin residual alone is \(-3353749/354073635\), so the finite grid
does not define an exact scale-covariant response functor. WP893 supplies no
new detector-response law that could cancel this witness.

## Interface accounting

WP893 genuinely repairs two source-side fields for the Spin(5) radial modes:

1. the two physical pole labels on the frozen slice;
2. physical Higgs-mediated branching semantics under the no-exotic-decay
   assumption.

It does not repair the six detector-side fields needed to transport the 2015
tau response: common tau topology at the actual poles, common detector era and
reconstruction, the unchanged event selection evaluated at those poles, QCD
control, weighted full-sample completion, and correlated uncertainty
transport. Thus the actual-pole tau adapter has capability vector
\((1,1,0,0,0,0,0,0)\) in this eight-field grammar.

## Disposition

The dimuon acquisition morphism remains valid on WP893's explicitly frozen
slice. The tau acquisition object remains valid only on its labelled
130/140/160 GeV pilot domain. Their coexistence does not authorize a tau
actual-pole morphism. This is an interface failure, not absence of tau
detection and not a flavor selector.

The smallest constructive repair is either same-frame, physically normalized
tau samples at both actual poles or an independently derived detector kernel
that predicts the held-out 140 GeV template within a declared correlated
uncertainty set and then survives full weighted, QCD, and nuisance completion.
The kernel must be frozen before inspecting the actual-pole answer.

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp894_spin5_tau_actual_pole_transfer_audit.py
~~~
