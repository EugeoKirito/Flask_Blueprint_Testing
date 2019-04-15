from flask  import Blueprint

app_goods=Blueprint('app_goods',__name__)

@app_goods.route('/get_goods')
def get_goods():
    return 'goods page'