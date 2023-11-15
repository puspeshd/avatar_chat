from flask import Flask,render_template,request,jsonify

app=Flask("__name__")
@app.route("/",methods=["GET","POST"])
def holo():
    return render_template("index.html")
@app.route("/process_text",methods=["GET","POST"])
def kolo():
    data = request.get_json()
    user_input = data.get('text', '')

    # Perform processing on user_input (you can replace this with your logic)
    processed_output = f"Flask Processed: {user_input}"
    #return render_template("index.html",output=processed_output)
    return jsonify({'output': processed_output})
if __name__=="__main__":
    app.run("0.0.0.0",debug=True)