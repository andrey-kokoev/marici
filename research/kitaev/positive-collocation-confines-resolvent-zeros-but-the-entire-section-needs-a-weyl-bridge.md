# Positive collocation confines resolvent zeros, but the entire section needs a Weyl bridge

## Question

The previous packet separated three proposed gates: adjoint mate, positive
port collocation, and cyclic completion.  Which of these actually excludes an
off-real scalar zero, and can the completed theta/Tate scalar section itself
be the resulting diagonal resolvent coefficient?

## Strict Herglotz theorem

Let `A` be self-adjoint on a Hilbert space and let `v` be a nonzero vector.
For nonreal `z`, define

\[
m(z)=\langle v,(A-z)^{-1}v\rangle.
\]

The resolvent identity gives

\[
\operatorname{Im}m(z)
=
\operatorname{Im}z\,|(A-z)^{-1}v\|^2.
\]

Hence `m` maps the upper half-plane strictly into the upper half-plane and
the lower half-plane strictly into the lower half-plane.  In particular,
`m(z)` cannot vanish away from the real axis.

No cyclicity hypothesis is needed.  A noncyclic port can miss an invariant
sector, but it still cannot make its own diagonal resolvent coefficient zero
off the spectrum.  Cyclicity is needed for faithful realization or recovery
of the whole carrier, not for this pointwise zero exclusion.

The metric version is identical.  If `H` is positive, `A` is self-adjoint in
the `H` metric, and the observer is collocated with the forcing port by
`u=Hv`, then the cross coefficient becomes a diagonal coefficient in that
metric and inherits the strict sign.

## Kernel certificate

The stronger finite-family statement is the positive Pick kernel

\[
K_m(z,w)
=
\frac{m(z)-\overline{m(w)}}{z-\overline w}
=
\left\langle
(A-w)^{-1}v,
(A-z)^{-1}v
\right\rangle.
\]

Thus every finite matrix `[K_m(z_i,z_j)]` is positive semidefinite.  This
provides a scalar falsifier for any proposed positive colligation without
first reconstructing its internal metric.  One negative Pick minor rejects
the proposal.

In a finite simple-spectrum model, the same condition says that every pole
residue of `m` is nonnegative in the frozen spectral frame.  A cross-resolvent
coefficient generally has signed or complex residues and therefore fails
before its zeros are inspected.

## Entire-function obstruction

This theorem cannot be applied by simply declaring the completed scalar
theta/Tate section to be `m`.

An entire Herglotz function is affine:

\[
m(z)=az+b,
\qquad
a\geq0,
\qquad
b\in\mathbb R.
\]

Therefore a non-affine completed entire section cannot itself be a diagonal
self-adjoint resolvent coefficient.  The analytic types disagree even before
arithmetic data enter.

The same obstruction is visible from spectral representation: a genuine
diagonal resolvent coefficient is a Cauchy transform of a positive measure.
Its poles, cut, boundary values, and behavior at infinity are not those of a
nontrivial completed entire determinant section.

## Corrected compiler target

Positive collocation remains the right mechanism, but it must live one layer
behind the scalar section.  The missing source-derived bridge must identify
the completed section with a characteristic, determinant, or denominator
object of a positive Weyl function.  It must prove an implication of the
form:

```text
zero of the completed scalar section
  -> forbidden pole, nontransversality, or boundary event
     of a source-derived Herglotz/Weyl family.
```

The arrow cannot be inferred from matching zero sets or fitted after scalar
completion.  Its normalization, boundary triple, source and observer ports,
and reciprocal sheet action must all be derived before the zero is used.

Typical abstract possibilities include:

- the scalar section is a perturbation determinant whose logarithmic
  derivative is a Herglotz difference;
- the scalar section is one denominator in a linear-fractional Weyl
  relation;
- the scalar section is a characteristic function of a conservative
  colligation;
- reciprocal scalar sheets are boundary values of one canonical system.

These are analytic types, not interchangeable formulas.  Each has different
zero, pole, normalization, and completion laws.

## Revised role of the three gates

1. **Adjoint mate:** makes reverse dynamics source-compatible.
2. **Positive collocation:** supplies the strict half-plane sign that excludes
   off-real zeros of the Weyl coefficient.
3. **Cyclic completion:** establishes realization faithfulness and prevents
   the completed scalar bridge from discarding an invariant summand.
4. **Weyl bridge:** transfers the strict sign theorem from the operator
   coefficient to the actual completed scalar section.

The fourth item was previously implicit.  It is logically independent and is
now the principal missing theorem.

## Falsifiers

- A negative finite Pick minor for the proposed Weyl coefficient.
- A complex or negative residue at a real simple pole.
- Direct identification of a non-affine entire section with a resolvent
  coefficient.
- A scalar zero-to-Weyl event correspondence obtained only after dividing by
  the scalar section.
- A boundary triple chosen after inspecting the desired zero set.
- A valid Herglotz coefficient whose characteristic map loses a source
  boundary channel.
- Cutoffwise characteristic identities with no fixed rigged graph closure.

## Verdict

Positive collocation is more powerful and more limited than previously
stated.  It alone excludes off-real zeros of a diagonal resolvent coefficient;
cyclicity is not required for that fact.  But it cannot act directly on the
non-affine entire completed section.  The remaining Deutschian question is:

> Which source-derived Weyl or characteristic construction makes a zero of
> the completed theta/Tate section equivalent to an event forbidden by the
> strict Herglotz sign?

Until that bridge is constructed, positive colligation is a mechanism with no
authorized connection to the scalar proposition being explained.
