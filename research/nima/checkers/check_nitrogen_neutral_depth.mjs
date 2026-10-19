import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {compile,solve,witness} from './check_nitrogen_alternative_placements.mjs';
const out='research/nima/results/nitrogen-neutral-depth';mkdirSync(out,{recursive:true});
const report={schema:'marici.nima.nitrogen-neutral-depth.v1',scope:'Exact 7P/7N/7e and 7P/8N/7e from seed. Local exit certificates only, not neutral-atom binding or global field sewing.',cases:[],resourceLimits:{maxNodes:1000000,maxMilliseconds:60000},sourceHashes:Object.fromEntries(['research/nima/checkers/check_nitrogen_neutral_depth.mjs','research/nima/checkers/check_nitrogen_alternative_placements.mjs','research/nima/origin-bounded-assemblies.mjs','research/nima/generative-phase-assembly.mjs'].map(p=>[p,createHash('sha256').update(readFileSync(p)).digest('hex')]))};
// Explicit resource-stop negative controls must never become UNSAT.
const control=compile(0);assert.equal(solve(control,{}, {maxNodes:0}).status,'incomplete');assert.equal(solve(control,{}, {maxMilliseconds:-1}).status,'incomplete');
for(const D of [3,4,5]){
 const f=compile(D),cases=[];
 for(const neutron of (D===5?[7]:[7,8])){
 const s=solve(f,{proton:7,neutron,electron:7},report.resourceLimits),{assignment,...meta}=s;
 const row={maxOrigin:D,counts:{proton:7,neutron,electron:7},...meta};
 if(assignment){row.witness=witness(f,assignment);assert.deepEqual(row.witness.counts,row.counts);assert.ok(row.witness.grade<=D);}
 if(D===3)assert.equal(row.status,'unsat');cases.push(row);console.log(JSON.stringify(row));
 }
 report.cases.push({maxOrigin:D,packetUniverse:f.universe.packets.length,variables:f.n,clauses:f.clauses.length,results:cases,registry:{root:f.g.root,packets:f.g.packets,charts:f.g.charts,cells:f.g.geometry.cells.map(({owner,...c})=>c),points:Object.fromEntries(f.g.geometry.points),operations:f.g.operations}});
 writeFileSync(out+'/verification.json',JSON.stringify(report,null,2)+'\n');
}
