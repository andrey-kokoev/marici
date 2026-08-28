# Equivariance Forces Either Reference Charge or External Comparison

## Central-character grading

Let \(z\) be the nontrivial central element in the kernel of

\[
Mp(4,\mathbb R)\longrightarrow Sp(4,\mathbb R).
\]

On the endpoint oscillator module \(H\), \(z\) acts as \(-I\). On a trivial
reference module \(K\), it acts as \(+I\). These are the two characters of the
central \(\mathbb Z_2\).

If \(f:H\to K\) is metaplectically equivariant, then

\[
f\rho_H(z)=\rho_K(z)f.
\]

Substitution gives \(-f=f\). Over characteristic different from two,
\(f=0\). The same argument annihilates equivariant morphisms in the opposite
direction.

Therefore a direct off-diagonal comparison with a trivial reference cannot be
generated inside the equivariant endpoint category.

## Tensor powers do not repair the obstruction

Central characters multiply under tensor product. If \(H\) has odd character,
then

\[
z|_{H^{\otimes n}}=(-1)^n I.
\]

Even tensor powers can supply a sector with trivial central character, but no
equivariant morphism connects an odd tensor power directly to an even one.
Direct sums, subobjects, quotients, and invariant completion preserve this
character decomposition.

A second identical endpoint copy also fails when the loop acts diagonally on
both copies: both acquire the same sign, so no relative phase appears.

## Hostile correction: a charged dual reference

At finite cutoff, the equivariant category contains the dual module
\(H_N^\vee\) and the evaluation

\[
\operatorname{ev}:H_N^\vee\otimes H_N\longrightarrow \mathbf 1.
\]

Both factors have odd central character, so their tensor product is even and
evaluation is equivariant. This falsifies the stronger claim that every
detecting pairing must itself break metaplectic symmetry.

Under diagonal central action, both factors change sign and evaluation is
unchanged. Evaluation changes sign only if the loop acts on one factor while
the other remains fixed. Thus the irreducible missing datum is either:

- a non-equivariant comparison to an even reference; or
- a charged dual reference together with authority to address one tensor
  factor selectively.

This is only a finite-cutoff counterexample. The completed oscillator Hilbert
space is infinite-dimensional and is not dualizable in the Hilbert tensor
category. Its formal coevaluation has divergent norm, so the global charged
reference does not follow from Hilbert completion. Entry 3696 records this
completion obstruction and the trace-class repair.

## The missing constructor

One minimal missing constructor is a relative-central-character comparison:

```text
input: one odd central-character sector and one even sector
action: an off-diagonal pairing not equivariant under the central element
output: a scalar or port state whose sign changes under selective central action
authority requirement: a source declaration that breaks or frames central symmetry
```

Alternatively, one may use the equivariant dual evaluation and add a
controlled-action constructor that applies the metaplectic loop to one sector
while holding the charged reference fixed. This adds authority to address one
factor asymmetrically. Diagonal group action alone does not furnish it.

## Categorical no-go theorem

Let \(\mathcal C\) be a characteristic-zero additive monoidal category of
\(Mp(4,\mathbb R)\)-representations, and let \(\mathcal C_+\) and
\(\mathcal C_-\) denote the full subcategories on which \(z\) acts as \(+I\)
and \(-I\). Then

\[
\operatorname{Hom}_{\mathcal C}(X_+,X_-)=0
=
\operatorname{Hom}_{\mathcal C}(X_-,X_+).
\]

Consequently, closure under equivariant categorical constructors cannot create
a direct port between opposite central characters. It may create an invariant
odd-odd pairing, but detecting the sign then requires factor-selective action.
Any successful readout therefore witnesses additional comparison or
addressability authority; it need not witness symmetry breaking in the port
itself.

## Meaning for the tower hierarchy

The reference capability is not simply the next rung of the existing
metaplectic tower. It is a transverse attachment plus an addressing rule. The
next coherence level must type both:

1. which component the central loop acts on;
2. which comparison is authorized and whether it is equivariant or framed.

This predicts a concrete failure mode: a system may possess invariant closure
and arbitrarily many internally coherent tensor powers while remaining unable
to execute the comparison that exposes its global lift class.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/metaplectic_reference_port_no_go_checks.py
```

The finite exact checker tests central-character selection, tensor parity, the
absence of equivariant mixed ports, the charged-dual counterexample, and the
distinction between diagonal and factor-selective action.
