from flask import Flask, render_template, abort

def create_app():
    app = Flask(__name__)

    projects = [
        {
            "name": "Microblog with Python, Flask, and MongoDB",
            "thumb": "/blog.png",
            "hero": "/microblog-hero.png",
            "categories": ["Python", "Flask", "MongoDB"],
            "slug": "microblog",
            "prod": "https://python-micro-blog.onrender.com/"
        },
        {
            "name": "Person Detection Surveillance Camera with YoloV5",
            "thumb": "/body-scan.png",
            "hero": "/fafi_state_diagram.jpg",
            "categories": ["Python", "Flask", "Yolov5", "sqlite3", "cv2", "torch"],
            "slug": "person-detection-surveillance-app",
            "prod": "https://github.com/aidanschang/CS673-Person-Detection-Surveillance-APP"
        },
        {
            "name": "Self Pay Kiosk RDBMS with Oracle SQL Developer",
            "thumb": "/self-service.png",
            "hero": "/database-hero.png",
            "categories": ["Oracle SQL Developer"],
            "slug": "self-pay-kiosk-rdbms",
            "prod": "https://github.com/aidanschang/Self-Pay-Kiosk-System-RDBS"
        }
    ]

    slug_to_project = {project["slug"]:project for project in projects}

    @app.route("/")
    def home():
        return render_template("home.html", projects = projects)

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    @app.route("/project/<string:slug>")
    def project(slug):
        if slug not in slug_to_project:
            abort(404)
        return render_template(
            f"project_{slug}.html",
            project = slug_to_project[slug]
        )
    # create a custom 404 page
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

    return app