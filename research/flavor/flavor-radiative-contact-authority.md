# Radiative-contact authority audit (WP382)

## Bounded question

Can a one-loop threshold generate a positive source-derived contact for the
WP378 invariant residual \(F\), avoiding the classical obstructions in
WP379--WP381?

## Exact one-loop response

Take a mode whose invariant mass-squared depends affinely on the residual,

\[
m^2(F)=M^2+gF.
\]

With multiplicity \(n\) and statistics sign \(\sigma\), its one-loop potential
in the declared subtraction convention is

\[
V_1(F)=\frac{\sigma n}{64\pi^2}m^4(F)
\left(\log\frac{m^2(F)}{\mu^2}-\frac32\right).
\]

The exact local shell curvature is

\[
K_{\mathrm{loop}}
=\left.\frac{d^2V_1}{dF^2}\right|_{F=0}
=\frac{\sigma n g^2}{32\pi^2}\log\frac{M^2}{\mu^2}.
\]

This is a genuine source response and descends whenever \(F\) and the mass
map are weak-basis invariant. It does not, however, have a fixed sign. For a
bosonic mode it is positive below the threshold scale, zero at \(\mu^2=M^2\),
and negative above it. Fermionic statistics reverses the sign.

## Running versus boundary authority

Include the allowed local contact \(cF^2/2\). The physical local curvature is

\[
K_{\mathrm{tot}}=c(\mu)+K_{\mathrm{loop}}(\mu).
\]

Under \(\mu^2\mapsto\mu^2e^{2t}\), the loop term shifts by

\[
-\frac{\sigma n g^2}{16\pi^2}t.
\]

The counterterm running cancels this shift. Thus the loop determines the
transport law, but a finite boundary value for \(c\) remains necessary. A
subtraction convention setting \(c(M)=0\) is a convention unless tied to an
independently measured observable or a UV boundary theorem.

## Contextual partition and descent

At fixed spectrum and coupling, contexts with different finite boundary
conditions occupy different \(K_{\mathrm{tot}}\) classes despite sharing the
same beta function. Boson--fermion pairs can also cancel the loop contact.
Therefore neither source coupling nor nonzero running implies positive
selection.

The operation descends under the full weak-basis groupoid only if the complete
mass map \(m^2(F)\), multiplicities, and subtraction observable do. A
texture-chart mass prescription would remain a rigidifier and fail the gate.
No new reference port is needed, but a physical subtraction instrument is.

## Disposition

Radiative generation is progressive relative to WP380: it supplies a legal
mechanism outside classical stable minimization and predicts exact running.
It does not yet provide a numerical selector because the finite contact and
even the loop sign are not source-fixed.

The smallest hostile pair is the same scalar source evaluated at
\(\mu^2=M^2/e^2\) and \(\mu^2=M^2e^2\); the curvatures have opposite signs.
The remaining gate is a physical subtraction observable or UV boundary
condition fixing (c), followed by positivity and fitted-ensemble tests.

Run `uv run --with sympy python
research/flavor/checkers/wp382_radiative_contact_authority.py` to regenerate
the result.
