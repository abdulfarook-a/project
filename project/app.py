from flask import Flask, render_template, request

app = Flask(__name__)

# FLAMES Logic
def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    combined = list(name1 + name2)

    for char in name1:
        if char in name2:
            combined.remove(char)
            name2 = name2.replace(char, '', 1)

    count = len(combined)
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    
    return flames[0]

# Meaning for FLAMES
def flames_meaning(result):
    meanings = {
        'F': 'Friends',
        'L': 'Lovers',
        'A': 'Affectionate',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings'
    }
    return meanings[result]

@app.route('/')
def home():
    return render_template('flames.html')

@app.route('/calculate_flames', methods=['POST'])
def calculate_flames():
    name1 = request.form['name1']
    name2 = request.form['name2']
    
    result = flames_game(name1, name2)
    meaning = flames_meaning(result)
    
    return render_template('flames.html', result=result, meaning=meaning)

if __name__ == '__main__':
    app.run(debug=True)
