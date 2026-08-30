# Charged bipartite orientation is removable chart data

Work package: WP608  
Owner: marici.Figueiredo

## Proposed source grammar

Take two cyclic operator families (A_i,B_i) and three complex mediators
(X_i). Under (Z_2^3\rtimes C_3), assign

\[
q(X_i)=q(A_i)=e_i,
\qquad
q(B_j)=e_{j-1}.
\]

The complete charge-allowed linear incidence is

\[
X_i^\dagger A_i,
\qquad
X_i^\dagger B_{i+1}.
\]

At fixed displayed labels, every (X_i^\dagger B_{i-1}) coupling is
forbidden. With common mass and couplings, Gaussian elimination produces

\[
K=-{g_Ag_B\over M^2}P_+,
\]

where (P_+) is the forward cyclic shift. Its rank is three, so three
mediator modes are necessary and sufficient for this displayed kernel.

## Hostile relabelling

The labels of the two operator families have not yet been physically aligned.
Apply the legal independent chart change

\[
B'=P_+B.
\]

Then (B=P_+^TB'), and the cross interaction becomes

\[
A^T K B=-{g_Ag_B\over M^2}A^TB'.
\]

The apparent orientation has disappeared. In the primed chart the charge rule
simply pairs equal nodes.

There is an equivalent generalized-reflection witness. Let (S) reflect the
(A) labels and act on (B) by

\[
S_B=P_+^TSP_+.
\]

Both (S) and (S_B) are involutions, and

\[
S^TKS_B=K.
\]

Thus the typed incidence retains a reflection once each family is allowed its
own legal label frame. Merely declaring the families inequivalent does not
canonically identify their cyclic origins.

## Classification

The charged construction rigidifies a bipartite presentation. It does not
select a physical orientation on the quotient by independent family
relabelings. The exact hostile is the single relabelling (B'=P_+B), which
turns the allegedly directed kernel into a scalar identity without changing
the source theory.

This is the same structural warning as the nine-link phase result: a sparse
or directed pattern can be invariant under its declared texture group while
failing to descend under the larger physical groupoid.

## What would repair it

A source-derived operation must physically align the (A) and (B) labels
before a forward/reverse comparison is meaningful. Examples could include a
shared calibrated charge tag, a common decay product carrying the node label,
or a dynamical diagonal pairing derived independently of the desired
orientation.

Such an alignment is not free. It creates a relational experiment whose
groupoid is the stabilizer of the added port. It does not reveal an absolute
orientation that existed before the port was supplied.

Only in that new experiment could a family-resolved support test criticize
the incidence by comparing the two ordered branches. Detector leakage,
background and the temporal phase process would still require independent
calibration.

## Remaining source gate

The next architecture must provide, from one source grammar:

- physically instantiated (A_i,B_i) flavor composites;
- a weak-basis-invariant common alignment between their labels;
- an oriented interaction not removable by the stabilizer of that alignment;
- descent of the resulting constraint to a proper `physical16` family;
- an executable aligned-channel experiment with temporal phase control.

WP608 therefore closes the bare charged-incidence proposal negative. It is a
presentation rigidifier, not yet a source selector.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp608_charged_bipartite_mediator_incidence.py

The generated result is
research/flavor/results/wp608_charged_bipartite_mediator_incidence.json.
