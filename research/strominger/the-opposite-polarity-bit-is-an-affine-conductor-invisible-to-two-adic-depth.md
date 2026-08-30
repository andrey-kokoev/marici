# The Opposite-Polarity Bit Is an Affine Conductor Invisible to Two-Adic Depth

The square bridge factors \(28^2\) and \(36^2\) are the two values of one
source-character law.

For \(\omega_C\in\{-1,+1\}\), define

\[
\kappa_C(\omega_C)=4(8-\omega_C).
\]

Then the terminal full-to-relational Smith ratio is exactly

\[
\frac{s^{\mathrm{full}}_3(C_{\omega_C})}
     {s^{\mathrm{rel}}_2(C_{\omega_C})}
=\kappa_C(\omega_C)^2.
\]

The two values are

\[
\kappa_C(+1)=28=4\cdot7,
\qquad
\kappa_C(-1)=36=4\cdot9.
\]

Their 2-adic valuations agree:

\[
v_2(\kappa_C(+1))=v_2(\kappa_C(-1))=2.
\]

Therefore 2-adic depth necessarily forgets \(\omega_C\): the bit resides in
the odd unit \(8-\omega_C\), while the common factor \(4\) fixes the visible
2-primary depth. The exact integral Smith packet sees \(7\) versus \(9\);
valuation sees only the common power of two.

This explains the \(C_+\) and \(C_-\) merger without appealing to a numerical
coincidence.

## Snake-boundary modulus

For every exact Smith packet define the full-to-relational torsion quotient

\[
\mu=\frac{\prod_i s_i^{\mathrm{full}}}
          {\prod_j s_j^{\mathrm{rel}}}.
\]

It is integral on all five packets. On the opposite-polarity stratum,

\[
\mu_C(\omega)=2^{13}\,3\,(8-\omega)^2.
\]

Thus the affine conductor is not only a ratio of terminal factors. It controls
the complete torsion index of the full gauge extension over its relational
quotient.

Replay:

    python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py

The checker verifies seventy-seven exact gates.
