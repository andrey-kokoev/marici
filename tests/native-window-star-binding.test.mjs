import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';
import {decodeChannel,encodeFixture} from '../research/strominger/checkers/native_retained_channel.mjs';
import {nativeWindowStarView,auditNativeWindowStarViews} from '../research/strominger/native-window-star-binding.mjs';
import {buildCentralBeltLayout} from '../research/realization-tower/central-belt-layout.mjs';
const f=decodeChannel(encodeFixture(JSON.parse(fs.readFileSync(new URL('../research/strominger/results/joint-field-sewing-fixture.json',import.meta.url),'utf8')))),layout=buildCentralBeltLayout();
const permutations=xs=>xs.length?xs.flatMap((x,i)=>permutations(xs.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
test('every real native packet has one source-selected three-plus-context star on both layouts',()=>{
 for(const index of [0,5]){const result=auditNativeWindowStarViews(f,layout.layers[index]);assert.equal(result.status,'native-selected-window-bound');assert.equal(result.composition.status,'verified-conditionally');assert.deepEqual(result.counts,{packets:14,selectedWindows:14,alternativeGeometricContexts:42});
  for(const v of result.views){assert.equal(v.rows.length,12);const selected=v.stars.filter(s=>s.selectedByProtocol);assert.equal(selected.length,1);assert.equal(selected[0].contextMark,v.protocol.continuation);assert.deepEqual(selected[0].orderedNativeWindow.map(id=>selected[0].satellites.find(s=>s.node===id).targetMark),v.protocol.window);assert.equal(v.packetRef.permutation.length,5);assert.equal(v.stars.filter(s=>s.admission==='alternative-geometric-context-only').length,3);}
 }
});
test('all 24 local marking orders preserve the actual native face and context while recording arm order',()=>{
 const layer=layout.layers[0],base=nativeWindowStarView(f,f.rootPacket,layer);for(const marks of permutations(base.marks)){const v=nativeWindowStarView(f,f.rootPacket,layer,{markOrder:marks}),selected=v.stars.find(s=>s.selectedByProtocol);assert.equal(selected.contextVertex,base.context.vertex);assert.deepEqual(selected.orderedNativeWindow.map(id=>selected.satellites.find(s=>s.node===id).targetVertex),base.window.map(w=>w.vertex));assert.deepEqual(v.packetRef,base.packetRef);}
});
test('fixed-carrier coordinates reveal changed context without erasing distinct histories',()=>{
 const r=auditNativeWindowStarViews(f,layout.layers[0]),root=f.packets.find(p=>p.id===f.rootPacket),cell=f.charts.find(c=>c.index===root.chart).cell,c=r.perCarrierContexts.find(c=>c.cell===cell);assert.deepEqual(c.observedContextIndices,[1,3]);assert.ok(c.packets.length>2);assert.ok(new Set(c.packets.map(p=>p.origin)).size>1);
 const exits=r.views.filter(v=>v.protocol.species==='electron');assert.equal(exits.length,2);for(const v of exits){assert.equal(v.context.mark,'M2');assert.equal(v.packetRef.permutation.length,5,'geometric context does not replace the five native coefficients');}
});
test('forged aliases, dropped history references and invented marks are not hidden by geometry',()=>{
 const bad=structuredClone(f),root=bad.packets.find(p=>p.id===bad.rootPacket),chart=bad.charts.find(c=>c.index===root.chart);chart.aliases.M1='not-a-native-vertex';assert.throws(()=>nativeWindowStarView(bad,bad.rootPacket,layout.layers[0]));
 assert.throws(()=>nativeWindowStarView(f,f.rootPacket,layout.layers[0],{markOrder:['C0','M0','C1','invented']}));assert.throws(()=>nativeWindowStarView(f,'unknown',layout.layers[0]));
 const v=nativeWindowStarView(f,f.rootPacket,layout.layers[0]);assert.equal(v.historyPositions.length,2);assert.equal(new Set(v.historyPositions.map(p=>p.history)).size,2);for(const row of v.rows)assert.deepEqual(row.payload.historyPositions,v.historyPositions);
});
