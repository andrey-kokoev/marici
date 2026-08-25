# A global adjoint fault swaps four sectors and flags four

Owner: `marici.Kitaev`

## Deutsch-style question

Does the controller logical (X) actually change the final (D(S_3)) sector
readout, or is it detectable or gauge?

The physical answer requires the missing interface constructor. We can still
propagate two precisely typed algebraic fault actions through the exact CDFG
codebook.

## Global-adjoint action

Replacing every controlled quarter evolution by its adjoint sends the residue
signature to its negative:

\[
(r_C,r_D,r_F,r_G)\longmapsto
-(r_C,r_D,r_F,r_G)\pmod4.
\]

Exact codebook lookup gives

\[
A\leftrightarrow B,qquad D\leftrightarrow E,
\]

while (C,F,G,H) are sent outside the valid eight-word codebook. If the
fault mode is unobserved, the sixteen sector-mode inputs have only twelve
distinct observations. Four observations have two-element fibers, so the
readout is not jointly faithful.

This is neither harmless nor uniformly detectable: it is a valid logical
sector permutation on half the sectors and an invalid-word flag on the other
half.

## Global-omission proxy

If every controlled phase is omitted, every sector returns (0000). That
word is outside the valid CDFG codebook and is therefore detectable by
codebook membership, although all sector information is lost.

## Constructor boundary

Neither proxy is asserted to be the physical effect of a controller logical
(X). That identification requires

\[
\Phi_{\rm fault}:
\{\text{controller fault classes}\}
\longrightarrow
\{\text{logical CPTP maps on data and pointers}\}.
\]

No admitted ququart/binary interface supplies this map. The exact result is a
family of conditional predictions against which a future constructor can be
tested.

## Falsifiers

- Negating every CDFG residue does not exchange (A/B) and (D/E).
- Any of (C,F,G,H) remains inside the nominal codebook after negation.
- The sixteen sector-mode inputs produce more or fewer than twelve distinct
  signatures.
- (0000) is a valid nominal sector signature.
- A physical interface derives a different controller-fault action.

## Artifacts

- Checker: `checkers/check_s3_common_mode_readout_propagation.py`
- Result: `results/s3-common-mode-readout-propagation.json`
- Result SHA256:
  `EC8A0CFD713907B1FEF2FD31D76012CAF9D3E58B200473D136B1269860B0F441`
- Graph admission: `ev-000000003509-94131a08-7b99-491d-acaa-c08ba7acb32d`
- Ledger: entry 2525, `seqclaim-e83ad0bcee723891a9980a73`
