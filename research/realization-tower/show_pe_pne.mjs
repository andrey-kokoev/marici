import assert from 'node:assert/strict';
import {writeFile} from 'node:fs/promises';
import {makeAtom} from '../strominger/demos/particle-overlap-tetrahedron/atom-model.mjs';
import {lattice,worldPoint,cellNeighbors} from '../strominger/demos/particle-overlap-tetrahedron/simplex-model.mjs';
import {createWindowConstruction} from '../strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {itemKey} from '../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
const model=createWindowConstruction();model.step();const triple=model.step();assert.equal(triple.status,'complete');
const keys=lattice.cells.map(c=>itemKey(c.map(i=>lattice.nodes[i].address)));
const root=keys.indexOf(triple.items[0].key);assert(root>=0);
const pair=makeAtom('hydrogen',root);
const shapes=[pair.bodies.map(b=>({species:b.species,cell:b.cellId,vertices:lattice.cells[b.cellId].map(i=>lattice.nodes[i].address)})),triple.items.map(b=>({species:b.species,cell:keys.indexOf(b.key),vertices:b.vertices}))];
assert(shapes.flat().every(b=>b.cell>=0));
const shared=(a,b)=>a.vertices.filter(p=>b.vertices.some(q=>itemKey([p])===itemKey([q])));
assert.equal(shared(...shapes[0]).length,3);assert.equal(shared(shapes[1][0],shapes[1][1]).length,3);assert.equal(shared(shapes[1][1],shapes[1][2]).length,3);assert.equal(shared(shapes[1][0],shapes[1][2]).length,2);
const colors={proton:'#46b6e0',neutron:'#edb65d',electron:'#ed80c2'},symbol={proton:'P',neutron:'N',electron:'E'};
const edges=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]],faces=[[0,1,2],[0,1,3],[0,2,3],[1,2,3]];
const project=p=>{const [x,y,z]=worldPoint(p);return [0.82*x-0.57*y,-0.30*x-0.43*y+0.85*z,0.49*x+0.70*y+0.52*z];};
let svg='<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="650" viewBox="0 0 1100 650"><rect width="1100" height="650" fill="#101923"/><style>text{font-family:Arial,sans-serif;fill:#edf5ff}.small{font-size:16px}.title{font-size:25px;font-weight:bold}</style><text x="35" y="40" class="title">Same lattice, same proton seed — two configurations</text>';
const panels=[];
for(let k=0;k<2;k++){
 const bodies=shapes[k],points=bodies.flatMap(b=>b.vertices.map(project));
 const min=[0,1].map(i=>Math.min(...points.map(p=>p[i]))),max=[0,1].map(i=>Math.max(...points.map(p=>p[i])));
 const scale=Math.min(340/(max[0]-min[0]),330/(max[1]-min[1]));
 const plot=p=>{const q=project(p);return [275+550*k+(q[0]-(min[0]+max[0])/2)*scale,295-(q[1]-(min[1]+max[1])/2)*scale];};
 const coords=ps=>ps.map(p=>plot(p).map(x=>x.toFixed(2)).join(',')).join(' ');
 const line=(a,b,color,width,opacity=1)=>{const u=plot(a),v=plot(b);return `<line x1="${u[0]}" y1="${u[1]}" x2="${v[0]}" y2="${v[1]}" stroke="${color}" stroke-width="${width}" opacity="${opacity}"/>`;};
 svg+=`<svg x="${550*k}" y="65" width="550" height="430" viewBox="${550*k} 65 550 430">`;
 const nearby=[...new Set(bodies.flatMap(b=>cellNeighbors(b.cell)))].filter(i=>i>=0&&!bodies.some(b=>b.cell===i));
 for(const id of nearby){const v=lattice.cells[id].map(i=>lattice.nodes[i].address);for(const [a,b] of edges)svg+=line(v[a],v[b],'#8294aa',1,.16);}
 const polys=bodies.flatMap(b=>faces.map(f=>({b,points:f.map(i=>b.vertices[i]),depth:f.reduce((s,i)=>s+project(b.vertices[i])[2],0)/3}))).sort((a,b)=>a.depth-b.depth);
 for(const f of polys)svg+=`<polygon points="${coords(f.points)}" fill="${colors[f.b.species]}" fill-opacity=".22"/>`;
 for(const b of bodies)for(const [a,c] of edges)svg+=line(b.vertices[a],b.vertices[c],colors[b.species],2.5);
 const interfaces=[];
 for(let i=0;i<bodies.length;i++)for(let j=i+1;j<bodies.length;j++){
  const s=shared(bodies[i],bodies[j]);interfaces.push({pair:[symbol[bodies[i].species],symbol[bodies[j].species]],vertices:s});
  if(s.length===3)svg+=`<polygon points="${coords(s)}" fill="#91f0ae" fill-opacity=".16" stroke="#a3ffbc" stroke-width="3"/>`;
  if(s.length===2)svg+=line(s[0],s[1],'#ffffff',4);
 }
 for(const b of bodies){const center=b.vertices[0].map((_,i)=>b.vertices.reduce((s,p)=>s+p[i]/4,0)),q=plot(center);svg+=`<circle cx="${q[0]}" cy="${q[1]}" r="19" fill="#101923" stroke="${colors[b.species]}" stroke-width="2"/><text x="${q[0]}" y="${q[1]+7}" text-anchor="middle" font-size="23">${symbol[b.species]}</text>`;}
 svg+='</svg>';
 svg+=`<text x="${35+550*k}" y="520" class="title">${k?'P–N–E triple':'P–E pair'}</text>`;
 const lines=k?['P/N and N/E share complete faces.','P/E share an edge (white), not a face.','Marked-window construction; not the pair plus a hidden N.']:['P and E share one complete face (green).','Actual neighbouring lattice primitives.','Existing occupancy rule; phase compatibility not asserted.'];
 lines.forEach((s,i)=>svg+=`<text x="${35+550*k}" y="${551+i*25}" class="small">${s}</text>`);
 panels.push({bodies,interfaces});
}
svg+='<line x1="550" y1="75" x2="550" y2="620" stroke="#465568"/><text x="35" y="640" font-size="14">Faint edges: neighbouring lattice cells. Colours: P blue · N gold · E pink. No new particle or duality rule introduced.</text></svg>';
await writeFile(new URL('./pe-pne-lattice.svg',import.meta.url),svg);
await writeFile(new URL('./results/pe-pne-lattice.json',import.meta.url),JSON.stringify({panels,bindings:triple.bindings,sourcePair:'atom-model.makeAtom(hydrogen, native proton seed)',sourceTriple:'window-construction-model.createWindowConstruction'},null,2)+'\n');
console.log('PASS: face-attached PE; native PN and NE faces; PE edge in triple. Saved pe-pne-lattice.svg');
