import test from 'node:test';
import assert from 'node:assert/strict';
import * as T from 'three';
import {buildSulfurIncomingBundle} from '../research/realization-tower/sulfur-32-incoming-bundle.mjs';
import {buildPESymmetricSector} from '../research/strominger/pe-symmetric-sector.mjs';
import {worldPoint} from '../research/realization-tower/normal-ray-model.mjs';
import {createSulfurChannelCutaway} from '../examples/normal-ray/sulfur-channel-cutaway.js';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
test('cutaway hollows chambers and carves connected passages through native walls',()=>{
 const model=buildSulfurIncomingBundle(),before=JSON.stringify(model),mesh=createSulfurChannelCutaway(model),sample=mesh.userData.sampleSolid;
 assert.equal(mesh.userData.audit.carrierCells,51);assert.equal(mesh.userData.audit.passages,63);
 assert.equal(mesh.userData.audit.surfaceGrooves,52);assert.equal(mesh.userData.audit.interiorPassages,11);
 assert(mesh.userData.audit.triangles>0);assert.equal(mesh.geometry.attributes.position.count,mesh.userData.audit.triangles*3);
 for(const passage of mesh.userData.passages){assert(sample(passage.start.clone().lerp(passage.end,.5))<0);assert(sample(passage.start)<0);assert(sample(passage.end)<0);}
 for(const strand of model.strands)for(const run of strand.edgeRuns)for(const p of run.points)assert(sample(new T.Vector3(...worldPoint(p)))<0);
 const sector=buildPESymmetricSector(1),centre=new T.Vector3(...worldPoint(sector.centre));
 assert(sample(centre.clone().add(new T.Vector3(0,-.5,0)))<0);
 // Every cell centre is empty, rather than rendered as one filled block.
 for(const c of sector.cells)assert(sample(new T.Vector3(...worldPoint(c.vertices[0].map((_,i)=>c.vertices.reduce((sum,p)=>sum+p[i]/c.vertices.length,0)))))<0);
 assert(sector.cells.some(c=>c.faces.some(face=>sample(new T.Vector3(...worldPoint(face[0].map((_,i)=>face.reduce((sum,p)=>sum+p[i]/face.length,0)))))>0)));
 assert.equal(mesh.userData.audit.kind,'honeycomb-walls-minus-wire-passages');
 assert.equal(mesh.userData.audit.wallThickness,.08);
 assert.equal(mesh.userData.audit.openExterior,true);assert(mesh.userData.audit.passageSurfaceVertices>1000);
 for(const x of mesh.geometry.attributes.position.array)assert(Number.isFinite(x));
 assert.equal(JSON.stringify(model),before);mesh.geometry.dispose();mesh.material.dispose();
});
test('full exterior and adjustable cut are independent persisted view settings',()=>{
 const model=buildSulfurIncomingBundle(),full=createSulfurChannelCutaway(model,{cut:1,resolution:48,openExterior:false}),cut=createSulfurChannelCutaway(model,{cut:.5,resolution:48});
 assert.notEqual(full.userData.audit.triangles,cut.userData.audit.triangles);
 const settings=normalizeSceneSettings({appearance:{sulfurChannels:true,sulfurChannelCut:.7}});assert(settings.appearance.sulfurChannels);assert.equal(settings.appearance.sulfurChannelCut,.7);assert.equal(settings.appearance.sulfurWireBundle,false);
 for(const m of [full,cut]){m.geometry.dispose();m.material.dispose();}
});
