import argparse
import os
import sys
import tempfile
#from flask_ngrok import run_with_ngrok
import requests
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

app = Flask(__name__)
app.secret_key = "LeafmanZSecretKey"

# PAGES #
@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        if "user_prompt" in request.form:
            user_prompt = request.form["user_prompt"]
            print(f"User Prompt: {user_prompt}")

            main_prompt_url = "http://localhost:5110/api/prompt_route"
            response = requests.post(main_prompt_url, data={"user_prompt": user_prompt})
            print(response.status_code)  # print HTTP response status code for debugging
            if response.status_code == 200:
                # print(response.json())  # Print the JSON data from the response
                return render_template("home-NGROK.html", show_response_modal=True, response_dict=response.json())
        elif "documents" in request.files or "text" in request.form:
            delete_source_url = "http://localhost:5110/api/delete_source"  # URL of the /api/delete_source endpoint
            if request.form.get("action") == "reset":
                response = requests.get(delete_source_url)

            save_document_url = "http://localhost:5110/api/save_document"
            run_ingest_url = "http://localhost:5110/api/run_ingest"  # URL of the /api/run_ingest endpoint

            if "documents" in request.files:
                files = request.files.getlist("documents")
                for file in files:
                    if file.filename != "":
                        print(file.filename)
                        filename = secure_filename(file.filename)
                        with tempfile.SpooledTemporaryFile() as f:
                            f.write(file.read())
                            f.seek(0)
                            response = requests.post(save_document_url, files={"document": (filename, f)})
                            print(response.status_code)  # print HTTP response status code for debugging

            if "text" in request.form:
                text = request.form.get("text")
                response = requests.post(save_document_url, data={"text": text})
                print(response.status_code)  # print HTTP response status code for debugging

            # Make a GET request to the /api/run_ingest endpoint
            response = requests.get(run_ingest_url)
            print(response.status_code)  # print HTTP response status code for debugging

    # Display the form for GET request
    return render_template(
        "home-NGROK.html",
        show_response_modal=False,
        response_dict={"Prompt": "None", "Answer": "None", "Sources": [("ewf", "wef")]},
    )


if __name__ == "__main__":
    # run_with_ngrok(app)
    # app.run()
     app.run(debug=False, host="0.0.0.0" , port=5111)
