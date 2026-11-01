import assert from 'node:assert/strict';
import {mkdir,readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSulfurIncomingBundle} from '../research/realization-tower/sulfur-32-incoming-bundle.mjs';
import {worldPoint} from '../research/realization-tower/normal-ray-model.mjs';
import {buildSulfurLocalTransitions,learnLocalRule,enterLocalCarrier,leaveLocalCarrier,compareHexLocalStars} from '../research/realization-tower/sulfur-local-transition.mjs';
const reference=buildSulfurIncomingBundle(),original=JSON.stringify(reference),model=buildSulfurLocalTransitions(reference),rule=learnLocalRule(model.motifs),hex=compareHexLocalStars(model);
const passages=[];
for(const motif of model.motifs){
 const heldOutRule=learnLocalRule(model.motifs.filter(m=>m.id!==motif.id));
 assert.equal(heldOutRule.selectorByA[motif.context.a],motif.selector);
 for(const row of motif.rows){
  const strand=reference.strands.find(s=>s.id===row.strandId),i=strand.edgeIds.indexOf(motif.id);
  const input={strandId:strand.id,polarities:structuredClone(strand.polarities),colour:strand.label,payload:{ordinal:passages.length,values:[null,{phase:[2,-3]}]},port:strand.edgeIds[i-1]};
  const carrier=enterLocalCarrier(motif,input,heldOutRule),output=leaveLocalCarrier(motif,carrier,heldOutRule);
  assert.equal(output.port,strand.edgeIds[i+1]);
  assert.deepEqual(output,{...input,port:strand.edgeIds[i+1]});
  assert.deepEqual(leaveLocalCarrier(motif,enterLocalCarrier(motif,output,heldOutRule,'reverse'),heldOutRule),input);
  passages.push({motif:motif.number,input,carrier,output,nativeGuide:strand.guide.slice(i-1,i+3),passed:true});
 }
 // Independently confirm the reported angles in the actual viewer's 3D metric.
 const sub=(a,b)=>a.map((x,i)=>x-b[i]),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
 for(const side of ['tail','head']){
  const origin=worldPoint(motif[side]),opposite=worldPoint(motif[side==='tail'?'head':'tail']);
  const ports=(side==='tail'?motif.inputs:motif.outputs).map(p=>worldPoint(p.point));
  const arms=[opposite,...ports].map(p=>sub(p,origin));
  const cosines=arms.flatMap((a,i)=>arms.slice(i+1).map(b=>dot(a,b)/Math.sqrt(dot(a,a)*dot(b,b)))).sort((a,b)=>a-b);
  assert(cosines.every((c,i)=>Math.abs(c-motif.geometry[side].cosines[i])<1e-10));
 }
}
assert.equal(passages.length,16);assert.equal(new Set(passages.map(p=>p.input.strandId)).size,16);
assert.equal(JSON.stringify(reference),original);assert.equal(hex.rigidStarMatches.length,0);
const files=['research/realization-tower/sulfur-32-incoming-bundle.mjs','research/strominger/pe-symmetric-sector.mjs','research/realization-tower/sulfur-local-transition.mjs','research/realization-tower/branching-seed.mjs','research/realization-tower/hex-edge-grid-model.generated.mjs'];
const hashes=Object.fromEntries(await Promise.all(files.map(async path=>[path,createHash('sha256').update(await readFile(path)).digest('hex')])));
const receipt={schema:'sulfur-local-transition-check.v1',passed:true,sourceHashes:hashes,sourceRoutingScope:model.sourceScope,rule,checks:{forward:16,reverse:16,heldOut:16,opaquePayloadsPreserved:true,sourceRoutesUnchanged:true,viewerMetricChecked:true},passages,motifs:model.motifs,candidateGeometry:model.candidates.map(m=>({edge:m.id,geometry:m.geometry})),hexComparison:hex};
const out='research/strominger/results/sulfur-local-transition-v1';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify(receipt,null,2)+'\n');
const rows=model.motifs.flatMap(m=>m.rows.map(r=>`| ${m.number} | \`${r.strandId}\` | ${r.colour} | ${m.selector}=${r.polarities[m.selector]} | ${m.heldBit}=${m.heldSign} | ${r.input} → ${r.output} |`)).join('\n');
const example=model.motifs[0],native=passages.filter(p=>p.motif===1).map(p=>`| \`${p.input.strandId}\` | ${p.nativeGuide.map(v=>'('+v.join(',')+')').join(' → ')} |`).join('\n');
const report=`# Su-32 local transition reproduction v1

## Result

Reproduced all 16 observed passages through the eight upper mixing edges of the
existing Sulfur-32 incoming-bundle wiring. Every record exits on its actual next
reference edge, with identity, colour, polarity tuple and opaque payload intact.
Reversal recovers every input. No source route or layer geometry was changed.

This reproduces an existing candidate wiring. It does not derive its globally
chosen rim/interior middle matching from the eight-layer construction.

## The local carrier rule

Each examined carrier edge has two arrivals and two departures. Its two records
agree on three polarity bits and differ on one. Within that fixed context, one
bit distinguishes the two lanes; erasing it leaves two possible departures.
The carrier is proposed as an analogue of a white connector; its two native wires
retain their original colours, rather than being recoloured white.

- When a=+, the varying bit is p and the held bit is e.
- When a=−, the varying bit is e and the held bit is p.
- Number ports 0,1 by numeric lexicographic native coordinates, separately at
  each endpoint. In this convention, input slot = 0 for selector +, 1 for −.
- Output slot = input slot XOR [held sign is +]. Thus held + swaps slots;
  held − preserves them. This is coordinate-convention dependent.
- On reverse traversal use the inverse switch, preserving the selector value
  and the complete record. Strand ID is not consulted to choose an exit.

The same rule is learned from the other seven motifs and predicts both passages
of each held-out motif. This is an internal generalization check on this reference,
not a proof of a universal rule or independent physical validation.

| Motif | Retained strand | Colour | Carried selector | Held bit | Input → output slot |
|---|---|---|---|---|---|
${rows}

## First reproduced neighbourhood

Shared directed carrier: (${example.tail.join(',')}) → (${example.head.join(',')}).
The rows below are exact consecutive reference vertices, not new routes.

| Strand | Previous → carrier tail → carrier head → next |
|---|---|
${native}

## Comparison with the eight layers

There are ${hex.hexMotifs} complete white-edge neighbourhoods in the layers,
grouped into ${hex.patterns.length} decorated states. Both endpoints have three
coplanar arms 120° apart.

The eight upper native motifs instead have:

- Tail arm-angle set: **60°, 120°, 180°**.
- Head arm-angle set: **60°, 60°, 90°** or **60°, 90°, 120°**.
- Head normalized Gram determinant: **1/2**, hence not coplanar.

An exhaustive scan of the occupied reference edges finds ${hex.referenceCandidates}
co-oriented, two-record, two-input/two-output candidate carriers. **None** has the
120° three-star at both ends. The angles were also checked independently using
the viewer's actual 3D world-coordinate map.

Therefore this reproduces the **local transport**, but not a rigid geometric
identification with a single white segment of the planar layers. A specified
folding or a larger, multi-edge neighbourhood could change the comparison; this
check does not rule those out. No octahedral gluing is inferred from equal counts.

## Verification

- Implementation: research/realization-tower/sulfur-local-transition.mjs
- Tests: node --test tests/sulfur-local-transition.test.mjs
- Fresh checker: node scripts/check-sulfur-local-transition.mjs
- Full coordinates, port IDs, packets, angle evidence and source hashes:
  results/sulfur-local-transition-v1/verification.json
`;
await writeFile('research/strominger/sulfur-local-transition-v1.md',report);
console.log(JSON.stringify({passed:true,forward:16,reverse:16,heldOut:16,rule,hexMotifs:hex.hexMotifs,referenceCandidates:hex.referenceCandidates,rigidMatches:hex.rigidStarMatches.length,report:'research/strominger/sulfur-local-transition-v1.md'},null,2));
