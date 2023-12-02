from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import json
from datetime import datetime, timedelta
from sqlalchemy import and_

#===========================================================================================
# Configurações inicias do Flask
#===========================================================================================

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'EaYw6a_Szf3ju8llj4HkLA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

#===========================================================================================
# Configurações do Banco de Dados
# Para essa tarefa, usa-se o pacote SQLAlchemy
#===========================================================================================

db = SQLAlchemy() # Responsável por realizar a conexão com o banco de dados
db.init_app(app)  # Inicia a conexão

# Modelo ORM - Aluno
class Aluno(UserMixin, db.Model):
    id = db.Column(db.String(10), primary_key=True)
    plano = db.Column(db.String(100))
    situacao = db.Column(db.String(100))
    nome = db.Column(db.String(100))
    identidade = db.Column(db.String(100))
    nascimento = db.Column(db.String(100))
    genero = db.Column(db.String(100))
    endereco = db.Column(db.String(100))
    numero = db.Column(db.String(100))
    complemento = db.Column(db.String(100))
    cep = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(100))
    situacao_medica = db.Column(db.String(100))
    data_atestado = db.Column(db.String(100))
    observacoes_saude = db.Column(db.String(500))
    senha = db.Column(db.String(100))

# Modelo ORM - Colaborador
class Colaborador(UserMixin, db.Model):
    id = db.Column(db.String(10), primary_key=True)
    cargo = db.Column(db.String(100))
    situacao = db.Column(db.String(100))
    nome = db.Column(db.String(100))
    identidade = db.Column(db.String(100))
    nascimento = db.Column(db.String(100))
    genero = db.Column(db.String(100))
    endereco = db.Column(db.String(100))
    numero = db.Column(db.String(100))
    complemento = db.Column(db.String(100))
    cep = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(100))
    regime_trabalho = db.Column(db.String(100))
    data_contratacao = db.Column(db.String(100))
    observacoes = db.Column(db.String(500))
    senha = db.Column(db.String(100))

# Modelo ORM - Treino
class Treino(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno = db.Column(db.String(100))
    treinador = db.Column(db.String(100))
    status = db.Column(db.String(100))
    data_criacao = db.Column(db.String(100))
    exercicio1_1 = db.Column(db.String(100))
    frequencia1_1 = db.Column(db.String(100))
    carga1_1 = db.Column(db.String(100))
    exercicio1_2 = db.Column(db.String(100))
    frequencia1_2 = db.Column(db.String(100))
    carga1_2 = db.Column(db.String(100))
    exercicio1_3 = db.Column(db.String(100))
    frequencia1_3 = db.Column(db.String(100))
    carga1_3 = db.Column(db.String(100))
    exercicio1_4 = db.Column(db.String(100))
    frequencia1_4 = db.Column(db.String(100))
    carga1_4 = db.Column(db.String(100))
    exercicio1_5 = db.Column(db.String(100))
    frequencia1_5 = db.Column(db.String(100))
    carga1_5 = db.Column(db.String(100))
    exercicio1_6 = db.Column(db.String(100))
    frequencia1_6 = db.Column(db.String(100))
    carga1_6 = db.Column(db.String(100))
    exercicio1_7 = db.Column(db.String(100))
    frequencia1_7 = db.Column(db.String(100))
    carga1_7 = db.Column(db.String(100))
    exercicio1_8 = db.Column(db.String(100))
    frequencia1_8 = db.Column(db.String(100))
    carga1_8 = db.Column(db.String(100))
    exercicio1_9 = db.Column(db.String(100))
    frequencia1_9 = db.Column(db.String(100))
    carga1_9 = db.Column(db.String(100))
    exercicio1_10 = db.Column(db.String(100))
    frequencia1_10 = db.Column(db.String(100))
    carga1_10 = db.Column(db.String(100))
    exercicio2_1 = db.Column(db.String(100))
    frequencia2_1 = db.Column(db.String(100))
    carga2_1 = db.Column(db.String(100))
    exercicio2_2 = db.Column(db.String(100))
    frequencia2_2 = db.Column(db.String(100))
    carga2_2 = db.Column(db.String(100))
    exercicio2_3 = db.Column(db.String(100))
    frequencia2_3 = db.Column(db.String(100))
    carga2_3 = db.Column(db.String(100))
    exercicio2_4 = db.Column(db.String(100))
    frequencia2_4 = db.Column(db.String(100))
    carga2_4 = db.Column(db.String(100))
    exercicio2_5 = db.Column(db.String(100))
    frequencia2_5 = db.Column(db.String(100))
    carga2_5 = db.Column(db.String(100))
    exercicio2_6 = db.Column(db.String(100))
    frequencia2_6 = db.Column(db.String(100))
    carga2_6 = db.Column(db.String(100))
    exercicio2_7 = db.Column(db.String(100))
    frequencia2_7 = db.Column(db.String(100))
    carga2_7 = db.Column(db.String(100))
    exercicio2_8 = db.Column(db.String(100))
    frequencia2_8 = db.Column(db.String(100))
    carga2_8 = db.Column(db.String(100))
    exercicio2_9 = db.Column(db.String(100))
    frequencia2_9 = db.Column(db.String(100))
    carga2_9 = db.Column(db.String(100))
    exercicio2_10 = db.Column(db.String(100))
    frequencia2_10 = db.Column(db.String(100))
    carga2_10 = db.Column(db.String(100))
    exercicio3_1 = db.Column(db.String(100))
    frequencia3_1 = db.Column(db.String(100))
    carga3_1 = db.Column(db.String(100))
    exercicio3_2 = db.Column(db.String(100))
    frequencia3_2 = db.Column(db.String(100))
    carga3_2 = db.Column(db.String(100))
    exercicio3_3 = db.Column(db.String(100))
    frequencia3_3 = db.Column(db.String(100))
    carga3_3 = db.Column(db.String(100))
    exercicio3_4 = db.Column(db.String(100))
    frequencia3_4 = db.Column(db.String(100))
    carga3_4 = db.Column(db.String(100))
    exercicio3_5 = db.Column(db.String(100))
    frequencia3_5 = db.Column(db.String(100))
    carga3_5 = db.Column(db.String(100))
    exercicio3_6 = db.Column(db.String(100))
    frequencia3_6 = db.Column(db.String(100))
    carga3_6 = db.Column(db.String(100))
    exercicio3_7 = db.Column(db.String(100))
    frequencia3_7 = db.Column(db.String(100))
    carga3_7 = db.Column(db.String(100))
    exercicio3_8 = db.Column(db.String(100))
    frequencia3_8 = db.Column(db.String(100))
    carga3_8 = db.Column(db.String(100))
    exercicio3_9 = db.Column(db.String(100))
    frequencia3_9 = db.Column(db.String(100))
    carga3_9 = db.Column(db.String(100))
    exercicio3_10 = db.Column(db.String(100))
    frequencia3_10 = db.Column(db.String(100))
    carga3_10 = db.Column(db.String(100))
    exercicio4_1 = db.Column(db.String(100))
    frequencia4_1 = db.Column(db.String(100))
    carga4_1 = db.Column(db.String(100))
    exercicio4_2 = db.Column(db.String(100))
    frequencia4_2 = db.Column(db.String(100))
    carga4_2 = db.Column(db.String(100))
    exercicio4_3 = db.Column(db.String(100))
    frequencia4_3 = db.Column(db.String(100))
    carga4_3 = db.Column(db.String(100))
    exercicio4_4 = db.Column(db.String(100))
    frequencia4_4 = db.Column(db.String(100))
    carga4_4 = db.Column(db.String(100))
    exercicio4_5 = db.Column(db.String(100))
    frequencia4_5 = db.Column(db.String(100))
    carga4_5 = db.Column(db.String(100))
    exercicio4_6 = db.Column(db.String(100))
    frequencia4_6 = db.Column(db.String(100))
    carga4_6 = db.Column(db.String(100))
    exercicio4_7 = db.Column(db.String(100))
    frequencia4_7 = db.Column(db.String(100))
    carga4_7 = db.Column(db.String(100))
    exercicio4_8 = db.Column(db.String(100))
    frequencia4_8 = db.Column(db.String(100))
    carga4_8 = db.Column(db.String(100))
    exercicio4_9 = db.Column(db.String(100))
    frequencia4_9 = db.Column(db.String(100))
    carga4_9 = db.Column(db.String(100))
    exercicio4_10 = db.Column(db.String(100))
    frequencia4_10 = db.Column(db.String(100))
    carga4_10 = db.Column(db.String(100))
    exercicio5_1 = db.Column(db.String(100))
    frequencia5_1 = db.Column(db.String(100))
    carga5_1 = db.Column(db.String(100))
    exercicio5_2 = db.Column(db.String(100))
    frequencia5_2 = db.Column(db.String(100))
    carga5_2 = db.Column(db.String(100))
    exercicio5_3 = db.Column(db.String(100))
    frequencia5_3 = db.Column(db.String(100))
    carga5_3 = db.Column(db.String(100))
    exercicio5_4 = db.Column(db.String(100))
    frequencia5_4 = db.Column(db.String(100))
    carga5_4 = db.Column(db.String(100))
    exercicio5_5 = db.Column(db.String(100))
    frequencia5_5 = db.Column(db.String(100))
    carga5_5 = db.Column(db.String(100))
    exercicio5_6 = db.Column(db.String(100))
    frequencia5_6 = db.Column(db.String(100))
    carga5_6 = db.Column(db.String(100))
    exercicio5_7 = db.Column(db.String(100))
    frequencia5_7 = db.Column(db.String(100))
    carga5_7 = db.Column(db.String(100))
    exercicio5_8 = db.Column(db.String(100))
    frequencia5_8 = db.Column(db.String(100))
    carga5_8 = db.Column(db.String(100))
    exercicio5_9 = db.Column(db.String(100))
    frequencia5_9 = db.Column(db.String(100))
    carga5_9 = db.Column(db.String(100))
    exercicio5_10 = db.Column(db.String(100))
    frequencia5_10 = db.Column(db.String(100))
    carga5_10 = db.Column(db.String(100))

# Modelo ORM - Aula
class Aula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    treinador = db.Column(db.String(100))
    status = db.Column(db.String(100))
    nome = db.Column(db.String(100))
    ocorre_em = db.Column(db.String(100))
    data_especifica = db.Column(db.String(100))
    hora_inicio = db.Column(db.String(100))
    hora_fim = db.Column(db.String(100))
    quantidade_vagas = db.Column(db.String(100))
    
# Modelo ORM - Reserva
class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aula = db.Column(db.String(100))
    aluno = db.Column(db.String(100))
    data = db.Column(db.String(100))
    
with app.app_context():
    # Cria o banco de dados, caso ele não exista
    db.create_all()
    
    # Cria o perfil dos diretores, caso eles não existam
    colaboradores = Colaborador.query.all()
    if len(colaboradores)==0:
    
        novo_registro = Colaborador(id='C00001', cargo='Diretor', situacao='Ativo', nome='Afonso', email='afonso@oficinadocorpo.com.br', senha=generate_password_hash('movement'))
        db.session.add(novo_registro)
        db.session.commit()
        
        novo_registro = Colaborador(id='C00002', cargo='Diretor', situacao='Ativo', nome='Cláudio', email='claudio@oficinadocorpo.com.br', senha=generate_password_hash('movement'))
        db.session.add(novo_registro)
        db.session.commit()

#===========================================================================================
# Configurações do sistema de login
# Para essa tarefa, usa-se o pacote LoginManager
#===========================================================================================

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message = ''
login_manager.init_app(app)

# Essa função é padrão do LoginManager. 
# A partir dessa função, a função "current_user" do Flask-Login passa estar disponível.
@login_manager.user_loader
def load_user(user_id):
    return Colaborador.query.get(user_id) or Aluno.query.get(user_id)
   

#===========================================================================================
# Configurações das Rotas URL (Autenticação)
#===========================================================================================

# Página de login
@app.route('/login')
def login():
    return render_template('login.html')

# Página de login - POST
@app.route('/login', methods=['POST'])
def login_post():

    # Captura e-mail e senha informados
    email = request.form.get('email')
    password = request.form.get('password')

    user = Colaborador.query.filter_by(email=email).first()
	
    if user != None:
        if user.situacao != 'Ativo': session['perfil'] = 'inativo'
        elif user.cargo == 'Diretor': session['perfil'] = 'diretor'
        elif user.cargo == 'Supervisor Administrativo' : session['perfil'] = 'administrativo'
        elif user.cargo == 'Técnico Administrativo' : session['perfil'] = 'administrativo'
        elif user.cargo == 'Treinador' : session['perfil'] = 'treinador'
        else: session['perfil'] = 'inativo'    
    else:
        user = Aluno.query.filter_by(email=email).first()
        if user!=None: 
            if user.situacao == 'Ativo': session['perfil'] = 'aluno'
            else: session['perfil'] = 'inativo'

    # Checa se o usuário existe
    # A função "check_password_hash" compara a senha informada pelo usuário com a senha do banco de dados (em formato hash)
    if not user or not check_password_hash(user.senha, password):
        flash('Dados incorretos. Tente novamente.')
        return redirect(url_for('login')) # Se o usuário não existir, recarrega a página para apresentar a mensagem flash

    # Caso o usuário exista, mas esteja inativo, redireciona-o de volta à página de login
    if session['perfil'] == 'inativo':
        flash('Seu acesso não está autorizado. Entre em contato com o administrador.')
        return redirect(url_for('login'))

    # Caso o uruário exista, loga o usuário e o redireciona para a página principal (index/raíz)
    login_user(user, remember=False)
    return redirect(url_for('index'))

# Página de logout - POST
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Página de recuperacao de senha
@app.route('/recuperar_senha')
def recuperarSenha():
    email = request.args.get('email')
    aluno = Aluno.query.filter(Aluno.email==email).first()
    colaborador = Colaborador.query.filter(Colaborador.email==email).first()
    
    if aluno: 
        aluno.senha = generate_password_hash('movement')
        db.session.commit()
    if colaborador: 
        colaborador.senha = generate_password_hash('movement')
        db.session.commit()

    return render_template('recuperar-senha.html', email=email)
    
#===========================================================================================
# Configurações das Rotas URL (Gerais)
#===========================================================================================

# Index
@app.route('/')
@login_required
def index():
    return render_template('index.html', name=current_user.nome)

# Página de perfil para alteração de senha 
@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html', name=current_user.nome, migalhas=['Perfil','Alterar senha'])

# Página de perfil para alteração de senha - método Post
@app.route('/perfil', methods=['POST'])
@login_required
def perfil_post():
    senha_atual = request.form.get('senha_atual')
    nova_senha1 = request.form.get('nova_senha1')
    nova_senha2 = request.form.get('nova_senha2')
    
    if check_password_hash(current_user.senha, senha_atual) == False:
        flash('Senha atual incorreta')
        return redirect('/perfil')
        
    if nova_senha1 != nova_senha2:
        flash("Verifique se as senhas digitadas nos campos 'Nova senha' e 'Confirmar nova senha' são iguais")
        return redirect('/perfil')
    
    if session['perfil'] == 'aluno':
        user = Aluno.query.filter_by(id=current_user.id).first()
    else:
        user = Colaborador.query.filter_by(id=current_user.id).first()
    
    user.senha = generate_password_hash(nova_senha1)
    db.session.commit()

    flash("Senha alterada com sucesso")
    return redirect('/perfil')
    
#===========================================================================================
# Configurações das Rotas URL (Alunos)
#===========================================================================================

# Menu >> Alunos >> Cadastrar
@app.route('/aluno/cadastrar')
@login_required
def cadastrarAluno():

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "treinador": return redirect('/')

    contexto = {
    "name":current_user.nome, 
    "migalhas":['Alunos','Cadastrar novo aluno']
    }
    return render_template('Alunos/aluno-cadastrar.html', **contexto)

# Menu >> Alunos >> Cadastrar - método POST
@app.route('/aluno/cadastrar', methods=['POST'])
@login_required
def cadastrarAluno_post():
    
    ultimo_registro = Aluno.query.order_by(Aluno.id.desc()).first()
    
    if ultimo_registro == None:
        ultimo_registro = 1
    else:
        ultimo_registro = int(ultimo_registro.id[1:])
    
    id = ultimo_registro + 1
    id = 'A' + f'{id:05}'
    
    plano = request.form.get('plano')
    situacao = request.form.get('situacao')
    nome = request.form.get('nome')
    identidade = request.form.get('identidade')
    nascimento = request.form.get('nascimento')
    genero = request.form.get('genero')
    endereco = request.form.get('endereco')
    numero = request.form.get('numero')
    complemento = request.form.get('complemento')
    cep = request.form.get('cep')
    cidade = request.form.get('cidade')
    estado = request.form.get('estado')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    situacao_medica = request.form.get('situacao_medica')
    data_atestado = request.form.get('data_atestado')
    observacoes_saude = request.form.get('observacoes_saude')

    senha=generate_password_hash('movement')

    # Verifica se o e-mail já foi cadastrado
    aluno = Aluno.query.filter_by(email=email).first()
    colaborador = Colaborador.query.filter_by(email=email).first()

    if aluno or colaborador:
        flash('O e-mail informado já se encontra cadastrado na base de dados.')
        return redirect('/aluno/cadastrar')
        
    # prepara o registro para ser gravado no banco de dados
    novo_registro = Aluno(id=id, plano=plano, situacao=situacao, nome=nome, identidade=identidade, nascimento=nascimento, genero=genero, endereco=endereco, numero=numero, complemento=complemento, cep=cep, cidade=cidade, estado=estado, email=email, telefone=telefone, situacao_medica=situacao_medica, data_atestado=data_atestado, observacoes_saude=observacoes_saude, senha=senha)

    # grava o registro no banco de dados
    db.session.add(novo_registro)
    db.session.commit()
	
    session['mensagem'] = "Novo aluno cadastrado com sucesso!"
    session['matricula'] = novo_registro.id
    session['nome'] = novo_registro.nome
    return redirect(url_for('cadastroAluno_sucesso'))

# Menu >> Alunos >> Consultar
@app.route('/aluno/consultar')
@login_required
def consultarAluno():
    if session['perfil'] == 'aluno':
        return redirect('/aluno/'+current_user.id)

    contexto = {
    "name":current_user.nome, 
    "migalhas":['Alunos','Consultar cadastro']
    }
    return render_template('Alunos/aluno-consultar.html', **contexto)

# Menu >> Alunos >> Consultar - método POST: Caso se pesquise pela matrícula
@app.route('/aluno/consultar-matricula', methods=['POST'])
@login_required
def consultarAluno_porMatricula_post():
    matricula = request.form.get('matricula')    
    session['matricula'] = matricula.upper()
    session['nome'] = ""
    return redirect(url_for('consultarAluno_listaResultados_post'))

# Menu >> Alunos >> Consultar - método POST: Caso se pesquise pelo nome
@app.route('/aluno/consultar-nome', methods=['POST'])
@login_required
def consultarAluno_porNome_post():
    nome = request.form.get('nome')    
    session['matricula'] = ""
    session['nome'] = nome
    return redirect(url_for('consultarAluno_listaResultados_post'))

#  Menu >> Alunos >> Consultar >> Resultado da consulta
@app.route('/aluno/consultar/lista')
@login_required
def consultarAluno_listaResultados_post():

    if session['perfil'] == "aluno": return redirect('/')

    if session['matricula'] != "":
        matricula = session['matricula']
        alunos = Aluno.query.filter_by(id=matricula)
    else:
        nome = session['nome']
        alunos = Aluno.query.filter(Aluno.nome.contains(nome))
    
    contexto = {
    "name":current_user.nome, 
    "migalhas":['Alunos','Consultar cadastro','Lista de resultados'],
    "alunos":alunos
    }
    
    return render_template('Alunos/aluno-consultar-resultados.html', **contexto)

#  Exibe dados de um determinado aluno
@app.route('/aluno/<matricula>')
@login_required
def dadosAluno_exibir(matricula):

    if session['perfil'] == "aluno" and matricula != current_user.id: return redirect('/')

    aluno = Aluno.query.filter_by(id=matricula).first_or_404()
    contexto = {
    "name":current_user.nome,
    "migalhas":['Alunos','Consultar cadastro','Dados do aluno'],
    "matricula":aluno.id, 
    "plano":aluno.plano, 
    "situacao":aluno.situacao, 
    "nome":aluno.nome, 
    "identidade":aluno.identidade, 
    "nascimento":aluno.nascimento, 
    "genero":aluno.genero, 
    "endereco":aluno.endereco, 
    "numero":aluno.numero, 
    "complemento":aluno.complemento, 
    "cep":aluno.cep, 
    "cidade":aluno.cidade, 
    "estado":aluno.estado, 
    "email":aluno.email, 
    "telefone":aluno.telefone, 
    "situacao_medica":aluno.situacao_medica, 
    "data_atestado":aluno.data_atestado, 
    "observacoes_saude":aluno.observacoes_saude
    }
    return render_template('Alunos/aluno-dados-completos.html', **contexto)

#  Edita dados de um determinado aluno
@app.route('/aluno/<matricula>/editar')
@login_required
def dadosAluno_editar(matricula):

    if session['perfil'] == "treinador": return redirect('/')
    if session['perfil'] == "aluno" and matricula != current_user.id: return redirect('/')

    aluno = Aluno.query.filter_by(id=matricula).first_or_404()
    contexto = {
    "name":current_user.nome,
    "migalhas":['Alunos','Editar cadastro de aluno'],
    "matricula":aluno.id, 
    "plano":aluno.plano, 
    "situacao":aluno.situacao, 
    "nome":aluno.nome, 
    "identidade":aluno.identidade, 
    "nascimento":aluno.nascimento, 
    "genero":aluno.genero, 
    "endereco":aluno.endereco, 
    "numero":aluno.numero, 
    "complemento":aluno.complemento, 
    "cep":aluno.cep, 
    "cidade":aluno.cidade, 
    "estado":aluno.estado, 
    "email":aluno.email, 
    "telefone":aluno.telefone, 
    "situacao_medica":aluno.situacao_medica, 
    "data_atestado":aluno.data_atestado, 
    "observacoes_saude":aluno.observacoes_saude
    }
    return render_template('Alunos/aluno-editar.html', **contexto)

#  Edita dados de um determinado aluno - método POST
@app.route('/aluno/<matricula>/editar', methods=['POST'])
@login_required
def dadosAluno_editar_post(matricula):
    aluno = Aluno.query.filter_by(id=matricula).first()

    if session['perfil']=='aluno':
        aluno.endereco = request.form.get('endereco')
        aluno.numero = request.form.get('numero')
        aluno.complemento = request.form.get('complemento')
        aluno.cep = request.form.get('cep')
        aluno.cidade = request.form.get('cidade')
        aluno.estado = request.form.get('estado')
        aluno.telefone = request.form.get('telefone')
    else:
        aluno.plano = request.form.get('plano')
        aluno.situacao = request.form.get('situacao')
        aluno.nome = request.form.get('nome')
        aluno.identidade = request.form.get('identidade')
        aluno.nascimento = request.form.get('nascimento')
        aluno.genero = request.form.get('genero')
        aluno.endereco = request.form.get('endereco')
        aluno.numero = request.form.get('numero')
        aluno.complemento = request.form.get('complemento')
        aluno.cep = request.form.get('cep')
        aluno.cidade = request.form.get('cidade')
        aluno.estado = request.form.get('estado')
        aluno.email = request.form.get('email')
        aluno.telefone = request.form.get('telefone')
        aluno.situacao_medica = request.form.get('situacao_medica')
        aluno.data_atestado = request.form.get('data_atestado')
        aluno.observacoes_saude = request.form.get('observacoes_saude')
    
    # grava as alterações no banco de dados
    db.session.commit()
	
    session['mensagem'] = "Registro atualizado com sucesso!"
    session['matricula'] = aluno.id
    if session['perfil'] == "aluno":
        session['nome'] = current_user.nome
    else: 
        session['nome'] = request.form.get('nome')
    return redirect(url_for('cadastroAluno_sucesso'))

# Mensagens de sucesso ao cadastrar ou alterar dados do aluno
@app.route('/aluno/cadastrar/sucesso')
@login_required
def cadastroAluno_sucesso():

    if session['perfil'] == "treinador": return redirect('/')

    contexto = {
    "mensagem":session['mensagem'],
    "matricula":session['matricula'],
    "nome":session['nome'], 
    "name":current_user.nome,
    "migalhas":['Alunos','Cadastro de aluno', 'Registro atualizado com sucesso']
    }
    return render_template('cadastro-sucesso.html', **contexto)

# Mensagens de cancelamento de procedimento
@app.route('/aluno/cadastrar/cancelado')
@login_required
def cadastroAluno_cancelado():
    flash('Procedimento de cadastramento cancelado.')
    return redirect('/')
       
#===========================================================================================
# Configurações das Rotas URL (Colaboradores)
#===========================================================================================
    
# Menu >> Colaboradores >> Cadastrar
@app.route('/colaborador/cadastrar')
@login_required
def cadastrarColaborador():

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "treinador": return redirect('/')

    contexto = {
    "name":current_user.nome, 
    "migalhas":['Colaborador','Cadastrar novo colaborador']
    }
    return render_template('Colaboradores/colaborador-cadastrar.html', **contexto)

# Menu >> Colaboradores >> Cadastrar - método POST
@app.route('/colaborador/cadastrar', methods=['POST'])
@login_required
def cadastrarColaborador_post():

    ultimo_registro = Colaborador.query.order_by(Colaborador.id.desc()).first()
    ultimo_registro = int(ultimo_registro.id[1:])
    
    id = ultimo_registro + 1
    id = 'C' + f'{id:05}'

    cargo = request.form.get('cargo')
    situacao = request.form.get('situacao')
    nome = request.form.get('nome')
    identidade = request.form.get('identidade')
    nascimento = request.form.get('nascimento')
    genero = request.form.get('genero')
    endereco = request.form.get('endereco')
    numero = request.form.get('numero')
    complemento = request.form.get('complemento')
    cep = request.form.get('cep')
    cidade = request.form.get('cidade')
    estado = request.form.get('estado')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    regime_trabalho = request.form.get('regime_trabalho')
    data_contratacao = request.form.get('data_contratacao')
    observacoes = request.form.get('observacoes')

    senha=generate_password_hash('movement')

    # Verifica se o e-mail já foi cadastrado
    aluno = Aluno.query.filter_by(email=email).first()
    colaborador = Colaborador.query.filter_by(email=email).first()

    if aluno or colaborador:
        flash('O e-mail informado já se encontra cadastrado na base de dados.')
        return redirect('/colaborador/cadastrar')
        
    # prepara o registro para ser gravado no banco de dados
    novo_registro = Colaborador(id=id, cargo=cargo, situacao=situacao, nome=nome, identidade=identidade, nascimento=nascimento, genero=genero, endereco=endereco, numero=numero, complemento=complemento, cep=cep, cidade=cidade, estado=estado, email=email, telefone=telefone, regime_trabalho=regime_trabalho, data_contratacao=data_contratacao, observacoes=observacoes, senha=senha)

    # grava o novo registro no banco de dados
    db.session.add(novo_registro)
    db.session.commit()
	
    session['mensagem'] = "Novo colaborador cadastrado com sucesso!"
    session['matricula'] = novo_registro.id
    session['nome'] = novo_registro.nome
    return redirect(url_for('cadastroColaborador_sucesso'))

# Menu >> Colaboradores >> Consultar
@app.route('/colaborador/consultar')
@login_required
def consultarColaborador():

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "treinador": return redirect('/')

    contexto = {
    "name":current_user.nome, 
    "migalhas":['Colaboradores','Consultar cadastro']
    }
    return render_template('Colaboradores/colaborador-consultar.html', **contexto)

# Menu >> Colaboradores >> Consultar - método POST: Caso se pesquise pela matrícula
@app.route('/colaborador/consultar-matricula', methods=['POST'])
@login_required
def consultarColaborador_porMatricula_post():
    matricula = request.form.get('matricula')    
    session['matricula'] = matricula.upper()
    session['nome'] = ""
    return redirect(url_for('consultarColaborador_listaResultados_post'))

# Menu >> Colaboradores >> Consultar - método POST: Caso se pesquise pelo nome
@app.route('/colaborador/consultar-nome', methods=['POST'])
@login_required
def consultarColaborador_porNome_post():
    nome = request.form.get('nome')    
    session['matricula'] = ""
    session['nome'] = nome
    return redirect(url_for('consultarColaborador_listaResultados_post'))

#  Menu >> Colaboradores >> Consultar >> Resultado da consulta
@app.route('/colaborador/consultar/lista')
@login_required
def consultarColaborador_listaResultados_post():

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "treinador": return redirect('/')

    if session['matricula'] != "":
        matricula = session['matricula']
        colaboradores = Colaborador.query.filter_by(id=matricula)
    else:
        nome = session['nome']
        colaboradores = Colaborador.query.filter(Colaborador.nome.contains(nome))
    
    contexto = {
    "name":current_user.nome, 
    "migalhas":['Colaboradores','Consultar cadastro','Lista de resultados'],
    "colaboradores":colaboradores
    }
    
    return render_template('Colaboradores/colaborador-consultar-resultados.html', **contexto)

#  Exibe dados de um determinado colaborador
@app.route('/colaborador/<matricula>')
@login_required
def dadosColaborador_exibir(matricula):

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "treinador": return redirect('/')

    colaborador = Colaborador.query.filter_by(id=matricula).first_or_404()
    contexto = {
    "name":current_user.nome,
    "migalhas":['Colaboradores','Consultar cadastro','Dados do colaborador'],
    "matricula":colaborador.id, 
    "cargo":colaborador.cargo, 
    "situacao":colaborador.situacao, 
    "nome":colaborador.nome, 
    "identidade":colaborador.identidade, 
    "nascimento":colaborador.nascimento, 
    "genero":colaborador.genero, 
    "endereco":colaborador.endereco, 
    "numero":colaborador.numero, 
    "complemento":colaborador.complemento, 
    "cep":colaborador.cep, 
    "cidade":colaborador.cidade, 
    "estado":colaborador.estado, 
    "email":colaborador.email, 
    "telefone":colaborador.telefone, 
    "regime_trabalho":colaborador.regime_trabalho, 
    "data_contratacao":colaborador.data_contratacao, 
    "observacoes":colaborador.observacoes
    }
    return render_template('Colaboradores/colaborador-dados-completos.html', **contexto)

#  Edita dados de um determinado colaborador
@app.route('/colaborador/<matricula>/editar')
@login_required
def dadosColaborador_editar(matricula):

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "treinador": return redirect('/')

    colaborador = Colaborador.query.filter_by(id=matricula).first_or_404()
    contexto = {
    "name":current_user.nome,
    "migalhas":['Colaboradores','Editar cadastro de colaborador'],
    "matricula":colaborador.id, 
    "cargo":colaborador.cargo, 
    "situacao":colaborador.situacao, 
    "nome":colaborador.nome, 
    "identidade":colaborador.identidade, 
    "nascimento":colaborador.nascimento, 
    "genero":colaborador.genero, 
    "endereco":colaborador.endereco, 
    "numero":colaborador.numero, 
    "complemento":colaborador.complemento, 
    "cep":colaborador.cep, 
    "cidade":colaborador.cidade, 
    "estado":colaborador.estado, 
    "email":colaborador.email, 
    "telefone":colaborador.telefone, 
    "regime_trabalho":colaborador.regime_trabalho, 
    "data_contratacao":colaborador.data_contratacao, 
    "observacoes":colaborador.observacoes
    }
    return render_template('Colaboradores/colaborador-editar.html', **contexto)

#  Edita dados de um determinado colaborador - método POST
@app.route('/colaborador/<matricula>/editar', methods=['POST'])
@login_required
def dadosColaborador_editar_post(matricula):
    colaborador = Colaborador.query.filter_by(id=matricula).first()

    colaborador.cargo = request.form.get('cargo')
    colaborador.situacao = request.form.get('situacao')
    colaborador.nome = request.form.get('nome')
    colaborador.identidade = request.form.get('identidade')
    colaborador.nascimento = request.form.get('nascimento')
    colaborador.genero = request.form.get('genero')
    colaborador.endereco = request.form.get('endereco')
    colaborador.numero = request.form.get('numero')
    colaborador.complemento = request.form.get('complemento')
    colaborador.cep = request.form.get('cep')
    colaborador.cidade = request.form.get('cidade')
    colaborador.estado = request.form.get('estado')
    colaborador.email = request.form.get('email')
    colaborador.telefone = request.form.get('telefone')
    colaborador.regime_trabalho = request.form.get('regime_trabalho')
    colaborador.data_contratacao = request.form.get('data_contratacao')
    colaborador.observacoes = request.form.get('observacoes')
        
    # grava as alterações no banco de dados
    db.session.commit()
	
    session['mensagem'] = "Registro atualizado com sucesso!"
    session['matricula'] = colaborador.id
    session['nome'] = request.form.get('nome')
    return redirect(url_for('cadastroColaborador_sucesso'))

# Mensagens de sucesso ao cadastrar ou alterar dados do colaborador
@app.route('/colaborador/cadastrar/sucesso')
@login_required
def cadastroColaborador_sucesso():

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "treinador": return redirect('/')

    contexto = {
    "mensagem":session['mensagem'],
    "matricula":session['matricula'],
    "nome":session['nome'], 
    "name":current_user.nome,
    "migalhas":['Colaborador','Cadastro de colaborador', 'Registro atualizado com sucesso']
    }
    return render_template('cadastro-sucesso.html', **contexto)

# Mensagens de cancelamento de procedimento
@app.route('/colaborador/cadastrar/cancelado')
@login_required
def cadastroColaborador_cancelado():
    flash('Procedimento de cadastramento cancelado.')
    return redirect('/')
    
#===========================================================================================
# Configurações das Rotas URL (Treinos)
#===========================================================================================

# Menu >> Treinos >> Cadastrar
@app.route('/treino/cadastrar')
@login_required
def cadastrarTreino():

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "administrativo": return redirect('/')
    
    contexto = {
    "name":current_user.nome, 
    "migalhas":['Treinos','Cadastrar treino']
    }
    return render_template('Treinos/treino-cadastrar-selecionar-aluno.html', **contexto)

# Menu >> Treinos >> Cadastrar - método POST: Caso se pesquise pela matrícula
@app.route('/treino/cadastrar/consultar-matricula', methods=['POST'])
@login_required
def cadastrarTreino_porMatricula_post():
    matricula = request.form.get('matricula')    
    session['matricula'] = matricula.upper()
    session['nome'] = ""
    return redirect(url_for('cadastrarTreino_listaResultados_post'))

# Menu >> Treinos >> Cadastrar - método POST: Caso se pesquise pelo nome
@app.route('/treino/cadastrar/consultar-nome', methods=['POST'])
@login_required
def cadastrarTreino_porNome_post():
    nome = request.form.get('nome')    
    session['matricula'] = ""
    session['nome'] = nome
    return redirect(url_for('cadastrarTreino_listaResultados_post'))

#  Menu >> Treinos >> Cadastrar >> Resultado da consulta (lista de alunos)
@app.route('/treino/cadastrar/lista')
@login_required
def cadastrarTreino_listaResultados_post():

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "administrativo": return redirect('/')

    if session['matricula'] != "":
        matricula = session['matricula']
        alunos = Aluno.query.filter(Aluno.id==matricula, Aluno.situacao=='Ativo')
    else:
        nome = session['nome']
        alunos = Aluno.query.filter(Aluno.nome.contains(nome), Aluno.situacao=='Ativo')
    contexto = {
    "name":current_user.nome, 
    "migalhas":['Treinos','Cadastrar treino','Selecionar aluno'],
    "alunos":alunos
    }
    return render_template('Treinos/treino-cadastrar-resultados.html', **contexto)

#  Abre formulário de cadastro de treino para um determinado aluno
@app.route('/aluno/<matricula>/treino/cadastrar')
@login_required
def cadastrarTreino_aluno(matricula):

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "administrativo": return redirect('/')
    
    aluno = Aluno.query.filter_by(id=matricula).first_or_404()
    treinadores = Colaborador.query.filter(Colaborador.cargo=='Treinador',Colaborador.situacao=='Ativo')
    contexto = {
    "name":current_user.nome,
    "migalhas":['Treino','Cadastrar treino','Inserção de dados'],
    "matricula":aluno.id,
    "nome":aluno.nome
    }
    return render_template('Treinos/treino-cadastrar-formulario.html', **contexto)  

# Abre formulário de cadastro de treino para um determinado aluno - método POST
@app.route('/aluno/<matricula>/treino/cadastrar', methods=['POST'])
@login_required
def cadastrarTreino_aluno_post(matricula):
    aluno = Aluno.query.filter_by(id=matricula).first()
    treinador = current_user.nome
    status = "Ativo"
    data_criacao = datetime.now().strftime('%d/%m/%Y')
    
    exercicio={}
    frequencia={}
    carga={}
    for i in range(1,6):
        for j in range(1,11):
            exercicio[i,j] = request.form.get('exercicio{}_{}'.format(i,j))
            frequencia[i,j] = request.form.get('frequencia{}_{}'.format(i,j))
            carga[i,j] = request.form.get('carga{}_{}'.format(i,j))
       
    # Prepara o registro para ser gravado
    novo_registro = Treino(aluno=aluno.id, treinador=treinador, status=status, data_criacao=data_criacao, exercicio1_1=exercicio[1,1], frequencia1_1=frequencia[1,1], carga1_1=carga[1,1], exercicio1_2=exercicio[1,2], frequencia1_2=frequencia[1,2], carga1_2=carga[1,2], exercicio1_3=exercicio[1,3], frequencia1_3=frequencia[1,3], carga1_3=carga[1,3], exercicio1_4=exercicio[1,4], frequencia1_4=frequencia[1,4], carga1_4=carga[1,4], exercicio1_5=exercicio[1,5], frequencia1_5=frequencia[1,5], carga1_5=carga[1,5], exercicio1_6=exercicio[1,6], frequencia1_6=frequencia[1,6], carga1_6=carga[1,6], exercicio1_7=exercicio[1,7], frequencia1_7=frequencia[1,7], carga1_7=carga[1,7], exercicio1_8=exercicio[1,8], frequencia1_8=frequencia[1,8], carga1_8=carga[1,8], exercicio1_9=exercicio[1,9], frequencia1_9=frequencia[1,9], carga1_9=carga[1,9], exercicio1_10=exercicio[1,10], frequencia1_10=frequencia[1,10], carga1_10=carga[1,10], exercicio2_1=exercicio[2,1], frequencia2_1=frequencia[2,1], carga2_1=carga[2,1], exercicio2_2=exercicio[2,2], frequencia2_2=frequencia[2,2], carga2_2=carga[2,2], exercicio2_3=exercicio[2,3], frequencia2_3=frequencia[2,3], carga2_3=carga[2,3], exercicio2_4=exercicio[2,4], frequencia2_4=frequencia[2,4], carga2_4=carga[2,4], exercicio2_5=exercicio[2,5], frequencia2_5=frequencia[2,5], carga2_5=carga[2,5], exercicio2_6=exercicio[2,6], frequencia2_6=frequencia[2,6], carga2_6=carga[2,6], exercicio2_7=exercicio[2,7], frequencia2_7=frequencia[2,7], carga2_7=carga[2,7], exercicio2_8=exercicio[2,8], frequencia2_8=frequencia[2,8], carga2_8=carga[2,8], exercicio2_9=exercicio[2,9], frequencia2_9=frequencia[2,9], carga2_9=carga[2,9], exercicio2_10=exercicio[2,10], frequencia2_10=frequencia[2,10], carga2_10=carga[2,10], exercicio3_1=exercicio[3,1], frequencia3_1=frequencia[3,1], carga3_1=carga[3,1], exercicio3_2=exercicio[3,2], frequencia3_2=frequencia[3,2], carga3_2=carga[3,2], exercicio3_3=exercicio[3,3], frequencia3_3=frequencia[3,3], carga3_3=carga[3,3], exercicio3_4=exercicio[3,4], frequencia3_4=frequencia[3,4], carga3_4=carga[3,4], exercicio3_5=exercicio[3,5], frequencia3_5=frequencia[3,5], carga3_5=carga[3,5], exercicio3_6=exercicio[3,6], frequencia3_6=frequencia[3,6], carga3_6=carga[3,6], exercicio3_7=exercicio[3,7], frequencia3_7=frequencia[3,7], carga3_7=carga[3,7], exercicio3_8=exercicio[3,8], frequencia3_8=frequencia[3,8], carga3_8=carga[3,8], exercicio3_9=exercicio[3,9], frequencia3_9=frequencia[3,9], carga3_9=carga[3,9], exercicio3_10=exercicio[3,10], frequencia3_10=frequencia[3,10], carga3_10=carga[3,10], exercicio4_1=exercicio[4,1], frequencia4_1=frequencia[4,1], carga4_1=carga[4,1], exercicio4_2=exercicio[4,2], frequencia4_2=frequencia[4,2], carga4_2=carga[4,2], exercicio4_3=exercicio[4,3], frequencia4_3=frequencia[4,3], carga4_3=carga[4,3], exercicio4_4=exercicio[4,4], frequencia4_4=frequencia[4,4], carga4_4=carga[4,4], exercicio4_5=exercicio[4,5], frequencia4_5=frequencia[4,5], carga4_5=carga[4,5], exercicio4_6=exercicio[4,6], frequencia4_6=frequencia[4,6], carga4_6=carga[4,6], exercicio4_7=exercicio[4,7], frequencia4_7=frequencia[4,7], carga4_7=carga[4,7], exercicio4_8=exercicio[4,8], frequencia4_8=frequencia[4,8], carga4_8=carga[4,8], exercicio4_9=exercicio[4,9], frequencia4_9=frequencia[4,9], carga4_9=carga[4,9], exercicio4_10=exercicio[4,10], frequencia4_10=frequencia[4,10], carga4_10=carga[4,10], exercicio5_1=exercicio[5,1], frequencia5_1=frequencia[5,1], carga5_1=carga[5,1], exercicio5_2=exercicio[5,2], frequencia5_2=frequencia[5,2], carga5_2=carga[5,2], exercicio5_3=exercicio[5,3], frequencia5_3=frequencia[5,3], carga5_3=carga[5,3], exercicio5_4=exercicio[5,4], frequencia5_4=frequencia[5,4], carga5_4=carga[5,4], exercicio5_5=exercicio[5,5], frequencia5_5=frequencia[5,5], carga5_5=carga[5,5], exercicio5_6=exercicio[5,6], frequencia5_6=frequencia[5,6], carga5_6=carga[5,6], exercicio5_7=exercicio[5,7], frequencia5_7=frequencia[5,7], carga5_7=carga[5,7], exercicio5_8=exercicio[5,8], frequencia5_8=frequencia[5,8], carga5_8=carga[5,8], exercicio5_9=exercicio[5,9], frequencia5_9=frequencia[5,9], carga5_9=carga[5,9], exercicio5_10=exercicio[5,10], frequencia5_10=frequencia[5,10], carga5_10=carga[5,10])

    # Grava o novo registro no banco de dados
    db.session.add(novo_registro)
    db.session.commit()
	
    session['mensagem'] = "Novo plano de treino cadastrado com sucesso!"
    session['código'] = novo_registro.id
    session['aluno'] = aluno.nome
    session['treinador'] = novo_registro.treinador
    return redirect(url_for('cadastroTreino_sucesso'))
    
# Mensagens de sucesso ao cadastrar ou alterar dados do colaborador
@app.route('/treino/cadastrar/sucesso')
@login_required
def cadastroTreino_sucesso():

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "administrativo": return redirect('/')
    
    contexto = {
    "mensagem":session['mensagem'],
    "aluno":session['aluno'], 
    "treinador":session['treinador'], 
    "name":current_user.nome,
    "migalhas":['Treino','Cadastro de plano de treino', 'Registro atualizado com sucesso']
    }
    return render_template('Treinos/treino-cadastro-sucesso.html', **contexto)

@app.route('/treino/consultar')
@login_required
def consultarTreino():

    if session['perfil'] == "administrativo": return redirect('/')

    if session['perfil'] == 'aluno':
        return redirect('/aluno/'+current_user.id+'/treinos')
    return render_template('Treinos/treino-consultar.html', name=current_user.nome, migalhas=['Treinos','Consultar treino'])
    
# Menu >> Treinos >> Consultar - método POST: Caso se pesquise pela matrícula
@app.route('/treino/consultar-matricula', methods=['POST'])
@login_required
def consultarTreino_porMatricula_post():
    matricula = request.form.get('matricula')    
    session['matricula'] = matricula.upper()
    session['nome'] = ""
    return redirect(url_for('consultarTreino_listaResultados_post'))

# Menu >> Treinos >> Consultar - método POST: Caso se pesquise pelo nome
@app.route('/treino/consultar-nome', methods=['POST'])
@login_required
def consultarTreino_porNome_post():
    nome = request.form.get('nome')    
    session['matricula'] = ""
    session['nome'] = nome
    return redirect(url_for('consultarTreino_listaResultados_post'))

#  Menu >> Treinos >> Consultar >> Resultado da consulta (alunos) 
@app.route('/treino/consultar/lista')
@login_required
def consultarTreino_listaResultados_post():

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "administrativo": return redirect('/')

    if session['matricula'] != "":
        matricula = session['matricula']
        alunos = Aluno.query.filter_by(id=matricula)
    else:
        nome = session['nome']
        alunos = Aluno.query.filter(Aluno.nome.contains(nome),Aluno.situacao=='Ativo')
    
    contexto = {
    "name":current_user.nome, 
    "migalhas":['Treinos','Consultar treino','Selecione o aluno'],
    "alunos":alunos
    }
    
    return render_template('Treinos/treino-consultar-resultados.html', **contexto)
 
#  Menu >> Treinos >> Consultar >> Resultado da consulta (alunos) >> Resultado da consulta (treinos por aluno)
@app.route('/aluno/<matricula>/treinos')
@login_required
def consultarAluno_treinos(matricula):

    if session['perfil'] == "administrativo": return redirect('/')
    if session['perfil'] == "aluno" and matricula != current_user.id: return redirect('/')

    aluno = Aluno.query.filter_by(id=matricula).first()
    treinos = Treino.query.filter_by(aluno=matricula).all()
    contexto = {
    "name":current_user.nome, 
    "migalhas":['Treinos','Consultar treino','Selecione o treino'],
    "aluno":aluno,
    "treinos":treinos
    }
    return render_template('Treinos/treino-consultar-resultados2.html', **contexto)

#  Exibe dados de um determinado treino
@app.route('/treino/<id>')
@login_required
def dadosTreino_exibir(id):

    if session['perfil'] == "administrativo": return redirect('/')

    treino = Treino.query.filter_by(id=id).first_or_404()
    
    if session['perfil'] == "aluno" and treino.aluno != current_user.id: return redirect('/')
    
    aluno_nome = Aluno.query.filter_by(id=treino.aluno).first().nome
    contexto = {
    "name":current_user.nome,
    "migalhas":['Treinos','Consultar treino','Dados do plano de treino'],
    "treino":treino,
    "aluno_nome":aluno_nome
    }
    return render_template('Treinos/treino-dados-completos.html', **contexto)

#  Edita dados de um determinado treino
@app.route('/treino/<codigo>/editar')
@login_required
def dadosTreino_editar(codigo):

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "administrativo": return redirect('/')

    treino = Treino.query.filter_by(id=codigo).first_or_404()
    aluno = Aluno.query.filter_by(id=treino.aluno).first_or_404()
    contexto = {
    "name":current_user.nome,
    "migalhas":['Colaboradores','Editar cadastro de colaborador'],
    "treino":treino,
    "aluno":aluno
    }
    return render_template('Treinos/treino-editar.html', **contexto)

#  Edita dados de um determinado treino - método POST
@app.route('/treino/<codigo>/editar', methods=['POST'])
@login_required
def dadosTreino_editar_post(codigo):
    treino = Treino.query.filter_by(id=codigo).first()

    treino.treinador = current_user.nome
    treino.status = request.form.get('status')

    treino.exercicio1_1 = request.form.get('exercicio1_1')
    treino.frequencia1_1 = request.form.get('frequencia1_1')
    treino.carga1_1 = request.form.get('carga1_1')
    treino.exercicio1_2 = request.form.get('exercicio1_2')
    treino.frequencia1_2 = request.form.get('frequencia1_2')
    treino.carga1_2 = request.form.get('carga1_2')
    treino.exercicio1_3 = request.form.get('exercicio1_3')
    treino.frequencia1_3 = request.form.get('frequencia1_3')
    treino.carga1_3 = request.form.get('carga1_3')
    treino.exercicio1_4 = request.form.get('exercicio1_4')
    treino.frequencia1_4 = request.form.get('frequencia1_4')
    treino.carga1_4 = request.form.get('carga1_4')
    treino.exercicio1_5 = request.form.get('exercicio1_5')
    treino.frequencia1_5 = request.form.get('frequencia1_5')
    treino.carga1_5 = request.form.get('carga1_5')
    treino.exercicio1_6 = request.form.get('exercicio1_6')
    treino.frequencia1_6 = request.form.get('frequencia1_6')
    treino.carga1_6 = request.form.get('carga1_6')
    treino.exercicio1_7 = request.form.get('exercicio1_7')
    treino.frequencia1_7 = request.form.get('frequencia1_7')
    treino.carga1_7 = request.form.get('carga1_7')
    treino.exercicio1_8 = request.form.get('exercicio1_8')
    treino.frequencia1_8 = request.form.get('frequencia1_8')
    treino.carga1_8 = request.form.get('carga1_8')
    treino.exercicio1_9 = request.form.get('exercicio1_9')
    treino.frequencia1_9 = request.form.get('frequencia1_9')
    treino.carga1_9 = request.form.get('carga1_9')
    treino.exercicio1_10 = request.form.get('exercicio1_10')
    treino.frequencia1_10 = request.form.get('frequencia1_10')
    treino.carga1_10 = request.form.get('carga1_10')
    treino.exercicio2_1 = request.form.get('exercicio2_1')
    treino.frequencia2_1 = request.form.get('frequencia2_1')
    treino.carga2_1 = request.form.get('carga2_1')
    treino.exercicio2_2 = request.form.get('exercicio2_2')
    treino.frequencia2_2 = request.form.get('frequencia2_2')
    treino.carga2_2 = request.form.get('carga2_2')
    treino.exercicio2_3 = request.form.get('exercicio2_3')
    treino.frequencia2_3 = request.form.get('frequencia2_3')
    treino.carga2_3 = request.form.get('carga2_3')
    treino.exercicio2_4 = request.form.get('exercicio2_4')
    treino.frequencia2_4 = request.form.get('frequencia2_4')
    treino.carga2_4 = request.form.get('carga2_4')
    treino.exercicio2_5 = request.form.get('exercicio2_5')
    treino.frequencia2_5 = request.form.get('frequencia2_5')
    treino.carga2_5 = request.form.get('carga2_5')
    treino.exercicio2_6 = request.form.get('exercicio2_6')
    treino.frequencia2_6 = request.form.get('frequencia2_6')
    treino.carga2_6 = request.form.get('carga2_6')
    treino.exercicio2_7 = request.form.get('exercicio2_7')
    treino.frequencia2_7 = request.form.get('frequencia2_7')
    treino.carga2_7 = request.form.get('carga2_7')
    treino.exercicio2_8 = request.form.get('exercicio2_8')
    treino.frequencia2_8 = request.form.get('frequencia2_8')
    treino.carga2_8 = request.form.get('carga2_8')
    treino.exercicio2_9 = request.form.get('exercicio2_9')
    treino.frequencia2_9 = request.form.get('frequencia2_9')
    treino.carga2_9 = request.form.get('carga2_9')
    treino.exercicio2_10 = request.form.get('exercicio2_10')
    treino.frequencia2_10 = request.form.get('frequencia2_10')
    treino.carga2_10 = request.form.get('carga2_10')
    treino.exercicio3_1 = request.form.get('exercicio3_1')
    treino.frequencia3_1 = request.form.get('frequencia3_1')
    treino.carga3_1 = request.form.get('carga3_1')
    treino.exercicio3_2 = request.form.get('exercicio3_2')
    treino.frequencia3_2 = request.form.get('frequencia3_2')
    treino.carga3_2 = request.form.get('carga3_2')
    treino.exercicio3_3 = request.form.get('exercicio3_3')
    treino.frequencia3_3 = request.form.get('frequencia3_3')
    treino.carga3_3 = request.form.get('carga3_3')
    treino.exercicio3_4 = request.form.get('exercicio3_4')
    treino.frequencia3_4 = request.form.get('frequencia3_4')
    treino.carga3_4 = request.form.get('carga3_4')
    treino.exercicio3_5 = request.form.get('exercicio3_5')
    treino.frequencia3_5 = request.form.get('frequencia3_5')
    treino.carga3_5 = request.form.get('carga3_5')
    treino.exercicio3_6 = request.form.get('exercicio3_6')
    treino.frequencia3_6 = request.form.get('frequencia3_6')
    treino.carga3_6 = request.form.get('carga3_6')
    treino.exercicio3_7 = request.form.get('exercicio3_7')
    treino.frequencia3_7 = request.form.get('frequencia3_7')
    treino.carga3_7 = request.form.get('carga3_7')
    treino.exercicio3_8 = request.form.get('exercicio3_8')
    treino.frequencia3_8 = request.form.get('frequencia3_8')
    treino.carga3_8 = request.form.get('carga3_8')
    treino.exercicio3_9 = request.form.get('exercicio3_9')
    treino.frequencia3_9 = request.form.get('frequencia3_9')
    treino.carga3_9 = request.form.get('carga3_9')
    treino.exercicio3_10 = request.form.get('exercicio3_10')
    treino.frequencia3_10 = request.form.get('frequencia3_10')
    treino.carga3_10 = request.form.get('carga3_10')
    treino.exercicio4_1 = request.form.get('exercicio4_1')
    treino.frequencia4_1 = request.form.get('frequencia4_1')
    treino.carga4_1 = request.form.get('carga4_1')
    treino.exercicio4_2 = request.form.get('exercicio4_2')
    treino.frequencia4_2 = request.form.get('frequencia4_2')
    treino.carga4_2 = request.form.get('carga4_2')
    treino.exercicio4_3 = request.form.get('exercicio4_3')
    treino.frequencia4_3 = request.form.get('frequencia4_3')
    treino.carga4_3 = request.form.get('carga4_3')
    treino.exercicio4_4 = request.form.get('exercicio4_4')
    treino.frequencia4_4 = request.form.get('frequencia4_4')
    treino.carga4_4 = request.form.get('carga4_4')
    treino.exercicio4_5 = request.form.get('exercicio4_5')
    treino.frequencia4_5 = request.form.get('frequencia4_5')
    treino.carga4_5 = request.form.get('carga4_5')
    treino.exercicio4_6 = request.form.get('exercicio4_6')
    treino.frequencia4_6 = request.form.get('frequencia4_6')
    treino.carga4_6 = request.form.get('carga4_6')
    treino.exercicio4_7 = request.form.get('exercicio4_7')
    treino.frequencia4_7 = request.form.get('frequencia4_7')
    treino.carga4_7 = request.form.get('carga4_7')
    treino.exercicio4_8 = request.form.get('exercicio4_8')
    treino.frequencia4_8 = request.form.get('frequencia4_8')
    treino.carga4_8 = request.form.get('carga4_8')
    treino.exercicio4_9 = request.form.get('exercicio4_9')
    treino.frequencia4_9 = request.form.get('frequencia4_9')
    treino.carga4_9 = request.form.get('carga4_9')
    treino.exercicio4_10 = request.form.get('exercicio4_10')
    treino.frequencia4_10 = request.form.get('frequencia4_10')
    treino.carga4_10 = request.form.get('carga4_10')
    treino.exercicio5_1 = request.form.get('exercicio5_1')
    treino.frequencia5_1 = request.form.get('frequencia5_1')
    treino.carga5_1 = request.form.get('carga5_1')
    treino.exercicio5_2 = request.form.get('exercicio5_2')
    treino.frequencia5_2 = request.form.get('frequencia5_2')
    treino.carga5_2 = request.form.get('carga5_2')
    treino.exercicio5_3 = request.form.get('exercicio5_3')
    treino.frequencia5_3 = request.form.get('frequencia5_3')
    treino.carga5_3 = request.form.get('carga5_3')
    treino.exercicio5_4 = request.form.get('exercicio5_4')
    treino.frequencia5_4 = request.form.get('frequencia5_4')
    treino.carga5_4 = request.form.get('carga5_4')
    treino.exercicio5_5 = request.form.get('exercicio5_5')
    treino.frequencia5_5 = request.form.get('frequencia5_5')
    treino.carga5_5 = request.form.get('carga5_5')
    treino.exercicio5_6 = request.form.get('exercicio5_6')
    treino.frequencia5_6 = request.form.get('frequencia5_6')
    treino.carga5_6 = request.form.get('carga5_6')
    treino.exercicio5_7 = request.form.get('exercicio5_7')
    treino.frequencia5_7 = request.form.get('frequencia5_7')
    treino.carga5_7 = request.form.get('carga5_7')
    treino.exercicio5_8 = request.form.get('exercicio5_8')
    treino.frequencia5_8 = request.form.get('frequencia5_8')
    treino.carga5_8 = request.form.get('carga5_8')
    treino.exercicio5_9 = request.form.get('exercicio5_9')
    treino.frequencia5_9 = request.form.get('frequencia5_9')
    treino.carga5_9 = request.form.get('carga5_9')
    treino.exercicio5_10 = request.form.get('exercicio5_10')
    treino.frequencia5_10 = request.form.get('frequencia5_10')
    treino.carga5_10 = request.form.get('carga5_10')

    # grava as alterações no banco de dados
    db.session.commit()
    
    session['mensagem'] = "Registro atualizado com sucesso!"
    session['aluno'] = Aluno.query.filter_by(id=treino.aluno).first().nome
    session['treinador'] = treino.treinador
    return redirect(url_for('cadastroTreino_sucesso'))  

# Mensagens de cancelamento de procedimento
@app.route('/treino/cadastrar/cancelado')
@login_required
def cadastroTreino_cancelado():
    flash('Procedimento de cadastramento cancelado.')
    return redirect('/')
    
#===========================================================================================
# Configurações das Rotas URL (Aulas)
#===========================================================================================

@app.route('/aula/cadastrar')
@login_required
def cadastrarAula():

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "treinador": return redirect('/')

    treinadores = Colaborador.query.filter(Colaborador.cargo=='Treinador',Colaborador.situacao=='Ativo').all()
    contexto={
    "name":current_user.nome,
    "migalhas":['Aulas','Cadastrar nova aula'],
    "treinadores":treinadores
    }
    return render_template('Aulas/aula-cadastrar.html', **contexto)

@app.route('/aula/cadastrar', methods=['POST'])
@login_required
def cadastrarAula_post():

    treinador = request.form.get('treinador')
    status = request.form.get('status')
    nome = request.form.get('nome')
    ocorre_em = request.form.get('ocorre_em')
    data_especifica = request.form.get('data_especifica')
    hora_inicio = request.form.get('hora_inicio')
    hora_fim = request.form.get('hora_fim')
    quantidade_vagas = request.form.get('quantidade_vagas')
       
    # Prepara o registro para ser gravado no banco de dados
    novo_registro = Aula(treinador=treinador, status=status, nome=nome, ocorre_em=ocorre_em, data_especifica=data_especifica, hora_inicio=hora_inicio, hora_fim=hora_fim, quantidade_vagas=quantidade_vagas)

    # Grava o novo registro no banco de dados
    db.session.add(novo_registro)
    db.session.commit()
	
    session['mensagem'] = "Nova aula cadastrada com sucesso!"
    session['nome'] = novo_registro.nome
    session['treinador'] = novo_registro.treinador
    session['ocorre_em'] = novo_registro.ocorre_em
    session['data_especifica'] = novo_registro.data_especifica
    session['hora_inicio'] = novo_registro.hora_inicio
    session['hora_fim'] = novo_registro.hora_fim
    session['quantidade_vagas'] = novo_registro.quantidade_vagas
    return redirect(url_for('cadastroAula_sucesso'))
    
# Mensagens de sucesso ao cadastrar ou alterar dados da aula
@app.route('/aula/cadastrar/sucesso')
@login_required
def cadastroAula_sucesso():

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "treinador": return redirect('/')

    semana=["Toda segunda-feira", "Toda terça-feira", "Toda quarta-feira", "Toda quinta-feira", "Toda sexta-feira", "Todo sábado"]
    if int(session['ocorre_em']) in range(6):
        session['ocorre_em'] = semana[int(session['ocorre_em'])]
    elif int(session['ocorre_em']) ==9:
        session['ocorre_em'] = session['data_especifica']
    else:
        session['ocorre_em']==session['ocorre_em']
    contexto = {
    "mensagem":session['mensagem'],
    "nome":session['nome'],
    "treinador":session['treinador'], 
    "ocorre_em":session['ocorre_em'], 
    "hora_inicio":session['hora_inicio'], 
    "hora_fim":session['hora_fim'], 
    "quantidade_vagas":session['quantidade_vagas'], 
    "name":current_user.nome,
    "migalhas":['Aulas','Cadastro de nova aula', 'Registro atualizado com sucesso']
    }
    return render_template('Aulas/aula-cadastro-sucesso.html', **contexto)
    
# Menu >> Aulas >> Editar
@app.route('/aula/consultar')
@login_required
def consultarAula():

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "treinador": return redirect('/')

    aulas = Aula.query.order_by(Aula.ocorre_em.asc(), Aula.hora_inicio.asc()).all()
    semana=["Toda segunda-feira", "Toda terça-feira", "Toda quarta-feira", "Toda quinta-feira", "Toda sexta-feira", "Todo sábado"]
    contexto = {
    "name":current_user.nome, 
    "migalhas":['Aulas','Consultar aula', 'Selecionar aula'],
    "aulas":aulas,
    "semana":semana
    }
    return render_template('Aulas/aula-consultar.html', **contexto)

#  Exibe dados de uma determinada aula
@app.route('/aula/<id>')
@login_required
def dadosAula_exibir(id):

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "treinador": return redirect('/')

    aula = Aula.query.filter_by(id=id).first_or_404()
    treinadores = Colaborador.query.filter(Colaborador.cargo=='Treinador',Colaborador.situacao=='Ativo').all()
    semana=["Toda segunda-feira", "Toda terça-feira", "Toda quarta-feira", "Toda quinta-feira", "Toda sexta-feira", "Todo sábado"]
    contexto = {
    "name":current_user.nome,
    "migalhas":['Aulas','Consultar aula','Dados da aula'],
    "aula":aula,
    "treinadores":treinadores,
    "semana":semana
    }
    return render_template('Aulas/aula-dados-completos.html', **contexto)

# Menu >> Aulas >> Atualizar - método POST
@app.route('/aula/<id>', methods=['POST'])
@login_required
def dadosAula_post(id):
    aula = Aula.query.filter_by(id=id).first()
    
    aula.treinador = request.form.get('treinador')
    aula.status = request.form.get('status')
    aula.nome = request.form.get('nome')
    aula.ocorre_em = request.form.get('ocorre_em')
    aula.data_especifica = request.form.get('data_especifica')
    aula.hora_inicio = request.form.get('hora_inicio')
    aula.hora_fim = request.form.get('hora_fim')
    aula.quantidade_vagas = request.form.get('quantidade_vagas')

    db.session.commit()
	
    session['mensagem'] = "Aula atualizada com sucesso!"
    session['nome'] = aula.nome
    session['treinador'] = aula.treinador
    session['ocorre_em'] = aula.ocorre_em
    session['data_especifica'] = aula.data_especifica
    session['hora_inicio'] = aula.hora_inicio
    session['hora_fim'] = aula.hora_fim
    session['quantidade_vagas'] = aula.quantidade_vagas
    return redirect(url_for('cadastroAula_sucesso'))

#  Exclui aula
@app.route('/aula/<id>/delete')
@login_required
def excluiAula(id):

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "treinador": return redirect('/')

    aula = Aula.query.filter_by(id=id).first_or_404()
    db.session.delete(aula)
    db.session.commit()
    
    return redirect(url_for('consultarAula'))

#  Consulta reservas realizadas
@app.route('/aula/<id>/reservas')
@login_required
def reservasRealizadas(id):

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "treinador": return redirect('/')

    hoje = datetime.now()
    hoje = hoje.replace(hour=0, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M:%S')

    reservas = Reserva.query.filter(Reserva.aula==id).filter(Reserva.data>=hoje).order_by(Reserva.data).all()
    
    aula = Aula.query.filter(Aula.id==id).first()
    semana=["Toda segunda-feira", "Toda terça-feira", "Toda quarta-feira", "Toda quinta-feira", "Toda sexta-feira", "Todo sábado"]
    
    if aula.ocorre_em == "9":
        ocorre_em = f'Em {aula.data_especifica[8:10]}/{aula.data_especifica[5:7]}/{aula.data_especifica[0:4]}'
    else:
        ocorre_em = semana[int(aula.ocorre_em)]
    
    datas = []
    alunos = []
    for reserva in reservas:
        datas.append(f'{reserva.data[8:10]}/{reserva.data[5:7]}/{reserva.data[0:4]}')
        alunos.append(Aluno.query.filter(Aluno.id==reserva.aluno).first())
    
    contexto = {
    "name":current_user.nome, 
    "migalhas":['Aulas','Reservas realizadas'],
    'aula':aula,
    'ocorre_em':ocorre_em,
    'datas':datas,
    'alunos':alunos
    }
    return render_template('Aulas/aula-lista-reservas-realizadas.html', **contexto)

# Apresenta Grade semanal de aulas
@app.route('/aulas/grade-semanal')
@login_required
def aulasGradeSemanal():

    if session['perfil'] == "treinador": return redirect('/')
    
    segundas = Aula.query.filter(Aula.ocorre_em=='0').filter(Aula.status=='Ativo').order_by(Aula.hora_inicio.asc()).all()
    tercas = Aula.query.filter(Aula.ocorre_em=='1').filter(Aula.status=='Ativo').order_by(Aula.hora_inicio.asc()).all()
    quartas = Aula.query.filter(Aula.ocorre_em=='2').filter(Aula.status=='Ativo').order_by(Aula.hora_inicio.asc()).all()
    quintas = Aula.query.filter(Aula.ocorre_em=='3').filter(Aula.status=='Ativo').order_by(Aula.hora_inicio.asc()).all()
    sextas = Aula.query.filter(Aula.ocorre_em=='4').filter(Aula.status=='Ativo').order_by(Aula.hora_inicio.asc()).all()
    sabados = Aula.query.filter(Aula.ocorre_em=='5').filter(Aula.status=='Ativo').order_by(Aula.hora_inicio.asc()).all()
    
    contexto = {
    "name":current_user.nome, 
    "migalhas":['Aulas','Grade semanal'],
    'segundas':segundas,
    'tercas':tercas,
    'quartas':quartas,
    'quintas':quintas,
    'sextas':sextas,
    'sabados':sabados
    }
    return render_template('Aulas/grade-semanal.html', **contexto)
    
# Menu >> Aulas >> Reservar
@app.route('/aula/reservar')
@login_required
def reservarAula():

    if session['perfil'] == "treinador": return redirect('/')

    if session['perfil'] == 'aluno':
        return redirect('/aluno/'+current_user.id+'/reservar-aula')
        
    contexto = {
    "name":current_user.nome, 
    "migalhas":['Aulas','Reservar aula']
    }
    return render_template('Aulas/reserva-selecionar-aluno.html', **contexto)

# Menu >> Aulas >> Reserva - método POST: Caso se pesquise pela matrícula
@app.route('/aula/reservar/consultar-matricula', methods=['POST'])
@login_required
def reservarAula_consultarAluno_porMatricula_post():
    matricula = request.form.get('matricula')    
    session['matricula'] = matricula.upper()
    session['nome'] = ""
    return redirect(url_for('reservarAula_consultarAluno_listaResultados'))

# Menu >> Aulas >> Reserva - método POST: Caso se pesquise pelo nome
@app.route('/aula/reservar/consultar-nome', methods=['POST'])
@login_required
def reservarAula_consultarAluno_porNome_post():
    nome = request.form.get('nome')    
    session['matricula'] = ""
    session['nome'] = nome
    return redirect(url_for('reservarAula_consultarAluno_listaResultados'))

#  Menu >> Aulas >> Reservar - Selecionar aluno a partir da lista apresentada 
@app.route('/aula/reservar/selecionar_aluno')
@login_required
def reservarAula_consultarAluno_listaResultados():

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "treinador": return redirect('/')

    if session['matricula'] != "":
        matricula = session['matricula']
        alunos = Aluno.query.filter(Aluno.id==matricula)
    else:
        nome = session['nome']
        alunos = Aluno.query.filter(Aluno.nome.contains(nome),Aluno.situacao=='Ativo')
    contexto = {
    "name":current_user.nome, 
    "migalhas":['Aulas','Reservar aula','Selecione o aluno'],
    "alunos":alunos
    }
    return render_template('Aulas/reserva-selecionar-aluno-lista-resultado.html', **contexto)

#  Menu >> Aulas >> Reservar - Reserva aula para um determinado aluno
@app.route('/aluno/<matricula>/reservar-aula')
@login_required
def reservarAula_selecionarData(matricula):

    if session['perfil'] == "treinador": return redirect('/')
    if session['perfil'] == "aluno" and matricula != current_user.id: return redirect('/')

    aluno = Aluno.query.filter(Aluno.id==matricula).first()
    hoje = datetime.now()
    contexto={
    "name":current_user.nome,
    "migalhas":['Aulas','Reservar aula'],
    "aluno":aluno,
    "hoje":hoje.strftime('%Y-%m-%d')
    }
    return render_template('Aulas/reserva-selecionar-data.html', **contexto)

#  Menu >> Aulas >> Reservar - Reserva aula para um determinado aluno - Método Post
@app.route('/aluno/<matricula>/reservar-aula', methods=['POST'])
@login_required
def reservarAula_selecionarData_post(matricula):

    aluno = Aluno.query.filter(Aluno.id==matricula).first()
    if request.form.get('data') == '':
        flash('Insira uma data válida.')
        return redirect(url_for('reservarAula_selecionarData',matricula=matricula))
        
    data = datetime.strptime(request.form.get('data'), '%Y-%m-%d')
    diaSemana = datetime.weekday(data)
    hoje = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    agora = datetime.now() + timedelta(hours=1)
    
    aulas = Aula.query.filter((Aula.ocorre_em==diaSemana) | (Aula.data_especifica==request.form.get('data'))).filter(Aula.status=="Ativo").order_by(Aula.hora_inicio.asc()).all()
    
    vagas = [] # Armazena informação de vagas disponíveis em cada aula do dia
    for aula in aulas:
        # Calcula quantidade de vagas disponíveis
        vagas_total = aula.quantidade_vagas
        vagas_reservadas = Reserva.query.filter((Reserva.aula==aula.id) | (Reserva.data==request.form.get('data'))).all()
        vagas_disponiveis = int(vagas_total) - len(vagas_reservadas)
        vagas.append(vagas_disponiveis)
    
    semana=["Toda segunda-feira", "Toda terça-feira", "Toda quarta-feira", "Toda quinta-feira", "Toda sexta-feira", "Todo sábado"]
    
    contexto={
    "name":current_user.nome, 
    "migalhas":['Aulas','Reservar aula'], 
    "aluno":aluno,
    "data":data,
    "hoje":hoje,
    "agora":agora,
    "aulas":aulas, 
    "vagas":vagas,
    "semana":semana
    }
    return render_template('Aulas/reserva-lista-aulas-em-determinado-dia.html', **contexto)

# Essa página processa os pedidos de reservas (a partir de parâmetros e argumentos)
@app.route('/aula/<id>/reservar')
@login_required
def reservarAula_dataEspecifica(id):

    if session['perfil'] == "treinador": return redirect('/')

    aluno = request.args.get('aluno')
    data = request.args.get('data')
    
    # Verifica se o registro já existe
    registro_existente = Reserva.query.filter(and_(Reserva.aula == id, Reserva.aluno == aluno, Reserva.data == data)).first()

    if not registro_existente:
        novo_registro = Reserva(aula=id, aluno=aluno, data=data)
        db.session.add(novo_registro)
        db.session.commit()
        flash('Aula reservada com sucesso.')
    else:
        flash('Aula já reservada.')
        
    
    return redirect('/aluno/'+aluno+'/reservas')

# Menu >> Aulas > Consultar reservas
@app.route('/reservas/consultar')
@login_required
def consultarReservas():

    if session['perfil'] == "treinador": return redirect('/')
    
    if session['perfil'] == 'aluno':
        return redirect('/aluno/'+current_user.id+'/reservas')

    contexto={
    "name":current_user.nome, 
    "migalhas":['Aulas','Reservar aula'], 
    }
    return render_template('Aulas/consulta-reserva-selecionar-aluno.html', **contexto)

# Menu >> Aulas > Consultar reservas - Método Post: caso se consulta o aluno pela matrícula
@app.route('/reservas/consultar/consultar-matricula', methods=['POST'])
@login_required
def consultarReservas_consultarAluno_porMatricula_post():
    matricula = request.form.get('matricula')    
    session['matricula'] = matricula.upper()
    session['nome'] = ""
    return redirect(url_for('consultarReservas_consultarAluno_listaResultados'))

# Menu >> Aulas > Consultar reservas - Método Post: caso se consulta o aluno pelo nome
@app.route('/reservas/consultar/consultar-nome', methods=['POST'])
@login_required
def consultarReservas_consultarAluno_porNome_post():
    nome = request.form.get('nome')    
    session['matricula'] = ""
    session['nome'] = nome
    return redirect(url_for('consultarReservas_consultarAluno_listaResultados'))

# Menu >> Aulas > Consultar reservas - apresenta lista de alunos com base na pesquisa realizada
@app.route('/reservas/consultar/selecionar_aluno')
@login_required
def consultarReservas_consultarAluno_listaResultados():

    if session['perfil'] == "aluno": return redirect('/')
    if session['perfil'] == "treinador": return redirect('/')

    if session['matricula'] != "":
        matricula = session['matricula']
        alunos = Aluno.query.filter(Aluno.id==matricula)
    else:
        nome = session['nome']
        alunos = Aluno.query.filter(Aluno.nome.contains(nome),Aluno.situacao=='Ativo')
    contexto = {
    "name":current_user.nome, 
    "migalhas":['Aulas','Consultar reservas','Selecione o aluno'],
    "alunos":alunos
    }
    return render_template('Aulas/consulta-reserva-selecionar-aluno-lista-resultado.html', **contexto)

# Menu >> Aulas > Consultar reservas - apresenta reservas de um determinado aluno
@app.route('/aluno/<matricula>/reservas')
@login_required
def consultarReservas_aluno(matricula):

    if session['perfil'] == "treinador": return redirect('/')
    if session['perfil'] == "aluno" and matricula != current_user.id: return redirect('/')

    aluno = Aluno.query.filter(Aluno.id==matricula).first()
    hoje = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    agora = datetime.now()
    
    reservas = Reserva.query.filter(Reserva.aluno==matricula).order_by(Reserva.data.asc()).all()
    
    ids=[]
    datas=[]
    aulas=[]
    treinadores=[]
    horas_inicio=[]
    horas_fim=[]
    
    cancelar=[] #se pode ou não cancelar a reserva (se a aula já começou, não pode ser mais cancelada)
    for reserva in reservas:
        
        data = datetime.strptime(reserva.data.split()[0], '%Y-%m-%d')
        aula = Aula.query.filter(Aula.id==reserva.aula).first()
        
        if (data>=hoje): 
            ids.append(reserva.id)
            datas.append(reserva.data)
            aulas.append(aula.nome)
            treinadores.append(aula.treinador)
            horas_inicio.append(aula.hora_inicio)
            horas_fim.append(aula.hora_fim)
            
            if (data==hoje):
                inicio_aula = agora.replace(hour=int(aula.hora_inicio[:2]), minute=int(aula.hora_inicio[3:5]))
                if agora >= inicio_aula: cancelar.append("nao")
                else: cancelar.append("sim")
            else:
                cancelar.append("sim")
        
    contexto={
    "name":current_user.nome, 
    "migalhas":['Aulas','Reservar aula'], 
    "aluno":aluno,
    "ids":ids,
    "datas":datas,
    "aulas":aulas,
    "treinadores":treinadores,
    "horas_inicio":horas_inicio,
    "horas_fim":horas_fim,
    "reservas":reservas,
    "cancelar":cancelar
    }
    return render_template('Aulas/consulta-reserva-lista-reservas-do-aluno.html', **contexto)

# Menu >> Aulas > Excluir reservas - exclui reserva
@app.route('/reserva/<id>/delete')
@login_required
def excluiReserva(id):

    if session['perfil'] == "treinador": return redirect('/')

    aluno = request.args.get('aluno')
    reserva = Reserva.query.filter_by(id=id).first_or_404()
    if session['perfil'] == "aluno" and reserva.aluno != current_user.id: return redirect('/')
    
    db.session.delete(reserva)
    db.session.commit()
    
    flash('Reserva cancelada')
    return redirect('/aluno/'+aluno+'/reservas')
