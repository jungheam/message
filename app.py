from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('friends'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port= 5000, debug=True)


@app.route('/friends', methods=["GET", "POST"]) #친구목록
def friends():
    return render_template('friends.html')
@app.route('/chats') #채팅목록
def chats():
    return render_template('chats.html')
@app.route('/chat') #채팅방
def chat():
    return render_template('chat.html')

