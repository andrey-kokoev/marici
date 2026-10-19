// Offline reference generation. Browser assets contain geometry, not search code.
import {readFile,writeFile,mkdir,readdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import assert from 'node:assert/strict';
const source=new URL('../demos/particle-overlap-tetrahedron/',import.meta.url);
const out=new URL('isotope-geometry/',source);
const hash=bytes=>createHash('sha256').update(bytes).digest('hex');
export async function prepareIsotopeGeometry({check=false}={}){
  const sourceHashes={};
  // Conservative dependency closure: all authored model modules plus this exporter.
  for(const name of (await readdir(source)).filter(n=>n.endsWith('.mjs')).sort())sourceHashes[name]=hash(await readFile(new URL(name,source)));
  sourceHashes['../../checkers/prepare_isotope_geometry.mjs']=hash(await readFile(new URL(import.meta.url)));
  const previous=await readFile(new URL('manifest.json',out),'utf8').then(JSON.parse).catch(()=>null);
  if(previous&&JSON.stringify(previous.sourceHashes)===JSON.stringify(sourceHashes)){
    let fresh=true;
    for(const [name,digest] of Object.entries(previous.assets))if(hash(await readFile(new URL(name,out)).catch(()=>Buffer.alloc(0)))!==digest)fresh=false;
    if(fresh)return previous;
  }
  if(check)throw Error('Isotope geometry is missing or stale; run prepare_isotope_geometry.mjs');
  const [{isotopeStructureData:records,isotopeStructureIds:ids},simplex,local,atom,phase]=await Promise.all([
    import(new URL('isotope-structure-data.mjs',source)),import(new URL('simplex-model.mjs',source)),
    import(new URL('local-reference-display.mjs',source)),import(new URL('atom-model.mjs',source)),import(new URL('phase-assembly-model.mjs',source))
  ]);
  const grid={nodes:simplex.lattice.nodes.map(n=>({address:n.address,point:n.point})),cells:simplex.lattice.cells};
  const nodeByAddress=new Map(grid.nodes.map((n,i)=>[JSON.stringify(n.address),i]));
  const cellKeys=new Set(grid.cells.map(c=>[...c].sort((a,b)=>a-b).join(',')));
  const assets={},pending=new Map();
  const stage=(name,value)=>{const bytes=JSON.stringify(value)+'\n';pending.set(name,bytes);assets[name]=hash(bytes);};
  stage('grid.json',grid);
  for(const id of ids){
    const start=performance.now();let items,validation;
    if(local.localReferenceIds.includes(id)){
      const snapshot=local.createLocalReferenceDisplay(id).snapshot();
      items=snapshot.items.map(i=>({species:i.species,cells:i.components.map(c=>c.map(a=>nodeByAddress.get(JSON.stringify(a))))}));
      validation='local-reference-display';
    }else if(['hydrogen','deuterium'].includes(id)){
      items=atom.makeAtom(id).bodies.map(b=>({species:b.species,cells:[b.nodeIds]}));validation='atom-model';
    }else{
      // createPhaseAssembly performs the source phase/certificate audit.
      const snapshot=phase.createPhaseAssembly(id).snapshot();
      assert.equal(snapshot.phaseAudit.status,'phase-coherent-reference');
      items=snapshot.items.map(i=>({species:i.species,cells:i.components.map(c=>c.map(a=>nodeByAddress.get(JSON.stringify(a))))}));
      validation='phase-coherent-reference';
    }
    for(const [species,key] of [['proton','protons'],['neutron','neutrons'],['electron','electrons']])assert.equal(items.filter(i=>i.species===species).length,records[id][key],`${id}: ${species} count`);
    for(const item of items){assert.ok(['proton','neutron','electron'].includes(item.species));for(const cell of item.cells){assert.equal(cell.length,4);assert.ok(cell.every(n=>Number.isInteger(n)&&grid.nodes[n]?.point.every(Number.isFinite)));assert.ok(cellKeys.has([...cell].sort((a,b)=>a-b).join(',')),`${id}: non-native cell`);}}
    stage(`${id}.json`,{schema:'marici.isotope-geometry.v1',isotope:id,validation,coordinateFrame:'native isotope construction',items});
    console.log(`${id}: validated ${items.length} items (${Math.round(performance.now()-start)} ms)`);
  }
  const manifest={schema:'marici.isotope-geometry-manifest.v1',source:'research/strominger/demos/particle-overlap-tetrahedron',sourceHashes,assets,isotopes:ids,scope:'Validated display geometry from source constructions; no physical binding or R-space placement claim.'};
  await mkdir(out,{recursive:true});
  for(const [name,bytes] of pending)await writeFile(new URL(name,out),bytes);
  // Manifest last: incomplete writes cannot pass freshness checks.
  await writeFile(new URL('manifest.json',out),JSON.stringify(manifest,null,2)+'\n');
  return manifest;
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))await prepareIsotopeGeometry({check:process.argv.includes('--check')});
