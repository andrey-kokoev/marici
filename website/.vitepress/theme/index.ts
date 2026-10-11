import DefaultTheme from 'vitepress/theme'
import { defineAsyncComponent } from 'vue'
import PagefindSearch from '../components/PagefindSearch.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('GraphExplorer', defineAsyncComponent(() => import('../components/GraphExplorer.vue')))
    app.component('StandardModelGraph', defineAsyncComponent(() => import('../components/StandardModelGraph.vue')))
    app.component('PagefindSearch', PagefindSearch)
  },
}
