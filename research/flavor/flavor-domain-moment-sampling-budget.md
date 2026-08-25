# Sampling budget for the flavor domain-moment instrument (WP98)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

Assume `N` independent, identically prepared, branch-resolved outcomes
`X_k=J_k/J0 in {-1,0,+1}`. Estimate

\[
\hat m_1=N^{-1}\sum_kX_k,\qquad
\hat m_2=N^{-1}\sum_kX_k^2.
\]

Hoeffding and a union bound give simultaneous error at most `eta` with
probability at least `1-delta` whenever

\[
N\ge {2\over\eta^2}\log{4\over\delta}.
\]

The `m1` channel, whose range length is two, is the limiting channel. Under
the WP97 inverse, simultaneous moment error `eta` implies

\[
|\Delta p_+|,|\Delta p_-|,|\Delta p_0|\le\eta,
\qquad d_{TV}(\hat p,p)\le3\eta/2.
\]

This is a mathematical sampling certificate, conditional on independent
reset and correctly resolved canonical outcomes. It does not establish those
resources physically.

There is also an exact rare-route obstruction. Against the null `p_+=0`, an
alternative of weight `p_+=q` produces no plus observation with probability
`(1-q)^N`. Any occurrence-based instrument demanding miss probability at most
`delta` needs

\[
N\ge {\log\delta\over\log(1-q)}.
\]

Thus no fixed finite tower and sample count is uniformly faithful as an
allowed route weight approaches zero. Faithfulness is relative to a declared
minimum weight or finite precision.

Classification: finite-sample separator with stated confidence; neither
selector nor rigidifier. Smallest falsifier of uniform finite-sample
faithfulness is any `q>0` with an all-nonplus sample, an event of exact
probability `(1-q)^N`. Remaining instrument gate: certify IID preparation,
reset, domain resolution, canonical WP93 matching and detector errors.

Verification: `uv run --with sympy python research/flavor/checkers/wp98_domain_moment_sampling_budget.py`.
