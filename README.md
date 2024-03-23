# petrit_todo_app-.
 
Petrit Kukaj
Petrit.kukaj@student.kyh.se

Inlämning av Projekt: Databas för To-Do-anteckningar
Projektbeskrivning
Projektet är en webbapplikation för att hantera To-Do-listor. Användare kan skapa nya uppgifter, markera dem som färdiga och ta bort dem från listan.
Teknisk Stack
•	Python: Backend-språk för att hantera logik och datahantering.
•	Flask: Webbapplikationsramverk för att bygga och köra webbapplikationer.
•	SQLite: Inbyggd databas för att lagra To-Do-listorna.
•	HTML/CSS: Frontend-gränssnitt för att interagera med användaren.
•	Docker: För att containerisera applikationen och hantera dess beroenden.
Projektgenomförande
Steg 1: Projektsetup
1.	Skapade en ny mapp för projektet.
2.	Skapade en virtuell miljö för Python.
Steg 2: Flask App Setup
1.	Skapade en Flask-app med hjälp av flask-modulen.
2.	Konfigurerade Flask-appen och lade till nödvändiga inställningar i app.py.
Steg 3: Databasdesign
1.	Skapade en SQLite-databas för att lagra To-Do-listornas uppgifter.
2.	Designade tabeller för att lagra användarinformation och uppgifter.
Steg 4: Implementering av funktionalitet
1.	Skapade routar för att hantera CRUD-operationer (Skapa, Läsa, Uppdatera, Ta bort) i app.py.
2.	Implementerade logik för att interagera med databasen och utföra operationer.
Steg 5: Dockerisering av applikationen
1.	Skapade en Dockerfile för att bygga en Docker-image av Flask-applikationen.
2.	Byggde Docker-bilden lokalt med docker build -t todo-app ..
3.	Körde Docker-containern med docker run -p 5000:5000 todo-app för att testa applikationen.
Steg 6: GitHub-uppladdning
1.	Skapade ett nytt GitHub-repository för att lagra projektet.
2.	Laddade upp alla projektfiler och dokumentation till GitHub-repositoryt.
Steg 7: Ladda upp till DockerHub
1.	Loggade in på DockerHub med docker login.
2.	Taggade Docker-bilden med min DockerHub-användarnamn och repositories namn: docker tag todo-app <DockerHub-användarnamn>/<repositories namn>.
3.	Pushade Docker-bilden till DockerHub: docker push <DockerHub-användarnamn>/<repositories namn>.
Sammafattning
Projektet uppfyller alla krav från dagens material. Genom att använda Python, Flask och Docker har jag lyckats skapa en funktionell webbapplikation för att hantera To-Do-listor. Genom att ladda upp projektets källkod till GitHub och Docker-bilden till DockerHub, har jag säkerställt att projektet är tillgängligt för granskning och användning. Jag är nöjd med resultatet och ser fram emot att fortsätta utforska dessa teknologier.

