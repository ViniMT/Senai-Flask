from . import db

class Estudante(db.Model):
    __tablename__ = 'estudantes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=True)
    data_nascimento = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f'<Estudante {self.nome}>'

class Curso(db.Model):
    __tablename__ = 'cursos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    duracao = db.Column(db.Integer, nullable=True)
    preco = db.Column(db.Numeric, nullable=True)
    id_professor = db.Column(db.Integer, db.ForeignKey('professores.id'))

    professor = db.relationship("Professor", backref="cursos")

    def __repr__(self):
        return f'<Curso {self.nome}>'

class Inscricao(db.Model):
    __tablename__ = 'inscricoes'
    id = db.Column(db.Integer, primary_key=True)
    id_estudante = db.Column(db.Integer, db.ForeignKey('estudantes.id'))
    id_curso = db.Column(db.Integer, db.ForeignKey('cursos.id'))
    data_inscricao = db.Column(db.Date, nullable=False)

    estudante = db.relationship("Estudante", backref="inscricoes")
    curso = db.relationship("Curso", backref="inscricoes")

    def __repr__(self):
        return f'<Inscricao Estudante ID {self.id_estudante} Curso ID {self.id_curso}>'

class Professor(db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=True)
    data_admissao = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f'<Professor {self.nome}>'
