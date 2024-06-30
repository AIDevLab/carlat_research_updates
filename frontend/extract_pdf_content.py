import os
from openai import OpenAI
from PyPDF2 import PdfReader


print(os.path.dirname(os.path.abspath(__file__)))


def get_text_from_dir(dir_path):
    files = os.listdir(dir_path)
    # files = ['Part 1_ Software and Mobile App Introduction.pdf']

    files_txt = []
    for file in files:
        pdf_reader = PdfReader(os.path.join(dir_path, file))

        raw_text = ''
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                raw_text += '\n' + text

        files_txt.append(raw_text)

    for i, raw_text in enumerate(files_txt):
        with open(f'docs_txt/{i}.txt', 'w', encoding='utf-8') as f:
            f.write(raw_text)

    raw_text = '\n'.join(files_txt)
    return raw_text


def do_formating_with_gpt(raw_text):
    print('1')
    client = OpenAI()
    final_text=f"""\
You are given an raw text from a pdf file. You are asked to format the text into a readable format. \
The raw text may include tables and nested lists. The text is as follows:
```{raw_text}```"""

    response = client.chat.completions.create(
        messages=[
            {'role': 'system', 'content': final_text},
        ],
        model="gpt-3.5-turbo",
        temperature=0,
    )
    txt = response.choices[0].message.content
    return txt



if __name__ == "__main__":
    path = "C:\\Users\\dell\\Desktop\\Carlat  Reaserch Updates\\documents"
    raw_text = get_text_from_dir(path)
