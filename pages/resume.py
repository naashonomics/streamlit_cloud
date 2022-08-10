import streamlit as st
from PIL import Image

with open("pages/resume_style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Avinash Anantharamu
##### *Resume* 
''')

image = Image.open('db.jpg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Educator, Software Engineer with 10+ of experience in platform and data. 

''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #6495ED;">
  <a class="navbar-brand" href="https://youtube.com/channel/UC5ASIl3Js_XSsb95sedH5kQ" target="_blank">Avinash Anantharamu</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#patents">Patents</a>
      </li>
       <li class="nav-item">
        <a class="nav-link" href="#certification">Certifications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#patents">Patents</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
    
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

def txt5(a, b,c):
  col1, col2,col3 = st.columns([2.5,1.5,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)
#####################
st.markdown('''
## Work Experience
''')

txt('**Senior Software Engineer**, ASML, San Jose , United States',
'2022-Current')
st.markdown('''
- Working with Brion Platform Group on Computational Lithography Products ranging from OPC, LMC and SMO.
- Skills: PERL , Python , Azure , MongoDB and SQL  
''')

txt('**Lead Software Engineer**,Cadence Design System , San Jose , United States',
'2020-2022')
st.markdown('''
- Worked with Design group on Virtuso, Conformal  and CAT 
- Skills: PERL , Python, C++ , Jenkins , Streamlit 
''')

txt('**Senior Software Engineer**, Synopsys , Sunnyvale , United States',
'2014-2020')
st.markdown('''
- Worked with Verification Projects on Zebu (Emulation) and HAPS (prototypying) platforms 
- Skills: Python, C++ , Jenkins , Streamlit , Pandas , ELK , Scikit Learn, MongoDB and SQL  
''')

#####################
st.markdown('''
## Education
''')

txt('**Master of Science** (Computer Science), *San Jose State Univeristy*, United States',
'2012-2014')
st.markdown('''
- GPA: `3.5`
- Coursework:  
    - CS 255 : Design and Analysis of Algorithms 
    - CS 249 : Distributed Computing 
    - CS 257 : Data Base System Principles
    - CS 267 : Topics in Database Systems
    - CS 251A : Object-Oriented Analysis
    - CS 251B : Object-Oriented Design 
    - CS 274 : Topics in XML and Web Intelligence
    - CS 180I : Internship 
    - CS 297 : Preparation for Writing Project
    - CS 298 : Master's Writing Project
''')

txt('**Bachelors of Engineering** (Computer Science), *VTU*, India',
'2006-2010')
st.markdown('''
- GPA: `75`
- Graduated with First Class Distinction .
''')

#####################
st.markdown('''
## Patents 
''')
txt('**Machine Learning Enchnaced Compiler**, [US11366948B2](https://pdfpiw.uspto.gov/.piw?Docid=11366948&homeurl=http%3A%2F%2Fpatft.uspto.gov%2Fnetacgi%2Fnph-Parser%3FSect1%3DPTO2%2526Sect2%3DHITOFF%2526p%3D1%2526u%3D%25252Fnetahtml%25252FPTO%25252Fsearch-bool.html%2526r%3D1%2526f%3DG%2526l%3D50%2526co1%3DAND%2526d%3DPTXT%2526s1%3D%252522MACHINE-LEARNING%252BENHANCED%252BCOMPILER%252522%2526OS%3D%2526RS%3D&PageNum=&Rtype=&SectionNum=&idkey=NONE&Input=View+first+page)',
'July 2022')


####################
st.markdown('''
## Certification 
''')
txt('**Microsoft Azure Fundamentals Certified**, [AZ-900](https://www.credly.com/badges/6aaae579-64d8-4e94-9d9d-b5f81106bd7b?source=linked_in_profile)',
'July 2022-Present')
txt('**Microsoft Azure AI Fundamentals Certified**, [AI-900](https://www.credly.com/badges/c01d6d82-df51-43b2-a267-fd8c7d8898b7?source=linked_in_profile)',
'July 2022-Present')


#####################
st.markdown('''
## Projects
''')
txt5('**Personal expense tracker**, [Demo](https://naashonomics-streamlit-cloud-streamlit-app-tgu0tp.streamlitapp.com/expense_tracker)','**[Streamlit,Demodb,Plotly]**' ,'August 2022')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `C++`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `Azure`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/anantharamuavinash')
txt2('GitHub', 'https://github.com/naashonomics/')

