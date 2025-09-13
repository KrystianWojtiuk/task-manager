# task-manager

#### A Django web application for managing tasks assigned to different workers across the company, with support for projects, deadlines, priorities, and completion tracking.

👉 [TRY IT LIVE](https://task-manager-49l5.onrender.com)

### ✨ Features
- Create, update, and delete projects and tasks
- Deadlines validation (must be at least 1 day from now for incomplete items)
- Assign tasks to multiple users
- Project/task filtering and search with DataTables
- Responsive forms styled with Crispy Forms

### 🛠️ Tech Stack
- **Backend**: Django, SQLite
- **Frontend**: Bootstrap, DataTables, Crispy Forms
- **Auth**: Django built-in authentication


### 🚀 Getting Started
```bash
# Clone repository
git clone https://github.com/yourusername/your-repo.git
cd your-repo

# Create virtual environment
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver
```
Then open: http://127.0.0.1:8000
