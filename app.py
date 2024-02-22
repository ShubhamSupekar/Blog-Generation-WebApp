import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# # Function to get response from Llama 2 model

def getLLamaresponse(input_text,no_words,blog_style):

#     # Make a call to Llama 2 model
#     # CTransformers lib. provides python building for GGML models
#     # GGML: It defines a binary format for distributing large language models (LLMs). 
#     # To do that it uses quantization, a technique that allows LLMs to run on consumer hardware with effective CPU inferencing.
    # replace this path 'Model\llama-2-7b-chat.ggmlv3.q8_0.bin' with model file path  
    llm=CTransformers(model='Model\llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ## Prompt Template

    template="""
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response




# page config

st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter the Blog Topic")




# # Creating two more colums for additional 2 fields
# # 1. for getting number of words
# # 2. to whome you want to write this blog 


col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Data Scientist','Common People'),index=0)
    



# # Creating submit button 

submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))