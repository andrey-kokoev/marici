// Capture screen-up once as a world-space translation; never follow later rotations.
export function cellulationStartTranslation(quaternion){
 const length=Math.hypot(...quaternion);
 if(quaternion.length!==4||!quaternion.every(Number.isFinite)||!length)throw Error('Invalid camera quaternion');
 const [x,y,z,w]=quaternion.map(v=>v/length);
 return [2*(x*y-z*w),1-2*(x*x+z*z),2*(y*z+x*w)].map(v=>8*v);
}
