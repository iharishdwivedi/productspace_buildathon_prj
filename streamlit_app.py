import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="OnboardAI - Nova",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    * { font-family: 'Arial', sans-serif; }
    .stApp { background: #F8FFF4; }
    .main .block-container { padding: 2rem; max-width: 1200px; margin: 0 auto; }
    .welcome-header { background: #011638; color: #F8FFF4; padding: 3rem; border-radius: 15px; text-align: center; margin-bottom: 2rem; }
    .welcome-box { background: #FCFFEB; padding: 2rem; border-radius: 15px; border: 2px solid #BCD39C; margin-bottom: 2rem; color: #474350; }
    .chat-header { background: #FAFAC6; padding: 1rem; border-radius: 15px; border: 2px solid #474350; text-align: center; margin-bottom: 1rem; }
    .chat-message { padding: 1rem; border-radius: 15px; margin: 1rem 0; max-width: 70%; }
    .user-message { background: #474350; color: #F8FFF4; margin-left: auto; }
    .bot-message { background: #FAFAC6; color: #011638; border: 1px solid #474350; }
    .stButton > button { background: #FECDAA; color: #011638; border: 2px solid #474350; border-radius: 10px; padding: 0.5rem 1rem; font-weight: 600; }
    .stButton > button:hover { background: #BCD39C; }
    .doc-box { padding: 1rem; border-radius: 10px; margin-bottom: 1rem; border: 2px solid #474350; }
    .doc-box-1 { background: #FECDAA; }
    .doc-box-2 { background: #BCD39C; }
    .doc-box-3 { background: #FAFAC6; }
    .doc-box-4 { background: #FCFFEB; }
    .doc-box-5 { background: #F8FFF4; }
</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "page" not in st.session_state:
    st.session_state.page = "chat"

API_KEY = 'AIzaSyD-JjJC_OVrc6i-zix15GWZQEw9N8qT1u8'
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")

def load_allatone_content():
    try:
        with open('data/allatone.txt', 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error loading content: {str(e)}"

def load_document(filename):
    try:
        with open(f'data/{filename}', 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error loading {filename}: {str(e)}"

def get_document_mapping():
    return {
        'benefits': 'benefits.txt', 'health': 'benefits.txt', 'insurance': 'benefits.txt',
        'payroll': 'payroll_faq.txt', 'salary': 'payroll_faq.txt', 'pay': 'payroll_faq.txt',
        'conduct': 'code_of_conduct.txt', 'ethics': 'code_of_conduct.txt',
        'laptop': 'it_setup.txt', 'computer': 'it_setup.txt', 'setup': 'it_setup.txt',
        'security': 'security_guidelines.txt', 'leave': 'leave_policy.txt',
        'travel': 'travel_policy.txt', 'expense': 'reimbursement_policy.txt',
        'contact': 'important_contacts.txt', 'values': 'company_values.txt',
        'organization': 'org_structure.txt', 'tools': 'tools_onboarding.txt',
        'work policy': 'work_policy.txt', 'week 1': 'week1_checklist.txt',
        'week 2': 'week2_checklist.txt', 'week 3': 'week3_checklist.txt',
        'week 4': 'week4_checklist.txt'
    }

def find_relevant_document(query):
    query_lower = query.lower()
    doc_mapping = get_document_mapping()
    for keyword, doc_file in doc_mapping.items():
        if keyword in query_lower:
            return doc_file
    return 'allatone.txt'

def get_ai_response(user_query, context):
    document_keywords = ['find document', 'where can i find', 'locate document', 'access document', 'get document', 'formal document', 'official document', 'page structure', 'navigate', 'documents page']
    is_document_query = any(keyword in user_query.lower() for keyword in document_keywords)
    
    introduction_keywords = ['who are you', 'what are you', 'introduce yourself', 'tell me about yourself', 'who is nova', 'what is nova']
    is_introduction_query = any(keyword in user_query.lower() for keyword in introduction_keywords)
    
    page_info = """

PAGE STRUCTURE INFORMATION:
This OnboardAI system has two main pages:

1. **CHAT PAGE** (Current page):
   - Main chat interface with Nova AI assistant
   - Get instant answers to questions about policies, benefits, IT setup
   - Use the "📁 Get Formal Documents" button (located above the chat area) to access official documents

2. **DOCUMENTS PAGE**:
   - Access by clicking the "📁 Get Formal Documents" button on the chat page
   - Contains 17 official company documents organized in 5 professional categories:
   
   **📋 Company Information:**
   - Company Values, Organization Structure, Important Contacts
   
   **📜 Policies & Guidelines:**
   - Code of Conduct, Work Policy, Leave Policy, Travel Policy, Security Guidelines
   
   **💰 Benefits & Payroll:**
   - Benefits Guide, Payroll FAQ, Reimbursement Policy
   
   **💻 IT Setup & Tools:**
   - IT Setup Guide, Tools Onboarding
   
   **📅 Weekly Onboarding Checklists:**
   - Week 1 Checklist, Week 2 Checklist, Week 3 Checklist, Week 4 Checklist
   
   - Each document has Download and Preview buttons
   - Preview opens expandable content viewer
   - Use "← Back to Chat" button to return to this chat interface

To access documents: Click "📁 Get Formal Documents" → Find your category → Download or Preview the document you need
""" if is_document_query else ""
    
    introduction_info = """

INTRODUCTION:
Hi! I'm Nova, your AI-powered onboarding assistant. Here's what you should know about me:

🤖 **Who I Am:**
- I'm an intelligent assistant specifically designed to help new employees with their onboarding journey
- I'm powered by Google Gemini 2.5 Flash AI technology
- I have access to all 17 company onboarding documents and can provide instant answers

💡 **What I Can Do:**
- Answer questions about company policies, benefits, IT setup, and procedures
- Guide you to the right documents and information
- Help you navigate through your first weeks at the company
- Provide 24/7 support for all your onboarding needs

📚 **My Knowledge Base:**
- Company values and organizational structure
- HR policies including benefits, payroll, and leave policies
- IT setup guides and security guidelines
- Weekly onboarding checklists for your first month
- Important contacts and resources

🎯 **My Goal:**
To make your onboarding experience smooth, efficient, and stress-free by providing instant access to information and personalized guidance.

Feel free to ask me anything about your onboarding process!
""" if is_introduction_query else ""
    
    prompt = f"""
You are Nova, an AI Onboarding Assistant for new employees.

CONTEXT FROM COMPANY DOCUMENTS:
{context}{page_info}{introduction_info}

USER QUERY: {user_query}

INSTRUCTIONS:
- Use ONLY the provided context to answer questions
- Be friendly, professional, and helpful
- If user asks about finding documents or page navigation, include the page structure information
- If user asks who you are or for an introduction, use the introduction information provided
- When providing specific information, you can reference document types (like "the benefits guide" or "company policy") but never mention exact filenames
- If information isn't in the context, say "I don't have that specific information in my knowledge base. Please contact HR at hr@abc.com"
- Provide structured, clear answers with bullet points when appropriate
- Keep responses concise but comprehensive
- Do not introduce yourself in regular responses unless specifically asked

RESPONSE:
"""
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"I apologize, but I'm experiencing technical difficulties. Please try again or contact IT support at x4357. Error: {str(e)}"

if st.session_state.page == "chat":
    st.markdown("""
    <div class="welcome-header">
        <h1>🤖 Welcome to OnboardAI</h1>
        <p>Your AI-powered onboarding assistant</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="welcome-box">
        <strong>👋 Hi! I'm Nova, your AI Onboarding Assistant.</strong><br><br>
        I can help you with:
        <ul>
            <li>Company policies and procedures</li>
            <li>Benefits and HR information</li>
            <li>IT setup and security guidelines</li>
            <li>Contact information and resources</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📁 Get Formal Documents", use_container_width=True):
        st.session_state.page = "documents"
        st.rerun()
    
    st.markdown("""
    <div class="chat-header">
        <h3>💬 Chat with Nova</h3>
    </div>
    """, unsafe_allow_html=True)
    
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="chat-message user-message">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message bot-message">{message["content"]}</div>', unsafe_allow_html=True)
    
    user_input = st.chat_input("Ask Nova anything about onboarding...")
    
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        with st.spinner("Nova is thinking..."):
            relevant_doc = find_relevant_document(user_input)
            if relevant_doc == 'allatone.txt':
                context = load_allatone_content()
            else:
                context = load_document(relevant_doc)
            response = get_ai_response(user_input, context)
            
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
    
    if st.session_state.messages:
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.rerun()

elif st.session_state.page == "documents":
    st.markdown("""
    <div class="welcome-header">
        <h1>📁 Company Documents</h1>
        <p>Access all official onboarding documents</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Back to Chat", use_container_width=True):
        st.session_state.page = "chat"
        st.rerun()
    
    # Company Information
    st.subheader("📋 Company Information")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="doc-box doc-box-1"><h4>Company Values</h4></div>', unsafe_allow_html=True)
        content = load_document("company_values.txt")
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("⬇️ Download", content, "company_values.txt", "text/plain", key="values")
        with c2:
            if st.button("👁️ Preview", key="prev_values"):
                with st.expander("Company Values", expanded=True):
                    st.text_area("", content, height=300, label_visibility="collapsed")
    
    with col2:
        st.markdown('<div class="doc-box doc-box-2"><h4>Organization Structure</h4></div>', unsafe_allow_html=True)
        content = load_document("org_structure.txt")
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("⬇️ Download", content, "org_structure.txt", "text/plain", key="org")
        with c2:
            if st.button("👁️ Preview", key="prev_org"):
                with st.expander("Organization Structure", expanded=True):
                    st.text_area("", content, height=300, label_visibility="collapsed")
    
    with col3:
        st.markdown('<div class="doc-box doc-box-3"><h4>Important Contacts</h4></div>', unsafe_allow_html=True)
        content = load_document("important_contacts.txt")
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("⬇️ Download", content, "important_contacts.txt", "text/plain", key="contacts")
        with c2:
            if st.button("👁️ Preview", key="prev_contacts"):
                with st.expander("Important Contacts", expanded=True):
                    st.text_area("", content, height=300, label_visibility="collapsed")
    
    st.divider()
    
    # Policies & Guidelines
    st.subheader("📜 Policies & Guidelines")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="doc-box doc-box-4"><h4>Code of Conduct</h4></div>', unsafe_allow_html=True)
        content = load_document("code_of_conduct.txt")
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("⬇️ Download", content, "code_of_conduct.txt", "text/plain", key="conduct")
        with c2:
            if st.button("👁️ Preview", key="prev_conduct"):
                with st.expander("Code of Conduct", expanded=True):
                    st.text_area("", content, height=300, label_visibility="collapsed")
    
    with col2:
        st.markdown('<div class="doc-box doc-box-5"><h4>Work Policy</h4></div>', unsafe_allow_html=True)
        content = load_document("work_policy.txt")
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("⬇️ Download", content, "work_policy.txt", "text/plain", key="work")
        with c2:
            if st.button("👁️ Preview", key="prev_work"):
                with st.expander("Work Policy", expanded=True):
                    st.text_area("", content, height=300, label_visibility="collapsed")
    
    with col3:
        st.markdown('<div class="doc-box doc-box-1"><h4>Leave Policy</h4></div>', unsafe_allow_html=True)
        content = load_document("leave_policy.txt")
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("⬇️ Download", content, "leave_policy.txt", "text/plain", key="leave")
        with c2:
            if st.button("👁️ Preview", key="prev_leave"):
                with st.expander("Leave Policy", expanded=True):
                    st.text_area("", content, height=300, label_visibility="collapsed")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="doc-box doc-box-2"><h4>Travel Policy</h4></div>', unsafe_allow_html=True)
        content = load_document("travel_policy.txt")
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("⬇️ Download", content, "travel_policy.txt", "text/plain", key="travel")
        with c2:
            if st.button("👁️ Preview", key="prev_travel"):
                with st.expander("Travel Policy", expanded=True):
                    st.text_area("", content, height=300, label_visibility="collapsed")
    
    with col2:
        st.markdown('<div class="doc-box doc-box-3"><h4>Security Guidelines</h4></div>', unsafe_allow_html=True)
        content = load_document("security_guidelines.txt")
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("⬇️ Download", content, "security_guidelines.txt", "text/plain", key="security")
        with c2:
            if st.button("👁️ Preview", key="prev_security"):
                with st.expander("Security Guidelines", expanded=True):
                    st.text_area("", content, height=300, label_visibility="collapsed")
    
    st.divider()
    
    # Benefits & Payroll
    st.subheader("💰 Benefits & Payroll")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="doc-box doc-box-4"><h4>Benefits Guide</h4></div>', unsafe_allow_html=True)
        content = load_document("benefits.txt")
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("⬇️ Download", content, "benefits.txt", "text/plain", key="benefits")
        with c2:
            if st.button("👁️ Preview", key="prev_benefits"):
                with st.expander("Benefits Guide", expanded=True):
                    st.text_area("", content, height=300, label_visibility="collapsed")
    
    with col2:
        st.markdown('<div class="doc-box doc-box-5"><h4>Payroll FAQ</h4></div>', unsafe_allow_html=True)
        content = load_document("payroll_faq.txt")
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("⬇️ Download", content, "payroll_faq.txt", "text/plain", key="payroll")
        with c2:
            if st.button("👁️ Preview", key="prev_payroll"):
                with st.expander("Payroll FAQ", expanded=True):
                    st.text_area("", content, height=300, label_visibility="collapsed")
    
    with col3:
        st.markdown('<div class="doc-box doc-box-1"><h4>Reimbursement Policy</h4></div>', unsafe_allow_html=True)
        content = load_document("reimbursement_policy.txt")
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("⬇️ Download", content, "reimbursement_policy.txt", "text/plain", key="reimburse")
        with c2:
            if st.button("👁️ Preview", key="prev_reimburse"):
                with st.expander("Reimbursement Policy", expanded=True):
                    st.text_area("", content, height=300, label_visibility="collapsed")
    
    st.divider()
    
    # IT Setup & Tools
    st.subheader("💻 IT Setup & Tools")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="doc-box doc-box-2"><h4>IT Setup Guide</h4></div>', unsafe_allow_html=True)
        content = load_document("it_setup.txt")
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("⬇️ Download", content, "it_setup.txt", "text/plain", key="it")
        with c2:
            if st.button("👁️ Preview", key="prev_it"):
                with st.expander("IT Setup Guide", expanded=True):
                    st.text_area("", content, height=300, label_visibility="collapsed")
    
    with col2:
        st.markdown('<div class="doc-box doc-box-3"><h4>Tools Onboarding</h4></div>', unsafe_allow_html=True)
        content = load_document("tools_onboarding.txt")
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("⬇️ Download", content, "tools_onboarding.txt", "text/plain", key="tools")
        with c2:
            if st.button("👁️ Preview", key="prev_tools"):
                with st.expander("Tools Onboarding", expanded=True):
                    st.text_area("", content, height=300, label_visibility="collapsed")
    
    st.divider()
    
    # Weekly Checklists
    st.subheader("📅 Weekly Onboarding Checklists")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="doc-box doc-box-4"><h4>Week 1 Checklist</h4></div>', unsafe_allow_html=True)
        content = load_document("week1_checklist.txt")
        st.download_button("⬇️ Download", content, "week1_checklist.txt", "text/plain", key="week1", use_container_width=True)
        if st.button("👁️ Preview", key="prev_week1", use_container_width=True):
            with st.expander("Week 1 Checklist", expanded=True):
                st.text_area("", content, height=300, label_visibility="collapsed")
    
    with col2:
        st.markdown('<div class="doc-box doc-box-5"><h4>Week 2 Checklist</h4></div>', unsafe_allow_html=True)
        content = load_document("week2_checklist.txt")
        st.download_button("⬇️ Download", content, "week2_checklist.txt", "text/plain", key="week2", use_container_width=True)
        if st.button("👁️ Preview", key="prev_week2", use_container_width=True):
            with st.expander("Week 2 Checklist", expanded=True):
                st.text_area("", content, height=300, label_visibility="collapsed")
    
    with col3:
        st.markdown('<div class="doc-box doc-box-1"><h4>Week 3 Checklist</h4></div>', unsafe_allow_html=True)
        content = load_document("week3_checklist.txt")
        st.download_button("⬇️ Download", content, "week3_checklist.txt", "text/plain", key="week3", use_container_width=True)
        if st.button("👁️ Preview", key="prev_week3", use_container_width=True):
            with st.expander("Week 3 Checklist", expanded=True):
                st.text_area("", content, height=300, label_visibility="collapsed")
    
    with col4:
        st.markdown('<div class="doc-box doc-box-2"><h4>Week 4 Checklist</h4></div>', unsafe_allow_html=True)
        content = load_document("week4_checklist.txt")
        st.download_button("⬇️ Download", content, "week4_checklist.txt", "text/plain", key="week4", use_container_width=True)
        if st.button("👁️ Preview", key="prev_week4", use_container_width=True):
            with st.expander("Week 4 Checklist", expanded=True):
                st.text_area("", content, height=300, label_visibility="collapsed")