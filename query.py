from flask import Flask, render_template, request
from bardapi import BardCookies
import re
EXPLAIN_TEMPLATE_LOADING = True
app = Flask(__name__)
else_conditon="Page Not Found"
Cookies_dict={
    "__Secure-1PSIDTS":"sidts-CjEBNiGH7qxf3_0MdHCBYPAILLqGbyWP-wuHJXgxCTkWuwdG_mbrwQuNcb-Xuv4fSADsEAA",
    "__Secure-1PSID" :"fAjWW-CVyTwERJBlDrVrceu5qNEqYuEsKD9unKP3C3lGt40-FCjx80oH6MbATipsHp7b-A.",
    "__Secure-1PSIDCC" : "ABTWhQHc2DdyS7EqWFshDU3n42E333l9VBSGWcqyP8LlryESmcHnd5ljQmYL42E_obp87uVVe8qh" }
@app.route("/", methods=["GET", "POST"])
def index():
    Reply = ""
    if request.method == "POST":
        question = request.form["question"]
        # if question == "":
        #     return render_template("draft.html", reply="please click on submit button")
        # else:
        with open("data.txt", "w", encoding="utf-8") as f:
            f.writelines(str(question)+"\n")
        with open("data.txt", "r", encoding="utf-8") as f:
            R=f.read()
        R_variable=R

        Bard = BardCookies(cookie_dict=Cookies_dict)
        Reply = Bard.get_answer(R_variable)['content']
        with open("data2.txt", "w", encoding="utf-8") as f:
            f.writelines(Reply)

        def remove_bold(text):
            return re.sub(r'\**', '', text)

        def main():
        
            with open('data2.txt', 'r') as f:
                text = f.read()

            text = remove_bold(text)

            with open('data3.txt', 'w') as f:
                f.write(text)
        main()
        with open("data3.txt", "r", encoding="utf-8") as f:

            read=f.read()      
        return render_template("draft.html", reply=read)    
    else:
        return render_template("bard.html", reply=Reply)
if __name__ == "__main__":
    app.run(debug=True)

