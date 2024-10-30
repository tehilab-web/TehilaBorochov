#   סעיף א
# 1
class Product:


    def __init__(self, name, bought_with=None):
        if len(name) < 2:  # בודקת אם שם הנוצר קטן מ2 תווים
            raise ValueError("name Invalid")  # אם כן מעלה חריגה
        self.name = name
        self.bought_with = bought_with.copy() if bought_with is not None else {}  # אם לא נתון מאתחלת כרשימה ריקה
        # 2


def __repr__(self):
    return self.name
    # 3


def update(self, product_names):
    for product in product_names:
        if product in self.bought_with:
            self.bought_with[product] += 1  # אם מוצר כבר נמצא במילון מגדיל ב1
        else:
            self.bought_with[product] = 1  # אם לא נמצא במילון מאתחל ב1
    # 4


def get_recommendations(self, k):
    if k == 0:  # k=0 תוחזר רשימה ריקה עבור
        return []

    sorted_recommendations = sorted(self.bought_with.items(),
                                    key=lambda item: item[1],
                                    reverse=True)  # ממיין בסדר יורד לפי מספר הפעמים בהם נקנה כל מוצר
    return [product for product, _ in sorted_recommendations[:k]]  # מחזיר k של שמות מוצרים מהרשמיה הממויינת

    # סעיף ב
    # 1
    class GoldProduct(product):


def __init__(self, name, amount, bought_with=None):
    super().__init__(name, bought_with)  # יורש מ_init_ את השם והמילון
    self.amount = amount
    # 2


def __repr__(self):


return f"{self.name} Gold Prodoct Amount: {self.amount}"  # מחזירה את שמו של המוצר+ מס' היחידות שנותרו ממנו


# 3
def update(self, product_names)
    super().update(product_name):  # קוראת למתודת העדכון של המחלקה ההורה update() כדי לעדכן את המוצרים הנלווים
    self.amount = max(0, self.amount - 1)  # מפחיתה 1 מכמות המוצר ומוודאה שהכמות לא מתחת ל0


# 4
def get_recommendations(self, k)
    recommendations = super().get_recommendations(k)  # קוראת למתודה של המחלקה ההורה כדי לקבל המלצות
    filtered_recommendations = [product for product in recommendations if self.bought_with[
        product] >= 10]  # מסננת את ההמלצות ומחזירה רק מוצרים שנרכשו לפחות 10 פעמים.


return filtered_recommendations[:k]  # החזרת רשימת המוצרים המסוננת עד k מוצרים בלבד


# סעיף ג
class RecommendationSystem


# 1
def __init__(self, product_tuples):
    # יצירת מילון מוצרים מהטאפלים
    self.products = {}
    for name, amount in product_tuples:  # מקבלת רשימת טאפלים שם וכמות ומאחסנת את המוצרים במילון products
        if amount == -1:
            self.products[name] = Product(
                name)  # אם הכמות היא מינוס 1 היא יוצרת אובייקט מסוג פרודאקט אחרת יוצרת אובייקט מסוג גולד פרודאקט
        else:
            self.products[name] = GoldProduct(name, amount)


# 2


def update(self, purchased_product_names):
    for name in purchased_product_names:  # מקבלת רשימה של שמות מוצרים שנקנו
        if name in self.products:  # אם המוצר קיים במילון פרודאקטס
            product = self.products[name]
            product.update([name])  # קוראת למתודה אפדייט של המוצר ומעדכנת אותו עם עצמו


# 3
def get_recommendations(self, product_name, k):
    product = self.products[product_name]  # מקבלת שם של מוצר
    return product.get_recommendations(k)  # מחזירה את התוצאה של הפעלת המתודה על המוצר המתאים במילון פרודאקטס
