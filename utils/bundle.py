from flask_assets import Environment, Bundle
from app import app

bundles = {
   'base_css': Bundle (
       'vendor/bootstrap/bootstrap.min.css',
       output='gen/base.css'),
   'base_js': Bundle (
       'vendor/popper.js/popper.min.js',
       'vendor/bootstrap/bootstrap.min.js',
       output='gen/base.js')
}

assets = Environment(app)
assets.register(bundles)
