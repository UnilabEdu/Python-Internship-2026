from flask import Flask, render_template, url_for, request

app = Flask(__name__)


class Photo():
    def __init__(self, title, artist, img):
        self.title = title
        self.artist = artist
        self.img = img

photo1 = Photo("Hand mosaic", "Unknown",
               "https://scontent.ftbs6-2.fna.fbcdn.net/v/t1.15752-9/694531756_858353106637023_2505383973973620837_n.png?_nc_cat=103&ccb=1-7&_nc_sid=9f807c&_nc_ohc=fSMV2d9nMbgQ7kNvwGOILNi&_nc_oc=AdpPA2OgfdMmi-DZBiXiFptF2dAIyVZUDWNIX8zXuHoP5P8U1pyoVPkkKFj-DnUlehA&_nc_zt=23&_nc_ht=scontent.ftbs6-2.fna&_nc_ss=7b2a8&oh=03_Q7cD5QGbJfuGqCMO9JRVNY6LX4RiHd19JKHF9p0j9hEeJnJJaQ&oe=6A2FCD7A")
photo2 = Photo("Street Number Plate", "Unknown",
       "https://scontent.ftbs4-2.fna.fbcdn.net/v/t1.15752-9/694533369_1466854341908792_4842174725836018292_n.png?_nc_cat=105&ccb=1-7&_nc_sid=9f807c&_nc_ohc=0XJLNJhdnHIQ7kNvwEJC9vo&_nc_oc=AdrA0zSoT3ZARWJBAe1Z66ASrX5DypZibqqFjTSV3V39TIYnCiMQ5KBXd_axvMYP4AM&_nc_zt=23&_nc_ht=scontent.ftbs4-2.fna&_nc_ss=7b2a8&oh=03_Q7cD5QGS7wHZiqxilinVndn_p2cE8HpUL2TlTfoQpjUiWt9b8g&oe=6A2FDDE4")
photo3 = Photo("Flower Sculpture Relif", "Unknown",
    "https://scontent.ftbs6-2.fna.fbcdn.net/v/t1.15752-9/693544242_1648723442908907_8796596297526633500_n.png?_nc_cat=106&ccb=1-7&_nc_sid=9f807c&_nc_ohc=Q0n4V9tJEV8Q7kNvwGc5rjN&_nc_oc=AdpT8ra-8rjQNlOFXwFqqsHyUFCH2gBI6CdIfqY2rZMLfS47Q116zOfdLlb2wA6BxEU&_nc_zt=23&_nc_ht=scontent.ftbs6-2.fna&_nc_ss=7a2a8&oh=03_Q7cD5QH_yYK_3DNU-9vQh712XrZdQoUQ5vqqmW0MJJsVwbtxPw&oe=6A2FE70E")
photo4 = Photo("Park Bench Decoration", "Unknown",
       "https://scontent.ftbs4-2.fna.fbcdn.net/v/t1.15752-9/699879303_1293129706270009_2611754670896799763_n.png?_nc_cat=101&ccb=1-7&_nc_sid=9f807c&_nc_ohc=DL5HmtyUBFIQ7kNvwFhEh02&_nc_oc=AdoyZ1G1nqlXYeACm0yc3cWB6LQMUewBw49oIHK7LgclL-jMTVHVC_MxApcO_SlcmQg&_nc_zt=23&_nc_ht=scontent.ftbs4-2.fna&_nc_ss=7a2a8&oh=03_Q7cD5QEIg7kSx-JAWZg1Y-80N4fzB8pXZZK_Zl_TruZQae_83Q&oe=6A2FB8EA")
photo5 = Photo("Wall Decoration", "Lironism",
       "https://scontent.ftbs6-2.fna.fbcdn.net/v/t1.15752-9/696489407_971447965738608_4451664832830370176_n.png?_nc_cat=110&ccb=1-7&_nc_sid=9f807c&_nc_ohc=_JpE-rowz9sQ7kNvwGXzJ6j&_nc_oc=AdrYLuMtTaz3dN4vOsdApBFaQNuNrx6e8PMQ0FuAWavUzPorAvFKeTTTBc3eUMhCMJc&_nc_zt=23&_nc_ht=scontent.ftbs6-2.fna&_nc_ss=7a2a8&oh=03_Q7cD5QGqkAdZbyc6AEvNfjO_73bLI1Tp3G31a3gReyh5A7T01g&oe=6A2FE367")
photo6 = Photo("Cat Paw Print", "Some random cat",
     "https://scontent.ftbs6-2.fna.fbcdn.net/v/t1.15752-9/667958067_1503340308209344_2076100038851782294_n.png?_nc_cat=108&ccb=1-7&_nc_sid=9f807c&_nc_ohc=4hSJ7ii3HCgQ7kNvwGbFJ4g&_nc_oc=AdoMxytBgl_aZgeqpDTxI3K2MTwa8utBPmYFOfCP-wfzzH7EcFpK7B77piFzlPt1knE&_nc_zt=23&_nc_ht=scontent.ftbs6-2.fna&_nc_ss=7a2a8&oh=03_Q7cD5QEhEbAugQy0LL9YguFPtT91JJvPtOWfFdiPnoaewRkfnw&oe=6A2FD95E")

gallery = [photo1, photo2, photo2, photo4, photo5, photo6]

@app.route('/')
def index():
    print(request.path)
    return render_template("index.html", title="Gallery", photos=gallery)


@app.route('/photos')
def photos():
    return render_template('photos.html', products=gallery)

@app.route('/photos/<int:id>')
def photo(id):
    return render_template('photo.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')


app.run(debug=True)
