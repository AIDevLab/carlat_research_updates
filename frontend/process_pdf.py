from openai import OpenAI
from extract_pdf_content import *
import streamlit as st


client = OpenAI(api_key=st.secrets["api_key"])



def get_research_updates(pdf_content):

    try:
        llm_messages = [{
                        "role": "system",
                        "content": "You're a helpful research Editor assistant."
                        },

                        {
                        "role": "user",
                        "content":

                        """
                        <Start of Reaserch Article>"""+

                        pdf_content

                        +"""<End of Reaserch Article>

                        Given the above seasearch article content follow the bellow instructions:

                        <INSTRUCTIONS START>
                        
                        take your time parsing it first to a more readable content including the tables.
                        Next, extract the following information: 

                        -authors names,
                        -study name, 
                        -summary pargraph of the study 
                        -carlat's take


                        return the extracted information in the following textuel order:

                        
                        REVIEW OF: <authors_names>
                        STUDY TYPE: <study_name>

                        <summary paragraph of the study>

                        CARLAT TAKE 
                        <carlat_take>
                        


                        ----------------------------
                        Follow the bellow example when generating a response: 


                        <start of an output example to follow in organization, subtitles and style>

                        REVIEW OF: Davidson et al, Mol Psychiatry 2022;27(10):3992–4000.

                        TYPE OF STUDY: Prospective open label study

                        Despite several FDA-approved medications, thoroughly researched psychotherapies, numerous support groups, and a slew of off-label treatments, alcohol use disorder (AUD) is still a leading driver of morbidity and mortality (GBD 2016 Alcohol Collaborators, Lancet 2018;392(10152):1015–1035). Novel treatment approaches are clearly needed, particularly for those with severe disease. One such promising approach is deep brain stimulation (DBS), a procedure most used in Parkinson’s disease, in which a fine electrode is placed into the brain to stimulate deep structures. 

                        In this 12-month observational study, six patients (33% female; mean age 49) with severe refractory AUD had a DBS electrode surgically implanted into the nucleus accumbens (NAc), a brain region critical in the maintenance of addiction. After surgery, patients were assessed over a 12-month period for self-reported drinking behaviors, depression, anxiety, obsessive and compulsive drinking, and liver function. PET scans were used to determine glucose metabolism in the NAc and fMRI was utilized to gauge connectivity alterations and brain activity while viewing alcohol related images. 

                        Over the year-long trial, measurements of alcohol consumption, obsessive-compulsive drinking, and anxiety showed consistent improvements. By the end of the trial, mean number of daily drinks had dropped from 10.4 to 2.7 (p>0.05). The mean score on the Obsessive-Compulsive Drinking Scale decreased from 28.7 to 8.3 and mean Beck Anxiety Inventory scores dropped from 20.3 to 9.3. AST and ALT values dropped significantly as well. Hamilton Depression Rating Scale scores, however, did not change significantly. 
                        Neuroimaging showed brain changes correlated with these clinical improvements. PET scans showed a decrease in glucose metabolism in the NAc six months post-surgery. fMRI revealed decreased connectivity between the NAc and areas of the visual association cortex, a finding previously associated with a decrease in alcohol craving (Bach P et al, Psychoneuroendocrin 2019;109:104385). Finally, researchers observed a decrease in the activation of the dorsal striatum, which is normally seen when participants view alcohol imagery.
                        While these results are promising, the intervention is not benign; it is brain surgery, after all. One participant developed an infection on the DBS hardware and required device removal. Researchers cautioned that they would expect an elevated risk of hemorrhage and seizure as well, even though it was not observed in this small trial. It is also worth noting that participants choosing to take a step as invasive as brain surgery are likely to be unusually motivated to stop drinking, and without a control group, we don’t know how much of the observed effect is due to the intervention itself or placebo.

                        CARLAT TAKE 
                        This small scale, open label trial shows promise for DBS as a novel treatment approach for those with severe AUD. Participants had an impressive drop in their drinking, and researchers were able to use neuroimaging to correlate this clinical response with brain changes. At this point, however, data is preliminary, and the procedure is not without risks, so even if DBS one day becomes an approved treatment, it will almost certainly be reserved only for the most severe patients. 
                        <end of an output example to follow>





                        <INSTRUCTIONS END>

                        
                        """

                        },
        ]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-16k-0613",
            messages=llm_messages,
            temperature=0.4,
            frequency_penalty=0,
            max_tokens= 600 ## estimated as 1 page 
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"Exception at LLM function level : {e}")
        return ""





if __name__ == "__main__": 
    path = "C:\\Users\\dell\\Desktop\\Carlat  Reaserch Updates\\documents"
    raw_text = get_text_from_dir(path)
    generated_content = get_research_updates(raw_text)
