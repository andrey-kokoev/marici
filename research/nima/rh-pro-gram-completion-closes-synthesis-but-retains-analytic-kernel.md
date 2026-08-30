# Pro-Gram completion closes synthesis but retains its analytic kernel

## Continuity is built into the topology

Let \(\mathcal M_{\mathrm{src}}\) be the authorized arithmetic constructor
monoid and define seminorms on finite packets by

\[
q_C(v)=\lVert U(Cv)\rVert_H,
\qquad
C\in\mathcal M_{\mathrm{src}}.
\]

The identity constructor belongs to the monoid, so

\[
q_1(v)=\lVert Uv\rVert_H.
\]

Therefore synthesis \(U\) is continuous by construction. Since \(H\) is
complete, it extends uniquely to the completion of the Hausdorff pro-Gram
packet space. The graph of the extended map is closed.

This resolves the graph-closedness gate conditionally on two source facts:

1. the identity synthesis constructor is admitted;
2. the constructor seminorm family is separating, or the packet space is first
   quotiented by its common null space.

No independent analytic closed-range theorem is needed.

The constructor family must be restricted to the declared RH target family.
Before completion, its common null space is quotiented. Otherwise the
pro-Gram construction safely over-retains the arithmetic presentation but
does not produce Aspect's minimal marked germ.

## Closed graph does not mean analytic faithfulness

The extended synthesis may have a nontrivial kernel. A completed arithmetic
state can have zero analytic image while remaining visible to another
constructor seminorm. This is not a defect in the graph architecture. It is
the reason the arithmetic component was retained.

Consequently, three properties must remain distinct:

- continuity of synthesis;
- closedness of its graph;
- injectivity or bounded-below behavior of its analytic projection.

The pro-Gram construction supplies the first and hence the second. It does not
supply the third.

## Trace continuity becomes the live gate

A linear anomaly trace \(\ell\) is continuous in the pro-Gram topology only
if one fixed finite constructor family \(F\) and one constant \(C\) satisfy

\[
|\ell(v)|
\le
C\max_{D\in F}q_D(v).
\]

The identity seminorm alone cannot satisfy this for the Tate traces, as shown
by adjacent-label collapse. An authorized valuation constructor may supply the
missing control. The question is now exactly which finite constructor family
dominates each of the primitive and square traces.

## Minimal model

Take an arithmetic state \((x,y)\). Let analytic synthesis read only \(x\),
while one authorized constructor rotates the hidden arithmetic coordinate into
the analytic port. Then

\[
q_1(x,y)=|x|,
\qquad
q_C(x,y)=|y|.
\]

The combined topology is separating. Synthesis remains noninjective because
\((0,y)\) maps to zero, but the anomaly trace \(\ell(x,y)=y\) is continuous by
the constructor seminorm. This is the exact finite pattern required from the
valuation/Fock port.

## DPC verdict

Once the source-authorized pro-Gram topology includes identity synthesis,
closed extension of the arithmetic-to-analytic map is formal. The frontier
moves to finite-family domination of the two anomaly traces and reciprocal
compatibility of those dominating constructors.

## Verification

`check_rh_pro_gram_synthesis_closure.py` verifies the separating two-seminorm
model, closed synthesis graph, retained analytic kernel, failure of identity
control, and successful anomaly domination by one authorized constructor.
