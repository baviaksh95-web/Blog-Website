from flask import Flask, render_template, request, redirect, url_for
from models import db,Post
from config import Config

app = Flask(__name__)
app.config.from_object(Config)  # Load Configuration settings in Flask
db.init_app(app)

@app.route('/')
def home():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = Post.query.get_or_404(post_id)
    return render_template('post.html',requested_post=requested_post)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create.html')

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        db.session.commit()
        return redirect(url_for('show_post',post_id=post.id))
    return render_template('post.html', requested_post=post, edit_mode=True)

@app.route('/delete/<int:post_id>', methods=['GET', 'POST'])
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('delete.html', post=post, post_id=post.id)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)