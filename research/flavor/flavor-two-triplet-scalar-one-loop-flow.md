# Two-triplet scalar one-loop flow: WP662

## Domain and normalization

For two real labelled triplets define

\[
a=|n|^2,\qquad b=|m|^2,\qquad c=n\mathbin\cdot m
\]

and the closed scalar potential

\[
V=-r_na-r_mb+\lambda_na^2+\lambda_mb^2+\lambda_xab+\lambda_cc^2.
\]

The calculation retains the coefficient of every scalar operator in
\(\operatorname{Tr}(\operatorname{Hess}V)^2\). A common positive one-loop
normalization is omitted because only support, signs, and exact relative flow
are used here.

## Complete scalar flow

The four quartic coefficients are

\[
\begin{aligned}
\beta_n&=4\lambda_c^2+8\lambda_c\lambda_x+176\lambda_n^2+12\lambda_x^2,\\
\beta_m&=4\lambda_c^2+8\lambda_c\lambda_x+176\lambda_m^2+12\lambda_x^2,\\
\beta_x&=8\lambda_c^2+16\lambda_c(\lambda_n+\lambda_m)
+80\lambda_x(\lambda_n+\lambda_m)+32\lambda_x^2,\\
\beta_c&=\lambda_c(40\lambda_c+32\lambda_n+32\lambda_m+64\lambda_x).
\end{aligned}
\]

The two mass parameters flow as

\[
\beta_{r_n}=80\lambda_nr_n+(8\lambda_c+24\lambda_x)r_m,
\qquad
\beta_{r_m}=80\lambda_mr_m+(8\lambda_c+24\lambda_x)r_n.
\]

No scalar operator outside the admitted two masses and four quartics is
generated.

## Benchmark stability

At the WP661 point

\[
(r_n,r_m,\lambda_n,\lambda_m,\lambda_x,\lambda_c)=(2,2,1,1,1,1),
\]

the mass flow is \((224,224)\) and the quartic flow is
\((200,200,232,168)\). The radial stability determinant
\(D=4\lambda_n\lambda_m-\lambda_x^2\) equals three and has forward
derivative 1136. The orthogonality coupling remains positive, while the
symmetric vacuum norm has finite derivative \(-592/9\). Hence an open forward
neighborhood retains the orthogonal trivial-stabilizer frame.

## Typed disposition

This is complete only for the scalar subsector. It upgrades WP661 from support
closure to local scalar-flow stability. It does not include messenger, gauge,
or Yukawa contributions and therefore does not authorize an RG-complete source
model or a numerical selector.

Smallest exact falsifier: a scalar operator outside the six-parameter support,
or a nonpositive radial determinant after an infinitesimal forward step.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp662_two_triplet_scalar_one_loop_flow.py

Generated result: results/wp662_two_triplet_scalar_one_loop_flow.json.
