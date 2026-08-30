# Primitive-index positive-cost selector: WP764

## Question

Can the total rank missing from WP762 be selected dynamically rather than
inserted as a separate tadpole input?

## Claim boundary

Assume three source-derived facts:

1. the domain-wall class has primitive labelled index \(I=+1\);
2. both endpoint sectors must be nonempty;
3. adding a diagonal vectorlike pair has strictly positive energy.

Every admissible ordered representative is then

\[
(n_0,n_\pi)=(k+2,k+1),
\qquad k\in\mathbb Z_{\geq0}.
\]

Take the most general positive additive endpoint cost

\[
E(k)=\mu_0(k+2)+\mu_\pi(k+1),
\qquad
\mu_0,\mu_\pi>0.
\]

## Exact selector theorem

The discrete energy step is

\[
E(k+1)-E(k)=\mu_0+\mu_\pi>0.
\]

Therefore the unique minimum is

\[
(n_0,n_\pi)=(2,1),
\qquad
T=3.
\]

Composed with WP760, this selects

\[
r=2,
\qquad
\Delta=\frac{9}{50}.
\]

The total has not been inserted: it is the minimal positive representative of
the primitive index class. Reversing the source orientation to \(I=-1\)
selects \((1,2)\), reversing the labelled sign.

The selection is gapped. If a quantum or threshold correction has discrete
step bounded below by

\[
\delta E(k+1)-\delta E(k)
>-(\mu_0+\mu_\pi),
\]

the corrected energy remains strictly increasing and the selected class
survives.

## Disposition

This is the first theorem in the branch that derives the exceptional \(T=3\)
from a primitive source class rather than choosing it. Conditional on its
premises, it is a discrete selector with a genuine preparation gap.

Those premises are not yet flavor theorems. The current source does not derive
primitive \(I=+1\), explain why both endpoint sectors are compulsory, or prove
positive vectorlike energy after all interactions. If an endpoint may be
empty, the minimum becomes \((1,0)\). If binding corrections cancel the
positive step, uniqueness is lost.

Nor has endpoint rank been derived as the WP759 boundary-value ratio. The
discrete preparation gap is not yet a four-dimensional RG basin and does not
exclude additive threshold portal counterterms. WP763 gives only a formal
two-port readout until physical endpoint couplings and detector calibration
are constructed.

The next bounded task is to seek one compactification or defect action that
derives all three premises simultaneously and then compute its complete
massive spectrum and threshold step.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp764_primitive_index_positive_cost_selector.py

Generated result:
research/flavor/results/wp764_primitive_index_positive_cost_selector.json
