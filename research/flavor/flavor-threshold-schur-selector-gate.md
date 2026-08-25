# Threshold reduction loses UV data but need not select IR flavor (WP63, move 4/12)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

A generic heavy-field threshold has the Schur-complement form

\[
H_{eff}=A-BD^{-1}B^\dagger.
\]

The exact checker proves covariance under independent light and heavy basis
changes and constructs distinct UV blocks with the same EFT image. Threshold
matching is therefore noninjective and creates contextual equivalence classes
of UV sources.

But it is surjective on the light target: every (H_{eff}) has the
block-diagonal completion ((A,B,D)=(H_{eff},0,D)). Hence information loss is
not selection. A proper IR image requires an independently motivated
restriction on admissible UV blocks and frozen threshold parameters.

The declared flavor source contains no threshold law, heavy-sector domain, or
threshold instrument. Classification: noninjective reduction, neither
selector nor rigidifier of the original `physical16` family.

Verification:
`uv run --with sympy python research/flavor/checkers/wp63_threshold_schur_selector_gate.py`.
