from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager
from extensions import db, login_manager
from models.user import User
from routes.voter_routes import voter_bp
from routes.candidate_routes import candidate_bp
from routes.vote_routes import vote_bp
from routes.auth_routes import auth_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init extensions
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth_bp.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    from models import voter, candidate, vote, user
    db.create_all()

app.register_blueprint(voter_bp)
app.register_blueprint(candidate_bp)
app.register_blueprint(vote_bp)
app.register_blueprint(auth_bp)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register-voter', methods=['GET', 'POST'])
def register_voter():
    from models.voter import Voter
    from models.candidate import Candidate

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        if Candidate.query.filter_by(name=name).first():
            flash('Este usuario está registrado como candidato.')
        elif Voter.query.filter_by(email=email).first():
            flash('El correo ya existe.')
        else:
            new_voter = Voter(name=name, email=email)
            db.session.add(new_voter)
            db.session.commit()
            flash('Votante registrado exitosamente.')
            return redirect(url_for('index'))
    return render_template('register_voter.html')

@app.route('/register-candidate', methods=['GET', 'POST'])
def register_candidate():
    from models.candidate import Candidate
    from models.voter import Voter

    if request.method == 'POST':
        name = request.form['name']
        party = request.form['party']
        if Voter.query.filter_by(name=name).first():
            flash('Este usuario está registrado como votante.')
        else:
            new_candidate = Candidate(name=name, party=party)
            db.session.add(new_candidate)
            db.session.commit()
            flash('Candidato registrado exitosamente.')
            return redirect(url_for('index'))
    return render_template('register_candidate.html')

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    from models.voter import Voter
    from models.candidate import Candidate
    from models.vote import Vote

    if request.method == 'POST':
        voter_id = request.form['voter_id']
        candidate_id = request.form['candidate_id']
        voter = Voter.query.get(voter_id)
        candidate = Candidate.query.get(candidate_id)
        if not voter or not candidate:
            flash('Votante o candidato inválido.')
        elif voter.has_voted:
            flash('Este votante ya ha votado.')
        else:
            voter.has_voted = True
            candidate.votes += 1
            new_vote = Vote(voter_id=voter_id, candidate_id=candidate_id)
            db.session.add(new_vote)
            db.session.commit()
            flash('Voto emitido exitosamente.')
            return redirect(url_for('index'))

    voters = Voter.query.filter_by(has_voted=False).all()
    candidates = Candidate.query.all()
    return render_template('vote.html', voters=voters, candidates=candidates)

@app.route('/statistics')
def statistics():
    from models.candidate import Candidate
    from models.vote import Vote
    from models.voter import Voter

    total_votes = Vote.query.count()
    voters_voted = Voter.query.filter_by(has_voted=True).count()
    stats = []
    for c in Candidate.query.all():
        percent = round((c.votes / total_votes * 100), 2) if total_votes else 0
        stats.append({'name': c.name, 'votes': c.votes, 'percent': percent})
    return render_template('statistics.html', stats=stats, total_votes=total_votes, voters_voted=voters_voted)

if __name__ == "__main__":
    app.run(debug=True)
