from app import create_app
from app import db

app = create_app()

@app.route("/")
def hello_world():
    return "Rwanda Financial Markets Api: Financial Data At The Right Time"

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
