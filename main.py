from flask import Flask

app = Flask(__name__)

coockies = []

@app.route("/")
def homepage():
    return "<h1 style='color: blue; text-align: center'>Criador de Cookies</h1>"

# CREATE
@app.route("/create-cookies/<username>")
def create_cookie(username):
    if username not in coockies:
        coockies.append(username)
        return "<h1>Cookie criado!</h1>"
    else:
        return "<h1>Esse usuario já existe</h1>"

# READ
@app.route("/read-cookies")
def read_cookies():
    if coockies == []:
        return "<h1>Nenhum Cookie encontrado</h1>"
    else:
        return coockies
    
# UPDATE
@app.route("/update-cookies/<new_user>/<username>")
def update_cookies(new_user, username):
    if username in coockies:
        x = coockies.index(username)
        coockies.pop(x)
        coockies.insert(x, new_user)
        return "<h1>Usuário atualizado com sucesso</h1>"
    else:
        return "Usuário não encontrado"

# DELETE
@app.route("/clear-cookies")
def clear_cookier():
    coockies.clear()
    return "<h1>Todos os Cookies foram deletados com sucesso!!!</h1>"

@app.route("/delete-cookies/<username>")
def delete_cookie(username):
    if username in coockies:
        coockies.remove(username)
        return "<h1>Cookie de usuário excluído com sucesso!!!</h1>"
    else:
        return "<h1>Usuario não encontrado!</h1>"

if __name__ == "__main__":
    app.run(debug=True)