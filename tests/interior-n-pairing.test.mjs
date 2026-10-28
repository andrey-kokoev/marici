import test from 'node:test';import assert from 'node:assert/strict';
import {interiorNPairing,decomposeInteriorN,reconstructInteriorN,probeInteriorNCancellation} from '../research/strominger/interior-n-pairing.mjs';
import {dualPoint} from '../research/strominger/pe-symmetric-sector.mjs';
const key=vs=>vs.map(p=>p.join(',')).sort().join('|');
test('85 actual interior N cells give 42 geometric inversion pairs and one fixed cell',()=>{
 const p=interiorNPairing(3),cells=new Map(p.cells.map(c=>[c.id,c]));assert.equal(p.cells.length,85);assert.equal(p.pairs.length,42);assert.deepEqual(p.fixed,['neutron:1,1,1,0']);assert.equal(new Set([...p.pairs.flat(),...p.fixed]).size,85);
 for(const[a,b]of p.pairs)assert.equal(key(cells.get(a).vertices.map(dualPoint)),key(cells.get(b).vertices));assert.equal(key(cells.get(p.fixed[0]).vertices.map(dualPoint)),key(cells.get(p.fixed[0]).vertices));
});
test('mean/contrast change of coordinates retains every amplitude and squared norm',()=>{
 const p=interiorNPairing(3),values=Object.fromEntries(p.cells.map((c,i)=>[c.id,i-42])),d=decomposeInteriorN(p,values);assert.deepEqual(reconstructInteriorN(d),values);assert.equal(d.originalNorm2,d.transformedNorm2);assert.equal(d.total,Object.values(values).reduce((a,b)=>a+b,0));
 const reversed=decomposeInteriorN({...p,pairs:p.pairs.map(([a,b])=>[b,a])},values);assert.equal(reversed.total,d.total);for(let i=0;i<d.pairs.length;i++)assert.equal(reversed.pairs[i].contrast,-d.pairs[i].contrast);
 assert.throws(()=>decomposeInteriorN(p,{}),/Missing finite/);
});
test('uniform occupancy remains 85; cancellation requires imposed opposite amplitudes',()=>{
 const p=probeInteriorNCancellation(3);assert.equal(p.uniform.total,85);assert.equal(p.opposedWithCentralOne.total,1);assert.equal(p.opposedWithCentralOne.norm2,85);assert.equal(p.opposedWithCentralOne.activePairs,42);assert.equal(p.axialOdd.total,0);assert.equal(p.axialOdd.activePairs,30);assert.equal(p.scalarCommonModes+p.scalarContrastModes,85);
});
