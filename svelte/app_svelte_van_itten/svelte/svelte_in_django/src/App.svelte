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

  export let uzenetek:string[] = []

  const chatSocket = new WebSocket('ws://127.0.0.1:8000/ws/uzenetek/');

  chatSocket.onmessage = function(e) {
      const data = JSON.parse(e.data);
      const message = data['message'];
      // Handle incoming message
      uzenetek.push(message)
      uzenetek = uzenetek
  };

  chatSocket.onclose = function(e) {
      console.error('Chat socket closed unexpectedly'); // fun
  };

  // Send message to server
  function sendMessage(message) {
      chatSocket.send(JSON.stringify({
          'message': message
      }));
  }
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

<div>
  realtime
  <ol>
    {#each uzenetek as li}
      <li>{li}</li>
    {/each}
  </ol>
</div>

<input type="text" placeholder="irj vmit" bind:value={text_v}>
<button on:click={() => sendMessage(text_v)}>kuld</button>