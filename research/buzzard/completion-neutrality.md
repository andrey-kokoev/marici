# Completion neutrality interface

## Descended-kernel typing

`descendedKernel_of_compatibleEmbedding` deliberately does not construct a
completed operator. It accepts a source operator, an already supplied
completed operator, and an embedding that is explicitly injective,
zero-preserving, and compatible with both operators. Only then does a kernel
equation at an embedded source point descend back to the source kernel.

The finite `Fin 2` fixture keeps the embedding injective and zero-preserving
but chooses incompatible source and completed operators. Every embedded point
is killed by the completed operator while no point is killed by the source
operator. `compatibility_is_independent_for_descendedKernel` proves that the
missing compatibility square is genuinely false. Completion or embedding
data therefore cannot manufacture the operator-extension interface.

Two further finite fixtures complete the premise audit:

- `collapsedEmbedding` maps `Fin 2` into `Fin 1`. It preserves zero and is
  compatible with the chosen operators, but it is not injective; the completed
  kernel therefore cannot distinguish the nonzero source output.
- `zeroMovingEmbedding` swaps zero and one in `Fin 2`. It is injective and
  compatible with the chosen operators, but it does not preserve zero; a
  completed zero therefore need not reflect a source zero.

Thus injectivity, zero preservation, and operator compatibility are pairwise
independent requirements of this minimal descended-kernel interface.

## Compatible-extension uniqueness

`compatibleOperators_agree_on_image` proves exactly what the algebraic
compatibility square supplies: two candidate completed operators agree at
embedded source points. `compatibleOperators_eq_of_surjective` shows that a
surjective embedding is a sufficient discrete coverage condition for global
uniqueness.

The `properEmbedding : Fin 1 → Fin 2` hostile admits two different target
operators that are both compatible with the same source operator. They agree
on the embedded point and disagree at the unobserved target point, as proved by
`compatibleExtensions_not_unique_without_coverage`. For an actual completion,
surjectivity is normally replaced by density together with continuity or
boundedness of the candidate extensions. Those topological assumptions remain
an explicit missing interface; bare compatibility does not manufacture a
canonical extension.

`compatibleContinuousOperators_eq_of_denseRange` supplies that topological
interface: in a Hausdorff target, two continuous operators compatible with the
same source operator along a dense-range embedding are equal everywhere. The
theorem still assumes both candidate extensions; it proves uniqueness and does
not construct existence.

`existsUnique_uniformContinuousExtension` records the stronger positive
construction under Mathlib's actual completion hypotheses. A uniformly
continuous source map extends uniquely along a uniformly inducing dense
embedding when the codomain is complete and separated. The result packages
existence, uniform continuity, agreement on embedded points, and uniqueness;
none of these premises is inferred merely from the word “completion.”

`existsUnique_compatibleOperatorExtension` specializes this constructor to a
source operator. Its regularity premise is deliberately imposed on the
transported action `embed ∘ sourceOperator`, which is the map actually being
extended into the completion. `kernel_descends_for_compatibleUniformExtension`
then combines compatibility, zero preservation, and injectivity supplied by a
uniform embedding to reflect a completed kernel equation back to the source.
Existence/uniqueness and kernel reflection remain separate conclusions with
separate premises.

## Represented versus completion-only ordinary kernel

`IsRepresentedKernelPoint` records a completed zero whose point lies in the
embedding range. `IsCompletionOnlyKernelPoint` records a completed zero with
no source representative. `completedKernelPoint_partition` proves that every
ordinary completed-kernel point falls into exactly one of these cases, and
`represented_and_completionOnly_disjoint` proves they cannot overlap.

The proper `Fin 1 → Fin 2` embedding supplies an executable completion-only
fixture: the constant-zero completed operator kills target point `1`, which is
not in the embedding range. This is ordinary kernel created in the enlarged
carrier, not a derived/Tor obstruction. Formalizing the latter still requires
sector-supplied chain complexes, differentials, and an exactness convention.

The rational embedding into the reals gives the continuity hostile. The
constant-zero extension and the rational-image indicator agree on every
rational and are compatible with the same zero source operator. They differ at
√2, so `denseCompatibility_not_unique_without_continuity` proves that dense
agreement alone does not determine a target operator. Continuity is therefore
an independent uniqueness premise, not authority transported from density.

`rationalImageIndicator_not_continuous` derives the missing continuity failure
from the same dense-agreement theorem. The stronger
`denseEmbedding_does_not_manufacture_continuousExtension` then uses the dense
identity embedding on the reals: compatibility would force any candidate
extension to equal the discontinuous source operator, so no continuous
candidate exists. This separates extension uniqueness from extension
existence. A completion can make a compatible continuous extension unique; it
cannot manufacture one for arbitrary source data.

## Minimal statement

`asymptoticChargeNeutrality` takes:

- one fixed complex spectral parameter `z` with nonzero imaginary part;
- a real charge sequence `charge`;
- a real sequence `imaginaryResidual` representing the imaginary part of the
  already-paired dynamics error;
- the exact balance
  \(\operatorname{Im}(z)q_n=\varepsilon_n\);
- convergence \(\varepsilon_n\to0\).

It concludes \(q_n\to0\). The companion theorem proves that this convergence
is incompatible with an eventually uniform lower bound
\(\kappa\leq|q_n|\), where \(\kappa>0\).

`pairedResidual_im_tendsto_zero` and
`asymptoticChargeNeutrality_of_pairedResidual` provide the narrow bridge from
an explicitly constructed complex paired residual tending to zero. They use
continuity of the imaginary-part projection and do not infer the paired
residual from raw state-space data.

## Why the residual is already paired

Convergence of raw vectors

\[
(A_n-zI)x_n+b_n\longrightarrow0
\]

does not by itself imply convergence after pairing with `x_n` and `K_n`.
That implication needs uniform boundedness or another explicit control law.
The Lean interface therefore requests the paired imaginary residual directly
instead of manufacturing it from weaker convergence data.

## Hostile omission

`uncontrolledCharge` and `uncontrolledImaginaryResidual` are both constantly
one. At \(z=i\) they satisfy the same balance law, but the residual does not
converge to zero and the charge remains nonneutral. Thus residual convergence
is an independent premise.

A sharper hostile separates raw and paired residuals:

\[
r_n=\frac1{n+1}\longrightarrow0,
\qquad
w_n=n+1,
\qquad
w_nr_n=1.
\]

`vanishingRawResidual_tendsto_zero` proves the first limit, while
`amplifiedResidual_does_not_vanish` proves failure after the unbounded pairing
amplification. Uniform pairing control is therefore an independent premise,
not a consequence of raw residual convergence.

## Positive transport repair

`pairedResidual_tendsto_zero_of_boundedAmplifier` uses Mathlib's native
`Filter.isBoundedUnder_le_mul_tendsto_zero` interface. It proves the minimal
scalar repair: norm-bounded pairing amplification transports a vanishing raw
residual to a vanishing paired residual. The composed theorem
`asymptoticChargeNeutrality_of_boundedAmplifier` then yields charge neutrality.

`pairedResidual_tendsto_zero_of_convergentAmplifier` proves that a convergent
complex amplifier times a vanishing raw residual tends to zero. The composed
theorem `asymptoticChargeNeutrality_of_convergentAmplifier` then yields charge
neutrality. Amplifier convergence is retained as a convenient sufficient
specialization but is no longer mistaken for the minimal interface.

What remains sector-specific is proving that the actual state-metric pairing
amplifiers form a bounded family. The scalar library records the consequence
of such a proof but supplies no authority for the bound itself.

## Scope and verification

This is a scalar completion interface, not a construction of completed
operators, domains, or source metrics. Those objects remain sector-specific.
Per Nima's instruction, no Lean compilation or project build was run, and the
module is not imported into `MariciFormal.lean`.
