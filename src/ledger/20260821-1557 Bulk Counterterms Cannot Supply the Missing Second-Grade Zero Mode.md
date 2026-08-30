# 1557 — Bulk Counterterms Cannot Supply the Missing Second-Grade Zero Mode

## Hard-to-vary claim

For the three quadratic bulk counterterms printed in the primary source, the
maximal finite-lower-end grades are

\[
\boxed{
\deg_{\eta_0}(c_1,c_2,c_3)=(0,0,2).
}
\]

At grade two, \(c_3\) has only frequencies \(\pm2p\). None of the three
counterterms has a nonoscillatory \(\eta_0^2\) component.

## Derivation

In conformal time:

- \(c_1\) contributes \(a^2(\zeta')^2\). Each differentiated mode is
  proportional to \(\eta\), so the scale factor cancels the two powers and
  the maximal integrand power is zero.
- \(c_2\) contributes \(a^2p^2\zeta^2\). The two undifferentiated modes have
  maximal power two, again canceled by \(a^2\).
- \(c_3\) contributes \(p^4\zeta^2\) without a conformal scale factor, so its
  maximal power is two.

All quadratic commutators carry nonzero frequency \(\pm2p\); their endpoint
primitives preserve the maximal Laurent power. The corrected counterterm
labels of Entry 1536 are used.

## Artifacts

- `research/benincasa/checkers/finite_time_counterterm_endpoint_grades.rs`
- `research/benincasa/results/finite-time-counterterm-endpoint-grades.json`

## Narrow conclusion

Entry 1556's corrected cubic cancellation cannot be completed to the printed
\(-(1+p^2\eta^2)J_0\) by the three displayed quadratic bulk counterterms.
Thus one convention in the cubic-sector assembly remains wrong or incomplete.

The obstruction is narrow: frequency support is correct, the bulk--bulk
coefficient is independently selected by large-\(|\eta_0|\) numerical
asymptotics, and the remaining uncertainty lies in the mixed and
boundary--boundary endpoint normalization/Wick factors.

## Next falsifier

Derive the mixed and boundary--boundary contraction multiplicities directly
from Eq. (18), retaining:

- the two ordered cross terms;
- the formal endpoint delta normalization from Entry 1539;
- the three choices of the undifferentiated leg at each cubic vertex;
- identical-line automorphisms;
- the relative \(+iS_0^{(3)}\) contour phase.

No coefficient may be normalized by fitting Eq. (19). The derived census must
either restore \(-J_0\) or expose a source inconsistency.
