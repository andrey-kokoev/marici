// Three.js renderer for the declared R-layer lattice and exact-node P/N/E cells.
// Geometry comes only from vacuum-model.mjs and vacuum-carriers.mjs; this is a
// visualization adapter, not a physical-space or particle-dynamics claim.
import {makeSpace} from './vacuum-model.mjs';
import {latticeCarriers} from './vacuum-carriers.mjs';
import {orientedVolume} from './carrier.mjs';

const TETRA_FACES=[0,2,1,0,1,3,0,3,2,1,2,3];
const colorHex=value=>`#${value.toString(16).padStart(6,'0')}`;
function rotateAddress([q,r],steps){for(let n=((steps%6)+6)%6;n>0;n--)[q,r]=[q-r,q];return [q,r];}
function repeatedPNECells(space,level){
  const seed=latticeCarriers(space,'all',level);
  if(seed.status!=='constructed')return seed;
  const steps=space.parameters.turn/60;
  if(Math.abs(steps-Math.round(steps))>1e-10)return {...seed,status:'blocked',obstruction:'PNE repetition requires a multiple-of-60° lattice rotation.'};
  const turn=Math.round(steps),triangles=[];
  // Each of four unit parallelograms contributes both complementary triangles.
  for(let q=0;q<2;q++)for(let r=0;r<2;r++){
    triangles.push({q,r,orientation:'up',vertices:[[q,r],[q+1,r],[q+1,r+1]]});
    triangles.push({q,r,orientation:'down',vertices:[[q,r],[q,r+1],[q+1,r+1]]});
  }
  const frames=space.frames,points={},bindings={},bodies=[],edges=[];
  const siteMaps=new Map(frames.map(frame=>[frame.level,new Map(space.patch.sites.map(([q,r],i)=>[`${q},${r}`,{point:frame.points[i],siteIndex:i}]))]));
  const lowerNames=['C0','M0','C1'],upperNames=['M1','C2','M2'];
  for(let fi=0;fi<frames.length-1;fi++){
    const lower=frames[fi],upper=frames[fi+1],template=latticeCarriers(space,'all',lower.level);
    if(template.status!=='constructed')return template;
    for(const tile of triangles){
      const prefix=`R${lower.level}-${tile.q}${tile.r}-${tile.orientation}`;
      const names={};
      for(let i=0;i<3;i++){
        const [q,r]=tile.vertices[i],mapped=rotateAddress([q,r],-turn);
        for(const [name,frame,address] of [[lowerNames[i],lower,[q,r]],[upperNames[i],upper,mapped]]){
          const hit=siteMaps.get(frame.level)?.get(`${address[0]},${address[1]}`);
          if(!hit)return {...seed,status:'blocked',obstruction:`PNE tiling requires absent node (${address.join(',')}) at R=${frame.level}.`};
          const id=`${prefix}:${name}`;names[name]=id;points[id]=hit.point;
          bindings[id]={level:frame.level,q:address[0],r:address[1],siteIndex:hit.siteIndex,unitCell:[tile.q,tile.r],triangle:tile.orientation};
        }
      }
      for(const body of template.bodies){
        const nodes=body.nodes.map(name=>names[name]),id=`${prefix}-${body.id}`;
        bodies.push({...body,id,nodes,repeat:[tile.q,tile.r,tile.orientation],level:lower.level,volume:Math.abs(orientedVolume(nodes,points))});
        for(let i=0;i<nodes.length;i++)for(let j=i+1;j<nodes.length;j++)edges.push([nodes[i],nodes[j]]);
      }
    }
  }
  return {...seed,points,bindings,bodies,
    edges:[...new Map(edges.map(edge=>[edge.slice().sort().join('|'),edge])).values()],
    repeatCount:triangles.length*(frames.length-1),trianglesPerLayer:triangles.length,
    repeatShape:'Both complementary triangular prisms in each 2x2 axial parallelogram, repeated across every adjacent R-layer pair.',
    tilingExtent:{axialParallelograms:[2,2],RIntervals:frames.length-1}};
}

/**
 * Build a Three.js Group displaying the 2x2 axial PNE column. Its cross-section
 * is tiled by complementary up/down triangular prisms; each prism is the
 * existing three-tetrahedron P/N/E chain. Every displayed vertex references
 * an actual model lattice node; no snapping or interpolated vertices are used.
 */
export function createTessellatedSpace(THREE,{level=0,opacity=.24,...spaceOptions}={}) {
  if(!THREE?.Group||!THREE?.BufferGeometry)throw new TypeError('A loaded Three.js namespace is required');
  const space=makeSpace(spaceOptions),group=new THREE.Group();group.name='2x2 PNE realization column';
  const objects=[];
  const addLine=(pairs,color,alpha=1)=>{
    if(!pairs.length)return;
    const geometry=new THREE.BufferGeometry().setFromPoints(pairs.flatMap(pair=>pair.map(p=>new THREE.Vector3(...p))));
    const material=new THREE.LineBasicMaterial({color,transparent:alpha<1,opacity:alpha,depthWrite:false});
    const line=new THREE.LineSegments(geometry,material);group.add(line);objects.push(line);return line;
  };
  // Only show the two adjacent planes surrounding the selected interval.
  const displayedFrames=space.frames.filter(frame=>frame.level===level||frame.level===level+1);
  for(const frame of displayedFrames){
    addLine(space.patch.edges.map(([a,b])=>[frame.points[a],frame.points[b]]),0x9cc6ce,frame.level===level?.38:.16);
    addLine([[[0,frame.origin[1],0],[0,frame.origin[1]+.12,0]]],0xa4efd0,.8);
  }
  const cells=repeatedPNECells(space,level);
  if(cells.status==='constructed'){
    const positionsBySpecies={proton:[],neutron:[],electron:[]};
    for(const body of cells.bodies){
      const species=['proton','neutron','electron'].find(name=>body.id.endsWith(`-${name}`));
      for(const index of TETRA_FACES)positionsBySpecies[species].push(...cells.points[body.nodes[index]]);
    }
    for(const [species,positions] of Object.entries(positionsBySpecies)){
      const geometry=new THREE.BufferGeometry().setAttribute('position',new THREE.Float32BufferAttribute(positions,3));geometry.computeVertexNormals();
      const color=cells.bodies.find(body=>body.id.endsWith(`-${species}`)).color;
      const material=new THREE.MeshBasicMaterial({color,side:THREE.DoubleSide,transparent:true,opacity,depthWrite:false});
      const mesh=new THREE.Mesh(geometry,material);mesh.name=`batched ${species} PNE cells`;group.add(mesh);objects.push(mesh);
    }
    addLine(cells.edges.map(([a,b])=>[cells.points[a],cells.points[b]]),0xf0eee2,.72);
    const nodeGeometry=new THREE.BufferGeometry().setFromPoints(Object.values(cells.points).map(point=>new THREE.Vector3(...point)));
    const nodePoints=new THREE.Points(nodeGeometry,new THREE.PointsMaterial({color:0xffdfaa,size:.07,sizeAttenuation:true}));nodePoints.name='PNE lattice nodes';group.add(nodePoints);objects.push(nodePoints);
  }
  return {group,space,cells,status:cells.status,obstruction:cells.obstruction??null,
    dispose(){for(const object of objects){object.geometry?.dispose();
      if(Array.isArray(object.material))object.material.forEach(m=>m.dispose());else object.material?.dispose();}group.clear();}};
}
export function addTessellatedSpace(THREE,scene,options={}){
  if(!scene?.add)throw new TypeError('A Three.js Scene or Group is required');
  const rendered=createTessellatedSpace(THREE,options);scene.add(rendered.group);return rendered;
}
export {colorHex};
