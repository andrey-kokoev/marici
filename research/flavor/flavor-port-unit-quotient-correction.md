# Port-unit quotient correction (WP365)

## Bounded question

Are the unit claims \(s=1\), \(\alpha=1\), and equal port norms invariant
statements, or do they depend on the chosen units for the two relational
ports?

Let \(v=(x,y)^T\), where \(x=J^2\) and \(y=Q/M^2\), and change port units by

\[
v'=Sv,
\qquad
S=\operatorname{diag}(a,b),
\qquad a,b>0.
\]

The scaled exchange transforms by conjugation:

\[
P_s'=SP_sS^{-1}=P_{s'},
\qquad
s'=\frac{a}{b}s.
\]

The shell \(x=\alpha y\) becomes \(x'=\alpha' y'\), with

\[
\alpha'=\frac{a}{b}\alpha.
\]

Therefore neither \(s\) nor \(\alpha\) is invariant under independent port
unit changes. Their ratio is:

\[
\frac{\alpha'}{s'}=\frac{\alpha}{s}.
\]

The Ward statement from WP363 descends as \(\alpha/s=1\). Its expression as
\(\alpha=1\) is the equal-unit chart \(s=1\).

## Metric covariance

A Gram matrix transforms as \(G'=S^{-T}GS^{-1}\). For a diagonal metric,

\[
A'=\frac{A}{a^2},
\qquad
D'=\frac{D}{b^2},
\qquad
\sqrt{D'/A'}=\frac{a}{b}\sqrt{D/A}.
\]

Thus equal coordinate norms \(A=D\) are not preserved by independent unit
changes. The invariant content is that the exchange scale agrees with the
metric norm ratio, not that either equals one.

For example, the unit presentation \((s,\alpha,G)=(1,1,I)\) becomes, under
\((a,b)=(2,1)\),

\[
s'=2,
\qquad
\alpha'=2,
\qquad
G'=\operatorname{diag}(1/4,1).
\]

Both presentations describe the same relational Ward condition.

## Disposition

WP365 corrects the claim boundary of WP362--WP364. The exchange Ward identity
can select the invariant relation \(\alpha/s=1\), but cannot by itself predict
the chart value \(J^2=Q/M^2\). That numerical equality requires a physically
fixed common unit or a source-derived calibration map between the ports.

The smallest exact falsifier is the unit presentation and its \((2,1)\)
reparameterization: they are equivalent but have different \(s\) and
\(\alpha\). The remaining instrument gate is an executable common-unit
standard whose calibration is source-derived rather than chosen after the
flavor readout.

Run `uv run --with sympy python
research/flavor/checkers/wp365_port_unit_quotient_correction.py` to regenerate
the exact result.
