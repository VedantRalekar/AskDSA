
const CONFIG = {
  API_URL: "http://localhost:3000/api/ask",
  METHOD: "POST",

  buildRequestBody(query) {
    return {
      question: query
    };
  },

  parseResponse(json) {
    return {
      answer: json.answer || "",
      sources: []
    };
  }
};

const EXAMPLE_QUESTIONS = [
  "How do you reverse a linked list?",
  "What is the time complexity of binary search?",
  "Explain how quicksort works.",
  "What is dynamic programming?",
  "Difference between BFS and DFS?",
  "How does a hash table work?",
  "What is the knapsack problem?",
  "How do you detect a cycle in a linked list?"
];

const exampleListEl = document.getElementById("exampleList");
const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById("searchBtn");
const statusEl = document.getElementById("status");
const resultsEl = document.getElementById("results");

let history = JSON.parse(localStorage.getItem("askdsa")) || [];

function renderExamples() {
  exampleListEl.innerHTML = EXAMPLE_QUESTIONS
    .map(q => `<li data-q="${q}">${q}</li>`)
    .join("");

  exampleListEl.querySelectorAll("li").forEach(li => {
    li.addEventListener("click", () => {
      searchInput.value = li.dataset.q;
      runSearch();
    });
  });
}

function setStatus(text) {
  statusEl.hidden = !text;
  statusEl.textContent = text;
}

function renderResults(question, answer) {


    const card = document.createElement("div");

    card.className = "result-card";

    card.innerHTML = `
          <div class="user-message">
            <div class="user-title">Question</div>
            <div class="user-text">${question}</div>
        </div>

             <div class="ai-message">
            <div class="ai-title">Agent</div>

            <div class="answer markdown-body">
                ${marked.parse(answer)}
            </div>
        </div>

    `;

    resultsEl.appendChild(card);
   
      card.scrollIntoView({
        behavior: "smooth",
        block: "end"
    });

}

async function runSearch() {
  const query = searchInput.value.trim();
  if (!query) return;

  searchInput.value = "";

  searchBtn.disabled = true;
  setStatus("searching...");
  
  
  try {

    const res = await fetch(CONFIG.API_URL, {
      method: CONFIG.METHOD,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(CONFIG.buildRequestBody(query))
    });

    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const json = await res.json();
    const { answer } = CONFIG.parseResponse(json);

    setStatus("");

    const loading = document.getElementById("loading");

    if (loading) {
        loading.remove();
    }

    renderResults(query, answer);


localStorage.setItem("askdsa", JSON.stringify(history));

  } catch (err) {
    setStatus(`error: ${err.message}`);
  } finally {
    searchBtn.disabled = false;
  }


  
}

renderExamples();



searchBtn.addEventListener("click", runSearch);

searchInput.addEventListener("keydown", e => {
  if (e.key === "Enter") runSearch();
});

