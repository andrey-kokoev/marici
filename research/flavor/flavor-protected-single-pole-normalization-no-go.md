# Protected single-pole normalization no-go: WP1032

## Question

Can the protected completions left open by WP1031—an Abelian moment map or
identical auxiliary/Yukawa squares—fix \(m_S^2=17f^2\) without importing a
fitted normalization?

## Transfer

WP715 proves that a moment-map square fixes relative portal coefficients from
charges but retains its gauge normalization. WP718 proves the analogous result
for auxiliary squares: a representation theorem may fix a Clebsch Gram while
an overall coupling remains continuous. WP1032 specializes both results to
the surviving WP1028 single-pole candidate.

## Protected completions

For \(x=S^2\), \(z=\sum_i|\phi_i|^2\), let

\[
V_D=\frac{G}{2}(q_Sx+q_\phi z-\xi)^2.
\]

After \(z=Nf^2\), \(m_S^2=Nh_Df^2\) with
\(h_D=2Gq_Sq_\phi\). Charges may be quantized, but \(G\) is continuous and
\(\partial(f/m_S)/\partial G\ne0\).

For \(N\) identical contributions \(|yS\phi_i|^2\),
\(m_S^2=N|y|^2f^2\). The Clebsch pattern is rigid, but \(|y|^2\) is continuous.

## Contextual partition and instrument

Fixed charges or Clebsches define discrete representation classes, each with a
continuous \(G\) or \(|y|^2\) fiber. Pole-mass and condensate measurements
determine the effective \(h\); they do not derive or decompose it.

For \(N=17\), the exact compatible interval is

\[
\frac{4835703278458516698824704}{4952981812772558139483425}<h<
\frac{19342813113834066795298816}{19171543993850513913265593}.
\]

The smallest exact falsifier fixes \(N\), charges, and Clebsches: \(h=1\) is
compatible, while \(h=2\) gives \(f/m_S=1/\sqrt{34}\), outside the interval.

## Claim boundary

This closes minimal one-moment-map and identical-auxiliary-square completions,
not a genuinely quantized topological coupling or separately proved
gauge-Yukawa fixed point with typed nondecoupling realization.

## Disposition

Negative. Protection is a relative rigidifier, not an absolute selector. The
remaining constructor must derive \(2Gq_Sq_\phi=1\) or \(|y|^2=1\)
independently of the flavor fit.

Reproduce with
'uv run --with sympy python research/flavor/checkers/wp1032_protected_single_pole_normalization_no_go.py'.

Generated result:
'results/wp1032_protected_single_pole_normalization_no_go.json'.
