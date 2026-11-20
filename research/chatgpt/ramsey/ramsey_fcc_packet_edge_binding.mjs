// Actual validated packet paths. Read the FCC site of the current C1 alias and independently track its initial coefficient.
import assert from 'node:assert/strict';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
const names=['C0','M0','C1','M1'];const perm=a=>a.length?a.flatMap(x=>perm(a.filter(y=>y!==x)).map(p=>[x,...p])):[[]];
const coord=(r,id)=>r.charts[r.packets[id].chart].aliases.C1.split(',').map(x=>2-Number(x));
function sector(p,q){let d=q.map((u,i)=>u-p[i]);return d.filter(v=>v===1).length===1&&d.filter(v=>v===-1).length===1&&d.filter(v=>v===0).length===2?[d.indexOf(-1),d.indexOf(1)]:null;}
let seeds=0,starts=0,paths=0,moving=0,diagonals=0,samePacket=0,held=0;const kinds=new Map();
for(const p of perm([0,1,2,3])){
 const aliases=Object.fromEntries(names.map((x,j)=>[x,[0,1,2,3].map(k=>+(k===p[j])).join(',')]));
 const r=new GenerativeAssemblyRules({seedBindings:aliases});seeds++;
 const out=id=>r.outgoing(id).map(i=>r.operations[i]);const n=out(r.root).find(o=>o.kind==='PN').target;
 for(const id of [r.root,n]){starts++;let list=[];
 for(const op of out(id)){
 assert(r.validateTransfer(op));const h=sector(coord(r,id),coord(r,op.target));const fixed=op.permutation[2]===2;const key=JSON.stringify([op.kind,h?'moves':coord(r,id).join()==coord(r,op.target).join()?'stays':'nonroot',fixed]);kinds.set(key,(kinds.get(key)??0)+1);
 for(const next of out(op.target)){assert(r.validateTransfer(next));paths++;let j=sector(coord(r,op.target),coord(r,next.target));if(!h||!j)continue;moving++;if(new Set([...h,...j]).size!==4)continue;
 diagonals++;list.push({h:h.join(),j:j.join(),end:next.target});if(fixed&&next.permutation[2]===2)held++;
 }}for(const x of list)for(const y of list)if(x.h===y.j&&x.j===y.h&&x.end===y.end)samePacket++;
 }}
console.log({seeds,starts,paths,moving,diagonals,held,samePacket});console.log(Object.fromEntries(kinds));
