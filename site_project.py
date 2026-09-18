from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "loja_secret_key_123"


PRODUTOS = [
    {
        'id': 1,
        'nome': 'Castanha do Pará',
        'preco': '12,90',
        'imagem': 'castanhapara.jpg',
    },

    {
        'id': 2,
        'nome': 'Alho Frito',
        'preco': '10,90',
        'imagem': 'alhofrito.jpg',
    },

    {
        'id': 3,
        'nome': 'Fava Branca Graúda',
        'preco': '9,46',
        'imagem': 'favabranca.jpg',
    }
]


@app.route('/')
def home():

    if 'carrinho' not in session:
        session['carrinho'] = []

    total_itens = len(session['carrinho'])

    return render_template(
        'index.html',
        lista_produtos=PRODUTOS,
        total_itens=total_itens
    )


@app.route('/adicionar/<int:produto_id>')
def adicionar_ao_carrinho(produto_id):

    if 'carrinho' not in session:
        session['carrinho'] = []

    for produto in PRODUTOS:

        if produto['id'] == produto_id:

            session['carrinho'].append(produto['nome'])

            session.modified = True

            break

    return redirect(url_for('home'))


@app.route('/limpar')
def limpar_carrinho():

    session['carrinho'] = []

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=8000)