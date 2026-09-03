# The transition trace sharpens the concentration eigenvalue count

## Question

Can concentration-spectrum decay be used without importing a specialized prolate asymptotic theorem?

## Claim boundary

Yes. The second trace defect \(\operatorname{Tr}(T-T^2)\) controls the number of concentration eigenvalues above the required leakage threshold. This replaces the trace-only factor \(1/\eta\) on the full Shannon mass by an additive transition correction. A usable numerical bound still requires control of the transition trace for the actual multi-interval bad set.

## Count identity

Let

\[
1\geq\lambda_1\geq\lambda_2\geq\cdots\geq0
\]

be the concentration eigenvalues, and fix \(0<\eta<1\). Define

\[
N_\eta
=
\#\{j:\lambda_j\geq\eta\}.
\]

For every \(\lambda\geq\eta\),

\[
1
=
\lambda+(1-\lambda)
\leq
\lambda+rac{\lambda(1-\lambda)}{\eta}.
\]

Summing over eigenvalues above threshold and then enlarging both nonnegative sums gives

\[
N_\eta
\leq
\operatorname{Tr}(T)
+
\frac{\operatorname{Tr}(T-T^2)}{\eta}.
\]

Therefore any integer satisfying

\[
M
\geq
\operatorname{Tr}(T)
+
\frac{\operatorname{Tr}(T-T^2)}{\eta}
\]

forces

\[
\lambda_{M+1}<\eta.
\]

## Application

For the combined-symbol tail,

\[
\eta
=
\frac{\delta}{\delta+C_-},
\]

and

\[
\operatorname{Tr}(T)
=
\frac{L|\Omega_{L,\delta}|}{\pi}.
\]

The resulting sufficient dimension is

\[
M
\geq
\frac{L|\Omega_{L,\delta}|}{\pi}
+
\frac{\delta+C_-}{\delta}
\operatorname{Tr}(T-T^2).
\]

The first term is the Shannon mass itself; only the transition region pays the large leakage factor.

## Comparison with the trace-only bound

The previous estimate was

\[
M+1
>
\frac{\operatorname{Tr}(T)}{\eta}.
\]

When most eigenvalues lie near zero or one, \(\operatorname{Tr}(T-T^2)\) is much smaller than \(\operatorname{Tr}(T)\), so the new bound approaches the concentration dimension rather than multiplying the entire trace by \(1/\eta\).

## Remaining geometry

For frequency set \(\Omega\),

\[
\operatorname{Tr}(T-T^2)
\]

is the leakage across the spatial support boundary. Its bound depends not only on \(|\Omega|\) but also on the geometry and boundary complexity of \(\Omega\). The combined-symbol bad set may have many components, so a single-interval prolate estimate cannot be copied without proving a component-sensitive extension.

## Disposition

The exact concentration-decay target is now the transition trace, not an unspecified prolate theorem. The next object is a certified bound for \(\operatorname{Tr}(T_{L,\delta}-T_{L,\delta}^2)\) from the enclosed bad-set intervals. No RH implication is asserted.

## Verification

- `research/voevodsky/checkers/check_transition_trace_eigenvalue_count.py`
- `research/voevodsky/results/transition_trace_eigenvalue_count.json`
