# Gapped-class affine threshold fiber: WP765

## Question

Does WP764's gapped selection of the endpoint class survive as a numerical
low-energy portal prediction after threshold matching?

## Claim boundary

WP764 conditionally selects the discrete class with pre-matching contrast

\[
\Delta_{\mathrm{top}}=\frac{9}{50}.
\]

WP726 independently established that integrating out symmetry-allowed heavy
messengers generates the same CP-even portal operator and that an allowed
renormalized local counterterm can cancel its finite loop contribution.

The threshold-completed coordinate must therefore include both multiplicative
matching and the additive operator boundary:

\[
\Delta_{\mathrm{IR}}
=Z\Delta_{\mathrm{top}}+c
=\frac{9Z}{50}+c.
\]

## Exact obstruction

The discrete preparation class is unchanged by varying \(c\), but the physical
low-energy coefficient is not. In particular,

\[
c=-\frac{9Z}{50}
\]

cancels the selected portal exactly.

If the counterterm runs as

\[
c(\mu)=c_0+b\log\frac{\mu}{M},
\]

then an allowed boundary choice \(c_0\) cancels the contrast at any declared
scale. Renormalization-scale motion is not the physical ambiguity; the
independent renormalized boundary is.

A bounded correction can protect only the sign. If

\[
c> -\frac{9Z}{50},
\]

then \(\Delta_{\mathrm{IR}}>0\), but its magnitude remains continuously
variable.

## Disposition

The pipeline now factors into a gapped discrete selector followed by a
nonfaithful affine threshold arrow. WP764 can explain which topological class
is prepared while failing to predict the numerical low-energy portal. These
are not contradictory statements.

Numerical selection requires a source theorem that forbids or independently
fixes the additive boundary \(c\) and determines \(Z\). A symmetry must forbid
the operator itself, which would also remove the desired portal; therefore the
more plausible repair is a nonrenormalization or complete matching theorem
that ties the boundary to the same source action. Such a theorem is not
currently present.

WP763's eventual instrument must measure the threshold-completed
\(\Delta_{\mathrm{IR}}\), not the pre-matching topological coordinate. Until
then neither the numerical magnitude nor its detector realization has source
authority.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp765_gapped_class_affine_threshold_fiber.py

Generated result:
research/flavor/results/wp765_gapped_class_affine_threshold_fiber.json
