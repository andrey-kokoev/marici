import fs from 'node:fs/promises';
import {traceBeltParentBranches} from '../research/realization-tower/belt-parent-branch-trace.mjs';
const audit=traceBeltParentBranches(),path='research/strominger/results/belt-parent-branch-trace.json';await fs.mkdir('research/strominger/results',{recursive:true});await fs.writeFile(path,JSON.stringify(audit,null,2)+'\n');
for(const p of audit.parents){console.log(p.copy,'endpoint',p.endpoint,'mediator',p.firstMediator);console.table(p.candidateRoots);console.log('Boundary root multiplicities',p.rootMultiplicityHistogram);}
console.log('Seam crossings:',Object.fromEntries(Object.entries(audit.crossings).map(([k,v])=>[k,v.length])));for(const f of audit.findings)console.log('-',f);console.log('Receipt:',path);
