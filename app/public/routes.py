from flask import abort, render_template, current_app
from werkzeug.exceptions import NotFound

from app.models import Post
from . import public_bp
import logging

logger = logging.getLogger(__name__)

@public_bp.route("/")
def index():
    current_app.logger.info("Mostrando los posts del blog")
    logger.info('Mostrando los posts del blog')
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts)

@public_bp.route("/p/<string:slug>/")
def show_post(slug):
    logger.info('Mostrando un Post')
    logger.debug(f'Slug: {slug}')
    post = Post.get_by_slug(slug)
    if post is None:
        logger.info(f'El post {slug} no existe')
        raise NotFound(slug)
        #abort(404)
    return render_template("public/post_view.html", post=post)

@public_bp.route("/error/")
def error():
    current_app.logger.error("Error: Prueba Error.")
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts)