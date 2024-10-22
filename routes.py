@app.route("/products", methods=["GET"])
def get_products_by_name():
    name = request.args.get("name")
    products = Product.find_by_name(name)
    return jsonify([p.serialize() for p in products]), 200
