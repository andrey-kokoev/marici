import {buildBeryllium8Reference} from './beryllium-8-reference.mjs';
export function buildBeryllium9Wiring({be9WiringStep=0}={}){
 const step=be9WiringStep>0?1:0,source=buildBeryllium8Reference();
 const ordered=[0,2,4,6,1,3,5,7].map(i=>source.strands[i]);
 const wires=ordered.flatMap((s,i)=>[0,1].map(j=>{
  const lane=(i-3.5)*.46+(j-.5)*.14;
  return {id:`${s.id}:conductor:${j}`,strandId:s.id,outputSlot:s.outputSlot,colour:s.colors[j%s.colors.length],lane,
   // Two straight half-bundles, a single coincident pinch point, and the
   // opposite endpoint order after the half-turn. No distributed torsion.
   points:step?[[lane,-4,0],[0,0,0],[-lane,4,0]]:[[lane,-4,0],[lane,4,0]]};
 }));
 const bounds=[0,1,2].map(i=>[Math.min(...wires.flatMap(w=>w.points.map(p=>p[i])))-.2,Math.max(...wires.flatMap(w=>w.points.map(p=>p[i])))+.2]);
 return {wires,subbundles:[],envelope:bounds[0].flatMap(x=>bounds[1].flatMap(y=>bounds[2].map(z=>[x,y,z]))),audit:{step,plane:'XY',maxOutOfPlane:0,strands:8,wires:16,
  whiteWires:wires.filter(w=>w.colour===0xffffff).length,colouredWires:wires.filter(w=>w.colour!==0xffffff).length,
  subbundles:0,midpointTwist:step?180:0,pinchPoint:step?[0,0,0]:null,straightHalves:true,
  initialPlane:'XY',initialNormal:[0,0,1],wireIds:wires.map(w=>w.id),strandIds:source.strands.map(s=>s.id)}};
}
