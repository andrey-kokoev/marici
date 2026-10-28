# A finite interval-to-cavity process dictionary

## Question and disposition

Constructed the comparison frozen in `interval-cavity-process-dictionary-protocol.md`: all six interval records at m=3 (NNMHV n=8) map injectively to contiguous process operators of the existing three-round cavity. The dictionary preserves all twelve legal L/R/l/r edits, four adjacent segment compositions and complete source-record recovery.

This supplies a previously missing **finite mathematical process encoding**. It does not encode interval identity faithfully into every output state, derive a physical preparation/observer, authorize inverse controls or select the two causal interpretations. Earlier claims that no interval/cavity map was supplied are superseded only at this bounded process level.

SCC obligation: forward realization and operation/composition compatibility. No new optical coefficients, modes, metrics or fitted response are introduced. The proposed comparison identifies existing chronological round incidence with the existing three-edge line; its physical significance remains unproved.

## Definition and source recovery

Let W_k be the actual `round_map(k)`, k=0,1,2. Define

    E(i,j)=W_(j-1) ... W_(i-1), 1<=i<=j<=3.

The process carries a fixed labelled amplitude/phase frame. Each round's incident slot is u_k=1+3k. On that diagonal,

    E(i,j)[u_k,u_k] = -3/5 if i-1<=k<=j-1,
                       1 otherwise.

Earlier rounds leave a later incident input untouched. Its own round reflects it with amplitude -3/5; later rounds leave that reflected output slot untouched. An unselected incident slot is untouched by the whole segment. Thus the diagonal signature recovers exactly the nonempty consecutive set of selected rounds.

The six signatures are distinct. Decode i,j from that set and reconstruct the complete actual compiler record h_8(j+4,i+4), including its prefix and diagonal upper-boundary replacement. The implemented decoder also checks the **entire** matrix against the canonical E(i,j); a correct diagonal on a corrupted matrix is not enough. It does not consult a retained interval label to recover that label.

This is recovery from the specified process matrix. Acquisition of that matrix, or a sufficient calibrated probe family, is not supplied by a numerical inspection of it. Keeping source/edit history remains necessary because the matrix cannot reconstruct arbitrary execution genealogy.

## Four operation squares

With rightmost matrix acting first, source path composition gives

    E(Lp)=E(p) W_(i-2),       i>1,
    E(Rp)=W_j E(p),           j<3,
    E(lp)=E(p) W_(i-1)^T,     i<j,
    E(rp)=W_(j-1)^T E(p),     i<j.

The checker uses the actual endpoint-compatible `compose` implementation for extensions, unique path trims for inverses, and recompiles full source records. Orthogonality supplies the cancellations on these domains. These are left/right **process** actions, not a claim that a bare first-round inverse correctly acts on the final state.

For each source edit p->p', define the based output correction

    C_(p,p')=E(p') E(p)^T.

Then C_(p,p') E(p)=E(p'). For left trim this reduces to the suffix-transported correction of the preceding component result. Left extension similarly requires transport through the existing segment. Right extension acts by the next round on the output; right trim removes the last chronological round. There is no single state-independent fixed flip replacing these controls.

For adjacent segments, E(i,k)=E(j+1,k)E(i,j). Empty process words can represent identity attachments, but are not admitted as nonempty interval objects. Distinct admissible edit routes, including LR/RL, keep their intermediate records and tags even when final process operators agree.

## Exact execution

`python research/nima/checkers/check_interval_cavity_process_dictionary.py` passed:

- six full source-record recoveries;
- twelve legal edit squares;
- 792 occupation columns across N=0,1,2 for the based corrections;
- factorial norm preservation on every tested column;
- four adjacent concatenations and two distinct-history endpoint squares.

The full-space based correction identity is an exact matrix equality. Its all-number-sector lift follows from the supplied symmetric-power composition theorem, not extrapolation from the finite-sector tests. The source horizon remains fixed at three rounds.

Receipt: `results/interval-cavity-process-dictionary.json`.

## Deliberate failures and the surviving state gap

The decoder rejects an empty or noncontiguous signature, a wrong-order product and a matrix corrupted off the signature diagonal. Source guards reject illegal L and a trim of a one-edge object. Diagonal records are retained algebraically but rejected as metric-visible points. The bare left-prefix inverse fails, as in the preceding compiler test.

All six passive processes fix the common optical vacuum. Consequently

    E(i,j)|vac> = |vac>

for every interval. The process dictionary is injective, while this output-state map is constant. This is an explicit successful rejection of the claim that a faithful process dictionary automatically supplies a faithful encoding on a fixed common input. It does not exclude other specified preparations or process-probe families.

The source labelled process and its operator are thus useful new interfaces. A physical state/readout binding still needs independently justified preparations, calibrated observations and inverse-control access. Neither the coordinate signature nor the correction matrix selects physical future cones, chart time or metric scale.

## Stop

The finite process dictionary is complete at the frozen scope. Do not repeat the broad search for an unspecified mathematical interval map: this one is now explicit. Reopen physical realization only with a stated preparation/probe/control package; do not promote the process matrix, an external label log or the vacuum output into that missing package.
