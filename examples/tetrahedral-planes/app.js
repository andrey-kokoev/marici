import { createApp } from 'vue';
import App from './App.vue';
import '../threejs-reference/style.css';
import './style.css';
const app = createApp(App, { host: document.querySelector('#viewport') });
const panel = app.mount('#panel');
window.TetrahedralPlanes = Object.freeze({ dispose: () => panel.dispose(), snapshot: () => panel.snapshot() });
window.addEventListener('pagehide', event => { if (!event.persisted) app.unmount(); });
