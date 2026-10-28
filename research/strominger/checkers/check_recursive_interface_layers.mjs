// Recursive interface expansion in a PL tetrahedral collar.
// Radial levels are semantic layers, NOT primitive lattice spacing or species.
// The center and exterior stay fixed; old collar layers are reparameterized.
import assert from 'node:assert/strict';
const indices=[0,1,2,3],roles=['P','E','N','N'];
const unit=indices.map(i=>indices.map(j=>12*(i===j?1:0)-3));
let nextLayer=0,nextInterface=0;
const link=(left,right)=>({id:`interface-${nextInterface++}`,left:left.id,right:right.id});
const center={id:'central-P',kind:'center',type:'P'};
const surface={id:'retained-surface',kind:'surface',types:roles};
const initialCollar={id:`coherence-${nextLayer++}`,kind:'coherence',type:null,origin:'initial inserted layer'};
let layers=[center,initialCollar,surface];
let interfaces=layers.slice(1).map((r,i)=>link(layers[i],r));
const history=[];
function expand(){
 const oldLayers=layers,oldInterfaces=interfaces,newLayers=[];
 for(let i=0;i<oldLayers.length;i++){
  newLayers.push(oldLayers[i]);
  if(i<oldInterfaces.length)newLayers.push({id:`coherence-${nextLayer++}`,kind:'coherence',type:null,expandedInterface:oldInterfaces[i]});
 }
 layers=newLayers;interfaces=layers.slice(1).map((r,i)=>link(layers[i],r));
 assert.equal(layers.length,2*oldLayers.length-1);
 assert.deepEqual(layers.filter((_,i)=>i%2===0),oldLayers);
 for(let i=0;i<oldInterfaces.length;i++){
  assert.deepEqual(layers[2*i+1].expandedInterface,oldInterfaces[i]);
  assert.equal(interfaces[2*i].left,oldInterfaces[i].left);
  assert.equal(interfaces[2*i+1].right,oldInterfaces[i].right);
 }
 history.push({retainedLayers:oldLayers.map(l=>l.id),expandedInterfaces:oldInterfaces,insertedLayers:layers.filter((_,i)=>i%2).map(l=>l.id)});
}
const key=xs=>[...xs].sort().join('|');
const det=(a,b,c)=>a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]);
function geometry(){
 const bands=layers.slice(1,-1),B=bands.length,points={};
 // Coordinates below are integers; divide by B to compare physical positions
 // across runs. Then inner/outer radii are always 1 and 2.
 for(let r=0;r<=B;r++)for(const v of indices)points[`r${r}v${v}`]=unit[v].map(x=>(B+r)*x);
 for(const i of indices)points[`cap${i}`]=unit[i].map(x=>-10*B*x/3);
 const face=(r,i)=>indices.filter(j=>j!==i).map(j=>`r${r}v${j}`);
 const cells=[{id:center.id,layer:center.id,vertices:indices.map(j=>`r0v${j}`)}];
 for(let r=0;r<B;r++)for(const i of indices){
  const [a,b,c]=indices.filter(j=>j!==i),lo=v=>`r${r}v${v}`,hi=v=>`r${r+1}v${v}`;
  const pieces=[[lo(a),lo(b),lo(c),hi(c)],[lo(a),lo(b),hi(b),hi(c)],[lo(a),hi(a),hi(b),hi(c)]];
  pieces.forEach((vertices,j)=>cells.push({id:`${bands[r].id}/face${i}/piece${j}`,layer:bands[r].id,vertices}));
 }
 for(const i of indices)cells.push({id:`boundary-${i}`,layer:surface.id,type:roles[i],vertices:[...face(B,i),`cap${i}`]});
 const volume6=cell=>{
  const vs=cell.vertices.map(v=>points[v].slice(0,3));
  return Math.abs(det(...vs.slice(1).map(v=>v.map((x,j)=>x-vs[0][j]))));
 };
 const table=new Map();
 for(const cell of cells){
  assert.ok(volume6(cell)>0);
  for(const i of indices){const f=key(cell.vertices.filter((_,j)=>j!==i));if(!table.has(f))table.set(f,[]);table.get(f).push(cell);}
 }
 assert.ok([...table.values()].every(owners=>owners.length<=2));
 assert.equal(cells.filter(c=>bands.some(b=>b.id===c.layer)).reduce((s,c)=>s+volume6(c),0),7*volume6(cells[0]));
 // Every inter-layer face crosses an immediate semantic interface, no shortcuts.
 const counts=new Map(),position=new Map(layers.map((l,i)=>[l.id,i]));
 for(const owners of table.values())if(owners.length===2&&owners[0].layer!==owners[1].layer){
  const p=owners.map(c=>position.get(c.layer)).sort((a,b)=>a-b);
  assert.equal(p[1]-p[0],1);
  counts.set(p[0],(counts.get(p[0])??0)+1);
 }
 assert.equal(counts.size,interfaces.length);
 assert.ok([...counts.values()].every(n=>n===4));
 // Only three outward faces on each retained cap remain exposed.
 const exposed=[...table.values()].filter(os=>os.length===1);
 assert.equal(exposed.length,12);
 assert.ok(exposed.every(os=>os[0].layer===surface.id));
 // Physical center and cap vertex coordinates never change.
 assert.deepEqual(cells[0].vertices.map(v=>points[v].map(x=>x/B)),unit);
 for(const i of indices)assert.deepEqual(points[`cap${i}`].map(x=>x/B),unit[i].map(x=>-10*x/3));
 return {layerCount:layers.length,coherenceBands:B,untypedTetrahedra:12*B,totalTetrahedra:cells.length,interfaces:interfaces.length,facesPerInterface:4,externalFaces:12,collarVolumeInCentralUnits:7,layerIds:layers.map(l=>l.id)};
}
const stages=[geometry()];
for(let i=0;i<3;i++){expand();stages.push(geometry());}
assert.deepEqual(stages.map(s=>s.layerCount),[3,5,9,17]);
console.log(JSON.stringify({
 scope:'Recursive PL interface expansion after the initial three-layer construction',
 stages,history,
 checks:{oldLayerIdentitiesRetained:true,eachOldInterfaceBecomesOneLayer:true,conformingFacesAndSixEdgeSeams:true,noInterLayerShortcuts:true,centerAndSurfaceFixed:true,collarVolumeFixed:true},
 limitations:['P/N/E types of inserted cells are not assigned','Old coherence bands are compressed/reparameterized; their metric embedding is not retained','Radii are rational and band widths shrink: this is not one-unit growth or an esd7 primitive filling','The initial 1-to-3 step is a separate seed construction, not generated by the interface recurrence'],
 typingForced:false
},null,2));
