<script>
  let responseData;
  let type;
  const handleSubmit = (e) => {
    // Getting api address
    const api = "http://127.0.0.1:5000";

    const text = document.querySelector(
      "textarea[name='user-input-text']"
    ).value;
    type = e.target.getAttribute("data-type");

    fetch(api, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text, type }),
    })
      .then((response) => response.json())
      .then((data) => {
        responseData = data;
        console.log(responseData);
      });
  };
</script>

<h1 class="text-3xl font-bold text-center">Natural language tagger app</h1>

<div class="flex flex-col center items-center justify-items-center gap-4 px-8">
  <textarea
    type="text"
    name="user-input-text"
    class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-m shadow-sm placeholder-slate-400
  focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 h-32 max-h-96"
  />
  <div>
    <button
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded cursor-pointer"
      data-type="token"
      on:click={handleSubmit}>Get tokens</button
    >
    <button
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded cursor-pointer"
      data-type="tag"
      on:click={handleSubmit}>Get tags</button
    >
    <button
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded cursor-pointer"
      data-type="stem"
      on:click={handleSubmit}
      >Get stems
    </button>
  </div>
</div>

<div class="flex flex-row gap-4 px-3">
  {#if responseData && type === "tag"}
    {#each [...responseData] as [key, value]}
      <div class="flex flex-col text-center">
        <span>{key}</span>
        <span>{value}</span>
      </div>
    {/each}
  {:else if responseData && type ==="token"} 
    {#each responseData as element}
      <div class="flex flex-col text-center">
        <span>{element}</span>
      </div>
    {/each}
  {:else if responseData && type ==="stem"} 
  {#each responseData as element}
    <div class="flex flex-col text-center">
      <span>{element}</span>
    </div>
  {/each}
{/if}
</div>

<style lang="postcss">
</style>
