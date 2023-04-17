from flask import Flask, flash, redirect, render_template, request, url_for
import pymongo
from bson import ObjectId
import logging
#
file_path="logging/app.log"
logging.basicConfig(filename=file_path)
logger = logging.getLogger('app')


app = Flask(__name__)

app.config['SECRET_KEY'] = '661a50e0edbb39371492d2a3518cb98b94c7b22efc972448c8'

# MongoDB client
client = pymongo.MongoClient("mongodb+srv://oratar333:Aa123456@cluster0.xyggxii.mongodb.net/?retryWrites=true&w=majority")
collection = client.products.products

# Product catalog
products = [
    {"name": "Brush", "price": 5},
    {"name": "Book", "price": 10},
    {"name": "Bag", "price": 15}
]

# Routes
@app.route("/")
def index():
    app.logger.warning("user asks for home page")
    return render_template("index.html", products=products)

@app.route("/purchase", methods=["POST"])
def purchase_item():
    product_name = request.form.get("product_name")
    quantity = int(request.form.get("quantity"))
    total_price = int(request.form.get("total_price"))
    total_price = total_price * quantity
    purchase_data = {"product_name": product_name, "quantity": quantity, "total_price": total_price}
    collection.insert_one(purchase_data)
    if purchase_data:
        flash('successfully adding to cart')
        return render_template("index.html", products=products)
    return redirect(url_for('index'))



@app.route("/cart")
def purchase_history():
    # Retrieve purchase history from MongoDB
    purchases = collection.find()
    sum =0
    print(purchases)
    # for product_name, data in purchases:
    #     quantity = data["quantity"]
    #     print(quantity)
    #     total_price = data["total_price"]
    #     print(total_price)
    #     sum += data["total_price"]
    #     print(sum)
    #     purchases_list.append({"product_name": product_name, "quantity": quantity, "total_price": total_price})

    return render_template("cart.html", purchases=purchases)

@app.route("/update_quantity", methods=["POST"])
def update_quantity():
    product_id = request.form.get("product_id")
    new_quantity = int(request.form.get("quantity"))
    print(new_quantity)
    collection.update_one({"_id": ObjectId(product_id)}, {"$set": {"quantity": new_quantity}})
    flash("Product quantity updated")
    return redirect(url_for("purchase_history"))

@app.route('/remove_product', methods=['POST'])
def delete_product():
    product_id = request.form['product_id']
    print("product id", product_id)
    collection.delete_one({"_id": ObjectId(product_id)})
    flash("Product deleted successfully", "success")
    return redirect(url_for("purchase_history"))


if __name__ == "__main__":
    app.run()