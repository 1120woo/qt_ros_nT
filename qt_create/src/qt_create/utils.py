##############################################################################
# Utilities
##############################################################################

def author_name():
    """
    Utility to compute logged in user name
    
    :returns: name of current user, ``str``
    """
    import getpass
    name = getpass.getuser()
    try:
        import pwd
        login = name
        name = pwd.getpwnam(login).pw_name
        name = ''.join(name.split(',')) # strip commas
        # in case pwnam is not set
        if not name:
            name = login
    except:
        #pwd failed
        pass
    if type(name) == str:
        name = name.decode('utf-8')
    return name

# Finds and reads one of the templates.
def read_template(tmplf):
    with open(tmplf, 'r') as f:
        t = f.read()
    return t

# This inserts the labelled variables into the template wherever the corresponding
# %package, %brief, %description and %depends is found.
def instantiate_template(template, package, description, author, depends):
    return template.format(package=package, description=description, author=author, depends=depends)
