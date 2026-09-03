# Audit of the infinitesimal Dirichlet conjecture

## Question

Does passage from finite mesh to an infinitesimal Dirichlet form supply a new positivity mechanism?

## Claim boundary

The finite and infinitesimal forms are exactly related by integration and differentiation. An unnamed square-root factor adds no explanatory content. No explicit arithmetic kernel has been constructed.

## Exact forms

For a fixed test \(F\), define

\[
Q_{t,h}(F)
=
\left\langle
W,
e^{-tu^2}(1-e^{-hu^2})|F(u)|^2
\right\rangle
\]

and

\[
\mathcal E_t(F)
=
\left\langle
W,
u^2e^{-tu^2}|F(u)|^2
\right\rangle.
\]

The multiplier identity

\[
e^{-tu^2}(1-e^{-hu^2})
=
\int_0^h
u^2e^{-(t+s)u^2}\,ds
\]

gives

\[
Q_{t,h}(F)
=
\int_0^h\mathcal E_{t+s}(F)\,ds
\]

whenever the Weil functional may be interchanged with this integral.

Similarly,

\[
\lim_{h\downarrow0}
\frac{Q_{t,h}(F)}h
=
\mathcal E_t(F)
\]

under continuity along the test path.

## Mesh composition

The two-channel law

\[
1-e^{-(h_1+h_2)u^2}
=
(1-e^{-h_1u^2})
+
e^{-h_1u^2}(1-e^{-h_2u^2})
\]

is exactly additivity of adjacent integration intervals. It is a coherence identity, not positivity evidence.

## Falsification result

If every infinitesimal form is positive, every finite-mesh form is positive by integration. Conversely, finite-mesh positivity combined with small-mesh test density recovers infinitesimal positivity on the corresponding closure.

Thus replacing the finite cone by \(\mathcal E_t\geq0\) relocates the same RH-strength condition. It does not weaken it.

Moreover, if \(\mathcal E_t\geq0\) is already assumed, quotient completion automatically supplies an abstract operator \(R_t\) with

\[
\mathcal E_t(F)=\|R_tF\|^2.
\]

Therefore the bare assertion that such an \(R_t\) exists is circular. It is another GNS construction unless \(R_t\) is defined from arithmetic source data before positivity.

## Surviving conjecture

A noncircular conjecture must provide an explicit nonlocal kernel

\[
K_t(u,v)
\]

or source operator \(R_t\) satisfying

\[
\mathcal E_t(F)
=
\iint
\overline{F(u)}K_t(u,v)F(v)\,du\,dv
\]

and prove positivity from an independent identity. It must reproduce the negative prime singular coefficients rather than replace them by a positive density.

Required data include:

- the source domain and topology;
- the exact kernel or operator formula;
- convergence and adjoint domains;
- the identity with the explicit formula;
- positivity before quotient completion;
- compatibility in \(t\).

## Analytic-topology boundary

Real-line Schwartz density of the heat-polynomial family does not settle this equivalence for the general-zero form, because complex evaluation is not controlled by ordinary Schwartz seminorms. The exact converse requires the analytic graph topology of the completed Weil form.

Generic-mesh pole rigidity avoids that density problem for the reverse RH implication. It does not provide forward positivity.

## Disposition

Reject the unnamed infinitesimal Dirichlet factor as a mechanism. Retain \(\mathcal E_t\) as a useful localization of the same cone. Further work is justified only after an explicit arithmetic \(K_t\) or \(R_t\) is proposed; otherwise another reformulation would be redundant.

## Verification

- `research/voevodsky/infinitesimal-dirichlet-conjecture-audit-v1.json`
- `research/voevodsky/checkers/check_infinitesimal_dirichlet_conjecture_audit.py`
- `research/voevodsky/results/infinitesimal_dirichlet_conjecture_audit.json`
