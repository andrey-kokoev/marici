# Flavor integer-numerology fork: WP761

## Question

Does the admitted WP737/WP738 representation and anomaly packet derive the
exceptional tadpole total required by WP760?

## Claim boundary

The faithful object would be a named integral map

\[
I:K_{\mathrm{flavor}}\longrightarrow
\mathbb Z_{>0}^2
\]

from a declared representation, compactification, or defect-charge lattice to
the ordered boundary charges \((n_0,n_\pi)\). Merely finding an integer in the
four-dimensional presentation does not define \(I\).

The largest currently authorized probes are the perturbative gauge anomalies,
mixed gravitational-hypercharge anomaly, the \(SU(2)\) Witten parity, and
vectorlike cancellation.

## Exact anomaly record

For one Standard Model family in left-handed conventions,

\[
\sum Y=0,
\qquad
\sum Y^3=0,
\qquad
SU(2)^2Y=0,
\qquad
SU(3)^2Y=0.
\]

The color-weighted number of weak doublets is \(3+1=4\), hence Witten-even
familywise. Every new WP737/WP738 fermion pair is vectorlike and contributes
zero net chiral anomaly. These probes therefore return zero or even parity;
none returns a positive oriented tadpole total.

## Competing exceptional integers

The presentation nevertheless exposes both exceptional WP760 values:

\[
T_{\mathrm{families}}=3,
\qquad
T_{\mathrm{link\ dimension}}=2\cdot2=4.
\]

If the first is renamed as the tadpole, WP760 predicts

\[
\Delta=\frac{9}{50}.
\]

If the second is renamed as the tadpole, it predicts

\[
\Delta=\frac{8}{25}.
\]

The anomaly vector is zero in both readings and chooses neither map. This is
not a finite ambiguity inside an established index; the index constructor is
absent.

A hostile five-family replication remains perturbatively anomaly-free and
Witten-even because cancellation is familywise, yet interpreting family count
as \(T=5\) produces a two-element oriented fiber. Thus anomaly consistency
does not derive the observed family number or the singleton condition.

## Disposition

The current flavor packet does not derive \(T=3\) or \(T=4\). It contains two
presentation integers that would each produce a different desired-looking
singleton. Choosing between them after computing the portal is discrete
numerology, not a Deutschian explanation.

The next source must define an integral index map from an actual
compactification, defect charge, or K-theory class to the ordered boundary
lattice. Its normalization, endpoint orientation, and total must follow from
that construction. Only then may the WP760 singleton theorem be applied.

Even a successful index would settle only the ratio and labelled sign. RG
basin, continuous threshold corrections, `physical16` descent, and a calibrated
instrument remain independent acceptance gates.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp761_flavor_integer_numerology_fork.py

Generated result:
research/flavor/results/wp761_flavor_integer_numerology_fork.json
