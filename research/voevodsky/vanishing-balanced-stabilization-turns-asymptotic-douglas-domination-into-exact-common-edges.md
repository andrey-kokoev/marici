# Vanishing balanced stabilization turns asymptotic Douglas domination into exact common edges

Let the exactly aligned physical Grams satisfy

$$
G_\alpha^T-G_\alpha^0=D_\alpha,
$$

and define the forced common remainder

$$
C_\alpha
=G_\alpha^T-(D_\alpha)_+
=G_\alpha^0-(D_\alpha)_-.
$$

Suppose there is a positive graph-control form \(B_\alpha\) and \(\varepsilon_\alpha\downarrow0\) such that

$$
C_\alpha\succeq-\varepsilon_\alpha B_\alpha.
$$

Adjoin the same balanced feature

$$
\sqrt{\varepsilon_\alpha}\,B_\alpha^{1/2}
$$

to both polarities. The stabilized Grams are

$$
\widetilde G_\alpha^T
=G_\alpha^T+\varepsilon_\alpha B_\alpha,
$$

$$
\widetilde G_\alpha^0
=G_\alpha^0+\varepsilon_\alpha B_\alpha.
$$

Their signed difference is unchanged:

$$
\widetilde G_\alpha^T-\widetilde G_\alpha^0=D_\alpha.
$$

Their forced common remainder is positive:

$$
\widetilde C_\alpha
=C_\alpha+\varepsilon_\alpha B_\alpha
\succeq0.
$$

Douglas factorization therefore constructs an exact common subfeature for every stabilized regulator. If \(B_\alpha\) is uniformly controlled in the completion graph norm, the added balanced feature has norm tending to zero because \(\varepsilon_\alpha\to0\).

Thus exact finite-regulator domination can be replaced by the asymptotic form estimate

$$
\boxed{
C_\alpha\succeq-\varepsilon_\alpha B_\alpha,
\qquad
\varepsilon_\alpha\to0.
}
$$

The remaining source task is to derive this lower bound for the transported eight-leg Grams with a graph-control form compatible with the phase-energy completion and regulator successors.
