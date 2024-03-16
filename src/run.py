from app import app,db, create_topic

if __name__ == "__main__":
    with app.app_context():
        create_topic()
        db.create_all()
    app.run(debug=True)
