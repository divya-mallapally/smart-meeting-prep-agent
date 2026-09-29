import streamlit as st

st.set_page_config(
    page_title="Smart Meeting Prep Agent",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="expanded",
)

CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #1e293b;
    }
    .stApp { background-color: #f8fafc; }
    .sidebar-brand {
        display: flex; align-items: center; gap: 12px;
        padding: 10px 0 20px 0; border-bottom: 1px solid #e2e8f0; margin-bottom: 20px;
    }
    .brand-icon {
        background: #4f46e5; color: white; padding: 8px 10px;
        border-radius: 10px; font-size: 1.15rem;
    }
    .brand-title {
        font-weight: 700; font-size: 0.95rem; line-height: 1.2; color: #1e1b4b;
    }
    .profile-pill {
        display: flex; align-items: center; justify-content: space-between;
        padding: 8px 12px; background: #ffffff; border: 1px solid #e2e8f0;
        border-radius: 12px; margin-top: 30px;
    }
    .avatar-bubble {
        width: 32px; height: 32px; border-radius: 50%;
        background: #4f46e5; color: white; font-size: 13px;
        font-weight: 600; display: flex; align-items: center; justify-content: center;
    }
    .card-container {
        background: #ffffff; border-radius: 16px; border: 1px solid #e2e8f0;
        padding: 24px; box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05); margin-bottom: 18px;
    }
    .template-card {
        background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px;
        padding: 18px; transition: all 0.2s ease-in-out; height: 100%;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .template-card:hover {
        border-color: #6366f1; box-shadow: 0 4px 12px rgba(99, 102, 241, 0.08);
    }
    .start-meeting-banner {
        background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%);
        border-radius: 16px; padding: 30px; color: white; text-align: center;
        margin-bottom: 24px; box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.25);
    }
    .stepper-wrap {
        display: flex; align-items: center; justify-content: center;
        gap: 20px; margin-bottom: 28px;
    }
    .step-node {
        display: flex; flex-direction: column; align-items: center; gap: 6px;
        font-size: 12px; font-weight: 600;
    }
    .step-circle {
        width: 28px; height: 28px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 12px; font-weight: 700;
    }
    .step-active { background: #4f46e5; color: #ffffff; }
    .step-inactive { background: #f1f5f9; color: #94a3b8; }
    .step-completed { background: #e0e7ff; color: #4f46e5; }
    .stepper-line { height: 2px; width: 60px; background: #e2e8f0; margin-bottom: 18px; }
    .meeting-row {
        background: #ffffff; border: 1px solid #f1f5f9; border-radius: 12px;
        padding: 14px 18px; display: flex; align-items: center;
        justify-content: space-between; margin-bottom: 10px;
    }
    .meeting-badge-completed {
        background-color: #ecfdf5; color: #059669; font-size: 11px;
        font-weight: 600; padding: 4px 10px; border-radius: 9999px;
    }
    .file-item {
        background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px;
        padding: 10px 14px; display: flex; align-items: center;
        justify-content: space-between; margin-bottom: 8px; font-size: 13px;
    }
    .stButton > button {
        border-radius: 10px !important; font-weight: 600 !important;
        border: none !important; padding: 0.5rem 1.25rem !important;
    }
    .stButton > button[kind="primary"] {
        background: #4f46e5 !important; color: #ffffff !important;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --- Session Defaults ---
if "current_screen" not in st.session_state:
    st.session_state.current_screen = "Dashboard"

if "new_meeting" not in st.session_state:
    st.session_state.new_meeting = {
        "title": "Project Update Meeting",
        "date": "2026-09-20",
        "time": "10:00 AM",
        "participants": "Product Team, Manager, Client",
        "objective": "Discuss project progress, next steps...",
    }

if "app_settings" not in st.session_state:
    st.session_state.app_settings = {
        "api_key": "",
        "model_name": "gemini-1.5-flash",
        "default_platform": "Google Meet",
        "auto_extract_actions": True,
        "email_notifications": True,
    }

def set_screen(screen_name):
    st.session_state.current_screen = screen_name
    st.rerun()

def render_sidebar():
    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-brand">
                <div class="brand-icon">📅</div>
                <div class="brand-title">Smart Meeting<br><span style="color:#64748b; font-weight:500;">Prep Agent</span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption("NAVIGATION")
        if st.button("🏠  Home", use_container_width=True):
            set_screen("Dashboard")
        if st.button("📁  My Meetings", use_container_width=True):
            set_screen("History")
        if st.button("📋  Templates", use_container_width=True):
            set_screen("Templates")
        if st.button("⚙️  Settings", use_container_width=True):
            set_screen("Settings")

        st.markdown("<div style='height: 160px;'></div>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="profile-pill">
                <div style="display:flex; align-items:center; gap: 10px;">
                    <div class="avatar-bubble">D</div>
                    <span style="font-size: 13px; font-weight: 600; color: #1e293b;">Divya</span>
                </div>
                <span style="color: #94a3b8; font-size: 14px;">›</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ==============================================================================
# SCREEN: Templates
# ==============================================================================
def screen_templates():
    if st.button("← Back to Dashboard"):
        set_screen("Dashboard")

    st.markdown(
        """
        <div style="margin-bottom: 20px;">
            <h2 style="font-weight: 700; margin:0; color:#0f172a;">Meeting Templates</h2>
            <p style="color: #64748b; font-size: 14px;">Select a ready-to-use template to jumpstart your meeting preparation.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    templates = [
        {
            "icon": "🚀",
            "title": "Client Proposal Review",
            "desc": "Pitching proposals, covering deliverables, budget timelines, and Q&A points.",
            "parts": "Client Executive, Sales Lead, Solutions Architect",
            "obj": "Align on project milestones, scope boundaries, and pricing approvals.",
        },
        {
            "icon": "⚡",
            "title": "Sprint Planning & Sync",
            "desc": "Review blockers, prioritize backlog tickets, and assign sprint owners.",
            "parts": "Scrum Master, Frontend Devs, Backend Devs, QA Lead",
            "obj": "Establish commit items for the upcoming two-week iteration cycle.",
        },
        {
            "icon": "👥",
            "title": "1-on-1 Feedback & Growth",
            "desc": "Bi-weekly sync to review recent achievements, feedback, and career goals.",
            "parts": "Manager, Team Member",
            "obj": "Discuss progress, personal blockers, growth opportunities, and well-being.",
        },
        {
            "icon": "📊",
            "title": "Product Demo & Walkthrough",
            "desc": "Demonstrate newly developed feature sets and capture live stakeholder feedback.",
            "parts": "Product Manager, UI/UX Designer, Key Stakeholders",
            "obj": "Walk through release-candidate screens and document revisions.",
        },
    ]

    cols = st.columns(2)
    for i, t in enumerate(templates):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="template-card">
                    <div>
                        <div style="font-size: 26px; margin-bottom: 8px;">{t['icon']}</div>
                        <h4 style="margin: 0 0 6px 0; font-weight: 700; color: #0f172a;">{t['title']}</h4>
                        <p style="font-size: 13px; color: #64748b; line-height: 1.5;">{t['desc']}</p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown("<div style='height: 4px;'></div>", unsafe_allow_html=True)
            if st.button(f"Use '{t['title']}'", key=f"tpl_btn_{i}", use_container_width=True):
                st.session_state.new_meeting["title"] = t["title"]
                st.session_state.new_meeting["participants"] = t["parts"]
                st.session_state.new_meeting["objective"] = t["obj"]
                st.toast(f"Loaded '{t['title']}' template!")
                set_screen("Meeting_Details")
            st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

# ==============================================================================
# SCREEN: Settings
# ==============================================================================
def screen_settings():
    if st.button("← Back to Dashboard"):
        set_screen("Dashboard")

    st.markdown(
        """
        <div style="margin-bottom: 20px;">
            <h2 style="font-weight: 700; margin:0; color:#0f172a;">Application Settings</h2>
            <p style="color: #64748b; font-size: 14px;">Manage your AI model configurations, integrations, and preferences.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    t_ai, t_int, t_pref = st.tabs(["🤖 AI Model & Keys", "🔗 Integrations", "⚙️ Preferences"])

    with t_ai:
        st.markdown("<div class='card-container'>", unsafe_allow_html=True)
        st.markdown("<h4 style='font-weight: 700;'>Gemini AI Configuration</h4>", unsafe_allow_html=True)

        api_input = st.text_input(
            "Gemini API Key",
            type="password",
            value=st.session_state.app_settings["api_key"],
            help="Stored securely in your current session. Never shared.",
            placeholder="AIzaSy...",
        )
        model_choice = st.selectbox(
            "Default Generation Model",
            ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.5-flash"],
            index=["gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.5-flash"].index(st.session_state.app_settings["model_name"]),
        )

        col1, col2 = st.columns(2)
        with col1:
            st.slider("Summary Creativity (Temperature)", min_value=0.0, max_value=1.0, value=0.2, step=0.1)
        with col2:
            st.slider("Max Question Suggestions", min_value=3, max_value=10, value=5, step=1)

        if st.button("Save AI Settings", type="primary"):
            st.session_state.app_settings["api_key"] = api_input
            st.session_state.app_settings["model_name"] = model_choice
            st.success("AI settings updated successfully!")
        st.markdown("</div>", unsafe_allow_html=True)

    with t_int:
        st.markdown("<div class='card-container'>", unsafe_allow_html=True)
        st.markdown("<h4 style='font-weight: 700;'>Meeting & Calendar Integrations</h4>", unsafe_allow_html=True)

        platform = st.selectbox(
            "Default Video Call Provider",
            ["Google Meet", "Zoom", "Microsoft Teams"],
            index=["Google Meet", "Zoom", "Microsoft Teams"].index(st.session_state.app_settings["default_platform"]),
        )

        st.checkbox("Google Calendar Sync", value=True, help="Automatically import scheduled events.")
        st.checkbox("Export Action Items to Notion / Jira", value=True)

        if st.button("Save Integrations"):
            st.session_state.app_settings["default_platform"] = platform
            st.success("Integrations saved!")
        st.markdown("</div>", unsafe_allow_html=True)

    with t_pref:
        st.markdown("<div class='card-container'>", unsafe_allow_html=True)
        st.markdown("<h4 style='font-weight: 700;'>User Experience</h4>", unsafe_allow_html=True)

        auto_act = st.toggle("Automatically extract action items from attachments", value=st.session_state.app_settings["auto_extract_actions"])
        email_notif = st.toggle("Email meeting prep summaries 1 hour prior", value=st.session_state.app_settings["email_notifications"])

        if st.button("Save Preferences"):
            st.session_state.app_settings["auto_extract_actions"] = auto_act
            st.session_state.app_settings["email_notifications"] = email_notif
            st.success("Preferences updated!")
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# SCREEN: Dashboard
# ==============================================================================
def screen_dashboard():
    st.markdown(
        """
        <div style="margin-bottom: 24px;">
            <h2 style="font-weight: 700; margin:0; color:#0f172a;">Good Morning, Divya! 👋</h2>
            <p style="color: #64748b; font-size: 14px; margin-top:4px;">Prepare smarter. Make better meetings.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col_a, _ = st.columns([1.8, 1])
    with col_a:
        st.markdown(
            """
            <div class="start-meeting-banner">
                <div style="background: rgba(255,255,255,0.2); width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 12px auto; font-size: 20px;">＋</div>
                <div style="font-size: 18px; font-weight: 700;">Start New Meeting</div>
                <div style="font-size: 13px; opacity: 0.9; margin-top: 4px;">Add meeting details, upload documents and let AI do the rest.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        c_btn1, c_btn2 = st.columns(2)
        with c_btn1:
            if st.button("🚀 Prepare New Meeting Now", type="primary", use_container_width=True):
                set_screen("Meeting_Details")
        with c_btn2:
            if st.button("📋 Use a Template", use_container_width=True):
                set_screen("Templates")

    st.markdown("<h4 style='font-weight:700; color:#0f172a; margin: 24px 0 12px 0;'>Recent Meetings</h4>", unsafe_allow_html=True)
    meetings = [
        {"title": "Project Update Meeting", "date": "Sep 20, 2026 • 10:00 AM", "url": "https://meet.google.com/new"},
        {"title": "Client Proposal Review", "date": "Sep 18, 2026 • 2:00 PM", "url": "https://meet.google.com/new"},
        {"title": "Team Sync", "date": "Sep 16, 2026 • 11:00 AM", "url": "https://meet.google.com/new"},
    ]
    for m in meetings:
        col_m1, col_m2, col_m3 = st.columns([3.5, 1, 1])
        with col_m1:
            st.markdown(
                f"""
                <div class="meeting-row">
                    <div style="display:flex; align-items:center; gap: 14px;">
                        <span style="font-size: 18px;">📅</span>
                        <div>
                            <div style="font-weight: 600; font-size: 14px; color: #0f172a;">{m['title']}</div>
                            <div style="color: #64748b; font-size: 12px;">{m['date']}</div>
                        </div>
                    </div>
                    <div><span class="meeting-badge-completed">Completed</span></div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col_m2:
            st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
            if st.button("Open Guide", key=f"btn_{m['title']}", use_container_width=True):
                set_screen("Results")
        with col_m3:
            st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
            st.link_button("🎥 Join", m["url"], use_container_width=True)

# ==============================================================================
# SCREEN: Meeting Details (Wizard Step 1)
# ==============================================================================
def screen_meeting_details():
    if st.button("← Back to Dashboard"):
        set_screen("Dashboard")

    st.markdown("<h3 style='font-weight:700;'>New Meeting</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="stepper-wrap">
            <div class="step-node"><div class="step-circle step-active">1</div><span>Details</span></div>
            <div class="stepper-line"></div>
            <div class="step-node"><div class="step-circle step-inactive">2</div><span style="color:#94a3b8;">Documents</span></div>
            <div class="stepper-line"></div>
            <div class="step-node"><div class="step-circle step-inactive">3</div><span style="color:#94a3b8;">Generate</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='card-container'>", unsafe_allow_html=True)
    st.markdown("<h4 style='font-weight:600; margin-top:0;'>Meeting Details</h4>", unsafe_allow_html=True)
    st.session_state.new_meeting["title"] = st.text_input("Meeting Name *", value=st.session_state.new_meeting["title"])
    c1, c2 = st.columns(2)
    with c1:
        st.session_state.new_meeting["date"] = st.text_input("Date *", value=st.session_state.new_meeting["date"])
    with c2:
        st.session_state.new_meeting["time"] = st.text_input("Time *", value=st.session_state.new_meeting["time"])
    st.session_state.new_meeting["participants"] = st.text_input("Participants", value=st.session_state.new_meeting["participants"])
    st.session_state.new_meeting["objective"] = st.text_area("Meeting Objective", value=st.session_state.new_meeting["objective"])

    col_l, col_r = st.columns([4, 1])
    with col_r:
        if st.button("Next →", type="primary", use_container_width=True):
            set_screen("Upload_Docs")
    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# SCREEN: Upload Documents (Wizard Step 2)
# ==============================================================================
def screen_upload_documents():
    if st.button("← Back to Details"):
        set_screen("Meeting_Details")

    st.markdown("<h3 style='font-weight:700;'>New Meeting</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="stepper-wrap">
            <div class="step-node"><div class="step-circle step-completed">✓</div><span>Details</span></div>
            <div class="stepper-line"></div>
            <div class="step-node"><div class="step-circle step-active">2</div><span>Documents</span></div>
            <div class="stepper-line"></div>
            <div class="step-node"><div class="step-circle step-inactive">3</div><span style="color:#94a3b8;">Generate</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='card-container'>", unsafe_allow_html=True)
    st.markdown("<h4 style='font-weight:600; margin-top:0;'>Upload Documents</h4>", unsafe_allow_html=True)
    st.file_uploader("Drag & drop files here", accept_multiple_files=True)
    
    st.markdown("<h5 style='font-weight:600; margin: 18px 0 10px 0;'>Uploaded Files</h5>", unsafe_allow_html=True)
    files = [("📄", "Project_Overview.pdf", "2.4 MB"), ("📝", "Meeting_Notes.docx", "1.2 MB"), ("📊", "Requirements.pdf", "3.1 MB")]
    for icon, name, size in files:
        st.markdown(f"<div class='file-item'><div>{icon} {name}</div><div style='color:#64748b;'>{size} ✕</div></div>", unsafe_allow_html=True)

    col_l, col_r = st.columns([4, 1])
    with col_r:
        if st.button("Generate Prep →", type="primary", use_container_width=True):
            set_screen("Processing")
    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# SCREEN: Processing (Wizard Step 3)
# ==============================================================================
def screen_processing():
    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown(
            """
            <div style="text-align: center; padding-top: 30px;">
                <h3 style="font-weight: 700;">Processing Your Meeting...</h3>
                <p style="color: #64748b; font-size: 14px;">Our AI is analyzing your documents and preparing your personalized meeting guide.</p>
                <div style="font-size: 60px; margin: 20px 0;">🤖</div>
                <h2 style="font-weight: 700; color: #4f46e5;">72%</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.progress(0.72)
        if st.button("Complete Processing (Demo)", type="primary", use_container_width=True):
            set_screen("Results")

# ==============================================================================
# SCREEN: Results
# ==============================================================================
def screen_results():
    if st.button("← Back to Dashboard"):
        set_screen("Dashboard")

    st.markdown("<h3 style='font-weight:700;'>Meeting Preparation</h3>", unsafe_allow_html=True)
    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Questions", "Action Items", "Insights"])

    with tab1:
        st.markdown("<div class='card-container'>", unsafe_allow_html=True)
        col_h, col_b = st.columns([3, 1])
        with col_h:
            st.markdown("<h4 style='font-weight:700; margin:0;'>Meeting Summary</h4>", unsafe_allow_html=True)
        with col_b:
            if st.button("📋 Copy Summary", key="btn_cp_sum"):
                st.toast("Copied!")
        st.markdown(
            f"""
            <p style="color: #475569; font-size: 14px; line-height: 1.6; margin-top: 10px;">
                Summary for <b>{st.session_state.new_meeting['title']}</b>: Review of progress, timeline targets,
                and milestone requirements. Objective: {st.session_state.new_meeting['objective']}
            </p>
            <h5 style="font-weight: 700;">Key Points</h5>
            <ul style="color: #475569; font-size: 14px; line-height: 1.8;">
                <li>Model accuracy improved to 92%</li>
                <li>Dataset collection is 80% complete</li>
                <li>Deployment planned for next month</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("<div class='card-container'>", unsafe_allow_html=True)
        col_h, col_b = st.columns([3, 1])
        with col_h:
            st.markdown("<h4 style='font-weight:700; margin:0;'>💡 Suggested Questions</h4>", unsafe_allow_html=True)
        with col_b:
            if st.button("📋 Copy All Questions", key="btn_cp_q"):
                st.toast("Questions copied!")

        for q in [
            "1. What are the next steps for the deployment process?",
            "2. Are there any additional data requirements from the client?",
            "3. What are the expected timelines for the UI changes?",
        ]:
            st.markdown(f"<div style='padding: 8px 0; border-bottom: 1px solid #f1f5f9; font-size: 14px;'>{q}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab3:
        st.info("Sync active with Jira & Notion.")

    with tab4:
        st.info("Sentiment score: 88% positive.")

# ==============================================================================
# SCREEN: History
# ==============================================================================
def screen_history():
    st.markdown("<h3 style='font-weight:700;'>My Meetings</h3>", unsafe_allow_html=True)
    meetings = [
        {"title": "Project Update Meeting", "date": "Sep 20, 2026 • 10:00 AM"},
        {"title": "Client Proposal Review", "date": "Sep 18, 2026 • 2:00 PM"},
        {"title": "Team Sync", "date": "Sep 16, 2026 • 11:00 AM"},
    ]
    for m in meetings:
        col_m1, col_m2 = st.columns([4, 1])
        with col_m1:
            st.markdown(
                f"""
                <div class="meeting-row">
                    <div style="display:flex; align-items:center; gap: 14px;">
                        <span style="font-size: 18px;">📅</span>
                        <div>
                            <div style="font-weight: 600; font-size: 14px; color: #0f172a;">{m['title']}</div>
                            <div style="color: #64748b; font-size: 12px;">{m['date']}</div>
                        </div>
                    </div>
                    <div><span class="meeting-badge-completed">Completed</span></div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col_m2:
            st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
            if st.button("View Guide", key=f"hist_view_{m['title']}", use_container_width=True):
                set_screen("Results")

# ==============================================================================
# ROUTER
# ==============================================================================
with st.expander("🛠️ Screen Switcher", expanded=False):
    screens = ["Dashboard", "Templates", "Settings", "Meeting_Details", "Upload_Docs", "Processing", "Results", "History"]
    selected_screen = st.selectbox(
        "Jump to Screen:",
        screens,
        index=screens.index(st.session_state.current_screen) if st.session_state.current_screen in screens else 0
    )
    if st.button("Navigate"):
        set_screen(selected_screen)

render_sidebar()

if st.session_state.current_screen == "Dashboard":
    screen_dashboard()
elif st.session_state.current_screen == "Templates":
    screen_templates()
elif st.session_state.current_screen == "Settings":
    screen_settings()
elif st.session_state.current_screen == "Meeting_Details":
    screen_meeting_details()
elif st.session_state.current_screen == "Upload_Docs":
    screen_upload_documents()
elif st.session_state.current_screen == "Processing":
    screen_processing()
elif st.session_state.current_screen == "Results":
    screen_results()
elif st.session_state.current_screen == "History":
    screen_history()