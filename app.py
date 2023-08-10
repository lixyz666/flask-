from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


# 项目1（前端）
@app.route("/rnu", methods=["GET", "POST"])
def rnu():
    if request.method == "GET":
        return render_template("rnu.html")
    # 第一题
    a1 = request.form.get("A1")
    b1 = request.form.get("B1")
    c1 = request.form.get("C1")
    d1 = request.form.get("D1")
    # 第二题
    a2 = request.form.get("A2")
    b2 = request.form.get("B2")
    c2 = request.form.get("C2")
    d2 = request.form.get("D2")
    # 第三题
    three = request.form.get("three")
    # 第四题
    four = request.form.get("four")
    # 第五题
    five = request.form.get("five")
    # 第六题
    six = request.form.get("six")
    # 第七题
    seven = request.form.get("seven")
    # 第八题
    ait = request.form.get("ait")
    # 第九题
    zb = request.form.get("zb")

    # 连接数据库
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='rnu123', password="rnu123", charset='utf8', db='rnu123')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 发送给MySQL
    sql = ("insert into admin(a1, b1, c1, d1, a2, b2, c2, d2, three, four, five, six, seven, ait, zb) values (%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    cursor.execute(sql, [a1, b1, c1, d1, a2, b2, c2, d2, three, four, five, six, seven, ait, zb])
    conn.commit()
    # 关闭
    cursor.close()
    conn.close()

    return render_template("dd.html")


# 项目1（后端
@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/admin", methods=["POST"])
def admin():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='rnu123', password="rnu123", charset='utf8', db='rnu123')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "select * from admin"
    cursor.execute(sql)
    data_list = cursor.fetchall()

    cursor.close()
    conn.close()
    print(data_list)
    return render_template('admin.html', data_list=data_list)

@app.errorhandler(405)
def handle_not_found_error(error):
    # 返回自定义的错误页面或错误信息
    return "要访问admin，请输入/login登录", 405

@app.errorhandler(404)
def handle_not_found_error(error):
    # 返回自定义的错误页面或错误信息
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run()
