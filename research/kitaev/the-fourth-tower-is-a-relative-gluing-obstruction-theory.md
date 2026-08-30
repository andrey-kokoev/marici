# The fourth tower is a relative gluing obstruction theory

## Aim

Make precise the claim that an RH-bearing failure can be visible only when a point is placed in its complete source, symmetry, cutoff, and readout context.

This is an abstract compiler theorem. It does not assert that the theta/Tate data satisfy its hypotheses.

## Context category

Let a context be a tuple

\[
i=(U,S,\sigma,F,M),
\]

where \(U\) is a parameter neighborhood, \(S\) is a finite Euler cutoff, \(\sigma\) is a sheet, \(F\) is a source/readout frame, and \(M\) declares the retained memory locus.

An admissible refinement or transport \(i\to j\) carries a typed state module \(H_i\) to \(H_j\) by

\[
T_{ji}:H_i\longrightarrow H_j.
\]

Each context also has a constructor algebra \(A_i\), a scalar readout \(L_i\), and a reference family \(R_i\).

## Layer zero: scalar gluing

The weakest square is

\[
L_jT_{ji}=L_i.
\]

It says only that transported states have the same reported scalar. A nontrivial operator

\[
G_i\in\ker L_i
\]

can remain completely invisible.

Falsifier: two transports have identical completed scalar sections but different actions on a constructor probe.

## Layer one: constructor-natural gluing

For every authorized constructor \(a\in A_i\), require an induced constructor \(\alpha_{ji}(a)\in A_j\) and

\[
T_{ji}a=\alpha_{ji}(a)T_{ji}.
\]

This is stronger than scalar covariance. It prevents transport from silently changing the operations available on the state.

Falsifier: scalar covariance holds while a primitive, square, seam, phase, or ordered-product constructor acquires a residual.

## Layer two: path and loop coherence

For a triangle \(i\to j\to k\), compare direct and composite transports:

\[
\Omega_{kji}=T_{ki}^{-1}T_{kj}T_{ji}.
\]

When the maps are only partially invertible, the same comparison is restricted to their common supported module.

Scalar gluing sees no defect whenever

\[
L_i\Omega_{kji}=L_i.
\]

Constructor gluing is nevertheless violated if \(\Omega_{kji}\) acts nontrivially on an authorized constructor orbit. The invisible holonomy group is therefore

\[
\mathcal G_i=\{g\in\operatorname{Aut}(H_i):L_ig=L_i\}.
\]

The fourth tower asks whether the resulting cocycle is trivial in the smaller subgroup that preserves the complete authorized constructor and reference packet.

Falsifier: a loop returns every reported scalar but rotates an unmeasured phase or process direction.

## Layer three: reference-span coverage

A stable reference does not trivialize holonomy unless its authorized constructor orbit spans the science probe module \(P_i\):

\[
\operatorname{span}(A_iR_i)=P_i.
\]

Quantitatively, if \(C_i\) is the calibration analysis map on \(P_i\), closure-stable coverage requires

\[
\inf_i s_{\min}(C_i)>0.
\]

A single invariant reference can miss gain or phase drift on its orthogonal complement.

Falsifier: a stable reference scalar remains fixed while an orthogonal science quadrature undergoes undetected gain or phase holonomy.

## Layer four: completion coherence

Every finite transition can be invertible while completion loses strict invertibility. Let \(T_N\) be the finite-stage maps. Pointwise algebraic coherence gives

\[
\ker T_N=0
\]

for every \(N\). It does not give

\[
\inf_N s_{\min}(T_N)>0.
\]

If the latter infimum vanishes, normalized states \(v_N\) can satisfy

\[
\lVert T_Nv_N\rVert\longrightarrow0.
\]

This is the minimal completion-escape witness. The limit may acquire an invisible state even though no finite stage contains a kernel.

Falsifier: construct such a normalized sequence while all finite covariance and cocycle equations remain exact.

## Layer five: locus-relative closure

Apparent information loss in a reduced object need not be permanent. An excluded memory can store the distinction and later return it. Closure coherence must therefore be indexed by a boundary cut and a declared memory locus:

\[
\kappa_{\mathrm{cl}}(X\mid\partial X,M_X,L_X,R_X).
\]

Preparation and readout maps belong to the same contextual diagram. Calibration drift can otherwise imitate loss or revival.

Falsifier: reduced states coincide at an intermediate stage while enlarged system-memory states remain distinguishable, or an unspanned analyzer drift produces false revival.

## Exact order of failure

The diagnostic order is typed rather than chronological:

1. scalar square;
2. constructor-natural square;
3. path cocycle on the supported module;
4. reference-span coverage;
5. uniform singular margin;
6. declared memory and observation cut.

The first failed law is the earliest implication needed to justify the next layer. Later tests cannot repair an earlier type failure without adding new authorized data.

## RH hostile interpretation

At a fixed parameter \(s\), every finite Euler stage may be zero-free and every finite transition may satisfy exact covariance. A completed zero is then not explained by a finite local kernel.

Within this compiler, the remaining alternatives are:

- constructor holonomy hidden by scalar Tate readout;
- incomplete reference-span coverage;
- collapsing transfer margin under restricted-product completion;
- an incorrectly declared source, memory, or observation cut.

An RH-strength theorem would have to exclude all authorized off-seam witnesses of these types. This classification does not itself exclude them.

## Finite gluing criterion

On a finite connected context graph under invertible, environment-free transport, one complete constructor-faithful root frame and constructor-complete comparisons on a spanning tree determine every vertex frame up to the common authorized center. Additional scalar comparisons are redundant.

For general channels or hidden memory, diagonal vertex data and tree-edge scalar data do not determine coherent off-diagonal process blocks. A process-level overlap object is required.

## Main conclusion

The fourth tower is not an extra observable. It is the hierarchy of laws required for local typed realizations to glue into one completion-stable global realization. Its characteristic obstruction is a distinction that is invisible on every local scalar chart but survives as constructor holonomy, reference-blind drift, or inverse-limit escape.

