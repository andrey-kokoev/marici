# 3857 — The Two Active Walls Must Be Sewn at Their Common Endpoint

## Obstruction found during finite-remainder integration

Entry 3855 fixed the principal Laurent jet at each interior conductor. Attempting to integrate the remaining wall forms separately exposes another singularity: both active segments begin at

\[
q_{g_1}=q_{g_2}=0,
\qquad
a=x+z,
\qquad
b=y+z.
\]

At this common endpoint, the Cayley–Menger square root is

\[
\sqrt K
=
(-x+y+z)(x-y+z)(x+y+z),
\]

which is nonzero in the strict triangle chamber. Therefore the analytic continuation

\[
K^{-1/2}\longmapsto K^{-1/2+\epsilon}
\]

does not regulate this marked-wall endpoint pole.

## Exact endpoint residues

Using the source wall orientations, the two residues are

\[
\rho_{g_1}
=
-\frac{2z}
{(x-y-z)^2(x-y+z)^2(x+y+z)(x+y+3z)},
\]

\[
\rho_{g_2}
=
\frac{2z}
{(x-y-z)^2(x-y+z)^2(x+y+z)(x+y+3z)}.
\]

Hence

\[
\rho_{g_1}+\rho_{g_2}=0.
\]

At ((x,y,z)=(2,3,4)),

\[
\rho_{g_1}=-\frac8{34425},
\qquad
\rho_{g_2}=\frac8{34425}.
\]

## Result

The individual full wall finite parts do not exist under dimensional continuation alone. Their common endpoint logarithms cancel only after the two source-oriented walls are sewn.

This is a concrete distinction between two types of singular data:

- interior conductor poles are regulated by the (K^{-1/2+\epsilon}) analytic family and retain separate Laurent costalks;
- the shared marked-wall endpoint is not regulated by (K), but cancels through source Čech sewing.

Thus neither “everything is an analytic-regulator problem” nor “everything cancels by sewing” is correct. The source uses both mechanisms on differently typed strata.

## Classification

- common endpoint: existing (g_1\cap g_2) Carrier corner;
- endpoint cancellation: source incidence/Čech calculus;
- conductor Laurent jets: coefficient data;
- independent full wall periods: mistyped;
- new Carrier datum: none.

## Durable artifacts

- `research/benincasa/checkers/check_rank26_active_wall_endpoint_sewing.py`
- `research/benincasa/results/rank26-active-wall-endpoint-sewing.json`

The checker passes six exact gates.

## Next falsifier

Form the sewn two-wall integrand first, cancel its common endpoint pole algebraically, and only then perform conductor singular subtraction. Test whether the resulting finite analytic continuation is unique and whether its two interior residue coefficients remain independent.
