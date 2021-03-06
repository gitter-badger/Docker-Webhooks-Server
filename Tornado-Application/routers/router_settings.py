# Import os libraries
import os

# router_settings.py is responsible for setting up the tornado web applications, such as enabling cookies,
# security features, and paths for our static and template files

settings = {
    # static path is set to a folde rnamed static
    "static_path": os.path.join(os.path.dirname(__file__), "static"),

    # template path is set to a folder named templates
    "template_path": os.path.join(os.path.dirname(__file__), "templates")
}