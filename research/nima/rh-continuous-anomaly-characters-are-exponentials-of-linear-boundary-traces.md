# Continuous anomaly characters are exponentials of linear boundary traces

This theorem is conditional on an individual scalar-valued continuous
character existing. The native theta primitive and square currents do not
separately admit the undamped critical-boundary readout. Their actual
totalization may exist only as a joint relative character after archimedean
sewing. The theorem therefore classifies any proposed factorization; it does
not assert that theta supplies one.

## Character linearization

Let \(V\) be a real locally convex topological vector space under addition,
and let

\[
\chi:V\longrightarrow\mathbb C^\times
\]

be a normalized continuous character. Since \(V\) is contractible, \(\chi\)
has a continuous logarithmic lift \(\ell\) with \(\ell(0)=0\). Multiplicativity
gives

\[
\ell(x+y)-\ell(x)-\ell(y)\in2\pi i\mathbb Z.
\]

The left side is continuous on the connected space \(V\times V\) and vanishes
at the origin. It therefore vanishes everywhere. Consequently \(\ell\) is
continuous and additive, hence real-linear:

\[
\chi(x)=\exp(\ell(x)).
\]

If the carrier and character are holomorphic, \(\ell\) is complex-linear.

## Collapse of the missing constructor

The two anomaly characters required by global determinant totalization are
therefore controlled by two continuous linear boundary traces:

\[
\chi_1(P)=\exp(\ell_1(P)),
\qquad
\chi_2(Q)=\exp(\ell_2(Q)).
\]

This does not construct the traces. It reduces the search from arbitrary
multiplicative regularizations to source-derived continuous linear
functionals on two separately typed boundary carriers.

The primitive and square currents already give finite-cutoff candidates for
their differentials. The remaining questions are whether those candidates
extend continuously through their respective riggings and whether the
extensions are natural under cutoff refinement.

If finite labelled packets form a dense source subspace, any continuous
extension is unique. Two continuous traces agreeing on that subspace have a
continuous difference vanishing on a dense set, hence vanish everywhere.
After the carrier and dense source domain are fixed, the problem is existence
of the extension rather than freedom to select one.

## Reciprocal dagger law

Suppose reciprocal sewing acts by a continuous real-linear map \(R\), and the
determinant-line involution requires

\[
\chi(Rx)=\overline{\chi(x)}.
\]

The normalized logarithmic lift removes the integral branch ambiguity and
forces

\[
\ell(Rx)=\overline{\ell(x)}.
\]

Thus reciprocal compatibility can be checked infinitesimally on the linear
boundary trace. There is no need to compare full exponentials first.

## Hostile alternatives

A quadratic logarithm can agree with a linear character on selected packets
but fails additivity because of its polarization cross term. A discontinuous
additive functional is algebraically multiplicative after exponentiation but
does not descend through the declared completion. Both are excluded by the
same constructor signature: continuous linearity before exponentiation.

## New finite gate

For each typed anomaly carrier, compute the finite-cutoff boundary functional
and verify:

1. additivity on independently supported packets;
2. cutoff-refinement naturality;
3. reciprocal dagger intertwining;
4. one fixed continuity domination bound in the declared carrier topology.

Passing the first three gates produces a pro-linear trace. The fourth gate is
what makes its exponential a completed anomaly character.

## DPC verdict

The missing anomaly characters contain no extra nonlinear freedom once
continuity and source composition are imposed. The unresolved RH datum is a
pair of continuous source-linear boundary traces with naturality and dagger
compatibility. On dense finite source packets, such extensions are unique if
they exist.

## Verification

`check_rh_anomaly_character_linearization.py` verifies exact additive
linearization, direct-sum composition, reciprocal conjugation, and the
quadratic polarization falsifier.
