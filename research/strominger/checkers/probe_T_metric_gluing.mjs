// Explicit five-vertex quotient metric, tested against all 24 H reference charts.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const file='research/strominger/results/hydrogen-edge-attachment/verification.json',bytes=await readFile(file),samples=JSON.parse(bytes).rows;
const labels=['u','v','a','b','c'],q={C1:'u',M1:'v',C0:'a',M2:'a',M0:'b',C2:'c'},specs={proton:['C0','M0','C1','M1'],neutron:['M0','C1','M1','C2'],electron:['M1','C1','C2','M2']},facets=Object.fromEntries(Object.entries(specs).map(([s,ns])=>[s,ns.map(n=>q[n]).sort()]));
const pair=(a,b)=>[a,b].sort().join('|'),squared=(a,b)=>a.reduce((s,x,i)=>s+(x-b[i])**2,0);
function det(m){if(!m.length)return 1;if(m.length===1)return m[0][0];return m[0].reduce((s,x,i)=>s+(i%2?-1:1)*x*det(m.slice(1).map(r=>r.filter((_,j)=>j!==i))),0);}
const cycle={u:'u',v:'v',a:'b',b:'c',c:'a'},reflection={u:'v',v:'u',a:'a',b:'c',c:'b'},rows=[];
assert.deepEqual(facets.proton.map(x=>cycle[x]).sort(),facets.neutron);assert.deepEqual(facets.neutron.map(x=>cycle[x]).sort(),facets.electron);assert.deepEqual(facets.electron.map(x=>cycle[x]).sort(),facets.proton);
for(const sample of samples){
 const aliases=sample.bodies.find(b=>b.species==='electron').aliases,p=n=>aliases[n].split(',').map(Number),metric={},conflicts=[];
 for(const [species,ns] of Object.entries(specs))for(let i=0;i<ns.length;i++)for(let j=i+1;j<ns.length;j++){
  const key=pair(q[ns[i]],q[ns[j]]),value=squared(p(ns[i]),p(ns[j]));if(Object.hasOwn(metric,key)&&metric[key]!==value)conflicts.push({species,edge:key,existing:metric[key],proposed:value});else metric[key]=value;
 }
 assert.equal(Object.keys(metric).length,10);
 if(conflicts.length){rows.push({marking:sample.marking,electronGeometry:sample.electronGeometry,metricCompatible:false,conflicts});continue;}
 const D=(a,b)=>a===b?0:metric[pair(a,b)],others=labels.slice(1),twiceGram=others.map(a=>others.map(b=>D('u',a)+D('u',b)-D(a,b))),principal=[];
 for(let mask=1;mask<16;mask++){const indices=[0,1,2,3].filter(i=>mask&(1<<i));principal.push(det(indices.map(i=>indices.map(j=>twiceGram[i][j]))));}assert.ok(principal.every(x=>x>0));
 const reflectionIsometry=labels.every(a=>labels.every(b=>D(a,b)===D(reflection[a],reflection[b]))),cycleIsometry=labels.every(a=>labels.every(b=>D(a,b)===D(cycle[a],cycle[b])));
 rows.push({marking:sample.marking,electronGeometry:sample.electronGeometry,metricCompatible:true,metric,twiceGram,gramDeterminant:det(twiceGram)/16,allPrincipalMinorsPositive:true,minimumEuclideanDimension:4,reflectionIsometry,cycleIsometry});
}
assert.equal(rows.length,24);assert.ok(rows.every(r=>r.metricCompatible&&r.minimumEuclideanDimension===4));assert.equal(rows.filter(r=>r.reflectionIsometry).length,8);assert.ok(rows.every(r=>r.reflectionIsometry===(r.electronGeometry==='proton')));assert.ok(rows.every(r=>!r.cycleIsometry));
const out='research/strominger/results/T-metric-gluing';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'metric-seam-tested',source:file,sourceSha256:createHash('sha256').update(bytes).digest('hex'),checkerSha256:createHash('sha256').update(await readFile(new URL('./probe_T_metric_gluing.mjs',import.meta.url))).digest('hex'),quotient:q,facets,cycle,reflection,rows,coordinateProposal:{a:'realization',b:'M',c:'C',fixedByReader:{proton:'C',neutron:'realization',electron:'M'}},scope:'Identify C0/M2 as an abstract boundary seam and ask whether all intrinsic reader edge lengths extend to one Euclidean five-point metric. Positive Gram minors test existence of a 4D simplex whenever overlap metrics agree. Coordinates are barycentric-frame squared norms, proportional to physical squared lengths. Three facets share edge u/v. Facet labels can cycle combinatorially, but the actual metric is not cyclically invariant. a/b/c assignment to R/M/C is a convention compatible with the tested reversal, not a derived configuration-space chart or dynamics. Original spatial C0 and M2 remain distinct; no production/viewer changes.'},null,2)+'\n');console.log(JSON.stringify({compatible:rows.filter(r=>r.metricCompatible).length,incompatible:rows.filter(r=>!r.metricCompatible).length,reflectionIsometries:rows.filter(r=>r.reflectionIsometry).length,cyclicIsometries:rows.filter(r=>r.cycleIsometry).length,representative:rows.find(r=>r.metricCompatible)},null,2));
