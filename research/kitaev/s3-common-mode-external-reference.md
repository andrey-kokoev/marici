# Common-mode detection requires one external reference bit

Owner: `marici.Kitaev`

## Internal no-go theorem

Let (E_n(1)=\mathbf1_n) encode the replicated controller command. Any linear
internal syndrome (L) preserving both valid codewords must satisfy

\[
LE_n=0.
\]

Therefore

\[
L(\mathbf1_n)=L(E_n(1))=0.
\]

No number of additional internal parity checks can detect the common-mode
logical (X). It is motion along the valid encoded line, not motion normal to
it.

## Required external datum

Detection requires an independently rooted intended-command bit (c). If
(\hat c) is the decoded replicated command, then

\[
s_{\rm ext}=\hat c+c

\]

detects logical inversion. The reference must not share the same common-mode
orbit; otherwise it flips with the command and the comparison again vanishes.

## CDFG sufficiency and minimality

Under the conditional global-adjoint fault action, the sixteen pairs
((\text{sector},\text{mode})) produce twelve residue signatures, with maximum
fiber size two. Hence at least

\[
\left\lceil\log_2 2\right\rceil=1
\]

additional bit is necessary. Adjoining the external mode bit produces sixteen
distinct augmented observations, so one bit is also sufficient.

## Explanation

Replica parity protects transverse directions to the encoded command line.
An external reference fixes orientation along that line. This is why adding
more replicas increases distance against local faults but never reveals a
global logical flip.

## Boundary and falsifiers

- The external reference is not yet physically constructed or independently
  rooted.
- The CDFG sufficiency statement is conditional on global adjoint being the
  physical controller-fault action.
- An internal linear syndrome with (LE_n=0) but (L\mathbf1_n\ne0) would
  falsify the no-go.
- An augmented ((\text{signature},\text{mode})) collision would falsify
  sufficiency.

## Artifacts

- Checker: `checkers/check_s3_common_mode_external_reference.py`
- Result: `results/s3-common-mode-external-reference.json`
- Result SHA256:
  `B78F0870C6E672408C9F906D3030C9A62BB87A46B9E8793D00BBEF8415369E3A`
- Graph admission: `ev-000000003509-94131a08-7b99-491d-acaa-c08ba7acb32d`
- Ledger: entry 2525, `seqclaim-e83ad0bcee723891a9980a73`
