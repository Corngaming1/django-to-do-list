# 📝 To-Do List App  
A simple and interactive To-Do List application built using **Django** for the backend and **Tailwind CSS + JavaScript** for the frontend.  

## 🌟 Features  
- ✅ Add, Edit, and Delete tasks  
- ✅ Mark tasks as complete  
- ✅ Categorize tasks (Work, Personal, Other)  
- ✅ Dark Mode Support 🌙  
- ✅ Local Storage to retain tasks  

🚀 Installation & Setup

1️⃣ Clone the Repository
Run this command to download the project from GitHub:

```bash
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
```

2️⃣ Navigate into the Project Directory
Move into the downloaded project folder:
```bash
cd "to-do-list-pt2"
```

3️⃣ Create a Virtual Environment
Set up a virtual environment to manage dependencies:

Windows
```bash
python -m venv venv
```

macOS/Linux
```bash
python3 -m venv venv
```
4️⃣ Activate the Virtual Environment
Windows
```bash
venv\Scripts\activate
```
macOS/Linux
```bash
source venv/bin/activate
```

5️⃣ Install Dependencies
Install the required Python packages:

Important: In order to install the requirements you must be in the backend use this command to do so: cd "djago-to-do/backend" (if you are already in to-do-list pt2 directory)

```bash
pip install -r requirements.txt
```
6️⃣ Apply Migrations
Set up the database schema:
```bash
python manage.py migrate
```

7️⃣ Start the Django Server
Run the development server:

!note: in order to run the server you must be in the backend use this command to do so: cd "djago-to-do/backend" (if you are already in to-do-list pt2 directory)

```bash
python manage.py runserver
```
Now, open 127.0.0.1:8000 in your browser.

📜 License
This project is open-source under the MIT License.



