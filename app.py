from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

app = Flask(__name__)
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            temperature=0.5,
            max_tokens=150,
            top_p=1,
            stop=None,
            stream=False,
        )
        assistant_message = response.choices[0].message.content
        return jsonify({'message': assistant_message})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
