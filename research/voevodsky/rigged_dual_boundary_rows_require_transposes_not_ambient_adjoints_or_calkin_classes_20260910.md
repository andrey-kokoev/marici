# Rigged-dual boundary rows require transposes, not ambient adjoints or Calkin classes

## Question

How should distributional boundary rows, Green identities, Real comparison, and stable graph observation be typed when boundary evaluation is not bounded on the ambient Hilbert space?

## Claim boundary

This packet gives a rigged-dual typing theorem and identifies the precise conditions under which a boundary transpose can also be represented by a graph-Hilbert adjoint. It does not assign a Hilbert adjoint or Calkin class to an ambient-unbounded trace. It does not prove a nuclear spectral theorem or construct a sector-specific test space.

## Rigged setup

Let

\[
\Phi\hookrightarrow H\hookrightarrow\Phi'
\]

be a rigged Hilbert triple. The first inclusion is continuous and dense, and \(H\) is embedded in the continuous dual \(\Phi'\) by the Hilbert pairing. The topology on \(\Phi\) is part of the datum.

Let \(D\) be a closed operator on \(H\), with graph Hilbert space

\[
\mathcal E_D=(\operatorname{Dom}D,\|\cdot\|_D).
\]

Choose a test-domain rung \(\Phi_D\) with continuous dense maps

\[
\Phi_D\hookrightarrow\mathcal E_D\hookrightarrow H\hookrightarrow\mathcal E_D'\hookrightarrow\Phi_D'.
\]

The duals here are continuous anti-duals or duals according to one fixed pairing convention; that convention may not change inside a formula.

Let \(B\) be a boundary space with its own topology and dual \(B'\).

## Four distinct boundary constructors

### Test-space trace

A boundary trace is first a continuous map

\[
\gamma:\Phi_D\to B.
\]

This map need not extend continuously to \(H\), or even to \(\mathcal E_D\).

### Continuous transpose

The transpose is always defined at the declared locally convex level:

\[
\gamma':B'\to\Phi_D',
\]

by

\[
\langle\gamma'\beta,\varphi\rangle_{
\Phi_D',\Phi_D}
=
\langle\beta,\gamma\varphi\rangle_{B',B}.
\]

This is the correct constructor for boundary distributions. For point evaluation, \(\gamma'\beta\) may be a delta-type functional in \(\Phi_D'\) with no representative in \(H\).

### Graph-Hilbert adjoint

If and only if the trace extends to a bounded map

\[
\gamma_D:\mathcal E_D\to B_H
\]

for a Hilbert realization \(B_H\) of the boundary space, it has a graph adjoint

\[
\gamma_D^{*D}:B_H\to\mathcal E_D.
\]

The Riesz embeddings \(R_D:\mathcal E_D\to\mathcal E_D'\) and \(R_B:B_H\to B_H'\) relate transpose and graph adjoint by

\[
\gamma_D'\,R_B
=
R_D\,\gamma_D^{*D}.
\]

This identity depends on both metric realizations. It does not identify \(\gamma'\beta\in\Phi_D'\) with an ambient vector in \(H\).

### Ambient adjoint

An ambient Hilbert adjoint \(\gamma_H^*\) exists only if \(\gamma\) extends boundedly as

\[
\gamma_H:H\to B_H.
\]

Ordinary boundary evaluation on \(L^2\) has no such extension. Writing \(\gamma_H^*\) in that setting is a type error.

## Green identity as a dual-pairing statement

Let \(D^\times\) denote the formal or distributional transpose on the chosen test rung. A Green identity has the typed form

\[
\langle D\varphi,\psi\rangle_H
-
\langle\varphi,D^\times\psi\rangle_H
=
\langle J_B\gamma\varphi,\gamma^\sharp\psi\rangle_{B',B},
\]

for test vectors in declared domains. The second trace \(\gamma^\sharp\) and the boundary operator \(J_B:B\to B'\) are part of the Green datum.

This identity produces boundary functionals through \(\gamma'J_B\gamma^\sharp\). It does not turn those functionals into bounded ambient observers.

## Real comparison on the rigged ladder

Let \(R_H:H\to H\) be an antiunitary involution. Real compatibility requires separately:

1. \(R_H\Phi_D=\Phi_D\) continuously;
2. an induced dual involution \(R_{\Phi'}\) on \(\Phi_D'\);
3. a boundary involution \(R_B:B\to B\);
4. trace naturality

   \[
   \gamma R_H=R_B\gamma;
   \]

5. transpose naturality

   \[
   R_{\Phi'}\gamma'=\gamma'R_{B'}.
   \]

The transpose relation follows from the trace relation only after the dual pairing conventions and induced dual actions have been fixed. Antilinearity prevents treating it as an untyped matrix transpose.

## Comparison between rigged systems

For systems \((\Phi_D,H,\Phi_D')\) and \((\widetilde\Phi_{\widetilde D},\widetilde H,
\widetilde\Phi_{\widetilde D}')\), a comparison requires a ladder

\[
C_\Phi:\Phi_D\to\widetilde\Phi_{\widetilde D},
\qquad
C_H:H\to\widetilde H,
\qquad
C_{\Phi'}:\Phi_D'\to\widetilde\Phi_{\widetilde D}'.
\]

The maps must agree on inclusions and dual pairings. Boundary comparison additionally requires \(C_B:B\to\widetilde B\) with

\[
\widetilde\gamma C_\Phi=C_B\gamma.
\]

A boundedly invertible ambient map \(C_H\) does not automatically induce continuous invertible maps on \(\Phi_D\) or \(\Phi_D'\). Rigged comparison is therefore a three-rung constructor, not an ambient comparison decorated with notation.

## Calkin eligibility gate

The Calkin algebra applies to bounded endomorphisms of a Hilbert rung, modulo compact endomorphisms of that same rung. Consequently:

- a bounded graph observer \(Q:\mathcal E_D\to Z\) has graph Gramian \(Q^{*D}Q\in B(\mathcal E_D)\), hence a graph Calkin class;
- a finite-dimensional graph-bounded trace \(\gamma_D:\mathcal E_D\to B_H\) has finite-rank Gramian and zero graph Calkin class;
- a test-space trace \(\gamma:\Phi_D\to B\) has no Calkin class merely from continuity on \(\Phi_D\);
- a boundary distribution \(\gamma'\beta\in\Phi_D'\) has no Hilbert Calkin class merely from membership in the dual;
- an ambient-unbounded trace has no ambient Gramian \(\gamma_H^*\gamma_H\) in \(B(H)\).

Any essential-observability claim must first exhibit a bounded observer on the declared Hilbert or graph Hilbert source.

## Finite boundary rows and bulk stability

Suppose \(B_H\) is finite dimensional and \(\gamma_D:\mathcal E_D\to B_H\) is bounded. Then \(\gamma_D\) is finite rank. For infinite-dimensional \(\mathcal E_D\), it cannot supply a positive essential Calkin margin.

It may still:

- define a closed operator domain;
- encode Green compatibility;
- separate a finite residual kernel;
- serve as finite-defect repair.

These roles do not promote it to an essential bulk observer.

## Half-line example

Take

\[
H=L^2(0,\infty),
\qquad
\mathcal E_D=H^1(0,\infty),
\]

for the weak derivative graph norm. Endpoint evaluation

\[
\gamma f=f(0)
\]

is bounded on \(H^1\) but unbounded on \(L^2\).

Therefore:

- \(\gamma_D^{*D}:\mathbb C\to H^1\) exists;
- \(\gamma_H^*:\mathbb C\to L^2\) does not exist as the adjoint of a bounded ambient trace;
- the transpose of endpoint evaluation is the boundary delta in a test-space dual;
- the graph Gramian \(\gamma_D^{*D}\gamma_D\) is rank one and has zero Calkin class;
- derivative plus endpoint trace still fails to control broad half-line packets.

A thick bulk multiplier repairs the last failure on the graph rung. The boundary delta does not.

## Constructor-role table

| Symbol | Source and target | Role | Calkin eligible? |
|---|---|---|---|
| \(\gamma\) | \(\Phi_D\to B\) | test-space boundary trace | no |
| \(\gamma'\) | \(B'\to\Phi_D'\) | distributional transpose | no |
| \(\gamma_D\) | \(\mathcal E_D\to B_H\) | graph-bounded trace | Gramian only |
| \(\gamma_D^{*D}\) | \(B_H\to\mathcal E_D\) | graph adjoint | participates in graph Gramian |
| \(\gamma_H\) | \(H\to B_H\) | ambient trace, if bounded | Gramian only |
| \(\gamma_H^*\) | \(B_H\to H\) | ambient adjoint, if defined | participates in ambient Gramian |
| \(\gamma'\beta\) | element of \(\Phi_D'\) | boundary distribution | no |

## Deliberate failures

1. Writing \(\gamma_H^*\) for endpoint evaluation on \(L^2\) fails boundedness at the source.
2. Identifying \(\gamma'\) with \(\gamma_D^{*D}\) omits both Riesz maps.
3. Assigning a Calkin class to \(\gamma'\beta\) mistakes a dual element for a bounded Hilbert endomorphism.
4. Treating ambient invertibility as rigged-ladder invertibility omits test and dual continuity.
5. Treating finite graph-bounded trace as an essential observer contradicts its zero Calkin class.

## Disposition

Rigged boundary calculus is compatible with the programme once transpose, graph adjoint, ambient adjoint, and boundary distribution are treated as four different constructors. Green and Real identities live on declared pairings and ladders. Essential observation remains a Hilbert- or graph-Hilbert Gramian property and cannot be assigned to an ambient-unbounded trace or a distributional boundary row.
