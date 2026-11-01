import assert from 'node:assert/strict';
import {mkdir,readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSulfurIncomingBundle} from '../research/realization-tower/sulfur-32-incoming-bundle.mjs';
import {buildSulfurLocalTransitions} from '../research/realization-tower/sulfur-local-transition.mjs';
import {worldPoint} from '../research/realization-tower/normal-ray-model.mjs';
import {analyzeNativePortFrame,learnGeometricLocalRule,replayGeometricLocalPacket,scanSharedCarriers,testSingleEdgeSheetFolds} from '../research/realization-tower/sulfur-local-geometry.mjs';
const reference=buildSulfurIncomingBundle(),snapshot=JSON.stringify(reference),model=buildSulfurLocalTransitions(reference);
const rule=learnGeometricLocalRule(model.motifs),scan=scanSharedCarriers(reference),folds=testSingleEdgeSheetFolds(model.motifs),passages=[];
const transform=p=>{const [x,y,z]=worldPoint(p);return [7+3*(.6*x-.8*y),-3+3*(.8*x+.6*y),2-3*z];};
for(const motif of model.motifs){
 const learned=learnGeometricLocalRule(model.motifs.filter(m=>m.id!==motif.id));
 const moved={...motif,tail:transform(motif.tail),head:transform(motif.head),inputs:motif.inputs.map(p=>({...p,point:transform(p.point)})).reverse(),outputs:motif.outputs.map(p=>({...p,point:transform(p.point)})).reverse()};
 delete moved.rows;delete moved.observedPermutation;delete moved.selector;
 for(const row of motif.rows){
  const strand=reference.strands.find(s=>s.id===row.strandId),i=strand.edgeIds.indexOf(motif.id);
  const input={strandId:strand.id,polarities:{...strand.polarities},colour:strand.label,payload:{nested:[2,-4,null]},port:strand.edgeIds[i-1]};
  const output=replayGeometricLocalPacket(motif,input,learned);
  assert.deepEqual(output,{...input,port:strand.edgeIds[i+1]});
  assert.deepEqual(replayGeometricLocalPacket(motif,output,learned,'reverse'),input);
  assert.deepEqual(replayGeometricLocalPacket(moved,input,learned),output);
  const frame=analyzeNativePortFrame(motif);
  passages.push({motif:motif.number,input,output,inputClass:frame.inputs.find(p=>p.edge===input.port).kind,outputClass:frame.outputs.find(p=>p.edge===output.port).kind,selector:motif.selector,selectorSign:row.polarities[motif.selector],heldOutPassed:true,reversePassed:true,transformedFramePassed:true});
 }
}
assert.equal(passages.length,16);assert.equal(new Set(passages.map(p=>p.input.strandId)).size,16);
assert.equal(scan.windows,432);assert.equal(scan.counts.candidates,46);assert.equal(scan.counts.chordAngleMatches,0);
assert(folds.every(f=>!f.necessaryNonExpansionSatisfied&&Math.abs(f.tail.maxChordExpansion-4/3)<1e-12));
assert.equal(JSON.stringify(reference),snapshot);
const paths=['research/realization-tower/sulfur-32-incoming-bundle.mjs','research/strominger/pe-symmetric-sector.mjs','research/realization-tower/sulfur-local-transition.mjs','research/realization-tower/sulfur-local-geometry.mjs','research/realization-tower/branching-seed.mjs'];
const hashes=Object.fromEntries(await Promise.all(paths.map(async p=>[p,createHash('sha256').update(await readFile(p)).digest('hex')])));
const receipt={schema:'sulfur-local-geometry-check.v2',passed:true,sourceHashes:hashes,referenceScope:reference.audit.routingStatus,rule,
 checks:{forward:16,reverse:16,heldOut:16,changedFrame:16,identitiesPreserved:true,sourceRoutesUnchanged:true},passages,
 frames:model.motifs.map(m=>({motif:m.number,frame:analyzeNativePortFrame(m)})),sharedCarrierSearch:scan,singleEdgeSheetFolds:folds};
const out='research/strominger/results/sulfur-local-geometry-v2';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify(receipt,null,2)+'\n');
const table=passages.map(p=>`| ${p.motif} | \`${p.input.strandId}\` | ${p.input.colour} | ${p.selector}=${p.selectorSign} | ${p.inputClass} | ${p.outputClass} |`).join('\n');
const report=`# Su-32 local geometry reproduction v2

## A coordinate-independent description of the reproduced switch

The v1 straight/swap table depended on independently numbering the ports at each
end. That table was correct in its stated convention, but its held-bit parity
was not an intrinsic geometric description. The reference admits a cleaner one.

For each of the eight upper mixing carriers:

1. One incoming arm is straight back along the carrier; the other is oblique.
2. The oriented carrier and the oblique incoming arm define a plane P.
3. Exactly one outgoing arm lies in P. The other lies outside P.
4. The varying polarity bit **+ selects the out-of-plane departure**;
   **− selects the coplanar departure**.

As in v1, a=+ selects p and a=− selects e. At entry, agreement of the selected
sign with b identifies the oblique arrival; disagreement identifies the straight
arrival. Thus a identifies the polarity being read, b identifies how it arrives,
and its sign chooses the geometric exit class. The full identity and payload
remain intact. The other polarity remains carrier context, not a separate
coordinate-order switch in this description.

This is reproduction of the existing reference's upper local transitions, not
a derivation of its globally chosen middle matching. The labels a,b,p,e are
still supplied by that reference, not assigned to the eight layers by this work.

## Verification and physical angle

All 16 passages match their actual next reference edges. All reverse passages
recover their inputs. Each motif is predicted by a rule learned from the other
seven. Prediction survives reversed port-array order, removal of the observed
route table, and a rotation, reflection, translation and uniform rescaling into
the viewer's actual 3D metric. Strand IDs are retained but not read to choose exits.

For vectors (carrier, oblique arrival, outgoing arm), native Gram determinants
are exactly 0 for the coplanar departure and 4 for the skew departure. The latter
has transverse cosine 1/3, hence an **unoriented plane angle acos(1/3) =
70.528779°** about the carrier; its supplementary oriented angle is 109.471221°.
These values come from the reference geometry. Neither is an assumed 120° twist.

Only one outgoing arm is skew. The entire three-arm output junction is not a
single plane. Rotating a complete planar fork as a rigid object would not
reproduce that junction.

| Motif | Retained identity | Colour | Selector | Arrival | Departure |
|---|---|---|---|---|---|
${table}

## Larger carriers: bounded exhaustive search

Enumerated all ${scan.windows} contiguous internal windows of the sixteen existing
routes, with either orientation: ${scan.distinctRuns} distinct runs,
${scan.sharedGroups} shared by at least two records. There are
${scan.counts.candidates} eligible two-arrival/two-departure candidates, including
both all-traffic carriers and two-strand subtraffic without deleting other
identities. Eligible runs span 1, 2 or 4 edges; four was a result, not a search cap.
An independent strand-pair enumerator in the tests recovers all 44 two-record
cases; two additional candidates carry more than two records.

There are **no** matches to 120° three-stars at both ends, either using actual
first/last tangents or replacing the internal run by its endpoint chord. The
latter intentionally relaxes internal shape and length before testing angles.
A synthetic true hex carrier passes the same search as a positive control.

This excludes these particular shared-run coarse-grainings. It does not cover
arbitrary new paths, larger branched regions, virtual ports inside edges/faces,
or cross-layer identifications.

## Folding: one precise obstruction

For a filled planar chart, a non-stretching fold cannot increase the Euclidean
distance beyond the length of an available straight path on that chart.
Two unit arms 120° apart have endpoint distance sqrt(3). Each reference incoming
star instead contains an opposite pair of unit arms with endpoint distance 2.
The required squared-distance expansion is **4/3** at every upper motif.

Thus an ordinary non-stretching fold of that single filled white-edge
neighbourhood cannot reproduce these unit-edge junctions. This statement assumes
the chart contains the local straight chords. It is **not** a no-go theorem for
a freely hinged wire graph, a cut sheet, a branched coarse-graining, or a different
assignment of virtual boundary ports. Those require additional explicit geometry.

## What this establishes, and what remains

We now reproduce the local routing using intrinsic input-plane / output-plane
information, rather than arbitrary coordinate port numbering. The proposed
white connector needs to distinguish coplanar from noncoplanar continuation.
The current separate planar layers do not yet supply that interface: each of
their own complete white-edge stars has two coplanar outgoing arms.

The next geometric object to seek is a **branched multi-edge or cross-layer
interface with explicit boundary ports**, not another rigid alignment or a
longer shared chain. Any such correspondence must preserve the reference
records and predict the exit classes above. No inter-layer joins or routes were
added to either viewer by this investigation.

## Reproduction

- node --test tests/sulfur-local-geometry.test.mjs
- node scripts/check-sulfur-local-geometry.mjs
- Source: research/realization-tower/sulfur-local-geometry.mjs
- Receipt: results/sulfur-local-geometry-v2/verification.json
`;
await writeFile('research/strominger/sulfur-local-geometry-v2.md',report);
console.log(JSON.stringify({passed:true,rule,forward:16,reverse:16,heldOut:16,changedFrame:16,carrierSearch:scan.counts,foldObstructions:folds.filter(f=>!f.necessaryNonExpansionSatisfied).length,report:'research/strominger/sulfur-local-geometry-v2.md'},null,2));
