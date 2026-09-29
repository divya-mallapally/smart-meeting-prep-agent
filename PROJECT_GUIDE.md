# 🎓 Smart Meeting Prep Agent — Complete Beginner Guide

Everything from **START → BUILD → RUN → TEST → GITHUB → DEMO → VIVA**.
All project code already exists in this folder — this guide teaches you how to set it up, run it, understand it, and present it.

---

## PART 1 — Project Structure (what every file does)

```
smart-meeting-prep-agent/
│
├── app.py                  ← Streamlit web UI: forms, buttons, results
├── agent.py                ← The AI brain: builds prompts, calls Gemini
├── prompts.py              ← All prompt templates + anti-hallucination rules
├── document_processor.py   ← Extracts text from uploaded PDF/TXT files
├── requirements.txt        ← List of Python packages to install
├── .env.example            ← Template showing the .env format (safe to upload)
├── .env                    ← YOUR SECRET API KEY (never uploaded — you create this)
├── .gitignore              ← Tells Git which files to ignore (.env, venv, …)
├── README.md               ← Project documentation shown on GitHub
├── PROJECT_GUIDE.md        ← This guide
│
├── documents/              ← Optional folder for sample documents
└── venv/                   ← Virtual environment (created in Step 7, never uploaded)
```

**Flow of data:** user types into `app.py` → uploaded files go through `document_processor.py` → everything is combined by `agent.py` using templates from `prompts.py` → sent to Gemini → answer comes back as Markdown → displayed in `app.py`.

---

## PART 2 — Step-by-Step Setup (from absolute zero)

### Step 1 — Install Python
- **Check first** (you may already have it): open Terminal (macOS: Spotlight → "Terminal"; Windows: Start → "cmd") and type `python3 --version` (macOS) or `python --version` (Windows).
- If missing: download from **python.org** → during Windows installation **tick "Add Python to PATH"** (critical!).

### Step 2 — Check Python version
```bash
python3 --version    # macOS
python --version     # Windows
```
You should see Python 3.11 or newer. ✅ (This project was verified working on Python 3.14.)

### Step 3 — Install VS Code
Download from **code.visualstudio.com** → install with default options. VS Code is the editor where you'll view and edit files.

### Step 4 — Create the project folder
Already done — the folder `smart-meeting-prep-agent` exists with all code inside.

### Step 5 — Open the folder in VS Code
VS Code → File → Open Folder → select `smart-meeting-prep-agent`. You'll see all files in the left sidebar.

### Step 6 — Open Terminal
Inside VS Code: menu **Terminal → New Terminal** (or `` Ctrl+` ``). It opens at the project folder — always run commands from here.

### Step 7 — Create a virtual environment
A virtual environment ("venv") is a private folder where this project's packages live, so they don't clash with other projects.
```bash
# macOS
python3 -m venv venv
# Windows
python -m venv venv
```
Result: a new `venv/` folder appears.

### Step 8 — Activate the virtual environment
```bash
# macOS
source venv/bin/activate
# Windows (PowerShell or CMD)
venv\Scripts\activate
```
Result: your prompt now starts with `(venv)`. You must activate it **every time** you open a new terminal.

> Windows PowerShell error "running scripts is disabled"? Run once:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Step 9 — Create all required files
Already done for you — `app.py`, `agent.py`, `prompts.py`, `document_processor.py`, `requirements.txt`, `.gitignore`, `.env.example`, `README.md` all exist.

### Step 10 — Install dependencies
```bash
pip install -r requirements.txt
```
Result: many lines ending in `Successfully installed …`. This was already verified to work in this project.

### Step 11 — Create a Gemini API key
1. Go to **https://aistudio.google.com/apikey**
2. Sign in with a Google account.
3. Click **Create API key** → copy the key (starts with `AIza…`).
It's free for light use.

### Step 12 — Create the .env file
```bash
cp .env.example .env      # macOS
copy .env.example .env    # Windows
```
`.env` is a plain text file that holds secrets. It is separate from `.env.example` (which is safe to upload).

### Step 13 — Add your API key safely
Open `.env` in VS Code and replace the placeholder:
```
GEMINI_API_KEY=AIza...your_real_key...
```
Rules: no quotes, no spaces around `=`, never paste the key into any `.py` file, never send it to anyone.

### Step 14 — Review the Python files
Open each file in VS Code and read the comments at the top. Order to read: `prompts.py` → `document_processor.py` → `agent.py` → `app.py`.

### Step 15 — Run the application
```bash
streamlit run app.py
```
Result: the terminal prints a **Local URL: http://localhost:8501** and your browser opens automatically. Leave this terminal running while you use the app; stop it with `Ctrl+C`.

### Step 16 — Test the application
Use the sample meeting in **PART 3** below. The sidebar should show "✅ Gemini API key loaded". Click **🚀 Prepare My Meeting** and wait ~10–20 seconds for the 12-section result.

### Step 17 — Fix common errors
See the full troubleshooting table in **PART 4**.

### Step 18 — Upload to GitHub
See **PART 5** for exact commands.

---

## PART 3 — Testing: Sample Meeting Data

Paste these into the app:

**Sidebar**
- Title: `College Project Review Meeting`
- Date/Time: next week, 10:00
- Type: `Project Review`
- Participants:
```
Dr. Sharma — Project Guide
Alice — Team Lead
Bob — Developer
Carol — Tester
Me — Presenter
```

**Main page**
- Agenda:
```
1. Review project progress
2. Discuss current problems
3. Decide next steps and deadlines
```
- Description:
```
Monthly review of our BTech final-year project "Smart Meeting Prep Agent".
We must demo the current Streamlit app and get approval for the final
feature list before the mid-semester deadline.
```
- Previous Meeting Notes:
```
Last meeting (2 weeks ago):
- Alice will finish the UI design — DONE
- Bob will integrate the Gemini API — IN PROGRESS, delayed by 3 days
- Carol will write 10 test cases — NOT STARTED
- Next meeting: full demo expected
```
- Your Questions: `How do I explain the architecture clearly?`
- Upload: any PDF (e.g., your project report) — optional.

**Expected output:** a summary describing the review meeting; objectives about progress/demo/approval; a participant table (only the 5 people you listed); questions about Bob's delay and Carol's test cases; a follow-up section listing the 3 action items from the notes with statuses; a time-boxed suggested agenda; a short 5-minute briefing. The AI should NOT invent new people, dates, or facts — anything missing shows "Information not provided."

---

## PART 4 — Error Troubleshooting

| Error | Why it happens | What to check | Fix |
|---|---|---|---|
| `python: command not found` | Python not installed or not on PATH | `python3 --version` | Reinstall from python.org; on Windows tick **Add Python to PATH** |
| `pip: command not found` | pip not on PATH | which python is active? | `python3 -m pip install …` or re-activate venv |
| `ModuleNotFoundError: No module named 'streamlit'` | Packages installed in a different environment than the one running | Does prompt show `(venv)`? | `source venv/bin/activate` (or `venv\Scripts\activate`), then `pip install -r requirements.txt` |
| `GEMINI_API_KEY not found` (app error box) | `.env` missing, misspelled, or in the wrong folder | Is `.env` next to `app.py`? Is the line exactly `GEMINI_API_KEY=...`? | Recreate `.env` from `.env.example`, paste key, **restart** streamlit |
| `API key not valid` / `PERMISSION_DENIED` | Key typo, deleted, or from the wrong service | Key starts with `AIza`? Created in AI Studio? | Generate a new key at aistudio.google.com/apikey, update `.env`, restart |
| `429 / RESOURCE_EXHAUSTED` | Free-tier rate limit | Did you click many times quickly? | Wait ~60 seconds, retry |
| `streamlit: command not found` | venv not activated, or streamlit not installed | `(venv)` in prompt? | Activate venv → `pip install streamlit` → or run `python -m streamlit run app.py` |
| `localhost:8501 not opening` | App not actually running, or browser issue | Terminal still shows the URL? | Re-run `streamlit run app.py`; try http://127.0.0.1:8501; check firewall |
| `Port 8501 is already in use` | Another streamlit instance is running | | macOS: `lsof -ti:8501 \| xargs kill` • Windows: `netstat -ano \| findstr :8501` then `taskkill /PID <pid> /F` • or run `streamlit run app.py --server.port 8502` |
| PDF extraction error / empty text | Scanned (image) PDF — no text layer inside | Open the PDF: can you select text with the mouse? | Use a text-based PDF, or OCR the scan first |
| Empty AI response | Prompt too long or content blocked | Very large uploads? | Upload smaller documents; the app already caps text at 100k characters |
| `.env not loading` | File named wrong (`.env.txt`) or wrong folder | Enable "show hidden files" in your OS | Rename to exactly `.env` in the project root; restart the app |
| **API key visible on GitHub** | `.env` was committed | Check repo files online | **Immediately delete the key in AI Studio and create a new one**, then remove it from Git: `git rm --cached .env && git commit -m "Remove .env" && git push`. Note: it stays in history — that's why rotating the key is mandatory. |

---

## PART 5 — GitHub: Step-by-Step

### 1. Create a GitHub repository
- Go to **github.com** → sign in (create a free account if needed).
- Click **+ (top right) → New repository**.
- Name: `smart-meeting-prep-agent`. Keep it **Public**. Do **NOT** tick "Add a README" (we already have one). Click **Create repository**.
- GitHub shows your repo URL, e.g. `https://github.com/YOUR_USERNAME/smart-meeting-prep-agent.git`.

### 2–6. Initialize, add, commit, connect, push
Run in the project folder (replace `YOUR_USERNAME`):
```bash
git init
git add .
git status                # VERIFY: .env and venv/ must NOT be listed!
git commit -m "Initial commit: Smart Meeting Prep Agent"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/smart-meeting-prep-agent.git
git push -u origin main
```
First push asks you to log in — follow the browser prompt (GitHub CLI / Git Credential Manager) or use a Personal Access Token as the password.

### 7. Verify the files
Open your repo URL in the browser. You should see: `app.py`, `agent.py`, `prompts.py`, `document_processor.py`, `requirements.txt`, `.gitignore`, `.env.example`, `README.md`, `documents/`. You should **NOT** see `.env` or `venv/`.

### 8–9. README and screenshots
- README.md already renders automatically on your repo's front page.
- Screenshots: run the app, take screenshots (macOS `Cmd+Shift+4`, Windows `Win+Shift+S`), put them in a `screenshots/` folder, then:
```bash
git add screenshots/
git commit -m "Add screenshots"
git push
```

### 10. Keep the API key private
The key lives only in `.env`, which `.gitignore` blocks. Double-check with `git status` before every commit. If a key ever leaks, delete and regenerate it immediately (see troubleshooting).

### Future updates
After any code change:
```bash
git add .
git commit -m "describe your change"
git push
```

---

## PART 6 — Architecture Explanation (simple language)

```
User
 ↓
Streamlit UI (app.py)
 ↓
Meeting Input (forms + uploaded files)
 ↓
Document Processor (document_processor.py)
 ↓
AI Meeting Agent (agent.py) + Prompts (prompts.py)
 ↓
Gemini LLM (Google's AI model, via API)
 ↓
Structured Meeting Preparation (Markdown)
 ↓
User (reads on screen, downloads)
```

- **User** — enters meeting details and documents; receives the preparation pack.
- **Streamlit UI** — turns Python code into a web page. Handles all input forms and displays results. It contains no AI logic.
- **Meeting Input** — the collected raw data: title, date, participants, agenda, notes, questions, files.
- **Document Processor** — converts PDF/TXT files into plain text (PDFs store an invisible "text layer"; pypdf reads it page by page). Text is kept in memory only, capped at a safe length, and never written to disk.
- **AI Meeting Agent** — the coordinator. It labels every piece of input ("Agenda: …", "Previous notes: …"), picks the right prompt template, calls Gemini, and translates errors into friendly messages.
- **Prompts** — the instructions to the AI, including strict rules: use only supplied info, never invent facts, separate facts from suggestions, say "Information not provided" when data is missing.
- **Gemini LLM** — Google's Large Language Model. It reads the prompt and generates the structured preparation content.
- **Structured output** — clean Markdown sections shown in the UI and downloadable as `.md` files.

**Why no LangChain / vector database?** LangChain is useful when you chain multiple models, tools, or memory together. FAISS/Chroma are useful when you must *search* thousands of documents. Here we have one model and a few short documents, so passing text directly into the prompt is simpler, cheaper, and just as accurate. Adding RAG would be over-engineering — mentioning this reasoning in your viva earns marks.

---

## PART 7 — Flowchart for your presentation

```
        ┌──────────────────────┐
        │        START         │
        └──────────┬───────────┘
                   ▼
        ┌──────────────────────┐
        │  User opens Streamlit │
        │      web app          │
        └──────────┬───────────┘
                   ▼
        ┌──────────────────────┐
        │ Enter meeting details │
        │ + upload PDF/TXT      │
        └──────────┬───────────┘
                   ▼
        ┌──────────────────────┐     no documents
        │ Extract text from     │──────────────┐
        │ uploaded documents    │              │
        └──────────┬───────────┘              │
                   ▼                           ▼
        ┌─────────────────────────────────────────┐
        │ Agent builds safe prompt (rules + data) │
        └──────────┬──────────────────────────────┘
                   ▼
        ┌──────────────────────┐
        │ Send to Gemini LLM    │
        │ via API               │
        └──────────┬───────────┘
                   ▼
        ┌──────────────────────┐
        │ Receive structured    │
        │ Markdown response     │
        └──────────┬───────────┘
                   ▼
        ┌──────────────────────┐
        │ Display in UI +       │
        │ allow download        │
        └──────────┬───────────┘
                   ▼
        ┌──────────────────────┐
        │         END          │
        └──────────────────────┘
```

---

## PART 8 — 10-Slide PPT Outline

**Slide 1 — Title**
Smart Meeting Prep Agent — An AI-Powered Meeting Preparation Assistant. Your name, roll number, branch, guide's name, college.

**Slide 2 — Problem Statement**
Professionals and students attend meetings unprepared. Reviewing notes, documents, and past action items manually takes 30+ minutes and is often skipped → wasted meeting time, missed decisions, repeated discussions.

**Slide 3 — Existing System**
Manual preparation: re-reading emails/notes, manually listing questions, no tracking of previous action items. Limitations: slow, inconsistent, depends on individual effort, no standard output.

**Slide 4 — Proposed System**
An AI agent (Python + Streamlit + Google Gemini) that takes meeting details and documents as input and instantly generates a structured preparation pack: summary, objectives, questions, talking points, risks, briefing, and action-item follow-up. Anti-hallucination prompts ensure it never invents information.

**Slide 5 — Objectives**
• Reduce meeting prep time from ~30 min to ~2 min • Provide consistent, structured output • Track previous action items automatically • Keep data honest — separate facts from suggestions • Simple UI usable by non-technical people.

**Slide 6 — System Architecture**
Use the flowchart from Part 7: User → Streamlit UI → Document Processor → Agent + Prompts → Gemini API → Structured output → User.

**Slide 7 — Technologies Used**
Python, Streamlit (UI), Google Gemini API + google-genai SDK (LLM), pypdf (PDF text extraction), python-dotenv (secure key handling), Git/GitHub (version control).

**Slide 8 — Working Process**
1) User fills meeting form and uploads documents 2) pypdf extracts text 3) Agent labels all inputs and applies strict prompt rules 4) Gemini generates Markdown sections 5) UI displays results with download option.

**Slide 9 — Results**
Live demo screenshots: full 12-section preparation pack, 5-minute briefing, questions, talking points, action-item table. Note: tested with a real "College Project Review Meeting" scenario — output was accurate and never invented facts.

**Slide 10 — Future Scope**
Google Calendar integration, automatic email summarisation, RAG (FAISS) for large document libraries, multi-meeting history, PDF/Notion export, voice input, team collaboration features.

---

## PART 9 — Viva Questions & Answers (35)

**AI / LLM / Generative AI**

1. **What is AI?** A field of computer science where machines perform tasks that normally need human intelligence — understanding language, recognising patterns, making decisions.
2. **What is an LLM?** A Large Language Model — a neural network trained on huge amounts of text to predict the next word, which lets it understand and generate human language. Examples: Gemini, GPT, Claude.
3. **What is Generative AI?** AI that creates new content (text, images, code) rather than just classifying data. My project uses generative AI to create meeting preparation material.
4. **What is an "AI agent"?** A program that perceives input, reasons about it (often using an LLM), and produces goal-directed output. My agent takes meeting data, decides how to prompt the LLM, and returns a preparation pack.
5. **What is hallucination?** When an LLM confidently outputs false or invented information. I reduce it with strict prompt rules: "use only supplied info", "never invent facts", "say Information not provided when data is missing", and a low temperature (0.4).
6. **What is temperature in an LLM?** A setting controlling randomness. Low (0–0.4) = factual, consistent; high (0.8+) = creative, varied. I use 0.4 because meeting prep must be reliable.
7. **What are tokens?** The units LLMs split text into (roughly ¾ of a word). Models have a context window measured in tokens; I cap document text to stay inside it.
8. **Difference between AI, ML, and Deep Learning?** AI is the broad goal; ML is learning patterns from data instead of hard-coded rules; Deep Learning is ML using multi-layer neural networks. LLMs are deep learning models.

**Prompt Engineering**

9. **What is prompt engineering?** Designing the instructions given to an LLM so it produces accurate, well-structured output. It's the core skill in my project — all templates live in `prompts.py`.
10. **What makes a good prompt?** Clear role ("You are an expert meeting-preparation assistant"), explicit task, strict constraints (no invention), required output format (Markdown headings), and handling of missing data.
11. **How do you prevent hallucination in your prompts?** Six rules embedded in every prompt: use only provided info; separate facts from suggestions; write "Information not provided" for missing data; be concise and structured; never leak secrets; reject empty input.
12. **What is few-shot vs zero-shot prompting?** Zero-shot = instruction only, no examples. Few-shot = include example input/output pairs. My project uses zero-shot with very detailed instructions.

**APIs & Gemini**

13. **What is an API?** Application Programming Interface — a contract that lets one program request services from another. My app sends HTTP requests to Google's Gemini API and receives generated text back.
14. **What is an API key and why keep it secret?** A password identifying you to the service, used for billing and access control. If leaked, others can use your quota or run up charges. Mine lives in `.env`, blocked by `.gitignore`.
15. **What is Google Gemini?** Google's family of LLMs. I use `gemini-2.0-flash` — fast and free for light usage.
16. **What SDK do you use and why not LangChain?** The official `google-genai` Python SDK. LangChain adds abstraction layers useful for multi-model chains and RAG pipelines; for one model and one prompt per action, direct SDK calls are simpler and easier to debug.
17. **What happens if the API fails?** `agent.py` catches exceptions and converts them into friendly messages: invalid key, rate limit (429), empty response — each with instructions on what to do.
18. **What is a REST API?** An API using HTTP methods (GET/POST) with JSON data. Gemini's generate-content endpoint works this way.

**Streamlit & Python**

19. **What is Streamlit and why did you choose it?** A Python library that turns scripts into web apps with no HTML/CSS/JavaScript. Perfect for ML/AI demos and beginner-friendly — one `st.text_input()` line creates a form field.
20. **How does Streamlit handle user interaction?** The script re-runs top-to-bottom on every interaction (button click, form change). State that must survive re-runs is kept in `st.session_state` — I use it to store generated results.
21. **What is `st.session_state`?** A dictionary persisting across re-runs for one user session. I store each AI result there so results stay visible after clicking another button.
22. **What is a virtual environment?** An isolated folder (`venv/`) with its own Python packages, so project dependencies don't conflict with each other. Activate before running, deactivate with `deactivate`.
23. **What does python-dotenv do?** Loads variables from `.env` into the program via `load_dotenv()`, so `os.getenv("GEMINI_API_KEY")` works. This keeps secrets out of source code.
24. **Why requirements.txt?** It lists exact packages so anyone can reproduce your environment with one command: `pip install -r requirements.txt`.

**RAG, Embeddings, Vector DBs**

25. **What is RAG?** Retrieval-Augmented Generation — instead of relying on the model's memory, you *retrieve* relevant documents and put them in the prompt, so answers are grounded in your data.
26. **What are embeddings?** Numeric vectors (lists of hundreds/thousands of numbers) representing the meaning of text. Similar meanings → vectors close together in space.
27. **What is a vector database?** A database storing embeddings that can quickly find the most similar vectors to a query (similarity search). Examples: FAISS, Chroma, Pinecone.
28. **What is FAISS?** Facebook AI Similarity Search — a fast local library for storing embeddings and finding nearest neighbours.
29. **Does your project use RAG or a vector DB? Why not?** No. Meeting documents are short enough to fit directly in Gemini's context window, so I pass extracted text straight into the prompt. A vector DB only pays off when you must search large collections where everything won't fit. I designed for the simplest reliable solution — and my `vectorstore/` folder + architecture leave room to add FAISS later as an enhancement.
30. **When WOULD you add a vector database?** If users upload hundreds of past meetings and you need to retrieve only the relevant few per query — then: chunk documents → embed with a model → store in FAISS → retrieve top-k similar chunks → add to prompt.

**PDF Processing & Documents**

31. **How does PDF text extraction work?** Text-based PDFs store characters with position instructions. `pypdf` parses the PDF structure and reconstructs the text per page. Scanned PDFs are just images — they have no text layer, so extraction returns empty and OCR would be needed.
32. **Where is extracted text stored?** Nowhere on disk — only in memory during the request, inside the prompt string. This protects confidentiality. I also cap it (40k chars/file, 100k total) to stay within the model's context window.

**Environment Variables, Security & GitHub**

33. **Why use .env instead of hard-coding the key?** Hard-coded keys get committed to Git and leak publicly (bots scan GitHub for keys within minutes). `.env` is loaded at runtime and excluded by `.gitignore`.
34. **What is .gitignore?** A file listing patterns Git must never track — mine blocks `.env`, `venv/`, `__pycache__/`, and OS junk files.
35. **What if you accidentally pushed your API key?** Delete the key in Google AI Studio immediately (rotate it), then `git rm --cached .env`, commit, push. Old commits still contain it — which is why rotation, not just deletion, is mandatory.

**Bonus**

36. **What is Git vs GitHub?** Git is the local version-control tool (commits, branches, history). GitHub is the cloud hosting service for Git repositories, enabling sharing and collaboration.
37. **Explain your project's data flow in one sentence.** User input + extracted document text are combined into a rules-bound prompt by the agent, sent to Gemini, and the structured Markdown response is displayed and downloadable in the Streamlit UI.

---

## PART 10 — Project Explanations (for your demo)

### 30-second version
"This is my Smart Meeting Prep Agent. You enter your meeting details — title, participants, agenda, and previous notes — optionally upload PDFs, and click one button. Google Gemini's AI then generates a complete preparation pack: summary, objectives, questions to ask, talking points, risks, and a 5-minute briefing. It's built with Python and Streamlit, and the prompts strictly prevent the AI from inventing information."

### 1-minute version
(30-second version, plus:)
"The system has four modules. `app.py` is the Streamlit interface. `document_processor.py` extracts text from uploaded PDFs using pypdf. `agent.py` combines everything into a labelled context and calls the Gemini API. `prompts.py` holds prompt templates with six strict anti-hallucination rules — the AI must use only supplied information, separate facts from suggestions, and say 'Information not provided' when data is missing. My API key sits in a `.env` file that `.gitignore` blocks from GitHub. Let me show you a live example…"

### 2-minute version
(1-minute version, plus a live walkthrough:)
"Let me demonstrate. I'll enter a College Project Review Meeting — participants are my project guide and four team members. The agenda is: review progress, discuss problems, decide next steps. I'll also paste notes from the last meeting, which contain three action items — one done, one delayed, one not started. Now I click **Prepare My Meeting**… In about fifteen seconds we get twelve structured sections: the summary, objectives, a participant table, questions to ask — notice it asks about the delayed API integration, which came straight from my notes — risks, preparation tasks, action-item follow-up, a suggested time-boxed agenda, and a 5-minute briefing. I can also generate questions, talking points, or an action-item table separately, and download any result as Markdown. The whole preparation that would take thirty minutes manually now takes under two."

### 5-minute detailed version
1. **Problem (30s):** Meetings fail when people arrive unprepared. Manual prep — rereading notes, listing questions, checking old action items — takes 30+ minutes, so people skip it.
2. **Solution (30s):** An AI agent that converts raw meeting information into a structured preparation pack in under a minute.
3. **Architecture (60s):** Walk through the flow diagram: User → Streamlit UI → input forms + PDF/TXT upload → document processor (pypdf extraction, in-memory only, length-capped) → agent (labels every input, applies prompt templates) → Gemini 2.0 Flash via API (temperature 0.4 for factual output) → Markdown results → UI display + download.
4. **Key design decisions (60s):**
   - *Anti-hallucination:* six strict rules in every prompt — only supplied info, facts vs suggestions labelled, explicit "Information not provided", secret protection.
   - *Simplicity:* no LangChain (single model, single prompt per action — direct SDK is easier to debug); no vector DB (documents fit in the context window; RAG would be over-engineering, but the design allows adding FAISS later for large document libraries).
   - *Security:* key in `.env`, loaded by python-dotenv, blocked by `.gitignore`; error handling converts invalid-key/quota/empty responses into friendly guidance.
5. **Live demo (90s):** Run the college-review scenario from Part 3. Show the full pack, then the 5-minute briefing, then the action-item table extracted from previous notes. Point out that follow-up items match the notes exactly — nothing invented.
6. **Future scope (30s):** Calendar and email integration, RAG for large archives, meeting history tracking, PDF/Notion export.

---

## PART 11 — Final Demo Checklist

Before your demonstration, verify every box:

- ☐ **Project runs** — `streamlit run app.py` starts and http://localhost:8501 opens
- ☐ **API key works** — sidebar shows "✅ Gemini API key loaded" and one real generation succeeds
- ☐ **PDF upload works** — upload a text-based PDF, confirm no extraction error
- ☐ **Meeting preparation works** — "Prepare My Meeting" returns all 12 sections
- ☐ **Questions generation works** — grouped questions appear
- ☐ **Talking points work** — opening/core/closing points appear
- ☐ **Briefing works** — short 5-minute brief appears
- ☐ **Action items work** — table extracted from the sample previous notes
- ☐ **.env is protected** — `git status` shows nothing about `.env`; repo online has no `.env`
- ☐ **GitHub repository works** — repo URL opens, all files visible, README renders
- ☐ **README is complete** — title, features, installation, run steps, architecture
- ☐ **Backup plan** — screenshots/PDF of previous successful outputs saved, in case Wi-Fi or quota fails during the demo
- ☐ **Pre-run the demo scenario once** so results are cached in your head and you know the expected output

**Demo-day tips:** start the app *before* your slot; keep the terminal visible to prove it runs locally; have the sample data from Part 3 pre-typed in a notes app for fast pasting; if the API rate-limits live, show your saved screenshots and explain the error handling — examiners appreciate seeing graceful failure.
