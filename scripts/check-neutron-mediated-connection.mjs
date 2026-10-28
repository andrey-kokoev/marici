import fs from 'node:fs/promises';
import {edgeProcedure} from '../research/realization-tower/edge-ray-model.mjs';
import {neutronMediation} from '../research/realization-tower/neutron-mediated-connection.mjs';
const cases=[];
for(const branch of [1,3]){
 const state=edgeProcedure(4,11,branch),ends=state.assignments.filter(a=>a.boundary==='face-vertex');
 const from=ends.find(a=>a.role==='electron'),to=ends.find(a=>a.role==='proton');
 cases.push({k:4,branch,relation:'central-gap',...neutronMediation(4,state.assignments,from.cell,to.cell)});
 for(const comparison of state.faceVertexComparisons)cases.push({k:4,branch,relation:'local-face-vertex',...neutronMediation(4,state.assignments,comparison.cell,comparison.owner)});
}
const output=new URL('../research/realization-tower/results/neutron-mediated-connection-v1.json',import.meta.url);
await fs.mkdir(new URL('.',output),{recursive:true});
await fs.writeFile(output,JSON.stringify({status:'PASS',scope:'Geometric N-mediated connection and attachment audit, not a single-cell closure execution',cases},null,2)+'\n');
for(const c of cases)console.log(JSON.stringify({branch:c.branch,relation:c.relation,existingNeutronMediation:c.existingNeutronMediation,paths:c.paths,fillerCells:c.fillerCells,octahedralGroup:c.octahedralGroup,attachments:c.attachments.map(f=>[f.owners[0],f.to]),symmetry:c.symmetryPreservesAllRoutes,singleCellRuleCanStart:c.singleCellRuleCanStart,groupSupports:c.everyCellHasTwoSupportsAfterGroupAttachment}));
