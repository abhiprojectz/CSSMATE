from flask import Flask, render_template , redirect , url_for, request
from flask import jsonify
from txtai.embeddings import Embeddings

# Create embeddings model, backed by sentence-transformers & transformers
embeddings = Embeddings({"method": "transformers", "path": "sentence-transformers/bert-base-nli-mean-tokens"})
app = Flask(__name__)

from conversions import rules


def getcode(response):
  for i in rules:
    if response in i:
      return i[-1]

sections = []

for i in rules:
  for t in i[:-1]:
      sections.append(t)



def bot_response(t):
	userinput = t 
	embeddings.index([(uid, text, None) for uid, text in enumerate(sections)])
	uid = embeddings.search(userinput, 1)[0][0]
	print(sections[uid])
	response = getcode(sections[uid])
	template = f'<html><head><link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet"></head> <body> {response} </body></html>'
	print(template)
	return template

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/codegen', methods=['POST'])
def codegen():
    sen = request.get_json()
    print(sen['data'])
    pem = sen['data']
    text = bot_response(pem)
    ata = {'name':text}
    return jsonify(ata)



if __name__ == '__main__':
   app.run(debug=True)