import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import html
from pathlib import Path

load_dotenv()

st.set_page_config(
    page_title="OnboardAI - Nova",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------  GLOBAL CSS  --------------------
st.markdown("""
<style>
    * { font-family: 'Arial', sans-serif; }

    body {
        background-color: #F2F6FF;
    }

    .stApp {
        background: #F2F6FF;
    }

    /* Header */
    .welcome-header {
        background: #0A1A33;
        color: #FFFFFF;
        padding: 3rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
    }

    /* Welcome Box */
    .welcome-box {
        background: #E8EEFF;
        padding: 1.8rem;
        border-radius: 15px;
        border: 2px solid #1F75FE;
        margin-bottom: 2rem;
        color: #0A1A33;
    }

    /* Chat Header */
    .chat-header {
        background: linear-gradient(135deg, #87CEEB, #B0E0E6);
        padding: 1rem;
        border-radius: 15px;
        color: #0A1A33;
        text-align: center;
        margin-bottom: 1rem;
        border: 2px solid #87CEEB;
    }

    /* Chat Bubbles */
    .chat-message {
        padding: 1rem;
        border-radius: 15px;
        margin: 0.7rem 0;
        max-width: 75%;
        font-size: 1.05rem;
        line-height: 1.45rem;
    }

    .user-message {
        background: #1F3C88;
        color: white;
        margin-left: auto;
    }

    .bot-message {
        background: #E8EEFF;
        color: #0A1A33;
        border: 1px solid #1F75FE;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #1F75FE, #559AFE);
        color: #FFFFFF;
        border: none;
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        font-size: 1rem;
    }
    .stButton > button:hover {
        background: #0A57D0;
        color: white;
    }

    /* Custom Button Colors */
    .green-button .stButton > button {
        background: linear-gradient(90deg, #28a745, #20c997) !important;
        color: white !important;
        border: none !important;
    }
    .green-button .stButton > button:hover {
        background: #1e7e34 !important;
        color: white !important;
    }

    .red-button .stButton > button {
        background: linear-gradient(90deg, #dc3545, #e74c3c) !important;
        color: white !important;
        border: none !important;
    }
    .red-button .stButton > button:hover {
        background: #c82333 !important;
        color: white !important;
    }

    /* Document Boxes */
    .doc-box {
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        border: 2px solid #1F75FE;
        font-weight: 600;
        text-align: left;
        color: #0A1A33;
        min-height: 120px;
        display: flex;
        align-items: center;
        font-size: 1.1rem;
    }

    .doc-blue   { background: #E8EEFF; }
    .doc-green  { background: #DFF7E8; }
    .doc-yellow { background: #FFF6D9; }
    .doc-red    { background: #FFE5E5; }
    .doc-grey   { background: #F4F6F8; }

</style>
""", unsafe_allow_html=True)

# -------------------- SESSION STATE --------------------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "page" not in st.session_state:
    st.session_state.page = "chat"
if "preview_open" not in st.session_state:
    st.session_state.preview_open = None

# -------------------- AI MODEL --------------------
try:
    API_KEY = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY", ""))
    if not API_KEY:
        st.error("API key not found. Please configure GOOGLE_API_KEY.")
        st.stop()
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("models/gemini-2.5-flash-lite")
except Exception as e:
    st.error(f"Failed to initialize AI model: {str(e)}")
    st.stop()


# -------------------- LOAD DOCS --------------------
def load_document(filename):
    """Securely load document with path traversal protection."""
    ALLOWED_DOCUMENTS = {
        "allatone.txt", "benefits.txt", "payroll_faq.txt", "code_of_conduct.txt",
        "security_guidelines.txt", "leave_policy.txt", "travel_policy.txt",
        "reimbursement_policy.txt", "important_contacts.txt", "company_values.txt",
        "org_structure.txt", "tools_onboarding.txt", "work_policy.txt",
        "week1_checklist.txt", "week2_checklist.txt", "week3_checklist.txt", 
        "week4_checklist.txt", "it_setup.txt"
    }
    
    if not filename or filename not in ALLOWED_DOCUMENTS:
        return "Error: Invalid document requested."
    
    try:
        base_dir = Path("data").resolve()
        file_path = (base_dir / filename).resolve()
        
        if not str(file_path).startswith(str(base_dir)):
            return "Error: Invalid file path."
            
        with open(file_path, "r", encoding="utf-8") as file_handle:
            content = file_handle.read()
            if len(content) > 1000000:
                return "Error: Document too large."
            return content
            
    except FileNotFoundError:
        return "Error: Document not found."
    except PermissionError:
        return "Error: Access denied."
    except UnicodeDecodeError:
        return "Error: Invalid file encoding."
    except Exception as e:
        return f"Error: Could not load document - {type(e).__name__}"


def get_document_mapping():
    return {
        "benefits": "benefits.txt",
        "payroll": "payroll_faq.txt",
        "conduct": "code_of_conduct.txt",
        "security": "security_guidelines.txt",
        "leave": "leave_policy.txt",
        "travel": "travel_policy.txt",
        "expense": "reimbursement_policy.txt",
        "contact": "important_contacts.txt",
        "values": "company_values.txt",
        "organization": "org_structure.txt",
        "tools": "tools_onboarding.txt",
        "work policy": "work_policy.txt",
        "week 1": "week1_checklist.txt",
        "week 2": "week2_checklist.txt",
        "week 3": "week3_checklist.txt",
        "week 4": "week4_checklist.txt",
    }


def find_relevant_document(user_query):
    """Find relevant document with input validation."""
    if not user_query or not isinstance(user_query, str):
        return "allatone.txt"
    
    sanitized_query = user_query.lower().strip()[:500]
    document_mapping = get_document_mapping()
    
    for keyword, document_file in document_mapping.items():
        if keyword in sanitized_query:
            return document_file
    return "allatone.txt"


# -------------------- AI RESPONSE --------------------
def get_ai_response(user_query, context):
    """Generate AI response with input validation and rate limiting."""
    if not user_query or not isinstance(user_query, str) or len(user_query) > 1000:
        return "Please provide a valid question under 1000 characters."
    
    if not context or len(context) > 50000:
        return "Unable to process request due to context limitations."
    
    safe_query = html.escape(user_query.strip())
    safe_context = html.escape(context[:50000])
    
    prompt = f"""
You are Nova, an AI onboarding assistant for OnboardAI system.

SYSTEM NAVIGATION:
- Current page: Chat interface with Nova
- To access documents: Click "📁 Get Formal Documents" button above
- Document categories: Company Information, Policies & Guidelines, Benefits & Payroll, IT Setup & Tools, Weekly Checklists
- Each document has Download and Preview options

Use ONLY the context below:

CONTEXT:
{safe_context}

USER QUESTION:
{safe_query}

ANSWER RULES:
- Provide clear, structured information.
- Use bullet points where helpful.
- If user asks about documents/files, mention: "You can find all formal documents by clicking the '📁 Get Formal Documents' button above."
- Do NOT mention filenames.
- If you don't know, say: "I don't have that specific information in my knowledge base. Please contact HR."
"""

    try:
        response = model.generate_content(prompt)
        if response and hasattr(response, 'text') and response.text:
            return html.escape(response.text)
        else:
            return "I couldn't generate a response. Please try rephrasing your question."
    except Exception as api_error:
        error_type = type(api_error).__name__
        return f"Nova is experiencing technical issues ({error_type}). Please try again later."


# --------------------  CHAT PAGE  --------------------
if st.session_state.page == "chat":

    st.markdown("""
    <div class="welcome-header">
        <h1>🤖 OnboardAI – Nova</h1>
        <p>Your onboarding assistant</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="welcome-box">', unsafe_allow_html=True)
    st.markdown("## 👋 Welcome to OnboardAI!")
    st.markdown("**Meet Nova** - Your intelligent onboarding assistant powered by Google Gemini 2.5 Flash")
    st.markdown("### 🚀 What I Can Help You With:")
    st.markdown("""
    - **📋 Company Policies** - Code of conduct, work policies, security guidelines
    - **💰 Benefits & Payroll** - Health insurance, retirement plans, salary information  
    - **💻 IT Setup** - Laptop configuration, software access, security protocols
    - **📅 Onboarding Checklists** - Week-by-week guidance for your first month
    - **📞 Important Contacts** - HR, IT support, emergency contacts
    - **✈️ Travel & Expenses** - Booking policies, reimbursement procedures
    """)
    st.markdown("**💡 Pro Tip:** Ask me anything about your onboarding journey - I have access to all 17 company documents and can provide instant, personalized answers!")
    st.markdown("*Available 24/7 • Instant Responses • Comprehensive Knowledge Base*")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <style>
    .green-btn button { background-color: #28a745 !important; color: white !important; border: 1px solid #28a745 !important; }
    .red-btn button { background-color: #dc3545 !important; color: white !important; border: 1px solid #dc3545 !important; }
    </style>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="green-btn">', unsafe_allow_html=True)
        if st.button("📁 Get Formal Documents", use_container_width=True):
            st.session_state.page = "documents"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="red-btn">', unsafe_allow_html=True)
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""<div class="chat-header"><h3>💬 Chat with Nova</h3></div>""", unsafe_allow_html=True)

    for msg in st.session_state.messages:
        if "role" in msg and "content" in msg:
            bubble_class = "user-message" if msg["role"] == "user" else "bot-message"
            safe_content = html.escape(str(msg["content"]), quote=True)
            st.markdown(f'<div class="chat-message {bubble_class}">{safe_content}</div>', unsafe_allow_html=True)



    user_input = st.chat_input("Ask Nova anything...")
    if user_input:
        try:
            if len(user_input.strip()) == 0:
                st.warning("Please enter a question.")
            elif len(user_input) > 1000:
                st.error("Question too long. Please keep it under 1000 characters.")
            else:
                st.session_state.messages.append({"role": "user", "content": user_input})
                
                document_name = find_relevant_document(user_input)
                document_content = load_document(document_name)
                
                if document_content.startswith("Error:"):
                    ai_response = "I'm having trouble accessing the relevant documents. Please try again or contact support."
                else:
                    ai_response = get_ai_response(user_input, document_content)
                
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
                st.rerun()
            
        except Exception as e:
            st.error("An error occurred while processing your request. Please try again.")
            print(f"Chat error: {type(e).__name__}: {str(e)}")
# -------------------- DOCUMENT PAGE --------------------
else:
    st.markdown("""
    <div class="welcome-header">
        <h1>📁 Company Documents</h1>
    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅ Back to Chat", use_container_width=True):
        st.session_state.page = "chat"
        st.rerun()

    def doc_card(title, filename, color_class):
        """Display document card with secure content handling."""
        try:
            safe_title = html.escape(str(title), quote=True)
            st.markdown(f'<div class="doc-box {color_class}">{safe_title}</div>', unsafe_allow_html=True)
            
            document_content = load_document(filename)
            
            col1, col2 = st.columns(2)
            with col1:
                if not document_content.startswith("Error:"):
                    st.download_button("⬇ Download", document_content, filename, key=f"download_{filename}")
                else:
                    st.error("Download unavailable")
            
            with col2:
                if st.button(f"👁️ Preview", key=f"preview_{filename}"):
                    st.session_state.preview_open = filename
                    st.rerun()
            
            if st.session_state.preview_open == filename:
                close_col, _ = st.columns([1, 4])
                with close_col:
                    if st.button("❌ Close", key=f"close_{filename}"):
                        st.session_state.preview_open = None
                        st.rerun()
                
                if not document_content.startswith("Error:"):
                    st.text_area(f"📄 {safe_title} Content:", document_content, height=300, key=f"content_{filename}")
                else:
                    st.error(document_content)
                    
        except Exception as e:
            st.error(f"Error displaying document: {type(e).__name__}")
            print(f"Document card error: {str(e)}")

    # All documents in 2-column layout
    documents = [
        ("🏢 Company Values", "company_values.txt", "doc-blue"),
        ("🏗️ Organization Structure", "org_structure.txt", "doc-yellow"),
        ("📞 Important Contacts", "important_contacts.txt", "doc-green"),
        ("⚖️ Code of Conduct", "code_of_conduct.txt", "doc-blue"),
        ("💼 Work Policy", "work_policy.txt", "doc-grey"),
        ("🏖️ Leave Policy", "leave_policy.txt", "doc-red"),
        ("🚫 Security Guidelines", "security_guidelines.txt", "doc-red"),
        ("✈️ Travel Policy", "travel_policy.txt", "doc-yellow"),
        ("💰 Benefits Guide", "benefits.txt", "doc-green"),
        ("💳 Payroll FAQ", "payroll_faq.txt", "doc-yellow"),
        ("💸 Reimbursement Policy", "reimbursement_policy.txt", "doc-blue"),
        ("💻 IT Setup Guide", "it_setup.txt", "doc-grey"),
        ("🛠️ Tools Onboarding", "tools_onboarding.txt", "doc-blue"),
        ("📅 Week 1 Checklist", "week1_checklist.txt", "doc-blue"),
        ("📅 Week 2 Checklist", "week2_checklist.txt", "doc-yellow"),
        ("📅 Week 3 Checklist", "week3_checklist.txt", "doc-green"),
        ("📅 Week 4 Checklist", "week4_checklist.txt", "doc-grey")
    ]

    # Display documents in 2-column grid
    for i in range(0, len(documents), 2):
        col1, col2 = st.columns(2)
        
        with col1:
            title, file, color = documents[i]
            doc_card(title, file, color)
        
        if i + 1 < len(documents):
            with col2:
                title, file, color = documents[i + 1]
                doc_card(title, file, color)
