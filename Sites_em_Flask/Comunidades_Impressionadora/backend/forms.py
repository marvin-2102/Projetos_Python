from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):#Criando uma sublcasse da classe "FlaskForm
    username = StringField('Nome de Usuário:', validators=[DataRequired()])
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha:', validators=[DataRequired(), Length(6, 20)])
    confirmacao = PasswordField('Confirmar Senha:', validators=[DataRequired(), EqualTo('senha')])
    botao_submit = SubmitField('Criar Conta', validators=[])

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Email já está sendo usado, faça login ou use outro email para criar a conta')

class FormLogin(FlaskForm):
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha:', validators=[DataRequired(), Length(6, 20)])
    lembrar_me = BooleanField('Lembrar dados de acesso')
    botao_submit = SubmitField('Login')

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário:', validators=[DataRequired()])
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar a foto de perfil', validators=[FileAllowed(['jpg', 'png'], message='Tipo de arquivo não permitido! Use um jpg ou png')])
    curso_excel = BooleanField('Excel Impressionador')
    curso_vba = BooleanField('VBA Impressionador')
    curso_powerbi = BooleanField('PowerBi Impressionador')
    curso_python = BooleanField('Python Impressionador')
    curso_ppt = BooleanField('PPT Impressionador')
    curso_sql = BooleanField('SQL Impressionador')
    botao_submit = SubmitField('Confirmar Edição!')

    def validate_email(self, email):
        #verifica se o email mudou
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Email já está sendo usado, use outro endereço de e-mail')


class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post:', validators=[DataRequired(), Length(2, 200)])
    corpo = TextAreaField('Escreva aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post!')