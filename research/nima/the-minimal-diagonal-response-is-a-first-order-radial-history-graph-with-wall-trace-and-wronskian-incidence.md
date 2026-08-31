# The minimal diagonal response is a first-order radial history graph with wall trace and Wronskian incidence

## Question

What is the smallest graph that attaches the completed-theta radial state to
wall and linking data without scalarizing its separation dependence?

## Claim boundary

The exact radial Stokes identity defines a first-order history graph whose
state is the shell autocorrelation, whose wall coordinate is its value at zero,
and whose incidence is the function-valued Wronskian current. This graph is a
closed subgraph of the existing translation history carrier on the rapid
source core. It supplies the correct boundary architecture but not the final
G4 arithmetic loading or codiagonal.

## Radial state and source terms

For one theta label and shell, write

\[
 \rho(t)=\int_a^b\Phi(u)\Phi(u+t)\,du,
\]

\[
 e(t)=\frac12\left[
 \Phi(b)\Phi(b+t)-\Phi(a)\Phi(a+t)
 \right],
\]

and

\[
 w(t)=\int_a^b
 \left[
 \Phi'(u)\Phi(u+t)-\Phi(u)\Phi'(u+t)
 \right]du.
\]

The exact source equation is

\[
 D_t\rho=e-\frac12w.
\]

## Graph definition

Let \(\mathcal H_{\rm rad}\) be the rapid translation-cyclic module generated
by \(\Phi\) and \(\Phi'\). Define

\[
 \mathcal G_{\rm rad}
 =\left\{
 (\rho,e,w,\gamma_0\rho):
 \rho,e,w\in\mathcal H_{\rm rad},
 \ D_t\rho=e-\frac12w,
 \ \gamma_0\rho=\rho(0)
 \right\}.
\]

Use the graph norm

\[
 \|\rho\|_{H^1}^2
 +\|e\|_2^2
 +\|w\|_2^2
 +|\rho(0)|^2.
\]

All shell sections belong to this graph because completed-theta translation
orbits are smooth and rapidly decaying.

## Closedness

The derivative

\[
 D_t:H^1(\mathbb R_+)\to L^2(\mathbb R_+)
\]

is closed, and the trace

\[
 \gamma_0:H^1(\mathbb R_+)\to\mathbb C
\]

is continuous. Therefore the constraint

\[
 D_t\rho-e+\frac12w=0
\]

defines a closed subspace of the product graph. No limiting-absorption or
output-only completion is needed.

## Boundary and incidence typing

The graph contains two distinct kinds of data:

- scalar wall trace \(\gamma_0\rho=\rho(0)\);
- function-valued incidence \(w\in\mathcal H_{\rm rad}\).

The existing scalar incidence coordinate may be obtained only after a declared
continuous readout of \(w\), such as a Laplace probe. It cannot replace \(w\)
before the parameter-jet family is formed.

At zero separation,

\[
 w(0)=0,
\]

but

\[
 \rho'(0)=e(0)
 =\frac12\left[\Phi(b)^2-\Phi(a)^2\right].
\]

Thus using the vanishing Wronskian trace as the sole wall coordinate would
lose the nonzero radial boundary flux.

## Laplace boundary relation

For

\[
 R(z)=\int_0^\infty e^{-zt}\rho(t)\,dt,
\]

\[
 E(z)=\int_0^\infty e^{-zt}e(t)\,dt,
 \qquad
 W(z)=\int_0^\infty e^{-zt}w(t)\,dt,
\]

the graph equation becomes

\[
 zR(z)-\rho(0)=E(z)-\frac12W(z).
\]

Every parameter jet is a continuous probe on the rapid radial source. This is
the correct scalarization stage.

## Shell concatenation

Each coordinate is additive under adjacent-shell composition:

\[
 (\rho,e,w)_{[a,c]}
 =(\rho,e,w)_{[a,b]}+(\rho,e,w)_{[b,c]}.
\]

The intermediate endpoint cancels in \(e\), so the graph equation is
cutoff-natural.

## Relation to the retained wall/incidence port

The scalar G4 linking form can occur as a boundary compression of
\(\mathcal G_{\rm rad}\) only after declaring a map

\[
 \Pi_{p,z}:
 (\rho,e,w,\rho(0))
 \longmapsto
 (\gamma_0,\eta)_{p,z}
\]

that preserves the Laplace identity, analytic-transpose sign, and source
arithmetic coefficient. A \(z\)-dependent probe family may represent the
entire section, but one fixed two-scalar map cannot.

## Hostile

Any attachment fails if it:

- uses \(w(0)=0\) to declare the diagonal response zero;
- replaces function-valued \(w\) by one scalar before forming all jets;
- omits \(\rho(0)\) or the endpoint state \(e\);
- breaks shell concatenation at the intermediate endpoint.

## Disposition

The minimal diagonal response graph is now explicit and closed. It uses only
the existing translation-history carrier plus one wall trace and the
source-forced Wronskian incidence. Candidate one remains open at the arithmetic
probe family \(\Pi_{p,z}\) and its identification with the canonical G4
conservative-complex boundary. No RH conclusion is authorized.
