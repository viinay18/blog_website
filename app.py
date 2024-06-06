from website import app, create_database


if __name__ == "__main__":
    
    with app.app_context():
        create_database(app)
        
    app.run(debug=True, port=8000)
