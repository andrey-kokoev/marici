# Associated-production beam tag: WP680

## Source constructor

The admitted entrance vertex and the reconstructed messenger representation
already supply

\[
\overline Q_L\widetilde H A_R,
\qquad
A_R\sim(3,1,2/3).
\]

QCD therefore generates the associated partonic channel

\[
qg\longrightarrow A H.
\]

Its source support is proportional to (g_s^2\lambda^2). This establishes a
nonzero algebraic production constructor without fitting the desired CP
answer. It does not establish a hadronic rate.

## Relational beam orientation

Let (t=\operatorname{sign}(y_{AH})) be the sign of the reconstructed
associated-system rapidity. Under exchange of the identical proton beams,
both the fixed beam orientation and (t) reverse. Their product therefore
descends to the identical-beam quotient.

Multiplying the WP678 signed triple product by (t) gives a relational CP-odd
observable. With quark-direction mistag probability (omega), its phase port
is

\[
S_o=\eta D\sqrt{uv}\sin\phi,
\qquad
\eta=1-2\omega.
\]

For nonzero calibrated (eta D), this third port generically restores the
three-coordinate algebraic response rank. At (omega=1/2), the tag is random
and the phase port collapses exactly.

## Authority boundary

This packet establishes source existence and groupoid descent only. It does
not yet supply:

- the complete finite-mass (qg\to AH) matrix element in the physical pole
  basis;
- a PDF-calibrated quark-direction dilution;
- reconstruction and sign-assignment response for (A), (H), and the
  cascade products;
- backgrounds, detector covariance, or context-saturated support.

Thus the operation is a source-derived candidate relational probe, not an
executed physical instrument and not a flavor selector.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp680_associated_production_beam_tag.py

Generated result: results/wp680_associated_production_beam_tag.json.
