import streamlit as st
import sys

sys.path.append("mount/src/Carlat  Reaserch Updates/src")

from docs_txt import *
from process_pdf import *

from extract_pdf_content import *
from docx import Document as doc



# Apply the custom CSS
with st.container(border=False):
    st.title("📝Carlat Reaserch Updates")
    st.caption("🚀 A streamlit editor powered by OpenAI LLM")
    st.divider()

    file = st.file_uploader(label="", type=[".pdf"], key="upload")
    if file:
        # process the pdf
        path = "mount/src/Carlat  Reaserch Updates/documents"
        raw_text = get_text_from_dir(path)
        generated_content = get_research_updates(raw_text)

        # Read the content of the temporary file as bytes

         #save the content of the uploaded file
        document = doc()

        # Add content to the document
        document.add_paragraph(generated_content)

        # Save the document
        document.save("generated_content.docx")
        with open("generated_content.docx", "rb") as f:
            document_bytes = f.read()

            # Provide the bytes to the download button
            st.download_button("Download RU", data=document_bytes, mime="application/octet-stream", file_name="reaserch_update.docx")


        print(generated_content)
