// Interface-driven generation: source guards are compiled once, not consulted
// during search. PE policies come from the retained path-interface catalog.
import assert from 'node:assert/strict';
export function compileInterfaces(u,catalogCase){
 const g=u.rules,packets=u.packets,bit=packets.map((_,i)=>1n<<BigInt(i)),index=new Map(packets.map((p,i)=>[p,i])),cell=p=>g.charts[g.packets[p].chart].cell;
 for(const p of packets){assert.deepEqual(g.packets[p],catalogCase.registry.packets[p]);assert.deepEqual(g.charts[g.packets[p].chart],catalogCase.registry.charts[g.packets[p].chart]);}
 const mask=ids=>ids.reduce((m,p)=>m|bit[index.get(p)],0n),interfaces=u.operations.map(i=>{const o=g.operations[i];return {kind:o.kind,operation:i,source:o.source,target:o.target,permutation:o.permutation,forbidden:0n};});
 for(const r of catalogCase.records.filter(r=>r.contractedPolicy)){
 const p=r.contractedPolicy,forbidden=packets.filter(id=>p.requiredVacant.includes(cell(id))||p.forbiddenSelectedNativeSuccessors.includes(id));
 interfaces.push({kind:'experimental-terminal-PE',operation:r.id,source:r.source,target:r.target,permutation:r.permutation,factors:r.factors,forbidden:mask(forbidden)});
 }
 interfaces.forEach((o,i)=>{o.index=i;o.bit=1n<<BigInt(i);o.sourceBit=bit[index.get(o.source)];o.targetBit=bit[index.get(o.target)];o.required=o.sourceBit|o.targetBit;});
 const conflicts=packets.map(()=>0n);for(let i=0;i<packets.length;i++)for(let j=i+1;j<packets.length;j++)if(!g.describe([packets[i],packets[j]]).valid){conflicts[i]|=bit[j];conflicts[j]|=bit[i];}
 const watchers=bit.map(b=>interfaces.filter(o=>!!((o.required|o.forbidden)&b)));
 const enabled=(o,m)=>(m&o.required)===o.required&&!(m&o.forbidden);
 function update(active,m,p){for(const o of watchers[p])active=enabled(o,m)?active|o.bit:active&~o.bit;return active;}
 const root=bit[index.get(g.root)];
 function rooted(m,active){let reached=root;for(let changed=true;changed;){changed=false;for(const o of interfaces)if((active&o.bit)&&(reached&o.sourceBit)&&!(reached&o.targetBit)){reached|=o.targetBit;changed=true;}}return reached===m;}
 return {packets,bit,index,interfaces,conflicts,watchers,root,mask,enabled,update,rooted,decode:m=>packets.filter((_,i)=>!!(m&bit[i]))};
}
export function synthesize(c,{maxConfigurations=1000000}={}){
 let active=0n;for(const o of c.interfaces)if(c.enabled(o,c.root))active|=o.bit;
 const nodes=[{mask:c.root,active,parent:-1,added:-1}],byMask=new Map([[c.root,0]]),rejected=new Set();let lostRootCandidates=0,guardDisablingCandidates=0;
 for(let i=0;i<nodes.length;i++){
 const n=nodes[i];let targets=0n;for(const o of c.interfaces)if(n.mask&o.sourceBit)targets|=o.targetBit;targets&=~n.mask;
 for(let p=0;p<c.packets.length;p++){
 if(!(targets&c.bit[p])||(n.mask&c.conflicts[p]))continue;
 const m=n.mask|c.bit[p];if(byMask.has(m)||rejected.has(m))continue;
 const a=c.update(n.active,m,p);if(n.active&~a)guardDisablingCandidates++;
 if(!c.rooted(m,a)){rejected.add(m);lostRootCandidates++;continue;}
 if(nodes.length>=maxConfigurations)return {complete:false,reason:'configuration-resource-limit',nodes,byMask,lostRootCandidates,guardDisablingCandidates};
 byMask.set(m,nodes.length);nodes.push({mask:m,active:a,parent:i,added:c.packets[p]});
 }
 }
 return {complete:true,nodes,byMask,lostRootCandidates,guardDisablingCandidates};
}
