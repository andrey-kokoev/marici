import {buildPESymmetricSector,neutralCentre,dualPoint} from './pe-symmetric-sector.mjs';
const axis=[1,-1,-1,1],key=ps=>ps.map(p=>p.join(',')).sort().join('|'),mean=ps=>ps[0].map((_,i)=>ps.reduce((s,p)=>s+p[i]/ps.length,0));
const tally=cs=>Object.fromEntries(['proton','neutron','electron'].map(r=>[r,cs.filter(c=>c.role===r).length]));
// An explicit trial growth rule, NOT a signed-field law: retain every shortest
// shared-face path between the two native cells at the facing E-labelled poles.
export function probeOctahedralNativeBridge(radius=2,extraShell=0){
 if(!Number.isInteger(radius)||radius<0||radius>2||![0,1].includes(extraShell))throw Error('Probe radius 0..2 and extra shell 0 or 1 required');
 const parent=buildPESymmetricSector(radius),ambient=buildPESymmetricSector(2*radius+1+extraShell),byGeometry=new Map(ambient.cells.map(c=>[key(c.vertices),c])),byId=new Map(ambient.cells.map(c=>[c.id,c])),parentSets=[];
 for(const sign of [1,-1]){const ids=new Set();for(const cell of parent.cells){const vertices=cell.vertices.map(p=>p.map((x,i)=>x+sign*(radius+1)*axis[i])),found=byGeometry.get(key(vertices));if(!found||found.role!==cell.role)throw Error('Parent not registered on common native lattice');ids.add(found.id);}parentSets.push(ids);}
 if([...parentSets[0]].some(id=>parentSets[1].has(id)))throw Error('Parents overlap');
 const terminals=[1,-1].map(sign=>ambient.cells.find(c=>c.kind==='octahedron'&&mean(c.vertices).every((x,i)=>Math.abs(x-neutralCentre[i]-sign*axis[i])<1e-9))?.id);
 if(terminals.some((id,i)=>!id||!parentSets[i].has(id)))throw Error('Missing pole cell');
 const blocked=new Set(parentSets.flatMap(s=>[...s]).filter(id=>!terminals.includes(id))),adj=new Map(ambient.cells.filter(c=>!blocked.has(c.id)).map(c=>[c.id,[]]));
 for(const f of ambient.faces)if(f.owners.length===2&&f.owners.every(id=>adj.has(id))){const[a,b]=f.owners;adj.get(a).push(b);adj.get(b).push(a);}
 const distances=start=>{const ds=new Map([[start,0]]),queue=[start];for(let i=0;i<queue.length;i++)for(const next of adj.get(queue[i]))if(!ds.has(next)){ds.set(next,ds.get(queue[i])+1);queue.push(next);}return ds;};
 const from=distances(terminals[0]),to=distances(terminals[1]),length=from.get(terminals[1]);if(length===undefined)throw Error('No face-connected bridge');
 const corridor=ambient.cells.filter(c=>from.has(c.id)&&to.has(c.id)&&from.get(c.id)+to.get(c.id)===length),corridorIds=new Set(corridor.map(c=>c.id)),bridge=corridor.filter(c=>!terminals.includes(c.id)),selected=new Set([...parentSets[0],...parentSets[1],...corridorIds]);
 const connections=ambient.faces.filter(f=>f.owners.length===2&&f.owners.every(id=>selected.has(id))),attachmentFaces=connections.filter(f=>f.owners.some(id=>corridorIds.has(id)&&!terminals.includes(id))&&f.owners.some(id=>parentSets.some(s=>s.has(id))));
 const boundary=ambient.faces.filter(f=>f.owners.filter(id=>selected.has(id)).length===1),edgeCounts=new Map();for(const f of boundary)for(let i=0;i<3;i++){const k=key([f.vertices[i],f.vertices[(i+1)%3]]);edgeCounts.set(k,(edgeCounts.get(k)??0)+1);}
 const dualClosed=corridor.every(c=>corridorIds.has(byGeometry.get(key(c.vertices.map(dualPoint)))?.id));
 const paths=new Map([[terminals[0],1n]]);for(const c of [...corridor].sort((a,b)=>from.get(a.id)-from.get(b.id)))for(const next of adj.get(c.id))if(corridorIds.has(next)&&from.get(next)===from.get(c.id)+1)paths.set(next,(paths.get(next)??0n)+(paths.get(c.id)??0n));
 return {radius,parentCellIds:parentSets.map(s=>[...s]),edgeUnits:parent.edgeUnits,translation:axis.map(x=>(radius+1)*x),terminals,bridgeCells:bridge,corridorCells:corridor,assemblyCells:[...selected].map(id=>byId.get(id)),boundary,connections,attachmentFaces,audit:{parentCells:parent.cells.length,bridgeCells:bridge.length,bridgeRoles:tally(bridge),assemblyCells:selected.size,assemblyRoles:tally([...selected].map(id=>byId.get(id))),shortestFaceSteps:length,shortestPaths:String(paths.get(terminals[1])),distanceLayers:Array.from({length:length+1},(_,i)=>tally(corridor.filter(c=>from.get(c.id)===i))),dualClosed,attachmentFaces:attachmentFaces.length,sharedFaceLinks:connections.length,nonmanifoldBoundaryEdges:[...edgeCounts.values()].filter(n=>n!==2).length,pointOnlyLinks:0,scope:'Common-lattice all-shortest-path corridor under an explicit adjacency-growth assumption. No inherited belt, target counts, port-dependent transport or unique physical selection.'}};
}
