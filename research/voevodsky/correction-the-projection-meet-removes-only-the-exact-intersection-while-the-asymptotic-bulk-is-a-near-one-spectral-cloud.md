# Correction: the projection meet removes only the exact intersection, while the asymptotic bulk is a near-one spectral cloud

## Claim being corrected

The fixed-cutoff meet

\[
E_\Lambda^{meet}
=P_\Lambda
\wedge
Q_\Lambda
=P_{\{1\}}(B_\Lambda)
\]

was proposed as the required one-sided inner bulk projection.

It is a canonical exact-intersection projection, but it need not carry the asymptotic volume bulk. Calling it the completed bulk projection was too strong.

## Exact atom versus approximate common subspace

The meet sees only vectors satisfying both cutoff constraints exactly:

\[
P_\Lambda x=x,
\qquad
Q_\Lambda x=x.
\]

The prolate bulk consists instead of vectors satisfying the second condition approximately:

\[
P_\Lambda x=x,
\qquad
\|(I-Q_\Lambda)x\|
\ll
\|x\|.
\]

These are spectral vectors of

\[
B_\Lambda
=P_\Lambda Q_\Lambda P_\Lambda
\]

with eigenvalues

\[
\lambda
=1-\varepsilon,

\qquad
\varepsilon
\ll1.
\]

An extensive family of such eigenvalues can generate the full cutoff volume even when

\[
P_{\{1\}}(B_\Lambda)=0.
\]

This is exactly what happens in ordinary compact prolate theory.

## Instability of exact intersections

For the pure translated Hardy pair, one projection range may be nested in the other, producing an infinite exact meet. Multiplication by a nontrivial scattering phase can destroy exact nesting while retaining an extensive almost-common subspace.

Thus

\[
\boxed{
\text{large }P\wedge Q
\]

is not stable under the Tate scattering perturbation, whereas

\[
\boxed{
\text{large near-one spectral mass of }PQP
}
\]

is the robust prolate datum.

The universal volume cannot be assigned solely to the exact meet without proving a special inner-factor theorem for the full Tate symbol.

## Noncommuting limits

At fixed cutoff,

\[
B_\Lambda^m
\xrightarrow[s]{m\to\infty}
P_{\{1\}}(B_\Lambda).
\]

But the asymptotic boundary requires a joint path

\[
m=m(\Lambda)
\]

with

\[
m(\Lambda)\varepsilon_\Lambda
\asymp1.
\]

Taking `m->infinity` first kills every eigenvalue strictly below one, including the entire near-one cloud. Therefore

\[
\boxed{
\lim_{\Lambda\to\infty}
\lim_{m\to\infty}
B_\Lambda^m
\]

is generally not the bulk object selected by

\[
\boxed{
\lim_{
\Lambda\to\infty,
\;m\varepsilon_\Lambda\asymp1
}
B_\Lambda^m.
}
\]

The meet computes the first expression, not the second.

## Source-derived orthogonal bulk projection

To remove bulk orthogonally, choose a threshold scale

\[
\delta_\Lambda
\downarrow0
\]

and define

\[
\boxed{
E_{\Lambda}^{bulk}(\delta_\Lambda)
=
1_{[1-\delta_\Lambda,1]}
(B_\Lambda).
}
\]

This projection contains:

- the exact meet `P_{\{1\}}(B_Lambda)`;
- all near-one modes above the selected concentration threshold.

The physical residual is

\[
\boxed{
R_{\Lambda,\delta}^{in}g
=
[B_\Lambda
(I-E_\Lambda^{bulk}(\delta_\Lambda))]^{1/2}
A_g.
}
\]

Because the spectral projection commutes with `B_Lambda`, this is an exact orthogonal feature split.

## Relation to dyadic depth

The soft bulk filter at depth `n` is

\[
B_\Lambda^{2^n}.
\]

It transitions near

\[
1-\lambda
\asymp
2^{-n}.
\]

Thus the hard threshold and soft dyadic scale correspond through

\[
\boxed{
\delta_\Lambda
\asymp
2^{-n(\Lambda)}.
}
\]

If `epsilon_Lambda` is the relevant extremal or observer-selected near-one gap, the joint rule is

\[
\boxed{
\delta_\Lambda
\asymp
\varepsilon_\Lambda,
\qquad
2^{n(\Lambda)}
\varepsilon_\Lambda
\asymp1.
}
\]

The exact constants must come from the rescaled near-one spectral law, not from functional calculus alone.

## Soft and hard residuals

The dyadic tower supplies the smooth partition

\[
B_\Lambda
=
B_\Lambda^{2^n}
+
\sum_{j=0}^{n-1}
B_\Lambda^{2^j}
(I-B_\Lambda^{2^j}).
\]

At finite depth:

- `B^(2^n)` is the soft bulk;
- the finite defect sum is the soft residual.

The hard spectral projection gives an orthogonal bulk/residual split. Comparison between them follows from scalar filter bounds away from the threshold, but uniform comparison requires control of observer spectral mass in the transition band

\[
1-\lambda
\asymp
\delta_\Lambda.
\]

That transition-band mass is precisely the missing near-one limit theorem.

## Correct role of the meet

The meet remains useful as the exact terminal atom:

\[
\boxed{
E_\Lambda^{meet}
=
\bigcap_{\delta>0}
E_\Lambda^{bulk}(\delta).
}
\]

It must be tracked separately because exact intersection modes survive every dyadic power. But it is only the deepest endpoint of the filtered bulk system.

Hence the correct hierarchy is

\[
\boxed{
\text{near-one bulk projection}
\supseteq
\text{exact meet atom}.
}
\]

## Sonin distinction remains valid

Nothing in this correction changes the exact typing:

\[
P_{\{1\}}(PQP)
=P_{H_{11}},
\]

whereas

\[
P_{\{1\}}((I-P)(I-Q)(I-P))
=P_{H_{00}}.
\]

The meet is not Sonin. The correction is that `H_11` is also not automatically the entire asymptotic inner bulk.

## Absolute-Gram target with threshold

The physically meaningful positive residual Gram is

\[
\boxed{
K_{\Lambda,\delta}(g,h)
=
\operatorname{Tr}
\left(
A_h^*
B_\Lambda
(I-E_\Lambda^{bulk}(\delta_\Lambda))
A_g
\right).
}
\]

The positive `C_34` theorem requires a source-derived scale `delta_Lambda` for which

\[
K_{\Lambda,\delta}
\]

converges, after both polarizations and endpoint handling, to the absolute Tate form

\[
q_{|A_S|}.
\]

Choosing `delta_Lambda` too small leaves volume bulk in the residual. Choosing it too large removes finite boundary mass. The rescaled observer-weighted spectral measure determines the admissible window.

## Corrected status of the one-sided bulk gate

Established:

1. exact meet projection `P meet Q`;
2. exact hard threshold projections by spectral calculus;
3. exact soft dyadic bulk/residual identity;
4. relation `delta approximately 2^(-n)`.

Not established:

1. the source-derived threshold `delta_Lambda`;
2. convergence of transition-band observer mass;
3. equivalence of hard and soft bulk removal in the joint limit;
4. absolute-Gram convergence to `|A_S|`.

## Disposition

The previous statement

\[
E_\Lambda^{bulk}
=P_\Lambda
\wedge
Q_\Lambda
\]

is withdrawn as a description of the full asymptotic bulk. The correct filtered object is

\[
\boxed{
E_\Lambda^{bulk}(\delta_\Lambda)
=
1_{[1-\delta_\Lambda,1]}(B_\Lambda),
}
\]

with the meet retained only as its exact endpoint atom. Determining `delta_Lambda` and the transition-band limit is the unresolved observer-weighted prolate problem.
