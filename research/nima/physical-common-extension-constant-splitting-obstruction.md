# The typed common localization extension has no constant invariant lift

The common five-mark localization presentation gives the source-derived
horizontal sequence

\[
0\longrightarrow F_{25}\longrightarrow H_{26}
\longrightarrow T_{\rm top}\longrightarrow0,
\]

where \(F_{25}=F_{23}+F_{31}\) and \(T_{\rm top}\) is the two-mark Kato
line. Unlike the withdrawn branch-to-union construction, all three terms and
both arrows are defined inside one presentation before taking homology.

In a basis adapted to \(F_{25}\subset H_{26}\), each of the two computed
connection matrices has block form

\[
A_\mu=
\begin{pmatrix}
A_{F,\mu}&0\\
C_\mu&\alpha_\mu
\end{pmatrix},
\qquad \operatorname{rank}C_\mu=1.
\]

A simultaneous constant invariant lift of the quotient generator would be a
vector \(e+h\), \(h\in F_{25}\), satisfying

\[
(A_{F,\mu}-\alpha_\mu)h=-C_\mu
\]

for both parameter directions. The combined system has 25 unknowns and 50
equations. At two independent primes its ranks are

\[
\boxed{
\operatorname{rank}M=25,
\qquad
\operatorname{rank}[M\mid b]=26.
}
\]

Thus no simultaneous constant invariant lift exists in either replication.
This is the first nonzero extension-channel result obtained after repairing
the source typing.

## Scope

This does **not** prove that the differential-module extension is globally
nonsplit. A parameter-dependent rational gauge \(h\) obeys

\[
\nabla_Fh-\alpha h=-C,
\]

which includes derivatives of \(h\). The present result excludes only a
constant-frame splitting at the sampled finite-field fibers. It also does not
activate the quotient physically: the literal source and its first
derivatives remain in \(F_{25}\).

## Next falsifier

Derive denominator and degree bounds from the source connection and solve the
rational gauge equation without choosing a primitive section. If it is
solvable, the extension class vanishes despite the constant obstruction. If
it is not, certify the resulting differential-module class and only then
inspect its intrinsic support for \(\mathcal Q\).

## Required input boundary

The present reducer constructs the rank-26 presentation and its two
connection matrices at a frozen finite-field kinematic fiber. It does not
export a parameter-dependent basis and connection over
\(\mathbb Q(x,y)\). Pointwise matrices cannot certify the derivative term in
the rational gauge equation. The older rank-21 proper-top extension packet is
not a substitute: it uses minimum pole level one and has dimensions
\(20\subset21\), whereas the common localization filtration here retains pole
levels zero and has dimensions \(25\subset26\).

Therefore the next implementation prerequisite is a source-labelled symbolic
or reconstructible family for the rank-26 adapted connection, with basis
transition certificates across samples. Only then is a bounded rational
ansatz or differential-cohomology calculation typed.

## Verification

- `research/nima/checkers/check_physical_common_extension_splitting.py`
- `research/nima/results/physical_common_extension_splitting_p32003.json`
- `research/nima/results/physical_common_extension_splitting_p32009.json`
