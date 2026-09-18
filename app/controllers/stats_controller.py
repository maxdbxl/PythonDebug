from flask import jsonify

from app import app
from app.framework.decorators.inject import inject
from app.services.item_service import ItemService
from app.services.user_service import UserService


@app.route('/api/stats')
@inject
def getStats(user_service: UserService, itemService: ItemService):
    return jsonify({
        'users': user_service.count(),
        'items': itemService.count()
    })
