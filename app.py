from app import create_app

app = create_app()

@app.route("/")
def hello_world():
    return "Rwanda Financial Markets Api: Financial Data At The Right Time"


if __name__ == "__main__":
    app.run(debug=True)
