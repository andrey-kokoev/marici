import {seed} from './normal-ray-model.mjs';
import {buildPESymmetricSector} from '../strominger/pe-symmetric-sector.mjs';
import {singleOctahedralEnvelope} from './single-octahedral-process.mjs';
const key=vs=>vs.map(v=>v.join(',')).sort().join('|');
let cached;
// The legacy process ID is retained for saved settings; the visible item is
// now 5-side oct. Historical Ru witness constructions remain separate research.
export function ruthenium98Process(k,step){
 if(step!==0)throw Error('5-side oct currently has one geometry stage');
 if(!cached){
  const sector=buildPESymmetricSector(2),boundary=new Set(sector.boundary.map(f=>key(f.vertices)));
  const bodies=sector.cells.map(c=>{const faces=c.faces.filter(f=>boundary.has(key(f)));return {...c,faces,faceRoles:Object.fromEntries(faces.map(f=>[key(f),c.role])),faceOpacity:.85,components:[],insideNSector:true,nativeWiring:{shape:'five-side-octahedron'}};});
  const row={id:'oct5-cells',label:'5-side oct cells',...Object.fromEntries(['proton','neutron','electron'].map(role=>[role,bodies.filter(c=>c.role===role).length])),total:bodies.length};
  const labels=['+P','−P','+N','−N','+E','−E'],roles=['proton','proton','neutron','neutron','electron','electron'];
  cached={bodies,row,ports:singleOctahedralEnvelope(2).map((point,i)=>({cell:`oct5:port:${i}`,point,text:labels[i],role:roles[i]})),graph:{nodes:bodies.map(body=>({id:body.id,body,position:body.vertices[0].map((_,i)=>body.vertices.reduce((s,p)=>s+p[i]/body.vertices.length,0))})),links:sector.faces.filter(f=>f.owners.length===2).map(f=>({from:f.owners[0],to:f.owners[1],kind:'native-face',directed:false}))},boundaryFaces:sector.boundary.length};
 }
 return {k:7,step,end:seed,assignments:[],firstRay:null,rays:[],faceNeighbors:[],faceVertexComparisons:[],neutronNeighbors:[],surfaceNeutronNeighbors:[],closureRounds:[],nextClosure:[],diamonds:[],conflicts:[],retainedBodies:cached.bodies,presentationLabels:cached.ports,interfaceGuides:[],nativeWiringGraph:cached.graph,
  presentationAudit:{nativeRealization:false,fixedCellSize:true},ruthenium98Audit:{shape:'octahedron',edgeUnits:5,baseCells:245,boundaryFaces:cached.boundaryFaces,template:'five-side-octahedron',outwardChains:false,inventoryCounts:cached.row},
  inventory:{rows:[cached.row],displayRows:[cached.row],records:cached.bodies,unit:'cells',unassigned:0,note:'Actual geometric cells of the five-edge octahedron; no isotope or witness counts.'},
  summary:'5-side oct · native octahedron · 245 cells · 80 P / 85 N / 80 E · Geometry / Lattice / Wiring.',canAdvance:false,history:[]};
}
