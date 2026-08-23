# The minimal sufficient readout quotient

Let \(V\) be a frozen finite-dimensional coefficient, response, or state
space and let the complete declared readout family be the linear map

\[
R:V\longrightarrow W=\prod_i W_i.
\]

Define

\[
V_R:=V/\ker R.
\]

Then \(R\) factors uniquely as

\[
V\twoheadrightarrow V_R\lhookrightarrow W,
\]

and \(V_R\cong\operatorname{im}R\). If another quotient
\(q:V\twoheadrightarrow Q\) preserves every readout, so that \(R=\bar Rq\),
then

\[
\ker q\subseteq\ker R.
\]

Consequently \(q\) factors uniquely through the canonical projection to
\(V_R\). Thus \(V_R\) is the coarsest quotient—and hence the smallest linear
object—that retains the complete declared readout family.

Equivalently, form the category whose objects are sufficient quotients
\(q:V\twoheadrightarrow Q\) through which \(R\) factors, and whose arrows are
further quotient maps commuting with \(V\) and the readout. Then

\[
\boxed{V_R\text{ is terminal in the category of sufficient quotients}.}
\]

This replaces numerical minimization with a universal property. No norm,
energy landscape, or comparison of heterogeneous obstruction grades is
required.

## Joint conservativity

The family is jointly conservative exactly when

\[
\ker R=0.

\]

In that case \(V_R=V\), and no nontrivial quotient of \(V\) preserves all
declared readouts. This supplies an exact meaning for readout-minimality.

## Controls

On the one-loop QED \(D_{12}\) coefficient plane, the Bell and transfer
readouts have matrix

\[
\begin{pmatrix}1&3/2\\1&1\end{pmatrix}
\]

with determinant \(-1/2\). Their product is injective, so the complete plane
is already its minimal sufficient readout object. Either readout alone has a
one-dimensional invisible kernel and is insufficient for the pair.

For the currently declared cosmological \(T_7\) continuation family, three
readouts have joint rank at most three. Its canonical quotient for that
restricted family therefore has dimension at most three and forgets at least
four directions. This is not a physical minimal object because the frozen
four-map cosmology protocol remains incomplete. Minimality is always relative
to a prospectively declared readout family; silently omitting readouts makes
the quotient artificially small.

## Categorical scope

In a general category, replace \(\ker R\) by the intersection of kernel pairs
when it exists and take the corresponding effective quotient. The conjectural
cross-sector statement requires the quotient to be source-derived and stable
under the sector's support, connection, and composition laws. A vector-space
quotient alone does not establish those properties.

## Experienced-world boundary

This theorem identifies minimal sufficient **records**, not consciousness or
experienced worlds. The stronger conjecture requires a source-derived,
jointly conservative readout family and a persistent record algebra. The
theorem prevents that conjecture from choosing its minimal object after the
fact.

Artifacts:

- `research/nima/checkers/check_minimal_sufficient_readout_quotient.py`
- `research/nima/results/minimal_sufficient_readout_quotient.json`
- `research/nima/checkers/check_jointly_conservative_d12_readouts.py`
- `research/nima/results/cosmology-source-cycle-family-rank-bound.json`
