#from blueprints.people.models import User
#from models import Person

from flask import render_template, request, redirect, url_for, Blueprint, flash

from blueprintapp.app import db
from blueprintapp.blueprints.people.models import Person


people = Blueprint('people', __name__, template_folder='templates' )

@people.route('/')
def index():
    people = Person.query.all()
    return render_template('people/index.html', people = people)



@people.route('/create', methods= ['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        job = request.form.get('job')

        # Verilerin boş olup olmadığını kontrol edin
        if not name:
            flash('Name is required!')
            return redirect(url_for('people.create'))

        # Age ve job için de benzer kontroller ekleyebilirsiniz
        if not age:
            flash('Age is required!')
            return redirect(url_for('people.create'))

        # Yaş kontrolü integer'a dönüştür
        try:
            age = int(age)
        except ValueError:
            flash('Age must be a number!')
            return redirect(url_for('people.create'))

        if not job:
            flash('Job is required!')
            return redirect(url_for('people.create'))

        # Person nesnesi oluştur ve veritabanına ekle
        new_person = Person(name=name, age=age, job=job)
        db.session.add(new_person)
        db.session.commit()
        return redirect(url_for('people.index'))

    return render_template('people/create.html')


""" 

def register_routes(app, db, bcrypt):


    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template('index.html')
        #if current_user.is_authenticated:
        #    return str(current_user.username)
        #else:
        #    return "No user is logged in"
        #if request.method == 'GET':
        #    # Tüm kişileri sorgula ve döndür
        #    people = Person.query.all()
        #    return render_template('index.html', people=people)
        #elif request.method == 'POST':
        #    name = request.form.get('name')
        #    age = request.form.get('age')
        #    job = request.form.get('job')
        #    person = Person(name=name, age=age, job=job)

        #   db.session.add(person)
        #    db.session.commit()
        #    people = Person.query.all()
        #    return render_template('index.html', people=people)

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            # Şifreyi hash'le
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            # Kullanıcıyı oluştur
            user = User(username=username, password=hashed_password)  # Hash'lenmiş şifreyi kullan

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            user = User.query.filter(User.username == username).first()

            # Kullanıcı bulunamadıysa hata ver
            if user is None:
                flash('Try Agin')
                return redirect(url_for('login'))

            # Hash'lenmiş şifre ile giriş kontrolü yap
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                return f"Try Again. <a href='{url_for('login')}'>Click here to try again</a>"


    @app.route('/secret')
    @login_required
    def secret():
        #if current_user.role == "admin":
            return "My secret message"




    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return "Logout Success"

    @app.route('/login_with_uid/<uid>', methods=['GET', 'POST'])
    def login_with_uid(uid):
        user = User.query.get(uid)
        if user:
            login_user(user)
            return "Login Success"
        return "User not found"

    @app.route('/delete/<pid>', methods=['Get', 'DELETE'])
    def delete(pid):
        Person.query.filter(Person.pid == pid).delete()
        db.session.commit()
        people = Person.query.all()
        return render_template('index.html', people=people)

    @app.route('/details/<pid>', methods=['Get'])
    def details(pid):
        person = Person.query.filter(Person.pid == pid).first()
        return render_template('details.html', person=person)

    @app.route('/set_data')
    def set_data():
        # Oturum verilerini ayarla
        session['name'] = 'Busra'
        session['other'] = 'Hello!'
        return render_template('index.html', message='Session data set.')

    @app.route('/get_data')
    def get_data():
        # Oturum verilerini al
        name = session.get('name')
        other = session.get('other')
        if name and other:
            return render_template('index.html', message=f'Name: {name}, Other: {other}')
        else:
            return render_template('index.html', message='No session found!')

    @app.route('/clear_session')
    def clear_session():
        # Oturumu temizle
        session.clear()
        return render_template('index.html', message='Session cleared.')

    @app.route('/set_cookie')
    def set_cookie():
        # Çerez ayarla
        response = make_response(render_template('index.html', message='Cookie set.'))
        response.set_cookie('cookie_name', 'cookie_value')
        return response

    @app.route('/get_cookie')
    def get_cookie():
        # Çerez değerini al
        cookie_value = request.cookies.get('cookie_name', 'Cookie not found!')
        return render_template('index.html', message=f'Cookie value: {cookie_value}')

    @app.route('/remove_cookie')
    def remove_cookie():
        # Çerezi kaldır
        response = make_response(render_template('index.html', message='Cookie removed.'))
        response.set_cookie('cookie_name', '', expires=0)
        return response

    @app.route('/other_login2', methods=['GET', 'POST'])
    def other_login2():
        if request.method == 'POST':
            # Kullanıcı girişi işlemi
            username = request.form.get('username')
            password = request.form.get('password')
            if username == 'busra' and password == '1234':
                flash('Welcome to Busra!')
                return render_template('other_login2.html', message='Welcome!')
            else:
                flash('Wrong username or password!')
                return render_template('other_login2.html', message='Wrong username or password!')
        return render_template('other_login2.html')

    @app.route('/index2')
    def index2():
        # Sabit veriler ile sayfayı döndür
        myvalue = 'NeuralNine'
        myresult = 10 + 20
        mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        return render_template('index2.html', myvalue=myvalue, myresult=myresult, mylist=mylist)

    @app.route('/file_upload', methods=['GET', 'POST'])
    def file_upload():
        if request.method == 'POST':
            # Dosya yükleme işlemi
            file = request.files.get('file')
            if file:
                if file.content_type == 'text/plain':
                    return file.read().decode()
                elif file.content_type in ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                                           'application/vnd.ms-excel']:
                    df = pd.read_excel(file)
                    return df.to_html()
        return render_template('file_upload.html')  # GET isteği için dosya yükleme sayfasını döndür

    @app.route('/convert_csv', methods=['GET', 'POST'])
    def convert_csv():
        if request.method == 'POST':
            # Excel dosyasını CSV'ye dönüştür
            file = request.files.get('file')
            if file:
                df = pd.read_excel(file, engine='openpyxl')
                response = Response(
                    df.to_csv(),
                    mimetype='text/csv',
                    headers={'Content-Disposition': 'attachment; filename=result.csv'}
                )
                return response
        return render_template('convert_csv.html')  # GET isteği için dönüştürme sayfasını döndür

    @app.route('/convert_csv_two', methods=['GET', 'POST'])
    def convert_csv_two():
        if request.method == 'POST':
            # Excel dosyasını CSV olarak kaydet
            file = request.files.get('file')
            if file:
                downloads_dir = '../../downloads'
                os.makedirs(downloads_dir, exist_ok=True)  # Klasör yoksa oluştur
                filename = f"{uuid.uuid4()}.csv"
                file_path = os.path.join(downloads_dir, filename)
                df = pd.read_excel(file)
                df.to_csv(file_path, index=False)
                return render_template('download.html', filename=filename)
        return render_template('convert_csv_two.html')  # GET isteği için dönüştürme sayfasını döndür

    @app.route('/download/<filename>')
    def download(filename):
        # Dosyayı indir
        return send_from_directory('../../downloads', filename, as_attachment=True)

    @app.route('/handle_post', methods=['POST'])
    def handle_post():
        # POST isteğini işleyin
        greeting = request.json.get('greeting')
        name = request.json.get('name')
        if greeting and name:
            with open('../../file.txt', 'w') as f:
                f.write(f'{greeting}, {name}')
            return jsonify({'message': 'Success'})
        return jsonify({'message': 'Missing parameters!'}), 400

    @app.route('/other')
    def other():
        # Diğer sayfayı döndür
        some_text = 'Hello World!'
        return render_template('other.html', some_text=some_text)

    @app.route('/redirect_endpoints')
    def redirect_endpoints():
        # Diğer sayfaya yönlendir
        return redirect(url_for('other'))

    @app.template_filter('reverse_string')
    def reverse_string(s):
        # String'i ters çevir
        return s[::-1]

    @app.template_filter('repeat')
    def repeat(s, times=2):
        # String'i tekrarla
        return s * times

    @app.template_filter('alternate_case')
    def alternate_case(s):
        # Karakterlerin büyük/küçük harfini sırayla değiştir
        return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

    @app.route('/hello', methods=['GET', 'POST'])
    def hello():
        # "Hello World!" yanıtını döndür
        response = make_response('Hello World!')
        response.status_code = 202
        response.headers['content-type'] = 'application/octet-stream'
        return response

    @app.route('/greet/<name>')
    def greet(name):
        # Kullanıcıyı selamla
        return f'Hello {name}!'

    @app.route('/add/<int:number1>/<int:number2>')
    def add(number1, number2):
        # İki sayıyı topla ve döndür
        return f'{number1} + {number2}'


"""