After I creating a folder and a virtual environment(venv), I install
command(pip install Django) inside the virtual environment. 

Then I start up the project with the command (django-admin startproject nom_du_projet . )

After that I enter into the project folder and I run the server on manage.py
to see if the steps above worked with the: 
commmand ( python3 manage.py runserver )

Once the server is working, I can start an application by using the 
command ( python3 manage.py startapp name of application )

Once the application is created and running, I create a class in (models.py) which will structure 
our database and we will be able to modify in the administration page which I will create after.

Next comes the migration system, migration allows us the applies the changes which were done within 
the database, the command is (python3 manage.py makemigrations)

I have to use this command everytime I apply changes within the database and if it keeps saying 
(No changes detected) that means that I have not register my application within the (settings.py). 

To register my application in (settings.py)I have to look for a list called (INSTALLED-APPS).
Once I have found the list (INSTALLED-APPS) I add my application in the list which is define in the 
folder (apps.py), so the item added to the list will be something like this: 
('name_of_application.apps.name_of_applicationConfig',) after this then we apply the changes 
done with the command(python3 manage.py migrate) and the changes should now be detected.

Once am done migrating, I have to create the administration interface. To create the administration 
interface, firstly I need a superuser who is the main administrator of the administration interface.
The commands is (python3 manage.py createsuperuser), after the user is created we import the module created 
in the (models.py) which was created in the file (admin.py). 

Exemple : 

from . models import nom_de_la_classe 

admin.site.register(nom_de_la_classe)

When the superuser is created and the admin interfaces is done then I can directly add elements or modify 
them in my database from the administration interface.

(Personalization of the Administration Interface)
To show the names of the items in the database, I can create a function in the (models.py).

Exemple: 
    
    def __str__(self): 
        return self.nom  

And if I want show the names of items within the our database, I create a class in the (admin.py)

Exemple:  

class nom_de_la_classe(admin.ModelAdmin):   
    list_displays = ("nom", "prenom")
    search_fields = ["nom"]

admin.site.register(nom_de_la_classe(models.py), nom_de_la_classe(admin.py))

[list_displays] = This allows us to put in order the elements in our database within the administration 
interface. 

Exemple: 

If in the database, I have a list of people with their first names, last names and date of birth.
With [list_displays] I can order them like this:

(first name, last name and date of birth)

or

(last names, first names and date of birth)

or 

(date of birth, first name and last name)

[search_fields] = This allows you to register an item in the search bar . 

Exemple: 

In the case of the example above, I search for the first name or last name.









 


















