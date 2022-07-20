from flask import render_template, redirect, url_for, flash, request, abort
from comunidadeimpressionadora import app, database, bcrypt
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta, FormEditarPerfil, FormCriarPost
from comunidadeimpressionadora.models import Usuario, Post
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image

@app.route('/')
def home():
    posts = Post.query.order_by(Post.id.desc())
    return render_template('home.html', posts=posts)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/users')
@login_required
def users():
    lista_users = Usuario.query.all()
    return render_template('users.html', lista_users=lista_users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()

    if form_login.validate_on_submit() and 'botao_submit' in request.form:#Essa última parte da verificação do submit não seria necessária pois eu estou separando a página de login e criar e conta, mais fica para didática
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_me.data)
        #Fez Login com sucesso
            flash(f'Login feito com sucesso {form_login.email.data}', 'alert-success')
            par_next = request.args.get('next')
            if par_next:
                return redirect(par_next)
            else:
                return redirect(url_for('home'))
        else:
            flash(f'Falha no login, e-mail ou senha incorretos no e-mail: {form_login.email.data}', 'alert-danger')
    return render_template('login.html', form_login=form_login)

@app.route('/criar_conta', methods=['GET', 'POST'])
def criarconta():
    form_criar_conta = FormCriarConta()

    if form_criar_conta.validate_on_submit() and 'botao_submit' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criar_conta.senha.data)
        usuario = Usuario(username=form_criar_conta.username.data, email=form_criar_conta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        #Criou a Conta com sucesso
        flash(f'Conta criada com sucesso feito com sucesso {form_criar_conta.username.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('criarconta.html', form_criar_conta=form_criar_conta)

@app.route('/sair')
@login_required
def sair():
    logout_user()
    return redirect(url_for('home'))

@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('perfil.html', foto_perfil=foto_perfil)

@app.route('/post/criar', methods=['GET', 'POST'])
@login_required
def criar_post():
    form_criar_post = FormCriarPost()

    if form_criar_post.validate_on_submit():
        post = Post(titulo=form_criar_post.titulo.data, corpo=form_criar_post.corpo.data, autor=current_user)
        database.session.add(post)
        database.session.commit()
        flash('Post Feito com Sucesso', 'alert-success')
        return redirect(url_for('home'))

    return render_template('criarpost.html', form_criar_post=form_criar_post)


#Adicionar um código aleátorio ao nome da imagem
#Reduzir o tamanho da imagem
#Salvar a imagem na pasta fotos_perfil
#Mudar o campo foto_perfil do usuário para o novo nome da imagem
def salvar_imagem(imagem):
    codigo = secrets.token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    nome_arquivo = nome + codigo + extensao
    caminho_completo = os.path.join(app.root_path, 'static/fotos_perfil', nome_arquivo)
    tamanho = (200, 200)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho)
    imagem_reduzida.save(caminho_completo)

    return nome_arquivo

def atualizar_cursos(form):
    lista_cursos = []
    for campo in form:
        if 'curso_' in campo.name:
            if campo.data:
                lista_cursos.append(campo.label.text)
    return '; '.join(lista_cursos)

@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    form_editar_perfil = FormEditarPerfil()

    if form_editar_perfil.validate_on_submit():
        current_user.email = form_editar_perfil.email.data
        current_user.username = form_editar_perfil.username.data
        if form_editar_perfil.foto_perfil.data:
            nome_imagem = salvar_imagem(form_editar_perfil.foto_perfil.data)
            current_user.foto_perfil = nome_imagem
        current_user.cursos = atualizar_cursos(form_editar_perfil)
        database.session.commit()
        flash(f'Perfil atualizado com sucesso {form_editar_perfil.username.data}', 'alert-success')
        return redirect(url_for('perfil'))
    elif request.method == 'GET':
        form_editar_perfil.email.data = current_user.email
        form_editar_perfil.username.data = current_user.username
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('editarperfil.html', foto_perfil=foto_perfil, form_editar_perfil=form_editar_perfil)


@app.route('/post/<post_id>', methods=['GET', 'POST'])
@login_required
def exibir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor:
        form_post = FormCriarPost()
        if request.method == 'GET':
            form_post.titulo.data = post.titulo
            form_post.corpo.data = post.corpo
        elif form_post.validate_on_submit():
            post.titulo = form_post.titulo.data
            post.corpo = form_post.corpo.data
            database.session.commit()
            flash('Post atualizado com sucesso!', 'alert-success')
            return redirect(url_for('home'))
    else:
        form_post = None

    return render_template('post.html', post=post, form_post=form_post)


@app.route('/post/<post_id>/excluir', methods=['GET', 'POST'])
@login_required
def excluir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor:
        database.session.delete(post)
        database.session.commit()
        flash('Post excluído com sucesso!', 'alert-danger')
        return redirect(url_for('home'))
    else:
        abort(403)

