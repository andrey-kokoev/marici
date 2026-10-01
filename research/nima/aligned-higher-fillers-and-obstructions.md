# Aligned higher fillers: two ascending steps and their obstructions

## Chosen filler realization

Use the full two-factor biclique comparison complex as an additive realization
of higher comparison data. For parallel chain endpoints u,v in degree k-1,
a degree-k filler is

    K in C_k with d_k*K=u-v.

The difference must be closed and lie in image(d_k). Its admissible fillers form
an affine space over ker(d_k). The record retains degree, both endpoint chains,
the chosen coefficient vector and its cost.

This supplies a concrete chain-level filler operator using existing retained
comparison cells. An adapter from the reference cone's named comparisons and
matrix responses into these chain endpoints is still required for the original
carrier model. The zero additive discrepancy has its unambiguous zero chain
input; a nonzero matrix residual has no such adapter supplied by this test.

## Exact section and retained choice

A deterministic labelled column elimination builds a section s_k on image(d_k).
A dependent column j supplies a kernel generator

    e_j - s_k(d_k*e_j).

Each such generator has its own unit dependent-column coordinate, proving their
independence. They parametrize all filler ambiguity.

Returning a new admissible boundary Delta while retaining existing filler K is

    K_new = K + s_k(Delta-d_k*K).

This preserves the kernel component K-s_k(d_k*K). The section is an explicit
selector, generally not a minimum-cost selector. Higher-cell unit coefficient
cost ||K||^2 is recorded without discarding cross terms. A constrained
minimum-cost selector can be substituted using the earlier exact-return machinery.

## Two consecutive steps

| Operator | Candidate dimension | Image rank | Fixed-boundary ambiguity |
|---|---:|---:|---:|
| d3 | 2496 | 1037 | 1459 |
| d4 | 2192 | 1459 | 733 |
| d5 | 864 | 732 | 132 |

Starting from the aligned reference discrepancy0, the fresh section gives K3=0.
A retained nonzero closed3-chain is also a valid filler of0 and is preserved by
the boundary-return rule. It has positive recorded cost.

Two3-fillers of the same boundary differ by a closed3-chain. Every such difference
has a4-filler: the checker solves all1459 independent3-cycle generators using d4.
For each resulting4-boundary,733 independent choices remain. Explicit records
for a3-filler and a4-filler demonstrate two genuine degree-ascending steps.

The nonzero-boundary case is also tested: a local3-cell boundary gets a3-filler,
and adding a closed kernel vector supplies another filler with the same boundary.

## Obstructions and support

The two independent H2 sphere classes are closed2-chains outside image(d3).
Each is rejected as a proposed3-boundary. Thus parallel/closed endpoints alone
do not guarantee a filler.

At the following stage, ker(d4) has dimension733 but image(d5) has rank732.
The remaining H4 class produces an explicit closed4-chain rejected as a5-boundary.
This is the product orientation class of the full two-factor geometry, consistent
with its previously computed Betti numbers.

Restricting the allowed candidate cells can create further support obstructions.
The checker exhibits a boundary that fills in the full frame but fails in a
single-cell support frame. Filler existence must therefore be checked in the
actual retained/support-constrained operator.

## Structural consequence

A type-ascending filler recurrence is now executable. Its admissible domains
and ambiguity dimensions are governed by the boundary operators and homology.
The dimensions1459 and733 differ from the independent-product class counts1,2,4;
these are distinct recursive constructions.

The next carrier-level task is the boundary adapter: map the actual aligned
reference comparison into the candidate chain complex, preserving its endpoints
and support. That adapter determines whether the computed obstructions vanish
for the intended successor. The additive cone's zero discrepancy alone selects
no new nonzero filler from a fresh state; retained kernel history can carry
additional data explicitly.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_aligned_higher_fillers.py

Exact sections for d3,d4,d5, all1459 degree3 kernel fillings, explicit successive
filler records, zero/fixed-history behaviour, two sphere obstructions, a surviving
degree4 obstruction and restricted-support rejection. Filler equations and
coefficient costs use Fraction arithmetic. This is an additive chain prototype,
not a new formal globular or physical realization theorem.
