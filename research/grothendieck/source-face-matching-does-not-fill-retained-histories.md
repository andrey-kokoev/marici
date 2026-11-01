# Source face matching does not fill retained histories

## Question

The operator requested execution of `research/chatgpt/marici_codim_one_pair_research_note.md`. Does compatible pairing itself produce a new source witness? Conjecture tested: endpoint matching suffices for one retained history realizing both records. Rival: matching retains incompatible histories, and a higher comparison requires separate structure.

## Claim boundary

`agda/SourceFacePairBoundary.agda` defines the universe-polymorphic homotopy pullback `Match r s`, its exchange by path reversal, and exchange involutivity. No generating arrow is inverted.

Its actual-source specialization uses full free histories from A and restriction to their endpoints. This is endpoint matching, not a simplicial codimension-one reconstruction theorem. Both records survive exchange exactly. The explicit filler notion is the fiber of the diagonal restriction: one history realizing both records. Canonical diagonal pairs fill; the pair AB and AD;DB does not, since the source's single-edge Boolean observation distinguishes them. Consequently this restriction has no total section. This does not rule out an independently supplied higher-cell relation between the histories.

A stronger continuation test uses every actual free suffix q from B: AB;q and AD;DB;q remain unequal, distinguished by their first occurrence. On the strict shared-endpoint pair slice, exchange commutes with appending every common suffix, and exchange twice returns the original pair. These theorems do not assert naturality for arbitrary presentation changes or supply inverse execution of directed suffixes.

## Disposition

The diagonal-filler conjecture is refuted in the source. Reversible pair exchange and suffix naturality are proved without erasing occurrences. The first missing object for genuinely new higher generation is a source-admitted higher filler type and its restriction/continuation operations, distinct from the diagonal used here. Acceptance requires a constructor or classified obstruction for that declared fiber; the present result neither chooses such a type nor fabricates an admission certificate.

Fresh safe Cubical Agda closure check exited 0. The final module and Nima's `.agda` dependencies were copied into `/tmp/marici-face-pair.ytFMC7` to avoid mutating Nima's generated interfaces:

```sh
agda --ignore-interfaces --transliterate --safe --cubical --guardedness --no-libraries -i /tmp/marici-face-pair.ytFMC7 -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 /tmp/marici-face-pair.ytFMC7/SourceFacePairBoundary.agda
```

Imported indexed-pattern warnings report limited computation on transports; compilation uses no holes or postulates. The note's S3, monoid, and K(Z/2,2) enumerations have not been rerun here, and their scripts were not found alongside the note. No four-face horn theorem is used. Higher period-four equivariance remains a separate open obligation. Files are uncommitted.
