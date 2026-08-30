# RH first Adams obligation reconciliation

## Question

What is the earliest unresolved theorem in the completed first Adams edge after reconciling packets written at different construction stages?

## Claim boundary

The four-front target identity alone does not close the edge. Later source packets prove more: the base-plus-curvature source square gives the four-front packet separately on every retained theta label, and evaluation at the multiplicative tensor unit recovers one Stieltjes boundary copy exactly.

For the diagonal orbit

\[
\Delta f=(\mathcal M_n f)_{n\ge1},
\]

the canonical counit is

\[
\varepsilon_1=\mathcal M_1^{-1}\operatorname{ev}_1,
\qquad
\varepsilon_1\Delta=I.
\]

Thus these stages are no longer open:

1. target four-front coefficients;
2. labelwise source constructor identity;
3. recovery of one source copy by a canonical labelled counit;
4. ordered primitive reconstruction on that copy.

The remaining local theorem is the source covariance of the reciprocal shifted-history Green block on the tensor-unit fiber:

\[
D_{p,\pm}^{(1)}
=
\mathcal M_1D_{p,\pm}^{\mathrm{St}}\mathcal M_1^{-1}.
\]

This identity must be proved for the actual completed operators and domains. Abstract diagonality or a finite proxy does not prove it. It must also survive the declared radical quotient and retain separate theta and valuation-prime labels.

## Disposition

Gate G1 remains open. Its earliest local residual is no longer source extraction of the four-front packet; it is unit-fiber shifted-history covariance plus radical-compatible completion. The exact tensor-unit checker verifies the categorical retract and rejects label mixing, but records the operator covariance as unproved.

Evidence:

- `research/nima/the-base-plus-curvature-green-square-closes-exactly-on-every-theta-label.md`
- `research/nima/the-theta-tensor-unit-projection-is-a-canonical-retract-of-the-diagonal-mellin-orbit.md`
- `research/nima/the-theta-tensor-unit-retract-closes-the-first-adams-green-metric-comparison.md`
- `research/nima/checkers/check_first_adams_tensor_unit_retract.py`
- `research/nima/results/first-adams-tensor-unit-retract.json`
