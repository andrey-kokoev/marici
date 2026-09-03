# Finite heat-derivative hierarchies are nonfaithful

## Question

Can checking finitely many complete-monotonicity inequalities for every heat parameter recover positivity?

## Claim boundary

The counterfamily addresses every finite derivative cutoff. It does not weaken the global Bernstein criterion.

## Uniform counterfamily

For a chosen cutoff \(N\geq0\), define the signed measure

\[
\eta_N=\delta_1-c_N\delta_2,
\qquad
c_N=\frac{3}{2^{N+2}}.
\]

Its heat transform is

\[
\Theta_N(t)=e^{-t}-c_Ne^{-2t}.
\]

For \(0\leq k\leq N\),

\[
(-1)^k\Theta_N^{(k)}(t)
=e^{-t}\left(1-c_N2^ke^{-t}\right).
\]

Since \(e^{-t}\leq1\) for \(t\geq0\) and \(c_N2^k\leq3/4\), every tested inequality is positive uniformly in \(t\), with bracket margin at least \(1/4\).

At the next derivative order and \(t=0\),

\[
(-1)^{N+1}\Theta_N^{(N+1)}(0)
=1-c_N2^{N+1}
=-\frac12.
\]

Thus the underlying negative atom is invisible to every prescribed finite derivative hierarchy, even when that hierarchy is checked for all heat parameters.

## Disposition

Both axes of the scalar criterion are irreducible:

- all derivative orders at one parameter are nonfaithful;
- finitely many derivative orders at all parameters are nonfaithful.

Only the complete product domain \(k\geq0\), \(t>0\) invokes Bernstein recovery. The checker verifies the construction for derivative cutoffs 0 through 12, covering 91 uniform inequalities.

## Verification

- `research/voevodsky/finite-heat-derivative-hierarchy-nonfaithfulness-v1.json`
- `research/voevodsky/checkers/check_finite_heat_derivative_hierarchy_nonfaithfulness.py`
- `research/voevodsky/results/finite_heat_derivative_hierarchy_nonfaithfulness.json`
