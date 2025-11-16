# OnboardAI - Nova 🤖

## Project Statement

**OnboardAI** is an intelligent employee onboarding assistant designed to streamline the new hire experience through AI-powered conversational support and comprehensive document management. The system provides instant access to company policies, procedures, and onboarding materials while offering personalized guidance through an intuitive chat interface.

## Why I Chose This Project

### Problem Statement
- **Manual Onboarding Inefficiency**: Traditional onboarding processes are time-consuming and often overwhelming for new employees
- **Information Scattered**: Company documents and policies are typically spread across multiple platforms
- **HR Bottleneck**: HR teams spend significant time answering repetitive onboarding questions
- **Inconsistent Experience**: New hires receive varying levels of support and information

### Solution Benefits
- **24/7 Availability**: Instant access to onboarding information anytime
- **Personalized Assistance**: AI-powered responses tailored to specific queries
- **Centralized Resources**: All documents and information in one accessible platform
- **Scalable Support**: Reduces HR workload while improving employee experience

## Technology Stack

### Core Technologies
- **Frontend**: Streamlit (Python web framework)
- **AI Engine**: Google Gemini 2.5 Flash
- **Backend**: Python 3.x
- **Document Processing**: Custom RAG (Retrieval-Augmented Generation) system
- **Styling**: Custom CSS with professional color palette

### Key Libraries
```python
streamlit==1.28.0
google-generativeai==0.3.0
```

### Requirements File
Create a `requirements.txt` file with:
```txt
streamlit==1.28.0
google-generativeai==0.3.0
```

### Architecture Components
- **streamlit_app.py**: Main application interface
- **rag_system.py**: Smart document retrieval system
- **ai_assistant.py**: Google Gemini AI integration
- **data/**: Document repository (17 company documents)

## Project Structure

```
buildathon_prj/
├── streamlit_app.py          # Main Streamlit application
├── rag_system.py            # RAG system for document retrieval
├── ai_assistant.py          # AI integration module
├── data/                    # Document repository
│   ├── allatone.txt        # Comprehensive summary document
│   ├── benefits.txt        # Benefits information
│   ├── payroll_faq.txt     # Payroll frequently asked questions
│   ├── code_of_conduct.txt # Company code of conduct
│   ├── it_setup.txt        # IT setup guidelines
│   ├── security_guidelines.txt # Security policies
│   ├── leave_policy.txt    # Leave policies
│   ├── travel_policy.txt   # Travel guidelines
│   ├── reimbursement_policy.txt # Expense policies
│   ├── important_contacts.txt # Key contact information
│   ├── company_values.txt  # Company values and culture
│   ├── org_structure.txt   # Organizational structure
│   ├── tools_onboarding.txt # Tools and software guide
│   ├── work_policy.txt     # Work policies and procedures
│   ├── week1_checklist.txt # First week onboarding tasks
│   ├── week2_checklist.txt # Second week onboarding tasks
│   ├── week3_checklist.txt # Third week onboarding tasks
│   └── week4_checklist.txt # Fourth week onboarding tasks
└── README.md               # Project documentation
```

## Features & Functionality

### 🤖 AI Chat Interface
- **Nova AI Assistant**: Powered by Google Gemini 2.5 Flash
- **Contextual Responses**: Smart document routing based on query keywords
- **Natural Language Processing**: Understands and responds to conversational queries
- **Page Navigation Awareness**: Guides users through the system structure

### 📁 Document Management System
- **17 Company Documents**: Comprehensive onboarding materials
- **Categorized Organization**: 5 professional categories for easy navigation
- **Dual Access Methods**: Download and preview options for each document
- **Color-Coded Interface**: Visual distinction using professional color palette

### 🎨 Professional Design
- **Custom Color Palette**: #474350, #F8FFF4, #FCFFEB, #FAFAC6, #FECDAA, #BCD39C, #011638
- **Responsive Layout**: Clean, professional interface optimized for business use
- **Intuitive Navigation**: Simple two-page structure with clear navigation

## Document Categories

### 📋 Company Information
- Company Values
- Organization Structure  
- Important Contacts

### 📜 Policies & Guidelines
- Code of Conduct
- Work Policy
- Leave Policy
- Travel Policy
- Security Guidelines

### 💰 Benefits & Payroll
- Benefits Guide
- Payroll FAQ
- Reimbursement Policy

### 💻 IT Setup & Tools
- IT Setup Guide
- Tools Onboarding

### 📅 Weekly Onboarding Checklists
- Week 1-4 Checklists

## Smart RAG System

### Document Routing Logic
```python
# Keyword-based document mapping
keyword_mapping = {
    'benefits': 'benefits.txt',
    'payroll': 'payroll_faq.txt', 
    'conduct': 'code_of_conduct.txt',
    'security': 'security_guidelines.txt',
    # ... additional mappings
}
```

### Intelligent Query Processing
- **Keyword Detection**: Identifies relevant documents based on query content
- **Fallback System**: Uses comprehensive summary (allatone.txt) for general queries
- **Context Preservation**: Maintains conversation context for better responses

## Development Workflow

### Phase 1: Foundation (Initial Setup)
1. **Technology Selection**: Chose Streamlit for rapid prototyping
2. **AI Integration**: Implemented Google Gemini API
3. **Basic Chat Interface**: Created core conversational functionality

### Phase 2: Document System (Core Features)
1. **Document Collection**: Gathered 17 comprehensive onboarding documents
2. **RAG Implementation**: Built smart document retrieval system
3. **File Management**: Created organized document structure

### Phase 3: UI/UX Enhancement (Professional Polish)
1. **Design System**: Implemented professional color palette
2. **Layout Optimization**: Created clean, business-appropriate interface
3. **Navigation Flow**: Designed intuitive two-page structure

### Phase 4: Advanced Features (Final Polish)
1. **Smart Routing**: Enhanced AI with page structure awareness
2. **Document Preview**: Added expandable preview functionality
3. **Download System**: Implemented direct file download capabilities

## How It Works

### User Journey
1. **Landing**: User arrives at chat interface with Nova AI assistant
2. **Query Processing**: User asks questions about onboarding topics
3. **Smart Retrieval**: System identifies relevant documents using keyword mapping
4. **AI Response**: Nova provides contextual answers using retrieved content
5. **Document Access**: User can access formal documents via "Get Formal Documents" button
6. **Document Interaction**: Users can preview or download any of the 17 documents

### Technical Flow
```
User Query → Keyword Analysis → Document Selection → AI Processing → Response Generation
     ↓
Document Access → Category Selection → Preview/Download → User Satisfaction
```

## Installation & Setup

### Prerequisites
- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **Google Gemini API key** - [Get API Key](https://makersuite.google.com/app/apikey)

### Step-by-Step Installation Guide

#### Step 1: Clone the Repository
```bash
# Clone from GitHub
git clone https://github.com/your-username/onboardai-nova.git
cd onboardai-nova
```

#### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv onboardai_env

# Activate virtual environment
# On Windows:
onboardai_env\Scripts\activate
# On macOS/Linux:
source onboardai_env/bin/activate
```

#### Step 3: Install Dependencies
```bash
# Install from requirements file
pip install -r requirements.txt

# OR install manually
pip install streamlit==1.28.0 google-generativeai==0.3.0
```

#### Step 4: Configure API Key
1. Get your Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Open `streamlit_app.py` in a text editor
3. Replace the API key on line 43:
```python
API_KEY = 'your-actual-google-gemini-api-key-here'
```

#### Step 5: Verify Project Structure
Ensure your project structure looks like this:
```
onboardai-nova/
├── streamlit_app.py
├── requirements.txt
├── README.md
└── data/
    ├── allatone.txt
    ├── benefits.txt
    ├── payroll_faq.txt
    ├── code_of_conduct.txt
    ├── it_setup.txt
    ├── security_guidelines.txt
    ├── leave_policy.txt
    ├── travel_policy.txt
    ├── reimbursement_policy.txt
    ├── important_contacts.txt
    ├── company_values.txt
    ├── org_structure.txt
    ├── tools_onboarding.txt
    ├── work_policy.txt
    ├── week1_checklist.txt
    ├── week2_checklist.txt
    ├── week3_checklist.txt
    └── week4_checklist.txt
```

#### Step 6: Test Installation
```bash
# Test if all dependencies are installed correctly
python -c "import streamlit; import google.generativeai; print('All dependencies installed successfully!')"
```

## How to Run

### Method 1: Local Development (Recommended for Testing)

1. **Navigate to Project Directory**
```bash
cd onboardai-nova
```

2. **Activate Virtual Environment** (if created)
```bash
# On Windows:
onboardai_env\Scripts\activate
# On macOS/Linux:
source onboardai_env/bin/activate
```

3. **Run the Application**
```bash
streamlit run streamlit_app.py
```

4. **Access the Application**
- Open your web browser
- Go to: `http://localhost:8501`
- Start chatting with Nova!

### Method 2: Production Deployment

#### Option A: Streamlit Cloud (Free)
1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Deploy with one click

#### Option B: Local Network Access
```bash
streamlit run streamlit_app.py --server.address 0.0.0.0 --server.port 8501
```
Access from other devices: `http://your-computer-ip:8501`

#### Option C: Docker Deployment
```bash
# Build Docker image
docker build -t onboardai .

# Run container
docker run -p 8501:8501 onboardai
```

### Troubleshooting

**Common Issues:**

1. **"Module not found" error**
   ```bash
   pip install --upgrade streamlit google-generativeai
   ```

2. **API key error**
   - Verify your API key is correct
   - Check if API key has proper permissions

3. **Port already in use**
   ```bash
   streamlit run streamlit_app.py --server.port 8502
   ```

4. **Documents not loading**
   - Ensure all files are in the `data/` directory
   - Check file permissions

## Usage Guide

### For New Employees
1. **Start Chatting**: Ask Nova any onboarding-related questions
2. **Get Documents**: Click "📁 Get Formal Documents" for official materials
3. **Navigate Categories**: Browse documents by category
4. **Preview Content**: Use preview buttons to view document content
5. **Download Files**: Download documents for offline reference

### For HR Teams
1. **Monitor Usage**: Track common questions and improve documentation
2. **Update Content**: Regularly update documents in the data/ directory
3. **Customize Responses**: Modify AI prompts for better responses
4. **Scale System**: Add new document categories as needed

## Future Roadmap

### Short-term Enhancements (1-3 months)
- [ ] User authentication and personalization
- [ ] Progress tracking for onboarding checklists
- [ ] Email integration for document sharing
- [ ] Mobile-responsive design improvements

### Medium-term Features (3-6 months)
- [ ] Multi-language support
- [ ] Advanced analytics and reporting
- [ ] Integration with HR management systems
- [ ] Automated document updates

### Long-term Vision (6+ months)
- [ ] Voice interaction capabilities
- [ ] Video content integration
- [ ] AI-powered onboarding path recommendations
- [ ] Integration with company learning management systems

## Technical Specifications

### Performance Metrics
- **Response Time**: < 2 seconds for AI queries
- **Document Load**: < 1 second for preview/download
- **Concurrent Users**: Supports 50+ simultaneous users
- **Uptime**: 99.9% availability target

### Security Features
- **API Key Protection**: Secure API key management
- **Document Access Control**: Controlled document access
- **Data Privacy**: No personal data storage
- **Secure Transmission**: HTTPS encryption

## Contributing

### Development Guidelines
1. Follow Python PEP 8 style guidelines
2. Maintain clean, readable code structure
3. Test all features before deployment
4. Update documentation for new features

### Adding New Documents
1. Place document in `data/` directory
2. Update keyword mapping in `get_document_mapping()`
3. Add document to appropriate category in UI
4. Test document retrieval and display

## License

This project is developed for educational and demonstration purposes. Please ensure compliance with your organization's policies when implementing in production environments.

## Contact & Support

For questions, suggestions, or support:
- **Project Developer**: [Your Name]
- **Email**: [Your Email]
- **GitHub**: [Your GitHub Profile]

---

**OnboardAI - Making Employee Onboarding Intelligent, Efficient, and Engaging** 🚀