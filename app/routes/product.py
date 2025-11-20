from flask import Blueprint, request
from app.utils import build_response, product_not_found_response

# 블루 프린트 정의
product_bp = Blueprint('product', __name__, url_prefix='/products')

product_db = {
    "1": {
        "id": "1",
        "category": "Electronics",
        "registration_date": "2025-11-20",
        "name": "Product A",
        "price": "10.99"
    }
}


##POST2 물건 등록
@product_bp.route('/', methods=['POST'])
def create_product():
    body = request.get_json()
    
    ## [ERROR]: product_db의 body 형식을 맞추지 않은 경우 (400)
    if not body or 'id' not in body or 'category' not in body or 'registration_date' not in body or 'name' not in body or 'price' not in body:
        return build_response(status="fail", code=400, message="Invalid request body")
    
    product_id = body['id']
    product_db[product_id] = body
    return build_response(status="success", code=201, message="Product created", data=product_db)

##PUT2 물건 정보 수정
@product_bp.route('/<product_id>', methods=['PUT'])
def discount_product(product_id):
    body = request.get_json()
   
    ## [ERROR]: product_db의 body 형식을 맞추지 않은 경우 (400)
    if not body or 'id' not in body or 'category' not in body or 'registration_date' not in body or 'name' not in body or 'price' not in body:
        return build_response(status="fail", code=400, message="Invalid request body")
   
    ## [ERROR]: product가 존재하지 않은 경우 (404)
    if product_id not in product_db:
        return product_not_found_response()
    
    product_db[product_id].update(body)
    return build_response(status="success", code=200, message="Product updated", data=product_db[product_id])


##DELETE2 물건 정보 삭제
@product_bp.route('/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id not in product_db:
        return product_not_found_response()
    
    del product_db[product_id]
    return build_response(status="success", code=204)





    