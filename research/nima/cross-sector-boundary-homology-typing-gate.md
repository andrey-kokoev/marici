# Cross-sector boundary--homology typing gate

## Candidate shared theorem

The strongest useful abstraction suggested by the topological pilot is not
“everything is an error-correcting code.” It is the following typed packet:

\[
R\xrightarrow{r}H\xrightarrow{s}S,
\qquad sr=0.
\]

Here \(H\) contains operational histories, \(s\) is a local residue readout,
and \(r\) supplies legal local equivalences or repairs. The protected
capability is

\[
\mathcal C=\ker s/\operatorname{im}r.
\]

For additional probes \(\ell:H\to P\) that vanish on
\(\operatorname{im}r\), the combined readout \((s,\ell)\) is jointly faithful
modulo repairs precisely when

\[
\boxed{
\ker s\cap\ker\ell=\operatorname{im}r.
}
\]

This statement separates three questions that our earlier language often
blurred:

1. Is an operation locally residue-free?
2. Is it equivalent to a legal local repair?
3. Do the admitted probes distinguish its remaining global class?

## Exact positive instance

The periodic toric chain complex supplies every datum canonically:

\[
C_2\xrightarrow{\partial_2}C_1\xrightarrow{\partial_1}C_0.
\]

The local syndrome alone has a kernel larger than the repair image by two
dimensions. Adding two noncontractible loop probes makes

\[
\ker(\partial_1,\ell_x,\ell_y)=\operatorname{im}\partial_2.
\]

Thus the probe family is jointly faithful exactly on the quotient relevant
to physical capability.

## Hostile rank falsifier

Matching dimensions and ranks do not establish this architecture. Over
\(\mathbf F_2\), take rank-one maps

\[
\mathbf F_2\xrightarrow{r}\mathbf F_2^2
\xrightarrow{s}\mathbf F_2
\]

with \(r(1)=(1,0)\) and \(s(x,y)=x\). Then \(sr\ne0\). The same rank census
as a legal complex therefore carries no homology at all.

Consequently:

\[
\boxed{
\text{matching kernels, ranks, or incidence diagrams do not create a
boundary--homology calculus.}
}

The zero composite or a source-derived nullhomotopy is mandatory.

## Sector audit

| Sector/object | \(s\) residue map | \(r\) repair map | \(sr=0\) | Capability status |
|---|---|---|---|---|
| Toric pilot | cellular \(\partial_1\) | cellular \(\partial_2\) | exact | \(H_1\), source-canonical |
| Reflection decoder | alternating \(z\)-maps | preceding alternating map | exact because \(z^2=0\) | nonzero homology, but physical support remains untyped |
| Strominger magnetic birth | magnetic matrix/Schur transport | none established | unavailable | canonical kernel birth, not yet homology |
| Benincasa correlator cube | no coefficient arrow between grades | none | unavailable | labelled sum, not a complex |
| Flavor texture quotient | physical quotient/readout exists | no chain repair map | unavailable | descent problem, not homology |

This is a partial confirmation and a strong correction. The toric and
reflection constructions instantiate the abstract complex. Strominger's
kernel births may eventually provide a capability object, but no preceding
repair map currently quotients them. Benincasa's cube cannot enter until one
actual localization arrow is derived.

## Meta-level result

The common Marici structure is presently weaker and more precise than “all
sectors are chain complexes”:

\[
\text{source-defined operational object}
\to
\text{typed local failure/readout},
\]

with a protected quotient only when the same source additionally supplies a
legal repair map and its coherence with the readout.

Homology is therefore not generic residue accumulation. It is what becomes
available when two independently typed operations compose to zero.

## Next falsifier

Attempt exactly one promotion rather than asserting universality:

- Strominger: search for a source-defined map into the magnetic history space
  whose image lies in the exceptional kernel; or
- Benincasa: derive one deletion-grade localization arrow and its adjacent
  zero-composite square.

Failure in either sector preserves its existing result while rejecting the
homological promotion.

## Verification

- `research/nima/checkers/check_boundary_homology_readout_gate.py`
- dependency-free invocation:
  `python research/nima/checkers/check_boundary_homology_readout_gate.py`

