# The five-margin Green theorem requires prior constructor coherence

## Logical order

The completed Green estimate has two layers that must not be conflated.

### Constructor layer

A terminating, coherently confluent, interface-preserving typed rewrite system must connect arithmetic and analytic constructor realizations. This certificate authorizes the component spaces, comparison maps, gauges, and observers to inhabit one system.

### Analytic layer

Only after constructor coherence is established may five independent margins be assembled:
\[
\delta_P,\quad
\delta_A,\quad
\delta_{\mathrm{glue}},\quad
\delta_{\mathrm{diag}},\quad
\delta_{\mathrm{mix}}.
\]

The rewrite certificate is not a sixth scalar margin. Without it, the five numbers may refer to incompatible presentations and their conjunction has no typed meaning.

## Gauge-reduced support formulation

Let
\[
A=J_c^*J_c,\qquad B=J_d^*J_d
\]
be the coherent and disagreement Green Gram forms. They may have gauge kernels. Therefore \(A^{-1/2}\) and \(B^{-1/2}\) must never be applied on the unreduced ambient spaces.

There are two valid formulations.

### Reduced support operators

Set
\[
H_c^{\mathrm{red}}=(\ker A)^\perp,
\qquad
H_d^{\mathrm{red}}=(\ker B)^\perp.
\]
After proving closed range and uniform lower bounds on these supports, define
\[
R=A_{\mathrm{red}}^{-1/2}CB_{\mathrm{red}}^{-1/2}.
\]

### Quotient forms

Let
\[
\dot H_c=H_c/\ker A,\qquad
\dot H_d=H_d/\ker B,
\]
with norms induced by the closed positive forms. The mixed form \(c(\dot x,\dot y)\) must annihilate the gauge radicals in each variable. Then \(\delta_{\mathrm{mix}}\) is the best constant \(\rho<1\) in
\[
|c(\dot x,\dot y)|
\le
\rho\,
a(\dot x,\dot x)^{1/2}
b(\dot y,\dot y)^{1/2}.
\]
This quotient-form statement is prior to and safer than pseudoinverse notation.

It also exposes a constructor obligation: if the mixed form does not annihilate either radical, the block Green form is not well-defined on the gauge quotient.

## Uniform mixed bound

For each compact off-seam region \(C\), require one number \(\rho_C<1\) such that
\[
|c_{X,s}(\dot x,\dot y)|
\le
\rho_C\,
a_{X,s}(\dot x,\dot x)^{1/2}
b_{X,s}(\dot y,\dot y)^{1/2}
\]
for all cutoffs \(X\), all \(s\in C\), and all reduced vectors.

Pointwise finite-cutoff positivity gives only
\[
\rho_{X,s}<1.
\]
It does not exclude
\[
\rho_{X,s}\to1.
\]
That limit creates asymptotic terminal cancellation without a finite-cutoff kernel.

## Five-margin implication

Suppose on a compact off-seam region:

- arithmetic realization has lower bound \(\delta_P\);
- analytic realization has lower bound \(\delta_A\);
- the seam difference map has lower bound \(\delta_{\mathrm{glue}}\);
- the coherent Green form has lower bound \(\delta_{\mathrm{diag}}\);
- the reduced mixed form has \(\rho\le1-\delta_{\mathrm{mix}}\).

Then the complete Green form has a positive lower bound depending monotonically on these five constants and on the fixed norm-equivalence data of the typed decompositions.

Symbolically,
\[
\delta_{\mathrm{total}}>0
\]
is derived from the positivity of all five margins, uniformly over cutoff and compact off-seam regions.

This is an implication, not an identity. The exact lower-bound formula depends on the source-derived assembly maps and cannot be chosen abstractly.

## Constructor coherence packet

Before the implication is legal, the rewrite certificate must prove:

1. arithmetic incidence and analytic feature packets are typed in one schema;
2. moving-seam transport preserves the complete external interface;
3. the positive Adams coefficient composes coherently;
4. every critical overlap has a unique reduct or authorized higher join;
5. the rewrite measure is strictly decreasing;
6. source energy, observer theory, reciprocal/Real typing, and gauge classes survive every rule;
7. normal-form equivalence is established before applying sector observers.

Terminal-value agreement proves none of these statements.

## Failure taxonomy

The categorical RH construction can now fail in six typed ways:

1. **Prime-plane observability loss:** \(\delta_P\to0\).
2. **Analytic-plane observability loss:** \(\delta_A\to0\).
3. **Seam tangency:** \(\delta_{\mathrm{glue}}\to0\).
4. **Coherent darkness:** \(\delta_{\mathrm{diag}}\to0\).
5. **Mixed terminal cancellation:** \(\delta_{\mathrm{mix}}\to0\), equivalently \(\rho\to1\).
6. **Constructor incoherence:** rewrite termination, confluence, interface preservation, or typing fails.

The sixth precedes numerical analysis. It means there is no authorized assembled system on which the five margins can jointly be asserted.

## Hostile: five good numbers on incompatible presentations

Let an arithmetic constructor reduce through one seam orientation and an analytic constructor through the opposite orientation. Suppose separate scalar observers erase orientation and produce identical positive Gram matrices. Each presentation can exhibit excellent internal, gluing, diagonal, and mixed numerical bounds after its own identification.

If the two orientation rewrites have no typed critical join, those five margins do not belong to one quotient object. Total Green coercivity inferred from them is invalid despite every numerical test passing.

This is constructor failure without analytic margin collapse.

## RH-strength conclusion boundary

Even a complete constructor certificate plus five uniform margins establishes faithfulness and coercivity of the assembled Green packet. To reach the RH claim, one must still identify the resulting generalized eigenvalue-one exclusion with the completed zeta-zero mechanism, including reciprocal symmetry and archimedean completion.

Thus the tower has three final strata:

1. constructor coherence;
2. five-margin analytic coercivity;
3. arithmetic identification of the forbidden spectral collision with off-seam zeros.

No lower stratum may be silently promoted to the next.

## Next finite theorem

The next executable theorem should take finite-cutoff source matrices and return:

- a convergent rewrite certificate;
- gauge radicals for coherent and disagreement forms;
- proof that the mixed form descends to the quotients;
- the five margin estimates;
- a block Green lower bound;
- the typed sector in which generalized eigenvalue \(1\) could occur.

This theorem would be the first complete finite certificate whose uniform passage to completion has exactly the data required by the categorical RH tower.
