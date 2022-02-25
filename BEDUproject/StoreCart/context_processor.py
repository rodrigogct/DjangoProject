def cart_total(request):
    total = 0
    if request.user.is_authenticated:

        if 'cart' in request.session:
            for key, value in request.session["cart"].items():
                total = total+(float(value["price"])*value["amount"])
    return {"cart_total":total}