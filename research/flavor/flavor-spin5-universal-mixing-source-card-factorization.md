# Spin(5) universal-mixing source-card factorization (WP897)

## Question

Can the two WP895 direct-pole source cards be derived from the admitted
Spin(5) Higgs portal without importing an unrelated MSSM spectrum or fitting
the mixing strengths to a desired detector answer?

## Exact factorization

On WP893's perturbative universal-Higgs-mixing, no-exotic-decay slice, let
\(q_i=\theta_i^2\). Every Standard Model partial width and the
bottom-associated production cross section scale by the same nonnegative
factor:

\[
\Gamma_{if}=q_i\Gamma_f^{\rm SM}(m_i),
\qquad
\Gamma_i=q_i\Gamma_{m SM}(m_i),
\qquad
\sigma_i=q_i\sigma_{bbH}^{\rm SM}(m_i).
\]

Therefore

\[
\operatorname{BR}_{if}
=\frac{q_i\Gamma_f^{\rm SM}}{q_i\Gamma_{m SM}}
=\operatorname{BR}_f^{\rm SM}
\]

for \(q_i>0\). The expected preselection tau rate is

\[
N_i/{\cal L}
=1000q_i\sigma_{bbH}^{\rm SM}(m_i)
\operatorname{BR}_{\tau\tau}^{\rm SM}(m_i).
\]

The checksum-pinned WP243/WP246 calibration gives, per inverse femtobarn and
per unit \(q_i\), 18.7241295132 and 3.31722675436 produced tau pairs. The
listed-mode Standard Model total widths at the two poles are
0.00582138883804 and 0.0247950213684 GeV. Physical mixing only narrows them.

## Minimal source-card family

Each direct card therefore needs only:

- the frozen pole mass \(m_i\);
- a neutral CP-even Higgs-like parent declaration and its ancestry;
- one free nonnegative normalization coordinate \(q_i\);
- the official mass-local Standard Model partial-width table and
  bottom-associated cross section;
- the unchanged shower, pile-up, reconstruction, and selection provenance.

An MSSM SLHA spectrum is not source-authorized and is unnecessary. A forced
tau decay may be used to estimate a conditional response shape only if it is
renormalized by the physical branching fraction above and kept separate from
the absolute event rate.

## Remaining gate and disposition

This factorization does not choose \(q_u\) or \(q_v\). It parameterizes an
instrument family and is neither a selector nor an identification result.
Moreover, detector-template independence from \(q_i\) requires a calibrated
narrow-width statement: the entire allowed interval
\(0<q_i\leq q_i^{\max}\) must remain unresolved by the tau mass response.
That detector resolution and its uncertainty are not supplied by the source
algebra.

Smallest algebraic falsifiers are an exotic partial width not proportional to
\(q_i\), a nonuniversal coupling rescaling, or interference invalidating the
narrow-width rate factorization. The smallest detector falsifier is a
mixing-dependent response column after normalized-rate removal.

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp897_spin5_universal_mixing_source_card_factorization.py
~~~
