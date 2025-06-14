from flask import Flask

app = Flask(__name__)

cookies = []

@app.route("/")
def homepage():
    return "<h1 style='color: blue; text-align: center'>Criador de Cookies</h1>"

# CREATE
@app.route("/create-cookies/<username>")
def create_cookie(username):
    if username not in cookies:
        cookies.append(username)
        return "<h1>Cookie criado!</h1>"
    else:
        return "<h1>Esse usuario já existe</h1>"

# READ
@app.route("/read-cookies")
def read_cookies():
    if cookies == []:
        return "<h1>Nenhum Cookie encontrado</h1>"
    else:
        return cookies
    
# UPDATE
@app.route("/update-cookies/<new_user>/<username>")
def update_cookies(new_user, username):
    if username in cookies:
        x = cookies.index(username)
        cookies.pop(x)
        cookies.insert(x, new_user)
        return "<h1>Usuário atualizado com sucesso</h1>"
    else:
        return "Usuário não encontrado"

# DELETE
@app.route("/clear-cookies")
def clear_cookier():
    cookies.clear()
    return "<h1>Todos os Cookies foram deletados com sucesso!!!</h1>"

@app.route("/delete-cookies/<username>")
def delete_cookie(username):
    if username in cookies:
        cookies.remove(username)
        return "<h1>Cookie de usuário excluído com sucesso!!!</h1>"
    else:
        return "<h1>Usuario não encontrado!</h1>"

if __name__ == "__main__":
    app.run(debug=True)