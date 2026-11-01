import {test} from 'node:test';
import assert from 'node:assert/strict';
import {cellulationGridVertices,pickCellulationGridVertex} from '../examples/normal-ray/cellulation-grid-picking.js';
test('grid vertex cache deduplicates shared endpoints using FCC coordinates',()=>{
 const a=[0,0,0],b=[1/Math.SQRT2,1/Math.SQRT2,0];
 const vertices=cellulationGridVertices([{vertices:[a,b]},{vertices:[b,a]}]);
 assert.equal(vertices.length,2);assert.deepEqual(vertices[1].latticePoint,[1,1,0]);
});
test('picking uses a fixed pixel radius, excludes placed dots and offscreen vertices, and favors frontmost ties',()=>{
 const vertices=[{key:'back',point:[0,0,.5]},{key:'front',point:[0,0,-.5]},{key:'clipped',point:[0,0,-2]}];
 const options={pointer:{x:50,y:50},width:100,height:100,project:p=>({x:p[0],y:p[1],z:p[2]})};
 assert.equal(pickCellulationGridVertex(vertices,options).key,'front');
 assert.equal(pickCellulationGridVertex(vertices,{...options,excluded:new Set(['front'])}).key,'back');
 assert.equal(pickCellulationGridVertex(vertices,{...options,excluded:new Set(['front','back'])}),null);
 assert.equal(pickCellulationGridVertex(vertices,{...options,pointer:{x:61,y:50}}),null);
 assert.equal(pickCellulationGridVertex(vertices,{...options,pointer:null}),null);
});
