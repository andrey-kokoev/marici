# Partial composition of source-authority grants

Owner: `marici.Strominger`

## Typed grant

An authority grant is not merely an implication between propositions. It is a
typed arrow

\[
g=(A\xrightarrow{o}B;k,D,v,T,\omega),
\]

containing:

- source object `A`;
- target operation `o` and target object `B`;
- authority kind `k`;
- evidence domain `D` with an explicit authority boundary;
- variance `v`;
- admissible transformations `T`;
- source-authority evidence and a required coherence witness `omega`.

Only admitted grants participate in composition.

## Partial composition law

For admitted grants `g:A->B` and `h:B->C`, `h o g` exists only if:

1. endpoints match;
2. authority kinds agree and the result has that same kind;
3. variances agree;
4. the evidence-domain rule for the declared composition mode holds;
5. every transformation preserves authority as well as evidence;
6. an explicit coherence witness is supplied.

There are three lawful modes:

- **Transport.** Existing authority is carried through an admitted
  transformation. The kind cannot change. Preserving evidence without
  preserving authority is insufficient.
- **Domain intersection.** Independently authorized grants compose only on
  the exact intersection of their evidence domains.
- **Authority extension.** A larger domain is allowed only with independent
  extension authority and evidence for every new domain atom. The authority
  kind remains fixed.

Any composite with a stronger or merely different authority kind is authority
laundering.

## Identity and associativity

Every typed object/domain/kind has an identity grant. Left and right identity
laws preserve the complete grant signature.

Associativity is conditional, not global. For three grants, both pairwise
factorizations must exist, have identical endpoint/kind/domain/variance
signatures, and be joined by a zero-defect triple coherence witness. Valid
pairwise squares do not imply this cell. A factorization-dependent result is
therefore rejected even when every local grant is individually valid.

## Required hostile cases

The machine-readable fixture suite rejects:

1. algebraic faithfulness plus support promoted to observer authority;
2. two readout grants promoted to selector authority;
3. completion plus executable ports promoted to constructor authority;
4. pairwise-valid composites with a nonzero triple coherence defect;
5. base change preserving evidence while destroying authority;
6. two factorizations producing different evidence domains.
7. replacement of an intermediate presentation without a source-derived
   coherence cell;
8. replacement that silently strengthens authority kind;
9. removal of the intermediate object without an independently authorized
   direct route.

These realize the decisive falsifier: local validity does not guarantee a
factorization-independent or kind-preserving composite.

## Deutsch--Popperian representation test

Let a claimed explanation be presented as

\[
A\xrightarrow{f}B\xrightarrow{g}C.
\]

Remove `B`, or replace it by `Bprime`. Compare the resulting arrow with the
original composite at the process boundary

\[
\sigma(g\circ f)=(A,C,\text{authority kind},\text{variance}).
\]

The contract returns exactly three verdicts:

1. `process_explained_strictly`: removing the intermediate presentation
   leaves an independently source-authorized direct grant with the same full
   signature;
2. `process_explained_coherently`: changing the presentation preserves the
   process signature and an invertible, source-derived natural coherence cell
   identifies the two composites;
3. `presentation_only`: no alternative composite or direct source grant
   exists, authority kind changes, or the required coherence cell is absent.

Thus the compositional DPC is

\[
\boxed{
\text{an explanation is process-level only if its authority survives every
admissible change of presentation coherently.}
}
\]

Agreement of outputs is insufficient. The coherence transformation itself
must be source-derived, invertible on the admitted evidence domain,
kind-preserving, and natural (zero coherence defect). Otherwise the account
explains why one representation computes the output, not why the underlying
process occurs.

## Grothendieck classification

The positive theta labels authorize the half-line overlap readout. Reciprocal
doubling extends that readout to the two folded charts. The square is not
strict: scale translation changes the lower endpoint, and the correction is
the explicit seam current

\[
\partial_cK_d(z;c)
=-e^{izc}\sqrt{\phi_1(c+d/2)\phi_1(c-d/2)}.
\]

Together with reciprocal reflection, this supplies the required coherence
cell. Therefore the result is:

\[
\boxed{\text{composable readout authority with an explicit coherence cell}.}
\]

It supplies neither observer authority nor an RH-bearing nonvanishing law.

## Kitaev classification

After nonlinear couplers and calibrated pulse angles are admitted, their
exponentials give a valid conditional logical executor grant. But the hostile
source-independence audit shows that the couplers are spectral logarithms of
the desired gates rather than consequences of native `D(S3)` dynamics.
Moreover, raw five-rail application fails encoded intertwining with large
codespace leakage.

Rail support and distance-three spread remain compatible evidence, but the
base-change-like lift preserves no executor authority. Thus:

\[
\boxed{\text{no composable authority map to the physical five-rail compiler}.}
\]

A native gauge-compatible gadget plus a verified encoded intertwiner would be
the smallest missing pair of grants.

## Smallest proposed extension to Nima v2

The standalone calculus passes before any shared-kernel modification. The
smallest proposed addition is:

- typed evidence domains;
- authority grants with endpoints, kind, variance, admissible transports, and
  coherence;
- partial compositions in the three modes above;
- identity laws and explicit associativity cells.

No ordering that automatically promotes authority kinds should be added.

## Artifacts

- Compiler: `authority_grant_composition.py`.
- Contract: `contracts/authority-grant-composition.v1.json`.
- Hostile fixtures:
  `contracts/authority-grant-composition-hostile-fixtures.v1.json`.
- Checker: `checkers/authority_grant_composition_checks.py`.
- Results: `results/authority_grant_composition.json`.
