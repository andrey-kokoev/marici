import fs from 'node:fs/promises';
import {auditFrontierAttachments} from '../research/realization-tower/edge-frontier-attachments.mjs';
const cases=[];
for(let k=2;k<=7;k++)for(const branch of [1,3])cases.push(auditFrontierAttachments(k,branch));
const output=new URL('../research/realization-tower/results/edge-frontier-attachments-v1.json',import.meta.url);
await fs.mkdir(new URL('.',output),{recursive:true});
await fs.writeFile(output,JSON.stringify({status:'PASS',scope:'Attachment dependency audit; no new assignments',cases},null,2)+'\n');
console.log(JSON.stringify(cases.find(c=>c.k===4&&c.branch===1),null,2));
console.log(`PASS ${cases.length} frontier audits`);
