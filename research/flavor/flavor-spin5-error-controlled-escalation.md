# Spin(5) error-controlled discordance escalation (WP907)

## Question

Can the paired response experiment stop early or escalate after observed
discordances without the optional-stopping defect identified by WP906?

## Frozen four-look rule

Use WP906's discordance target

\[
p_0=\frac{389}{2937600}.
\]

There are four preregistered looks per pole. Look (kin\{0,1,2,3\}) occurs at
the exact minimum (n_k) for which

\[
\Pr_{p_0}\{\operatorname{Bin}(n_k,p_0)\leq k\}\leq\frac1{160}.
\]

At look \(k\), stop and certify only if the cumulative discordance count is at
most (k). Otherwise continue to the next frozen look. If look three fails,
the escalation ends without certification.

Each look spends \(1/160\). By the union bound, the probability under any
\(p_D\geq p_0\) of certification at one or more looks is at most
\(4/160=1/40\) per pole. The two poles therefore retain total failure
probability at most \(1/20\). Dependence between looks is allowed; no
independence approximation is used for the familywise bound.

## Exact verification

The checker derives every (n_k) using the integer inequality

\[
160\sum_{j=0}^{k}{n_k\choose j}389^j
(2937600-389)^{n_k-j}\leq2937600^{n_k},
\]

implemented without floating-point probability arithmetic. For every look,
the reported count passes and one fewer pair fails. It also verifies the exact
per-pole and two-pole error sums.

The smallest protocol falsifier is an unregistered extra look or acceptance
at a look whose discordance boundary is exceeded. Either invalidates the
declared error allocation.

## Boundary

This rule repairs optional stopping only. It does not supply the paired CMS
samples, marginal validation, replay evidence, pair independence, or the
calibrated acceptance floor. It is a detector-response stopping instrument,
neither selector nor rigidifier.

Run:

~~~text
uv run python research/flavor/checkers/wp907_spin5_error_controlled_escalation.py
~~~
