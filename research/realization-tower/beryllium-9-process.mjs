import {beryllium8Process} from './beryllium-8-process.mjs';
// Depth-four layers stay cloned; the reference can trial a central sleeve.
export function beryllium9Process({be9AssemblySides=false,be9AssemblyFold=false,be9CentralSleeve=true,be9View='branching-seed'}={}){
 return {...beryllium8Process(),processId:'beryllium-9',clonedFrom:'beryllium-8',
  isotope:{symbol:'Be',mass:9,protons:4,neutrons:5},
  view:['3d-assembly','wiring-single-procedure'].includes(be9View)?be9View:'branching-seed',
  centralSleeveTrial:be9CentralSleeve,
  summary:be9View==='wiring-single-procedure'?'Be-9 · Wiring single procedure · eight retained strands, sixteen continuous conductors.':be9View==='3d-assembly'?(be9AssemblySides?'Be-9 · 3D assembly · four triangular faces · both side folds 60° toward the upper face.':be9AssemblyFold?'Be-9 · 3D assembly · 60° fold through red/blue midpoints above white-edge layer 5.':'Be-9 · 3D assembly · single depth-eight simplex · white–red / white–blue opening 120°.'): be9CentralSleeve?'Be-9 · central-sleeve reference trial · four retained strands in two pairs · depth-four layers.':'Be-9 · Be-8 construction clone · White-rooted hex simplex · depth 4 · eight retained layers.'};
}
