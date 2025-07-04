from flask import Blueprint, jsonify, request
from models.voter import Voter
from extensions import db

voter_bp = Blueprint('voter_bp', __name__, url_prefix='/voters')

@voter_bp.route('', methods=['GET'])
def get_voters():
    voters = Voter.query.all()
    return jsonify([{'id': v.id, 'name': v.name, 'email': v.email, 'has_voted': v.has_voted} for v in voters])

@voter_bp.route('/<int:voter_id>', methods=['GET'])
def get_voter(voter_id):
    voter = Voter.query.get_or_404(voter_id)
    return jsonify({'id': voter.id, 'name': voter.name, 'email': voter.email, 'has_voted': voter.has_voted})

@voter_bp.route('/<int:voter_id>', methods=['DELETE'])
def delete_voter(voter_id):
    voter = Voter.query.get_or_404(voter_id)
    db.session.delete(voter)
    db.session.commit()
    return jsonify({'message': 'Votante eliminado correctamente'})
