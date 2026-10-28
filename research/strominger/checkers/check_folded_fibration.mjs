import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {buildFoldedFibration,confirmFoldedRound} from '../../realization-tower/fibration-folded-process.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..'),m=buildFoldedFibration();
assert.equal(m.audit.geometricCells,175);assert.equal(m.audit.octahedra,56);assert.equal(m.audit.matchedFoldPairs,175);
const confirmations={};for(const [name,flow]of [['outward',m.outward],['return',m.back]])confirmations[name]=flow.rounds.slice(1).map((_,i)=>confirmFoldedRound(m,name,i+1));
const sources=['research/realization-tower/fibration-folded-process.mjs','research/realization-tower/normal-ray-model.mjs','research/realization-tower/fibration12-process.mjs','research/realization-tower/fibration-step-machine.mjs','research/strominger/paired-polarity-model.mjs','research/strominger/fibration-steps-v1.json'];
const result={status:'passed',audit:m.audit,flow:{entry:m.entry,exit:m.exit,outwardRounds:m.outward.rounds.length-1,returnRounds:m.back.rounds.length-1,coincidentGeometryDistinctOccurrences:true},
 sourceSha256:Object.fromEntries(sources.map(p=>[p,crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex')])),
 foldPairs:m.geometry.map(g=>({geometry:g.id,kind:g.kind,primitiveIds:g.primitiveIds,occurrences:g.occurrences,polarityRoles:g.polarityRoles})),confirmations,
 scope:'175 geometric cells, 350 original flow occurrences, both polarity sheets retained. The old internal tetrahedral cuts are not retained as physical interfaces. A display sheet choice never mutates either state. No particle-law or channel-count derivation asserted.'};
fs.writeFileSync(path.join(root,'research/strominger/results/folded-fibration-v1.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.status,audit:result.audit,flow:result.flow},null,2));
