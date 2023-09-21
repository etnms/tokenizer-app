<script>
  export let responseData;

  const handleSubmit = (e) => {
    // getting the action url
    const ACTION_URL = e.target.action;

    // get the form fields data and convert it to URLSearchParams
    const formData = new FormData(e.target);
    const data = new URLSearchParams();
    for (let field of formData) {
      const [key, value] = field;
      data.append(key, value);
    }

    // check the form's method and send the fetch accordingly
    if (e.target?.method.toLowerCase() == "get") fetch(`${ACTION_URL}?${data}`);
    else {
      fetch(ACTION_URL, {
        method: "POST",
        body: data,
      })
        .then((response) => response.json())
        .then((data) => {
          responseData = data;
        });
    }
  };
</script>

<h1>Natural language tagger app</h1>

<form
  method="POST"
  action="http://127.0.0.1:5000"
  on:submit|preventDefault={handleSubmit}
>
  <input type="text" name="text" />
  <input type="submit" value="Show result" />
</form>

<div class="container">
  {#if responseData}
    {#each [...responseData] as [key, value]}
      <div class="word-container">
        <span>{key}</span>
        <span>{value}</span>
      </div>
    {/each}
  {/if}
</div>

<style>
  .word-container {
    display: flex;
    flex-direction: column;
    text-align: center;
  }

  .container {
    display: flex;
    flex-direction: row;
    gap: 0.4rem;
  }
</style>
