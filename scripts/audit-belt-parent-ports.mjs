import fs from 'node:fs/promises';
import {buildBeltParentPortInventory} from '../research/realization-tower/belt-parent-port-inventory.mjs';
const audit=buildBeltParentPortInventory(),path='research/strominger/results/belt-parent-port-inventory.json';
await fs.mkdir('research/strominger/results',{recursive:true});await fs.writeFile(path,JSON.stringify(audit,null,2)+'\n');
console.table(audit.summary);console.log(audit.status);for(const b of audit.blockers)console.log('-',b);console.log('No parent wiring installed. Receipt:',path);
