from module import *
from config import *

from flask import render_template, request

""" Structures """

# Категории
category = StaticObjectsStructure(["Название"])
# Передавать 1 агрумент name
category.add_row(name="Ноутбуки")
category.add_row(name="Мобільні телефони")

# Товары
product = StaticObjectsStructure(["Название", "Описание", "Стоимость", "Категория", "Картинка"])
# Передавать 4 аргумента name, description, price, category
product.add_row(
	name="Aspire 5 A515-56G-54JD (NX.A1LEU.00A) Pure Silver",
	description="Екран 15.6 'IPS (1920x1080) Full HD, матовий / Intel Core i5-1135G7 (4.2 ГГц) / RAM 8 ГБ / SSD 512 ГБ / nVidia GeForce MX350, 2 ГБ / без ОД / LAN / Wi-Fi / Bluetooth / веб камера / без ОС / 1.9 кг / сріблястий",
	price="19 999 грн",
	category="Ноутбуки",
	images="1.jpg"
)
product.add_row(
	name="Asus ROG Strix G15 G512LI-HN058 (90NR0381-M01630) Black",
	description="Екран 15.6 IPS (1920x1080) Full HD 144 Гц, матовий / Intel Core i5-10300H (2.5 — 4.5 ГГц) / RAM 16 ГБ / SSD 512 ГБ / nVidia GeForce GTX 1650 Ti, 4 ГБ / без ОД / LAN / Wi-Fi / Bluetooth / без ОС / 2.39 кг / чорний",
	price="26 999 грн",
	category="Ноутбуки",
	images="2.jpg"
)
product.add_row(
	name="HP Pavilion 14-dv0002ua (34Q59EA) White/Silver",
	description="Екран 14 PS (1920x1080) Full HD, матовий / Intel Core i5-1135G7 (4.2 ГГц) / RAM 16 ГБ / SSD 512 ГБ / Intel Iris Xe Graphics / без ОД / Wi-Fi / Bluetooth / веб-камера / DOS / 1.41 кг / білий з сріблястим",
	price="22 499 грн",
	category="Ноутбуки",
	images="3.jpg"
)
product.add_row(
	name="Asus Laptop X515JP-BQ032 (90NB0SS2-M00630) Transparent Silver",
	description="Екран 15.6 IPS (1920x1080) Full HD, матовий / Intel Core i5-1035G1 (1.0 — 3.6 ГГц) / RAM 8 ГБ / SSD 256 ГБ / nVidia GeForce MX330, 2 ГБ / без ОД / Wi-Fi / Bluetooth / вебкамера / без ОС / 1.8 кг / сріблястий",
	price="18 900 грн",
	category="Ноутбуки",
	images="4.jpg"
)
product.add_row(
	name="Lenovo V145-15 (81MT002CRA) Black",
	description="Екран 15.6 (1920x1080) Full HD, матовий / AMD Dual-Core A4-9125 (2.3 — 2.6 ГГц) / RAM 4 ГБ / SSD 128 ГБ / AMD Radeon R3 Graphics / DVD+/-RW / LAN / Wi-Fi / Bluetooth / вебкамера / DOS / 2.1 кг / чорний",
	price="8 900 грн",
	category="Ноутбуки",
	images="5.jpg"
)
product.add_row(
	name="Samsung Galaxy A71 6/128GB Black (SM-A715FZKUSEK)",
	description="Екран (6.7, Super AMOLED Plus, 2400x1080) / Qualcomm Snapdragon 730 (2 x 2.2 ГГц + 6 x 1.8 ГГц) / основна квадрокамера: 64 Мп + 12 Мп + 5 Мп + 5 Мп, фронтальна 32 Мп / RAM 6 ГБ / 128 ГБ вбудованої пам'яті + microSD (до 512 ГБ) / 3G / LTE / GPS / підтримка 2 SIM-карток (Nano-SIM) / Android 10.0 (Q) / 4500 мА·год",
	price="9 999 грн",
	category="Мобільні телефони",
	images="6.jpg"
)
product.add_row(
	name="Samsung Galaxy A51 6/128GB Blue (SM-A515FZBWSEK)",
	description="Екран (6.5, Super AMOLED, 2400x1080) / Samsung Exynos 9611 (2.3 ГГц + 1.7 ГГц) / основна квадрокамера: 48 Мп + 12 Мп + 5 Мп + 5 Мп, фронтальна 32 Мп / RAM 6 ГБ / 128 ГБ вбудованої пам'яті + microSD (до 512 ГБ) / 3G / LTE / GPS / підтримка 2 SIM-карток (Nano-SIM) / Android 10.0 (Q) / 4000 мА·год",
	price="7499 грн",
	category="Мобільні телефони",
	images="7.jpg"
)
product.add_row(
	name="Samsung Galaxy A32 4/64 GB Blue",
	description="Екран (6.4, Super AMOLED, 2400x1080) / Mediatek Helio G80 (2 x 2.0 ГГц + 6 x 1.8 ГГц) / основна квадрокамера: 64 Мп + 8 Мп + 5 Мп + 5 Мп, фронтальна камера: 20 Мп / RAM 4 ГБ / 64 ГБ вбудованої пам'яті + microSD (до 1 ТБ) / 3G / LTE / GPS / A-GPS / ГЛОНАСС / BDS / підтримка 2 SIM-карток (Nano-SIM) / Android 11 (One UI) / 5000 мА·год",
	price="6 599 грн",
	category="Мобільні телефони",
	images="8.jpg"
)
product.add_row(
	name="Apple iPhone 12 Pro Max 128 GB Gold",
	description="Екран (6.7, OLED (Super Retina XDR), 2778x1284) / Apple A14 Bionic / потрійна основна камера: 12 Мп + 12 Мп + 12 Мп, фронтальна камера: 12 Мп / 128 ГБ вбудованої пам'яті / 3G / LTE / 5G / GPS / Nano-SIM / iOS 14",
	price="39 490 грн",
	category="Мобільні телефони",
	images="9.jpg"
)
product.add_row(
	name="Samsung Galaxy A11 2/32GB Red (SM-A115FZRNSEK)",
	description="Екран (6.4, PLS, 1560x720) / Qualcomm Snapdragon 450 (8 x 1.8 ГГц) / потрійна основна камера: 13 Мп + 5 Мп + 2 Мп, фронтальна камера: 8 Мп / RAM 2 ГБ / 32 ГБ вбудованої пам'яті + microSD (до 512 ГБ) / 3G / LTE / GPS / ГЛОНАСС / BDS / підтримка 2 SIM-карток (Nano-SIM) / Android 10.0 (Q) / 4000 мА·год",
	price="2 999 грн",
	category="Мобільні телефони",
	images="10.jpg"
)


# Контактные данные
contact = StaticObjectsStructure(["Сервис", "Данные"]) 

# Передавать 2 аргумента name, argument
contact.add_row(name="Номер телефона", argument="+380979560403")
contact.add_row(name="Email", argument="sivakd230@gmail.com")

print(category.table)
print(product.table)
print(contact.table)

global_data["contact"] = contact.structure
global_data["allcategory"] = category.structure
global_data['allproduct'] = product.structure

""" Sites """
site = App(__name__)

def category_search(category):

	return products
# logic

@site.site.route("/")
def index():
	notifications = []

	data = None

	return render_template(SETTING_TEMPLATE["index"], data=data, global_data=global_data, notifications=notifications)

@site.site.route("/category/<int:id>")
def categorys(id):
	notifications = []

	data = {}

	categors = category.search_to_structure(obj=id)

	products = []

	for prod in product.structure:
		if prod["category"] == categors["name"]:
			products.append(prod)

	data["products"] = products

	return render_template(SETTING_TEMPLATE["index"], data=data, global_data=global_data, notifications=notifications)

@site.site.route("/<int:id>")
def detail(id):
	notifications = []
	data = product.search_to_structure(obj=id)

	return render_template(SETTING_TEMPLATE["product_detail"], data=data, global_data=global_data, notifications=notifications)

@site.site.route("/order/<int:id>", methods=["POST"])
def ordering(id):
	
	notifications = []

	data = {}

	if request.method == "POST" and request.form.get("phone", False):

		products = product.search_to_structure(obj = id)

		notifications.append("Заказ успешно оформлен!")

		phone = request.form.get("phone", False)

		with open('orders.txt', 'a', encoding='utf-8') as file:
		    file.write(
		    	f"\n[{GetTime()}] Заказ оформлен. Номер телефона: {phone}. "
		    	f"Информация о заказе: Название {products['name']} | Описание: {products['description']} | Категория: {products['category']} | Цена: {products['price']}")

		return render_template(SETTING_TEMPLATE["product_detail"], data=products, global_data=global_data, notifications=notifications)

	notifications.append("Вы забыли указать номер!")

	data = product.search_to_structure(obj=id)

	return render_template(SETTING_TEMPLATE["product_detail"], data=data, global_data=global_data, notifications=notifications)

# Starting
site.start(debug=True)