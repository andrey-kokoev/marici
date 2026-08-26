# Up/down reciprocal-duality typing (WP310)

## Physical16 ratio candidate

Define the dimensionless spectral ratio

\[
r=\frac{m_{u,\max}/m_{u,\min}}{m_{d,\max}/m_{d,\min}}.
\]

It is built from ordered masses and therefore descends to `physical16` on the
nondegenerate domain. Exchanging the up- and down-type Yukawa sectors sends
$r\mapsto1/r$. WP309 would then select $r=1$, equal hierarchy ratios,
without normalizing by the observed answer.

## Source typing failure

The declared Standard Model source does not admit the proposed exchange. The
right-handed fields carry

\[
Y(u_R)=\frac23,
\qquad
Y(d_R)=-\frac13.
\]

They are inequivalent gauge representations. Direct exchange fails, and the
$U(1)$ charge-sign automorphism sends $2/3$ to $-2/3$, not to $-1/3$.
Thus a reciprocal map on quotient coordinates is not induced by a legal source
operation.

The exact mass benchmark in the checker has hierarchy ratio $r=15/11$, so it
also demonstrates that the reciprocal fixed locus is a substantive numerical
restriction rather than an identity.

## Classification

Up/down reciprocity is a mathematical selector in an enlarged
sector-exchange model. It is not a source-authorized Standard Model flavor
selector. A progressive repair needs an anomaly-consistent enlarged source,
an actual exchange operation, controlled breaking and matching, and an
ensemble-level test of the equal-hierarchy prediction declared before fitting.

Run `uv run --with sympy python
research/flavor/checkers/wp310_up_down_reciprocal_duality_typing.py` to
regenerate the exact source-typing audit.
