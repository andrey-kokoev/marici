# qRB microstep 19: window-defect input contract

A quantitative estimate for `E_X` cannot be proved from the regulator label alone. It requires a concrete sharp-window family:

$$
\widetilde Q_X=\mathbf 1_{I_X}(A)
$$

or a specified smoothed substitute, together with the source operator `A`, interval `I_X`, and observer class.

The minimum input contract is:

1. explicit `A` and `I_X`;
2. normalization of `\mathcal M_{\log}`;
3. finite observer/test core;
4. target trace norm or projective seminorm;
5. endpoint convention.

Without these data, the only valid result is the structural identity

$$
E_X=\widetilde Q_X\mathcal M_{\log}-\mathcal M_{\log}P_X.
$$

Status: dependency isolated. No numerical or analytic defect estimate is claimed until a concrete window family is supplied.
