import test from 'node:test';import assert from 'node:assert/strict';
import {buildBeltLayers} from '../research/realization-tower/belt-layer-model.mjs';
import {encodeBlockAddress,decodeBlockAddress,instantiateBlockWiring,reverseBlockWiring} from '../research/realization-tower/belt-wiring.mjs';
const model=()=>buildBeltLayers({origin:[0,0,0],x:[1,0,0],y:[0,1,0],normal:[0,0,1]});
test('symbolic bundle and branch addresses recover every fine address',()=>{
 for(let row=0;row<4;row++)for(let column=0;column<4;column++)assert.deepEqual(decodeBlockAddress(encodeBlockAddress({row,column})),{row,column});
 assert.throws(()=>encodeBlockAddress({row:4,column:0}));
});
test('selected central triangles connect only to their single matching square nodes',()=>{
 const m=model(),nodes=new Map(m.layers.flatMap(l=>l.nodes).map(n=>[n.id,n]));
 for(const [triangle,square,direction] of [[3,2,'P'],[4,5,'E']]){
  const wires=m.links.filter(e=>nodes.get(e.from).layer===triangle&&nodes.get(e.to).layer===square&&e.direction===direction);assert.equal(wires.length,3);assert.equal(new Set(wires.map(e=>e.to)).size,1);assert.equal(new Set(wires.map(e=>e.branch.vertex)).size,3);
  for(const e of wires){assert.equal(e.direction,direction);assert.equal(nodes.get(e.from).direction,direction);assert.equal(nodes.get(e.to).direction,direction);assert.equal(nodes.get(e.from).group,3);}
  assert.equal(m.links.filter(e=>[e.from,e.to].some(id=>nodes.get(id).layer===triangle)&&[e.from,e.to].some(id=>nodes.get(id).layer===square)).length,12);
 }
});
test('majority bundles interleave while minority triangles retain symbolic bundle wiring',()=>{
 const m=model(),byId=new Map(m.layers.flatMap(l=>l.nodes).map(n=>[n.id,n]));assert.equal(new Set(m.links.map(e=>[e.from,e.to].sort().join('|'))).size,74);
 for(const [square,triangle] of [[m.layers[1],m.layers[2]],[m.layers[4],m.layers[3]]])for(const target of square.nodes){
  const wires=m.links.filter(e=>e.outer===target.id&&byId.get(e.inner)?.layer===triangle.layer);assert.equal(wires.length,3);const interleaved=wires[0].sourceAddress!==undefined;
  assert.equal(new Set(wires.map(e=>e.group)).size,interleaved?3:1);
  if(interleaved){assert.equal(new Set(wires.map(e=>byId.get(e.inner).vertex)).size,1);assert.equal(new Set(wires.map(e=>e.branch.lane)).size,3);}
  else {const group=wires[0].group;assert.equal(triangle.bundleSlots[group],2*target.row+target.column);}
  for(const e of wires){assert.equal(e.direction,target.direction);assert.equal(byId.get(e.inner).direction,target.direction);const delta=byId.get(e.to).position[2]-byId.get(e.from).position[2];assert.ok(delta*(e.direction==='P'?1:-1)>0);}
 }
});
test('each interleaved triangle receives all three sources with reversible branch addresses',()=>{
 const m=model();for(const wiring of m.wiring.filter(w=>w.rule==='three-bundle-transpose')){
  assert.equal(wiring.branches.length,9);assert.equal(new Set(wiring.branches.map(e=>`${e.branch.bundle}:${e.branch.lane}`)).size,9);
  for(const group of new Set(wiring.branches.map(e=>e.group)))assert.equal(new Set(wiring.branches.filter(e=>e.group===group).map(e=>e.from)).size,3);
  for(const e of wiring.branches)assert.deepEqual({bundle:e.destinationAddress.vertex,lane:e.destinationAddress.triangle},e.sourceAddress);
  assert.deepEqual(reverseBlockWiring(reverseBlockWiring(wiring)),wiring);
 }
});
test('central exchange connects every star to every opposite star in both directions',()=>{
 const m=model(),byId=new Map(m.layers.flatMap(l=>l.nodes).map(n=>[n.id,n]));
 for(const [from,to,direction] of [[3,4,'E'],[4,3,'P']]){
  const wires=m.links.filter(e=>byId.get(e.from).layer===from&&byId.get(e.to).layer===to);assert.equal(wires.length,9);assert.equal(new Set(wires.map(e=>e.from)).size,9);assert.equal(new Set(wires.map(e=>e.to)).size,3);
  for(const id of new Set(wires.map(e=>e.to))){const incoming=wires.filter(e=>e.to===id);assert.equal(incoming.length,3);assert.equal(new Set(incoming.map(e=>e.sourceAddress.star)).size,3);}
  for(let star=0;star<3;star++){
   const outgoing=wires.filter(e=>byId.get(e.from).star===star),incoming=wires.filter(e=>byId.get(e.to).star===star);
   assert.equal(outgoing.length,3);assert.deepEqual([...new Set(outgoing.map(e=>byId.get(e.to).star))].sort(),[0,1,2]);
   assert.equal(incoming.length,3);assert.deepEqual([...new Set(incoming.map(e=>byId.get(e.from).star))].sort(),[0,1,2]);
  }
  for(const e of wires){const source=byId.get(e.from),target=byId.get(e.to);assert.equal(source.direction,direction);assert.equal(target.direction,direction);assert.equal(source.starCentre,false);assert.equal(target.starCentre,true);assert.deepEqual(e.branch,{group:source.group,vertex:source.vertex});assert.deepEqual(e.sourceAddress,{star:source.star,arm:source.arm});assert.deepEqual(e.destinationAddress,{star:target.star,centre:true});assert.ok((target.position[2]-source.position[2])*(direction==='P'?1:-1)>0);
   const reciprocal=m.links.find(r=>byId.get(r.from).layer===to&&byId.get(r.to).layer===from&&byId.get(r.from).star===target.star&&byId.get(r.to).star===source.star);assert.ok(reciprocal);assert.equal(target.star,source.arm);assert.equal(byId.get(reciprocal.from).arm,source.star);
  }
  const record=m.wiring.find(w=>w.rule==='three-star-complete-exchange-with-retained-branch'&&w.outerLayer===from);assert.deepEqual(reverseBlockWiring(reverseBlockWiring(record)),record);
 }
});
test('central four minority arrows feed the star centre; rim arrows form three retained fours',()=>{
 const m=model();for(const [outer,inner,minority] of [[m.layers[0],m.layers[1],'P'],[m.layers[5],m.layers[4],'E']]){
  const w=instantiateBlockWiring(outer,inner),byId=new Map([...outer.nodes,...inner.nodes].map(n=>[n.id,n]));assert.equal(w.rule,'central-block-and-three-rim-bundles');
  assert.equal(w.branches.filter(e=>e.region==='centre').length,4);assert.equal(w.branches.filter(e=>e.region==='perimeter').length,12);
  for(const edge of w.branches){const source=byId.get(edge.outer),target=byId.get(edge.inner),central=edge.region==='centre';assert.equal(source.direction===minority,central);assert.equal(target.direction===minority,central);if(central)assert.ok(Math.hypot(...target.local)<1e-10);assert.equal([1,2].includes(edge.fineAddress.row)&&[1,2].includes(edge.fineAddress.column),central);}
  assert.equal(new Set(w.branches.map(e=>`${e.fineAddress.row}:${e.fineAddress.column}`)).size,16);
 }
});
test('L1/L2 star wiring is directed, reversible and arm-aligned on both halves',()=>{
 const m=model(),nodes=new Map(m.layers.flatMap(l=>l.nodes).map(n=>[n.id,n])),before=JSON.stringify(m);
 for(const [outer,inner] of [[m.layers[0],m.layers[1]],[m.layers[5],m.layers[4]]]){
  const wiring=instantiateBlockWiring(outer,inner);if(outer.rotationDegrees===0)assert.deepEqual(wiring,instantiateBlockWiring({...outer,kind:'grid'},inner));
  for(const edge of wiring.branches){const node=nodes.get(edge.outer),target=nodes.get(edge.inner);assert.equal(target.slot,inner.starSlots[node.starCentre?3:node.arm],'every satellite connects to its corresponding star arm');}assert.equal(wiring.branches.length,16);assert.equal(new Set(wiring.branches.map(e=>e.outer)).size,16);
  for(const node of inner.nodes){const branches=wiring.branches.filter(e=>e.inner===node.id);assert.equal(branches.length,4);assert.equal(new Set(branches.map(e=>`${e.branch.row}:${e.branch.column}`)).size,4);}
  for(const edge of wiring.branches){const source=nodes.get(edge.from),target=nodes.get(edge.to);assert.equal(source.direction,target.direction);assert.ok((target.position[2]-source.position[2])*(edge.direction==='P'?1:-1)>0);}
  const reversed=reverseBlockWiring(wiring);assert.deepEqual(reverseBlockWiring(reversed),wiring);assert.equal(reversed.branches[0].from,wiring.branches[0].to);
 }
 assert.equal(JSON.stringify(m),before);assert.equal(m.links.length,74);assert.equal(m.wiring.length,8);
 for(const pair of [[1,2],[5,6]])assert.equal(m.links.filter(e=>pair.includes(nodes.get(e.from).layer)&&pair.includes(nodes.get(e.to).layer)).length,16);
});
