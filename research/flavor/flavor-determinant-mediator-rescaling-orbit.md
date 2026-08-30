# Determinant-mediator rescaling orbit

## Question

WP980 asks whether the source grammar admitted in WP977 contains an internal
relation that can fix the coefficient ray left open by WP979.

Write

\[
\rho=\frac{k}{q}
=\frac{\gamma^2\mu^4}{m_s^2(m_A^2)^5}.
\]

The admitted source domain has positive auxiliary masses and
\(\lambda>|\gamma|/16\). It contains the positive rescaling action

\[
R_t:m_s^2\longmapsto t m_s^2,\qquad t>0,
\]

with every other parameter fixed.

## Exact orbit theorem

The action preserves field content, vertex degree, positivity, and the strict
coercivity margin. On the induced coefficient ray it acts as

\[
\rho\longmapsto \frac{\rho}{t}.
\]

For arbitrary \(\rho_1,\rho_2>0\), the unique choice
\(t=\rho_1/\rho_2\) sends \(\rho_1\) to \(\rho_2\). The action is
therefore simply transitive on the full positive ray.

Equivalently, along logarithmic orbit coordinate \(u=\log t\),

\[
\rho(u)=\rho(0)e^{-u},\qquad
\frac{d\log\rho}{du}=-1.
\]

There is no finite stationary point on this orbit.

## Consequence

No condition invariant under all currently declared grammar constraints can
select a proper subset of the positive \(\rho\)-ray. In particular, the
WP978 crossing at \(24696\) is not a boundary of the source-authorized
domain: each side is reachable from the other without changing any declared
coercivity datum.

This is a source-support no-go, not a claim that every rescaled packet has the
same controlled-elimination range or phenomenology. Those extra conditions
could cut the orbit only if independently derived and stated as new source
structure.

The smallest falsifier is a source-derived relation involving \(m_s^2\) that
is not invariant under \(R_t\), fixes or bounds \(\rho\), and survives the
controlled-elimination and global-vacuum gates.

## Reproduction

Run:

    python research/flavor/checkers/wp980_determinant_mediator_rescaling_orbit.py

The generated result is
research/flavor/results/wp980_determinant_mediator_rescaling_orbit.json.
