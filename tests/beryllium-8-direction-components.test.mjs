import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildBeryllium8Reference} from '../research/realization-tower/beryllium-8-reference.mjs';
import {buildBranchingSeed} from '../research/realization-tower/branching-seed.mjs';
import {buildSulfurRouteComparison,projectComparisonColumns} from '../research/realization-tower/sulfur-route-comparison.mjs';
import {buildBerylliumDirectionComponents} from '../research/realization-tower/beryllium-8-direction-components.mjs';
const reference=buildBeryllium8Reference(),columns=buildSulfurRouteComparison(buildBranchingSeed({processId:'beryllium-8'}),{reference}).reference;
const rows=buildBerylliumDirectionComponents(columns);
test('direction selects components without reversing paths, edges, identities or slots',()=>{
 const snapshot=JSON.stringify(columns);assert.equal(rows.length,2);
 for(const row of rows){
  assert.equal(row.columns.length,8);
  for(const [i,s] of row.columns.entries()){
   const original=columns[i];
   for(const key of ['id','column','label','inputSlot','outputSlot','polarityDirection'])assert.equal(s[key],original[key]);
   for(const key of ['polarities','guide','edgeIds','paths'])assert.deepEqual(s[key],original[key]);
   for(const removed of ['readingReversed','polarityReadDirection','readFromSlot','readToSlot','colourOrder'])assert.equal(removed in s,false);
  }
 }
 assert.equal(JSON.stringify(columns),snapshot);assert.deepEqual(reference,buildBeryllium8Reference());
});
test('four mixed strands select two white and two red, swapped in opposite direction',()=>{
 assert.deepEqual(rows[0].columns.map(s=>s.selectedComponent),['white','white','white','red','red','white','blue','blue']);
 assert.deepEqual(rows[1].columns.map(s=>s.selectedComponent),['white','white','red','white','white','red','blue','blue']);
 for(const row of rows){
  const mixed=row.columns.filter(s=>s.componentSelected);
  assert.equal(mixed.length,4);assert.equal(mixed.filter(s=>s.selectedComponent==='white').length,2);assert.equal(mixed.filter(s=>s.selectedComponent==='red').length,2);
  for(const s of row.columns){
   assert.equal(s.colours.length,1);assert.deepEqual(s.sourceColours,columns[s.column].colours);
   if(s.componentSelected){
    assert.equal(s.selectionSign,s.polarityDirection*(s.polarities.t==='+'?1:-1)*row.direction);
    assert.equal(s.colours[0],s.selectionSign===1?0xffffff:0xff3030);
   }
  }
 }
 for(let i=0;i<8;i++){
  if(columns[i].polarityDirection)assert.notDeepEqual(rows[0].columns[i].colours,rows[1].columns[i].colours);
  else assert.deepEqual(rows[0].columns[i].colours,rows[1].columns[i].colours);
 }
 for(const i of [2,3,4,5])assert.deepEqual(columns[i].colours,[0xffffff,0xff3030]);
});
test('display alignment, original geometry and three midpoint arrows remain identical in both copies',()=>{
 const original=projectComparisonColumns(columns);
 for(const row of rows)for(const s of projectComparisonColumns(row.columns)){
  assert.equal(s.x,original[s.column].x);assert.deepEqual(s.paths,original[s.column].paths);
  const path=s.paths[0];assert.equal(path.polarityArrows.length,3);
  for(const arrow of path.polarityArrows){assert.equal(arrow.kind,s.polarityDirection?'polarity':'route');assert.equal(arrow.direction,s.polarityDirection||1);}
  for(const [i,arrow] of path.polarityArrows.entries())assert.deepEqual(arrow.centre,path.coordinates[i].map((x,j)=>(x+path.coordinates[i+1][j])/2));
 }
});
test('rejects incomplete or foreign reference columns',()=>{
 assert.throws(()=>buildBerylliumDirectionComponents(columns.slice(1)));
 assert.throws(()=>buildBerylliumDirectionComponents([...columns.slice(1),columns[1]]));
 assert.throws(()=>buildBerylliumDirectionComponents(columns.map(s=>({...s,id:s.id.replace('be8:','su32:')}))));
});
