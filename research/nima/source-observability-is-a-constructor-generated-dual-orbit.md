# Source observability is a constructor-generated dual orbit

## Cross-sector object

Let `H` be a source state module, `A` its authorized constructor algebra, and
`ell` a source-rooted reference observer. The scientifically available
observer packet is not merely `ell`. It is the dual orbit

\[
\mathcal O_{A,\ell}=\operatorname{span}\{\ell a:a\in A\}.
\]

Its common blind subspace is

\[
K_{A,\ell}=\bigcap_{a\in A}\ker(\ell a).
\]

The packet separates the admitted state module exactly when

\[
K_{A,\ell}=0.
\]

For a finite generating family, stack the observers into an analysis map `C`.
Then separation is equivalent to full column rank of `C`. Completion-stable
separation additionally requires a uniform positive lower singular margin.

## Minimal exact witness

On a two-dimensional state space, take

\[
\ell=(1,0)
\]

and let `S` exchange the two coordinates. The single observer is blind to the
second coordinate. Its constructor image is

\[
\ell S=(0,1).
\]

Together, `ell` and `ell S` form the identity analysis matrix and separate the
whole state.

The transformation

\[
T_a=\operatorname{diag}(1,a)
\]

is invisible to `ell` for every `a`, because `ell T_a=ell`. It is detected by
the full observer orbit unless `a=1`. Thus a stable scalar reference leaves a
large stabilizer; active constructor-generated observers shrink it.

Finite rank still does not ensure completion stability. The analysis maps

\[
C_N=\operatorname{diag}(1,N^{-1})
\]

are injective at every finite stage, while their smallest singular values tend
to zero.

## Sector interpretations

- In optics, constructors are authorized analyzer settings and the orbit is a
  spanning calibration frame.
- In control, constructors are admissible input sequences and the orbit is the
  Krylov observability family.
- In flavor, constructors are source-allowed tensor contractions; a radial
  scalar samples only one member of a larger mixed-invariant dual space.
- In RH, constructors include reciprocal, seam, valuation, and Clark–Green
  operations; the Evans scalar is only one observer. The unresolved question
  is whether the resulting source orbit both separates the admissible state
  and carries a completion-stable orientation law.

The final clause matters. Observability can expose a cancellation without
forbidding it. Grothendieck's seam cocycle is already an example: it detects
information erased by the scalar zero but does not exclude the hostile source.

## DPC

For any claim that a reference, readout, or completed scalar determines an
operative state distinction, require:

1. the admitted source module;
2. the authorized constructor algebra;
3. the source-rooted reference observer;
4. the generated dual orbit;
5. proof that its common kernel is zero on the claimed state class;
6. a cutoff-independent lower margin if completion is involved;
7. a separate orientation or admissibility law if nonvanishing is claimed.

Reject a proposed closure if it relies only on:

- one stable scalar reference;
- duplicate observers in the same dual direction;
- full rank at each finite cutoff without a uniform margin;
- an observer synthesized from the desired answer;
- observability alone as a positivity or exclusion theorem.

## Synthesis

The shared minimum system is therefore not two carriers plus an abstract
coherencer. It is a state carrier, a constructor algebra, a generated dual
observer orbit, and a comparison law between state transport and observer
transport. The coherencer is measurable only through that orbit. Its ability
to detect a defect and its authority to reject the defect remain distinct.

