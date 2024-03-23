from flask import Flask

app = Flask('petrit_todo_app')


@app.route('/')
def hello():
    return 'Hello, World Petrit Kukaj inlämning försenad :p !'

if __name__ == '__main__':
    app.run(debug=True)
