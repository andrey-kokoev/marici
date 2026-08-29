# Any zero-trace auxiliary elimination preserves the endpoint lower bound

## Partial auxiliary subspaces

Let \(T:\mathcal H\to E\) be the endpoint trace and let the Green energy satisfy

\[
\mathcal E(f)\ge m\|Tf\|^2
\]

for some \(m>0\).

Let \(N_0\) be any closed authorized auxiliary subspace satisfying

\[
N_0\subseteq\ker T.
\]

Choose an endpoint lift \(L:E\to\mathcal H\) with \(TL=I\). Form the Green block on

\[
L(E)\oplus N_0.
\]

Its Schur complement is

\[
Q_{N_0}(x)
=
\inf_{n\in N_0}
\mathcal E(Lx+n).
\]

Since every \(Lx+n\) has trace \(x\),

\[
Q_{N_0}(x)
\ge
m\|x\|^2.
\]

Thus strict endpoint loading does not require \(N_0=\ker T\). Eliminating fewer interior directions only increases the effective endpoint energy.

## Monotonicity

If

\[
N_0\subseteq N_1\subseteq\ker T,
\]

then

\[
Q_{N_0}\ge Q_{N_1}\ge Q_{\ker T}.
\]

The full harmonic Dirichlet-to-Neumann form is the smallest allowed endpoint Schur complement. Every correctly typed finite auxiliary approximation lies above it.

## Exact typing obstruction

The dangerous case is not failure to exhaust the zero-trace space. It is leakage:

\[
N_0\not\subseteq\ker T.
\]

Then auxiliary variation can alter endpoint data while the Schur minimization treats those data as fixed. The endpoint lower bound may collapse or acquire the wrong reciprocal character.

Therefore the decisive typing theorem is

\[
T\circ J_{\mathrm{aux}}=0,
\]

where \(J_{\mathrm{aux}}\) is the source map from tail/PV coordinates into the full history graph.

## Source-native zero-trace regularization

Given the bounded trace map and harmonic extension \(P_{\min}\), every history has a canonical regular part

\[
f_{\mathrm{reg}}
=
(I-P_{\min}T)f.
\]

It satisfies

\[
Tf_{\mathrm{reg}}=0.
\]

If the source tail/PV feature is defined by this relative subtraction before representation, then the required zero-trace law is exact and source-derived. Subtracting endpoint traces only after Schur formation would be too late.

## Reciprocal and label covariance

The harmonic extension is unique and the Green energy is reflection invariant, so

\[
RP_{\min}=P_{\min}R.
\]

It also acts within each valuation label. Hence the regularization preserves reciprocal parity and prime diagonality.

## Consequence

Endpoint-loading positivity is already robust under finite or incomplete auxiliary realization. The local gate contracts to one identity:

\[
T(I-P_{\min}T)J_{\mathrm{source}}=0.
\]

Once the tail/PV constructor is shown to use this relative regular part, endpoint loading closes uniformly with the source endpoint lower bound.

## Next calculation

Audit the actual tail/PV source formula for pre-representation wall and endpoint subtraction. If it equals the canonical zero-trace regularization, the entire enlarged first Adams cell is locally coercive on compact off-seam sets.
