// Isolated coherent diagonal alternatives; exact existing target-search replay.
import assert from 'node:assert/strict';
import {readFile,writeFile,readdir,mkdir,mkdtemp,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import path from 'node:path';
import {pathToFileURL,fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {spawnSync} from 'node:child_process';
const repo=path.resolve(fileURLToPath(new URL('../../../',import.meta.url))),demo='research/strominger/demos/particle-overlap-tetrahedron/',checks='research/strominger/checkers/',out='research/strominger/results/subdivision-dependence',hash=b=>createHash('sha256').update(b).digest('hex');
const literal='[[0,1,2,3],[3,0,1,2],[2,3,0,1],[1,2,3,0]]',perms=JSON.parse(literal);
const files=[...(await readdir(demo)).filter(f=>f.endsWith('.mjs')).map(f=>demo+f),'research/nima/generative-phase-assembly.mjs','research/nima/origin-bounded-assemblies.mjs',...['search_reference_n14.mjs','solve_reference_n14.py','check_reference_n14_search.mjs'].map(f=>checks+f)];
const originals=new Map();for(const f of files)originals.set(f,await readFile(f,'utf8'));
const protocolFile='research/strominger/subdivision-dependence-protocol-v1.md',protocolHash=hash(await readFile(protocolFile));
const key=vertices=>vertices.map(p=>p.join(',')).sort().join('|'),point=p=>p.join(',');
function* permutations(a){if(!a.length)yield [];for(const x of a)for(const p of permutations(a.filter(y=>y!==x)))yield [x,...p];}
const baselineItems=await import(pathToFileURL(path.join(repo,demo,'lattice-items.mjs'))),baselineComponents=await import(pathToFileURL(path.join(repo,demo,'simplex-components.mjs')));
const oldAssembly=baselineComponents.assembleComponents();
const faces=[[0,2,1],[0,1,3],[0,3,2],[1,2,3]];
function boundary(components){const table=new Map();for(const c of components)for(const f of faces){const k=key(f.map(i=>c[i]));table.set(k,(table.get(k)??0)+1);}assert.ok([...table.values()].every(n=>n<=2));return [...table].filter(([,n])=>n===1).map(([k])=>k).sort();}
function determinant(c){const [a,...rest]=c.map(v=>v.slice(0,3)),[u,v,w]=rest.map(p=>p.map((x,i)=>x-a[i]));return u[0]*(v[1]*w[2]-v[2]*w[1])-u[1]*(v[0]*w[2]-v[2]*w[0])+u[2]*(v[0]*w[1]-v[1]*w[0]);}
await mkdir(out,{recursive:true});const results=[];
for(const [name,spatial] of [['02-13',[0,1,2,3]],['01-23',[0,2,1,3]],['03-12',[0,1,3,2]]]){
 const root=await mkdtemp(path.join(tmpdir(),'marici-subdivision-'));const changes=[],snapshotHashes={};
 try{
  for(const [f,original] of originals){
   let text=original;
   if(['simplex-components.mjs','lattice-items.mjs'].some(s=>f===demo+s)){
    assert.equal(text.split(literal).length,2);text=text.replace(literal,JSON.stringify(perms.map(p=>spatial.map(i=>p[i]))));if(text!==original)changes.push(f);
   }
   await mkdir(path.dirname(path.join(root,f)),{recursive:true});await writeFile(path.join(root,f),text);snapshotHashes[f]=hash(text);
  }
  assert.deepEqual(changes,name==='02-13'?[]:[demo+'lattice-items.mjs',demo+'simplex-components.mjs'].sort((a,b)=>files.indexOf(a)-files.indexOf(b)));
  const local=await import(pathToFileURL(path.join(root,demo,'lattice-items.mjs'))),components=await import(pathToFileURL(path.join(root,demo,'simplex-components.mjs'))),windows=await import(pathToFileURL(path.join(root,demo,'window-construction-model.mjs')));
  const assembly=components.assembleComponents();assert.equal(assembly.components.length,oldAssembly.components.length);assert.deepEqual(assembly.components[0].addresses,oldAssembly.components[0].addresses);
  for(const [i,item] of assembly.items.entries()){
   const before=oldAssembly.items[i];assert.deepEqual({...item,children:[]},{...before,children:[]});
   const current=item.children.map(j=>assembly.components[j].addresses),previous=before.children.map(j=>oldAssembly.components[j].addresses);
   assert.equal(key([...new Map(current.flat().map(p=>[point(p),p])).values()]),key([...new Map(previous.flat().map(p=>[point(p),p])).values()]));assert.deepEqual(boundary(current),boundary(previous));current.forEach(c=>assert.equal(Math.abs(determinant(c)),1));
   if(item.kind==='octahedron'){
    assert.equal(current.length,4);const body=local.makeLatticeItem('octahedron',item.origin);assert.deepEqual(current.map(key).sort(),body.components.map(key).sort());
    const old=baselineItems.makeLatticeItem('octahedron',item.origin);assert.equal(body.key,old.key);assert.deepEqual(body.faces.map(key).sort(),old.faces.map(key).sort());
   }else assert.deepEqual(current,previous);
  }
  const seed=local.makeLatticeItem('tetrahedron',[0,0,0,0]),histogram={externalRegularEndpoint:0,internalSplitEndpoint:0};let canonical=null;
  for(const p of permutations([0,1,2,3])){
   const bindings=Object.fromEntries(['C0','M0','C1','M1'].map((k,i)=>[k,seed.vertices[p[i]]])),m=windows.createWindowConstruction({seed,bindings});m.step();const s=m.step();assert.equal(s.status,'complete');
   const whole=local.acrossFace(seed,s.events[0].face),external=whole.faces.some(f=>key(f)===key(s.events[1].face));histogram[external?'externalRegularEndpoint':'internalSplitEndpoint']++;
   if(JSON.stringify(p)==='[0,1,2,3]')canonical={bindings:s.bindings,externalRegularEndpoint:external,packet:s};
  }
  assert.deepEqual(histogram,{externalRegularEndpoint:8,internalSplitEndpoint:16});assert.ok(canonical);assert.deepEqual(Object.fromEntries(['C0','M0','C1','M1'].map(k=>[k,canonical.bindings[k]])),Object.fromEntries(['C0','M0','C1','M1'].map((k,i)=>[k,seed.vertices[i]])));
  console.log(JSON.stringify({diagonal:name,geometryValidated:true,canonicalExternal:canonical.externalRegularEndpoint,stage:'target-search'}));
  const child=spawnSync(process.execPath,[path.join(root,checks,'search_reference_n14.mjs')],{cwd:root,encoding:'utf8',timeout:720000,maxBuffer:4*1024*1024});await writeFile(out+'/'+name+'-search.log',child.stdout+'\n'+child.stderr);assert.equal(child.status,0,child.stderr??String(child.error));
  const cross=spawnSync(process.execPath,[path.join(root,checks,'check_reference_n14_search.mjs')],{cwd:root,encoding:'utf8',timeout:240000,maxBuffer:4*1024*1024});await writeFile(out+'/'+name+'-crosscheck.log',cross.stdout+'\n'+cross.stderr);assert.equal(cross.status,0,cross.stderr??String(cross.error));
  const resultDir=path.join(root,'research/strominger/results/reference-n14-search'),target=JSON.parse(await readFile(path.join(resultDir,'verification.json'))),crosscheck=JSON.parse(await readFile(path.join(resultDir,'crosscheck.json')));
  const artifactDir=out+'/'+name;await mkdir(artifactDir,{recursive:true});const artifactHashes={};for(const f of await readdir(resultDir)){const bytes=await readFile(path.join(resultDir,f));await writeFile(artifactDir+'/'+f,bytes);artifactHashes[f]=hash(bytes);}
  // Save changed modules and executable search/solver so alternatives can be
  // reconstructed exactly without mutating production or another owner.
  const snapshotDir=artifactDir+'/snapshot';for(const f of [...changes,...[checks+'search_reference_n14.mjs',checks+'solve_reference_n14.py',checks+'check_reference_n14_search.mjs']]){await mkdir(path.dirname(snapshotDir+'/'+f),{recursive:true});await writeFile(snapshotDir+'/'+f,await readFile(path.join(root,f)));}
  const querySummaries=[];for(const row of target.rows){const input=JSON.parse(await readFile(path.join(resultDir,`D${row.maxOrigin}-input.json`)));querySummaries.push({maxOrigin:row.maxOrigin,universePackets:row.universePackets,potentialBodiesBySpecies:Object.fromEntries(['proton','neutron','electron'].map(s=>[s,input.bodies.filter(b=>b.species===s).length])),potentialGeometricCells:new Set(input.bodies.map(b=>b.cell)).size,status:row.solver.status,witnessFile:row.witnessFile});}
  const result={diagonal:name,coordinatePermutation:spatial,changes,snapshotHashes,artifactHashes,geometry:{originalItems:assembly.items.length,primitiveCells:assembly.components.length,rootUnchanged:true,boundariesAndVolumesPreserved:true,coherentDiagonalAcrossAllOctahedra:true},localWindows:{histogram,canonical},search:{status:target.status,rows:querySummaries},smallSolverCrosscheck:{status:crosscheck.status,explicitConfigurations:crosscheck.explicitConfigurations,queries:crosscheck.controls.length}};results.push(result);await writeFile(artifactDir+'/comparison.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({diagonal:name,search:result.search}));
 }finally{await rm(root,{recursive:true,force:true});}
}
for(const [f,text] of originals)assert.equal(hash(await readFile(f)),hash(text),'Production source changed during experiment: '+f);assert.equal(hash(await readFile(protocolFile)),protocolHash);
await writeFile(out+'/verification.json',JSON.stringify({status:'uniform-subdivision-comparison-complete',protocolHash,originalSourceHashes:Object.fromEntries([...originals].map(([f,t])=>[f,hash(t)])),results,scope:'Three uniform diagonals, fixed root and unchanged prior reference rules. Geometry and local windows validated in isolated snapshots; target search origin bounds 3..10, first witness or complete bounded results. All D1 composition profiles cross-checked per subdivision. No arbitrary site-dependent subdivision search, global coupled-field sewing theorem, physical binding law or production/viewer change.'},null,2)+'\n');
