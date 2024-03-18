<script lang="ts">
  import { Router, Link, Route } from "svelte-routing";
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'
  import Home from "./routes/Home.svelte";
  import Masik from "./routes/Masik.svelte";
  import Harmadik from "./routes/Harmadik.svelte";

  export let url = ""

  let text_v = ""
</script>

<Router {url}>
  <nav>
    <Link to="/">Home</Link> ||
    <Link to="/masik">Masik</Link> ||
    <Link to="/harmadik/{text_v}">Nav harmadikra {text_v == "" ? "<még üres>" : text_v} paraméterrel</Link>
  </nav>
  <div>
    <Route path="/masik" component={Masik} />
    <Route path="/"><Home /></Route>
    <Route path="/harmadik/:id" let:params><Harmadik text_v={params.id} /></Route>
  </div>
</Router>

<input type="text" placeholder="irj vmit" bind:value={text_v}>