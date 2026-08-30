# Soft-Ward renormalization-section audit

## Question

Can the cosmological soft Ward identity select a unique section of the
rank-three finite-counterterm orbit established by Ledger 3037?

## Frozen-source typing gate

Collins--Holman--Vardanyan, arXiv:1408.4801, prints the complete gauge-fixed
cubic action in `paper.tex` lines 187--190. Lines 201--205 then retain only
\(\zeta(\partial\zeta)^2\) for the worked toy model and explicitly state that
all cubic operators are required to renormalize the theory at arbitrary time.

The source consequently does not contain the complete one-loop squeezed
three-point function or the nonlinear cubic completions of all three finite
quadratic counterterms. A direct two-point/three-point soft comparison within
the worked truncation is therefore untyped.

## Symmetry-kernel theorem

Let \(\mathcal W\) denote the linear Ward operator and let
\(O_1,O_2,O_3\) be symmetry-compatible local counterterms. For finite
coefficients \(f_i\),

\[
\mathcal W\!\left(S+\sum_i f_iO_i\right)
=\mathcal W(S)+\sum_i f_i\mathcal W(O_i)
=\mathcal W(S).
\]

Thus every properly completed finite counterterm direction lies in the kernel
of the Ward test. Ledger 3037 proves that these three directions span the
complete rank-three response space. Consequently a soft Ward identity can
verify compatibility of a proposed section but cannot select one from this
scheme orbit.

If a candidate finite counterterm fails the Ward identity, it is not an
admissible symmetry-preserving scheme direction. Removing it repairs the
counterterm space; it does not select among the remaining admissible
coefficients.

## Result

The proposed soft-Ward overdetermination test does not supply finite
renormalization authority:

- in the frozen toy source it lacks the required nonlinear completion;
- in a proper symmetry-compatible completion it is constant along every
  admitted scheme direction.

The surviving selector must therefore be a normalization observable or state
condition not identical to the symmetry identities obeyed by all local
counterterms. Examples include source-normalized amplitudes at declared
momenta or an independently specified state/short-distance condition.

## Scope

This does not make the soft theorem physically dispensable. It remains a
necessary compatibility test and can exclude mistyped counterterms. The result
only says that a homogeneous identity shared by the whole scheme orbit cannot
choose a point on that orbit.

## Verification

- primary source: arXiv:1408.4801, `paper.tex` lines 187--205
- scheme-orbit rank: Ledger 3037
- algebraic input: linearity of the Ward operator on independently admitted
  counterterm insertions
