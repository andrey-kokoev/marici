# The coefficient-wall rank obstruction does not survive multiplication representation

## Correction

A coefficient-space constant wall is one feature direction, so its coefficient Gram is rank one. It was incorrect to model its analytic representation as conjugation of that rank-one matrix by a linear map between state spaces.

The source representation is instead multiplication:

\[
\operatorname{Mult}(c)(f)=cf.
\]

For the normalized constant wall \(c=-1\),

\[
\operatorname{Mult}(-1)=-I,
\qquad
\operatorname{Mult}(-1)^*\operatorname{Mult}(-1)=I.
\]

Thus one coefficient feature acts nontrivially on every analytic state. Its represented Gram has full rank in every finite truncation and is the noncompact identity on an infinite-dimensional analytic carrier.

Rank is preserved under conjugation \(ARA^*\), but multiplication representation is not such a conjugation. The earlier rank hostile therefore addressed the wrong functor.

## What remains open

The correction removes the rank obstruction but does not complete G1.1. The completion differential annihilates the zero-mode wall. Consequently the represented identity cannot be treated as an ordinary image coordinate of the completed theta history.

The source-authorized common object must retain:

- the wall as kernel or relative data;
- the causal and anti-causal histories in the completed image;
- a connecting or boundary morphism coupling them;
- the multiplication representation that turns the normalized wall into the analytic identity before the relevant Schur return.

The required theorem is therefore a relative Green or mapping-cone identity, not a direct transport of the wall through completion.

## Revised earliest obligation

Construct the relative completion block and prove that its Schur return is

\[
\frac12(I\pm iH)^*(I\pm iH)
\]

with the source normalization and domains already fixed. Only then may the theta-mass bound be applied to close the uniform shifted-history estimate.

## Checker

`research/nima/checkers/check_rh_wall_history_rank_obstruction.py` now checks the corrected distinction exactly: a rank-one coefficient Gram and its scalar multiplication representation have different ranks, while the represented constant-wall Gram equals the full identity.

## Verdict

The proposed rank no-go is retracted. The genuine obstruction is relative extension and quadratic functoriality across completion. G1.1 remains open, and no RH conclusion is promoted.
