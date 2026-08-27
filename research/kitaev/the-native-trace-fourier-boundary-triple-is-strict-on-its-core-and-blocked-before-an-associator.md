# The native trace--Fourier--boundary triple is strict on its core and blocked before an associator

## Question

The first credible sixth-level witness would be three source-derived boundary
relations whose two graph-closed parenthesizations differ.  Instantiate the
test using the most native theta/Tate triple:

1. Schwartz--Bruhat restriction to the idelic trace;
2. Fourier-conjugated reciprocal sewing;
3. a typed primitive, square, seam, or endpoint boundary functional.

Does this triple already produce a genuine associator defect?

No.  It is strictly associative on its source core, and the completed problem
is blocked before both closed parenthesizations exist.

## Algebraic source triple

Let

\[
\tau:\mathcal S(\mathbb A)\longrightarrow\operatorname{Ran}\tau
\]

be restriction to the idelic trace range.  Density of the ideles in the
adeles and continuity of Schwartz--Bruhat functions make `tau` injective.

Additive Fourier transform is an automorphism of the Schwartz--Bruhat source.
It induces

\[
J_0(\tau\phi)=\tau(\mathcal F\phi).
\]

Injectivity of `tau` makes `J_0` well defined and invertible on the algebraic
trace range.

Let `ell` be any typed boundary current on a declared domain in that range.
On the common source domain

\[
\mathcal D_\ell
=
\{\phi:\tau\mathcal F\phi\in\operatorname{Dom}\ell\},
\]

one has the literal identity

\[
(\ell J_0)\tau\phi
=
\ell(J_0\tau\phi)
=
\ell\tau\mathcal F\phi.
\]

There is no algebraic associator.  Both parenthesizations are the same partial
map with the same domain.

## Pulled-back source topology

If the trace range is equipped with the topology transported from
`S(A)` through the injective map `tau`, then `tau` is a topological
isomorphism onto its range and `J_0` is continuous because Fourier transform
is continuous on the source.  Composition remains strict.

This topology does not automatically admit the desired primitive, square,
seam, and endpoint currents.  Enlarging it to a rigged boundary topology is
the substantive analytic problem.  In particular:

- the primitive current requires exponential or distributional control;
- the square current is Hilbert but not absolutely summable as a scalar
  coefficient;
- endpoint evaluation needs its own representing-kernel bound;
- the seam compression must become compact enough for determinant geometry.

## What completion can change

After choosing Hilbert or rigged completions, one may attempt to close `tau`,
`J_0`, `ell`, and their composites.  Graph closure is not generally a strict
functor on arbitrary unbounded maps.  It is therefore possible in principle
that closing binary composites in different orders gives different results.

But this possibility is not yet a witness.  For the native triple, the known
status is:

1. `tau` must remain a trace correspondence rather than bounded additive
   `L2` restriction;
2. closability of `J_0` in the full current-bearing trace topology is open;
3. continuity or closability of each boundary row is separately open;
4. consequently, both graph-closed triple parenthesizations have not been
   constructed.

The failure is therefore a binary domain/closability gate.  There is no
defined pair of triple composites whose difference could be a sixth-level
class.

## Relation semantics removes a false anomaly

Algebraic linear relations compose associatively.  One can retain
`tau`, `J_0`, and `ell` as typed partial correspondences and close only the
complete source word after its domain is frozen.  This avoids manufacturing
path dependence by applying graph closure prematurely after each binary
step.

If the programme instead insists on a completion functor applied at every
edge, it must supply comparison maps

```text
closure(S) composed with closure(R)
  -> closure(S composed with R).
```

Coherence of those comparison maps is part of the declared completion
functor.  It becomes independent sixth-level data only if two valid comparison
chains leave a nontrivial invariant residual.  Mere nonfunctoriality of an
arbitrary closure operation is not source physics.

## Smallest decisive domain audit

For each candidate boundary row `ell`, compute:

\[
\operatorname{Dom}(\ell J_0),
\qquad
\operatorname{Dom}((\ell J_0)^*),
\]

and compare them with

\[
\operatorname{Dom}(J_0),
\qquad
J_0^{-1}(\operatorname{Dom}\ell).
\]

The first gate is density of the adjoint domain.  Only if `ell J_0`, `J_0
tau`, and the relevant binary closures all exist should one compare

\[
\overline{(\ell J_0)\tau}
\quad\text{and}\quad
\overline{\ell(J_0\tau)}.
\]

Their source cores agree.  A difference must therefore be exhibited as an
extra boundary state admitted by one graph closure and rejected by the other.

## Falsifiers

- Claiming an associator before both closed parenthesizations exist.
- Using bounded additive `L2` restriction in place of the Schwartz trace.
- Completing the trace before applying Fourier transform and silently losing
  source injectivity.
- Treating different graph domains as a scalar phase anomaly.
- Choosing separate riggings for the two parenthesizations.
- A closure mismatch that disappears when the complete partial relation is
  closed only once.

## Verdict

The native trace--Fourier--boundary triple does not currently support a sixth
tower.  It is strictly associative on the Schwartz--Bruhat core.  The open
problem is whether one source-authorized rigging makes Fourier sewing and all
typed boundary rows jointly closable.

The paired-sector-plus-fifth-sewing architecture therefore survives this
first concrete triple test.  A sixth-level promotion remains conditional on
finding an actual extra boundary state produced by one valid graph-closure
parenthesization but not the other.
