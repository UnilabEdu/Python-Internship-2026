from app import app, db, Product, Category, Actor, Film, FilmActor

with app.app_context():
    db.drop_all()
    db.create_all()

    category1 = Category(name='პიანინო')
    category2 = Category(name='როიალი')
    category3 = Category(name='ციფრული')
    category4 = Category(name='სხვა')
    db.session.add(category1)
    db.session.add(category2)
    db.session.add(category3)
    db.session.add(category4)
    db.session.commit()

    piano1 = Product(name="ელექტრო პიანინო CASIO AP-270BNC2", price=10099.00, img="https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg", category_id=category1.id)
    piano2 = Product(name="ელექტრო პიანინო AP-270BNC2", price=599.00, img="https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg",  category_id=category2.id)
    piano3 = Product(name="ელექტრო CASIO AP-270BNC2", price=9.00, img="https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg",  category_id=category3.id)
    piano4 = Product(name="პიანინო CASIO AP-270BNC2", price=99.00, img="https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg",  category_id=category1.id)

    db.session.add(piano1)
    db.session.add(piano2)
    db.session.add(piano3)
    db.session.add(piano4)
    db.session.commit()

    db.session.add(Film(name='Avengers'))
    db.session.add(Film(name='Avengers End Game'))
    db.session.add(Film(name='Not Avengers'))

    db.session.add(Actor(name='Jason momoa'))
    db.session.add(Actor(name='Steheam'))
    db.session.add(Actor(name='Bret Pit'))

    db.session.commit()
    db.session.add(FilmActor(actor_id=1, film_id=1))
    db.session.add(FilmActor(actor_id=2, film_id=1))

    db.session.add(FilmActor(actor_id=2, film_id=2))
    db.session.add(FilmActor(actor_id=3, film_id=2))

    db.session.add(FilmActor(actor_id=1, film_id=3))

    db.session.commit()
num = [1, 2, 3, 4, 5, 6]
num2 = [x*x for x in num]

print(num2)