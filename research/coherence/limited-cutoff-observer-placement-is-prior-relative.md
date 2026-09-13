# Limited-cutoff observer placement is prior-relative

## Experiment

Use twelve ordered contexts, uniform correlation

\[
\rho=0.8,
\]

and independent observation noise with standard deviation \(0.1\). Candidate measurements are the exact right-tail observers

\[
B_i(u)=\sum_{j\ge i}\rho^{j-i}u_j.
\]

For each budget \(m=1,\ldots,6\), exhaustively search all cutoff subsets and minimize posterior trace under a diagonal Gaussian state prior.

## Uniform prior

When all state coordinates have equal prior variance, optimal cutoffs spread across the chain:

```text
budget 1: (0)
budget 2: (0, 7)
budget 3: (0, 5, 9)
budget 4: (0, 3, 6, 9)
budget 5: (0, 3, 6, 8, 10)
budget 6: (0, 2, 4, 6, 8, 10)
```

Spacing reduces overlap between exponentially nested tails.

## Right-heavy prior

Now let uncertainty increase toward the right:

\[
\operatorname{Var}(u_i)=1+0.15i.
\]

The optimal designs become consecutive right-edge cutoffs:

```text
budget 1: (11)
budget 2: (10, 11)
budget 3: (9, 10, 11)
...
budget 6: (6, 7, 8, 9, 10, 11)
```

The design spends its budget where uncertainty is greatest and where late tail observers isolate those states most directly.

## Interpretation

There is no source-independent optimal sparse cutoff set.

```text
uniform uncertainty:
  distribute cutoffs to reduce tail overlap

localized uncertainty:
  concentrate cutoffs near the uncertain region
```

This is precisely why approximate rank reduction required an explicit prior or noise model. Exact realization theory determines the complete observer bank; budgeted sensing selects a subset relative to operational data.

## Design problem

For prior covariance \(C\), noise covariance \(N\), and selected observer matrix \(A_S\), the posterior covariance is

\[
C_{\rm post}
=C-CA_S^T(A_SC A_S^T+N)^{-1}A_SC.
\]

The experiment minimizes

\[
\operatorname{tr}C_{\rm post}.
\]

Other objectives—worst-direction error, mutual information, or endpoint-weighted loss—may choose different cutoffs. The objective belongs in the protocol declaration.

## Verification

```text
python research/coherence/check_limited_cutoff_observer_budget.py
```

The experiment is numerical and exhaustive for the stated twelve-context model.

Artifacts:

- `check_limited_cutoff_observer_budget.py`
- `limited-cutoff-observer-budget.v1.json`
