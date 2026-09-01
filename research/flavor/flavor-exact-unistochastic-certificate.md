# Exact unistochastic certificate: WP1171

## Question

Does a rigorous exact solution exist near the numerical support-five
candidate?

## DPC resolution

- **Problem:** exactify the WP1170 real orthogonal fixed-\(q\) candidate.
- **Conjecture:** the candidate lies in a box containing an exact real
  orthogonal solution.
- **Rivals:** optimizer artifact; Newton refinement; Krawczyk interval
  certificate; symbolic elimination.
- **Risky consequences:** twenty-six gauge-fixed equations, a radius
  \(10^{-40}\) coordinate box, and nonzero off-diagonal entries.
- **Falsification attempt:** the Krawczyk operator contracts with
  infinity norm about \(1.64\times10^{-37}\) and maps the box strictly into
  itself.
- **Residual:** the certificate proves existence near the candidate but gives
  neither a symbolic closed form nor a sourced physical production law.
- **Disposition:** accept rigorous exact existence and select production
  realization.

Checker: `research/flavor/checkers/wp1171_exact_unistochastic_certificate.py`

Result: `results/wp1171_exact_unistochastic_certificate.json`
