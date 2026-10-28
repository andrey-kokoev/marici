import test from 'node:test';
import assert from 'node:assert/strict';
import {buildFoldedFibration,foldedFibrationProcess,foldedFibrationStages} from '../research/realization-tower/fibration-folded-process.mjs';
import {buildNeutralExtension,zeroNeutralValues,validateNeutralValues,liftNeutralValues,inspectNeutralValues} from '../research/realization-tower/neutral-state-extension.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
const model=buildFoldedFibration(),extension=buildNeutralExtension(model.geometry);
function rank(rows){const a=rows.map(r=>[...r]);let r=0;for(let c=0;c<a[0].length;c++){let p=a.findIndex((v,i)=>i>=r&&v[c]!==0);if(p<0)continue;[a[p],a[r]]=[a[r],a[p]];const d=a[r][c];a[r]=a[r].map(x=>x/d);for(let i=0;i<a.length;i++)if(i!==r&&a[i][c]!==0){const f=a[i][c];a[i]=a[i].map((x,j)=>x-f*a[r][j]);}r++;}return r;}
test('declared direct-sum embedding has rank 126, not a duplicated 56-channel bank',()=>{
 const matrix=Array.from({length:128},()=>Array(126).fill(0));
 for(const [i,m] of extension.modes.entries())for(const e of m.embedding)matrix[e.coordinate][i]=e.weight;
 assert.equal(rank(matrix),126);assert.equal(extension.complexCoefficientCount,630);
 assert.equal(new Set(extension.modes.map(m=>m.id)).size,126);
 assert.equal(new Set(extension.modes.filter(m=>m.site).map(m=>m.site)).size,56);
 assert.equal(extension.physicalNeutronsEstablished,false);assert.equal(extension.derivedFromNativeReplay,false);
 assert.ok(extension.modes.filter(m=>m.site).every(m=>model.geometry.find(g=>g.id===m.site).kind==='octahedron'));
});
test('every complex coefficient of every channel can vary with P/E boundary fixed',()=>{
 for(let i=0;i<126;i++)for(let c=0;c<5;c++)for(let part=0;part<2;part++){
  const values=zeroNeutralValues();values[i][c][part]=1;
  const observed=inspectNeutralValues(extension,values),ambient=liftNeutralValues(extension,values);
  assert.equal(observed.activeChannels,1);
  assert.deepEqual(observed.boundaryDelta,{P:Array.from({length:5},()=>[0,0]),E:Array.from({length:5},()=>[0,0])});
  assert.ok(ambient.some(p=>p[c][part]!==0));
  if(i<56)assert.deepEqual(values[i+56],Array.from({length:5},()=>[0,0]));
 }
});
test('neutral stage preserves geometry, charged carrier and previous filler confirmation',()=>{
 const last=foldedFibrationStages.length-1,before=foldedFibrationProcess(7,last-1),values=zeroNeutralValues();values[125][4]=[2,-3];
 const after=foldedFibrationProcess(7,last,{neutralValues:values,selectedNeutralMode:125});
 assert.equal(before.fibrationAudit.neutral,null);assert.equal(after.fibrationAudit.neutral.counts.total,126);
 assert.deepEqual(after.retainedBodies,before.retainedBodies);assert.deepEqual(after.collectiveCells,before.collectiveCells);
 assert.deepEqual(after.fibrationAudit.filler.confirmation,before.fibrationAudit.filler.confirmation);
 assert.equal(after.canAdvance,false);assert.equal(after.fibrationAudit.neutral.activeChannels,1);
 assert.ok(after.presentationLabels.some(l=>l.text==='N*'));
});
test('complete independent packets persist and malformed records are rejected',()=>{
 const values=zeroNeutralValues();values[0][4]=[2,3];values[56][4]=[5,7];values[125][0]=[11,13];
 const saved=normalizeSceneSettings({neutralValues:values,selectedNeutralMode:125});
 assert.deepEqual(saved.neutralValues,values);assert.equal(saved.selectedNeutralMode,125);
 saved.neutralValues[0][4][0]=9;assert.equal(values[0][4][0],2);assert.equal(saved.neutralValues[56][4][0],5);
 assert.throws(()=>validateNeutralValues(new Array(126)),/complete/);
 assert.throws(()=>validateNeutralValues(values.slice(1)),/complete/);
 const bad=zeroNeutralValues();bad[0][0][0]=NaN;assert.throws(()=>validateNeutralValues(bad),/complete/);
 assert.deepEqual(normalizeSceneSettings({neutralValues:bad}).neutralValues,zeroNeutralValues());
 assert.throws(()=>buildNeutralExtension(model.geometry.filter(g=>g.id!==extension.modes[0].site)),/56 distinct/);
});
