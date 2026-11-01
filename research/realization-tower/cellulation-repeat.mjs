import {packCellulation} from './cellulation-geometry.mjs';
import {completionTiming} from './cellulation-completion.mjs';
import {witnessTiming} from './cellulation-witness.mjs';
export const repeatTiming=Object.freeze({seed:600,arrow:1600,firstLoop:witnessTiming.proposal+2*witnessTiming.edge,secondLoop:witnessTiming.total,completion:completionTiming.total,total:600+1600+witnessTiming.proposal+2*witnessTiming.edge+witnessTiming.total+completionTiming.total});
export function cellulationRepeatAt(elapsed){
 const {seed,arrow,firstLoop,secondLoop,total}=repeatTiming;
 if(elapsed<seed)return {stage:2,phase:'seed',localElapsed:elapsed,active:true};
 if(elapsed<seed+arrow)return {stage:3,phase:'red-arrow',arrowProgress:(elapsed-seed)/arrow,localElapsed:elapsed-seed,active:true};
 if(elapsed<seed+arrow+firstLoop)return {stage:4,phase:'first-return-loop',localElapsed:elapsed-seed-arrow,active:true};
 if(elapsed<seed+arrow+firstLoop+secondLoop)return {stage:5,phase:'second-return-loop',localElapsed:elapsed-seed-arrow-firstLoop,active:true};
 return {stage:6,phase:elapsed<total?'connecting-candidates':'complete',localElapsed:Math.min(completionTiming.total,elapsed-seed-arrow-firstLoop-secondLoop),active:elapsed<total};
}
export function translateCellulationStep(model,delta,prefix='repeat:'){
 const point=p=>p.map((x,i)=>x+delta[i]),face=f=>f.map(point),marker=m=>({...m,point:point(m.point)});
 const cells=model.cells.map(c=>({...c,id:`${prefix}${c.id}`,vertices:face(c.vertices),faces:c.faces.map(face)}));
 const completion=model.completion?{arrow:{...model.completion.arrow,from:point(model.completion.arrow.from),to:point(model.completion.arrow.to)},faces:model.completion.faces.map(face)}:null;
 const witness=model.witness?{...model.witness,proposedVertex:point(model.witness.proposedVertex),returnPath:face(model.witness.returnPath),faces:model.witness.faces.map(face),turnMarker:marker(model.witness.turnMarker),priorTurnMarkers:model.witness.priorTurnMarkers.map(marker)}:null;
 return {...model,...packCellulation(cells,model.source),markedVertex:model.markedVertex?point(model.markedVertex):null,proposedVertex:model.proposedVertex?point(model.proposedVertex):null,arrows:model.arrows.map(a=>({...a,from:point(a.from),to:point(a.to)})),witness,completion};
}
