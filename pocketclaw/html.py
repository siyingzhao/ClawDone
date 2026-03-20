"""Embedded mobile web UI."""

INDEX_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
  <title>PocketClaw</title>
  <style>
    :root {
      color-scheme: dark;
      --background: #020817;
      --foreground: #e2e8f0;
      --card: #0f172a;
      --card-foreground: #e2e8f0;
      --muted: #94a3b8;
      --muted-foreground: #94a3b8;
      --popover: #0b1222;
      --border: #1e293b;
      --input: #0b1222;
      --ring: #3b82f6;
      --primary: #e2e8f0;
      --primary-foreground: #020617;
      --secondary: #1e293b;
      --secondary-foreground: #f8fafc;
      --destructive: #ef4444;
      --destructive-foreground: #fef2f2;
      --success: #22c55e;
      --warning: #f59e0b;
      --radius: 0.75rem;
      --shadow: 0 1px 3px rgba(15, 23, 42, 0.5), 0 12px 28px rgba(2, 6, 23, 0.35);
    }
    * { box-sizing: border-box; }
    html, body { min-height: 100%; }
    body {
      margin: 0;
      font-family: "Inter", "SF Pro Text", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background:
        radial-gradient(1100px 320px at 50% -140px, rgba(59, 130, 246, 0.2), rgba(59, 130, 246, 0) 62%),
        linear-gradient(180deg, #020617 0%, #020817 100%);
      color: var(--foreground);
      line-height: 1.45;
    }
    .wrap {
      width: min(1160px, 100%);
      margin: 0 auto;
      padding: 24px 16px 68px;
    }
    h1, h2, h3, p { margin: 0; }
    .hero {
      margin-bottom: 16px;
      display: grid;
      gap: 10px;
    }
    .hero h1 {
      font-size: clamp(1.45rem, 2.1vw, 1.95rem);
      line-height: 1.2;
      letter-spacing: -0.02em;
    }
    .sub {
      color: var(--muted-foreground);
      max-width: 90ch;
    }
    .pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      width: fit-content;
      padding: 6px 12px;
      border-radius: 999px;
      border: 1px solid rgba(59, 130, 246, 0.38);
      background: rgba(30, 58, 138, 0.2);
      color: #bfdbfe;
      font-size: 0.82rem;
      font-weight: 500;
    }
    .card {
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid var(--border);
      border-radius: calc(var(--radius) + 3px);
      box-shadow: var(--shadow);
      padding: 16px;
      margin-bottom: 14px;
    }
    .grid { display: grid; gap: 12px; }
    .grid-2 { display: grid; gap: 10px; grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .grid-3 { display: grid; gap: 10px; grid-template-columns: repeat(3, minmax(0, 1fr)); }
    .grid-4 { display: grid; gap: 10px; grid-template-columns: repeat(4, minmax(0, 1fr)); }
    .main-grid { display: grid; gap: 14px; grid-template-columns: 1.15fr 1fr; }
    label {
      display: block;
      margin-bottom: 7px;
      color: var(--muted-foreground);
      font-size: 0.85rem;
      font-weight: 500;
    }
    input, select, textarea {
      width: 100%;
      min-height: 40px;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 9px 12px;
      background: var(--input);
      color: var(--foreground);
      font: inherit;
      transition: border-color 120ms ease, box-shadow 120ms ease, background-color 120ms ease;
    }
    input::placeholder, textarea::placeholder {
      color: #64748b;
    }
    input:focus, select:focus, textarea:focus, button:focus-visible {
      outline: none;
      border-color: var(--ring);
      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.22);
    }
    textarea {
      min-height: 124px;
      resize: vertical;
      padding: 11px 12px;
    }
    button {
      width: 100%;
      min-height: 40px;
      border: 1px solid transparent;
      border-radius: var(--radius);
      padding: 9px 12px;
      background: var(--secondary);
      color: var(--secondary-foreground);
      font: inherit;
      font-weight: 600;
      cursor: pointer;
      transition: transform 120ms ease, background-color 120ms ease, border-color 120ms ease, opacity 120ms ease;
    }
    button:hover { transform: translateY(-1px); }
    button:active { transform: translateY(0); }
    button:disabled {
      opacity: 0.6;
      cursor: not-allowed;
      transform: none;
    }
    .primary {
      background: var(--primary);
      color: var(--primary-foreground);
    }
    .secondary {
      background: var(--secondary);
      border-color: var(--border);
      color: var(--secondary-foreground);
    }
    .danger {
      background: var(--destructive);
      color: var(--destructive-foreground);
    }
    .ghost {
      background: transparent;
      border-color: var(--border);
      color: var(--foreground);
    }
    .muted { color: var(--muted-foreground); }
    .status {
      min-height: 38px;
      border-radius: var(--radius);
      border: 1px dashed var(--border);
      background: rgba(15, 23, 42, 0.45);
      color: #86efac;
      font-size: 0.95rem;
      padding: 8px 10px;
      margin-top: 2px;
    }
    .status.error {
      color: #fecaca;
      border-color: rgba(239, 68, 68, 0.5);
      background: rgba(127, 29, 29, 0.34);
    }
    .status.warn {
      color: #fde68a;
      border-color: rgba(245, 158, 11, 0.45);
      background: rgba(120, 53, 15, 0.26);
    }
    .hint {
      color: var(--muted-foreground);
      font-size: 0.82rem;
      line-height: 1.45;
    }
    .kpi {
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 12px;
      background: rgba(15, 23, 42, 0.65);
    }
    .kpi strong {
      display: block;
      font-size: 1.18rem;
      margin-bottom: 4px;
      letter-spacing: -0.01em;
    }
    .list {
      display: grid;
      gap: 8px;
      max-height: 320px;
      overflow: auto;
      padding-right: 2px;
    }
    .target-card {
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 10px 12px;
      background: rgba(15, 23, 42, 0.62);
      color: var(--foreground);
      text-align: left;
      transition: border-color 120ms ease, background-color 120ms ease, transform 120ms ease;
    }
    .target-card:hover {
      border-color: #475569;
      background: rgba(30, 41, 59, 0.64);
      transform: translateY(-1px);
    }
    .target-card.active {
      border-color: var(--ring);
      background: rgba(30, 58, 138, 0.24);
    }
    .badge-row { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; }
    .badge {
      display: inline-flex;
      align-items: center;
      padding: 4px 8px;
      border-radius: 999px;
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid #334155;
      color: #cbd5e1;
      font-size: 0.78rem;
    }
    .badge.ok {
      color: #bbf7d0;
      border-color: rgba(34, 197, 94, 0.5);
      background: rgba(20, 83, 45, 0.4);
    }
    .badge.bad {
      color: #fecdd3;
      border-color: rgba(239, 68, 68, 0.5);
      background: rgba(127, 29, 29, 0.4);
    }
    .section-title { display: flex; align-items: center; justify-content: space-between; gap: 10px; }
    .section-title h2 {
      font-size: 1.02rem;
      letter-spacing: -0.01em;
    }
    .row-inline { display: flex; gap: 8px; align-items: center; }
    .row-inline > button { flex: 1; }
    .checkbox {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 9px 12px;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      background: var(--input);
    }
    .checkbox input {
      width: 16px;
      height: 16px;
      margin: 0;
      accent-color: #3b82f6;
    }
    pre {
      margin: 0;
      padding: 12px;
      background: rgba(2, 6, 23, 0.92);
      border-radius: var(--radius);
      border: 1px solid var(--border);
      color: #dbeafe;
      overflow: auto;
      white-space: pre-wrap;
      word-break: break-word;
      min-height: 240px;
      font-size: 0.86rem;
      line-height: 1.5;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
    }
    details.fold {
      border: 1px dashed var(--border);
      border-radius: var(--radius);
      background: rgba(11, 18, 34, 0.5);
      padding: 10px 12px;
    }
    details.fold > summary {
      cursor: pointer;
      font-weight: 600;
      color: var(--foreground);
      list-style: none;
      user-select: none;
    }
    details.fold > summary::-webkit-details-marker {
      display: none;
    }
    details.fold > summary::after {
      content: "Show";
      float: right;
      color: var(--muted-foreground);
      font-size: 0.78rem;
      font-weight: 500;
    }
    details.fold[open] > summary::after {
      content: "Hide";
    }
    .fold-body {
      margin-top: 10px;
      display: grid;
      gap: 10px;
    }
    @media (max-width: 900px) {
      .main-grid, .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
      .row-inline {
        flex-direction: column;
        align-items: stretch;
      }
      .wrap { padding-bottom: 110px; }
    }
    @media (max-width: 520px) {
      .wrap { padding: 18px 12px 100px; }
      .card { padding: 13px; }
      button, input, select, textarea { font-size: 16px; }
    }
  </style>
</head>
<body>
  <div class="wrap">
    <section class="hero">
      <span class="pill">PocketClaw · Mobile voice → SSH → tmux → Codex</span>
      <h1>Multi-target SSH control console</h1>
      <p class="sub">Manage multiple SSH targets, group and favorite them, monitor their tmux agent panes, then use local speech-to-text to send commands into the exact Codex pane you want.</p>
    </section>

    <section class="card grid">
      <div class="grid-2">
        <div>
          <label for="token">Access token</label>
          <input id="token" type="password" placeholder="Only needed if PocketClaw was started with --token">
        </div>
        <div class="row-inline">
          <button class="secondary" id="refreshDashboard">Refresh dashboard</button>
          <button class="ghost" id="refreshState">Refresh selected target</button>
        </div>
      </div>
      <div class="grid-4">
        <div class="kpi"><strong id="profileCount">0</strong><span>Targets</span></div>
        <div class="kpi"><strong id="onlineCount">0</strong><span>Online</span></div>
        <div class="kpi"><strong id="sessionCount">0</strong><span>Sessions</span></div>
        <div class="kpi"><strong id="paneCount">0</strong><span>Agent panes</span></div>
      </div>
      <div class="grid-4">
        <div class="kpi"><strong id="dispatchMetric">-</strong><span>T_dispatch (sec)</span></div>
        <div class="kpi"><strong id="doneMetric">-</strong><span>T_done (sec)</span></div>
        <div class="kpi"><strong id="verifyMetric">-</strong><span>T_verify (sec)</span></div>
        <div class="kpi"><strong id="misrouteMetric">0%</strong><span>Misroute</span></div>
      </div>
      <div id="status" class="status"></div>
    </section>

    <section class="main-grid">
      <div class="grid">
        <section class="card grid">
          <div class="section-title"><h2>SSH Targets</h2><span class="hint">Favorites appear first</span></div>
          <div>
            <label for="profileSelect">Saved target</label>
            <select id="profileSelect"></select>
          </div>
          <div id="targetList" class="list"></div>
        </section>

        <section class="card grid">
          <div class="section-title"><h2>Target Profile</h2><span class="hint">Quick setup: name + host + username + auth</span></div>
          <div class="grid-3">
            <div>
              <label for="profileName">Name</label>
              <input id="profileName" placeholder="gpu-box">
            </div>
            <div>
              <label for="host">SSH host / IP</label>
              <input id="host" placeholder="192.168.1.20">
            </div>
            <div>
              <label for="username">SSH username</label>
              <input id="username" placeholder="ubuntu">
            </div>
          </div>
          <div class="grid-2">
            <div>
              <label for="password">SSH password (optional)</label>
              <input id="password" type="password" placeholder="Leave blank to keep existing password">
            </div>
            <div>
              <label for="keyFilename">SSH key path (optional)</label>
              <input id="keyFilename" placeholder="~/.ssh/id_ed25519">
            </div>
          </div>
          <div class="grid-4">
            <button class="primary" id="saveProfile">Save target</button>
            <button class="secondary" id="testProfile">Test SSH</button>
            <button class="secondary" id="loadProfileState">Load tmux state</button>
            <button class="danger" id="deleteProfile">Delete target</button>
          </div>
          <details class="fold">
            <summary>Advanced target options</summary>
            <div class="fold-body">
              <div class="grid-3">
                <div>
                  <label for="port">SSH port</label>
                  <input id="port" type="number" value="22">
                </div>
                <div>
                  <label for="profileGroup">Group</label>
                  <input id="profileGroup" placeholder="work">
                </div>
                <div>
                  <label for="profileTags">Tags</label>
                  <input id="profileTags" placeholder="gpu, research">
                </div>
              </div>
              <div class="grid-2">
                <div>
                  <label for="passwordRef">Password ref (vault)</label>
                  <input id="passwordRef" placeholder="env:POCKETCLAW_OFFICE_PWD or file:~/.secrets/office.pwd">
                </div>
                <div>
                  <label for="tmuxBin">tmux binary</label>
                  <input id="tmuxBin" value="tmux">
                </div>
              </div>
              <div>
                <label for="profileDescription">Description</label>
                <input id="profileDescription" placeholder="Research box with multiple Codex agents">
              </div>
              <div class="grid-3">
                <div>
                  <label for="hostKeyPolicy">Host key policy</label>
                  <select id="hostKeyPolicy">
                    <option value="">Inherit server default</option>
                    <option value="strict">strict (verify known_hosts)</option>
                    <option value="accept-new">accept-new (trust first use)</option>
                    <option value="insecure">insecure (skip verification)</option>
                  </select>
                </div>
                <div>
                  <label for="sshTimeout">SSH connect timeout (sec)</label>
                  <input id="sshTimeout" type="number" min="0" placeholder="0 = inherit">
                </div>
                <div>
                  <label for="sshCommandTimeout">SSH command timeout (sec)</label>
                  <input id="sshCommandTimeout" type="number" min="0" placeholder="0 = inherit">
                </div>
              </div>
              <div class="grid-2">
                <div>
                  <label for="sshRetries">SSH retries</label>
                  <input id="sshRetries" type="number" min="0" placeholder="0 = no retry">
                </div>
                <div>
                  <label for="sshRetryBackoffMs">Retry backoff (ms)</label>
                  <input id="sshRetryBackoffMs" type="number" min="0" placeholder="250">
                </div>
              </div>
              <div class="checkbox">
                <input id="profileFavorite" type="checkbox">
                <label for="profileFavorite" style="margin:0">Favorite target</label>
              </div>
            </div>
          </details>
        </section>
      </div>

      <div class="grid">
        <section class="card grid">
          <div class="section-title"><h2>Agent Pane</h2><span class="hint">Choose target → session → window → pane</span></div>
          <div class="grid-3">
            <div>
              <label for="session">tmux session</label>
              <select id="session"></select>
            </div>
            <div>
              <label for="window">tmux window</label>
              <select id="window"></select>
            </div>
            <div>
              <label for="pane">Agent pane</label>
              <select id="pane"></select>
            </div>
          </div>
          <div class="grid-2">
            <div>
              <label for="agentAlias">Pane alias</label>
              <input id="agentAlias" placeholder="backend-agent">
            </div>
            <div class="row-inline">
              <button class="secondary" id="saveAlias">Save alias</button>
              <button class="ghost" id="refreshPane">Refresh output</button>
            </div>
          </div>
        </section>

        <details class="card fold">
          <summary>Command templates (optional)</summary>
          <div class="fold-body">
            <div class="hint">Global or target-specific command snippets</div>
            <div class="grid-3">
              <div>
                <label for="templateSelect">Saved template</label>
                <select id="templateSelect"></select>
              </div>
              <div>
                <label for="templateName">Template name</label>
                <input id="templateName" placeholder="Run tests + summarize">
              </div>
              <div>
                <label for="templateScope">Scope</label>
                <select id="templateScope">
                  <option value="">Global</option>
                  <option value="current">Current target</option>
                </select>
              </div>
            </div>
            <div class="grid-3">
              <button class="secondary" id="applyTemplate">Apply template</button>
              <button class="secondary" id="saveTemplate">Save template</button>
              <button class="danger" id="deleteTemplate">Delete template</button>
            </div>
          </div>
        </details>

        <details class="card fold">
          <summary>Recent commands (optional)</summary>
          <div class="fold-body">
            <div class="hint">Quickly reuse recent prompts</div>
            <div class="grid-3">
              <div>
                <label for="historySelect">History</label>
                <select id="historySelect"></select>
              </div>
              <button class="secondary" id="applyHistory">Apply recent command</button>
              <button class="danger" id="clearHistory">Clear history</button>
            </div>
          </div>
        </details>
      </div>
    </section>

    <section class="card grid">
      <div class="section-title"><h2>Current Agent</h2><span class="hint">All sends and todo actions go to this target</span></div>
      <div class="kpi">
        <strong id="currentAgentLabel">No pane selected</strong>
        <span id="currentAgentHint">Choose profile → session → window → pane first.</span>
      </div>
    </section>

    <section class="card grid">
      <div class="section-title"><h2>Agent Todos</h2><span class="hint">Publish tasks, track status, and attach evidence</span></div>
      <div class="grid-3">
        <div>
          <label for="todoTitle">Todo title</label>
          <input id="todoTitle" placeholder="Fix auth flaky test">
        </div>
        <div>
          <label for="todoPriority">Priority</label>
          <select id="todoPriority">
            <option value="low">low</option>
            <option value="medium" selected>medium</option>
            <option value="high">high</option>
            <option value="urgent">urgent</option>
          </select>
        </div>
        <div>
          <label for="todoAssignee">Assignee</label>
          <input id="todoAssignee" placeholder="backend-agent">
        </div>
      </div>
      <div>
        <label for="todoDetail">Todo detail</label>
        <textarea id="todoDetail" placeholder="Expected output, acceptance criteria, and constraints"></textarea>
      </div>
      <div class="grid-4">
        <button class="primary" id="createTodo">Publish todo to current agent</button>
        <button class="secondary" id="quickTodo">Quick task</button>
        <button class="secondary" id="createTriplet">Triplet workflow</button>
        <button class="secondary" id="refreshTodos">Refresh todos</button>
      </div>
      <div class="grid-3">
        <div>
          <label for="todoSelect">Todos for current agent</label>
          <select id="todoSelect"></select>
        </div>
        <div>
          <label for="todoStatus">Status</label>
          <select id="todoStatus">
            <option value="todo">todo</option>
            <option value="in_progress">in_progress</option>
            <option value="done">done</option>
            <option value="verified">verified</option>
            <option value="blocked">blocked</option>
          </select>
        </div>
        <div>
          <label for="todoProgressNote">Progress note</label>
          <input id="todoProgressNote" placeholder="what changed in this step">
        </div>
      </div>
      <div>
        <label for="todoEvidence">Evidence (text or JSON)</label>
        <textarea id="todoEvidence" placeholder='Text note, or JSON like {"type":"pane_output","content":"tests passed"}'></textarea>
      </div>
      <div class="grid-4">
        <button class="secondary" id="applyTodoToCommand">Use todo in command</button>
        <button class="secondary" id="updateTodoStatus">Update status</button>
        <button class="secondary" id="addTodoEvidence">Add evidence</button>
        <button class="ghost" id="reportTodo">Agent report</button>
      </div>
      <div class="grid-3">
        <div>
          <label for="todoTemplateSelect">Todo template</label>
          <select id="todoTemplateSelect"></select>
        </div>
        <div>
          <label for="todoTemplateName">Template name</label>
          <input id="todoTemplateName" placeholder="Bugfix task template">
        </div>
        <div class="row-inline">
          <button class="secondary" id="applyTodoTemplate">Apply template</button>
          <button class="secondary" id="saveTodoTemplate">Save template</button>
          <button class="danger" id="deleteTodoTemplate">Delete template</button>
        </div>
      </div>
      <div class="grid-2">
        <div>
          <label for="todoTimeline">Todo timeline</label>
          <pre id="todoTimeline">No todo selected.</pre>
        </div>
        <div>
          <label for="todoEvidenceList">Evidence list</label>
          <pre id="todoEvidenceList">No evidence yet.</pre>
        </div>
      </div>
      <div>
        <label for="auditSelect">Recent audit events (current agent)</label>
        <select id="auditSelect"></select>
      </div>
      <div class="hint" id="todoMeta">No todo selected.</div>
    </section>

    <section class="card grid">
      <div class="section-title"><h2>Command Console</h2><span class="hint">Speech recognition runs in your mobile browser</span></div>
      <div>
        <label for="command">Command</label>
        <textarea id="command" placeholder="Say something like: analyze the auth bug, fix it, run tests, and summarize the diff"></textarea>
      </div>
      <div class="grid-4">
        <button class="primary" id="startVoice">Start voice</button>
        <button class="secondary" id="stopVoice">Stop voice</button>
        <button class="primary" id="sendCommand">Send to agent</button>
        <button class="danger" id="interrupt">Send Ctrl+C</button>
      </div>
      <div class="grid-2">
        <button class="ghost" id="appendNewline">Insert newline</button>
        <button class="ghost" id="copyTargetLabel">Copy target label</button>
      </div>
    </section>

    <section class="card grid">
      <div class="section-title"><h2>Recent Pane Output</h2><span class="hint" id="selectedPaneLabel">No pane selected</span></div>
      <pre id="paneOutput">Choose a target first.</pre>
    </section>
  </div>

  <script>
    const tokenInput = document.getElementById('token');
    const statusEl = document.getElementById('status');
    const profileSelect = document.getElementById('profileSelect');
    const targetListEl = document.getElementById('targetList');
    const profileNameInput = document.getElementById('profileName');
    const profileGroupInput = document.getElementById('profileGroup');
    const profileTagsInput = document.getElementById('profileTags');
    const hostInput = document.getElementById('host');
    const portInput = document.getElementById('port');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const passwordRefInput = document.getElementById('passwordRef');
    const keyFilenameInput = document.getElementById('keyFilename');
    const tmuxBinInput = document.getElementById('tmuxBin');
    const profileDescriptionInput = document.getElementById('profileDescription');
    const hostKeyPolicySelect = document.getElementById('hostKeyPolicy');
    const sshTimeoutInput = document.getElementById('sshTimeout');
    const sshCommandTimeoutInput = document.getElementById('sshCommandTimeout');
    const sshRetriesInput = document.getElementById('sshRetries');
    const sshRetryBackoffMsInput = document.getElementById('sshRetryBackoffMs');
    const profileFavoriteInput = document.getElementById('profileFavorite');
    const sessionSelect = document.getElementById('session');
    const windowSelect = document.getElementById('window');
    const paneSelect = document.getElementById('pane');
    const aliasInput = document.getElementById('agentAlias');
    const templateSelect = document.getElementById('templateSelect');
    const templateNameInput = document.getElementById('templateName');
    const templateScopeSelect = document.getElementById('templateScope');
    const historySelect = document.getElementById('historySelect');
    const commandInput = document.getElementById('command');
    const paneOutputEl = document.getElementById('paneOutput');
    const selectedPaneLabel = document.getElementById('selectedPaneLabel');
    const currentAgentLabelEl = document.getElementById('currentAgentLabel');
    const currentAgentHintEl = document.getElementById('currentAgentHint');
    const todoTitleInput = document.getElementById('todoTitle');
    const todoDetailInput = document.getElementById('todoDetail');
    const todoPrioritySelect = document.getElementById('todoPriority');
    const todoAssigneeInput = document.getElementById('todoAssignee');
    const todoSelect = document.getElementById('todoSelect');
    const todoStatusSelect = document.getElementById('todoStatus');
    const todoProgressNoteInput = document.getElementById('todoProgressNote');
    const todoEvidenceInput = document.getElementById('todoEvidence');
    const todoTemplateSelect = document.getElementById('todoTemplateSelect');
    const todoTemplateNameInput = document.getElementById('todoTemplateName');
    const todoTimelineEl = document.getElementById('todoTimeline');
    const todoEvidenceListEl = document.getElementById('todoEvidenceList');
    const auditSelect = document.getElementById('auditSelect');
    const todoMetaEl = document.getElementById('todoMeta');
    const profileCountEl = document.getElementById('profileCount');
    const onlineCountEl = document.getElementById('onlineCount');
    const sessionCountEl = document.getElementById('sessionCount');
    const paneCountEl = document.getElementById('paneCount');
    const dispatchMetricEl = document.getElementById('dispatchMetric');
    const doneMetricEl = document.getElementById('doneMetric');
    const verifyMetricEl = document.getElementById('verifyMetric');
    const misrouteMetricEl = document.getElementById('misrouteMetric');

    const storedToken = localStorage.getItem('pocketclaw-token') || '';
    tokenInput.value = storedToken;

    let profilesCache = [];
    let dashboardCache = { targets: [] };
    let stateCache = { sessions: [] };
    let templatesCache = [];
    let historyCache = [];
    let todosCache = [];
    let todoTemplatesCache = [];
    let auditLogsCache = [];
    let todoStream = null;

    function headers() {
      const token = tokenInput.value.trim();
      if (token) {
        localStorage.setItem('pocketclaw-token', token);
      } else {
        localStorage.removeItem('pocketclaw-token');
      }
      const result = { 'Content-Type': 'application/json' };
      if (token) {
        result['Authorization'] = `Bearer ${token}`;
      }
      return result;
    }

    function setStatus(message, type = 'info') {
      statusEl.textContent = message;
      statusEl.classList.remove('error', 'warn');
      if (type === 'error') statusEl.classList.add('error');
      if (type === 'warn') statusEl.classList.add('warn');
    }

    function optionalIntOrZero(value) {
      const parsed = Number.parseInt(String(value || '').trim(), 10);
      if (!Number.isFinite(parsed)) return 0;
      return Math.max(0, parsed);
    }

    async function api(path, options = {}) {
      const response = await fetch(path, {
        ...options,
        headers: { ...headers(), ...(options.headers || {}) },
      });
      const payload = await response.json().catch(() => ({}));
      if (!response.ok) {
        throw new Error(payload.error || `Request failed (${response.status})`);
      }
      return payload;
    }

    function currentProfileName() {
      return profileSelect.value.trim();
    }

    function currentProfile() {
      return profilesCache.find((profile) => profile.name === currentProfileName()) || null;
    }

    function currentDashboardTarget() {
      return (dashboardCache.targets || []).find((target) => target.name === currentProfileName()) || null;
    }

    function profileLabel(profile) {
      const favorite = profile.favorite ? '★ ' : '';
      const group = profile.group ? ` · ${profile.group}` : '';
      return `${favorite}${profile.name}${group}`;
    }

    function targetStatusLabel(target) {
      const status = target.online ? 'online' : 'offline';
      return `${target.name} · ${status} · ${target.session_count} sessions · ${target.pane_count} panes`;
    }

    function fillProfileForm(profile) {
      if (!profile) {
        profileNameInput.value = '';
        profileGroupInput.value = 'General';
        profileTagsInput.value = '';
        hostInput.value = '';
        portInput.value = '22';
        usernameInput.value = '';
        passwordInput.value = '';
        passwordRefInput.value = '';
        passwordInput.placeholder = 'Leave blank to keep existing password';
        keyFilenameInput.value = '';
        tmuxBinInput.value = 'tmux';
        profileDescriptionInput.value = '';
        hostKeyPolicySelect.value = '';
        sshTimeoutInput.value = '';
        sshCommandTimeoutInput.value = '';
        sshRetriesInput.value = '';
        sshRetryBackoffMsInput.value = '';
        profileFavoriteInput.checked = false;
        return;
      }
      profileNameInput.value = profile.name || '';
      profileGroupInput.value = profile.group || 'General';
      profileTagsInput.value = (profile.tags || []).join(', ');
      hostInput.value = profile.host || '';
      portInput.value = String(profile.port || 22);
      usernameInput.value = profile.username || '';
      passwordInput.value = '';
      passwordRefInput.value = profile.password_ref || '';
      passwordInput.placeholder = profile.has_password ? 'Stored password is kept unless you enter a new one' : 'Optional password';
      keyFilenameInput.value = profile.key_filename || '';
      tmuxBinInput.value = profile.tmux_bin || 'tmux';
      profileDescriptionInput.value = profile.description || '';
      hostKeyPolicySelect.value = profile.host_key_policy || '';
      sshTimeoutInput.value = profile.ssh_timeout ? String(profile.ssh_timeout) : '';
      sshCommandTimeoutInput.value = profile.ssh_command_timeout ? String(profile.ssh_command_timeout) : '';
      sshRetriesInput.value = profile.ssh_retries ? String(profile.ssh_retries) : '';
      sshRetryBackoffMsInput.value = profile.ssh_retry_backoff_ms ? String(profile.ssh_retry_backoff_ms) : '';
      profileFavoriteInput.checked = Boolean(profile.favorite);
    }

    function readProfileForm() {
      return {
        name: profileNameInput.value.trim(),
        group: profileGroupInput.value.trim() || 'General',
        tags: profileTagsInput.value.trim(),
        host: hostInput.value.trim(),
        port: Number(portInput.value || '22'),
        username: usernameInput.value.trim(),
        password: passwordInput.value,
        password_ref: passwordRefInput.value.trim(),
        key_filename: keyFilenameInput.value.trim(),
        tmux_bin: tmuxBinInput.value.trim() || 'tmux',
        description: profileDescriptionInput.value.trim(),
        host_key_policy: hostKeyPolicySelect.value.trim(),
        ssh_timeout: optionalIntOrZero(sshTimeoutInput.value),
        ssh_command_timeout: optionalIntOrZero(sshCommandTimeoutInput.value),
        ssh_retries: optionalIntOrZero(sshRetriesInput.value),
        ssh_retry_backoff_ms: optionalIntOrZero(sshRetryBackoffMsInput.value),
        favorite: profileFavoriteInput.checked,
      };
    }

    function updateKpis() {
      profileCountEl.textContent = String(dashboardCache.profile_count || profilesCache.length || 0);
      onlineCountEl.textContent = String(dashboardCache.online_count || 0);
      const sessions = stateCache.sessions || [];
      const windows = sessions.flatMap((session) => session.windows || []);
      const panes = windows.flatMap((window) => window.panes || []);
      sessionCountEl.textContent = String(sessions.length);
      paneCountEl.textContent = String(panes.length);
      const metrics = dashboardCache.workflow_metrics || {};
      const dispatch = Number(metrics.t_dispatch_avg_sec);
      const done = Number(metrics.t_done_avg_sec);
      const verify = Number(metrics.t_verify_avg_sec);
      const misroute = Number(metrics.misroute_pct);
      dispatchMetricEl.textContent = Number.isFinite(dispatch) ? String(Math.round(dispatch)) : '-';
      doneMetricEl.textContent = Number.isFinite(done) ? String(Math.round(done)) : '-';
      verifyMetricEl.textContent = Number.isFinite(verify) ? String(Math.round(verify)) : '-';
      misrouteMetricEl.textContent = Number.isFinite(misroute) ? `${misroute.toFixed(2)}%` : '0%';
    }

    function option(label, value) {
      const element = document.createElement('option');
      element.value = value;
      element.textContent = label;
      return element;
    }

    function selectedSessionData() {
      return (stateCache.sessions || []).find((session) => session.name === sessionSelect.value) || null;
    }

    function selectedWindowData() {
      const session = selectedSessionData();
      return session ? (session.windows || []).find((window) => String(window.index) === windowSelect.value) || null : null;
    }

    function selectedPaneData() {
      const window = selectedWindowData();
      return window ? (window.panes || []).find((pane) => pane.target === paneSelect.value) || null : null;
    }

    function currentTargetLabel() {
      const profile = currentProfileName();
      const target = paneSelect.value.trim();
      if (!profile || !target) return 'No pane selected';
      const pane = selectedPaneData();
      const alias = pane && pane.alias ? ` (${pane.alias})` : '';
      return `${profile} → ${target}${alias}`;
    }

    function updateCurrentAgentCard() {
      const profile = currentProfileName();
      const target = paneSelect.value.trim();
      currentAgentLabelEl.textContent = currentTargetLabel();
      if (!profile || !target) {
        currentAgentHintEl.textContent = 'Choose profile → session → window → pane first.';
        return;
      }
      const pane = selectedPaneData();
      const alias = pane && pane.alias ? pane.alias : '(no alias)';
      const cmd = pane && pane.current_command ? pane.current_command : 'shell';
      currentAgentHintEl.textContent = `profile=${profile} · pane=${target} · alias=${alias} · cmd=${cmd}`;
    }

    function requireCurrentAgent(action, silent = false) {
      const profile = currentProfileName();
      const target = paneSelect.value.trim();
      if (!profile || !target) {
        if (!silent) setStatus(`Choose a target and pane before ${action}.`, 'error');
        return null;
      }
      return { profile, target };
    }

    function selectedTodo() {
      return todosCache.find((todo) => todo.id === todoSelect.value) || null;
    }

    function parseEvidenceInput(raw) {
      const text = String(raw || '').trim();
      if (!text) return null;
      if ((text.startsWith('{') && text.endsWith('}')) || (text.startsWith('[') && text.endsWith(']'))) {
        try {
          return JSON.parse(text);
        } catch (_) {
          return text;
        }
      }
      return text;
    }

    function closeTodoStream() {
      if (todoStream) {
        todoStream.close();
        todoStream = null;
      }
    }

    function openTodoStream() {
      closeTodoStream();
      const selected = requireCurrentAgent('starting live updates', true);
      if (!selected || !window.EventSource) return;
      const token = tokenInput.value.trim();
      const query = new URLSearchParams({
        profile: selected.profile,
        target: selected.target,
        interval: '3',
      });
      if (token) query.set('token', token);
      const streamUrl = `/api/todos/stream?${query.toString()}`;
      todoStream = new EventSource(streamUrl);
      todoStream.onmessage = (event) => {
        try {
          const payload = JSON.parse(event.data || '{}');
          todosCache = payload.todos || [];
          renderTodos();
          loadAuditLogs().catch(() => {});
          loadDashboard().catch(() => {});
        } catch (_) {
          // ignore malformed chunks
        }
      };
      todoStream.onerror = () => {
        // Connection may be rotated by server; fallback polling remains active.
      };
    }

    function renderProfileSelect() {
      const previous = currentProfileName();
      profileSelect.innerHTML = '';
      if (!profilesCache.length) {
        profileSelect.appendChild(option('No saved targets', ''));
        fillProfileForm(null);
        return;
      }
      profilesCache.forEach((profile) => profileSelect.appendChild(option(profileLabel(profile), profile.name)));
      profileSelect.value = profilesCache.some((profile) => profile.name === previous) ? previous : profilesCache[0].name;
      fillProfileForm(currentProfile());
    }

    function renderTargetCards() {
      targetListEl.innerHTML = '';
      const targets = dashboardCache.targets || [];
      if (!targets.length) {
        targetListEl.innerHTML = '<div class="muted">No targets yet. Save one to get started.</div>';
        return;
      }
      targets.forEach((target) => {
        const card = document.createElement('button');
        card.type = 'button';
        card.className = `target-card ${target.name === currentProfileName() ? 'active' : ''}`;
        const todoSummary = target.todo_summary || {};
        const inProgress = Number(todoSummary.in_progress_count || 0);
        const lastNote = String(todoSummary.last_note || '').trim();
        card.innerHTML = `
          <div class="section-title"><strong>${target.favorite ? '★ ' : ''}${target.name}</strong><span class="muted">${target.host}</span></div>
          <div class="badge-row">
            <span class="badge ${target.online ? 'ok' : 'bad'}">${target.online ? 'Online' : 'Offline'}</span>
            <span class="badge">${target.group || 'General'}</span>
            <span class="badge">${target.session_count} sessions</span>
            <span class="badge">${target.pane_count} panes</span>
            <span class="badge">${inProgress} in-progress todos</span>
          </div>
          <div class="hint">${target.error ? target.error : (lastNote || target.description || target.tags.join(', ') || 'Ready')}</div>
        `;
        card.addEventListener('click', async () => {
          profileSelect.value = target.name;
          fillProfileForm(currentProfile());
          await loadSelectedProfile();
        });
        targetListEl.appendChild(card);
      });
    }

    function renderSessions() {
      const previousSession = sessionSelect.value;
      sessionSelect.innerHTML = '';
      const sessions = stateCache.sessions || [];
      if (!sessions.length) {
        sessionSelect.appendChild(option('No tmux sessions', ''));
        windowSelect.innerHTML = '';
        paneSelect.innerHTML = '';
        aliasInput.value = '';
        selectedPaneLabel.textContent = currentTargetLabel();
        updateKpis();
        return;
      }
      sessions.forEach((session) => {
        sessionSelect.appendChild(option(`${session.name} (${(session.windows || []).length} windows)`, session.name));
      });
      sessionSelect.value = sessions.some((session) => session.name === previousSession) ? previousSession : sessions[0].name;
      renderWindows();
      updateKpis();
    }

    function renderWindows() {
      const previousWindow = windowSelect.value;
      const session = selectedSessionData();
      windowSelect.innerHTML = '';
      if (!session || !(session.windows || []).length) {
        windowSelect.appendChild(option('No windows', ''));
        paneSelect.innerHTML = '';
        aliasInput.value = '';
        selectedPaneLabel.textContent = currentTargetLabel();
        return;
      }
      session.windows.forEach((window) => {
        windowSelect.appendChild(option(`${window.index}: ${window.name}${window.active ? ' · active' : ''}`, String(window.index)));
      });
      const fallback = session.windows.find((window) => window.active) || session.windows[0];
      windowSelect.value = session.windows.some((window) => String(window.index) === previousWindow) ? previousWindow : String(fallback.index);
      renderPanes();
    }

    function renderPanes() {
      const previousPane = paneSelect.value;
      const window = selectedWindowData();
      paneSelect.innerHTML = '';
      if (!window || !(window.panes || []).length) {
        paneSelect.appendChild(option('No panes', ''));
        aliasInput.value = '';
        selectedPaneLabel.textContent = currentTargetLabel();
        return;
      }
      window.panes.forEach((pane) => {
        const aliasPrefix = pane.alias ? `${pane.alias} · ` : '';
        const cmd = pane.current_command || 'shell';
        paneSelect.appendChild(option(`${aliasPrefix}${pane.target} · ${cmd}${pane.active ? ' · active' : ''}`, pane.target));
      });
      const fallback = window.panes.find((pane) => pane.active) || window.panes[0];
      paneSelect.value = window.panes.some((pane) => pane.target === previousPane) ? previousPane : fallback.target;
      syncAliasInput();
    }

    function syncAliasInput() {
      const pane = selectedPaneData();
      aliasInput.value = pane ? (pane.alias || '') : '';
      selectedPaneLabel.textContent = currentTargetLabel();
      updateCurrentAgentCard();
    }

    function renderTemplates() {
      templateSelect.innerHTML = '';
      if (!templatesCache.length) {
        templateSelect.appendChild(option('No templates yet', ''));
        return;
      }
      templatesCache.forEach((template) => {
        const scope = template.profile ? ` · ${template.profile}` : ' · global';
        templateSelect.appendChild(option(`${template.name}${scope}`, template.id));
      });
    }

    function renderHistory() {
      historySelect.innerHTML = '';
      if (!historyCache.length) {
        historySelect.appendChild(option('No recent commands', ''));
        return;
      }
      historyCache.forEach((entry) => {
        const label = `${entry.profile} · ${entry.alias || entry.target} · ${entry.command.slice(0, 40)}`;
        historySelect.appendChild(option(label, entry.id));
      });
    }

    function renderTodoTemplates() {
      const previous = todoTemplateSelect.value;
      todoTemplateSelect.innerHTML = '';
      if (!todoTemplatesCache.length) {
        todoTemplateSelect.appendChild(option('No todo templates', ''));
        todoTemplateNameInput.value = '';
        return;
      }
      todoTemplatesCache.forEach((template) => {
        const scope = template.target ? ` · ${template.target}` : (template.profile ? ` · ${template.profile}` : ' · global');
        todoTemplateSelect.appendChild(option(`${template.name}${scope}`, template.id));
      });
      todoTemplateSelect.value = todoTemplatesCache.some((item) => item.id === previous) ? previous : todoTemplatesCache[0].id;
      const selected = todoTemplatesCache.find((item) => item.id === todoTemplateSelect.value);
      todoTemplateNameInput.value = selected ? selected.name : '';
    }

    function renderAuditLogs() {
      auditSelect.innerHTML = '';
      if (!auditLogsCache.length) {
        auditSelect.appendChild(option('No audit events', ''));
        return;
      }
      auditLogsCache.forEach((entry) => {
        const actor = entry.actor || 'unknown';
        const label = `${entry.created_at} · ${entry.action} · ${actor} · ${entry.note || entry.status || '-'}`;
        auditSelect.appendChild(option(label.slice(0, 140), entry.id));
      });
    }

    function renderTodos() {
      const previous = todoSelect.value;
      todoSelect.innerHTML = '';
      if (!todosCache.length) {
        todoSelect.appendChild(option('No todos for current agent', ''));
        todoStatusSelect.value = 'todo';
        todoProgressNoteInput.value = '';
        todoMetaEl.textContent = 'No todo selected.';
        return;
      }

      todosCache.forEach((todo) => {
        const shortTitle = todo.title.length > 42 ? `${todo.title.slice(0, 42)}...` : todo.title;
        const label = `[${todo.status}] [${todo.priority}] ${shortTitle}`;
        todoSelect.appendChild(option(label, todo.id));
      });
      todoSelect.value = todosCache.some((todo) => todo.id === previous) ? previous : todosCache[0].id;
      syncTodoInspector();
    }

    function syncTodoInspector() {
      const todo = selectedTodo();
      if (!todo) {
        todoStatusSelect.value = 'todo';
        todoProgressNoteInput.value = '';
        todoMetaEl.textContent = 'No todo selected.';
        todoTimelineEl.textContent = 'No todo selected.';
        todoEvidenceListEl.textContent = 'No evidence yet.';
        return;
      }
      todoStatusSelect.value = todo.status || 'todo';
      todoProgressNoteInput.value = todo.progress_note || '';
      const evidenceCount = (todo.evidence || []).length;
      const alias = todo.alias || '(no alias)';
      todoMetaEl.textContent = `${todo.profile} -> ${todo.target} (${alias}) · ${todo.status} · evidence ${evidenceCount} · updated ${todo.updated_at || '-'}`;
      const timelineLines = (todo.events || []).map((event) => {
        const ts = event.created_at || '-';
        const actor = event.actor || 'unknown';
        const status = event.status ? ` [${event.status}]` : '';
        const note = event.note || '';
        return `${ts} · ${actor}${status} · ${note}`;
      });
      todoTimelineEl.textContent = timelineLines.length ? timelineLines.join('\n') : 'No timeline events.';
      const evidenceLines = (todo.evidence || []).map((entry) => {
        const ts = entry.created_at || '-';
        const source = entry.source ? ` · ${entry.source}` : '';
        return `${ts} · ${entry.type}${source}\n${entry.content}`;
      });
      todoEvidenceListEl.textContent = evidenceLines.length ? evidenceLines.join('\n\n') : 'No evidence yet.';
    }

    async function loadProfiles() {
      const data = await api('/api/profiles');
      profilesCache = data.profiles || [];
      renderProfileSelect();
    }

    async function loadDashboard() {
      const data = await api('/api/dashboard');
      dashboardCache = data;
      renderTargetCards();
      updateKpis();
    }

    async function loadTemplates() {
      const profile = currentProfileName();
      const data = await api(`/api/templates?profile=${encodeURIComponent(profile)}`);
      templatesCache = data.templates || [];
      renderTemplates();
    }

    async function loadHistory() {
      const profile = currentProfileName();
      const data = await api(`/api/history?profile=${encodeURIComponent(profile)}&limit=25`);
      historyCache = data.history || [];
      renderHistory();
    }

    async function loadTodoTemplates() {
      const profile = currentProfileName();
      const target = paneSelect.value.trim();
      const data = await api(`/api/todo-templates?profile=${encodeURIComponent(profile)}&target=${encodeURIComponent(target)}`);
      todoTemplatesCache = data.templates || [];
      renderTodoTemplates();
    }

    async function loadAuditLogs() {
      const selected = requireCurrentAgent('loading audit logs', true);
      if (!selected) {
        auditLogsCache = [];
        renderAuditLogs();
        return;
      }
      const data = await api(`/api/audit?profile=${encodeURIComponent(selected.profile)}&target=${encodeURIComponent(selected.target)}&limit=25`);
      auditLogsCache = data.logs || [];
      renderAuditLogs();
    }

    async function loadTodos() {
      const selected = requireCurrentAgent('loading todos', true);
      if (!selected) {
        todosCache = [];
        renderTodos();
        await loadAuditLogs();
        updateCurrentAgentCard();
        closeTodoStream();
        return;
      }
      const data = await api(`/api/todos?profile=${encodeURIComponent(selected.profile)}&target=${encodeURIComponent(selected.target)}`);
      todosCache = data.todos || [];
      renderTodos();
      await Promise.all([loadTodoTemplates(), loadAuditLogs()]);
      openTodoStream();
      updateCurrentAgentCard();
    }

    async function loadRemoteState() {
      const profile = currentProfileName();
      if (!profile) {
        stateCache = { sessions: [] };
        renderSessions();
        paneOutputEl.textContent = 'Choose a target first.';
        todosCache = [];
        renderTodos();
        updateCurrentAgentCard();
        return;
      }
      const currentSession = sessionSelect.value;
      const currentWindow = windowSelect.value;
      const currentPane = paneSelect.value;
      const data = await api(`/api/remote/state?profile=${encodeURIComponent(profile)}`);
      stateCache = data;
      renderSessions();
      if (currentSession) {
        const session = (stateCache.sessions || []).find((item) => item.name === currentSession);
        if (session) {
          sessionSelect.value = currentSession;
          renderWindows();
        }
      }
      if (currentWindow) {
        const window = selectedSessionData() ? (selectedSessionData().windows || []).find((item) => String(item.index) === currentWindow) : null;
        if (window) {
          windowSelect.value = currentWindow;
          renderPanes();
        }
      }
      if (currentPane) {
        const pane = selectedWindowData() ? (selectedWindowData().panes || []).find((item) => item.target === currentPane) : null;
        if (pane) {
          paneSelect.value = currentPane;
          syncAliasInput();
        }
      }
      await loadPane();
      await loadTodos();
      updateCurrentAgentCard();
    }

    async function loadPane() {
      const profile = currentProfileName();
      const target = paneSelect.value.trim();
      selectedPaneLabel.textContent = currentTargetLabel();
      if (!profile || !target) {
        paneOutputEl.textContent = 'Choose a target and pane first.';
        return;
      }
      const data = await api(`/api/pane?profile=${encodeURIComponent(profile)}&target=${encodeURIComponent(target)}&lines=120`);
      paneOutputEl.textContent = data.output || '[empty pane]';
    }

    async function loadSelectedProfile() {
      fillProfileForm(currentProfile());
      await Promise.all([loadTemplates(), loadHistory()]);
      try {
        await loadRemoteState();
      } catch (error) {
        stateCache = { sessions: [] };
        renderSessions();
        paneOutputEl.textContent = error.message;
        todosCache = [];
        renderTodos();
        closeTodoStream();
        updateCurrentAgentCard();
        setStatus(error.message, 'error');
      }
      renderTargetCards();
    }

    async function refreshAll() {
      try {
        await Promise.all([loadProfiles(), loadDashboard()]);
        await loadSelectedProfile();
        setStatus('Dashboard refreshed.');
      } catch (error) {
        setStatus(error.message, 'error');
      }
    }

    async function saveProfile() {
      const profile = readProfileForm();
      if (!profile.name || !profile.host || !profile.username) {
        setStatus('Name, host and username are required.', 'error');
        return;
      }
      try {
        await api('/api/profiles/save', { method: 'POST', body: JSON.stringify(profile) });
        await Promise.all([loadProfiles(), loadDashboard()]);
        profileSelect.value = profile.name;
        await loadSelectedProfile();
        setStatus(`Saved target ${profile.name}.`);
      } catch (error) {
        setStatus(error.message, 'error');
      }
    }

    async function testProfile() {
      const profile = readProfileForm();
      if (!profile.name || !profile.host || !profile.username) {
        setStatus('Fill name, host and username first.', 'error');
        return;
      }
      try {
        const data = await api('/api/profiles/test', { method: 'POST', body: JSON.stringify(profile) });
        if (data.ok) {
          setStatus(`SSH ok · ${data.session_count} session(s), ${data.pane_count} pane(s).`);
        } else {
          setStatus(data.error || 'SSH test failed.', 'error');
        }
      } catch (error) {
        setStatus(error.message, 'error');
      }
    }

    async function deleteProfile() {
      const name = currentProfileName() || profileNameInput.value.trim();
      if (!name) {
        setStatus('Choose a target to delete.', 'error');
        return;
      }
      try {
        await api('/api/profiles/delete', { method: 'POST', body: JSON.stringify({ name }) });
        await Promise.all([loadProfiles(), loadDashboard()]);
        await loadSelectedProfile();
        setStatus(`Deleted target ${name}.`);
      } catch (error) {
        setStatus(error.message, 'error');
      }
    }

    async function saveAlias() {
      const profile = currentProfileName();
      const target = paneSelect.value.trim();
      if (!profile || !target) {
        setStatus('Choose a pane first.', 'error');
        return;
      }
      try {
        await api('/api/alias/save', { method: 'POST', body: JSON.stringify({ profile, target, alias: aliasInput.value.trim() }) });
        await Promise.all([loadDashboard(), loadRemoteState()]);
        setStatus(`Saved alias for ${target}.`);
      } catch (error) {
        setStatus(error.message, 'error');
      }
    }

    async function saveTemplate() {
      const name = templateNameInput.value.trim();
      const command = commandInput.value.trim();
      if (!name || !command) {
        setStatus('Template name and command are required.', 'error');
        return;
      }
      const profile = templateScopeSelect.value === 'current' ? currentProfileName() : '';
      try {
        await api('/api/templates/save', { method: 'POST', body: JSON.stringify({ id: templateSelect.value, name, command, profile, target: paneSelect.value.trim() }) });
        await loadTemplates();
        setStatus(`Saved template ${name}.`);
      } catch (error) {
        setStatus(error.message, 'error');
      }
    }

    async function deleteTemplate() {
      const id = templateSelect.value.trim();
      if (!id) {
        setStatus('Choose a template first.', 'error');
        return;
      }
      try {
        await api('/api/templates/delete', { method: 'POST', body: JSON.stringify({ id }) });
        templateNameInput.value = '';
        await loadTemplates();
        setStatus('Template deleted.');
      } catch (error) {
        setStatus(error.message, 'error');
      }
    }

    function applyTemplate() {
      const template = templatesCache.find((item) => item.id === templateSelect.value);
      if (!template) {
        setStatus('Choose a template first.', 'error');
        return;
      }
      templateNameInput.value = template.name || '';
      commandInput.value = template.command || '';
      templateScopeSelect.value = template.profile ? 'current' : '';
      setStatus(`Applied template ${template.name}.`);
    }

    function applyHistory() {
      const entry = historyCache.find((item) => item.id === historySelect.value);
      if (!entry) {
        setStatus('Choose a history item first.', 'error');
        return;
      }
      commandInput.value = entry.command || '';
      setStatus('Applied recent command.');
    }

    async function clearHistory() {
      try {
        await api('/api/history/clear', { method: 'POST', body: JSON.stringify({ profile: currentProfileName() }) });
        await loadHistory();
        setStatus('History cleared for current target.');
      } catch (error) {
        setStatus(error.message, 'error');
      }
    }

    async function createTodo() {
      const selected = requireCurrentAgent('publishing a todo');
      if (!selected) return;
      const title = todoTitleInput.value.trim();
      if (!title) {
        setStatus('Todo title is required.', 'error');
        return;
      }
      const pane = selectedPaneData();
      try {
        const response = await api('/api/todos', {
          method: 'POST',
          body: JSON.stringify({
            title,
            detail: todoDetailInput.value.trim(),
            profile: selected.profile,
            target: selected.target,
            alias: (pane && pane.alias) || '',
            status: 'todo',
            priority: todoPrioritySelect.value,
            assignee: todoAssigneeInput.value.trim(),
          }),
        });
        await loadTodos();
        todoSelect.value = response.todo.id;
        syncTodoInspector();
        await loadDashboard();
        setStatus(`Published todo to ${selected.target}.`);
      } catch (error) {
        setStatus(error.message, 'error');
      }
    }

    async function quickTodo() {
      const selected = requireCurrentAgent('creating quick task');
      if (!selected) return;
      const pane = selectedPaneData();
      const fallbackTitle = commandInput.value.trim().split('\n')[0] || `Quick task for ${selected.target}`;
      const title = (todoTitleInput.value.trim() || fallbackTitle).slice(0, 140);
      try {
        await api('/api/todos/quick', {
          method: 'POST',
          body: JSON.stringify({
            title,
            detail: todoDetailInput.value.trim(),
            profile: selected.profile,
            target: selected.target,
            alias: (pane && pane.alias) || '',
            priority: todoPrioritySelect.value,
            assignee: todoAssigneeInput.value.trim(),
          }),
        });
        await loadTodos();
        await loadDashboard();
        setStatus(`Quick task created for ${selected.target}.`);
      } catch (error) {
        setStatus(error.message, 'error');
      }
    }

    async function createTripletWorkflow() {
      const selected = requireCurrentAgent('creating triplet workflow');
      if (!selected) return;
      const title = todoTitleInput.value.trim();
      if (!title) {
        setStatus('Todo title is required for triplet workflow.', 'error');
        return;
      }
      const detail = todoDetailInput.value.trim();
      const handoffPacket = {
        context: detail || title,
        constraints: 'Keep changes minimal, do not break existing behavior.',
        acceptance: 'All relevant tests pass and summary is provided.',
        rollback: 'If blocked, stop and provide rollback-safe patch plan.',
      };
      try {
        const response = await api('/api/workflows/triplet', {
          method: 'POST',
          body: JSON.stringify({
            title,
            detail,
            profile: selected.profile,
            target: selected.target,
            planner_target: selected.target,
            executor_target: selected.target,
            reviewer_target: selected.target,
            priority: todoPrioritySelect.value,
            handoff_packet: handoffPacket,
          }),
        });
        await loadTodos();
        await loadDashboard();
        setStatus(`Triplet workflow created: ${response.workflow_id}.`);
      } catch (error) {
        setStatus(error.message, 'error');
      }
    }

    async function updateTodoStatus() {
      const todo = selectedTodo();
      if (!todo) {
        setStatus('Choose a todo first.', 'error');
        return;
      }
      try {
        await api('/api/todos/status', {
          method: 'POST',
          body: JSON.stringify({
            todo_id: todo.id,
            status: todoStatusSelect.value,
            progress_note: todoProgressNoteInput.value.trim(),
            actor: 'mobile-user',
          }),
        });
        await loadTodos();
        await loadDashboard();
        setStatus(`Updated todo status to ${todoStatusSelect.value}.`);
      } catch (error) {
        setStatus(error.message, 'error');
      }
    }

    async function addTodoEvidence() {
      const todo = selectedTodo();
      if (!todo) {
        setStatus('Choose a todo first.', 'error');
        return;
      }
      const evidence = parseEvidenceInput(todoEvidenceInput.value);
      if (!evidence) {
        setStatus('Evidence text or JSON is required.', 'error');
        return;
      }
      try {
        await api('/api/todos/evidence', {
          method: 'POST',
          body: JSON.stringify({
            todo_id: todo.id,
            evidence,
            actor: 'mobile-user',
          }),
        });
        todoEvidenceInput.value = '';
        await loadTodos();
        await loadDashboard();
        setStatus('Todo evidence added.');
      } catch (error) {
        setStatus(error.message, 'error');
      }
    }

    async function reportTodo() {
      const todo = selectedTodo();
      if (!todo) {
        setStatus('Choose a todo first.', 'error');
        return;
      }
      const evidence = parseEvidenceInput(todoEvidenceInput.value);
      try {
        await api('/api/todos/report', {
          method: 'POST',
          body: JSON.stringify({
            todo_id: todo.id,
            status: todoStatusSelect.value,
            progress_note: todoProgressNoteInput.value.trim(),
            evidence: evidence || undefined,
            actor: 'agent',
          }),
        });
        todoEvidenceInput.value = '';
        await loadTodos();
        await loadDashboard();
        setStatus('Agent report applied to todo.');
      } catch (error) {
        setStatus(error.message, 'error');
      }
    }

    function applyTodoTemplate() {
      const template = todoTemplatesCache.find((item) => item.id === todoTemplateSelect.value);
      if (!template) {
        setStatus('Choose a todo template first.', 'error');
        return;
      }
      todoTemplateNameInput.value = template.name || '';
      todoTitleInput.value = template.title || '';
      todoDetailInput.value = template.detail || '';
      todoPrioritySelect.value = template.priority || 'medium';
      todoAssigneeInput.value = template.assignee || '';
      setStatus(`Applied todo template ${template.name}.`);
    }

    async function saveTodoTemplate() {
      const selected = requireCurrentAgent('saving todo template');
      if (!selected) return;
      const name = todoTemplateNameInput.value.trim();
      const title = todoTitleInput.value.trim();
      if (!name || !title) {
        setStatus('Template name and todo title are required.', 'error');
        return;
      }
      try {
        await api('/api/todo-templates/save', {
          method: 'POST',
          body: JSON.stringify({
            id: todoTemplateSelect.value,
            name,
            title,
            detail: todoDetailInput.value.trim(),
            priority: todoPrioritySelect.value,
            assignee: todoAssigneeInput.value.trim(),
            profile: selected.profile,
            target: selected.target,
          }),
        });
        await loadTodoTemplates();
        await loadAuditLogs();
        setStatus(`Saved todo template ${name}.`);
      } catch (error) {
        setStatus(error.message, 'error');
      }
    }

    async function deleteTodoTemplate() {
      const id = todoTemplateSelect.value.trim();
      if (!id) {
        setStatus('Choose a todo template first.', 'error');
        return;
      }
      try {
        await api('/api/todo-templates/delete', { method: 'POST', body: JSON.stringify({ id }) });
        await loadTodoTemplates();
        await loadAuditLogs();
        setStatus('Todo template deleted.');
      } catch (error) {
        setStatus(error.message, 'error');
      }
    }

    function applyTodoToCommand() {
      const todo = selectedTodo();
      if (!todo) {
        setStatus('Choose a todo first.', 'error');
        return;
      }
      const detail = todo.detail ? `\n\nDetails:\n${todo.detail}` : '';
      commandInput.value = `TODO ${todo.id}: ${todo.title}${detail}`;
      setStatus('Todo content copied into command box.');
    }

    async function sendCommand() {
      const profile = currentProfileName();
      const target = paneSelect.value.trim();
      const command = commandInput.value.trim();
      if (!profile || !target) {
        setStatus('Choose a target and pane first.', 'error');
        return;
      }
      if (!command) {
        setStatus('Enter a command first.', 'error');
        return;
      }
      try {
        await api('/api/send', {
          method: 'POST',
          body: JSON.stringify({ profile, target, command, press_enter: true, expected_target: target }),
        });
        await Promise.all([loadHistory(), loadPane()]);
        setStatus(`Sent command to ${target}.`);
      } catch (error) {
        if (String(error.message || '').includes('confirm_risk=true')) {
          const ok = window.confirm('This command looks dangerous. Send anyway?');
          if (ok) {
            try {
              await api('/api/send', {
                method: 'POST',
                body: JSON.stringify({ profile, target, command, press_enter: true, expected_target: target, confirm_risk: true }),
              });
              await Promise.all([loadHistory(), loadPane()]);
              setStatus(`Sent command to ${target} with risk confirmation.`, 'warn');
              return;
            } catch (retryError) {
              setStatus(retryError.message, 'error');
              return;
            }
          }
          setStatus('Cancelled risky command.', 'warn');
          return;
        }
        setStatus(error.message, 'error');
      }
    }

    async function interrupt() {
      const profile = currentProfileName();
      const target = paneSelect.value.trim();
      if (!profile || !target) {
        setStatus('Choose a target and pane first.', 'error');
        return;
      }
      try {
        await api('/api/interrupt', { method: 'POST', body: JSON.stringify({ profile, target }) });
        await loadPane();
        setStatus(`Sent Ctrl+C to ${target}.`);
      } catch (error) {
        setStatus(error.message, 'error');
      }
    }

    function appendNewline() {
      const value = commandInput.value;
      commandInput.value = value.endsWith('\n') ? value : `${value}\n`;
      commandInput.focus();
    }

    async function copyTargetLabel() {
      try {
        await navigator.clipboard.writeText(currentTargetLabel());
        setStatus('Copied selected target label.');
      } catch (error) {
        setStatus('Clipboard is unavailable in this browser.', 'warn');
      }
    }

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    let recognition = null;
    if (SpeechRecognition) {
      recognition = new SpeechRecognition();
      recognition.continuous = true;
      recognition.interimResults = true;
      recognition.lang = navigator.language || 'en-US';
      recognition.onresult = (event) => {
        let transcript = '';
        for (let index = event.resultIndex; index < event.results.length; index += 1) {
          transcript += event.results[index][0].transcript;
        }
        commandInput.value = transcript.trim();
        setStatus('Listening… local speech-to-text is updating the command box.');
      };
      recognition.onerror = (event) => {
        setStatus(`Voice input error: ${event.error}`, 'error');
      };
    } else {
      setStatus('Voice input is unavailable in this browser. Use Chrome-based browsers or type commands manually.', 'warn');
    }

    document.getElementById('refreshDashboard').addEventListener('click', refreshAll);
    document.getElementById('refreshState').addEventListener('click', loadSelectedProfile);
    document.getElementById('saveProfile').addEventListener('click', saveProfile);
    document.getElementById('testProfile').addEventListener('click', testProfile);
    document.getElementById('loadProfileState').addEventListener('click', loadSelectedProfile);
    document.getElementById('deleteProfile').addEventListener('click', deleteProfile);
    document.getElementById('saveAlias').addEventListener('click', saveAlias);
    document.getElementById('saveTemplate').addEventListener('click', saveTemplate);
    document.getElementById('deleteTemplate').addEventListener('click', deleteTemplate);
    document.getElementById('applyTemplate').addEventListener('click', applyTemplate);
    document.getElementById('applyHistory').addEventListener('click', applyHistory);
    document.getElementById('clearHistory').addEventListener('click', clearHistory);
    document.getElementById('createTodo').addEventListener('click', createTodo);
    document.getElementById('quickTodo').addEventListener('click', quickTodo);
    document.getElementById('createTriplet').addEventListener('click', createTripletWorkflow);
    document.getElementById('refreshTodos').addEventListener('click', loadTodos);
    document.getElementById('applyTodoToCommand').addEventListener('click', applyTodoToCommand);
    document.getElementById('updateTodoStatus').addEventListener('click', updateTodoStatus);
    document.getElementById('addTodoEvidence').addEventListener('click', addTodoEvidence);
    document.getElementById('reportTodo').addEventListener('click', reportTodo);
    document.getElementById('applyTodoTemplate').addEventListener('click', applyTodoTemplate);
    document.getElementById('saveTodoTemplate').addEventListener('click', saveTodoTemplate);
    document.getElementById('deleteTodoTemplate').addEventListener('click', deleteTodoTemplate);
    document.getElementById('sendCommand').addEventListener('click', sendCommand);
    document.getElementById('interrupt').addEventListener('click', interrupt);
    document.getElementById('appendNewline').addEventListener('click', appendNewline);
    document.getElementById('copyTargetLabel').addEventListener('click', copyTargetLabel);
    document.getElementById('refreshPane').addEventListener('click', loadPane);
    document.getElementById('startVoice').addEventListener('click', () => {
      if (!recognition) {
        setStatus('Voice input is unavailable in this browser.', 'error');
        return;
      }
      recognition.start();
      setStatus('Voice capture started.');
    });
    document.getElementById('stopVoice').addEventListener('click', () => {
      if (!recognition) return;
      recognition.stop();
      setStatus('Voice capture stopped.');
    });

    tokenInput.addEventListener('change', refreshAll);
    profileSelect.addEventListener('change', loadSelectedProfile);
    sessionSelect.addEventListener('change', () => { renderWindows(); loadPane(); loadTodos(); });
    windowSelect.addEventListener('change', () => { renderPanes(); loadPane(); loadTodos(); });
    paneSelect.addEventListener('change', () => { syncAliasInput(); loadPane(); loadTodos(); });
    templateSelect.addEventListener('change', () => {
      const template = templatesCache.find((item) => item.id === templateSelect.value);
      templateNameInput.value = template ? template.name : '';
      templateScopeSelect.value = template && template.profile ? 'current' : '';
    });
    todoSelect.addEventListener('change', syncTodoInspector);
    todoTemplateSelect.addEventListener('change', () => {
      const template = todoTemplatesCache.find((item) => item.id === todoTemplateSelect.value);
      todoTemplateNameInput.value = template ? template.name : '';
    });

    refreshAll();
    setInterval(() => {
      if (currentProfileName()) {
        loadPane().catch(() => {});
      }
    }, 5000);
    setInterval(() => {
      // SSE handles near-real-time todo updates; this is a fallback refresh.
      if (currentProfileName() && paneSelect.value.trim()) {
        loadTodos().catch(() => {});
      }
    }, 45000);
    setInterval(() => {
      loadDashboard().catch(() => {});
    }, 20000);
  </script>
</body>
</html>
"""
