# The Sonin Green form is closed in the absolute-connection graph norm

## Objective

Close the form-domain part of the signed Sonin Green map without assuming that
the Sonin projection reduces the unbounded Tate connection.

## Global absolute connection form

Let

\[
V_S=V_{loc,S}
\]

be the self-adjoint real multiplication operator representing the gamma--prime
logarithmic connection on \(\mathcal H_S\). Its absolute quadratic form

\[
q_S(f,g)
=
\langle |V_S|^{1/2}f,|V_S|^{1/2}g\rangle
\]

has domain

\[
\mathcal Q_S=D(|V_S|^{1/2})
\]

and is closed. Equip it with graph inner product

\[
\langle f,g\rangle_{Q_S}
=
\langle f,g\rangle+q_S(f,g).
\]

## Sonin restriction

Let \(i_S:\mathcal S_S\hookrightarrow\mathcal H_S\) be the closed semilocal
Sonin carrier and define

\[
\mathcal Q_S^{Son}
=
\mathcal S_S\cap\mathcal Q_S.
\]

Use the closure of the source Sonin Schwartz core in the absolute graph norm if
necessary. Then \(\mathcal Q_S^{Son}\) is a closed subspace of
\((\mathcal Q_S,\|\cdot\|_{Q_S})\): convergence in graph norm implies
convergence in \(\mathcal H_S\), and closedness of \(\mathcal S_S\) keeps the
limit in the Sonin carrier.

The source Sonin realization consists of rapidly controlled entire/Schwartz
vectors, while the finite-place current is bounded and the archimedean gamma
connection has only logarithmic growth. Hence the recorded source Sonin core
lies in \(\mathcal Q_S\) and is dense in the declared Sonin graph completion.

## Signed form

Let

\[
\operatorname{sgn}(V_S)
\]

be the bounded spectral sign. Define

\[
\mathfrak g_S(f,g)
=
\langle |V_S|^{1/2}f,
\operatorname{sgn}(V_S)|V_S|^{1/2}g\rangle,
\qquad
f,g\in\mathcal Q_S^{Son}.
\]

This equals \(\langle f,V_Sg\rangle\) on the operator core, but remains
well-defined on the larger form domain. Cauchy--Schwarz gives

\[
|\mathfrak g_S(f,g)|
\leq q_S(f,f)^{1/2}q_S(g,g)^{1/2}.
\]

Thus \(\mathfrak g_S\) is continuous on the complete Sonin graph Hilbert space.
In particular it is a closed/closable signed form in the precise rigged sense
needed for the helical presentation.

## Why no reducing projection is needed

The operator compression

\[
P_SV_SP_S
\]

need not be self-adjoint on \(\mathcal S_S\), because \([P_S,V_S]\) may be
nonzero. The form restriction does not require invariance of
\(D(V_S)\) under \(P_S\). It uses only the closed absolute form and intersection
with the closed Sonin carrier.

Accordingly, failure of a reducing-subspace theorem blocks a self-adjoint
compressed operator, but it does not block the signed Green form.

## Prime-successor transport

The unitary Euler transition \(U_{S,q}\) identifies the Sonin carriers. Pull
back the next-stage absolute graph norm along this unitary. The covariant
connection law identifies the signed forms after including the affine
connection increment. Therefore the transition is bicontinuous between the
object-indexed graph domains

\[
(\mathcal Q_S^{Son},\|\cdot\|_{Q_S})
\longrightarrow
(\mathcal Q_{S\cup\{q\}}^{Son},\|\cdot\|_{Q_{S\cup\{q\}}}),
\]

when these domains are regarded as the metric bundle determined by the
connection. Uniform equivalence to one fixed graph norm is neither required nor
claimed.

## Remaining strength

This closes existence, continuity, and form-level successor transport. It does
not prove:

1. self-adjointness of the literal operator compression;
2. positivity of \(\mathfrak g_S\);
3. trace-class compression against the Sonin projection;
4. equality of the Green boundary term with the completed endpoint bundle;
5. uniform coercivity over an unbounded place tower.

The signed Weil form is expected to be indefinite before the RH-strength gate,
so item 2 must not be silently imposed.

## Updated channel-3 status

\[
\boxed{
\text{stable Sonin carrier + natural signed closed Green form: constructed}.}
\]

The next genuine channel-3 question is whether the form's boundary trace equals
the independently constructed endpoint Green form, not whether the restricted
form exists.

## Repository dependencies

- `the-euler-connection-restricts-to-a-source-natural-signed-sonin-green-form.md`
- `the-semilocal-tate-logarithmic-derivative-is-a-global-self-adjoint-multiplication-operator-with-compatible-positive-boundary-legs.md`
- `semilocal-sonin-amplification-is-isometric-but-only-multiplies-by-local-euler-factors.md`
