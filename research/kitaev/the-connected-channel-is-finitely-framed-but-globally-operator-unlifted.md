# The connected channel is finitely framed but globally operator-unlifted

## Correction: a global coefficient-lens lift exists

The title's “globally operator-unlifted” claim is too broad.  The connected
prime channel has a canonical global Schatten-three lift on the prime
coefficient space:

\[
K_se_p=p^{-s}e_p
\quad\text{on}\quad
\ell^2(\{p\}).
\]

For `Re s>1/3`, this operator lies in `S_3` and its regularized determinant
recovers the connected Euler channel exactly.  What remains unlifted is the
**completed boundary realization** coupling this coefficient operator to the
primitive, square, seam, archimedean, forcing, and endpoint modules.  See
`the-connected-channel-has-an-exact-global-schatten-three-coefficient-lift.md`.

## Question

Does the connected channel `C` already mean the fully framed determinant of a
frozen source operator, thereby killing the odd-exponential adversary, or is
it only an unframed regularity class?

The answer splits by stage.  `C` is exactly framed by the finite local source
determinant, but no completed global Schatten-three operator realizing that
frame has been constructed.

## Exact finite framing

For each local valuation chain and every finite prime cutoff, the source gives
the exact cumulant decomposition

\[
E_X
=
\exp(P_{1,X}+P_{2,X})C_X.
\]

Equivalently,

\[
C_X
=
E_X\exp(-P_{1,X}-P_{2,X}).
\]

Here `E_X` is the full finite Euler determinant, while `P_1,X` and `P_2,X`
are the independently derived primitive and square cumulants.  The terminal
cutoff current remains inside `C_X`; it is not discarded.

This identity fixes `C_X` as a holomorphic function, not merely through a
finite list of jets.  The hostile transformation

\[
C_X\mapsto e^{g}C_X
\]

fails unless `e^g=1` identically.  For an odd holomorphic `g` in the frozen
frame, that forces the trivial reframe.

Thus the full labelled finite source identity kills the odd-exponential
adversary.  Bounded finite testing cannot verify the identity completely, but
the mathematical constructor law is all-order.

## Convergence-chamber framing

The connected Euler product beginning at grade three converges absolutely in
its source chamber extending toward the critical seam.  Consequently it
defines a canonical scalar holomorphic unit there.  Any proposed completed
sector frame agreeing with it on a nonempty open subset is uniquely fixed on
every connected domain to which both extend holomorphically.

Therefore a cutoff-independent odd entire reframe cannot be introduced after
continuation while preserving the source chamber.  The identity theorem
rejects it.

Completion ambiguity can reappear only if the alleged continuation is not the
compact-open continuation of the same framed finite system—for example, if a
cutoff-dependent reframe has no normal limit in the Euler chamber but is
assigned a different generalized limit elsewhere.

## Missing global operator lift

The exact local determinant filtration has the formal shape of

\[
\det_3(I+K_X).
\]

But the programme has not yet constructed a global source-derived operator
family `K_X(z)` satisfying all of:

1. `K_X(z)` lies in Schatten class three on the completed sector carrier;
2. its finite traces equal the typed primitive and square currents;
3. its third regularized determinant equals the connected `C_X` frame;
4. cutoff inclusions are operator-natural;
5. seam and archimedean boundary blocks are retained;
6. the limit operator graph is closable;
7. sector accretivity or inverse stability holds.

Accordingly, `C` is presently a source-framed local and finite scalar
determinant channel, not yet the determinant functor of one completed global
operator.

## Why the distinction matters

Finite scalar framing solves the uniqueness problem.  Global operator framing
would additionally solve provenance and composition:

- it would define how `C` responds to pre-sewing sector operations;
- it would determine the admissible determinant ideal;
- it would type the multiplicative anomaly through `P/Q` traces;
- it would make sector accretivity an operator statement;
- it would support compact-open determinant continuity.

Without the operator lift, one can reconstruct finite Euler scalars exactly
but cannot infer that the completed boundary relation preserves their
invertibility.

## Revised DPC status

The first finite uniqueness attack does not falsify the full source-closed
DPC.  It falsifies only replacements of the all-order finite determinant law
by bounded scalar and jet audits.

The DPC now has a sharper load-bearing arrow:

```text
exact framed finite connected determinants
  -> one source-derived global Schatten-three operator family
  -> determinant-class seam and archimedean sewing
  -> compact-open completed sector unit.
```

The first arrow is missing.  It is not an odd-frame choice.

## Falsifiers

- A finite cutoff where the exact `P/Q/C` reconstruction residual is nonzero.
- Two source-derived global `S_3` operator families with the same finite
  determinant packet but inequivalent seam action.
- A candidate `K_X` whose first or second traces do not equal `P_X` and `Q_X`.
- Schatten-three convergence without graph closability.
- A cutoff-dependent reframe that agrees only after reciprocal scalar sewing.
- An operator lift derived from the completed scalar determinant ratio.
- A source-chamber connected determinant that fails to match the proposed
  continuation on an open set.

## Verdict

`C` is neither merely an unframed regularity class nor yet a completed
operator determinant.  It occupies the intermediate status:

> all-order source-framed at every finite cutoff and in its convergence
> chamber, but globally operator-unlifted through the completed boundary.

This substantially narrows the next task.  Do not seek another frame probe.
Construct or obstruct the global Schatten-three operator lift whose traces,
regularized determinant, seam action, and cutoff maps reproduce the already
fixed finite packet.
