import {cellulationRepeatAt,repeatTiming} from './cellulation-repeat.mjs';
import {octahedronTiming} from './cellulation-octahedron.mjs';
export const cycleTiming=Object.freeze({tetrahedron:repeatTiming.total,octahedron:octahedronTiming.total,total:repeatTiming.total+octahedronTiming.total});
export const redExtensionCount=5;
export const extensionTiming=Object.freeze({count:redExtensionCount,cycle:cycleTiming.total,total:redExtensionCount*cycleTiming.total});
export function cellulationExtensionsAt(elapsed,count=redExtensionCount){
 const {cycle}=extensionTiming,total=count*cycle,index=Math.min(count-1,Math.floor(Math.max(0,elapsed)/cycle));
 return {phase:elapsed<total?'extending':'complete',index,iteration:index+1,completed:Math.min(count,Math.floor(Math.max(0,elapsed)/cycle)),localElapsed:Math.min(cycle,Math.max(0,elapsed-index*cycle)),active:elapsed<total};
}
export function cellulationCycleAt(elapsed){
 const {tetrahedron,total}=cycleTiming;
 if(elapsed<tetrahedron)return {phase:'first-tetrahedron',part:0,localElapsed:elapsed,construction:cellulationRepeatAt(elapsed),active:true};
 return {phase:elapsed<total?'octahedron':'complete',part:1,construction:null,localElapsed:Math.min(octahedronTiming.total,elapsed-tetrahedron),active:elapsed<total};
}
