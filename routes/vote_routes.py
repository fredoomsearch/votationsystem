from flask import Blueprint, jsonify, request
from models.vote import Vote
from models.voter import Voter
from models.candidate import Candidate
from extensions import db

vote_bp = Blueprint('vote_bp', __name__, url_prefix='/votes')

@vote_bp.route('', methods=['GET'])
def get_votes():
    votes = Vote.query.all()
    return jsonify([{'id': v.id, 'voter_id': v.voter_id, 'candidate_id': v.candidate_id} for v in votes])

@vote_bp.route('/statistics', methods=['GET'])
def statistics():
    total_votes = Vote.query.count()
    results = []
    candidates = Candidate.query.all()
    for c in candidates:
        percent = round((c.votes / total_votes * 100), 2) if total_votes else 0
        results.append({'candidate': c.name, 'votes': c.votes, 'percent': percent})
    voters_voted = Voter.query.filter_by(has_voted=True).count()
    return jsonify({'total_votes': total_votes, 'voters_voted': voters_voted, 'results': results})

@vote_bp.route('', methods=['POST'])
def cast_vote():
    data = request.json
    voter_id = data.get('voter_id')
    candidate_id = data.get('candidate_id')
    voter = Voter.query.get(voter_id)
    candidate = Candidate.query.get(candidate_id)

    if not voter or not candidate:
        return jsonify({'error': 'Votante o candidato inválido'}), 400
    if voter.has_voted:
        return jsonify({'error': 'Este votante ya ha votado'}), 400

    voter.has_voted = True
    candidate.votes += 1
    new_vote = Vote(voter_id=voter_id, candidate_id=candidate_id)
    db.session.add(new_vote)
    db.session.commit()
    return jsonify({'message': 'Voto emitido exitosamente'})
