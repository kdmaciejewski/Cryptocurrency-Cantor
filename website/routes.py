from flask import render_template, url_for, flash, redirect, request
from website import app, db, bcrypt
from website.forms import RegistrationForm, LoginForm, ExchangeForm
from website.models import User
from flask_login import login_user, current_user, logout_user, login_required
from website import prices
#forms pozwalają na sprawdzenie podawanych przez użytkownika danych

posts = [
    {
        'author': 'Krzysztof Maciejewski',
        'title': 'Kupujcie Bitcoina!!',
        'content': 'Moim zdaniem bitcoin niedługo poszybuje w górę, jeśli chcecie zyskać kupujcie.',
        'date_posted': '31.05.2022'
    },
    {
        'author': 'Julia Bober',
        'title': 'Na rynku z rozwagą',
        'content': 'Uważajcie na hurraoptymistyczne wiadomości z internetu, powściągliwość i opanowanie'
                   ' to prawdziwe cnoty inwestora!',
        'date_posted': '01.06.2022'
    },
    {
        'author': 'Franciszek Nepomucen',
        'title': 'Kocham kryptowaluty',
        'content': 'Uwielbiam krytpowaluty i szukam kolegów do dyskusji o nich.',
        'date_posted': '01.06.2022'
    },
{
        'author': 'Krzysztof Maciejewski',
        'title': 'Kupujcie Etherium!!',
        'content': 'Moim zdaniem bitcoin niedługo poszybuje w dół, jeśli chcecie zyskać kupujcie etherium.',
        'date_posted': '29.05.2022'
    },
    {
        'author': 'Julia Bober',
        'title': 'Na rynku z rozwagą',
        'content': 'Uważajcie na hurraoptymistyczne wiadomości z internetu, powściągliwość i opanowanie'
                   ' to prawdziwe cnoty inwestora!',
        'date_posted': '01.06.2022'
    },
    {
        'author': 'Franciszek Nepomucen',
        'title': 'Kocham kryptowaluty',
        'content': 'Uwielbiam krytpowaluty i szukam kolegów do dyskusji o nich.',
        'date_posted': '01.06.2022'
    }
]
@app.route("/")
@app.route("/home")
def home():
    #zwracamy stronę html
    return render_template('home.html', posts=posts)  


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:   #sprawdzamy czy jest już zalogowany
        return redirect('home')

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Poprawnie utworzono użytkownika {form.username.data}! Można się zalogować', 'success')
        #jeżeli poprawnie się zarejestrował to
        return redirect(url_for('login'))
    return render_template('register.html', title='Rejestracja', form=form) #przekazujemy tę instancję RegistrationForm

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:  # sprawdzamy czy jest już zalogowany
        return redirect('home')

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  #sprawdzamy czy jest taki email w bazie
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)                                        #, remember=form.remember.data
            #next_page to strona która wybraliśmy zanim przenieśliśmy się na strone logowania
            #(np nie mielismy dostępu do niej i nas przeniosło)
            next_page = request.args.get('next')
            #przenieś na next_page jeśli istnieje
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Nie udało się zalogować', 'danger')
    return render_template('login.html', title='Logowanie', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/exchange", methods=['GET', 'POST'])
@login_required
def exchange():
    form = ExchangeForm()
    if form.validate_on_submit():
        val1 = int(form.val1.data)
        cur1 = str(form.cur1.data)
        cur2 = str(form.cur2.data)

        res = prices.exchange(val1, cur1, cur2)

        if res[1] == True:
            flash(f'Wymieniono {res[0]}', 'success')
            return render_template('exchange.html', title='Wymiana', form=form)
        else:
            flash('Niepoprawnie podane dane', 'danger')


    return render_template('exchange.html', title='Wymiana', form=form)


@app.route("/plotbtc")
@login_required
def plotbtc():
    return render_template('plot-btc.html', title='Wykres BTC')

@app.route("/ploteth")
@login_required
def ploteth():
    return render_template('plot-eth.html', title='Wykres ETH')

@app.route("/plotdoge")
@login_required
def plotdoge():
    return render_template('plot-doge.html', title='Wykres DOGE')

@app.route("/plotbnb")
@login_required
def plotbnb():
    return render_template('plot-bnb.html', title='Wykres BNB')

@app.route("/account")
@login_required
def account():
    ima = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Konto', image_file=ima)

@app.route("/plots")
@login_required
def plots():
    return render_template('plots.html', title='Wymiana')
    
