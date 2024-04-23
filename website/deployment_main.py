from flask import Flask, jsonify, render_template, request, session
import os
import uuid
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.secret_key = 'mistral-key'

# Initialize Mistral Client
client = MistralClient(api_key=os.getenv("mistral-key"))
model = "open-mistral-7b"


@app.route('/')
def home():
  if 'conversations' not in session:
    session['conversations'] = []
  return render_template('index.html', conversations=session['conversations'])


@app.route('/general_summary', methods=['POST'])
def general_summary():
  user_input = request.form['user_input']
  conversation_id = request.form['conversation_id']
  if 'conversations' not in session:
    session['conversations'] = []

  if conversation_id == 'new':
    conversation_id = str(uuid.uuid4())
    session['conversations'].append({'id': conversation_id, 'messages': []})

  conversation = next(
      (c for c in session['conversations'] if c['id'] == conversation_id),
      None)
  if conversation is not None:
    conversation['messages'].append({'role': 'user', 'content': user_input})

    # Define your system prompt here
    system_prompt = "Do not guess the input's title. This assistant is a friendly and knowledgeable poetry guide for children. Its main goal is to help young readers understand and appreciate the beauty of poems by providing clear, concise, and engaging summaries. It focuses exclusively on discussing poems, their themes, language, and the emotions they evoke. The assistant avoids answering questions that are not related to poetry. When engaging with users, it uses simple language suited for children to make poetry more accessible and enjoyable."

    # Add the system prompt as the first message (if not already present)
    if not conversation['messages'][0]['content'] == system_prompt:
      conversation['messages'].insert(0, {
          'role': 'system',
          'content': system_prompt
      })

    messages = [
        ChatMessage(role=msg['role'], content=msg['content'])
        for msg in conversation['messages']
    ]
    chat_response = client.chat(model=model, messages=messages)
    assistant_response = chat_response.choices[0].message.content

    conversation['messages'].append({
        'role': 'assistant',
        'content': assistant_response
    })
    session.modified = True
    return jsonify({
        'response': assistant_response,
        'conversation_id': conversation_id
    })
  else:
    return jsonify({'error': 'Conversation not found'}), 404


@app.route('/line_by_line', methods=['POST'])
def line_by_line():

  logging.info('Processing line-by-line summary')
  user_input = request.form['user_input']
  conversation_id = request.form['conversation_id']
  if 'conversations' not in session:
    session['conversations'] = []

  if conversation_id == 'new':
    conversation_id = str(uuid.uuid4())
    session['conversations'].append({'id': conversation_id, 'messages': []})

  conversation = next(
      (c for c in session['conversations'] if c['id'] == conversation_id),
      None)
  if conversation is not None:
    conversation['messages'].append({'role': 'user', 'content': user_input})

    # Define your system prompt here
    system_prompt = "Convert each line of the poem into simple english that a child could understand. Explain any relevant metaphors, tones, or themes. Also explain how this line contributes to the overall meaning of the poem. Begin each with the line you are currently summarizing like 'Line 1: '. Use simple language that is easy to understand for children."

    # Add the system prompt as the first message (if not already present)
    if not conversation['messages'][0]['content'] == system_prompt:
      conversation['messages'].insert(0, {
          'role': 'system',
          'content': system_prompt
      })

    messages = [
        ChatMessage(role=msg['role'], content=msg['content'])
        for msg in conversation['messages']
    ]
    chat_response = client.chat(model=model, messages=messages)
    assistant_response = chat_response.choices[0].message.content

    conversation['messages'].append({
        'role': 'assistant',
        'content': assistant_response
    })
    session.modified = True
    return jsonify({
        'response': assistant_response,
        'conversation_id': conversation_id
    })
  else:
    return jsonify({'error': 'Conversation not found'}), 404


@app.route('/history', methods=['GET'])
def history():
  conversation_id = request.args.get('conversation_id')
  if 'conversations' not in session:
    return jsonify({'error': 'No conversations found'}), 404
  conversation = next(
      (c for c in session['conversations'] if c['id'] == conversation_id),
      None)
  if conversation is not None:
    return jsonify({'history': conversation['messages']})
  else:
    return jsonify({'error': 'Conversation not found'}), 404


if __name__ == '__main__':
  app.run(debug=True)
