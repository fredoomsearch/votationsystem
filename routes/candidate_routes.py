from flask import Blueprint, jsonify, request
from models.candidate import Candidate
from extensions import db

candidate_bp = Blueprint('candidate_bp', __name__, url_prefix='/candidates')

@candidate_bp.route('', methods=['GET'])
def get_candidates():
    candidates = Candidate.query.all()
    return jsonify([{'id': c.id, 'name': c.name, 'party': c.party, 'votes': c.votes} for c in candidates])

@candidate_bp.route('/<int:candidate_id>', methods=['GET'])
def get_candidate(candidate_id):
    candidate = Candidate.query.get_or_404(candidate_id)
    return jsonify({'id': candidate.id, 'name': candidate.name, 'party': candidate.party, 'votes': candidate.votes})

@candidate_bp.route('/<int:candidate_id>', methods=['DELETE'])
def delete_candidate(candidate_id):
    candidate = Candidate.query.get_or_404(candidate_id)
    db.session.delete(candidate)
    db.session.commit()
    return jsonify({'message': 'Candidato eliminado correctamente'})
