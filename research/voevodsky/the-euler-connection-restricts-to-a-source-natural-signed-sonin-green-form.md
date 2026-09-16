# The Euler connection restricts to a source-natural signed Sonin Green form

## Objective

Advance the open signed Green map from the stable semilocal Sonin carrier to
the gamma--prime boundary current.

## Ambient connection is already constructed

For a finite place set \(S\), the weighted Sonin carrier has unitary prime
successors

\[
U_{S,q}f=m_qf,
\qquad
m_q(s)=1-q^{-1/2-is}.
\]

On a common smooth core, with \(D=-i\partial_s\),

\[
U_{S,q}^{-1}DU_{S,q}=D+a_q,
\]

where

\[
a_q(s)=-i\partial_s\log m_q(s)
=(\log q)\sum_{r\ge1}q^{-r/2}e^{-irs\log q}.
\]

The primal/contragredient sum is the real prime-power Weil current. Including
the archimedean gamma phase gives the real multiplication operator

\[
V_{loc,S}
=\frac1{2i}\partial_s\log J_{loc,S}.
\]

Thus the ambient signed current is not missing: it is the metric connection of
the dual/canonical pairing.

## Restriction to the Sonin carrier

Let

\[
i_S:\mathcal S_S\hookrightarrow\mathcal H_S
\]

be the source Sonin inclusion and let \(P_S=i_Si_S^*\). On the dense domain

\[
\mathcal D_S^{Son}
=\mathcal S_S\cap D(|V_{loc,S}|^{1/2}),
\]

define the pulled-back signed form

\[
\boxed{
\mathfrak g_S(f,g)
=
\langle i_Sf,V_{loc,S}i_Sg\rangle_{
\mathcal H_S}.}
\]

Equivalently, at the formal operator level this is the compression

\[
G_S^{Son}=i_S^*V_{loc,S}i_S=P_SV_{loc,S}P_S|_{\mathcal S_S}.
\]

This supplies a canonical source-typed map from the Sonin carrier to the signed
Weil-current form. No fitted scalar, endpoint identification, or positive
Sonin trace is introduced.

## Green identity

The semilocal bilinear pairing satisfies

\[
B_{J_S}((D+V_S)f,g)
+B_{J_S}(f,(D+V_S)g)=0
\]

on the boundary-vanishing core. On a finite contour interval the exact boundary
term is

\[
-i[f(s)g(s)J_S(s)]_{-T}^{T}.
\]

Restricting \(f,g\) to the Sonin core therefore gives a Green identity whose
interior current is precisely \(\mathfrak g_S\). After admissible contour
displacement, the same logarithmic differential carries the endpoint residues
at \(\pm i/2\). Hence Sonin current and endpoint terms are pieces of one
reflected logarithmic differential, not unrelated channels.

## Prime-successor naturality

Adjoining \(q\) gives

\[
V_{loc,S\cup\{q\}}=V_{loc,S}+V_q
\]

and the Sonin transition \(U_{S,q}\). For transported vectors,

\[
\begin{aligned}
\mathfrak g_{S\cup\{q\}}(U_{S,q}f,U_{S,q}g)
&=
\langle U_{S,q}f,
(V_{loc,S}+V_q)U_{S,q}g\rangle.
\end{aligned}
\]

Using unitarity, this is the old form plus the connection increment pulled back
to the old carrier. In connection notation,

\[
\boxed{
U_{S,q}^{-1}(D+V_{loc,S\cup\{q\}})U_{S,q}
=D+V_{loc,S}}
\]

with the sign convention fixed by the chosen primal/canonical orientation.
Equivalently, if the opposite convention is used, the same equation holds
with all connection signs reversed. This is the naturality law: the current
alone transforms affinely, while the covariant derivative transforms by
conjugation.

Because scalar Euler multipliers commute, adding primes in either order gives
zero discrete curvature. The signed Sonin Green forms therefore constitute a
flat source-authorized connection over the finite-place tower.

## What remains open

The pullback form does not prove that the Sonin projection reduces the
unbounded connection operator. In general

\[
[P_S,V_{loc,S}]\ne0.
\]

Therefore three stronger statements remain separate:

1. closability/self-adjointness of the compressed form on the completed Sonin
   domain;
2. a positive compressed-trace identity for this form;
3. equality of its contour boundary term with the independently constructed
   completed endpoint Green bundle, including all domain limits.

The first is an operator-domain problem; the second is the RH-strength
positivity problem; the third is the mixed coupling from residual channel 4.
None follows merely from the flat connection identity.

## Status change

“Sonin signed Green map open” is too broad. The correct status is:

- ambient logarithmic connection: constructed;
- pullback signed Green form on the common Sonin form core: constructed;
- prime-successor connection naturality: exact and flat;
- closed compressed operator and positive trace realization: open;
- completed endpoint boundary identification: open.

## Verdict

\[
\boxed{
\text{The source-natural signed Sonin Green form exists on the common form
core.}}
\]

The next nonredundant channel-3 task is a closability/reducing-domain theorem
for \(P_SV_{loc,S}P_S\), not construction of the prime current itself.

## Repository dependencies

- `the-euler-contratower-commutator-constructs-the-full-prime-power-weil-current.md`
- `differentiating-the-semilocal-dual-canonical-pairing-produces-the-prime-current-as-its-metric-connection.md`
- `a-single-reflected-logarithmic-contour-differential-unifies-the-local-weil-current-and-endpoint-residues.md`
- `connes-local-theorem-lifts-every-local-weil-distribution-to-the-affiliated-logarithmic-module-operator.md`
- `semilocal-sonin-amplification-is-isometric-but-only-multiplies-by-local-euler-factors.md`
