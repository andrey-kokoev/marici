import {Vector3} from 'three';
import {doubleEsd7Envelope,doubleEsd7VertexLabels} from '../../research/realization-tower/double-esd7-process.mjs';
import {geometryParentPoint} from './belt-geometry-layout.js';
import {wiringParentPoint} from './belt-wiring-layout.js';
import {centralParentPoint,buildCentralBeltLayout} from '../../research/realization-tower/central-belt-layout.mjs';
import {worldPoint} from '../../research/realization-tower/normal-ray-model.mjs';
const layout=buildCentralBeltLayout();
export function protonRotationLine(separated=false,wiring=false){
 const point=(label,copy)=>{const p=doubleEsd7Envelope[doubleEsd7VertexLabels.indexOf(label)],posed=separated?(wiring?wiringParentPoint:geometryParentPoint)(centralParentPoint(p,copy),copy,layout):p;return new Vector3(...worldPoint(posed));};
 const minus=point('−P','clone'),plus=point('+P','original');
 return {pivot:minus.clone().add(plus).multiplyScalar(.5),axis:plus.clone().sub(minus).normalize(),minus,plus};
}
export function locksAllowAxialRotation(line,points){return points.every(p=>p.clone().sub(line.pivot).cross(line.axis).length()<1e-8);}
