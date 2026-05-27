from app import db,app,Patient


with app.app_context():
    db.drop_all()
    db.create_all()

    p1 = Patient( name="ტატო", id_number="000",age=22,gender="female",img="https://stock.adobe.com/ge/search?k=person+face+background")  
    p2 = Patient( name="ლიკა", id_number="1111",age=88,gender="female",img="https://stock.adobe.com/ge/search?k=person+face+background")
    p3 = Patient(name="ირა", id_number="2222",age=78,gender="female",img="https://stock.adobe.com/ge/search?k=person+face+background")
    p4 = Patient( name="გია", id_number="3333",age=88,gender="female",img="https://stock.adobe.com/ge/search?k=person+face+background")
    p5 = Patient( name="რეზო", id_number="4444",age=90,gender="female",img="https://stock.adobe.com/ge/search?k=person+face+background")
    p6 = Patient( name="ნანული", id_number="5555",age=11,gender="female",img="https://stock.adobe.com/ge/search?k=person+face+background")
    p7 = Patient( name="როინი", id_number="6666",age=9,gender="female",img="https://stock.adobe.com/ge/search?k=person+face+background")
    p8 = Patient( name="ბადრი", id_number="7777",age=3,gender="female",img="https://stock.adobe.com/ge/search?k=person+face+background")
    p9 = Patient( name="აკაკი", id_number="8888",age=92,gender="female",img="https://stock.adobe.com/ge/search?k=person+face+background")

    all_patients=([p1,p2,p3,p4,p5,p6,p7,p8,p9])
    db.session.add_all(all_patients)
    db.session.commit()