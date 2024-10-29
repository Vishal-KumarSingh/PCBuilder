from flask import Flask, render_template, request, redirect, url_for, flash
import os
app = Flask(__name__)

app.secret_key = os.urandom(24)
productlist = [
        {"id": 1, "name": "Intel Core i9-11900K", "price": 539.99, "image": "Intel Core i9-11900K.jpeg", "description": "A high-performance CPU for gaming and productivity."},
        {"id": 2, "name": "AMD Ryzen 9 5900X", "price": 499.99, "image": "AMD Ryzen 9 5900X.webp", "description": "A powerful CPU with 12 cores and 24 threads."},
        {"id": 3, "name": "NVIDIA GeForce RTX 3080", "price": 699.99, "image": "NVIDIA GeForce RTX 3080.jpeg", "description": "A high-end GPU for gaming and creative work."},
        {"id": 4, "name": "Corsair Vengeance LPX 16GB", "price": 89.99, "image": "Corsair Vengeance LPX 16GB.jpeg", "description": "High-performance DDR4 RAM for gaming and multitasking."},
        {"id": 5, "name": "Samsung 970 EVO Plus 1TB", "price": 169.99, "image": "Samsung 970 EVO Plus 1TB.jpeg", "description": "A fast NVMe SSD for quick load times and file transfers."},
        {"id": 6, "name": "Noctua NH-D15", "price": 89.99, "image": "Noctua NH-D15.jpeg", "description": "A premium CPU cooler for efficient cooling."},
        {"id": 7, "name": "ASUS ROG Strix Z590-E", "price": 379.99, "image": "ASUS ROG Strix Z590-E.jpeg", "description": "A high-end motherboard with advanced features."},
        {"id": 8, "name": "EVGA SuperNOVA 850 G5", "price": 139.99, "image": "EVGA SuperNOVA 850 G5.jpeg", "description": "A reliable power supply with 850W capacity."},
        {"id": 9, "name": "NZXT H510", "price": 69.99, "image": "NZXT H510.jpeg", "description": "A sleek and compact mid-tower case."},
        {"id": 10, "name": "LG UltraGear 27GL850", "price": 449.99, "image": "LG UltraGear 27GL850.jpeg", "description": "A 27-inch monitor with a 144Hz refresh rate and 1ms response time."},
        {"id": 11, "name": "Logitech G502 HERO", "price": 49.99, "image": "Logitech G502 HERO.jpeg", "description": "A high-performance gaming mouse with customizable buttons."},
        {"id": 12, "name": "Razer BlackWidow Elite", "price": 129.99, "image": "Razer BlackWidow Elite.jpeg", "description": "A mechanical gaming keyboard with RGB lighting."},
        {"id": 13, "name": "HyperX Cloud II", "price": 99.99, "image": "HyperX Cloud II.jpeg", "description": "A comfortable gaming headset with 7.1 surround sound."},
        {"id": 14, "name": "Seagate Barracuda 2TB", "price": 54.99, "image": "Seagate Barracuda 2TB.jpeg", "description": "A reliable 2TB hard drive for mass storage."},
        {"id": 15, "name": "Cooler Master Hyper 212", "price": 34.99, "image": "Cooler Master Hyper 212.jpeg", "description": "An affordable and efficient CPU cooler."},
        {"id": 16, "name": "MSI MPG Z490 Gaming Edge", "price": 189.99, "image": "MSI MPG Z490 Gaming Edge.jpeg", "description": "A gaming motherboard with advanced features."},
        {"id": 17, "name": "Gigabyte AORUS 850W", "price": 129.99, "image": "Gigabyte AORUS 850W.jpeg", "description": "A high-performance power supply with 850W capacity."},
        {"id": 18, "name": "Phanteks Eclipse P400A", "price": 79.99, "image": "Phanteks Eclipse P400A.jpeg", "description": "A mid-tower case with excellent airflow."},
        {"id": 19, "name": "Dell UltraSharp U2720Q", "price": 599.99, "image": "Dell UltraSharp U2720Q.jpeg", "description": "A 27-inch 4K monitor with accurate color reproduction."},
        {"id": 20, "name": "SteelSeries QcK Gaming Surface", "price": 14.99, "image": "SteelSeries QcK Gaming Surface.jpeg", "description": "A high-quality mouse pad for precise control."},
        {"id": 21, "name": "Corsair K95 RGB Platinum", "price": 199.99, "image": "Corsair K95 RGB Platinum.jpeg", "description": "A mechanical gaming keyboard with customizable RGB lighting."},
        {"id": 22, "name": "ASUS TUF Gaming VG27AQ", "price": 429.99, "image": "ASUS TUF Gaming VG27AQ.jpeg", "description": "A 27-inch monitor with a 165Hz refresh rate and 1ms response time."},
        {"id": 23, "name": "Razer DeathAdder V2", "price": 69.99, "image": "Razer DeathAdder V2.jpeg", "description": "A high-precision gaming mouse with ergonomic design."},
        {"id": 24, "name": "Corsair RM850x", "price": 129.99, "image": "Corsair RM850x.jpeg", "description": "A reliable power supply with 850W capacity and modular cables."},
]

latestlist = [
        {"id": 17, "name": "Gigabyte AORUS 850W", "price": 129.99, "image": "Gigabyte AORUS 850W.jpeg", "description": "A high-performance power supply with 850W capacity."},
        {"id": 18, "name": "Phanteks Eclipse P400A", "price": 79.99, "image": "Phanteks Eclipse P400A.jpeg", "description": "A mid-tower case with excellent airflow."},
        {"id": 19, "name": "Dell UltraSharp U2720Q", "price": 599.99, "image": "Dell UltraSharp U2720Q.jpeg", "description": "A 27-inch 4K monitor with accurate color reproduction."},
        {"id": 20, "name": "SteelSeries QcK Gaming Surface", "price": 14.99, "image": "SteelSeries QcK Gaming Surface.jpeg", "description": "A high-quality mouse pad for precise control."},
        {"id": 21, "name": "Corsair K95 RGB Platinum", "price": 199.99, "image": "Corsair K95 RGB Platinum.jpeg", "description": "A mechanical gaming keyboard with customizable RGB lighting."},
        {"id": 22, "name": "ASUS TUF Gaming VG27AQ", "price": 429.99, "image": "ASUS TUF Gaming VG27AQ.jpeg", "description": "A 27-inch monitor with a 165Hz refresh rate and 1ms response time."},
        {"id": 23, "name": "Razer DeathAdder V2", "price": 69.99, "image": "Razer DeathAdder V2.jpeg", "description": "A high-precision gaming mouse with ergonomic design."},
        {"id": 24, "name": "Corsair RM850x", "price": 129.99, "image": "Corsair RM850x.jpeg", "description": "A reliable power supply with 850W capacity and modular cables."},
]
@app.route("/")
def index():
    global latestlist , productlist
    return render_template("index.html" , products=productlist , latest=latestlist)

@app.route("/contact")
def contact():
   
    return render_template("contact.html")
@app.route("/handle_contact" , methods=["POST"])
def handle_contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    
    # Validation
    if not name or not email or not message:
        flash("All fields are required!")
        return redirect(url_for("contact"))

    # Process the contact form data here
    return render_template("contact.html", name=name, email=email, message=message)
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/products")
def products():
    global productlist
    # Realistic data for products
   
    return render_template("products.html", products=productlist)


@app.route("/latest")
def latest():
    global latestlist
    # Realistic data for products
   
    return render_template("products.html", products=latestlist)
@app.route("/buy_product/<product_id>")
def buy_product(product_id):
    global productlist
    for item in productlist:
        if(str(item["id"])==product_id):
             return render_template("buy_product.html" , product=item)
   

if __name__ == "__main__":
    app.run()