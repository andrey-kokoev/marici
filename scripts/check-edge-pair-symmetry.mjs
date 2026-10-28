import fs from 'node:fs/promises';
import {auditEdgePairSymmetry} from '../research/realization-tower/edge-pair-symmetry.mjs';
const cases=[];
for(let k=1;k<=7;k++)for(const branch of [1,3])cases.push(auditEdgePairSymmetry(k,branch));
const output=new URL('../research/realization-tower/results/edge-pair-symmetry-v1.json',import.meta.url);
await fs.mkdir(new URL('.',output),{recursive:true});
await fs.writeFile(output,JSON.stringify({status:'PASS',scope:'Geometry, existing role assignments and attachment witnesses; no new particle assignments',cases},null,2)+'\n');
for(const c of cases.filter(c=>c.branch===1))console.log(JSON.stringify({k:c.k,cells:c.regionCells,octahedra:c.octahedralGroups,terminalStep:c.terminalStep,unassignedPairs:c.unassignedEdgePairs,fixedUnassigned:c.fixedUnassignedEdgeCells,unassignedSupportCounts:c.segments.filter(s=>s.role===null).map(s=>s.assignedFaceCount)}));
console.log(`PASS ${cases.length} symmetry audits; ${output.pathname}`);
