# Rung-four positivity is the positive-contraction binary-filter law

## Binary heat-step filter

Let \(Y_h\) transport the primitive observer from heat scale \(t\) to \(t+h\). Define the complementary innovation channel

\[
X_h=I-Y_h.
\]

The fundamental rung-four condition is the operator interval

\[
\boxed{0\leq Y_h\leq I.}
\]

Equivalently, both binary channels \(Y_h\) and \(X_h\) are positive.

If one common positive carrier contains a source vector \(v_t\), then

\[
H(t+nh)=\langle v_t,Y_h^nv_t\rangle
\]

and

\[
D_{k,h}H(t)=\langle v_t,X_h^kv_t\rangle.
\]

Since every power of a positive contraction is positive,

\[
D_{k,h}H(t)\geq0
\]

for every higher cubical rung \(k\).

Thus all higher complete-monotonicity inequalities follow from one operator-level rung-four law, not from independent scalar positivity checks.

## Forward/reverse coherence

For different heat steps, the filters must inhabit the same carrier and satisfy

\[
Y_{h_1+h_2}=Y_{h_1}Y_{h_2},
\qquad
Y_0=I.
\]

Strong continuity then gives

\[
Y_h=e^{-hL}
\]

for one nonnegative self-adjoint generator \(L\). This single generator produces the positive Bernstein measure, the oriented Fourier carrier, and every Gaussian Gram observer.

## Relation to primitive and primitive-square phases

The primitive phase supplies the action of \(Y_h\). The next primitive-square phase must supply the common positive quadratic form in which

\[
\langle x,Y_hx\rangle\geq0
\]

and

\[
\langle x,(I-Y_h)x\rangle\geq0.
\]

If those two readings are genuinely realized as quadratic forms of the same operator on the same carrier, rung-four positivity is automatic and all higher powers follow.

If they are merely scalar values \(H(t)\) and \(H(t+h)\), no operator inequality follows.

## Exact remaining source theorem

The noncircular target is therefore:

> Construct, directly from the coupled endpoint--gamma--prime primitive and primitive-square observer, one common Hilbert carrier and operators \(Y_h\) satisfying \(0\leq Y_h\leq I\), semigroup composition, and
> \[
> H(t+nh)=\langle v_t,Y_h^nv_t\rangle.
> \]

Constructing \(Y_h\) by GNS from already-positive Hankel matrices is circular. The required advance is to identify \(Y_h\) with an independently constructed forward/reverse source operation on the retained primitive-square carrier.

Under the established heat-kernel conformance and Weil criterion, this operator-level rung-four theorem implies RH.

## Durable inputs

- `research/voevodsky/hausdorff-semigroup-gns-contraction.md`
- `research/voevodsky/finite-difference-complete-monotonicity-gate.md`
- `research/grothendieck/one-heat-translation-dilation-generates-both-observer-families.md`
