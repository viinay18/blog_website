from website import create_app, create_database


if __name__ == "__main__":
    app = create_app()
    
    with app.app_context():
        create_database(app)
        
    app.run(debug=True, port=8000)