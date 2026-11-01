import {test} from 'node:test';
import assert from 'node:assert/strict';
import {Vector3,Euler,MathUtils} from 'three';
import {gridEdgeEuler,cellulationGridLabels} from '../examples/normal-ray/cellulation-grid-labels.js';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {buildCellulationNeighborhood,cellulationIncidentEdges} from '../research/realization-tower/cellulation-neighborhood.mjs';
test('XYZ Euler triples reconstruct all 12 outgoing FCC edge directions',()=>{
 const point=[0,0,0],grid=buildCellulationNeighborhood(buildCellulationStep(2).cells),edges=cellulationIncidentEdges(grid.edges,point);
 assert.equal(edges.length,12);
 for(const edge of edges){
  const other=edge.vertices.find(p=>p.some(x=>x!==0)),degrees=gridEdgeEuler(point,other);
  const reconstructed=new Vector3(1,0,0).applyEuler(new Euler(...degrees.map(MathUtils.degToRad),'XYZ'));
  assert(reconstructed.distanceTo(new Vector3(...other).normalize())<1e-12);
 }
 const labels=cellulationGridLabels({id:'seed',point,latticePoint:[0,0,0]},edges);
 assert.equal(labels.length,13);assert.equal(labels[0].text,'FCC (0, 0, 0)');
 labels.slice(1).forEach((label,i)=>{assert.match(label.text,/^XYZ \(.*°.*°.*°\)$/);assert.deepEqual(label.point,edges[i].vertices[0].map((x,j)=>(x+edges[i].vertices[1][j])/2));});
 assert.deepEqual(cellulationGridLabels({id:'seed',point,latticePoint:[0,0,0]},edges.map(e=>({...e,vertices:[...e.vertices].reverse()}))),labels);
});
