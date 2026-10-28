import * as T from 'three';
import {LineSegments2} from 'three/addons/lines/LineSegments2.js';
import {LineSegmentsGeometry} from 'three/addons/lines/LineSegmentsGeometry.js';
import {LineMaterial} from 'three/addons/lines/LineMaterial.js';
import {worldPoint} from '../../research/realization-tower/normal-ray-model.mjs';
import {transportColors} from '../../research/realization-tower/belt-layer-model.mjs';

export const insideNBorderStyle=Object.freeze({color:0xffffff,linewidth:3.5});

// One pickable mesh, centred at the model node. The normal convention is
// visual: P points toward the first ESD7, E toward the second; no wiring implied.
export function createBeltTransportLines(bodies,links){
 const byId=new Map(bodies.map(body=>[body.id,body])),positions=[],colors=[],tubes=new Map(),tubeTrunks=[];
 for(const edge of links){
  if(edge.kind!=='belt-transport')continue;
  const ends=[byId.get(edge.from),byId.get(edge.to)];
  if(ends.some(body=>!body||!(body.beltPort?.transportDirection in transportColors)&&!(body.beltTerminal&&edge.direction in transportColors)))continue;
  if(edge.tube){if(!tubes.has(edge.tube))tubes.set(edge.tube,[]);tubes.get(edge.tube).push(edge);continue;}
  for(const body of ends){positions.push(...worldPoint(body.point));colors.push(...new T.Color(transportColors[body.beltPort?.transportDirection??edge.direction]).toArray());}
 }
 // Shared trunks are presentation paths only, not extra graph nodes or field maps.
 for(const [id,edges] of tubes){
  const first=edges[0],terminal=worldPoint(byId.get(first.terminal).point),ends=edges.map(e=>worldPoint(byId.get(e.from===e.terminal?e.to:e.from).point)),mean=terminal.map((_,i)=>ends.reduce((s,p)=>s+p[i]/ends.length,0)),junction=terminal.map((v,i)=>v+.65*(mean[i]-v)),color=new T.Color(transportColors[first.direction]).toArray();
  const segment=(a,b)=>{positions.push(...a,...b);colors.push(...color,...color);};
  const outgoing=first.from===first.terminal;segment(...(outgoing?[terminal,junction]:[junction,terminal]));
  ends.forEach(p=>segment(...(outgoing?[junction,p]:[p,junction])));
  tubeTrunks.push({id,direction:first.direction,junction,lanes:edges.map(e=>e.lane),linkIds:edges.map(e=>e.id)});
 }
 const geometry=new T.BufferGeometry();geometry.setAttribute('position',new T.Float32BufferAttribute(positions,3));geometry.setAttribute('color',new T.Float32BufferAttribute(colors,3));
 const lines=new T.LineSegments(geometry,new T.LineBasicMaterial({vertexColors:true}));lines.userData.tubeTrunks=tubeTrunks;return lines;
}

export function createBeltSurface(surface,{wireOnly=false}={}){
 const group=new T.Group();group.userData.beltSurface=surface.id;
 const positions=[],colors=[],cellulation=surface.cellulation??surface;
 for(const f of cellulation.faces){const direction={proton:'P',electron:'E'}[f.colorRole];if(!direction)throw Error(`Missing belt face color: ${f.id}`);const color=new T.Color(transportColors[direction]).toArray();for(const i of f.indices){positions.push(...cellulation.vertices[i]);colors.push(...color);}}
 if(!wireOnly){const g=new T.BufferGeometry();g.setAttribute('position',new T.Float32BufferAttribute(positions,3));g.setAttribute('color',new T.Float32BufferAttribute(colors,3));group.add(new T.Mesh(g,new T.MeshBasicMaterial({vertexColors:true,side:T.DoubleSide,transparent:false,opacity:1,depthWrite:true})));}
 const g=new LineSegmentsGeometry().setPositions(cellulation.edges.flatMap(e=>e.indices.flatMap(i=>cellulation.vertices[i]))),outline=new LineSegments2(g,new LineMaterial({...insideNBorderStyle,worldUnits:false,depthTest:true,depthWrite:true}));outline.userData.sector='inside-N';group.add(outline);return group;
}

export function createBeltTerminal(body){
 const orb=new T.Mesh(new T.SphereGeometry(.085,12,8),new T.MeshBasicMaterial({color:body.color??0x76cfcf}));orb.position.set(...worldPoint(body.point));orb.userData.beltGlyph='terminal-bundle';orb.updateMatrixWorld(true);return orb;
}

export function createBeltNodeArrow(body){
 const direction=body.beltPort.transportDirection,axis=body.beltPort.normal;
 if(!(direction in transportColors))throw Error(`Unknown belt transport direction: ${direction}`);
 if(!axis||axis.length!==3||!axis.every(Number.isFinite)||Math.hypot(...axis)===0)throw Error('Belt arrow requires a nonzero finite normal');
 const profile=[[0,-.18],[.022,-.18],[.022,.05],[.075,.05],[0,.18]].map(([r,y])=>new T.Vector2(r,y));
 const arrow=new T.Mesh(new T.LatheGeometry(profile,12),new T.MeshBasicMaterial({color:transportColors[direction]}));
 const heading=new T.Vector3(...axis).normalize().multiplyScalar(direction==='P'?1:-1);
 arrow.quaternion.setFromUnitVectors(new T.Vector3(0,1,0),heading);
 arrow.position.set(...worldPoint(body.point));arrow.userData.beltGlyph='arrow';arrow.updateMatrixWorld(true);
 return arrow;
}
