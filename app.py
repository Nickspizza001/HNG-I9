from flask import Flask, request
from api import API_KEY
import openai

app = Flask(__name__)

stringUsername = "Damibod"
Boolean = True
Integer = 21
stringBio = "Ready to learn"

json_response ={
    "slackUsername": stringUsername,
    "backend": Boolean,
    "age": Integer,
    "bio": stringBio

}
@app.route("/hng", methods=['GET'])
def hng():
    return json_response

@app.route("/hng2", methods=['POST'])
def hng2():
    def do_openai(request):
        openai.api_key = API_KEY
        prompt = request
        response = openai.Completion.create(engine='text-davinci-002', prompt = prompt+" , Print only anwser", max_tokens=6)
        return response
    operators = ['addition', 'subtraction', 'multiplication']
  
    if request.json:

        requestAll = request.json
        requestX = requestAll['x']
        requestY = requestAll['y']
        print(requestAll['operation_type'])
        
        if requestAll['operation_type'] in operators:
            if requestAll['operation_type'] == 'addition':
                anwser = requestX + requestY
                json_anwser = {
                    'slackUsername': 'Damibod',
                    'result': int(anwser),
                    'operation_type': requestAll['operation_type']
                }
                return json_anwser

            elif requestAll['operation_type'] == 'subtraction':
                anwser = requestX - requestY
                json_anwser = {
                    'slackUsername': 'Damibod',
                    'result': int(anwser),
                    'operation_type': requestAll['operation_type']
                }
                return json_anwser
            elif requestAll['operation_type'] == 'multiplication':
                anwser = requestX * requestY
                json_anwser = {
                    'slackUsername': 'Damibod',
                    'result': int(anwser),
                    'operation_type': requestAll['operation_type']
                    
                }
                return json_anwser
        else:
                      
            result = do_openai(requestAll['operation_type'])
            print(result)
            result = result['choices'][0]['text'].strip()
            json_anwser = {
                    'slackUsername': 'Damibod',
                    'result': int(result),
                    'operation_type': requestAll['operation_type']           
                      }
            return json_anwser

       

        
        #use openai for the bonus

if __name__ == "__main__":
    
    app.run(debug=True)