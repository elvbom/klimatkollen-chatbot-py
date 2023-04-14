import openai
import gradio as gr

openai.api_key = "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"

messages = [{
    'role': 'system',
    'content': 'You are a kind and helpful AI assistant named Resa reko that is specialized in sustainable travel in '
               'Sweden. You only answer queries related to traveling Sweden either by bus, train or car, or hotels or '
               'activities in Sweden. You only speak Swedish.',
}]


def chatbot(query):
    if query:
        messages.append({
            'role': 'user',
            'content': query
        })

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        reply = chat.choices[0].message.content

        messages.append({
            'role': 'assistant',
            'content': reply})

        return reply


inputs = gr.inputs.Textbox(lines=7, label="Chatta med Resa reko")
outputs = gr.outputs.Textbox(label="Svara")

gr.Interface(fn=chatbot,
             inputs=inputs,
             outputs=outputs,
             title="Resa reko - AI-boten",
             description="Fråga mig om resor i Sverige",
             theme="compact") \
    .launch(share=True)
