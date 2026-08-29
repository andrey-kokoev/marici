# The killed wall survives as the Wronskian boundary class of completion

## Completion operator and kernel covector

Let

\[
\mathcal C
=
\partial_u^2-\frac14
=
\left(
\partial_u-\frac12
\right)
\left(
\partial_u+\frac12
\right).
\]

The growing wall

\[
w_+(u)=e^{u/2}
\]

and reciprocal decaying mode

\[
w_-(u)=e^{-u/2}
\]

both satisfy

\[
\mathcal Cw_\pm=0.
\]

Although completion kills the wall in the bulk, the decaying kernel mode supplies a canonical Wronskian covector.

Define

\[
\mathcal B_-(f;u)
=
W(f,w_-)(u)
=
f'(u)w_-(u)-f(u)w_-'(u).
\]

Explicitly,

\[
\mathcal B_-(f;u)
=
e^{-u/2}
\left(
f'(u)+\frac12f(u)
\right).
\]

For the wall \(f=a e^{u/2}\),

\[
\mathcal B_-(f;u)=a.
\]

Thus \(\mathcal B_-\) reads the growing-wall coefficient exactly.

## Relative Green identity

The Lagrange identity gives

\[
\partial_uW(f,g)
=
(\mathcal Cf)g-f(\mathcal Cg).
\]

Taking \(g=w_-\) yields

\[
\partial_u\mathcal B_-(f;u)
=
e^{-u/2}\mathcal Cf(u).
\]

Therefore, on an interval \([a,b]\),

\[
\mathcal B_-(f;b)
-
\mathcal B_-(f;a)
=
\int_a^b
e^{-u/2}\mathcal Cf(u)\,du.
\]

For the theta precursor \(h\) with \(\mathcal Ch=\Phi\),

\[
\mathcal B_-(h;b)
-
\mathcal B_-(h;a)
=
\int_a^b
e^{-u/2}\Phi(u)\,du.
\]

This is the missing relative connecting morphism: completed bulk forcing measures the change of the precursor wall coefficient through a Wronskian boundary port.

## Meaning for the mapping cone

The wall does not map into the completed bulk. Instead, it is detected by the boundary class

\[
[f]\longmapsto
\mathcal B_-(f;\partial).
\]

The relative completion packet is therefore

\[
\left(
\mathcal Cf,
\mathcal B_-(f;a),
\mathcal B_-(f;b)
\right),
\]

not merely \(\mathcal Cf\).

This packet is faithful to the killed wall because adding \(a_0w_+\) leaves the bulk unchanged but shifts both boundary values by \(a_0\).

## Reciprocal port

Using \(w_+\) as the kernel covector gives the complementary trace

\[
\mathcal B_+(f;u)
=
W(f,w_+)(u)
=
e^{u/2}
\left(
f'(u)-\frac12f(u)
\right),
\]

with

\[
\partial_u\mathcal B_+(f;u)
=
e^{u/2}\mathcal Cf(u).
\]

The two traces are reciprocal Mellin-weighted boundary ports. Reflection \(u\mapsto-u\) exchanges them up to the oriented Wronskian sign.

Thus the relative carrier naturally has two sheet traces, not one inserted identity.

## Consequence for auxiliary positivity

Any effective wall energy in the completed Schur block must come from the Gram of these boundary traces or from their connecting map. A candidate relative energy is schematically

\[
\|\mathcal Cf\|^2
+
|\mathcal B_-(f;\partial)|^2
+
|\mathcal B_+(f;\partial)|^2,
\]

with source-determined endpoint choices and coefficients.

Only after eliminating precursor variables may this produce an identity-like term on completed history. The coefficient is fixed by the trace normalization, not chosen as \(\lambda=1\).

## Exact hostiles

1. Two precursors differ by \(aw_+\). Their completed bulk histories are identical, but their relative wall traces differ.
2. Retaining only one Wronskian port loses the reciprocal kernel mode or breaks reflection typing.
3. An endpoint limit is taken where \(e^{u/2}\Phi(u)\) is not integrable; the corresponding trace requires a rigged or renormalized interpretation.
4. The wall trace is squared before proving its endpoint limit exists on the closed precursor domain.

## Next theorem

Freeze the precursor interval and admissible asymptotics, then prove the trace map

\[
f
\longmapsto
\left(
\mathcal Cf,
\mathcal B_-(f;\partial),
\mathcal B_+(f;\partial)
\right)
\]

is closed and has the required reciprocal reflection law. After that, form its complete Gram and compute the Schur return onto the completed causal-history carrier.

This is the first source-derived route by which the killed wall can legitimately re-enter auxiliary energy.
