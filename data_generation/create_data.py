# %% ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import json
import openai
import tiktoken
import random
import pandas as pd
import random
import time
import json

# %% ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# load the api key
with open('../config/config.json', 'r') as file:
    api_keys = json.load(file)

openai.api_key = api_keys['API_GPT4_KEY']

# %% ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# load the clinical notes dataset
df = pd.read_csv('data/mtsamples.csv')

# %% ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def gpt_response(system_message, user_message,): 
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"{system_message}"},
            {"role": "user", "content": f"{user_message}"},
        ],
        temperature=0,
    )
    return response["choices"][0]["message"]["content"]

# %% ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# prints a random value from the list
rand_list = [n for n in range(1,7)]
MAX_LEN = 20 # store this number of values to minimize costly API calls

questions_list = []
type_list = []

system_message = '''You are a patient who has a question for your doctor.The note following this message is 
            your most recent physician note, base your questions off the patient history provided in 
            the note, but only use layman terms, patient's typically do not use medical lingo in their 
            questions. You will also be given a 'Random Number' if this number is '1' ask a question 
            about a medication (but don't mention it by name), if this number is '2' ask a question 
            about a diagnosis (but don't mention its name, just describe it) if this number is 3 ask
            a question about when you should schedule a follow up to discuss your care of a condition 
            you have and what the plan is (don't specifically regurgitate the plan or name the conditon 
            by its medical term), if the number is '4' ask something that is poorly worded (do not include
            vocalizations like stuttering, or 'um' because people don't type out their vocalizations) and 
            incorrectly spells diseases and medications names, and has many punctuation and grammatical errors,
            if the number is '5' ask a question that includes something you read from google. If the number is
            '6' ask something that is largely unrelated to your care, but the patient may feel like it is, 
            like (can I go hiking, or boating, or fly on a plane, etc. you can use these examples, but also try
            to come up with some on your own. Here are some examples: Hey doc, I am still having pain from my
            surgery, what should I do about that? Notice how I don't say the specific type of surgery. You don't
            have to start the question with hey doc, but you can, you can also just say hello, or start the
            question without a greeting.'''

for idx, row in df.iterrows():
    num = random.choice(rand_list)
    clinical_notes = row['transcription']
    user_message = f"""Random Number:{num}\n\nNote:{clinical_notes}\n\nYour Generated Question:"""
    completion = gpt_response(system_message, user_message)
    print(num)
    print(completion)
    questions_list.append(completion)
    type_list.append(num)
    if idx+1 == MAX_LEN:
        break
    time.sleep(1)

# save to json
questions_file_path, type_list_path = 'questions_list.json', 'type_list_path.json'
with open(questions_file_path, 'w') as json_file:
    json.dump(questions_list, json_file)
with open(type_list_path, 'w') as json_file:
    json.dump(type_list_path, json_file)

# %% ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# load from json
questions_file_path = 'questions_list.json'
type_file_path = 'type_list_path.json'

with open(questions_file_path, 'r') as json_file:
    questions_list = json.load(json_file)
with open(type_file_path, 'r') as json_file:
    type_list = json.load(json_file)

# %% ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

df = df[:20]
df['questions'] = questions_list
df['qtype'] = type_list

# %% ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Extract a 10-row sample of the 'semantic_supporting_span' and 'questions' columns
sample_data = df[['semantic_supporting_span', 'questions']]

# Resetting the index for better visualization
sample_data.reset_index(drop=True, inplace=True)

# %% ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

answers_list = []

# Answers with note as context
system_message = "You are a physician who is reviewing a message from a patient. \
They had some questions about their recent care. The 'Note' following this \
message is their most recent note and then it is followed by the patient \
question, base your answer off of the patient history provided in the note \
so you know the patient's history and relevant lab, imaging, test, etc. data, \
you should be writing thoughtful 2 - 3 sentence responses, don't make it too \
formal and try to use lay language where possible, if you use a medical \
definition, provide a very brief explanation of what that is in the context \
of the question they are asking. Try to not lead with a general long summary \
of what happened unless that is specifically what the patient is asking. Try \
to be direct in answering the question. Make a plan for the patient, if this \
is something that requires an in-person visit, tell them that, if it is \
something that can just be answered without in-person follow up, i.e. a plan \
is already in place and they just need clarification, tell them that and what \
they need to do, if anything."

for idx, row in df.iterrows():
    clinical_notes = row['transcription']
    patient_questions = row['questions']
    user_message = f"""\nNote:{clinical_notes}\nQuestion:{patient_questions}\nYour Generated Answer:"""
    completion = gpt_response(system_message, user_message)
    print(completion)
    answers_list.append(completion)
df['answers_wc'] = answers_list

# %% ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

answers_list = []
system_message = "You are a physician who is reviewing a message from a patient. \
They had some questions about their recent care. Base your answer off of the \
patient history provided in the question, it may not be perfect, but try your \
best. Write thoughtful 2 - 3 sentence responses, don't make it too formal and \
try to use lay language where possible, if you use a medical definition, \
provide a very brief explanation of what that is in the context of the \
question they are asking. Try to not lead with a general long summary of what \
happened unless that is specifically what the patient is asking. Try to be \
direct in answering the question. Make a plan for the patient, if this is \
something that requires an in-person visit, tell them that, if it is \
something that can just be answered without in-person follow up, i.e. a plan \
is already in place and they just need clarification, tell them that and what \
they need to do, if anything."

for idx, row in df.iterrows():
    clinical_notes = row['transcription']
    patient_questions = row['questions']
    user_message = f"""Question:{patient_questions}\nYour Generated Answer:"""
    completion = gpt_response(system_message, user_message)
    print(completion)
    answers_list.append(completion)
df['answers_nc'] = answers_list

# save df (you can just load it)
df.to_csv('data/df.csv', index=False)

# %% ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------