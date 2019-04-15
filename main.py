#coding='utf-8'
from flask  import Flask
from goods  import app_goods
from users  import register
from orders import app_orders
from cart   import app_cart

app=Flask(__name__)


#单条路由
# app.route('/get_goods')(get_goods)
app.register_blueprint(app_goods,url_prefix='/yeye')
app.route('/register')(register)


app.register_blueprint(app_orders,url_prefix='/orders')
app.register_blueprint(app_cart,url_prefix='/cart')

@app.route('/')
def index():
    return 'index page'
print(app.url_map)
if __name__ == '__main__':
    app.run(port=5001)
    app.debug(True)


