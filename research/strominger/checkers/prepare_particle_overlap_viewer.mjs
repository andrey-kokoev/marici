// Targeted publisher: only this experiment's two new public directories.
import {readFile,writeFile,mkdir,copyFile,stat} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {prepareIsotopeGeometry} from './prepare_isotope_geometry.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const source=path.join(root,'research/strominger/demos/particle-overlap-tetrahedron');
const receiptPath='research/strominger/results/cmc-mcm-identity-attachment/verification.json';
const receiptBytes=await readFile(path.join(root,receiptPath)),receipt=JSON.parse(receiptBytes);
const hash=bytes=>createHash('sha256').update(bytes).digest('hex');
if(receipt.status!=='pass'||!Object.values(receipt.checks).every(Boolean))throw new Error('Identity attachment receipt has not passed');
for(const [file,digest] of Object.entries(receipt.source_sha256))if(hash(await readFile(path.join(root,file)))!==digest)throw new Error('Stale identity attachment source: '+file);
const identityData={schema:'marici.identity-viewer-data.v1',source_receipt:receiptPath,receipt_sha256:hash(receiptBytes),verified_checks:Object.keys(receipt.checks).length,
  original_walk:receipt.original_source_snapshot.walk,exact_points:receipt.exact_points,
  windows:receipt.windows.map(w=>({role:w.role,ordered_vertices:w.ordered_vertices,anchor:w.anchor,walk_occurrence_ids:w.walk_occurrence_ids,explicit_extra_closure:w.explicit_extra_closure,
    modes:Object.fromEntries(Object.entries(w.mode_records).map(([mode,r])=>[mode,{label:r.label,eigenvalue:r.eigenvalue,source_window:r.source_window}]))})),
  transitions:receipt.transitions.map(t=>({from:t.from,to:t.to,anchor_displacement:t.anchor_displacement,mode_transport:t.mode_transport,cyclic_target_convention:t.cyclic_target_convention})),
  scope:'Verified source geometry and conditional adapters, not physical particle identification or an isometry of every display chart.'};
await writeFile(path.join(source,'identity-data.mjs'),'// Generated from the verified attachment receipt; do not hand-edit.\nexport default '+JSON.stringify(identityData,null,2)+';\n');
// Preserve the previous planar implementation as an explicit comparison only.
if(!await stat(path.join(source,'planes.html')).catch(()=>null)) {
  const previous=await readFile(path.join(root,'public/experiments/particle-overlap-tetrahedron/vacuum.html'),'utf8');
  if(!previous.includes('vacuum-app.js'))throw new Error('Expected owned planar snapshot for migration');
  await writeFile(path.join(source,'planes.html'),previous.replace('<a class="view-link" href="./face-space.html">Face realizations ↗</a>','<a class="view-link" href="./vacuum.html">Three R axes ↗</a>').replace('href="./vacuum.html" aria-current="page"','href="./planes.html" aria-current="page"'));
}
const files=['tessellated-space.html','tessellated-space-viewer.js','tessellated-space.js','isotope-geometry-loader.js','isotope-structure-data.mjs','index.html','style.css','model.mjs','app.js','identity.mjs','identity-data.mjs','carrier.mjs','vacuum.html','vacuum.css','vacuum-model.mjs','vacuum-app.js','vacuum-carriers.mjs','face-space.html','planes.html','realization-model.mjs','realization-app.js','realization.css','simplex-model.mjs','simplex-components.mjs','simplex-app.js','atom-model.mjs','fiber-space-model.mjs','fiber-space-app.js','lead208-model.mjs','lattice-items.mjs','sequential-space-model.mjs','window-construction-model.mjs','fiber-coverage-model.mjs','deuterium-tunnel-model.mjs','helium3-tunnel-model.mjs','helium4-core-probe.mjs','helium4-window-model.mjs','assembly-display-model.mjs','phase-discipline-model.mjs','phase-advance-model.mjs','phase-assembly-model.mjs','nitrogen15-reference.mjs','local-reference-data.mjs','local-reference-display.mjs','local-reference-rules.mjs','local-reference-universe.mjs','lithium6-assembly-model.mjs','edge-segments.mjs','vendor/lines/LineSegmentsGeometry.js','vendor/lines/LineMaterial.js','vendor/lines/LineSegments2.js','vendor/lines/UPSTREAM.json','vendor/lines/LICENSE'];
const geometryManifest=await prepareIsotopeGeometry();
files.push('isotope-geometry/manifest.json',...Object.keys(geometryManifest.assets).map(name=>'isotope-geometry/'+name));
const vendors=['three.min.js','OrbitControls.js','THREE-LICENSE.txt'];
const lineUpstream=JSON.parse(await readFile(path.join(source,'vendor/lines/UPSTREAM.json'),'utf8'));
for(const entry of lineUpstream.files)if(hash(await readFile(path.join(source,'vendor/lines',entry.file)))!==entry.sha256)throw Error('Modified upstream line addon: '+entry.file);
const owner={owner:'marici.Strominger',source:'research/strominger/demos/particle-overlap-tetrahedron',generator:'research/strominger/checkers/prepare_particle_overlap_viewer.mjs'};
for(const dir of ['public/experiments/particle-overlap-tetrahedron','website/public/experiments/particle-overlap-tetrahedron']) {
  const target=path.join(root,dir),marker=path.join(target,'.owner.json');
  if(await stat(target).catch(()=>null)) {
    const previous=JSON.parse(await readFile(marker,'utf8'));
    if(previous.owner!==owner.owner||previous.source!==owner.source)throw new Error('Ownership mismatch: '+dir);
  }
  await mkdir(path.join(target,'vendor','lines'),{recursive:true});
  await mkdir(path.join(target,'isotope-geometry'),{recursive:true});
  for(const file of files)await copyFile(path.join(source,file),path.join(target,file));
  for(const file of vendors)await copyFile(path.join(root,'research/nima/demos/paw-cycle/vendor',file),path.join(target,'vendor',file));
  await writeFile(marker,JSON.stringify(owner,null,2)+'\n');
}
console.log(JSON.stringify({status:'prepared',route:'/experiments/particle-overlap-tetrahedron/',targets:2,local_three:true}));
