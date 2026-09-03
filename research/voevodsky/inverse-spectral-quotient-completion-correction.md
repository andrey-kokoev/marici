# Correction: spectral quotients have inverse variance

## Question

Does the controlled-radical completion model have the correct variance for positive spectral cutoffs?

## Claim boundary

This packet corrects the application of the fixed-radical synthetic model to Weil spectral cutoffs. It constructs the finite inverse-quotient mechanism but does not prove the required infinite projective-limit/completed-form comparison.

## Variance correction

For positive spectral truncations on a fixed test space \(V\),

\[
G_{N+1}=G_N+w_{N+1}F_{N+1}^{*}F_{N+1}
\]

implies

\[
\operatorname{rad}(G_{N+1})
=
\operatorname{rad}(G_N)\cap\ker F_{N+1}
\subseteq
\operatorname{rad}(G_N).
\]

Therefore identity on \(V\) induces a canonical surjection

\[
V/\operatorname{rad}(G_{N+1})
\longrightarrow
V/\operatorname{rad}(G_N),
\]

not a canonical map in the opposite direction. Additional spectral probes separate classes previously identified.

## Exact two-stage fixture

Take \(V=\mathbb Q^4\) with

\[
G_1=\operatorname{diag}(1,1,0,0),
\qquad
G_2=\operatorname{diag}(1,1,1,1).
\]

Then \(\operatorname{rad}(G_1)=\langle e_3,e_4\rangle\) and \(\operatorname{rad}(G_2)=0\). The canonical map \(V/0\to V/\langle e_3,e_4\rangle\) drops the last two coordinates and is surjective.

No identity-induced reverse map is well defined: zero and \(e_3\) define the same stage-one class, while their prospective stage-two images differ.

For this two-stage system, the projective limit consists of pairs \((x_1,x_2)\) with \(x_1=p(x_2)\), and is canonically isomorphic to \(V\). Thus no phantom compatible family appears in this bounded fixture.

## Correction to the previous model

`controlled-asymptotic-radical-completion.md` remains a valid synthetic theorem for a fixed nominated vanishing sector preserved by all transitions. It is not the generic variance of positive spectral cutoffs. Its proposed Weil acceptance test is superseded: one must either

1. retain the common pre-quotient core and quotient only after completion, or
2. prove that the inverse limit of shrinking-radical quotients agrees with the completed quotient and has no phantom compatible families.

## Disposition

The correct finite categorical object is an inverse system of quotient spaces. The next source/analytic gate is an infinite projective-limit theorem tied to the reciprocal Mellin-Schwartz core and completed Weil form. No direct-system transition preserving the initial rank-two radical should be requested.

## Verification

- `research/voevodsky/checkers/check_inverse_spectral_quotient_completion.py`
- `research/voevodsky/results/inverse_spectral_quotient_completion.json`
- `research/grothendieck/spectral-cutoff-radicals-form-an-inverse-not-direct-quotient-system.md`
