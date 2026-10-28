import fs from 'node:fs/promises';
import {createHelium3Tunnel} from '../research/strominger/demos/particle-overlap-tetrahedron/helium3-tunnel-model.mjs';
import {deriveHelium4Core} from '../research/strominger/demos/particle-overlap-tetrahedron/helium4-core-probe.mjs';
export function buildHeliumCarriers(){
  const model=createHelium3Tunnel();let state=model.snapshot();
  for(let i=0;i<20&&state.status!=='complete';i++)state=model.step();
  const probe=deriveHelium4Core(state);
  // Affine A3 chart: e0,e1,e2,e3 -> 000,110,101,011.
  const basis=[[0,0,0],[1,1,0],[1,0,1],[0,1,1]],counts={proton:0,neutron:0,electron:0};
  const items=probe.items.map(item=>{
    const indices=item.vertices.map(v=>basis[0].map((_,j)=>v.reduce((sum,n,i)=>sum+n*basis[i][j],0)));
    return {label:({proton:'P',neutron:'N',electron:'E'})[item.species]+(++counts[item.species]),species:item.species,sourceKey:item.key,sourceVertices:item.vertices,indices};
  });
  return {source:'research/strominger/demos/particle-overlap-tetrahedron/helium4-core-probe.mjs',status:probe.status,counts,items,ordinaryNeutronExitToRetainedElectron:probe.ordinaryNeutronExitToRetainedElectron};
}
const text=JSON.stringify(buildHeliumCarriers(),null,2)+'\n';
const file=new URL('../examples/realization-lattice/helium-carriers.json',import.meta.url);
if(process.argv.includes('--check')){if(await fs.readFile(file,'utf8')!==text)throw Error('Stale helium carrier fixture');console.log('PASS: helium carrier fixture matches owning constructor.');}
else{await fs.writeFile(file,text);console.log('Generated six-carrier helium fixture.');}
